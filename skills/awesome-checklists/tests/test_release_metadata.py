"""Release metadata consistency and current documentation tests."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "skills/awesome-checklists/scripts"))
from validate_release_metadata import inspect, check_prefix_table, verify_pin_ancestry


class ReleaseMetadataTests(unittest.TestCase):
    def test_live_metadata_matches_current_entry_points(self):
        self.assertEqual(inspect(ROOT, "false"), [])

    def test_public_docs_cannot_claim_private_repository(self):
        errors = inspect(ROOT, "true")
        self.assertTrue(any("private flag" in e for e in errors), errors)

    def test_scope_domain_tables_match_generated_prefix_register(self):
        content = (ROOT / "docs/agents/scope-inventory.md").read_text(encoding="utf-8")
        register = json.loads((ROOT / "lists/references/id-prefix-ranges.json").read_text(encoding="utf-8"))
        self.assertEqual(check_prefix_table(content, register["prefixes"]), [])

    def test_stale_sec_scope_count_is_detected(self):
        content = (ROOT / "docs/agents/scope-inventory.md").read_text(encoding="utf-8")
        register = json.loads((ROOT / "lists/references/id-prefix-ranges.json").read_text(encoding="utf-8"))
        self.assertIn("`SEC` | 121 |", content)
        stale = content.replace("`SEC` | 121 |", "`SEC` | 117 |", 1)
        errors = check_prefix_table(stale, register["prefixes"])
        self.assertTrue(any("SEC" in error and "117" in error for error in errors), errors)

    def test_cc0_text_mit_code_and_scoped_ci(self):
        content_license = (ROOT / "LICENSE").read_text(encoding="utf-8")
        code_license = (ROOT / "LICENSE-CODE").read_text(encoding="utf-8")
        self.assertTrue(content_license.startswith("CC0 1.0 Universal"))
        self.assertIn("Statement of Purpose", content_license)
        self.assertTrue(code_license.startswith("MIT License"))
        self.assertIn("Copyright (c) 2026 Pro-GenAI", code_license)
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("[CC0 1.0 Universal](LICENSE)", readme)
        self.assertIn("[MIT License](LICENSE-CODE)", readme)
        folder = ROOT / ".github/workflows"
        active = sorted(f.name for f in folder.glob("*.yml"))
        self.assertEqual(active, ["link-health.yml", "quality-gates.yml"])
        self.assertTrue((folder / "website.yml.disabled").is_file())
        self.assertTrue((folder / "checklist-lint.yml.disabled").is_file())

    @unittest.skipUnless(shutil.which("git"), "Git CLI unavailable")
    def test_local_main_pin_ancestry_and_missing_pin(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            def git(*args):
                return subprocess.run(["git", "-C", str(root), *args],
                                      capture_output=True, text=True, check=True).stdout.strip()
            git("init", "-q", "-b", "main")
            git("config", "user.email", "test@example.invalid")
            git("config", "user.name", "Test")
            (root / "fixture.txt").write_text("one", encoding="utf-8")
            git("add", "fixture.txt")
            git("commit", "-qm", "first")
            first = git("rev-parse", "HEAD")
            release = root / "skills/awesome-checklists/references/source-release.json"
            release.parent.mkdir(parents=True)
            release.write_text(json.dumps({"checklist_source_sha": first}), encoding="utf-8")
            (root / "fixture.txt").write_text("two", encoding="utf-8")
            git("commit", "-qam", "second")
            self.assertEqual(verify_pin_ancestry(root), [])
            self.assertTrue(any("unavailable" in e
                                for e in verify_pin_ancestry(root, "absent")))
            release.write_text(json.dumps({"checklist_source_sha": "f" * 40}), encoding="utf-8")
            self.assertTrue(any("missing" in e for e in verify_pin_ancestry(root)))

    def test_compact_agent_entry_has_functional_pointers(self):
        content = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertLess(len(content), 6000)
        for path in (
            "docs/agents/resources-and-tooling.md",
            "docs/agents/scope-inventory.md",
            "docs/agents/contributor-workflows.md",
        ):
            self.assertIn(path, content)
            self.assertTrue((ROOT / path).is_file())


if __name__ == "__main__":
    unittest.main()
