#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Export source checklist criteria as machine-readable JSON, with optional review template.

All judgments are project-specific. The repository's checkboxes never represent review results.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

from validate_inventory import EXPECTED, validate as validate_inventory

ROOT = Path(__file__).resolve().parents[3]
CORE = Path("lists/references/core-50.json")
LINE = re.compile(r"^\s*-\s*\[([ xX])\]\s+\*\*([A-Z][A-Z0-9]*-\d{3})\*\*\s+(.+)$")
FILENAME = re.compile(r"^\d{2}_[A-Za-z0-9_]+\.md$")
COMMIT = re.compile(r"^[a-fA-F0-9]{40}$")


def export(root: Path, scope: str, only_core: bool, source_commit: str | None) -> dict:
    core = json.loads((root / CORE).read_text(encoding="utf-8"))
    if core.get("schema_version") != 1 or not isinstance(core.get("checks"), list):
        raise ValueError("Invalid curated core-50 metadata schema")
    selected: dict[str, dict] = {}
    for item in core["checks"]:
        identifier = item["id"]
        if identifier in selected:
            raise ValueError(f"Duplicate curated ID: {identifier}")
        if item.get("priority") not in {"P0", "P1", "P2"}:
            raise ValueError(f"Invalid priority for {identifier}")
        selected[identifier] = item
    if len(selected) != 50:
        raise ValueError(f"Expected 50 curated IDs, found {len(selected)}")

    counts, errors = validate_inventory(root)
    if errors:
        raise ValueError("Source inventory failed validation: " + "; ".join(errors[:5]))
    expected_total = sum(value[1] for value in EXPECTED.values())
    if sum(counts.values()) != expected_total:
        raise ValueError("Unexpected source check count")

    entries = []
    seen: set[str] = set()
    for domain in EXPECTED:
        if scope != "all" and domain != scope:
            continue
        folder = root / "lists" / ("" if domain == "shared" else domain)
        for file in sorted(p for p in folder.glob("*.md") if FILENAME.fullmatch(p.name) and p.is_file()):
            relative = file.relative_to(root).as_posix()
            section = ""
            for number, line in enumerate(file.read_text(encoding="utf-8").splitlines(), 1):
                if line.startswith("## "):
                    section = line[3:].strip()
                match = LINE.match(line)
                if match is None:
                    continue
                checked, identifier, marked_criterion = match.groups()
                tier_match = re.fullmatch(r"`(P[012])` (.+)", marked_criterion)
                if tier_match is None:
                    raise ValueError(f"Missing or invalid visible priority for {identifier} in {relative}")
                tier, criterion = tier_match.groups()
                if checked.lower() == "x":
                    raise ValueError(f"Checked source item: {identifier} in {relative}")
                if identifier in seen:
                    raise ValueError(f"Duplicate checklist ID {identifier}")
                seen.add(identifier)
                curated = selected.get(identifier)
                if curated is not None and (
                    curated.get("source") != relative
                    or curated.get("scope") != domain
                    or curated.get("criterion") != criterion
                ):
                    raise ValueError(f"Curated metadata drift for {identifier}; update core-50.json")
                if curated is not None and curated["priority"] != tier:
                    raise ValueError(f"Curated priority drift for {identifier}: {tier} versus {curated['priority']}")
                if only_core and curated is None:
                    continue
                entries.append({
                    "id": identifier,
                    "scope": domain,
                    "source": relative,
                    "line": number,
                    "section": section,
                    "criterion_markdown": criterion,
                    "priority": tier,
                    "priority_basis": "curated-core-50" if curated else "provisional-text-triage",
                })
    missing = set(selected) - seen if scope == "all" else {
        identifier for identifier, item in selected.items()
        if item["scope"] == scope and identifier not in seen
    }
    if missing:
        raise ValueError(f"Curated IDs absent from source: {sorted(missing)}")
    if only_core and scope == "all" and len(entries) != 50:
        raise ValueError(f"Core selection should contain 50 checks, found {len(entries)}")
    if not only_core and len(entries) != (expected_total if scope == "all" else counts[scope]):
        raise ValueError("Exported criteria count differs from validated source inventory")
    return {
        "schema_version": 1,
        "generated_from": "unchecked source Markdown",
        "source_commit": source_commit,
        "scope": scope,
        "count": len(entries),
        "prioritized_count": sum(e["priority"] is not None for e in entries),
        "items": entries,
    }


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--scope", choices=("all", *EXPECTED), default="all")
    parser.add_argument("--only-core", action="store_true", help="Export only the 50 curated starter checks")
    parser.add_argument("--source-commit", help="Optional 40-character SHA for provenance, e.g. git rev-parse HEAD")
    parser.add_argument("--output", type=Path, help="Write catalog JSON to this path; stdout otherwise")
    parser.add_argument("--review-template", type=Path, help="Also write a separate project review status template")
    args = parser.parse_args()
    if args.source_commit and not COMMIT.fullmatch(args.source_commit):
        parser.error("--source-commit requires a 40-character hexadecimal Git SHA")
    try:
        catalog = export(args.repo_root.resolve(), args.scope, args.only_core, args.source_commit)
        if args.output:
            write_json(args.output, catalog)
        else:
            print(json.dumps(catalog, ensure_ascii=False, indent=2))
        if args.review_template:
            template = {
                "schema_version": 1,
                "source_commit": args.source_commit,
                "project": "",
                "project_version": "",
                "reviewer": "",
                "review_date": "",
                "note": "Unverified by default. PASS requires direct evidence, N/A a rationale; decisions require human approval.",
                "results": [{
                    "id": item["id"],
                    "status": "UNKNOWN",
                    "evidence": [],
                    "owner": "",
                    "notes": "Not reviewed",
                } for item in catalog["items"]],
            }
            write_json(args.review_template, template)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"export_checklists: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
