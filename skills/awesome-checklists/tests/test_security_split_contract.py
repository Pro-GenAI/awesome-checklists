# SPDX-License-Identifier: MIT
"""Source-level regression contract for editorial SEC-012/013/014 split.

Passing these tests verifies structure, not security or expert validation.
"""
import json
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "skills/awesome-checklists/scripts"))
from audit_compound_checks import compound_signals  # noqa: E402

LINE = re.compile(r"^- \[ \] \*\*(SEC-\d{3})\*\* `(P[012])` (.+)$", re.M)
EXPECTED = {
    "SEC-012": ("lists/05_Security.md", "Validate untrusted inputs against explicit server-side contracts at applicable trust boundaries."),
    "SEC-013": ("lists/backend/09_Security.md", "Test for HTTP request-smuggling and desynchronization at applicable proxy-to-backend boundaries."),
    "SEC-014": ("lists/backend/09_Security.md", "Test replay resistance for high-impact, non-idempotent API operations when a repeated request could cause unintended effects."),
    "SEC-118": ("lists/05_Security.md", "Test that user-controlled values cannot alter database query structure through SQL or NoSQL injection."),
    "SEC-119": ("lists/05_Security.md", "Test that user-controlled values cannot alter shell or subprocess command execution."),
    "SEC-120": ("lists/05_Security.md", "Verify that untrusted serialized input cannot instantiate unauthorized object types or execute code."),
    "SEC-121": ("lists/backend/09_Security.md", "Test that user-controlled filesystem paths cannot escape authorized directory boundaries."),
}


class SecuritySplitContract(unittest.TestCase):
    def test_criteria_have_one_id_and_no_compound_heuristic(self):
        for identifier, (relative, wording) in EXPECTED.items():
            with self.subTest(identifier=identifier):
                source = (ROOT / relative).read_text(encoding="utf-8")
                items = [match for match in LINE.finditer(source) if match.group(1) == identifier]
                self.assertEqual(len(items), 1)
                self.assertEqual(items[0].group(3), wording)
                self.assertEqual(compound_signals(wording), [])

    def test_security_owner_registry_and_core_metadata(self):
        registry = json.loads((ROOT / "lists/references/security-id-registry.json").read_text())["active"]
        for identifier, (relative, _) in EXPECTED.items():
            self.assertEqual(registry[identifier], relative)
        core = json.loads((ROOT / "lists/references/core-50.json").read_text())
        selected = [item for item in core["checks"] if item["id"] == "SEC-012"]
        self.assertEqual(len(selected), 1)
        self.assertEqual(selected[0]["criterion"], EXPECTED["SEC-012"][1])

    def test_database_injection_mapping_follows_new_id(self):
        crosswalk = json.loads((ROOT / "lists/references/control-crosswalk.json").read_text())
        mapped = [item for item in crosswalk["mappings"] if item["external_id"] == "v5.0.0-1.2.4"]
        self.assertTrue(any(item["check_id"] == "SEC-118" for item in mapped))
        self.assertFalse(any(item["check_id"] == "SEC-012" for item in mapped))


if __name__ == "__main__":
    unittest.main()
