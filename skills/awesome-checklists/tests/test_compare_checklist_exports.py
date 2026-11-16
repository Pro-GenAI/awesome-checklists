# SPDX-License-Identifier: MIT
"""Offline tests for downstream checklist-source drift reports."""
from pathlib import Path
import json
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from compare_checklist_exports import compare, load_catalog, markdown  # noqa: E402


def catalog(*items, scope="all", sha="a" * 40):
    return {
        "schema_version": 1, "scope": scope,
        "source_commit": sha,
        "count": len(items), "items": list(items),
    }


def item(identifier="SEC-001", criterion="Original", priority="P1",
         scope="shared", source="lists/05_Security.md", section="Security"):
    return {
        "id": identifier, "criterion_markdown": criterion, "priority": priority,
        "scope": scope, "source": source, "section": section,
    }


class CompareExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.dir = Path(self.temp.name)

    def write(self, name, obj):
        path = self.dir / name
        path.write_text(json.dumps(obj), encoding="utf-8")
        return path

    def test_no_change_requires_no_review(self):
        before = load_catalog(self.write("a.json", catalog(item())))
        after = load_catalog(self.write("b.json", catalog(item(), sha="b" * 40)))
        report = compare(before, after)
        self.assertEqual(report["summary"]["needs_review"], 0)
        self.assertIn("None", markdown(report))

    def test_changed_criterion_tier_and_owner_require_review(self):
        before = load_catalog(self.write("a.json", catalog(item())))
        after = load_catalog(self.write("b.json", catalog(
            item(criterion="Updated", priority="P0", scope="backend",
                 source="lists/backend/09_Security.md")
        )))
        report = compare(before, after)
        self.assertEqual(report["summary"]["needs_review"], 1)
        self.assertEqual(set(report["changed"][0]["changed_fields"]),
                         {"criterion_markdown", "priority", "scope", "source"})

    def test_added_removed_are_reported(self):
        before = load_catalog(self.write("a.json", catalog(item("SEC-001"))))
        after = load_catalog(self.write("b.json", catalog(item("SEC-002"))))
        summary = compare(before, after)["summary"]
        self.assertEqual((summary["added"], summary["removed"], summary["needs_review"]),
                         (1, 1, 2))

    def test_section_only_change_is_non_blocking(self):
        before = load_catalog(self.write("a.json", catalog(item(section="First"))))
        after = load_catalog(self.write("b.json", catalog(item(section="Second"))))
        self.assertFalse(compare(before, after)["changed"][0]["review_needed"])

    def test_duplicates_and_mixed_scopes_rejected(self):
        duplicate = self.write("duplicate.json", catalog(item(), item()))
        with self.assertRaisesRegex(ValueError, "duplicate"):
            load_catalog(duplicate)
        one = load_catalog(self.write("one.json", catalog(item(), scope="all")))
        two = load_catalog(self.write("two.json", catalog(item(), scope="shared")))
        with self.assertRaisesRegex(ValueError, "Export scopes differ"):
            compare(one, two)

    def test_cli_exit_two_on_actionable_diff(self):
        before = self.write("a.json", catalog(item()))
        after = self.write("b.json", catalog(item(criterion="New")))
        command = [sys.executable, str(SCRIPTS / "compare_checklist_exports.py"),
                   "--before", str(before), "--after", str(after),
                   "--fail-on-review-needed", "--format", "json"]
        run = subprocess.run(command, capture_output=True, text=True, check=False)
        self.assertEqual(run.returncode, 2, run.stderr)
        self.assertEqual(json.loads(run.stdout)["summary"]["needs_review"], 1)


if __name__ == "__main__":
    unittest.main()
