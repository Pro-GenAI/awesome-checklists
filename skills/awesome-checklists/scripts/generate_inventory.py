#!/usr/bin/env python3
"""Regenerate/check the machine-verifiable current checklist inventory."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

from validate_inventory import EXPECTED, validate

ROOT = Path(__file__).resolve().parents[3]
OUT = Path("lists/references/inventory.json")
PATTERN = re.compile(r"^\d{2}_[A-Za-z0-9_]+\.md$")
CHECK = re.compile(r"^- \[ \] \*\*[A-Z][A-Z0-9]*-\d{3}\*\* \x60P[012]\x60 ")


def generate(root: Path) -> dict:
    scopes = {}
    for scope in EXPECTED:
        folder = root / "lists" / ("" if scope == "shared" else scope)
        files = sorted(x for x in folder.glob("*.md") if x.is_file() and PATTERN.fullmatch(x.name))
        count = sum(1 for f in files for line in f.read_text(encoding="utf-8").splitlines()
                    if CHECK.match(line))
        scopes[scope] = {"files": len(files), "checks": count}
    return {
        "schema_version": 1,
        "method": "Computed from numbered source files and visible stable IDs; excludes references and gates",
        "total_files": sum(v["files"] for v in scopes.values()),
        "total_checks": sum(v["checks"] for v in scopes.values()),
        "scopes": scopes,
    }


def verify_readme(root: Path, manifest: dict) -> list[str]:
    content = (root / "README.md").read_text(encoding="utf-8")
    header = re.search(r"\*\*(\d+) scoped checklists · ([\d,]+) unique checks ·", content)
    if not header or (int(header.group(1)), int(header.group(2).replace(",", ""))) != (
        manifest["total_files"], manifest["total_checks"]
    ):
        return ["README headline counts differ from generated inventory"]
    return []


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo-root", type=Path, default=ROOT)
    p.add_argument("--check", action="store_true", help="Fail when committed inventory is stale")
    args = p.parse_args()
    root = args.repo_root.resolve()
    errors = []
    manifest = generate(root)
    totals, validated = validate(root)
    errors.extend(validated)
    if sum(totals.values()) != manifest["total_checks"]:
        errors.append("Source inventory and validator counts disagree")
    errors.extend(verify_readme(root, manifest))
    output = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    target = root / OUT
    if args.check:
        if not target.exists() or target.read_text(encoding="utf-8") != output:
            errors.append("Committed inventory.json is stale; regenerate before committing")
    elif not errors:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(output, encoding="utf-8")
        print("Generated " + str(OUT))
    for message in errors:
        print("FAIL: " + message, file=sys.stderr)
    print(f"Inventory: {manifest['total_files']} files, {manifest['total_checks']} checks")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
