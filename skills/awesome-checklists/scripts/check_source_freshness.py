#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Flag outdated checklist source reviews; dates are not proof links remain valid."""
from __future__ import annotations

import argparse
from datetime import date, datetime
from pathlib import Path
import re
import sys

from validate_inventory import EXPECTED

ROOT = Path(__file__).resolve().parents[3]
FILE = re.compile(r"^\d{2}_[A-Za-z0-9_]+\.md$")
SOURCE_DATE = re.compile(r"^\*\*Source review date:\*\* (\d{4}-\d{2}-\d{2})\b", re.M)


def inspect(root: Path, *, today: date, max_age_days: int = 180) -> tuple[list[str], list[str]]:
    failures, warnings = [], []
    for scope in EXPECTED:
        folder = root / "lists" / ("" if scope == "shared" else scope)
        for path in sorted(p for p in folder.glob("*.md") if FILE.fullmatch(p.name) and p.is_file()):
            rel = path.relative_to(root).as_posix()
            matches = SOURCE_DATE.findall(path.read_text(encoding="utf-8"))
            if len(matches) != 1:
                failures.append(f"{rel}: expected one YYYY-MM-DD source review date, found {len(matches)}")
                continue
            try:
                when = date.fromisoformat(matches[0])
            except ValueError:
                failures.append(f"{rel}: invalid source review date {matches[0]}")
                continue
            age = (today - when).days
            if age < 0:
                failures.append(f"{rel}: source review date is in the future: {matches[0]}")
            elif age > max_age_days:
                warnings.append(f"{rel}: source review is {age} days old (threshold {max_age_days})")
    return failures, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--max-age-days", type=int, default=180)
    parser.add_argument("--fail-stale", action="store_true", help="Treat old source reviews as CI failures")
    parser.add_argument("--today", type=date.fromisoformat, default=None, help="YYYY-MM-DD override for offline testing")
    args = parser.parse_args()
    if args.max_age_days < 1:
        parser.error("--max-age-days must be positive")
    bad, stale = inspect(args.repo_root.resolve(), today=args.today or date.today(), max_age_days=args.max_age_days)
    for msg in bad:
        print("FAIL: " + msg, file=sys.stderr)
    for msg in stale:
        print("STALE: " + msg, file=sys.stderr)
    print(f"Source freshness: {len(bad)} invalid/missing dates; {len(stale)} stale files; threshold {args.max_age_days} days")
    return 1 if bad or (args.fail_stale and stale) else 0


if __name__ == "__main__":
    raise SystemExit(main())
