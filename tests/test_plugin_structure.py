from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
EXPECTED_SKILLS = {
    "shape-ux-requirements",
    "shape-requirement-baseline",
    "shape-happy-paths",
    "shape-ascii-interactions",
    "deliver-ux-requirements",
}


class PluginStructureTests(unittest.TestCase):
    def test_manifest_packages_the_skill_directory(self) -> None:
        manifest = json.loads(
            (ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8")
        )

        self.assertEqual(manifest["name"], "shape-ux-requirements")
        self.assertEqual(manifest["skills"], "./skills/")

    def test_expected_specialists_are_discoverable(self) -> None:
        discovered = {
            path.parent.name for path in SKILLS_ROOT.glob("*/SKILL.md")
        }

        self.assertEqual(discovered, EXPECTED_SKILLS)

    def test_skill_folder_matches_frontmatter_name(self) -> None:
        for skill_file in SKILLS_ROOT.glob("*/SKILL.md"):
            with self.subTest(skill=skill_file.parent.name):
                text = skill_file.read_text(encoding="utf-8")
                match = re.search(r"^name:\s*([^\n]+)$", text, re.MULTILINE)
                self.assertIsNotNone(match)
                self.assertEqual(match.group(1).strip(), skill_file.parent.name)

    def test_skill_markdown_links_resolve(self) -> None:
        for skill_file in SKILLS_ROOT.glob("*/SKILL.md"):
            text = skill_file.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^]]+]\(([^)#]+)", text):
                if "://" in target:
                    continue
                with self.subTest(skill=skill_file.parent.name, target=target):
                    self.assertTrue((skill_file.parent / target).exists())

    def test_root_compatibility_entrypoint_routes_to_all_specialists(self) -> None:
        compatibility = (ROOT / "SKILL.md").read_text(encoding="utf-8")

        for skill_name in EXPECTED_SKILLS:
            self.assertIn(f"skills/{skill_name}/SKILL.md", compatibility)


if __name__ == "__main__":
    unittest.main()
