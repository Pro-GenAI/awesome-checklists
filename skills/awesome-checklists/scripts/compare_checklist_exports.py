#!/usr/bin/env python3
"""Compare two versioned checklist JSON exports without changing review outcomes.

The inputs come from export_checklists.py and must be from the same scope.
Changes require a new project-specific applicability/evidence decision; this
script does not claim any check was validated or that a change is safe.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

FIELDS = ("criterion_markdown", "priority", "scope", "source", "section")
ID = re.compile(r"^[A-Z][A-Z0-9]*-\d{3}$")
SCOPES = {"all", "shared", "frontend", "backend", "AI"}


def load_catalog(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise ValueError(f"{path}: expected schema_version=1")
    if data.get("scope") not in SCOPES or not isinstance(data.get("items"), list):
        raise ValueError(f"{path}: invalid scope or missing items")
    records = {}
    for item in data["items"]:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str) or not ID.fullmatch(item["id"]):
            raise ValueError(f"{path}: malformed checklist ID")
        ident = item["id"]
        if ident in records:
            raise ValueError(f"{path}: duplicate {ident}")
        if any(not isinstance(item.get(field), str) for field in FIELDS):
            raise ValueError(f"{path}: {ident} has missing or invalid fields")
        if item["priority"] not in ("P0", "P1", "P2"):
            raise ValueError(f"{path}: {ident} has invalid priority")
        records[ident] = {field: item[field] for field in FIELDS}
    if data.get("count") != len(records):
        raise ValueError(f"{path}: count differs from item count")
    return {
        "scope": data["scope"],
        "source_commit": data.get("source_commit"),
        "items": records,
    }


def compare(before: dict, after: dict) -> dict:
    if before["scope"] != after["scope"]:
        raise ValueError("Export scopes differ; compare matching full or scope-specific catalogs")
    old, new = before["items"], after["items"]
    added = sorted(set(new) - set(old))
    removed = sorted(set(old) - set(new))
    changed = []
    for ident in sorted(set(old) & set(new)):
        fields = {field: {"before": old[ident][field], "after": new[ident][field]}
                  for field in FIELDS if old[ident][field] != new[ident][field]}
        if fields:
            changed.append({
                "id": ident,
                "changed_fields": fields,
                "review_needed": any(field in fields for field in
                                     ("criterion_markdown", "priority", "scope", "source")),
            })
    return {
        "schema_version": 1,
        "scope": before["scope"],
        "before_source_commit": before["source_commit"],
        "after_source_commit": after["source_commit"],
        "summary": {
            "added": len(added), "removed": len(removed),
            "changed": len(changed),
            "needs_review": len(added) + len(removed)
                            + sum(change["review_needed"] for change in changed),
        },
        "added": [{"id": ident, "item": new[ident]} for ident in added],
        "removed": [{"id": ident, "item": old[ident]} for ident in removed],
        "changed": changed,
    }


def markdown(report: dict) -> str:
    summary = report["summary"]
    lines = [
        "# Checklist-source delta report",
        "",
        "Before source revision: " + str(report["before_source_commit"] or "not provided"),
        "After source revision: " + str(report["after_source_commit"] or "not provided"),
        "Scope: " + report["scope"],
        "",
        f"**Added:** {summary['added']} · **Removed:** {summary['removed']} · "
        f"**Changed:** {summary['changed']} · **Requires review:** {summary['needs_review']}",
        "",
        "Changes are candidates for re-assessment, not automatic PASS/FAIL results. "
        "Preserve prior review evidence and decisions with their original source SHA; "
        "evaluate affected criteria under the new source revision.",
        "",
        "| Checklist ID | Change | Fields affected | Next action |",
        "| --- | --- | --- | --- |",
    ]
    for item in report["added"]:
        lines.append(f"| {item['id']} | Added | new control | Determine applicability and collect evidence |")
    for item in report["removed"]:
        lines.append(f"| {item['id']} | Removed | retired/unavailable in new export | "
                     "Retain historic evidence; check ID history before migration |")
    for item in report["changed"]:
        fields = ", ".join(item["changed_fields"])
        action = ("Re-evaluate applicability and current evidence"
                  if item["review_needed"] else "Confirm section-only relocation")
        lines.append(f"| {item['id']} | Changed | {fields} | {action} |")
    if not (report["added"] or report["removed"] or report["changed"]):
        lines.append("| — | None | — | Retain the original source SHA with the review |")
    lines.extend(["", "For exact before/after values, rerun with --format json.", ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--before", required=True, type=Path, help="Pinned baseline export JSON")
    parser.add_argument("--after", required=True, type=Path, help="New export JSON")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--output", type=Path, help="Write report to a path instead of stdout")
    parser.add_argument("--fail-on-review-needed", action="store_true",
                        help="Return status 2 for actionable deltas, suitable for downstream CI")
    args = parser.parse_args()
    try:
        report = compare(load_catalog(args.before), load_catalog(args.after))
        value = (json.dumps(report, indent=2, ensure_ascii=False) + "\n"
                 if args.format == "json" else markdown(report))
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(value, encoding="utf-8")
        else:
            print(value, end="")
        return 2 if args.fail_on_review_needed and report["summary"]["needs_review"] else 0
    except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
        print("compare_checklist_exports: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
