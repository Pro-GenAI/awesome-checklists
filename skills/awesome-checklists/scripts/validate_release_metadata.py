#!/usr/bin/env python3
"""Check public repository metadata, source pin, spec references and README scope.

Static content checks are reproducible offline. GitHub Actions workflows are disabled.
The optional ancestry flag verifies pinned-source reachability in a full local checkout.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
RELEASE = Path("skills/awesome-checklists/references/source-release.json")
SHA = re.compile(r"^[0-9a-f]{40}$")


PREFIX_ROW = re.compile(
    r"^\|\s*\d+\s*\|\s*\x60[^\x60]+\.md\x60\s*\|\s*\x60([A-Z][A-Z0-9]*)\x60\s*\|\s*(\d+)\s*\|",
    re.MULTILINE,
)


def check_prefix_table(content: str, prefixes: dict) -> list[str]:
    """Reject stale source-domain totals in live scope inventory tables."""
    errors = []
    rows = PREFIX_ROW.findall(content)
    covered = {prefix for prefix, _ in rows}
    for prefix in sorted(set(prefixes) - covered):
        errors.append(f"Scope inventory omits domain prefix {prefix}")
    for prefix, displayed in rows:
        if prefix not in prefixes:
            errors.append(f"Scope inventory references unknown domain prefix {prefix}")
        elif int(displayed) != prefixes[prefix]["count"]:
            errors.append(
                f"Scope inventory {prefix}: table says {displayed}, "
                f"source ID range register says {prefixes[prefix]['count']}"
            )
    return errors


def inspect(root: Path, is_private: str | None = None) -> list[str]:
    errors = []
    try:
        meta = json.loads((root / RELEASE).read_text(encoding="utf-8"))
        if meta["schema_version"] != 1 or meta["repository"] != "Pro-GenAI/awesome-checklists":
            errors.append("Unknown source-release schema/repository")
        if meta["visibility"] != "public":
            errors.append("Repository metadata must describe a public repository")
        if not SHA.fullmatch(meta["checklist_source_sha"]):
            errors.append("Default checklist source must be an immutable 40-character SHA")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", meta["mcp_stable_revision"]):
            errors.append("MCP specification revision must be YYYY-MM-DD")
    except (OSError, ValueError, TypeError, KeyError) as exc:
        return ["Invalid source-release metadata: " + str(exc)]

    if is_private in ("true", "false"):
        if (is_private == "true") != (meta["visibility"] == "private"):
            errors.append("GitHub repository private flag disagrees with source-release metadata")
    elif is_private not in (None, ""):
        errors.append("Unexpected GITHUB_IS_PRIVATE value: " + is_private)

    readme = (root / "README.md").read_text(encoding="utf-8")
    agents = (root / "AGENTS.md").read_text(encoding="utf-8")
    ai_agents = (root / "lists/AI/11_AI_Agents_and_Tool_Orchestration.md").read_text(encoding="utf-8")
    helper = (root / "skills/awesome-checklists/scripts/checklists.py").read_text(encoding="utf-8")
    inventory_doc = (root / "docs/agents/scope-inventory.md").read_text(encoding="utf-8")
    resources_doc = (root / "docs/agents/resources-and-tooling.md").read_text(encoding="utf-8")
    prefix_register = json.loads((root / "lists/references/id-prefix-ranges.json").read_text(encoding="utf-8"))
    errors.extend(check_prefix_table(inventory_doc, prefix_register["prefixes"]))
    if re.search(r"\bno (?:pull request|PR) is required\b", resources_doc, re.IGNORECASE):
        errors.append("Live resource guide contradicts contributor review-first policy")
    if "**Public repository:**" not in readme:
        errors.append("README must explicitly describe public repository access")
    if re.search(r"currently private|no CI workflow is active", readme + "\n" + agents, re.I):
        errors.append("Current entry-point documents include obsolete private/CI instructions")
    starter = readme.find("## Start with 25–50 checks")
    skill_section = readme.find("## Agent skill for Codex and Claude Code")
    if starter == -1 or skill_section == -1 or starter > skill_section:
        errors.append("README must lead with bounded review starters")
    for ref in ("lists/references/core-50.md", "lists/references/minimum-viable-by-scope.md"):
        if ref not in readme:
            errors.append("README missing starter resource " + ref)
    if meta["mcp_stable_revision"] not in ai_agents:
        errors.append("AI Agent checklist and release metadata MCP versions differ")
    if "SOURCE_RELEASE.read_text" not in helper or '["checklist_source_sha"]' not in helper:
        errors.append("Skill helper must read default SHA from bundled source-release metadata")
    if "docs/agents/contributor-workflows.md" not in agents:
        errors.append("AGENTS.md must link current workflow")
    return errors


def verify_pin_ancestry(root: Path, head_ref: str = "main") -> list[str]:
    """Verify that the bundled immutable source commit is reachable from local main."""
    try:
        pin = json.loads((root / RELEASE).read_text(encoding="utf-8"))["checklist_source_sha"]
        if not SHA.fullmatch(pin):
            return ["Pinned checklist SHA is invalid"]
    except (OSError, ValueError, TypeError, KeyError) as exc:
        return ["Cannot read bundled source pin: " + str(exc)]

    def git(*args):
        return subprocess.run(["git", "-C", str(root), *args],
                              capture_output=True, text=True, timeout=15, check=False)
    try:
        if git("rev-parse", "--is-inside-work-tree").stdout.strip() != "true":
            return ["Pin verification requires a local Git checkout"]
        if git("rev-parse", "--is-shallow-repository").stdout.strip() == "true":
            return ["Pin verification needs full Git history; fetch --unshallow"]
        if git("cat-file", "-e", pin + "^{commit}").returncode:
            return ["Pinned source commit is missing locally; fetch full history"]
        if git("rev-parse", "--verify", head_ref + "^{commit}").returncode:
            return ["Main ref unavailable locally: " + head_ref]
        if git("merge-base", "--is-ancestor", pin, head_ref).returncode:
            return ["Pinned source SHA is not an ancestor of " + head_ref]
        return []
    except (OSError, subprocess.TimeoutExpired) as exc:
        return ["Cannot run pin verification: " + type(exc).__name__]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--verify-pin-ancestry", action="store_true",
                        help="check pinned source is an ancestor of local main (requires full history)")
    parser.add_argument("--head-ref", default="main", help="local branch to check")
    args = parser.parse_args()
    errors = inspect(args.repo_root, os.environ.get("GITHUB_IS_PRIVATE"))
    if args.verify_pin_ancestry:
        errors.extend(verify_pin_ancestry(args.repo_root, args.head_ref))
    for error in errors:
        print("FAIL: " + error, file=sys.stderr)
    if not errors:
        print("Source-release metadata: visibility, pinned SHA, spec and entry points agree")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
