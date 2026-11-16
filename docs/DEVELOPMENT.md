# Development and maintenance

Technical details for maintainers, integrators, and advanced users of [awesome-checklists](../README.md). For editorial rules and verification requirements, use [CONTRIBUTING.md](CONTRIBUTING.md); for agent-oriented maintenance, see [AGENTS.md](../AGENTS.md).

The public quick start, source-library overview, and checklist usage guidance remain in [README.md](../README.md).

## Pro-GenAI implementation companions

Use these projects as examples of **where to apply** the checklists, not proof that a dependency is safe or that an audit passed.

| Ecosystem project | Checklist connection and specific reason |
| --- | --- |
| [Agent-RT](https://github.com/Pro-GenAI/Agent-RT) | `[Runtime Guardrail]` Test the agent runtime's tool permissions, checkpoints, streaming and observability boundaries before production use. |
| [Agent-Action-Guard](https://github.com/Pro-GenAI/Agent-Action-Guard) | `[Security Audit]` Evaluate real-time tool/action classification alongside server-side authorization; classifiers do not replace permissions. |
| [Safe-LLM](https://github.com/Pro-GenAI/Safe-LLM) | `[Eval Benchmark]` Recheck held-out harmful-action and legitimate tool-call outcomes for the specific deployment, not just a project benchmark. |
| [Large-Supervisor-Models](https://github.com/Pro-GenAI/Large-Supervisor-Models) | `[Runtime Guardrail]` Test interruption timing, unsafe partial streams and false positives before using stream supervision. |
| [Agent-Swarm-Eval](https://github.com/Pro-GenAI/Agent-Swarm-Eval) | `[Eval Benchmark]` Use reproducible multi-agent task cases, observed tool side effects and regression thresholds when applicable. |
| [gen-ai-project-template](https://github.com/Pro-GenAI/gen-ai-project-template) | `[PR Template]` Review lazy initialization, Milvus/RAG setup, deployment configuration and secret handling before inheriting starter defaults. |

## Agent skill internals and source pinning

**Pinned-source default:** The installable skill uses the immutable checklist commit identified in [its bundled source-release metadata](../skills/awesome-checklists/references/source-release.json), not moving `main`. The install command below fetches the *skill package* from the repository at installation time; for a fully frozen installation, check out a specific commit before installing the local skill. Always record both the checklist-source SHA and the reviewed project's revision. The latest documentation on `main` may include changes not yet included in a pinned release.

> **Public repository:** The skill can be installed and its checklists retrieved anonymously while GitHub's public access and rate limits permit. Authentication (`gh auth login`, `GH_TOKEN`, or `GITHUB_TOKEN`) is optional for readers and can help with API rate limits. SSH installation is also supported when you have configured SSH credentials.

**Reproducibility:** the checklist fetch helper reads its immutable default SHA from [source-release.json](../skills/awesome-checklists/references/source-release.json), **not moving `main`**. Every review must record its checklist-source SHA and the reviewed project revision separately. The quick `npx skills add` command above is an unpinned convenience installation of the skill itself; do not mistake it for a frozen review source. For multi-file work, use `fetch-many` (maximum five files) or the public `--raw` mode if the API is rate-limited.

The skill includes a standard-library [checklist fetch helper](../skills/awesome-checklists/scripts/checklists.py), a [domain selection guide](../skills/awesome-checklists/references/domain-selection.md), and [offline unit tests](../skills/awesome-checklists/tests/test_checklists.py). It **does not** copy or claim to certify all checks; it loads relevant upstream files when accessible.

## Inventory reproduction and ID ownership

**Reproduce the inventory from source.** At a checked-out revision, run:

```bash
python3 skills/awesome-checklists/scripts/validate_inventory.py
python3 skills/awesome-checklists/scripts/generate_inventory.py --check
python3 skills/awesome-checklists/scripts/generate_id_prefixes.py --check
```

The [machine-readable inventory](../lists/references/inventory.json) records the 14/20/35/22 file counts and 701/684/1,118/1,712 formatted checks (4,215 total). The source validator counts actual numbered Markdown checklist entries, enforces uniqueness, and compares them against the tracked manifest. **These are mechanically verifiable counts, not 4,215 independently tested or semantically distinct assurances.** The stable ID prefix registry explains why `SEC-007` can belong to the backend file while `SEC-040` appears beside earlier shared security checks; renumbering to make one file sequential would break downstream review history. See [ID history and ownership](../lists/references/id-history.md).

## Machine-readable JSON and change history

The maintained [Core 50 JSON selection](https://github.com/Pro-GenAI/awesome-checklists/blob/main/lists/references/core-50.json) carries the selected IDs, source paths, exact criterion text and contextual priorities. Generate the **full current Markdown inventory** in JSON, and optionally an editable project review template, from a local clone:

```bash
python3 skills/awesome-checklists/scripts/export_checklists.py --output checklists.json \
  --source-commit "$(git rev-parse HEAD)"
python3 skills/awesome-checklists/scripts/export_checklists.py --only-core \
  --output core-catalog.json --review-template project-review.json
```

The exported catalog preserves Markdown criterion text, the visible suggested tier for every check, and a `priority_basis` field distinguishing the manually curated 50 from provisional text-based triage. Every project must validate the tiers against its actual risks. The review template starts every check at `UNKNOWN`; evidence and status belong to the reviewed project, not this source repository. Review [CHANGELOG.md](CHANGELOG.md) for updates that may affect earlier reports.

## Keep copied project reviews current

Every review should preserve its **checklist-source SHA** separately from the **reviewed product SHA**. Export the JSON catalog with a pinned SHA, retain the original project review/evidence, and [compare snapshots](../lists/references/downstream-update-guide.md) before adopting a newer checklist revision:

    python3 skills/awesome-checklists/scripts/compare_checklist_exports.py --before checklist-baseline.json --after checklist-current.json --output checklist-delta.md

The report identifies new, removed, reworded, re-tiered and moved IDs. It flags results that need re-evaluation; it never copies PASS decisions into a different source revision. This is safer than silently replacing a project's copied Markdown template.

## Public repository and review model

The repository is **public**; authentication is optional for readers. This is a relatively young, community-improvable reference library, **not independently audited or certified**. Its check count is verified against source IDs, not proof that every check has been externally validated or semantically deduplicated.

For contribution and review procedures, see [CONTRIBUTING.md](CONTRIBUTING.md). The historical source-lint and website-build workflows remain disabled (`.github/workflows/*.disabled`). The new [curation quality gates](../.github/workflows/quality-gates.yml) run on PRs and pushes, and [weekly curated-link checks](../.github/workflows/link-health.yml) can flag dead links and archived repositories after this change merges. Automated results are not independent technical review.

## Shared review method and optional compliance crosswalk

Every checklist now links to the centralized [review method](../lists/references/review-method.md) and [optional compliance crosswalk](../lists/references/compliance-crosswalk.md). The common template/usage/warning boilerplate and optional third-party AI-skill recommendation lists have been removed from numbered source checklists; domain-specific release gates and primary references remain. **No checklist implies GDPR, India DPDP, ASVS, or SOC 2 compliance.**

The shared security checks `SEC-006` and `SEC-017` were narrowed into independently testable criteria, with eight new globally unique IDs `SEC-102`–`SEC-109` for MFA, password hashing, audit verification, coverage and remediation. Earlier review reports must reevaluate the narrower checks and associated new IDs. The previously compound `SEC-012`, `SEC-013` and `SEC-014` have been decomposed into focused criteria plus four new stable IDs `SEC-118`–`SEC-121`; existing frontend/backend controls retain their separate responsibilities. Earlier PASS results for those three IDs must be re-evaluated. [Security atomicity map](../lists/references/security-compound-triage.md) documents the criterion-level migration and explicitly notes **no independent expert approval**. For other candidates run `python3 skills/awesome-checklists/scripts/audit_compound_checks.py --output compound-candidates.json`; this reports heuristic candidates, not proof of review.

## ID history, tool supply-chain risk and updated AI sources

The [Security ID history](../lists/references/id-history.md) and [active registry](../lists/references/security-id-registry.json) explain topical ID order across scopes. Security session and abuse controls have been split for independent verification, retaining the original IDs.

All optional testing-tool lists are now in a [central testing-tool index](../lists/references/optional-testing-tools.md), with separate file-specific Shared, Frontend, Backend and AI catalogs plus dedicated [Security](../lists/references/security-testing-tools.md) and [Agent](../lists/references/agent-testing-tools.md) guides. None is required or endorsed; commands and vendor links are not independent test evidence. The [AI source-currency watch](../lists/references/ai-source-watch.md) records verified NIST, OWASP 2026 and EU AI Act timeline updates without claiming a legal audit.

## Generate a project-specific review in one command

Don't attempt all 4,215 checks. Create an editable **25–100 item Markdown or JSON review** using a documented startup, regulated, or internal-tool selection profile. Source scopes and stable ID prefixes can be filtered explicitly; **AI checks are opt-in**. Every generated result starts `UNKNOWN` with blank evidence, and heuristically selected tiers require human review.

```bash
python3 skills/awesome-checklists/scripts/generate_review.py --profile startup --size 50 --project "My app" --output review.md
python3 skills/awesome-checklists/scripts/generate_review.py --profile regulated --scope shared --scope backend --size 100 --format json --output regulated-review.json
python3 skills/awesome-checklists/scripts/generate_review.py --scope AI --size 25 --output ai-review.md
```

See the [scoped review generator guide](../lists/references/scoped-review-generator.md) for selection logic, allowed overrides and release-evidence requirements.

## Standards mapping with explicit requirement IDs

The [control-level starter crosswalk](../lists/references/control-crosswalk.md) and its [machine-readable 22 mapping candidates](../lists/references/control-crosswalk.json) contain **primary-source-checked external identifiers** for OWASP ASVS 5.0.0, NIST CSF 2.0, ISO/IEC 27002:2022 and AICPA SOC 2 TSC. The identifier is verified, but **coverage is proposed and partial**—it is not certification, an equivalence claim, or evidence that applicable external requirements were satisfied. The [broader legal topic guide](../lists/references/compliance-crosswalk.md) remains separate.

## How the library was authored and validated

**Independent validation remains open:** The [field-review protocol and evidence ledger](../lists/references/independent-review-protocol.md) provide a structured process for practitioner testing and external sign-off; no reviewer, field trial or certification is claimed until independently supplied evidence is recorded.

The [maintainer entry point](../AGENTS.md) links to [scope inventory](agents/scope-inventory.md) and [editorial workflows](agents/contributor-workflows.md). `AGENT-026` tool-call validation was split into individually testable `AGENT-137`–`AGENT-141` facets; consult the [acceptance matrix](../lists/references/agent-testing-tools.md#tool-call-validation-matrix-agent-026137141) rather than carrying historical PASS results forward.

The [authorship and validation disclosure](AUTHORSHIP.md) explicitly documents **AI-assisted maintenance**, incomplete historical per-ID attribution, the limits of automated checks, and the steps required for future independent human review. No assertion is made that all 4,215 checks have undergone expert review. External adoption and standards compliance are not inferred from check count or successful CI.

## One-day starters and agent ID continuity

For a small first review, [generate **25 checks for each relevant scope**](../lists/references/minimum-viable-by-scope.md)—shared, frontend, backend, or AI—instead of attempting all 4,215. The profile is heuristic and UNKNOWN-first, not a verified release minimum or a substitute for additional required controls. The [worked source-inspection example](../lists/references/example-review.md) demonstrates evidence/result statuses but is not an independent product audit.

**The AGENT domain is complete across two files:** [AI agent and frontend checks](../lists/AI/11_AI_Agents_and_Tool_Orchestration.md) contain `AGENT-001`–`AGENT-094` and `AGENT-117`–`AGENT-141`; [backend API checks](../lists/backend/17_AI_Agents_and_Tool_Orchestration.md#api-checks) own `AGENT-095`–`AGENT-116`. The [domain map](../lists/references/agent-domain-map.md) and [CI-enforced contract](../lists/references/agent-domain-contract.json) check all 141 IDs and section links. The [overlap/evidence assessment](../lists/references/overlap-review.md) distinguishes controls from tests rather than deleting similar-looking IDs.

AI Agent testing suggestions are now [separate, optional check-specific recipes](../lists/references/agent-testing-tools.md), not a default vendor stack. The agent files cite the **MCP 2026-07-28 stable specification**, with a warning to confirm each runtime's negotiated version.

## Cross-file section and link integrity

The offline source linter checks required `## Release gate` and `## Trusted references and scope` headings, source-review dates, and local Markdown section anchors. These are mechanical structural checks, not a content or security certification. The GitHub Actions workflow that formerly ran them is disabled.

## Machine-checked inventory and source freshness

The [generated inventory](../lists/references/inventory.json) is compared against source IDs and the README headline in CI, preventing unreviewed count drift. The [full 35-prefix range and owner register](../lists/references/id-prefix-ranges.md) is also source-generated and checked on every push, so an ID disappearing from one of its owning files is detectable. The [180-day source freshness policy](../lists/references/source-freshness-policy.md) flags outdated references without pretending a timestamp verifies their content. The [security attack-surface coverage crosscheck](../lists/references/security-surface-coverage.md) locates existing IDOR/BOLA, SSRF, CSRF/CORS, logging and encryption/key-management controls across scopes.

`SEC-009` and `SEC-116` now independently test idle and absolute session expiry; `SEC-010` and `SEC-117` independently cover guessing and credential stuffing. `AGENT-043` now tests permissions only; existing AGENT approval IDs independently cover approvals. Previous compound-check PASS results require re-verification.

## Additional reference resources

**Optional SEO redesign worksheet:** [Website redesign URL-map template](../lists/frontend/references/seo-redesign-url-map-template.md) offers an old-to-new mapping and verification example for project-specific site migrations; it is not a checklist or a guarantee against ranking changes.

**Source provenance:** [External source-coverage audit](../lists/references/source-coverage-audit.md) records prior reviews, limitations, and why source suggestions were adopted or excluded. It is not a numbered checklist.

## Self-hosted review badge

For a **larger, 44 px-high badge with a prominent checkmark and more readable text**, you can instead **copy** the [custom SVG badge](website/assets/reviewed-with-awesome-checklists.svg) to `assets/reviewed-with-awesome-checklists.svg` and use:

```markdown
[![Reviewed with awesome-checklists](../assets/reviewed-with-awesome-checklists.svg)](https://github.com/Pro-GenAI/awesome-checklists)
```

The copy-and-host option is useful when you do not want a dependency on Shields.io. The source repository is **public**, so a raw GitHub SVG may be accessible, but copying the badge into your own project avoids an external GitHub dependency. The Shields.io badge remains a public alternative.
