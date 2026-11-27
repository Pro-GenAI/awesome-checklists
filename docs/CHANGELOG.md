# Changelog

## 2026-11-16 — Licensing scope, SPDX and voluntary reuse credit

- Documented the CC0-for-original-content / MIT-for-code path scopes, third-party exclusions and mixed-file rules in [LICENSING.md](LICENSING.md); the legal licenses themselves are unchanged.
- Added SPDX license identifiers to original executable source files and the drop-in checklist Markdown templates without altering checklist IDs or criteria.
- Added contribution provenance and rights-review checkpoints and an optional reuse credit that does not imply certification. Historical authorship and third-party license clearance remain subject to review; no global clearance is claimed.

## 2026-11-16 — Local pin verification, helper tests and filename stability

- Added an opt-in offline pin-ancestry verifier for full Git clones, with test coverage for missing pins and missing branch refs. The existing source pin was verified against `main` through GitHub comparison but is not auto-refreshed.
- Added `fetch FILE --id PREFIX-NNN` to the checklist helper, plus regression tests for single-ID retrieval, symlink escapes and truncated remote Git trees. Single-ID output intentionally omits source references and release gates.
- Froze existing numbered filename prefixes, allowing reserved gaps on future file removal and rejecting duplicated numeric prefixes. No existing paths or stable IDs were renamed.
- Corrected the README to describe pinned rather than automatically current checklist criteria. GitHub Actions remains disabled; manual validation is required and independent content review remains open.


## 2026-11-16 — Release-gate wording and domain-selection clarity

- Clarified that Security release blockers are determined by project-specific evidence and obligations, not by provisional text-derived priority tiers alone.
- Expanded skill domain selection to legal/privacy, internationalization, cost, and the shared counterparts to backend operations.
- Corrected stale overlap statistics: 4,215 distinct stable IDs, zero duplicate IDs under current inventory validation, and no quantified semantic deduplication claim.
- GitHub Actions remains disabled; these are editorial adjustments, not external technical certification.


## 2026-11-16 — MIT licensing and disabled GitHub Actions

- Licensed original code, written checklists and documentation under MIT (Copyright 2026 Praneeth Vadlapati), with third-party rights retained.
- Renamed the active source workflow to `.github/workflows/checklist-lint.yml.disabled`; website CI was already disabled. Updated live documentation to require local checks.
- Added bounded transient fetch retries with offline regression tests; ordinary HTTP 404 and lengthy rate-limit waits are not retried.
- No change to checklist counts, IDs, priorities, or external review status.


## 2026-11-16 — Documentation consistency and process guidance

- Removed direct-to-`main` contribution advice from README; detailed procedures remain in CONTRIBUTING.md.
- Corrected README AGENT contract coverage from 136 to 141 IDs, matching the generated prefix registry. Added an offline regression test for the count and README contribution-policy boundary.
- Updated CONTRIBUTING.md's CI description to match the actual push/PR validation workflow.
- No LICENSE file was introduced: license selection requires the rights holder's explicit decision.


## 2026-11-16 — Offline reviewability and generator-description consistency

- Corrected the scoped-review guide and exported selection metadata to reflect the existing ranking algorithm: only manually curated Core 50 priority tiers contribute severity points. Provisional text-derived tiers are displayed but never scored. Added regression coverage.
- Tightened AGENT-020 and AGENT-092 to require observable risk-acceptance and reviewer-competence evidence, with offline-only example verification recipes. No project controls were tested and no human endorsement is implied.
- Added a `--core-only` option to the read-only compound-check triage tool, with tests. Findings remain editorial candidates, not verified defects or independently validated checklist items.
- Kept the inventory at 91 files / 4,215 stable IDs; no priorities or IDs were reassigned. Independent practitioner and field validation remain outstanding.


Changes that affect checklist readers, stable IDs, review behavior and tooling are documented here. Dates refer to repository updates, not external compliance certification.

## 2026-11-15 — Live documentation and scope-table consistency follow-up

- Corrected eight stale LEG, SEC, ANL and LAUNCH global domain-count cells in the extracted maintainer scope tables. These numbers refer to cross-scope ID-prefix totals, not to the number of checks in an individual file.
- Reconciled two outdated direct-to-main/no-PR statements in the live site/skill resource guide with the [review-first contribution policy](CONTRIBUTING.md). The archived historical log remains unchanged and is not current guidance.
- Added a source CI regression guard that compares every displayed domain-count table cell to the generated stable-ID prefix register and rejects stale review-policy wording. This is structural validation, not an independent content review.
- Maintenance follow-up committed by an authorized maintainer to main after the previous refactor; no independent peer approval is asserted.

## 2026-11-15 — Short agent instructions, atomic tool inputs and release metadata

- Split the 126 KB `AGENTS.md` into a compact entry point and linked site/resources, scope inventory, contributor workflow, archived historical maintenance log and backlog documents. Removed its stale statement that source CI is inactive; archived history is not current operational policy.
- Placed Core 50 and 25-check scope starters at the top of README. The review generator no longer scores provisional keyword-derived P0/P1/P2 severity labels; profile-based selection is still a candidate shortlist, not a validated risk rating.
- Split six independently testable AGENT-026 tool-call input facets into narrowed AGENT-026 plus AGENT-137–141, with separate negative-test evidence examples. Updated cross-scope contract and ID ranges. Historic AGENT-026 PASS evidence must be re-evaluated.
- Added bundled release metadata for the public repository, stable MCP specification revision and SHA-pinned skill source, plus offline/CI checks. The default pin can lag `main` intentionally, and must only be advanced after source checks pass.
- Updated inventory to **91 numbered files and 4,215 IDs** (shared 701, frontend 684, backend 1,118, AI 1,712), with 50 curated and **4,165 provisional** priority labels. Documentation now prefers a PR and CI for substantive changes. GitHub protection settings and independent human reviews are not claimed to be enforced or completed.

## 2026-11-15 — Atomic Security criteria, migration evidence, and audit traceability

- Narrowed **SEC-012**, **SEC-013** and **SEC-014** to separate verifiable outcomes, with new **SEC-118–SEC-121** for database injection, command injection, unsafe deserialization and path traversal. Existing XSS, CSRF, SSRF, file handling and API controls retain their earlier IDs rather than being duplicated.
- Updated the curated SEC-012 Core 50 criterion, OWASP mapping to SEC-118, SEC registry, ID history, prefix ranges and inventory. Current total: **91 files / 4,210 checks** (701 shared, 684 frontend, 1,118 backend, 1,707 AI). The other **4,160** priorities remain provisional.
- Previous PASS decisions under the broader SEC-012/013/014 wording are **not** transferable to the revised text. A content decomposition and passing CI **do not constitute independent technical validation**. See the [atomicity map](../lists/references/security-compound-triage.md) and [independent review protocol](../lists/references/independent-review-protocol.md).
- Archived generated external-link audit logs for scheduled/manual reviews and added an executable fixture-based guard against accidentally recombining the decomposed criteria.

## 2026-11-15 — Visible inventory reproduction and assurance limits

- Added front-page commands to reproduce the 91-file/4,206-ID inventory, verify all 35 prefix ranges, and explain why cross-scope SEC numbering is intentionally nonsequential within one file.
- Clarified that the repository synthesizes existing OWASP, NIST, accessibility and readiness guidance, with value in selection, stable IDs, agent retrieval and evidence workflows—not novel standards or independently certified checks. GitHub engagement metrics do not establish technical validation.
- No checklist criteria, stable IDs, priorities or release gates changed.

## 2026-11-15 — Downstream review diffs and broader link/atomicity triage

- Added a [source-delta comparator](../skills/awesome-checklists/scripts/compare_checklist_exports.py) for pinned exported catalogs, with regression tests and [migration guidance](../lists/references/downstream-update-guide.md). It flags additions, removals, text/priority changes, and scope moves without auto-approving prior project results.
- Scheduled/manual external URL checks now rotate their fixed-size window weekly to cover more unique links; HEAD failures must be confirmed with GET before reporting a possible 404/410. These checks remain advisory and are not an external-source certification.
- Improved the compound-check heuristic to flag multi-surface Security controls such as SEC-012 and SEC-014; published an [editorial triage](../lists/references/security-compound-triage.md) with separate evidence expectations. **Those controls have not yet been independently split into new IDs.**
- Corrected the older 4,204/4,154 figures in AUTHORSHIP.md to the currently verified 4,206/4,156. No stable IDs, checklist criteria or tier assignments changed.

## 2026-11-15 — Reject ID gaps when regenerating prefix ranges

- The full stable-ID prefix generator now rejects numeric gaps (including a missing `-001`) across all four scopes, even if a maintainer regenerates the JSON register. AGENT-095–116 remain valid in their backend owner file.
- Added offline regression tests for cross-scope continuity, missing middle/start IDs, and duplicate IDs. Source CI now runs on optional pull requests as well as direct `main` pushes and weekly/manual checks.
- This enforces structural continuity, not check correctness; intentional future retirements require an explicit reviewed policy rather than silently dropping or reusing IDs.

## 2026-11-15 — Consolidated optional tools and source-reference ordering

- Relocated **85 generic optional-tool blocks** from numbered checklist templates into [four scope-specific catalogs](../lists/references/optional-testing-tools.md): shared 13, frontend 19, backend 33 and AI 20. Security and AI Agent checklists retain their dedicated, more focused tool guides. Each original template links to its catalog section; no check ID, criterion, priority or release gate changed.
- Added a central optional-tool index and documentation explaining that vendor tools, generic test commands and agents do not constitute PASS evidence, validation or permission to execute untrusted code.
- Source lint now requires each numbered checklist's **dated source review line to be the last nonblank line**, preventing generic tooling and reference links from drifting below that date. Added negative regression coverage for post-date content. This changes only editorial structure and automated validation, not external compliance status.

## 2026-11-15 — Required sections and local anchor integrity

- Extended [source lint](../skills/awesome-checklists/scripts/lint_repository.py) to check **all 91 numbered checklists** for unique Release gate and Trusted references headings, date metadata and correct ordering.
- Local Markdown `#fragment` links now require a real target heading rather than merely an existing file; added regression tests for missing anchors, duplicate headings and section changes. This is a CI structural check, **not** an external URL availability or compliance audit.
- Committed directly to `main` without a PR and preserved the disabled website build workflow.

## 2026-11-15 — Full stable-ID range register and pinned optional tooling

- Verified the 91 source files contain **4,206 unique IDs across 35 prefixes**, all currently contiguous across their combined scope owners. Published [generated ID-prefix ranges](../lists/references/id-prefix-ranges.json) and [range/owner guidance](../lists/references/id-prefix-ranges.md), with CI-backed change detection and offline tests. Apparent per-file gaps remain valid when another scope owns the IDs.
- Pinned the optional Cloudflare security-audit-skill *source link* to a concrete upstream commit, with explicit human supply-chain vetting and sandbox requirements. Source pinning does not imply endorsement or safe execution.
- No PR is required; the website workflow remains disabled.

## 2026-11-15 — Pinned skill sources, integrity checks and atomicity

- The source helper now defaults to an immutable commit, explicitly records source provenance, and provides rate-limit diagnostics, authenticated/API or public raw retrieval and five-file batches. Local `--ref` conflicts are errors; consumers must record the checklist-source SHA and reviewed project SHA.
- Split SEC-009 into idle lifetime and SEC-116 absolute lifetime checks; SEC-010 now covers password guessing and SEC-117 credential stuffing. Narrowed AGENT-043 to operation-specific permissions; distinct human-approval IDs remain. Preserve all old IDs, require new evidence after wording changes.
- Generated [inventory.json](../lists/references/inventory.json) and check it against the README headline: **91 files, 4,206 checks**, with 698 shared, 684 frontend, 1,117 backend and 1,707 AI.
- Added [180-day source review age rules](../lists/references/source-freshness-policy.md), [security surface coverage](../lists/references/security-surface-coverage.md), source-date link-order cleanup and more targeted JavaScript/TypeScript scanner guidance. CI performs structural, age and inventory checks.
- Kept direct-main contribution without PRs and left website build workflow disabled.

## 2026-11-15 — Agent cross-scope continuity and actionable test evidence

- Verified `AGENT-001`–`AGENT-136` form one contiguous domain, including `AGENT-095`–`AGENT-116` in `lists/backend/17_AI_Agents_and_Tool_Orchestration.md`; no IDs were removed or reassigned. Added an explicit [domain owner/section map](../lists/references/agent-domain-map.md) and [machine-readable contract](../lists/references/agent-domain-contract.json).
- Added offline [cross-scope structure validator](../skills/awesome-checklists/scripts/validate_domain_structure.py) and regression tests for missing/misplaced IDs, absent headings and invalid section anchors. Integrated it into existing main-push CI without requiring pull requests.
- Published four [25-check scope starters](../lists/references/minimum-viable-by-scope.md) using the existing deterministic UNKNOWN-first review generator. These are not a universal compliance minimum.
- Clarified `AGENT-046` as a single required audit-event schema criterion, documented distinct control/test/API acceptance evidence, and moved generic vendor/command suggestions from both AGENT files to [optional targeted test recipes](../lists/references/agent-testing-tools.md). No previously stable check ID was deleted, merged or renumbered.
- Updated both AGENT files to cite the **MCP 2026-07-28** stable release and compatibility guidance; retained older-version relevance only when a runtime actually negotiates it. Original 2025 sources remain historical rather than current.
- The repository is still public, the scoped review and worked historical example already existed, and the website build workflow remains disabled.

## 2026-11-15 — Scoped review generation, control-level mapping and authorship transparency

- Added [generate_review.py](../skills/awesome-checklists/scripts/generate_review.py), an offline bounded **25–100 check** Markdown/JSON review generator with `startup`, `regulated` and `internal-tool` profiles, explicit scope/domain/ID overrides, deterministic selection, empty evidence and **UNKNOWN** default status. AI review scope is opt-in; source revisions can be pinned only when matching local Git HEAD.
- Published the [generator usage guide](../lists/references/scoped-review-generator.md), including warning that profile weighting and provisional P0/P1/P2 tiers are not expert risk assessments.
- Added [control-crosswalk.md](../lists/references/control-crosswalk.md) and [machine-readable control-crosswalk.json](../lists/references/control-crosswalk.json): **22 proposed partial alignments** to primary-source-confirmed external identifiers in **OWASP ASVS 5.0.0, NIST CSF 2.0, ISO/IEC 27002:2022 and AICPA SOC 2 TSC**. Mapping presence does not assert complete coverage or conformance; full licensed texts and qualified assurance review may be needed.
- Added [AUTHORSHIP.md](AUTHORSHIP.md) transparently documenting AI-assisted November 2026 maintenance, absent historical per-ID author/reviewer attribution, and explicit future human evidence/source review requirements. Successful source lint is not independent expert validation.
- Added offline generator/crosswalk tests, updated source-link checks and CI coverage. No PR is required and the website workflow remains disabled. Checklist item text and existing stable IDs are unchanged; current inventory remains 91 files / 4,204 IDs.

## 2026-11-15 — Security atomicity, source hygiene and main-branch lint

- Total source inventory increased from 4,198 to **4,204 distinct IDs** across 91 numbered files: shared 696, frontend 684, backend 1,117, AI 1,707.
- Narrowed `SEC-009` to session expiration and added `SEC-110`–`SEC-112` for session rotation, logout revocation and expiring/single-use recovery tokens. Narrowed `SEC-010` to login brute-force/credential stuffing and added `SEC-113`–`SEC-115` for signup, recovery and email/SMS verification abuse.
- Added [ID history](../lists/references/id-history.md) and [Security registry](../lists/references/security-id-registry.json) to explain apparent gaps and prevent accidental deletion/moves without explicit updates.
- Normalized Security checklist whitespace, removed stray WCAG/AI references from non-AI Security scopes, and moved security testing/third-party agent recommendations into an [optional separate resource](../lists/references/security-testing-tools.md).
- Reviewed current [NIST, OWASP LLM 2026 and EU AI Act](../lists/references/ai-source-watch.md) headlines and updated relevant AI governance and oversight sources. This is not a comprehensive independent audit.
- Added an offline [repository linter](../skills/awesome-checklists/scripts/lint_repository.py) for source IDs, formatting and local links; added a new push-triggered [source lint workflow](../.github/workflows/checklist-lint.yml.disabled) with optional advisory external link checks. `website.yml.disabled` remains disabled.
- Documented that [PRs are optional, not required](CONTRIBUTING.md). Direct `main` commits remain allowed for authorized maintainers.

## 2026-11-15 — Library-wide review ergonomics and granular security controls

- Applied **visible P0/P1/P2 suggested tiers to all 4,198 checks** in the 91 numbered source checklists. The Core 50 tiers remain manually curated; the other 4,148 are **provisional deterministic text-based triage**, requiring project/domain review and never representing intrinsic severity or external control levels.
- Centralized review instructions, evidence/status definitions, context warnings and third-party-tool vetting in [review-method.md](../lists/references/review-method.md); each numbered file links there. Removed duplicate review-details/how-to/warning and AI-skill suggestion blocks while retaining domain-specific criteria, release gates, trusted sources and testing tools.
- Added an [optional compliance crosswalk](../lists/references/compliance-crosswalk.md) for ASVS levels and potential GDPR, India DPDP and SOC 2 topics. It **does not certify compliance or claim clause-level equivalence**; India DPDP staggered commencement must be considered.
- Split compound security checks while retaining the original IDs with narrowed meanings: `SEC-006` now addresses vetted authentication libraries, `SEC-102` MFA and `SEC-103` password hashing. `SEC-017` now defines audit scope; `SEC-104` static analysis, `SEC-105` secrets scanning, `SEC-106` authorized dynamic testing, `SEC-107` verification of findings, `SEC-108` remediation and `SEC-109` evidence coverage. **No existing ID was deleted**, and total checks increased from 4,190 to **4,198** (shared: 682 → 690).
- Updated inventory tests and JSON export to require inline tiers and distinguish manually curated versus provisional tiers; GitHub Actions remains disabled.
- **Granularity limitation:** Compound-check editorial review outside `SEC-006` and `SEC-017` is not complete; do not treat all remaining checks as proven atomic. Added a read-only `audit_compound_checks.py` to flag possible multi-verification items throughout the library for human review.

## 2026-11-15 — Risk-scoped reviews and machine-readable export

- Added a curated [Core 50](../lists/references/core-50.md) across shared, frontend, backend and AI scopes, with **contextual** `P0`/`P1`/`P2` priorities. The other checks were initially unprioritized; see the later library-wide release entry for provisional suggested tiers.
- Added [core-50.json](../lists/references/core-50.json) metadata and an offline JSON catalog and project-review-template exporter. Catalog text comes directly from checklist Markdown; project statuses default to `UNKNOWN`.
- Added a [real, bounded source-inspection example](../lists/references/example-review.md) and an [overlap assessment](../lists/references/overlap-review.md) for the agent authority/approval controls.
- Replaced dated GitHub-star-based skill suggestions with a review-of-provenance/permissions requirement across all **91** numbered checklist templates. The example skill links are *suggestions*, not vetted endorsements.
- Preserved all existing numbered checks and stable IDs: **91 files / 4,190 IDs**, pending any separate full-library semantic duplication review.
- Kept GitHub Actions intentionally disabled; no CI workflow was enabled.

## Earlier changes on 2026-11-15

- Corrected the README's public-repository access guidance.
- Hardened checklist retrieval with explicit HTTP errors, pinned source revisions, blob fallback and local-path limitations.
- Added offline source-inventory validation and unit tests.

When adding or changing a checklist, record stable-ID changes, behavioral effects, scope moves, and any successor ID here. The repository's source-coverage audit is internal provenance documentation, **not independent external validation**.
