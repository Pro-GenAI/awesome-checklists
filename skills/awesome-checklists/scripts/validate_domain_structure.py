#!/usr/bin/env python3
"""Validate cross-scope AGENT IDs and section links; structural check, not audit."""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from validate_inventory import EXPECTED

CONTRACT = "lists/references/agent-domain-contract.json"
CHECK = re.compile(r"^- \[ \] \*\*AGENT-(\d{3})\*\* \x60P[012]\x60 (.+)$", re.MULTILINE)
FILENAME = re.compile(r"^\d{2}_[A-Za-z0-9_]+\.md$")
LINK = re.compile(r"\]\(([^)\s]+)\)")


def slug(heading: str) -> str:
    return re.sub(r"[^a-z0-9\- ]", "", heading.lower()).strip().replace(" ", "-")


def validate(root: Path, contract_path: str = CONTRACT) -> list[str]:
    errors = []
    root = root.resolve()
    try:
        contract = json.loads((root / contract_path).read_text(encoding="utf-8"))
        if contract["schema_version"] != 1 or contract["domain"] != "AGENT":
            raise ValueError("Unknown domain contract schema/domain")
        low, high = contract["contiguous_numeric_ids"]
        if not (isinstance(low, int) and isinstance(high, int) and 1 <= low <= high <= 999):
            raise ValueError("Invalid contiguous numeric bounds")
        slices = contract["scope_slices"]
        if not isinstance(slices, list) or len(slices) < 2:
            raise ValueError("Cross-scope domain requires two or more slices")
    except (OSError, ValueError, TypeError, KeyError) as exc:
        return [f"Domain contract unreadable/invalid: {exc}"]

    expected, contracts = {}, {}
    for item in slices:
        path = item["path"]
        if path in contracts:
            errors.append(f"Repeated domain slice path: {path}")
        contracts[path] = item
        if not item.get("ranges"):
            errors.append(f"Missing declared ID ranges for {path}")
        for first, last in item.get("ranges", []):
            if not 1 <= first <= last <= 999:
                errors.append(f"{path}: invalid ID range {first}..{last}")
                continue
            for number in range(first, last + 1):
                if number in expected:
                    errors.append(f"AGENT-{number:03d}: overlapping owners in {expected[number]} and {path}")
                expected[number] = path

    required = set(range(low, high + 1))
    if set(expected) != required:
        errors.append(f"Contract ownership continuity: missing={sorted(required - set(expected))[:12]} "
                      f"extra={sorted(set(expected) - required)[:12]}")

    actual, occurrences = {}, Counter()
    for scope in EXPECTED:
        folder = root / "lists" / ("" if scope == "shared" else scope)
        for source in sorted(p for p in folder.glob("*.md") if p.is_file() and FILENAME.fullmatch(p.name)):
            relative = source.relative_to(root).as_posix()
            content = source.read_text(encoding="utf-8")
            for m in CHECK.finditer(content):
                number = int(m.group(1))
                occurrences[number] += 1
                actual[number] = relative
    for number, count in sorted(occurrences.items()):
        if count != 1:
            errors.append(f"AGENT-{number:03d}: appears {count} times instead of once")
    if set(actual) != required:
        errors.append(f"AGENT global continuity: missing={sorted(required - set(actual))[:12]} "
                      f"unexpected={sorted(set(actual) - required)[:12]}")
    for number, path in expected.items():
        if actual.get(number) is not None and actual[number] != path:
            errors.append(f"AGENT-{number:03d}: expected in {path}, found {actual[number]}")

    for path, item in contracts.items():
        source = root / path
        if not source.is_file():
            errors.append(f"Missing declared domain file {path}")
            continue
        content = source.read_text(encoding="utf-8")
        headings = {line[3:].strip() for line in content.splitlines() if line.startswith("## ")}
        for section in item.get("required_sections", []):
            if section not in headings:
                errors.append(f"{path}: missing required section ## {section}")
        links = set(LINK.findall(content))
        for link in item.get("required_links", []):
            if link not in links:
                errors.append(f"{path}: missing cross-scope link {link}")
                continue
            target = urlsplit(link)
            if target.scheme or target.netloc or not target.path:
                errors.append(f"{path}: link must be repository-relative: {link}")
                continue
            targetfile = (source.parent / unquote(target.path)).resolve()
            if not targetfile.is_relative_to(root) or not targetfile.is_file():
                errors.append(f"{path}: unresolved cross-scope target {link}")
                continue
            if target.fragment:
                target_text = targetfile.read_text(encoding="utf-8")
                anchors = [slug(line[3:].strip()) for line in target_text.splitlines() if line.startswith("## ")]
                if unquote(target.fragment) not in anchors:
                    errors.append(f"{path}: missing referenced section anchor {link}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    args = parser.parse_args()
    errors = validate(args.repo_root)
    for error in errors:
        print("FAIL:", error, file=sys.stderr)
    if not errors:
        low, high = json.loads((args.repo_root.resolve() / CONTRACT).read_text(encoding="utf-8"))["contiguous_numeric_ids"]
        print(f"AGENT domain: {high - low + 1} IDs continuous across two files; required sections and links resolve.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
