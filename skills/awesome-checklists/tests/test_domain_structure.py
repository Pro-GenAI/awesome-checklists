# SPDX-License-Identifier: MIT
"""Offline regression tests for cross-scope AGENT domain continuity and links."""
from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(SCRIPTS))
from validate_domain_structure import validate  # noqa: E402


class AgentDomainContractTests(unittest.TestCase):
    def test_live_domain_has_no_gaps_or_bad_section_links(self):
        self.assertEqual(validate(ROOT), [])

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "lists" / "AI").mkdir(parents=True)
        (self.root / "lists" / "backend").mkdir(parents=True)
        (self.root / "lists" / "references").mkdir(parents=True)
        self.ai = self.root / "lists" / "AI" / "11_Agents.md"
        self.backend = self.root / "lists" / "backend" / "17_Agents.md"
        self.ai.write_text(
            "# AI\n\n## Goals\n\n"
            "- [ ] **AGENT-001** \x60P1\x60 One.\n"
            "- [ ] **AGENT-002** \x60P1\x60 Two.\n\n"
            "[API Checks](../backend/17_Agents.md#api-checks)\n",
            encoding="utf-8",
        )
        self.backend.write_text(
            "# Backend\n\n## API Checks\n\n"
            "- [ ] **AGENT-003** \x60P1\x60 Three.\n\n"
            "[AI](../AI/11_Agents.md)\n",
            encoding="utf-8",
        )
        self.manifest = {
            "schema_version": 1,
            "domain": "AGENT",
            "contiguous_numeric_ids": [1, 3],
            "scope_slices": [
                {
                    "path": "lists/AI/11_Agents.md", "ranges": [[1, 2]],
                    "required_sections": ["Goals"],
                    "required_links": ["../backend/17_Agents.md#api-checks"],
                },
                {
                    "path": "lists/backend/17_Agents.md", "ranges": [[3, 3]],
                    "required_sections": ["API Checks"],
                    "required_links": ["../AI/11_Agents.md"],
                },
            ],
        }
        self.save_contract()

    def save_contract(self):
        (self.root / "lists" / "references" / "agent-domain-contract.json").write_text(
            json.dumps(self.manifest), encoding="utf-8",
        )

    def test_small_correct_cross_file_contract(self):
        self.assertEqual(validate(self.root), [])

    def test_missing_id_is_detected_across_files(self):
        content = self.backend.read_text(encoding="utf-8")
        self.backend.write_text(content.replace("AGENT-003", "AGENT-004"), encoding="utf-8")
        errors = validate(self.root)
        self.assertTrue(any("continuity" in x for x in errors), errors)

    def test_wrong_owner_is_detected(self):
        content = self.ai.read_text(encoding="utf-8")
        self.ai.write_text(content.replace("AGENT-002", "AGENT-003"), encoding="utf-8")
        content = self.backend.read_text(encoding="utf-8")
        self.backend.write_text(content.replace("AGENT-003", "AGENT-002"), encoding="utf-8")
        errors = validate(self.root)
        self.assertTrue(any("expected in" in x for x in errors), errors)

    def test_missing_section_and_anchor_are_detected(self):
        self.backend.write_text(
            self.backend.read_text(encoding="utf-8").replace("## API Checks", "## Operations"),
            encoding="utf-8",
        )
        errors = validate(self.root)
        self.assertTrue(any("missing required section" in x for x in errors), errors)
        self.assertTrue(any("missing referenced section anchor" in x for x in errors), errors)

    def test_broken_cross_scope_link_is_detected(self):
        self.ai.write_text(
            self.ai.read_text(encoding="utf-8").replace(
                "../backend/17_Agents.md#api-checks", "../backend/17_Missing.md#api-checks"
            ), encoding="utf-8",
        )
        errors = validate(self.root)
        self.assertTrue(any("missing cross-scope link" in x for x in errors), errors)


if __name__ == "__main__":
    unittest.main()
