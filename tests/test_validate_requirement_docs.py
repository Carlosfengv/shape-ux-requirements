from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "scripts" / "validate_requirement_docs.py"
SPEC = importlib.util.spec_from_file_location("requirement_validator_tested", VALIDATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


class HappyPathValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.site = validator.Site(Path("synthetic.md"), 1)

    def add_happy_path(
        self,
        analysis,
        suffix: str,
        *,
        confirmation_status: str = "Confirmed",
        include_basis: bool = True,
        include_adversarial: bool = True,
    ) -> str:
        path_id = f"FLOW-HP-{suffix}"
        scenario_id = f"SCN-{suffix}"
        story_id = f"US-{suffix}"
        decision_id = f"DEC-HAPPY-{suffix}"
        for stable_id in (path_id, scenario_id, story_id, decision_id):
            analysis.definitions[stable_id].add(self.site)
        for neighbor in (scenario_id, story_id, decision_id):
            analysis.edges[path_id].add(neighbor)
            analysis.edges[neighbor].add(path_id)
        if include_basis:
            analysis.happy_path_basis_ids[path_id].add(self.site)
        if include_adversarial:
            analysis.happy_path_adversarial_ids[path_id].add(self.site)
        analysis.happy_path_confirmation_statuses[decision_id].append(
            (confirmation_status, self.site)
        )
        return path_id

    @staticmethod
    def happy_findings(analysis):
        return [
            finding
            for finding in validator.semantic_findings(
                analysis, final=True, profile="full"
            )
            if "HAPPY_PATH" in finding.code
        ]

    def test_each_path_requires_its_own_basis_and_adversarial_review(self) -> None:
        analysis = validator.Analysis()
        self.add_happy_path(analysis, "001")
        missing_path = self.add_happy_path(
            analysis,
            "002",
            include_basis=False,
            include_adversarial=False,
        )

        findings = self.happy_findings(analysis)
        messages = {finding.code: finding.message for finding in findings}

        self.assertIn("MISSING_HAPPY_PATH_BASIS", messages)
        self.assertIn(missing_path, messages["MISSING_HAPPY_PATH_BASIS"])
        self.assertIn("MISSING_HAPPY_PATH_ADVERSARIAL_REVIEW", messages)
        self.assertIn(
            missing_path, messages["MISSING_HAPPY_PATH_ADVERSARIAL_REVIEW"]
        )

    def test_pending_decision_does_not_confirm_happy_path(self) -> None:
        analysis = validator.Analysis()
        path_id = self.add_happy_path(
            analysis, "001", confirmation_status="Pending"
        )

        findings = self.happy_findings(analysis)

        self.assertTrue(
            any(
                finding.code == "UNCONFIRMED_HAPPY_PATH"
                and path_id in finding.message
                for finding in findings
            )
        )

    def test_blocked_coverage_with_rationale_waives_happy_path(self) -> None:
        analysis = validator.Analysis()
        analysis.happy_path_coverage.append(
            ("Blocked", "Q-001 must be decided by the product owner", self.site)
        )

        codes = {finding.code for finding in self.happy_findings(analysis)}

        self.assertNotIn("MISSING_HAPPY_PATH", codes)
        self.assertNotIn("MISSING_HAPPY_PATH_WAIVER_RATIONALE", codes)

    def test_waiver_without_rationale_is_rejected(self) -> None:
        analysis = validator.Analysis()
        analysis.happy_path_coverage.append(("Not applicable", "", self.site))

        codes = {finding.code for finding in self.happy_findings(analysis)}

        self.assertIn("MISSING_HAPPY_PATH_WAIVER_RATIONALE", codes)

    def test_parser_links_rows_and_collects_confirmation_status(self) -> None:
        markdown = """\
| Happy Path coverage | Status | Rationale |
| --- | --- | --- |
| Primary paths | Confirmed | Reviewed with product owner |

| Fundamental user outcome | Observable completion evidence | Related IDs |
| --- | --- | --- |
| Outcome | Result visible | FLOW-HP-001 |

| Challenge | Path impact | Related IDs |
| --- | --- | --- |
| Hidden permission | Preconditions updated | FLOW-HP-001 |

| Decision | Covered IDs | Status | DEC ID |
| --- | --- | --- | --- |
| Confirm path | FLOW-HP-001 | Pending | DEC-HAPPY-001 |
"""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "requirements.md"
            path.write_text(markdown, encoding="utf-8")
            analysis = validator.inspect_file(path, final=True)

        self.assertIn("FLOW-HP-001", analysis.happy_path_basis_ids)
        self.assertIn("FLOW-HP-001", analysis.happy_path_adversarial_ids)
        self.assertEqual(
            analysis.happy_path_confirmation_statuses["DEC-HAPPY-001"][0][0],
            "Pending",
        )
        self.assertEqual(
            analysis.happy_path_coverage[0][0:2],
            ("Confirmed", "Reviewed with product owner"),
        )

    def test_reference_status_cannot_confirm_a_pending_decision(self) -> None:
        markdown = """\
| Happy path | Related IDs | Status | FLOW ID |
| --- | --- | --- | --- |
| Primary path | DEC-HAPPY-001 | Confirmed | FLOW-HP-001 |

| Decision | Covered IDs | Status | DEC ID |
| --- | --- | --- | --- |
| Confirm path | FLOW-HP-001 | Pending | DEC-HAPPY-001 |
"""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "requirements.md"
            path.write_text(markdown, encoding="utf-8")
            analysis = validator.inspect_file(path, final=True)

        self.assertEqual(
            [
                status
                for status, _site in analysis.happy_path_confirmation_statuses[
                    "DEC-HAPPY-001"
                ]
            ],
            ["Pending"],
        )

    def test_empty_rows_do_not_satisfy_path_analysis(self) -> None:
        markdown = """\
| Fundamental user outcome | Observable completion evidence | Related IDs |
| --- | --- | --- |
| | | FLOW-HP-001 |

| Challenge | Path impact | Related IDs |
| --- | --- | --- |
| | | FLOW-HP-001 |
"""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "requirements.md"
            path.write_text(markdown, encoding="utf-8")
            analysis = validator.inspect_file(path, final=True)

        self.assertNotIn("FLOW-HP-001", analysis.happy_path_basis_ids)
        self.assertNotIn("FLOW-HP-001", analysis.happy_path_adversarial_ids)

    def test_new_happy_path_placeholders_are_detected(self) -> None:
        placeholders = (
            "[Happy path name]",
            "[DEC-HAPPY reference]",
            "[related baseline IDs]",
            "[FLOW references]",
            "[SCN/REQ/TASK/US/JS references]",
        )

        for placeholder in placeholders:
            with self.subTest(placeholder=placeholder):
                self.assertIsNotNone(
                    validator.LOCALIZED_PLACEHOLDER_RE.search(placeholder)
                )

    def test_enterprise_template_confirms_path_before_deriving_functions(self) -> None:
        content = (
            ROOT / "assets" / "enterprise-requirement-output-template.md"
        ).read_text(encoding="utf-8")

        happy_path_position = content.index("### 6.3 Confirmed Happy Paths")
        function_position = content.index(
            "### 6.4 Story-to-functional-point decomposition"
        )
        surface_position = content.index(
            "### 6.5 Starting surface and experience topology"
        )

        self.assertLess(happy_path_position, function_position)
        self.assertLess(function_position, surface_position)


if __name__ == "__main__":
    unittest.main()
