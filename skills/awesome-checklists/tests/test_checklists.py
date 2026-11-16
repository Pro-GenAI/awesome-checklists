# SPDX-License-Identifier: MIT
"""Offline smoke tests for the standalone agent skill and helper."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import base64
import importlib.util
import os
from unittest.mock import patch, MagicMock
from urllib.error import HTTPError
from urllib.request import Request

SKILL_DIR = Path(__file__).resolve().parents[1]
SCRIPT = SKILL_DIR / "scripts" / "checklists.py"
spec = importlib.util.spec_from_file_location("checklists", SCRIPT)
checklists = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checklists)


def skill_description(frontmatter: str) -> str:
    """Read inline or folded description in the skill's supported YAML subset."""
    lines = frontmatter.splitlines()
    for index, line in enumerate(lines):
        if not line.startswith("description:"):
            continue
        value = line.partition(":")[2].strip()
        if value not in (">", ">-", "|", "|-"):
            return value.strip('"').strip("'")
        parts = []
        for continuation in lines[index + 1:]:
            if continuation.startswith(("  ", "\t")):
                parts.append(continuation.strip())
            else:
                break
        return " ".join(parts)
    raise ValueError("Missing frontmatter description")


class SkillTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        for name in ("lists/01_Requirements_and_Planning.md", "lists/frontend/05_Accessibility.md", "lists/backend/07_API_Design_and_Integrations.md", "lists/AI/11_AI_Agents_and_Tool_Orchestration.md"):
            path = self.repo / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"# {name}\n\n- [ ] **TEST-001** `P1` Sample.\n", encoding="utf-8")
        (self.repo / "AGENTS.md").write_text("# Agents\n", encoding="utf-8")
        (self.repo / "website").mkdir()
        (self.repo / "website" / "README.md").write_text("# Site\n", encoding="utf-8")

    def run_script(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--repo-root", str(self.repo), *args],
            text=True, capture_output=True, check=False,
        )

    def test_skill_frontmatter(self) -> None:
        content = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(content.startswith("---\n"))
        header = content.split("---\n", 2)[1]
        self.assertIn("name: awesome-checklists\n", header)
        self.assertIn("description: ", header)
        self.assertLessEqual(len(skill_description(header)), 1024)
        self.assertTrue(skill_description(header))

    def test_folded_frontmatter_description(self):
        fixture = "name: awesome-checklists\n" + "description: >\n  A long description\n  that spans multiple lines\n" + "compatibility: Python\n"
        self.assertEqual(skill_description(fixture),
                         "A long description that spans multiple lines")

    def test_list_scopes_and_excludes_nonscope_docs(self) -> None:
        result = self.run_script("list", "--scope", "all")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(result.stdout.strip().splitlines()), 4)
        self.assertNotIn("AGENTS.md", result.stdout)
        self.assertNotIn("website", result.stdout)
        self.assertIn("UNVERIFIED-LOCAL-SOURCE", result.stderr)
        self.assertNotIn("outreach-tools-and-skills.md", result.stdout)
        ai = self.run_script("list", "--scope", "ai")
        self.assertEqual(ai.stdout.strip(), "lists/AI/11_AI_Agents_and_Tool_Orchestration.md")
        shared = self.run_script("list", "--scope", "shared")
        self.assertEqual(shared.stdout.strip(), "lists/01_Requirements_and_Planning.md")

    def test_fetch_stdout_and_file(self) -> None:
        content = self.run_script("fetch", "lists/frontend/05_Accessibility.md")
        self.assertEqual(content.returncode, 0, content.stderr)
        self.assertIn("TEST-001", content.stdout)
        destination = self.repo / "out" / "selected.md"
        saved = self.run_script("fetch", "lists/AI/11_AI_Agents_and_Tool_Orchestration.md", "--output", str(destination))
        self.assertEqual(saved.returncode, 0, saved.stderr)
        self.assertIn("TEST-001", destination.read_text(encoding="utf-8"))

    def test_single_id_fetch_and_missing_id(self):
        result = self.run_script("fetch", "lists/01_Requirements_and_Planning.md",
                                 "--id", "TEST-001")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("TEST-001", result.stdout)
        self.assertIn("omits release gates", result.stderr)
        missing = self.run_script("fetch", "lists/01_Requirements_and_Planning.md",
                                  "--id", "TEST-999")
        self.assertNotEqual(missing.returncode, 0)
        self.assertIn("Expected exactly one", missing.stderr)

    def test_symlink_escape_not_listed_or_read(self):
        outside = self.repo.parent / "outside.md"
        outside.write_text("outside fixture", encoding="utf-8")
        link = self.repo / "lists/02_Outside.md"
        try:
            link.symlink_to(outside)
        except OSError:
            self.skipTest("Symlinks unavailable")
        self.assertNotIn("02_Outside.md", self.run_script("list").stdout)
        result = self.run_script("fetch", "lists/02_Outside.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("escapes repository root", result.stderr)
        self.assertNotIn("outside fixture", result.stdout)

    def test_remote_list_truncated_tree(self):
        with patch.object(checklists, "github_json", return_value={
            "truncated": True, "tree": []}):
            with self.assertRaises(checklists.SourceError) as context:
                checklists.list_paths(None, "a" * 40, "all")
        self.assertIn("truncated", str(context.exception))
        with patch.object(checklists, "github_json", return_value={
            "truncated": False,
            "tree": [{"type": "blob", "path": "lists/05_Security.md"},
                     {"type": "blob", "path": "README.md"}]}):
            self.assertEqual(checklists.list_paths(None, "a" * 40, "all"),
                             ["lists/05_Security.md"])

    def test_refuse_traversal_and_unknown_file(self) -> None:
        invalid = self.run_script("fetch", "../AGENTS.md")
        self.assertNotEqual(invalid.returncode, 0)
        self.assertIn("Not a checklist", invalid.stderr)
        legacy = self.run_script("fetch", "AI/11_AI_Agents_and_Tool_Orchestration.md")
        self.assertNotEqual(legacy.returncode, 0)
        missing = self.run_script("fetch", "lists/AI/02_Missing.md")
        self.assertNotEqual(missing.returncode, 0)
        ref = self.run_script("--ref", "main", "list")
        self.assertNotEqual(ref.returncode, 0)
        self.assertIn("--ref cannot be combined", ref.stderr)

    def test_http_error_includes_status_without_token(self) -> None:
        failure = HTTPError("https://api.github.com/", 403, "rate limited", {}, None)
        with patch.dict(os.environ, {"GH_TOKEN": "secret", "GITHUB_TOKEN": ""}), patch.object(checklists, "request_json", side_effect=failure):
            with self.assertRaises(checklists.SourceError) as ctx:
                checklists.github_json("git/trees/main")
        self.assertIn("HTTP 403", str(ctx.exception))
        self.assertNotIn("secret", str(ctx.exception))

    def test_anonymous_fallback_and_http_diagnostics(self) -> None:
        failure = HTTPError("https://api.github.com/", 404, "not found", {}, None)
        with patch.dict(os.environ, {"GH_TOKEN": "", "GITHUB_TOKEN": ""}), \
             patch.object(checklists.subprocess, "run", return_value=subprocess.CompletedProcess([], 1, "", "")), \
             patch.object(checklists, "request_json", side_effect=failure):
            with self.assertRaises(checklists.SourceError) as ctx:
                checklists.github_json("contents/missing")
        self.assertIn("HTTP 404", str(ctx.exception))
        self.assertIn("GitHub CLI did not have access", str(ctx.exception))

    def test_resolve_ref_and_blob_fallback(self) -> None:
        sha = "a" * 40
        item = {"type": "file", "encoding": "none", "sha": sha}
        blob = {"encoding": "base64", "content": base64.b64encode("# Large checklist\n".encode()).decode()}
        with patch.object(checklists, "github_json", side_effect=[{"sha": sha}, item, blob]) as mocked:
            self.assertEqual(checklists.resolve_ref("main"), sha)
            self.assertEqual(checklists.fetch_text(None, sha, "lists/05_Security.md"), "# Large checklist\n")
        self.assertIn(f"git/blobs/{sha}", mocked.call_args_list[-1].args[0])

    def test_default_is_immutable_sha_and_raw_source_unauthed(self):
        self.assertRegex(checklists.DEFAULT_REF, r"^[a-f0-9]{40}$")
        self.assertNotEqual(checklists.DEFAULT_REF, "main")
        response = unittest.mock.MagicMock()
        response.__enter__.return_value.read.return_value = b"# Pinned source"
        with patch.object(checklists, "build_opener") as opener:
            opener.return_value.open.return_value = response
            raw = checklists.raw_text(checklists.DEFAULT_REF, "lists/05_Security.md")
        self.assertEqual(raw, "# Pinned source")
        req = opener.return_value.open.call_args.args[0]
        self.assertNotIn("authorization", {k.lower() for k in req.headers})
        self.assertIn(checklists.DEFAULT_REF, req.full_url)

    def test_rate_limit_error_has_actionable_message(self):
        failure = HTTPError(
            "https://api.github.com", 403, "rate limited",
            {"X-RateLimit-Remaining": "0", "Retry-After": "60"}, None,
        )
        detail = checklists.error_detail(failure)
        self.assertIn("rate limit", detail)
        self.assertIn("retry after 60 seconds", detail)
        self.assertIn("--raw", detail)

    def test_bounded_transient_retries(self):
        temporary = HTTPError("https://api.github.com/", 503, "unavailable", {}, None)
        operation = MagicMock(side_effect=[temporary, {"ok": True}])
        with patch.object(checklists.time, "sleep") as sleeper:
            self.assertEqual(checklists.retry_transient(operation), {"ok": True})
        self.assertEqual(operation.call_count, 2)
        sleeper.assert_called_once_with(0.25)
        for status, headers in ((404, {}), (429, {"Retry-After": "60"})):
            operation = MagicMock(side_effect=HTTPError("https://api.github.com/", status, "error", headers, None))
            with patch.object(checklists.time, "sleep") as sleeper:
                with self.assertRaises(HTTPError):
                    checklists.retry_transient(operation)
            operation.assert_called_once()
            sleeper.assert_not_called()

    def test_batch_limit_and_local_multi_fetch(self):
        output = self.repo / "saved"
        ok = self.run_script("fetch-many",
            "lists/01_Requirements_and_Planning.md",
            "lists/AI/11_AI_Agents_and_Tool_Orchestration.md",
            "--output-dir", str(output),
        )
        self.assertEqual(ok.returncode, 0, ok.stderr)
        self.assertTrue((output / "lists/AI/11_AI_Agents_and_Tool_Orchestration.md").exists())
        large = self.run_script("fetch-many", *(
            ["lists/01_Requirements_and_Planning.md"] * 6),
            "--output-dir", str(output))
        self.assertNotEqual(large.returncode, 0)
        self.assertIn("1–5 distinct", large.stderr)

    def test_invalid_blob_and_cross_origin_redirect(self) -> None:
        with self.assertRaises(checklists.SourceError):
            checklists.decode_markdown({"encoding": "base64", "content": "!!!!"})
        handler = checklists.SameOriginRedirectHandler()
        with self.assertRaises(checklists.SourceError):
            handler.redirect_request(Request("https://api.github.com/repos/x"), None, 302, "Found", {}, "https://example.com/steal")


if __name__ == "__main__":
    unittest.main()
