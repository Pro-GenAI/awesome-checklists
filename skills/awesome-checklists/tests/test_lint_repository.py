# SPDX-License-Identifier: MIT
"""Targeted offline tests for repository Markdown link and format lint."""
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("lint_repository", SCRIPTS / "lint_repository.py")
linter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(linter)


class LintTests(unittest.TestCase):
    def test_local_links_and_missing_target(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "doc.md").write_text("# Title\n", encoding="utf-8")
            self.assertIsNone(linter.check_link(root, root / "doc.md", "#title"))
            self.assertIsNone(linter.check_link(root, root / "doc.md", "doc.md#title"))
            self.assertIsNotNone(linter.check_link(root, root / "doc.md", "missing.md"))
            self.assertIsNone(linter.check_link(root, root / "doc.md", "https://example.org/resource"))

    def test_markdown_sections_and_duplicates(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            doc = root / "source.md"
            doc.write_text(
                "# Title\n## API Checks\n## API Checks\n"
                "## Display the “Reviewed with awesome-checklists” badge\n",
                encoding="utf-8",
            )
            self.assertIsNone(linter.check_link(root, doc, "#api-checks"))
            self.assertIsNone(linter.check_link(root, doc, "source.md#api-checks-1"))
            self.assertIsNone(linter.check_link(
                root, doc, "#display-the-reviewed-with-awesome-checklists-badge"
            ))
            self.assertIsNotNone(linter.check_link(root, doc, "#does-not-exist"))
            self.assertIsNone(linter.check_link(root, doc, "source.md#L10"))

    def test_required_checklist_section_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "lists" / "01_Test.md"
            source.parent.mkdir(parents=True)
            good = (
                "# Checklist\n## Checks\n## Release gate\n"
                "## Trusted references and scope\n\n**Source review date:** 2026-11-15.\n"
            )
            self.assertEqual(linter.source_structure(source, good, root), [])
            problems = linter.source_structure(
                source,
                good.replace("## Release gate", "## Release checklist"),
                root,
            )
            self.assertTrue(any("Release gate" in x for x in problems), problems)
            self.assertTrue(any("source review" in x for x in linter.source_structure(
                source, good.replace("2026-11-15", "not-a-date"), root
            )))
            self.assertTrue(any("last nonblank line" in x for x in linter.source_structure(
                source, good + "\n- [Example](https://example.org)\n", root
            )))
            self.assertEqual(linter.source_structure(source, good + "\n\n", root), [])

    def test_code_fences_are_not_parsed_as_links(self):
        source = "# Title\n[good](doc.md)\n```markdown\n[bad](not-a-file.md)\n```\n"
        self.assertEqual(linter.extract_links(source), ["doc.md"])

    def test_inline_code_examples_are_not_live_links(self):
        document = (
            "# Example\n"
            "`[documentation sample](../not-a-real-target.md)`\n"
            "[real link](doc.md)\n"
            "``[example](also-not-real.md)``\n"
            "[link with `inline code` label](other.md)\n"
            "~~~markdown\n[ignored](fenced.md)\n~~~\n"
        )
        self.assertEqual(linter.extract_links(document), ["doc.md", "other.md"])

    def test_development_matches_agent_registry_and_readme_leaves_process_to_contributing(self):
        root = Path(__file__).resolve().parents[3]
        readme = (root / "README.md").read_text(encoding="utf-8")
        development = (root / "docs/DEVELOPMENT.md").read_text(encoding="utf-8")
        prefixes = json.loads(
            (root / "lists/references/id-prefix-ranges.json").read_text(encoding="utf-8")
        )
        agent_count = prefixes["prefixes"]["AGENT"]["count"]
        self.assertIn(f"check all {agent_count} IDs and section links", development)
        self.assertNotIn(f"check all {agent_count} IDs and section links", readme)
        self.assertIn("[DEVELOPMENT.md](docs/DEVELOPMENT.md)", readme)
        self.assertIn("[CONTRIBUTING.md](docs/CONTRIBUTING.md)", readme)
        self.assertNotIn("No pull request is required.", readme)
        self.assertNotIn("commit directly to `main`", readme)

    def test_security_registry_records_all_live_ids(self):
        root = Path(__file__).resolve().parents[3]
        errors, _ = linter.lint(root)
        self.assertEqual(errors, [], "\n".join(errors[:20]))


if __name__ == "__main__":
    unittest.main()
