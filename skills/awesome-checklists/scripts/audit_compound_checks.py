#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""List possible multi-verification checklist items for HUMAN editorial review.

Flags are heuristic signals, not proof that a check should be split. No files are edited.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

from validate_inventory import EXPECTED

CHECK = re.compile(r"^\s*-\s*\[ \]\s+\*\*([A-Z][A-Z0-9]*-\d{3})\*\*\s+\`P[012]\`\s+(.+)$")
NAME = re.compile(r"^\d{2}_[A-Za-z0-9_]+\.md$")
CLAUSES = re.compile(r";\s*\S")
# Distinct security control families often create several independent PASS
# conditions even without conjunctions or semicolons. Editorial triage only.
FAMILIES = (
    r"\bauthoriz\w*", r"\brate[\s-]*limit\w*", r"\bschema validat\w*",
    r"\breplay control\w*", r"\bsafe error\w*", r"\binput\w* validat\w*",
    r"\boutput\w* (?:safely |context[- ]appropriately )?encod\w*",
    r"\binjection\b", r"\bdeserializ\w*",
)


def compound_signals(criterion: str) -> list[str]:
    signals = []
    if CLAUSES.search(criterion):
        signals.append("multiple semicolon-delimited clauses")
    if ACTION.search(criterion):
        signals.append("multiple explicit verification verbs")
    if len(criterion.split()) >= 55:
        signals.append("long criterion (55+ words)")
    families = [pattern for pattern in FAMILIES if re.search(pattern, criterion, re.I)]
    if len(families) >= 3:
        signals.append("three or more distinct security-control families")
    return signals
ACTION = re.compile(r"\b(?:and (?:verify|test|enforce|record|review|validate|confirm|track|monitor|ensure|reject|check|require|perform|assess))\b", re.I)


def candidates(root: Path) -> list[dict]:
    matches = []
    for scope in EXPECTED:
        folder = root / "lists" / ("" if scope == "shared" else scope)
        for file in sorted(p for p in folder.glob("*.md") if NAME.fullmatch(p.name)):
            for lineno, line in enumerate(file.read_text(encoding="utf-8").splitlines(), 1):
                m = CHECK.match(line)
                if not m:
                    continue
                identifier, criterion = m.groups()
                signals = compound_signals(criterion)
                if signals:
                    matches.append({
                        "id": identifier,
                        "path": file.relative_to(root).as_posix(),
                        "line": lineno,
                        "signals": signals,
                        "criterion": criterion,
                        "status": "requires-human-editorial-review",
                    })
    return matches


def filter_core_candidates(root: Path, items: list[dict]) -> list[dict]:
    """Keep candidates from the curated Core 50 without treating flags as validation."""
    curated = json.loads((root / "lists" / "references" / "core-50.json").read_text(encoding="utf-8"))
    identifiers = [row["id"] for row in curated["checks"]]
    if len(identifiers) != 50 or len(set(identifiers)) != 50:
        raise ValueError("Core 50 manifest must contain exactly 50 unique IDs")
    return [item for item in items if item["id"] in set(identifiers)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--output", type=Path, help="JSON result file; stdout if not specified")
    parser.add_argument("--core-only", action="store_true", help="triage only the manually curated Core 50 IDs")
    args = parser.parse_args()
    items = candidates(args.repo_root)
    if args.core_only:
        items = filter_core_candidates(args.repo_root, items)
    result = {
        "schema_version": 1,
        "scope": "Core 50 only" if args.core_only else "all 91 numbered checklist files",
        "meaning": "Potential compound wording for editorial review only; not a security severity or confirmed duplicate",
        "candidates": items,
        "count": len(items),
    }
    data = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(data, encoding="utf-8")
    else:
        print(data, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
