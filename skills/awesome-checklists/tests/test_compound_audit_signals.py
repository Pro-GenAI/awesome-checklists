# SPDX-License-Identifier: MIT
"""Tests for the editorial compound-check heuristic, not semantic judgment."""
from pathlib import Path
import json
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from audit_compound_checks import candidates, compound_signals, filter_core_candidates  # noqa: E402


class CompoundSignalsTests(unittest.TestCase):
    def test_security_012_multi_assertion_is_flagged(self):
        sentence = "Inputs are validated and outputs safely encoded; injection and unsafe deserialization risks are tested."
        self.assertIn("multiple semicolon-delimited clauses", compound_signals(sentence))
        self.assertIn("three or more distinct security-control families", compound_signals(sentence))

    def test_security_014_multi_surface_without_semicolon(self):
        sentence = "APIs use appropriate authorization, rate limits, schema validation, replay controls, and safe error responses."
        self.assertIn("three or more distinct security-control families", compound_signals(sentence))

    def test_simple_criterion_is_not_flagged(self):
        self.assertEqual(compound_signals("Each user can revoke their own current session."), [])

    def test_fixture_surfaces_candidate_with_stable_id(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "lists/05_Security.md"
            source.parent.mkdir(parents=True)
            source.write_text(
                "- [ ] **SEC-012** `P0` Inputs are validated and outputs safely encoded; injection and unsafe deserialization risks are tested.\n",
                encoding="utf-8",
            )
            findings = candidates(root)
            self.assertEqual([entry["id"] for entry in findings], ["SEC-012"])

    def test_core_50_triage_is_a_subset_of_all_candidates(self):
        root = Path(__file__).resolve().parents[3]
        all_items = candidates(root)
        core_items = filter_core_candidates(root, all_items)
        curated = json.loads((root / "lists/references/core-50.json").read_text(encoding="utf-8"))
        selected = {item["id"] for item in curated["checks"]}
        self.assertEqual(len(selected), 50)
        self.assertTrue(all(item["id"] in selected for item in core_items))
        self.assertTrue(all(item["status"] == "requires-human-editorial-review" for item in core_items))
        self.assertLessEqual(len(core_items), len(all_items))


if __name__ == "__main__":
    unittest.main()
