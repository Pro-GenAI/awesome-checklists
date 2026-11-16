# SPDX-License-Identifier: MIT
"""Regression coverage: stable IDs must stay contiguous across scopes."""
from pathlib import Path
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from generate_id_prefixes import build  # noqa: E402


class StableIdContinuityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, relative: str, *identifiers: str) -> None:
        target = self.root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            "".join(f"- [ ] **{identifier}** `P1` Example criterion.\n" for identifier in identifiers),
            encoding="utf-8",
        )

    def test_contiguous_ids_can_be_owned_by_different_scopes(self) -> None:
        self.write("lists/AI/11_Agents.md", "AGENT-001")
        self.write("lists/backend/17_Agents.md", "AGENT-002")
        inventory = build(self.root)
        self.assertEqual(inventory["prefixes"]["AGENT"]["ranges"], [[1, 2]])
        self.assertEqual(inventory["total_ids"], 2)

    def test_missing_middle_id_fails_even_when_regenerating(self) -> None:
        self.write("lists/AI/11_Agents.md", "AGENT-001", "AGENT-003")
        with self.assertRaisesRegex(ValueError, "AGENT-002"):
            build(self.root)

    def test_missing_first_id_fails_even_when_regenerating(self) -> None:
        self.write("lists/05_Security.md", "SEC-002")
        with self.assertRaisesRegex(ValueError, "SEC-001"):
            build(self.root)

    def test_duplicate_across_scopes_fails(self) -> None:
        self.write("lists/AI/11_Agents.md", "AGENT-001")
        self.write("lists/backend/17_Agents.md", "AGENT-001")
        with self.assertRaisesRegex(ValueError, "Duplicate stable identifier AGENT-001"):
            build(self.root)


if __name__ == "__main__":
    unittest.main()
