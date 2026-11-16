#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Generate a bounded, project-specific UNKNOWN-first Markdown or JSON review.

This is a deterministic triage aid, not an audit, severity determination, or
substitute for evaluating all applicable release gates and legal obligations.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import subprocess
import sys

from export_checklists import COMMIT, ROOT, export

PROFILES = {
    "startup": {
        "description": "First launch: security, user journeys, API integrity, testing and release",
        "default_scopes": ["shared", "frontend", "backend"],
        "scope_weights": {"shared": 4, "frontend": 3, "backend": 4, "AI": 2},
        "anchors": ["SEC-007", "SEC-012", "SEC-021", "SEC-102", "A11Y-094", "APID-079"],
        "domains": {"SEC": 35, "TST": 30, "LAUNCH": 30, "APID": 22, "A11Y": 20, "UX": 15},
        "keywords": ["release", "authentication", "authorization", "backup", "critical", "production", "incident", "deploy", "accessibility", "recover"],
    },
    "regulated": {
        "description": "Higher assurance: data protection, access, traceability and oversight",
        "default_scopes": ["shared", "frontend", "backend"],
        "scope_weights": {"shared": 4, "frontend": 2, "backend": 5, "AI": 3},
        "anchors": ["SEC-007", "SEC-009", "SEC-102", "SEC-103", "SEC-023", "SEC-024", "SEC-031", "SEC-111"],
        "domains": {"SEC": 45, "LEG": 40, "DATA": 35, "AIG": 35, "AGENT": 30, "A11Y": 15},
        "keywords": ["personal data", "consent", "retention", "authorization", "audit", "evidence", "privacy", "regulatory", "access", "incident"],
    },
    "internal-tool": {
        "description": "Internal application: identity, roles, sensitive data and reliable workflows",
        "default_scopes": ["shared", "backend", "frontend"],
        "scope_weights": {"shared": 4, "frontend": 2, "backend": 5, "AI": 2},
        "anchors": ["SEC-007", "SEC-009", "SEC-102", "SEC-110", "SEC-111", "SEC-020", "APID-079"],
        "domains": {"SEC": 40, "APID": 30, "DATA": 25, "TST": 25, "AGENT": 20},
        "keywords": ["least privilege", "role", "access", "audit", "integration", "recovery", "backup", "deploy", "permission", "authentication"],
    },
}
PRIORITY_POINTS = {"P0": 90, "P1": 35, "P2": 0}
SCOPES = {"shared", "frontend", "backend", "AI"}


def item_score(item: dict, profile: dict) -> int:
    phrase = item["criterion_markdown"].lower()
    domain = item["id"].split("-", 1)[0]
    return (
        (PRIORITY_POINTS[item["priority"]] + 65 if item["priority_basis"] == "curated-core-50" else 0)
        + profile["domains"].get(domain, 0)
        + min(30, sum(10 for word in profile["keywords"] if word in phrase))
    )


def select(catalog: dict, *, profile: str, scopes: list[str] | None = None,
           domains: list[str] | None = None, size: int = 50,
           include: list[str] | None = None, exclude: list[str] | None = None) -> dict:
    if profile not in PROFILES:
        raise ValueError(f"Unknown profile: {profile}")
    if not 25 <= size <= 100:
        raise ValueError("--size must be between 25 and 100")
    config = PROFILES[profile]
    enabled_scopes = set(scopes or config["default_scopes"])
    if not enabled_scopes <= SCOPES:
        raise ValueError(f"Invalid scopes: {sorted(enabled_scopes - SCOPES)}")
    domain_filter = {s.upper() for s in (domains or [])}
    if any(not re.fullmatch(r"[A-Z][A-Z0-9]*", s) for s in domain_filter):
        raise ValueError("Domain names must be ID prefixes such as SEC, A11Y, AGENT")
    include = list(dict.fromkeys(include or []))
    excluded = set(exclude or [])
    if excluded.intersection(include):
        raise ValueError("The same ID cannot be included and excluded")
    universe = {item["id"]: item for item in catalog["items"]}
    unknown = (set(include) | excluded) - set(universe)
    if unknown:
        raise ValueError(f"Unknown checklist IDs: {sorted(unknown)}")

    pool = {
        item["id"]: item
        for item in catalog["items"]
        if item["scope"] in enabled_scopes
        and (not domain_filter or item["id"].split("-", 1)[0] in domain_filter)
        and item["id"] not in excluded
    }
    outside = set(include) - set(pool)
    if outside:
        raise ValueError(f"Requested IDs excluded by scope/domain filters: {sorted(outside)}")
    if len(pool) < size:
        raise ValueError(f"Only {len(pool)} eligible checks, cannot select {size}; widen scopes/domains or reduce size")
    if len(include) > size:
        raise ValueError(f"{len(include)} manually included IDs exceed --size={size}")

    selected: list[dict] = []
    seen = set()

    def add(identifier: str) -> None:
        if identifier in pool and identifier not in seen and len(selected) < size:
            selected.append(pool[identifier])
            seen.add(identifier)

    for identifier in include:
        add(identifier)
    for identifier in config["anchors"]:
        add(identifier)

    remaining = {scope: [] for scope in enabled_scopes}
    for item in pool.values():
        if item["id"] not in seen:
            remaining[item["scope"]].append(item)
    for bucket in remaining.values():
        bucket.sort(key=lambda item: (-item_score(item, config), item["id"]))
    counts = Counter(item["scope"] for item in selected)
    while len(selected) < size:
        ready = [scope for scope in remaining if remaining[scope]]
        if not ready:
            raise ValueError("Not enough eligible checks after exclusions")
        # Weighted fair selection stops a large source domain consuming the
        # entire shortlist. Lexical ties make the output stable.
        chosen_scope = min(
            ready,
            key=lambda scope: (counts[scope] / config["scope_weights"].get(scope, 1), scope),
        )
        chosen = remaining[chosen_scope].pop(0)
        selected.append(chosen)
        seen.add(chosen["id"])
        counts[chosen_scope] += 1
    return {
        "schema_version": 1,
        "profile": profile,
        "profile_description": config["description"],
        "source_commit": catalog["source_commit"],
        "selection_method": "profile anchors; curated Core 50 tiers only; domain and keyword weighting; weighted scope balancing; provisional tiers are never scored",
        "warning": "Triage suggestion only. All items UNKNOWN; not a minimum compliance profile, audit result, or release approval.",
        "scope_filter": sorted(enabled_scopes),
        "domain_filter": sorted(domain_filter),
        "count": len(selected),
        "items": [
            {
                **item, "status": "UNKNOWN", "owner": "", "evidence": [],
                "notes": "", "exception": "", "project_priority": None,
            }
            for item in selected
        ],
    }


def markdown(payload: dict, project: str, release: str) -> str:
    esc = lambda value: str(value).replace("|", r"\|").replace("\n", " ")
    commit = payload["source_commit"]
    if not isinstance(commit, str) or not COMMIT.fullmatch(commit):
        raise ValueError("Markdown reviews require an exact checklist-source commit SHA")
    result = [
        "# Scoped project review",
        "",
        f"**Project:** {esc(project) if project else 'TBD'}",
        f"**Release / environment:** {esc(release) if release else 'TBD'}",
        f"**Source revision:** {commit} (main is mutable if no SHA was provided)",
        f"**Profile:** {payload['profile']} — {esc(payload['profile_description'])}",
        f"**Selected scopes:** {', '.join(payload['scope_filter'])}",
        f"**Selected checks:** {payload['count']}",
        "",
        "> **UNVERIFIED STARTER TEMPLATE.** Every check starts UNKNOWN, not PASS. "
        "Inspect the product, add direct evidence and human sign-off. This profile "
        "does not replace threat modeling, jurisdiction-specific requirements or other applicable release gates.",
        "",
        "**Reviewer:** TBD  |  **Review date:** TBD  |  **Approval owner:** TBD",
        "",
        "| ID | Tier | Scope | Verification | Result | Evidence / owner / exceptions |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in payload["items"]:
        url = "https://github.com/Pro-GenAI/awesome-checklists/blob/" + commit + "/" + item["source"]
        original = "[{}]({})".format(item["id"], url)
        result.append(
            "| {} | {}{} | {} | {} | UNKNOWN | — |".format(
                original, item["priority"],
                "*" if item["priority_basis"] != "curated-core-50" else "",
                item["scope"], esc(item["criterion_markdown"]),
            )
        )
    result.extend([
        "",
        "*An asterisk on a tier means it is provisional text-based triage; "
        "Core 50 labels are contextual curated suggestions. Re-rate for this project.*",
        "",
        "## Decision and risk register",
        "",
        "**Decision:** NOT ASSESSED (not a release approval)",
        "",
        "**Blocking gaps and owners:** TBD",
        "",
        "**N/A decisions with rationale:** TBD",
        "",
        "**Exceptions / expiry / approval:** TBD",
        "",
        "**Additional applicable controls outside this shortlist:** TBD",
        "",
        "**Linked evidence and reviewed artifact SHA:** TBD",
        "",
    ])
    return "\n".join(result)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--profile", choices=tuple(PROFILES), default="startup")
    parser.add_argument("--scope", action="append", choices=sorted(SCOPES), help="Repeat to choose applicable scopes; AI is opt-in")
    parser.add_argument("--domain", action="append", help="Repeat with stable ID prefix, e.g. SEC or AGENT")
    parser.add_argument("--size", type=int, default=50, help="25 to 100 selected checks")
    parser.add_argument("--include-id", action="append", default=[], help="Require existing ID in selection (repeatable)")
    parser.add_argument("--exclude-id", action="append", default=[], help="Exclude existing ID (repeatable)")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--project", default="", help="Display name only; not verified from code")
    parser.add_argument("--release", default="", help="Human-provided release/environment label")
    parser.add_argument("--source-commit", help="Optional full SHA, must match clean local HEAD; inferred by default")
    parser.add_argument("--output", type=Path, help="Write file here; prints to stdout if omitted")
    args = parser.parse_args()
    if args.source_commit and not COMMIT.fullmatch(args.source_commit):
        parser.error("--source-commit requires a 40-character hexadecimal Git SHA")
    try:
        root = args.repo_root.resolve()
        check = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            capture_output=True, text=True, check=False,
        )
        source_commit = check.stdout.strip().lower()
        if check.returncode != 0 or not COMMIT.fullmatch(source_commit):
            raise ValueError("A Git checkout with a verifiable checklist-source HEAD is required for review output")
        if args.source_commit and source_commit != args.source_commit.lower():
            raise ValueError("--source-commit must equal the local checkout's Git HEAD; no arbitrary provenance labels")
        dirty = subprocess.run(
            ["git", "-C", str(root), "status", "--porcelain", "--untracked-files=no"],
            capture_output=True, text=True, check=False,
        )
        if dirty.returncode != 0 or dirty.stdout.strip():
            raise ValueError("Review generation requires a clean tracked source tree; uncommitted content cannot be attributed to a Git SHA")
        source = export(root, "all", False, source_commit)
        payload = select(
            source, profile=args.profile, scopes=args.scope, domains=args.domain,
            size=args.size, include=args.include_id, exclude=args.exclude_id,
        )
        payload["project"] = args.project
        payload["release"] = args.release
        output = (
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
            if args.format == "json" else markdown(payload, args.project, args.release)
        )
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(output, encoding="utf-8")
        else:
            print(output, end="")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"generate_review: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
