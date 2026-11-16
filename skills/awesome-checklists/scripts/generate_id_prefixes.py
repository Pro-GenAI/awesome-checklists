#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Generate/check every stable ID prefix, numeric interval and owning source path."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

from validate_inventory import EXPECTED

ROOT = Path(__file__).resolve().parents[3]
OUT = Path("lists/references/id-prefix-ranges.json")
FILE = re.compile(r"^\d{2}_[A-Za-z0-9_]+\.md$")
ITEM = re.compile(r"^- \[ \] \*\*([A-Z][A-Z0-9]*)-(\d{3})\*\* \x60P[012]\x60 ")


def build(root: Path) -> dict:
    groups = {}
    ids_seen = set()
    for scope in EXPECTED:
        folder = root / "lists" / ("" if scope == "shared" else scope)
        for path in sorted(p for p in folder.glob("*.md") if p.is_file() and FILE.fullmatch(p.name)):
            rel = path.relative_to(root).as_posix()
            for line in path.read_text(encoding="utf-8").splitlines():
                found = ITEM.match(line)
                if not found:
                    continue
                prefix, numeric = found.groups()
                identifier = prefix + "-" + numeric
                if identifier in ids_seen:
                    raise ValueError("Duplicate stable identifier " + identifier)
                ids_seen.add(identifier)
                group = groups.setdefault(prefix, {"nums": set(), "files": set()})
                group["nums"].add(int(numeric))
                group["files"].add(rel)
    result = {}
    for prefix in sorted(groups):
        group = groups[prefix]
        nums = sorted(group["nums"])
        intervals = []
        first = last = nums[0]
        for current in nums[1:]:
            if current == last + 1:
                last = current
            else:
                intervals.append([first, last])
                first = last = current
        intervals.append([first, last])
        # Checking only the generated JSON would allow a missing ID to be
        # normalized into two ranges. Reject gaps even during regeneration.
        if nums[0] != 1 or len(nums) != nums[-1]:
            missing = sorted(set(range(1, nums[-1] + 1)) - group["nums"])
            sample = ", ".join(f"{prefix}-{n:03d}" for n in missing[:8])
            extra = f" (+{len(missing) - 8} more)" if len(missing) > 8 else ""
            raise ValueError(
                f"{prefix}: noncontiguous stable IDs; missing {sample}{extra}. "
                "Do not delete or renumber existing IDs; document any retirement before changing the contract."
            )
        result[prefix] = {
            "count": len(nums),
            "first": prefix + "-" + str(nums[0]).zfill(3),
            "last": prefix + "-" + str(nums[-1]).zfill(3),
            "ranges": intervals,
            "source_files": sorted(group["files"]),
        }
    return {
        "schema_version": 1,
        "method": "Computed from numbered checklist stable IDs across all four scopes; noncontiguous ranges may be intentional",
        "total_ids": len(ids_seen),
        "total_prefixes": len(result),
        "prefixes": result,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--check", action="store_true", help="Fail when committed register differs from actual sources")
    args = parser.parse_args()
    root = args.repo_root.resolve()
    try:
        register = build(root)
        data = json.dumps(register, indent=2, ensure_ascii=False) + "\n"
        path = root / OUT
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != data:
                raise ValueError("ID prefix register is stale; regenerate and document any intentional ID retirement or move")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(data, encoding="utf-8")
        print(f"ID prefixes: {register['total_prefixes']} prefixes across {register['total_ids']} stable IDs")
    except (OSError, ValueError) as exc:
        print("FAIL: " + str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
