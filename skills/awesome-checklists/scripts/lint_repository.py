#!/usr/bin/env python3
"""Lint numbered checklists, stable IDs, Markdown links, and source formatting.

Offline checks run on every main push; --external performs optional advisory
checks of a bounded set of upstream links. This tool never modifies sources.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from datetime import date
from concurrent.futures import ThreadPoolExecutor
import json
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen

from validate_inventory import EXPECTED, validate
from validate_domain_structure import validate as validate_domain_structure
from validate_sections import source_structure, check_fragment

ROOT = Path(__file__).resolve().parents[3]
CHECKLIST = re.compile(r"^\d{2}_[A-Za-z0-9_]+\.md$")
CHECK = re.compile(r"^- \[ \] \*\*([A-Z][A-Z0-9]*-\d{3})\*\* \x60(P[012])\x60 (.+)$")
LINK = re.compile(r"!?\[[^]\n]+\]\((?:<([^>]+)>|([^\s)]+))")
SECURITY = (
    "lists/05_Security.md",
    "lists/frontend/09_Security.md",
    "lists/backend/09_Security.md",
    "lists/AI/04_Security.md",
)
SECURITY_REGISTRY = "lists/references/security-id-registry.json"


def checklist_files(root: Path) -> list[Path]:
    files = []
    for scope in EXPECTED:
        folder = root / "lists" / ("" if scope == "shared" else scope)
        files.extend(sorted(p for p in folder.glob("*.md") if p.is_file() and CHECKLIST.fullmatch(p.name)))
    return files


def markdown_files(root: Path) -> list[Path]:
    files = checklist_files(root)
    files.extend(sorted((root / "lists" / "references").glob("*.md")))
    files.extend(sorted((root / "lists" / "frontend" / "references").glob("*.md")))
    for relative in (
        "README.md",
        "AGENTS.md",
        "docs/agents/resources-and-tooling.md",
        "docs/agents/scope-inventory.md",
        "docs/agents/contributor-workflows.md",
        "docs/agents/maintenance-backlog.md",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "AUTHORSHIP.md",
        "skills/awesome-checklists/SKILL.md",
        "skills/awesome-checklists/references/domain-selection.md",
        "website/README.md",
    ):
        file = root / relative
        if file.is_file():
            files.append(file)
    return sorted(set(files))


def mask_inline_code(line: str) -> str:
    """Ignore links in inline code spans without hiding links around code labels.

    Uses matching backtick-run lengths and preserves character offsets. A
    missing closer leaves the opening delimiter as literal Markdown text.
    """
    chars = list(line)
    cursor = 0
    while cursor < len(line):
        if line[cursor] != chr(96):
            cursor += 1
            continue
        end = cursor
        while end < len(line) and line[end] == chr(96):
            end += 1
        delimiter = line[cursor:end]
        close = line.find(delimiter, end)
        if close < 0:
            cursor = end
            continue
        for pos in range(cursor, close + len(delimiter)):
            chars[pos] = " "
        cursor = close + len(delimiter)
    return "".join(chars)


def extract_links(text: str) -> list[str]:
    result = []
    fence = None
    for line in text.splitlines():
        match = re.match(r"^\s*(" + chr(96) + r"{3,}|~{3,})", line)
        if match:
            marker = match.group(1)[0]
            if fence is None:
                fence = marker
            elif fence == marker:
                fence = None
            continue
        if fence:
            continue
        for m in LINK.finditer(mask_inline_code(line)):
            result.append(m.group(1) or m.group(2))
    return result


def check_link(root: Path, source: Path, href: str) -> str | None:
    if href.startswith(("mailto:", "data:", "tel:")):
        return None
    parts = urlsplit(href)
    if parts.scheme in ("http", "https"):
        return None
    if parts.scheme or parts.netloc:
        return None
    target = unquote(parts.path)
    if target.startswith("/"):
        return None  # Absolute website-root paths are deployment-specific.
    if not target and not parts.fragment:
        return None
    if target.startswith(("$", "{")):
        return None
    resolved = (source.parent / target).resolve() if target else source.resolve()
    if not resolved.is_relative_to(root.resolve()):
        return f"{source.relative_to(root)}: local link escapes repository: {href}"
    if resolved.exists():
        return check_fragment(root, source, resolved, parts.fragment)
    return f"{source.relative_to(root)}: missing local link target: {href}"


def lint(root: Path) -> tuple[list[str], list[str]]:
    errors, external = [], []
    _, inventory_errors = validate(root)
    errors.extend(inventory_errors)
    ids = {}
    for path in checklist_files(root):
        rel = path.relative_to(root).as_posix()
        content = path.read_text(encoding="utf-8")
        errors.extend(source_structure(path, content, root))
        for lineno, line in enumerate(content.splitlines(), 1):
            if line != line.rstrip():
                errors.append(f"{rel}:{lineno}: trailing whitespace")
            match = CHECK.match(line)
            if match:
                identifier = match.group(1)
                if identifier in ids:
                    errors.append(f"{rel}:{lineno}: duplicate {identifier} first in {ids[identifier]}")
                ids[identifier] = rel
        if rel in SECURITY and "\n\n\n" in content:
            errors.append(f"{rel}: inconsistent triple-blank-line spacing")
        if rel in SECURITY and "## Suggested testing tools" in content:
            errors.append(f"{rel}: third-party tooling belongs in the optional reference catalog")

    registry = root / SECURITY_REGISTRY
    if not registry.is_file():
        errors.append(f"missing Security ID registry: {SECURITY_REGISTRY}")
    else:
        try:
            expected = json.loads(registry.read_text(encoding="utf-8"))["active"]
            actual = {identifier: source for identifier, source in ids.items() if identifier.startswith("SEC-")}
            if actual != expected:
                missing = sorted(set(expected) - set(actual))
                added = sorted(set(actual) - set(expected))
                moved = sorted(k for k in set(expected) & set(actual) if expected[k] != actual[k])
                errors.append(f"Security registry mismatch: missing={missing[:10]}, unregistered={added[:10]}, moved={moved[:10]}")
        except (OSError, ValueError, TypeError, KeyError) as exc:
            errors.append(f"invalid Security registry ({type(exc).__name__})")

    for path in markdown_files(root):
        content = path.read_text(encoding="utf-8")
        for href in extract_links(content):
            problem = check_link(root, path, href)
            if problem:
                errors.append(problem)
            if urlsplit(href).scheme in ("http", "https"):
                external.append(href)
    errors.extend(validate_domain_structure(root))
    return errors, sorted(set(external))


def external_batch(urls: list[str], limit: int, offset: int | None = None) -> tuple[list[str], int]:
    """Rotate weekly through all distinct URLs instead of always probing the first N."""
    if not urls:
        return [], 0
    # date ordinal week index changes every Monday; manual --external-offset
    # makes any shard reproducible without depending on the date.
    first = ((date.today().toordinal() // 7) * limit if offset is None else offset) % len(urls)
    return [urls[(first + i) % len(urls)] for i in range(min(limit, len(urls)))], first


def check_external(urls: list[str], limit: int) -> tuple[list[str], list[str]]:
    """HEAD failures are inconclusive until a GET confirms 404/410."""
    missing, warnings = [], []
    for url in urls[:limit]:
        headers = {"User-Agent": "awesome-checklists-link-audit/1.0"}
        req = Request(url, method="HEAD", headers=headers)
        try:
            with urlopen(req, timeout=9):
                continue
        except HTTPError as exc:
            if exc.code in (404, 405, 410):
                # Some sites deny HEAD even when ordinary GET works; avoid
                # false broken-link reports and never download response bodies.
                try:
                    with urlopen(Request(url, method="GET", headers=headers), timeout=9):
                        continue
                except HTTPError as get_exc:
                    if get_exc.code in (404, 410):
                        missing.append(f"confirmed GET {get_exc.code}: {url}")
                    else:
                        warnings.append(f"GET HTTP {get_exc.code}: {url}")
                except (URLError, TimeoutError, ValueError) as get_exc:
                    warnings.append(f"GET inconclusive {type(get_exc).__name__}: {url}")
            else:
                warnings.append(f"HEAD HTTP {exc.code}: {url}")
        except (URLError, TimeoutError, ValueError) as exc:
            warnings.append(f"HEAD inconclusive {type(exc).__name__}: {url}")
    return missing, warnings

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--external", action="store_true", help="Check a bounded selection of external URLs (advisory)")
    parser.add_argument("--external-limit", type=int, default=100)
    parser.add_argument("--external-offset", type=int, help="Explicit zero-based URL offset; default rotates weekly")
    args = parser.parse_args()
    if args.external_limit < 1:
        parser.error("--external-limit must be positive")
    if args.external_offset is not None and args.external_offset < 0:
        parser.error("--external-offset must be nonnegative")
    root = args.repo_root.resolve()
    errors, urls = lint(root)
    for error in errors:
        print("FAIL:", error, file=sys.stderr)
    print(f"Checked {len(checklist_files(root))} checklist files and local links; {len(errors)} lint errors; {len(urls)} distinct external references.")
    if args.external:
        batch, offset = external_batch(urls, args.external_limit, args.external_offset)
        for url in batch:
            print("EXTERNAL AUDIT URL:", url)
        # Bounded concurrency keeps weekly advisory audits within the job
        # timeout without changing the per-URL HEAD/GET confirmation rules.
        with ThreadPoolExecutor(max_workers=min(6, max(1, len(batch)))) as workers:
            results = list(workers.map(lambda url: check_external([url], 1), batch))
        missing = [message for group, _ in results for message in group]
        warnings = [message for _, group in results for message in group]
        for item in missing:
            print("POSSIBLY BROKEN EXTERNAL:", item, file=sys.stderr)
        for item in warnings:
            print("EXTERNAL INCONCLUSIVE:", item, file=sys.stderr)
        print(f"External advisory: checked {len(batch)} of {len(urls)} URLs, rotating offset {offset}; "
              f"{len(missing)} GET-confirmed 404/410 links; {len(warnings)} inconclusive. "
              "This advisory does not certify external link availability.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
