# SPDX-License-Identifier: MIT
"""Maintain the split from AGENT-026 into independent acceptance assertions."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[3]
FILE = ROOT / "lists/AI/11_AI_Agents_and_Tool_Orchestration.md"
TEXT = FILE.read_text(encoding="utf-8")
CHECK = re.compile(r"^- \[ \] \*\*(AGENT-\d{3})\*\* `P[012]` (.+)$", re.M)
EXPECTED = {
    "AGENT-026": "Reject tool calls naming tools absent from the trusted registry for the active workflow.",
    "AGENT-137": "Reject tool argument types that violate the server-owned input schema before invocation.",
    "AGENT-138": "Reject tool calls omitting fields required by the server-owned input schema.",
    "AGENT-139": "Reject tool argument values outside server-defined bounds or allowed enumerations.",
    "AGENT-140": "Reject tool resource identifiers that fail server-owned format and namespace validation.",
    "AGENT-141": "Reject tool calls whose argument payload exceeds the server-configured size limit.",
}


class AgentSchemaSplitTests(unittest.TestCase):
    def test_each_new_criterion_is_present_exactly_once(self):
        entries = {}
        for identifier, criterion in CHECK.findall(TEXT):
            entries.setdefault(identifier, []).append(criterion)
        for identifier, criterion in EXPECTED.items():
            with self.subTest(identifier=identifier):
                self.assertEqual(entries.get(identifier), [criterion])

    def test_owner_contract_preserves_other_scope(self):
        contract = json.loads((ROOT / "lists/references/agent-domain-contract.json").read_text(encoding="utf-8"))
        self.assertEqual(contract["contiguous_numeric_ids"], [1, 141])
        self.assertEqual(contract["scope_slices"][0]["ranges"], [[1, 94], [117, 141]])
        self.assertEqual(contract["scope_slices"][1]["ranges"], [[95, 116]])

    def test_acceptance_evidence_has_each_id(self):
        guide = (ROOT / "lists/references/agent-testing-tools.md").read_text(encoding="utf-8")
        for identifier in EXPECTED:
            self.assertIn("`" + identifier + "`", guide)


if __name__ == "__main__":
    unittest.main()
