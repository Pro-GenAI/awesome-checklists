#!/usr/bin/env python3
"""Validate drop-in Markdown and JSON parity against canonical stable-ID sources."""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CHECK = re.compile(r"^- \[ \] \*\*([A-Z][A-Z0-9]*-\d{3})\*\* — ", re.M)


def validate(root: Path) -> list[str]:
    problems: list[str] = []
    data = json.loads((root / "docs/checklists/catalog.json").read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        problems.append("Unexpected catalog schema_version")
    seen: set[str] = set()
    for group in data["checklists"]:
        slug = group["slug"]
        stage = group["stage"]
        path = root / "docs/checklists" / (slug + ".md")
        markdown = path.read_text(encoding="utf-8")
        ids = []
        for item in group["items"]:
            item_id = item["id"]
            if item_id in seen:
                problems.append("Duplicate catalog ID: " + item_id)
            seen.add(item_id)
            ids.append(item_id)
            if item["severity"] != "project-defined":
                problems.append(item_id + ": severity must remain project-defined")
            if item["priority_hint"] not in ("P0", "P1", "P2"):
                problems.append(item_id + ": invalid priority hint")
            automation = item["automated_check"]
            if automation is not None and (automation.get("status") != "integration-required" or not automation.get("suggested_signal")):
                problems.append(item_id + ": automation must be a non-executable integration hint")
            source = root / item["source"]
            if not source.is_file():
                problems.append(item_id + ": missing canonical source")
            elif f"**{item_id}** `{item['priority_hint']}`" not in source.read_text(encoding="utf-8"):
                problems.append(item_id + ": source ID/priority does not match")
            expected = f"- [ ] **{item_id}** — {item['label']}. [Canonical check](../../{item['source']}). *Why:* {item['why']}."
            if expected not in markdown:
                problems.append(item_id + ": Markdown/JSON description mismatch")
        if stage not in ("design-and-implementation", "data-and-retrieval", "agent-runtime", "verification-and-operations", "release"):
            problems.append(slug + ": unknown stage")
        actual = CHECK.findall(markdown)
        if actual != ids:
            problems.append(slug + ": Markdown ID order/list differs from catalog")
    return problems


if __name__ == "__main__":
    errors = validate(ROOT)
    for error in errors:
        print("FAIL: " + error, file=sys.stderr)
    print(f"Lifecycle catalog: {len(errors)} problems")
    raise SystemExit(bool(errors))
