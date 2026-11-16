"""Offline tests for scoped generator and reviewed external-ID starter metadata."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / "skills" / "awesome-checklists" / "scripts"
sys.path.insert(0, str(SCRIPTS))
from export_checklists import export  # noqa: E402
from generate_review import markdown, select  # noqa: E402


class ScopedReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = export(ROOT, "all", False, None)

    def test_three_profiles_and_sizes_are_bounded_unknown_and_unique(self):
        for profile in ("startup", "regulated", "internal-tool"):
            for size in (25, 50, 100):
                with self.subTest(profile=profile, size=size):
                    selection = select(self.catalog, profile=profile, size=size)
                    self.assertEqual(selection["count"], size)
                    self.assertEqual(len({x["id"] for x in selection["items"]}), size)
                    self.assertEqual({x["status"] for x in selection["items"]}, {"UNKNOWN"})
                    self.assertTrue(all(not x["evidence"] for x in selection["items"]))
                    self.assertTrue(all(x["scope"] != "AI" for x in selection["items"]))
                    self.assertEqual(
                        [x["id"] for x in selection["items"]],
                        [x["id"] for x in select(self.catalog, profile=profile, size=size)["items"]],
                    )

    def test_scope_specific_starters_are_bounded(self):
        for scope in ("shared", "frontend", "backend", "AI"):
            with self.subTest(scope=scope):
                result = select(self.catalog, profile="startup", scopes=[scope], size=25)
                self.assertEqual(result["count"], 25)
                self.assertEqual({item["scope"] for item in result["items"]}, {scope})
                self.assertEqual({item["status"] for item in result["items"]}, {"UNKNOWN"})
                self.assertEqual(len({item["id"] for item in result["items"]}), 25)

    def test_backend_agent_only_does_not_pad_22_ids(self):
        with self.assertRaises(ValueError):
            select(self.catalog, profile="startup", scopes=["backend"], domains=["AGENT"], size=25)

    def test_scope_and_domain_filters(self):
        review = select(self.catalog, profile="startup", scopes=["AI"], size=25)
        self.assertEqual({x["scope"] for x in review["items"]}, {"AI"})
        sec = select(self.catalog, profile="regulated", domains=["SEC"], size=25)
        self.assertTrue(all(x["id"].startswith("SEC-") for x in sec["items"]))

    def test_inclusion_exclusion_and_rejection(self):
        review = select(
            self.catalog, profile="startup", size=25,
            include=["SEC-111"], exclude=["SEC-007"],
        )
        ids = {x["id"] for x in review["items"]}
        self.assertIn("SEC-111", ids)
        self.assertNotIn("SEC-007", ids)
        for options in (
            {"size": 24},
            {"size": 101},
            {"domains": ["NONEXISTENT"], "size": 25},
            {"include": ["NOPE-999"]},
            {"include": ["SEC-007"], "exclude": ["SEC-007"]},
            {"scopes": ["AI"], "include": ["SEC-102"]},
        ):
            with self.subTest(options=options), self.assertRaises(ValueError):
                select(self.catalog, profile="startup", **options)

    def test_markdown_is_unverified_not_prechecked(self):
        selection = select(self.catalog, profile="startup", size=25)
        selection["source_commit"] = "a" * 40
        text = markdown(selection, "Demo | beta", "release-1")
        self.assertIn("UNVERIFIED STARTER TEMPLATE", text)
        self.assertIn("UNKNOWN", text)
        self.assertIn("Demo \\| beta", text)
        self.assertNotIn("- [x]", text.lower())
        self.assertIn("NOT ASSESSED", text)

    def test_cli_writes_scoped_markdown_and_json(self):
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder) / "review.md"
            cmd = [
                sys.executable, str(SCRIPTS / "generate_review.py"),
                "--repo-root", str(ROOT),
                "--profile", "internal-tool",
                "--domain", "SEC", "--size", "25",
                "--output", str(out),
            ]
            proc = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertIn("[SEC-111](", out.read_text(encoding="utf-8"))
            self.assertIn("UNKNOWN", out.read_text(encoding="utf-8"))
            proc2 = subprocess.run(
                cmd[:-2] + ["--format", "json", "--output", str(Path(folder) / "review.json")],
                capture_output=True, text=True,
            )
            self.assertEqual(proc2.returncode, 0, proc2.stderr)
            data = json.loads((Path(folder) / "review.json").read_text(encoding="utf-8"))
            self.assertEqual(data["count"], 25)
            self.assertRegex(data["source_commit"], r"^[a-f0-9]{40}$")
            self.assertEqual({x["status"] for x in data["items"]}, {"UNKNOWN"})

    def test_crosswalk_uses_existing_ids_and_referenced_verified_identifiers(self):
        root = ROOT / "lists" / "references"
        data = json.loads((root / "control-crosswalk.json").read_text(encoding="utf-8"))
        self.assertEqual(data["schema_version"], 1)
        self.assertGreaterEqual(len(data["mappings"]), 20)
        all_ids = {x["id"] for x in self.catalog["items"]}
        keys = set()
        for row in data["mappings"]:
            self.assertIn(row["check_id"], all_ids)
            self.assertIn(row["framework"], data["standards"])
            self.assertEqual(row["mapping_status"], "proposed-partial-topic-alignment")
            self.assertEqual(row["identifier_verification"], "primary-source-id-confirmed")
            self.assertTrue(row["source_url"].startswith("https://"))
            pair = (row["check_id"], row["framework"], row["external_id"])
            self.assertNotIn(pair, keys)
            keys.add(pair)
        self.assertEqual(
            set(row["framework"] for row in data["mappings"]),
            {"ASVS", "NIST_CSF", "ISO_27002", "SOC2_TSC"},
        )


if __name__ == "__main__":
    unittest.main()
