"""Only manually curated tiers may contribute severity score to review selection."""
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "skills/awesome-checklists/scripts"))
from export_checklists import export
from generate_review import item_score, PROFILES, select


class PriorityRankingTests(unittest.TestCase):
    def test_provisional_severity_labels_do_not_reorder_identical_controls(self):
        base = {
            "id": "SEC-099",
            "criterion_markdown": "Check that the deployed service enforces identity validation.",
            "priority_basis": "provisional-text-triage",
        }
        scores = [
            item_score({**base, "priority": priority}, PROFILES["startup"])
            for priority in ("P0", "P1", "P2")
        ]
        self.assertEqual(scores, [scores[0]] * 3)

    def test_curated_tiers_still_contribute_to_selection(self):
        base = {
            "id": "SEC-012",
            "criterion_markdown": "Validate input contracts.",
            "priority_basis": "curated-core-50",
        }
        self.assertGreater(
            item_score({**base, "priority": "P0"}, PROFILES["startup"]),
            item_score({**base, "priority": "P2"}, PROFILES["startup"]),
        )

    def test_selection_metadata_matches_actual_ranking(self):
        catalog = export(ROOT, "all", False, None)
        result = select(catalog, profile="startup", size=25)
        self.assertIn("curated Core 50 tiers only", result["selection_method"])
        self.assertIn("provisional tiers are never scored", result["selection_method"])
        guide = (ROOT / "lists/references/scoped-review-generator.md").read_text(encoding="utf-8")
        self.assertIn("Provisional `P0/P1/P2` labels remain visible", guide)
        self.assertNotIn("then uses the visible `P0/P1/P2` tiers", guide)


if __name__ == "__main__":
    unittest.main()
