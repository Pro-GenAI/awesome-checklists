# SPDX-License-Identifier: MIT
"""Offline inventory and source-date freshness regression tests."""
import importlib.util
from datetime import date
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / "skills" / "awesome-checklists" / "scripts"
sys.path.insert(0, str(SCRIPTS))

from generate_inventory import generate, verify_readme
from generate_id_prefixes import build as build_prefixes
from check_source_freshness import inspect


class ReviewMetadataTests(unittest.TestCase):
    def test_inventory_manifest_matches_source(self):
        result = generate(ROOT)
        frozen = json.loads((ROOT / "lists/references/inventory.json").read_text(encoding="utf-8"))
        self.assertEqual(result, frozen)
        self.assertEqual(result["total_files"], 91)
        self.assertEqual(result["total_checks"], 4215)
        self.assertEqual(verify_readme(ROOT, result), [])

    def test_prefix_register_covers_all_unique_ids(self):
        generated = build_prefixes(ROOT)
        frozen = json.loads((ROOT / "lists/references/id-prefix-ranges.json").read_text(encoding="utf-8"))
        self.assertEqual(generated, frozen)
        self.assertEqual(generated["total_ids"], 4215)
        self.assertEqual(generated["total_prefixes"], 35)
        self.assertEqual(generated["prefixes"]["AGENT"]["ranges"], [[1, 141]])
        self.assertEqual(generated["prefixes"]["SEC"]["ranges"], [[1, 121]])

    def test_freshness_current_sources_have_valid_dates(self):
        errors, _warnings = inspect(ROOT, today=date(2026, 11, 15), max_age_days=180)
        self.assertEqual(errors, [])

    def test_staleness_warning_and_invalid_date(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for part in ("", "frontend", "backend", "AI"):
                (root / "lists" / part).mkdir(parents=True, exist_ok=True)
            file = root / "lists" / "01_Demo.md"
            file.write_text("# Example\n**Source review date:** 2024-01-01.\n", encoding="utf-8")
            errors, warnings = inspect(root, today=date(2026, 11, 15), max_age_days=180)
            self.assertEqual(errors, [])
            self.assertEqual(len(warnings), 1)
            file.write_text("# Example\n**Source review date:** 2028-01-01.\n", encoding="utf-8")
            errors, _ = inspect(root, today=date(2026, 11, 15))
            self.assertTrue(any("future" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
