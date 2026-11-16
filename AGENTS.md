# AGENTS.md — agent and contributor entry point

**Purpose:** This is the compact index for maintainers and coding agents. The repository contains reusable, unchecked review prompts, **not** certifications or verified product reviews.

## Where instructions live

- [Site, skill and supporting tools](docs/agents/resources-and-tooling.md): website, reference catalogs, badge, agent-skill packaging.
- [Scope inventory and domain routing](docs/agents/scope-inventory.md): numbered file ownership, security and agent cross-scope IDs, domain responsibilities.
- [Contributor and review workflow](docs/agents/contributor-workflows.md): adding checks, evidence, safe source ingestion, quality and release procedures.
- [Ideas and maintenance backlog](docs/agents/maintenance-backlog.md): uncommitted candidates, optional tools and research questions.
- [Public changelog](docs/CHANGELOG.md) and [contribution policy](docs/CONTRIBUTING.md): current changes and review expectations.

## Non-negotiable review rules

- **Select a bounded subset first.** Use the [Core 50](lists/references/core-50.md) or [25-check scope starters](lists/references/minimum-viable-by-scope.md). Every actual review result begins UNKNOWN and must include target-project evidence, scope, reviewers and decisions.
- Treat the [machine-generated inventory](lists/references/inventory.json) and [ID range register](lists/references/id-prefix-ranges.json) as the counts/ID sources of truth. Run validators after edits. Preserve existing stable IDs and source checkboxes.
- **Priorities are not universal severity.** Only Core 50 tiers have editorial curation; the remaining tiers are provisional text heuristics. A security expert must adjust them for the reviewed project.
- The [AGENT cross-scope map](lists/references/agent-domain-map.md) defines ownership of backend API `AGENT-095`–`AGENT-116`. A gap in one source file is not a globally missing ID.
- **Fetch source at a pinned SHA.** The skill's [release metadata](skills/awesome-checklists/references/source-release.json) identifies its immutable default source. Record that checklist SHA separately from the reviewed project SHA. Newer `main` criteria are not silently included in older pinned releases.
- MCP compatibility must be checked against the running SDK's negotiated revision; the maintained stable specification date is in [release metadata](skills/awesome-checklists/references/source-release.json).
- Do not run unauthorized intrusive tests or untrusted third-party tools, grant production credentials, claim that a suggested tool is a validator, or fabricate an independent reviewer or PASS result. See [authorship limits](docs/AUTHORSHIP.md) and [field review protocol](lists/references/independent-review-protocol.md).
- For material checklist changes, run local checks and seek qualified review as appropriate. Legacy source-lint and website workflows remain disabled; new curation quality and weekly link workflows are active when merged. A direct commit does not prove independent review. See [CONTRIBUTING.md](docs/CONTRIBUTING.md).

## Verify source changes

```bash
python3 skills/awesome-checklists/scripts/lint_repository.py
python3 skills/awesome-checklists/scripts/generate_inventory.py --check
python3 skills/awesome-checklists/scripts/generate_id_prefixes.py --check
python3 skills/awesome-checklists/scripts/validate_domain_structure.py
python3 skills/awesome-checklists/scripts/validate_release_metadata.py
python3 -m unittest discover -s skills/awesome-checklists/tests -v
```

**Automation status:** Historical [source lint](.github/workflows/checklist-lint.yml.disabled) and [website build](.github/workflows/website.yml.disabled) remain disabled; [curation quality](.github/workflows/quality-gates.yml) runs on PRs and pushes, while [curated link health](.github/workflows/link-health.yml) runs weekly. Continue running the full local validations above when appropriate.
