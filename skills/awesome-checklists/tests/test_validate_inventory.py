"""Offline tests for checklist inventory validation."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_inventory.py"
spec = importlib.util.spec_from_file_location("validate_inventory", SCRIPT)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.folder = self.root / "lists"
        self.folder.mkdir()
        (self.folder / "01_Test.md").write_text("## Checks\n- [ ] **TST-001** `P1` Test\n", encoding="utf-8")

    def test_valid_inventory(self):
        totals, errors = validator.validate(self.root, {"shared": (1, 1)})
        self.assertEqual(totals["shared"], 1)
        self.assertEqual(errors, [])

    def test_detect_duplicate_prefix_checked_and_stable_id(self):
        (self.folder / "01_Other.md").write_text("## Checks\n- [x] **TST-001** `P1` Duplicate\n", encoding="utf-8")
        _, errors = validator.validate(self.root, {"shared": (2, 2)})
        message = "\n".join(errors)
        for word in ("duplicate filename numeric prefixes", "duplicate TST-001", "unchecked"):
            self.assertIn(word, message)

    def test_noncontiguous_filenames_can_preserve_existing_links(self):
        first = (self.folder / "01_Test.md").read_text(encoding="utf-8")
        (self.folder / "03_Other.md").write_text(
            first.replace("TST-001", "TST-002"), encoding="utf-8"
        )
        totals, errors = validator.validate(self.root, {"shared": (2, 2)})
        self.assertEqual(totals["shared"], 2)
        self.assertEqual(errors, [])

    def test_missing_id_and_wrong_counts(self):
        (self.folder / "01_Test.md").write_text("## Checks\n- [ ] No identifier\n", encoding="utf-8")
        _, errors = validator.validate(self.root, {"shared": (1, 1)})
        message = "\n".join(errors)
        self.assertIn("stable ID", message)
        self.assertIn("expected 1 checks", message)


if __name__ == "__main__":
    unittest.main()
