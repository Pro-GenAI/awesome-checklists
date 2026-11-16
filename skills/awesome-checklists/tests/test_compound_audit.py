# SPDX-License-Identifier: MIT
"""Offline tests for conservative compound-check candidate detection."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

BASE = Path(__file__).resolve().parents[1] / "scripts"
spec = importlib.util.spec_from_file_location("audit_compound_checks", BASE / "audit_compound_checks.py")
import sys
sys.path.insert(0, str(BASE))
auditor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(auditor)


class CompoundAuditTests(unittest.TestCase):
    def test_explicit_multi_action_is_candidate(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "lists").mkdir()
            (root / "lists" / "01_Demo.md").write_text(
                "- [ ] **SEC-001** `P1` Test authorization; verify tenant isolation.\n"
                "- [ ] **SEC-002** `P2` Record reviewer name.\n",
                encoding="utf-8",
            )
            result = auditor.candidates(root)
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]["id"], "SEC-001")


if __name__ == "__main__":
    unittest.main()
