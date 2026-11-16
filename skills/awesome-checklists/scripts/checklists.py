#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Read explicitly selected checklists at an immutable source revision (stdlib only)."""
from __future__ import annotations

import argparse
import base64
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

REPO = "Pro-GenAI/awesome-checklists"
API = "https://api.github.com/repos/" + REPO
RAW_ORIGIN = "https://raw.githubusercontent.com"
# Updated as an explicit maintenance step after a verified content release.
SOURCE_RELEASE = Path(__file__).resolve().parents[1] / "references" / "source-release.json"
DEFAULT_REF = json.loads(SOURCE_RELEASE.read_text(encoding="utf-8"))["checklist_source_sha"]
SHA = re.compile(r"^[0-9a-fA-F]{40}$")
CHECKLIST = re.compile(r"^lists/(?:(?:frontend|backend|AI)/)?\d{2}_[A-Za-z0-9_]+\.md$")
SCOPES = {"shared", "frontend", "backend", "ai", "all"}
MAX_BATCH = 5
CHECK_ID = re.compile(r"^[A-Z][A-Z0-9]*-\d{3}$")
CHECK_LINE = re.compile(r"^\s*-\s*\[ \]\s+\*\*([A-Z][A-Z0-9]*-\d{3})\*\*")


class SourceError(Exception):
    pass


class SameOriginRedirectHandler(HTTPRedirectHandler):
    """Do not send credentials or trust content from changed URL origins."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        original, target = urlsplit(req.full_url), urlsplit(newurl)
        if target.scheme != "https" or target.netloc != original.netloc:
            raise SourceError("Refusing cross-origin redirect")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def error_detail(exc: Exception) -> str:
    if isinstance(exc, HTTPError):
        headers = exc.headers or {}
        if exc.code == 429 or (
            exc.code == 403 and (
                headers.get("X-RateLimit-Remaining") == "0"
                or "rate" in str(exc.reason).lower()
            )
        ):
            retry = headers.get("Retry-After")
            reset = headers.get("X-RateLimit-Reset")
            info = "GitHub API rate limit (HTTP " + str(exc.code) + ")"
            if retry and retry.isdigit():
                info += "; retry after " + retry + " seconds"
            elif reset and reset.isdigit():
                info += "; reset at Unix timestamp " + reset
            return info + "; use --raw for known files or an authenticated GH_TOKEN/sparse clone"
        return "HTTP " + str(exc.code)
    if isinstance(exc, URLError):
        return "network error (" + type(exc.reason).__name__ + ")"
    return "invalid response (" + type(exc).__name__ + ")"


def retry_transient(operation):
    """Retry transient fetch errors without retrying 404 or lengthy rate limits."""
    for attempt in range(3):
        try:
            return operation()
        except (HTTPError, URLError) as exc:
            if attempt == 2:
                raise
            if isinstance(exc, HTTPError):
                if exc.code not in (429, 500, 502, 503, 504):
                    raise
                if exc.code == 429:
                    value = (exc.headers or {}).get("Retry-After")
                    if not value or not value.isdigit() or int(value) > 2:
                        raise
                    delay = int(value)
                else:
                    delay = 0.25 * (2 ** attempt)
            else:
                delay = 0.25 * (2 ** attempt)
            time.sleep(delay)


def request_json(url: str, headers: dict[str, str]) -> dict:
    req = Request(url, headers=headers)
    def perform():
        with build_opener(SameOriginRedirectHandler()).open(req, timeout=20) as response:
            return json.load(response)
    return retry_transient(perform)


def github_json(endpoint: str) -> dict:
    """Use explicit API token, then gh session, then anonymous public API."""
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "awesome-checklists-skill"}
    if token:
        headers["Authorization"] = "Bearer " + token
    url = API + "/" + endpoint
    if token:
        try:
            return request_json(url, headers)
        except (HTTPError, URLError, ValueError) as exc:
            raise SourceError(
                "GitHub API request failed (" + error_detail(exc)
                + "); check token/repository access or use --raw for public pinned files"
            ) from exc

    errors = []
    try:
        proc = subprocess.run(
            ["gh", "api", "repos/" + REPO + "/" + endpoint],
            capture_output=True, text=True, check=False, timeout=30,
        )
        if proc.returncode == 0:
            return json.loads(proc.stdout)
        errors.append("GitHub CLI did not have access")
    except (FileNotFoundError, subprocess.TimeoutExpired, ValueError):
        errors.append("GitHub CLI unavailable")
    try:
        return request_json(url, headers)
    except (HTTPError, URLError, ValueError) as exc:
        errors.append("GitHub API returned " + error_detail(exc))
    raise SourceError(
        "Unable to retrieve public checklist source (" + "; ".join(errors)
        + "). Try --raw with a pinned SHA, gh auth login, GH_TOKEN, or a local sparse clone."
    )


def validate_path(path: str) -> str:
    if not CHECKLIST.fullmatch(path):
        raise SourceError("Not a checklist Markdown path: " + repr(path))
    return path


def matches_scope(path: str, scope: str) -> bool:
    if not CHECKLIST.fullmatch(path):
        return False
    parts = path.split("/")
    selected = parts[1].lower() if len(parts) == 3 else "shared"
    return scope == "all" or selected == scope


def resolve_ref(ref: str) -> str:
    if SHA.fullmatch(ref):
        return ref.lower()
    item = github_json("commits/" + quote(ref, safe=""))
    sha = item.get("sha")
    if not isinstance(sha, str) or not SHA.fullmatch(sha):
        raise SourceError("GitHub did not return a valid commit SHA")
    return sha.lower()


def local_path(repo_root: Path, relative: str) -> Path:
    root = repo_root.resolve()
    file = (root / relative).resolve()
    if not file.is_relative_to(root):
        raise SourceError("Checklist path escapes repository root")
    return file


def local_ref(repo_root: Path) -> str:
    """Explicitly disclose missing Git HEAD instead of implying a pinned source."""
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
            capture_output=True, text=True, check=False, timeout=10,
        )
        if result.returncode == 0 and SHA.fullmatch(result.stdout.strip()):
            dirty = subprocess.run(
                ["git", "-C", str(repo_root), "status", "--porcelain", "--untracked-files=no"],
                capture_output=True, text=True, check=False, timeout=10,
            )
            if dirty.returncode == 0 and not dirty.stdout.strip():
                return result.stdout.strip().lower()
    except (OSError, subprocess.TimeoutExpired):
        pass
    return "UNVERIFIED-LOCAL-SOURCE"


def list_paths(repo_root: Path | None, ref: str, scope: str) -> list[str]:
    if repo_root:
        if not repo_root.is_dir():
            raise SourceError("Source directory not found: " + str(repo_root))
        root = repo_root.resolve()
        lists = root / "lists"
        folders = (lists, lists / "frontend", lists / "backend", lists / "AI")
        paths = [file.relative_to(root).as_posix()
                 for folder in folders for file in folder.glob("*.md")
                 if file.is_file() and file.resolve().is_relative_to(root)]
    else:
        tree = github_json("git/trees/" + quote(ref, safe="") + "?recursive=1")
        if tree.get("truncated"):
            raise SourceError("GitHub tree truncated; use a local sparse clone")
        paths = [entry["path"] for entry in tree.get("tree", [])
                 if entry.get("type") == "blob" and isinstance(entry.get("path"), str)]
    return sorted(path for path in paths if matches_scope(path, scope))


def decode_markdown(item: dict) -> str:
    if item.get("encoding") != "base64" or not isinstance(item.get("content"), str):
        raise SourceError("Unexpected GitHub file encoding")
    try:
        encoded = re.sub(r"\s+", "", item["content"])
        return base64.b64decode(encoded, validate=True).decode("utf-8")
    except (UnicodeError, ValueError, base64.binascii.Error) as exc:
        raise SourceError("Could not decode upstream Markdown") from exc


def raw_text(ref: str, path: str) -> str:
    """No Authorization header is ever sent to raw.githubusercontent.com."""
    validate_path(path)
    if not SHA.fullmatch(ref):
        raise SourceError("Raw URLs must use a pinned 40-hex source commit")
    url = RAW_ORIGIN + "/" + REPO + "/" + ref + "/" + quote(path, safe="/")
    request = Request(url, headers={"User-Agent": "awesome-checklists-skill"})
    def perform():
        with build_opener(SameOriginRedirectHandler()).open(request, timeout=20) as response:
            return response.read().decode("utf-8")
    try:
        return retry_transient(perform)
    except (HTTPError, URLError, UnicodeError) as exc:
        raise SourceError("Raw source fetch failed (" + error_detail(exc) + ")") from exc


def fetch_text(repo_root: Path | None, ref: str, path: str, raw: bool = False) -> str:
    validate_path(path)
    if repo_root:
        file = local_path(repo_root, path)
        if not file.is_file():
            raise SourceError("Checklist does not exist: " + str(file))
        return file.read_text(encoding="utf-8")
    if raw:
        return raw_text(ref, path)
    item = github_json("contents/" + quote(path, safe="/") + "?ref=" + quote(ref, safe=""))
    if item.get("type") != "file":
        raise SourceError("GitHub path is not a file")
    if item.get("encoding") != "base64":
        sha = item.get("sha")
        if not isinstance(sha, str) or not SHA.fullmatch(sha):
            raise SourceError("Missing blob SHA")
        item = github_json("git/blobs/" + sha)
    return decode_markdown(item)


def filter_check_id(markdown: str, identifier: str) -> str:
    """Return one source checkbox without claiming complete review coverage."""
    if not CHECK_ID.fullmatch(identifier):
        raise SourceError("Invalid stable checklist ID: " + repr(identifier))
    lines = [line for line in markdown.splitlines()
             if (m := CHECK_LINE.match(line)) and m.group(1) == identifier]
    if len(lines) != 1:
        raise SourceError("Expected exactly one criterion for " + identifier +
                          "; found " + str(len(lines)))
    return lines[0] + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, help="Read checked-out source offline; rejects --ref")
    parser.add_argument("--ref", help="Explicit source ref; defaults to an immutable commit SHA, never main")
    parser.add_argument("--raw", action="store_true",
                        help="Read public raw content without GitHub API or credentials (fetch commands only)")
    sub = parser.add_subparsers(dest="command", required=True)
    ls = sub.add_parser("list", help="List available numbered checklist paths")
    ls.add_argument("--scope", choices=sorted(SCOPES), default="all")
    fetch = sub.add_parser("fetch", help="Read one checklist")
    fetch.add_argument("path")
    fetch.add_argument("--id", dest="check_id", help="return only one exact stable-ID criterion")
    fetch.add_argument("--output", type=Path)
    many = sub.add_parser("fetch-many", help="Fetch at most five explicitly selected checklists")
    many.add_argument("paths", nargs="+")
    many.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.repo_root:
            if args.ref is not None:
                raise SourceError("--ref cannot be combined with --repo-root; check out that commit first")
            if args.raw:
                raise SourceError("--raw cannot be combined with --repo-root")
            ref = local_ref(args.repo_root)
            if ref == "UNVERIFIED-LOCAL-SOURCE":
                print("WARNING: no local Git HEAD; report source unverified, not an authenticated checklist revision",
                      file=sys.stderr)
        else:
            if args.ref and not SHA.fullmatch(args.ref):
                print("WARNING: --ref is movable; resolving to a commit before retrieval", file=sys.stderr)
            ref = resolve_ref(args.ref or DEFAULT_REF)
        print("checklists: source " + REPO + " @ " + ref, file=sys.stderr)
        if args.command == "list":
            if args.raw:
                raise SourceError("--raw supports fetch/fetch-many only; use API or sparse clone to list")
            for path in list_paths(args.repo_root, ref, args.scope):
                print(path)
        elif args.command == "fetch":
            if args.check_id and not CHECK_ID.fullmatch(args.check_id):
                raise SourceError("Invalid stable checklist ID")
            content = fetch_text(args.repo_root, ref, args.path, args.raw)
            if args.check_id:
                content = filter_check_id(content, args.check_id)
                print("NOTE: this single-ID excerpt omits release gates and references; fetch the complete file for sign-off", file=sys.stderr)
            if args.output:
                args.output.parent.mkdir(parents=True, exist_ok=True)
                args.output.write_text(content, encoding="utf-8")
                print("Saved " + args.path + " from " + ref + " to " + str(args.output), file=sys.stderr)
            else:
                sys.stdout.write(content)
        else:
            if len(args.paths) > MAX_BATCH or len(set(args.paths)) != len(args.paths):
                raise SourceError("fetch-many requires 1–5 distinct checklist paths; batch large reviews")
            for path in args.paths:
                validate_path(path)
            for path in args.paths:
                data = fetch_text(args.repo_root, ref, path, args.raw)
                destination = args.output_dir / path
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text(data, encoding="utf-8")
                print("Saved " + path + " from " + ref, file=sys.stderr)
    except (SourceError, OSError) as exc:
        print("checklists: " + str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
