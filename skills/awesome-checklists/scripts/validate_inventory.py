#!/usr/bin/env python3
"""Validate numbered checklist inventory and unique, unchecked stable IDs offline."""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import re
import sys

EXPECTED = {
    "shared": (14, 701),
    "frontend": (20, 684),
    "backend": (35, 1118),
    "AI": (22, 1712),
}
CHECKBOX = re.compile(r"^\s*-\s*\[([ xX])\]\s+(.*)$")
STABLE_ID = re.compile(r"^\*\*([A-Z][A-Z0-9]*-\d{3})\*\* `(P[012])` .+")
NUMBERED = re.compile(r"^(\d{2})_[A-Za-z0-9_]+\.md$")


def validate(root: Path, expected: dict[str, tuple[int, int]] = EXPECTED) -> tuple[Counter, list[str]]:
    errors: list[str] = []
    counts: Counter = Counter()
    seen: dict[str, str] = {}
    for scope, (files_expected, checks_expected) in expected.items():
        folder = root / "lists" / ("" if scope == "shared" else scope)
        files = sorted(p for p in folder.glob("*.md") if NUMBERED.fullmatch(p.name) and p.is_file())
        nums = [int(NUMBERED.fullmatch(p.name).group(1)) for p in files]
        duplicate_prefixes = sorted(n for n, count in Counter(nums).items() if count > 1)
        if duplicate_prefixes:
            errors.append(f"{scope}: duplicate filename numeric prefixes {duplicate_prefixes}; prefixes must not be reused")
        if len(files) != files_expected:
            errors.append(f"{scope}: expected {files_expected} files, found {len(files)}")
        for path in files:
            content = path.read_text(encoding="utf-8")
            if expected is EXPECTED:
                if "review-method.md" not in content or "compliance-crosswalk.md" not in content:
                    errors.append(f"{path.relative_to(root)}: missing shared method/crosswalk links")
                for obsolete in ("## Review details", "## How to use", "## Suggested AI skills for verification",
                                 "## Important warning: reference only"):
                    if obsolete in content:
                        errors.append(f"{path.relative_to(root)}: obsolete repeated section {obsolete}")
            section = ""
            for line_no, line in enumerate(content.splitlines(), 1):
                if line.startswith("## "):
                    section = line.removeprefix("## ").strip()
                match = CHECKBOX.match(line)
                if not match:
                    continue
                checked, remainder = match.groups()
                stable = STABLE_ID.match(remainder)
                location = f"{path.relative_to(root)}:{line_no}"
                if stable is None:
                    if section != "Release gate":
                        errors.append(f"{location}: checklist checkbox lacks a valid stable ID and visible P0/P1/P2 tier")
                    continue
                identifier = stable.group(1)
                counts[scope] += 1
                if checked.lower() == "x":
                    errors.append(f"{location}: upstream template must remain unchecked ({identifier})")
                if identifier in seen:
                    errors.append(f"{location}: duplicate {identifier} (first at {seen[identifier]})")
                else:
                    seen[identifier] = location
        if counts[scope] != checks_expected:
            errors.append(f"{scope}: expected {checks_expected} checks, found {counts[scope]}")
    return counts, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    args = parser.parse_args()
    if not (args.repo_root / "lists").is_dir():
        parser.error(f"No lists/ directory in {args.repo_root}")
    totals, errors = validate(args.repo_root)
    for scope in EXPECTED:
        print(f"{scope}: {EXPECTED[scope][0]} expected files; {totals[scope]} checks")
    print(f"Total checks: {sum(totals.values())}")
    for error in errors:
        print(f"FAIL: {error}", file=sys.stderr)
    if errors:
        return 1
    print("Checklist inventory validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
