# SPDX-License-Identifier: MIT
"""Offline regression checks for weekly external-link audit coverage."""
from pathlib import Path
from urllib.error import HTTPError
from unittest.mock import patch, MagicMock
import sys
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from lint_repository import external_batch, check_external  # noqa: E402


def http_error(status):
    return HTTPError("https://example.test/control", status, "test", {}, None)


class ExternalLinkAuditTests(unittest.TestCase):
    def test_shards_rotate_and_cover_all_urls(self):
        urls = [f"https://example.test/{n}" for n in range(8)]
        a, start = external_batch(urls, 3, offset=0)
        b, _ = external_batch(urls, 3, offset=3)
        c, _ = external_batch(urls, 3, offset=6)
        self.assertEqual(start, 0)
        self.assertEqual(len(set(a + b + c)), 8)

    def test_offset_wraps_without_duplicates(self):
        urls = ["https://example.test/a", "https://example.test/b"]
        batch, start = external_batch(urls, 10, offset=21)
        self.assertEqual(start, 1)
        self.assertEqual(len(batch), 2)
        self.assertEqual(len(set(batch)), 2)
        self.assertEqual(external_batch([], 10), ([], 0))

    def test_head_404_get_200_is_not_broken(self):
        with patch("lint_repository.urlopen", side_effect=[http_error(404), MagicMock()]) as getter:
            missing, warnings = check_external(["https://example.test/control"], 1)
        self.assertEqual((missing, warnings), ([], []))
        self.assertEqual(getter.call_count, 2)
        self.assertEqual(getter.call_args.args[0].get_method(), "GET")

    def test_head_405_get_404_reports_broken(self):
        with patch("lint_repository.urlopen", side_effect=[http_error(405), http_error(404)]):
            missing, warnings = check_external(["https://example.test/control"], 1)
        self.assertEqual(len(missing), 1)
        self.assertIn("GET 404", missing[0])
        self.assertEqual(warnings, [])

    def test_access_denied_is_inconclusive(self):
        with patch("lint_repository.urlopen", side_effect=http_error(403)):
            missing, warnings = check_external(["https://example.test/control"], 1)
        self.assertEqual(missing, [])
        self.assertEqual(len(warnings), 1)


if __name__ == "__main__":
    unittest.main()
