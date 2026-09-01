from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DELIVERY_SKILL = ROOT / "skills" / "deliver-ux-requirements"
VALIDATOR_PATH = DELIVERY_SKILL / "scripts" / "validate_requirement_docs.py"
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
            DELIVERY_SKILL / "assets" / "enterprise-requirement-output-template.md"
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


class StageProfileValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.site = validator.Site(Path("synthetic.md"), 1)

    def confirmed_baseline(self):
        analysis = validator.Analysis()
        for stable_id in (
            "BG-001",
            "OBJ-001",
            "ROLE-001",
            "SCN-001",
            "CON-001",
            "REQ-001",
            "TASK-001",
            "US-001",
            "DEC-BASELINE-001",
        ):
            analysis.definitions[stable_id].add(self.site)
        analysis.edges["US-001"].update({"REQ-001", "SCN-001", "TASK-001"})
        analysis.edges["REQ-001"].add("US-001")
        analysis.edges["SCN-001"].add("US-001")
        analysis.edges["TASK-001"].add("US-001")
        analysis.edges["DEC-BASELINE-001"].update(
            {"REQ-001", "TASK-001", "US-001"}
        )
        analysis.edges["REQ-001"].add("DEC-BASELINE-001")
        analysis.baseline_statuses.append(("Confirmed", self.site))
        return analysis

    def findings(self, analysis, profile):
        return validator.semantic_findings(
            analysis,
            final=True,
            profile=profile,
            file_count=1,
        )

    def test_baseline_profile_does_not_require_downstream_artifacts(self) -> None:
        codes = {
            finding.code
            for finding in self.findings(self.confirmed_baseline(), "baseline")
        }

        self.assertNotIn("MISSING_HAPPY_PATH", codes)
        self.assertNotIn("MISSING_FUNCTION_DECOMPOSITION", codes)
        self.assertNotIn("MISSING_REVIEW_HANDOFF", codes)
        self.assertNotIn("MISSING_STAGE_ARTIFACT", codes)

    def test_happy_path_profile_includes_baseline_and_path_contracts(self) -> None:
        findings = self.findings(self.confirmed_baseline(), "happy-path")
        codes = {finding.code for finding in findings}

        self.assertIn("MISSING_HAPPY_PATH", codes)
        self.assertTrue(
            any(
                finding.code == "MISSING_STAGE_ARTIFACT"
                and "happy path" in finding.message
                for finding in findings
            )
        )
        self.assertNotIn("MISSING_REVIEW_HANDOFF", codes)

    def test_delivery_profile_does_not_reopen_baseline_gate(self) -> None:
        codes = {
            finding.code
            for finding in self.findings(self.confirmed_baseline(), "delivery")
        }

        self.assertIn("MISSING_DELIVERY_PROFILE", codes)
        self.assertIn("MISSING_REVIEW_HANDOFF", codes)
        self.assertIn("MISSING_STAGE_ARTIFACT", codes)
        self.assertNotIn("MISSING_BASELINE_CONFIRMATION", codes)
        self.assertNotIn("MISSING_HAPPY_PATH", codes)


class ModelFitValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.site = validator.Site(Path("synthetic.md"), 1)

    def model_fit_analysis(self, *, include_ui: bool = True):
        analysis = validator.Analysis()
        stable_ids = ["ROLE-001", "SCN-001", "FLOW-001", "INT-001"]
        if include_ui:
            stable_ids.extend(["UI-001", "STATE-001"])
        for stable_id in stable_ids:
            analysis.definitions[stable_id].add(self.site)
        flow_ids = {"ROLE-001", "SCN-001", "FLOW-001", "INT-001"}
        analysis.model_fit_coverage.append(
            (
                "Flow-model fit",
                "Reviewed",
                "Domain-owner-confirmed",
                "No material gap found",
                flow_ids,
                self.site,
            )
        )
        if include_ui:
            representation_ids = {
                "ROLE-001",
                "SCN-001",
                "UI-001",
                "STATE-001",
            }
            analysis.model_fit_coverage.append(
                (
                    "Representation-model fit",
                    "Reviewed",
                    "Inferred",
                    "Representative-user validation remains planned",
                    representation_ids,
                    self.site,
                )
            )
        return analysis

    @staticmethod
    def model_fit_findings(analysis):
        return [
            finding
            for finding in validator.semantic_findings(
                analysis, final=True, profile="model-fit"
            )
            if finding.code in validator.STAGE_PROFILE_CODES["model-fit"]
            or finding.code == "MISSING_STAGE_ARTIFACT"
        ]

    def test_review_coverage_does_not_require_a_gap_finding(self) -> None:
        codes = {
            finding.code
            for finding in self.model_fit_findings(self.model_fit_analysis())
        }

        self.assertNotIn("MISSING_MODEL_FIT_COVERAGE", codes)
        self.assertNotIn("MISSING_FLOW_MODEL_FIT_REVIEW", codes)
        self.assertNotIn("MISSING_REPRESENTATION_MODEL_FIT_REVIEW", codes)
        self.assertNotIn("MISSING_STAGE_ARTIFACT", codes)

    def test_ui_scope_requires_representation_review(self) -> None:
        analysis = self.model_fit_analysis()
        analysis.model_fit_coverage = [analysis.model_fit_coverage[0]]

        codes = {
            finding.code for finding in self.model_fit_findings(analysis)
        }

        self.assertIn("MISSING_REPRESENTATION_MODEL_FIT_REVIEW", codes)

    def test_coverage_requires_role_scenario_scope_and_evidence(self) -> None:
        analysis = self.model_fit_analysis(include_ui=False)
        analysis.model_fit_coverage = [
            (
                "Flow-model fit",
                "Reviewed",
                "",
                "",
                {"FLOW-001", "INT-001"},
                self.site,
            )
        ]

        codes = {
            finding.code for finding in self.model_fit_findings(analysis)
        }

        self.assertIn("INCOMPLETE_MODEL_FIT_COVERAGE", codes)
        self.assertIn("ORPHAN_MODEL_FIT_COVERAGE", codes)

    def test_open_critical_gap_is_blocking_but_resolved_gap_is_not(self) -> None:
        analysis = self.model_fit_analysis()
        gap_id = "UXGAP-001"
        analysis.definitions[gap_id].add(self.site)
        for related_id in ("ROLE-001", "SCN-001", "UI-001", "STATE-001"):
            analysis.edges[gap_id].add(related_id)
            analysis.edges[related_id].add(gap_id)
        analysis.uxgap_records[gap_id].append(("Critical", "Open", self.site))

        codes = {
            finding.code for finding in self.model_fit_findings(analysis)
        }
        self.assertIn("OPEN_CRITICAL_UXGAP", codes)

        analysis.uxgap_records[gap_id] = [("Critical", "Resolved", self.site)]
        codes = {
            finding.code for finding in self.model_fit_findings(analysis)
        }
        self.assertNotIn("OPEN_CRITICAL_UXGAP", codes)

    def test_confirmed_ascii_cannot_hide_an_open_critical_gap(self) -> None:
        analysis = self.model_fit_analysis()
        gap_id = "UXGAP-001"
        decision_id = "DEC-ASCII-001"
        analysis.definitions[gap_id].add(self.site)
        analysis.definitions[decision_id].add(self.site)
        for related_id in ("ROLE-001", "SCN-001", "UI-001"):
            analysis.edges[gap_id].add(related_id)
            analysis.edges[related_id].add(gap_id)
        analysis.edges["UI-001"].add(decision_id)
        analysis.edges[decision_id].add("UI-001")
        analysis.ascii_confirmation_statuses[decision_id].append(
            ("Confirmed", self.site)
        )
        analysis.uxgap_records[gap_id].append(("Critical", "Open", self.site))

        codes = {
            finding.code for finding in self.model_fit_findings(analysis)
        }

        self.assertIn("CONFIRMED_ASCII_WITH_OPEN_CRITICAL_UXGAP", codes)

    def test_parser_collects_model_fit_coverage_and_gap_details(self) -> None:
        markdown = """\
| Model-fit review coverage | Target user/scenario | Reviewed FLOW/INT/UI/STATE | Evidence status | Result | Rationale/limitation |
| --- | --- | --- | --- | --- | --- |
| Flow-model fit | ROLE-001 · SCN-001 | FLOW-001 · INT-001 | Inferred | Reviewed with findings | User testing planned |

| Target user/scenario | Flow or interface point | Severity | Evidence | Resolution/status | Related IDs | UXGAP ID |
| --- | --- | --- | --- | --- | --- | --- |
| ROLE-001 · SCN-001 | FLOW-001 · INT-001 | Critical | Owner-confirmed | Open | UI-001 | UXGAP-001 |
"""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "requirements.md"
            path.write_text(markdown, encoding="utf-8")
            analysis = validator.inspect_file(path, final=True)

        self.assertEqual(len(analysis.model_fit_coverage), 1)
        self.assertEqual(analysis.model_fit_coverage[0][0:3], (
            "Flow-model fit",
            "Reviewed with findings",
            "Inferred",
        ))
        self.assertEqual(
            analysis.uxgap_records["UXGAP-001"][0][0:2],
            ("Critical", "Open"),
        )
        self.assertIn("ROLE-001", analysis.edges["UXGAP-001"])
        self.assertIn("UI-001", analysis.edges["UXGAP-001"])

    def test_audit_only_document_passes_model_fit_profile_without_baseline(self) -> None:
        markdown = """\
| Target role | ROLE ID |
| --- | --- |
| Occasional requester | ROLE-001 |

| Target scenario | SCN ID |
| --- | --- |
| Submit and verify a request | SCN-001 |

| Task flow | Related IDs | FLOW ID |
| --- | --- | --- |
| Submit request | ROLE-001 · SCN-001 · INT-001 | FLOW-001 |

| Interaction | Related IDs | INT ID |
| --- | --- | --- |
| Review consequence and submit | ROLE-001 · SCN-001 · FLOW-001 | INT-001 |

| Model-fit review coverage | Target user/scenario | Reviewed FLOW/INT/UI/STATE | Evidence status | Result | Rationale/limitation |
| --- | --- | --- | --- | --- | --- |
| Flow-model fit | ROLE-001 · SCN-001 | FLOW-001 · INT-001 | Domain-owner-confirmed | Reviewed | Representation review is outside the supplied scope |
"""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "audit.md"
            path.write_text(markdown, encoding="utf-8")
            analysis = validator.inspect_file(path, final=True)
            findings = validator.semantic_findings(
                analysis,
                final=True,
                profile="model-fit",
                file_count=1,
            )

        self.assertEqual(findings, [])

    def test_enterprise_template_reviews_flow_before_ascii_confirmation(self) -> None:
        content = (
            DELIVERY_SKILL / "assets" / "enterprise-requirement-output-template.md"
        ).read_text(encoding="utf-8")

        model_fit_position = content.index("### 7.2 Target-user model-fit review")
        queue_position = content.index("### 8.1 ASCII UX confirmation queue")

        self.assertLess(model_fit_position, queue_position)


if __name__ == "__main__":
    unittest.main()
