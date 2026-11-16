# SPDX-License-Identifier: MIT
"""End-to-end offline tests for the JSON export and review template."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / "skills" / "awesome-checklists" / "scripts" / "export_checklists.py"


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.folder = Path(self.tmp.name)

    def run_export(self, *arguments):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--repo-root", str(ROOT), *map(str, arguments)],
            capture_output=True, text=True, check=False,
        )

    def test_full_export_uses_exact_source_inventory(self):
        target = self.folder / "all.json"
        result = self.run_export("--output", target)
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(target.read_text(encoding="utf-8"))
        self.assertEqual(data["count"], 4215)
        self.assertEqual(data["prioritized_count"], 4215)
        self.assertEqual(len({item["id"] for item in data["items"]}), 4215)
        self.assertEqual(sum(item["priority"] is None for item in data["items"]), 0)

    def test_core_selection_and_separate_unverified_review_template(self):
        catalog_path = self.folder / "core.json"
        template_path = self.folder / "review.json"
        result = self.run_export("--only-core", "--output", catalog_path, "--review-template", template_path)
        self.assertEqual(result.returncode, 0, result.stderr)
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        template = json.loads(template_path.read_text(encoding="utf-8"))
        self.assertEqual(catalog["count"], 50)
        self.assertEqual(catalog["prioritized_count"], 50)
        self.assertEqual({r["status"] for r in template["results"]}, {"UNKNOWN"})
        self.assertEqual({r["id"] for r in template["results"]}, {e["id"] for e in catalog["items"]})

    def test_ai_scope_priorities(self):
        target = self.folder / "ai.json"
        result = self.run_export("--scope", "AI", "--output", target)
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(target.read_text(encoding="utf-8"))
        self.assertEqual(data["count"], 1712)
        self.assertEqual(data["prioritized_count"], 1712)
        self.assertTrue(all(item["scope"] == "AI" for item in data["items"]))

    def test_optional_skill_recommendations_have_no_star_based_vetting(self):
        import re
        files = []
        for location in (ROOT / "lists", ROOT / "lists" / "frontend",
                         ROOT / "lists" / "backend", ROOT / "lists" / "AI"):
            files.extend(p for p in location.glob("*.md")
                         if re.fullmatch(r"\d{2}_[A-Za-z0-9_]+\.md", p.name))
        self.assertEqual(len(files), 91)
        for path in files:
            with self.subTest(source=path.relative_to(ROOT)):
                content = path.read_text(encoding="utf-8")
                self.assertNotIn("repo stars", content)
                self.assertIn("review-method.md", content)
                self.assertIn("compliance-crosswalk.md", content)
                self.assertNotIn("## Suggested AI skills for verification", content)
                self.assertNotIn("## Important warning: reference only", content)
                self.assertNotIn("## Review details", content)

    def test_invalid_provenance_ref_rejected(self):
        result = self.run_export("--source-commit", "not-a-sha", "--only-core")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("40-character", result.stderr)


if __name__ == "__main__":
    unittest.main()
