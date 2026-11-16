# Scope inventory and routing

**Live routing reference (2026-11-15).** Numeric counts are generated and checked in [inventory.json](../../lists/references/inventory.json); update this explanatory snapshot when those counts change. For current AGENT ownership use [the domain map](../../lists/references/agent-domain-map.md). See [AGENTS.md](../../AGENTS.md) for core instructions.

## Files and review domains

**Source layout:** All numbered templates now live under `lists/`: 14 shared files directly in `lists/`, 20 in `lists/frontend/`, 35 in `lists/backend/`, and 22 in `lists/AI/` (case-sensitive). The root `AGENTS.md`, `README.md`, `skills/`, and `website/` stay at the repository root; domain-specific supporting references may live within `lists/`. This is a source-path relocation only: checklist IDs, control text, counts, and checkbox states do not change. Use `lists/...` paths for all future source links and agent fetches. The website generator preserves legacy published HTML URLs for retained checklist and reference paths.

File prefixes express the **recommended order of use within each folder** (planning and design → implementation → verification and operations → release). Each folder starts at `01_` and uses every integer up to its final file: **`lists/` `01–14`, `lists/frontend/` `01–20`, `lists/backend/` `01–35`, and `lists/AI/` `01–22`**. Review order is guidance, not a claim that all checks apply to every project or that late-stage checks can wait until launch.

**The descriptive suffix and globally unique checklist ID prefix identify the domain; the filename number is local and may differ by folder.** Frontend now contains only 20 general client/browser domain files. Specialized AI UI checks are grouped into `lists/AI/`'s domain-specific `## Frontend Checks` sections; backend retains its 35 domain files. Existing folder filenames are currently numbered contiguously, but filename prefixes are frozen to preserve links and future gaps are allowed. `AGENTS.md`, `README.md`, and unnumbered references under `lists/**/references/` remain outside the numbered checklist inventory.

### Shared — `lists/` (01–14)

| # | Filename | Checklist ID prefix |
| ---: | --- | --- |
| 01 | `01_Requirements_and_Planning.md` | `REQ` |
| 02 | `02_LegalIssues.md` | `LEG` |
| 03 | `03_Architecture_and_CodeQuality.md` | `ARC` |
| 04 | `04_Internationalization_and_Localization.md` | `I18N` |
| 05 | `05_Security.md` | `SEC` |
| 06 | `06_Cost_and_FinOps.md` | `COST` |
| 07 | `07_Documentation_and_DeveloperExperience.md` | `DOC` |
| 08 | `08_Testing.md` | `TST` |
| 09 | `09_Performance_and_Scalability.md` | `PERF` |
| 10 | `10_Reliability_and_DisasterRecovery.md` | `REL` |
| 11 | `11_DevOps_and_CI_CD.md` | `OPS` |
| 12 | `12_Monitoring_and_Observability.md` | `OBS` |
| 13 | `13_Analytics_and_ProductMetrics.md` | `ANL` |
| 14 | `14_Release_and_LaunchReadiness.md` | `LAUNCH` |

### Frontend — general client and browser checks (01–20)

General UI, accessibility, browser/API-consumer, SEO, and frontend operations checks belong here. **AI-specific UI checks, including fine-tuning/training dashboards, are owned by their corresponding files under `lists/AI/` in a `## Frontend Checks` section.** Match domains across scopes by their descriptive suffix or stable checklist ID prefix, not their local file number.

| # | Filename | Checklist ID prefix | Domain total |
| ---: | --- | --- | ---: |
| 01 | `01_Requirements_and_Planning.md` | `REQ` | 83 |
| 02 | `02_LegalIssues.md` | `LEG` | 74 |
| 03 | `03_Architecture_and_CodeQuality.md` | `ARC` | 96 |
| 04 | `04_UI_UX_and_Usability.md` | `UX` | 103 |
| 05 | `05_Accessibility.md` | `A11Y` | 112 |
| 06 | `06_Internationalization_and_Localization.md` | `I18N` | 122 |
| 07 | `07_API_Design_and_Integrations.md` | `APID` | 120 |
| 08 | `08_Data_and_DatabaseManagement.md` | `DATA` | 158 |
| 09 | `09_Security.md` | `SEC` | 121 |
| 10 | `10_Documentation_and_DeveloperExperience.md` | `DOC` | 122 |
| 11 | `11_Testing.md` | `TST` | 84 |
| 12 | `12_Performance_and_Scalability.md` | `PERF` | 106 |
| 13 | `13_SEO.md` | `SEO` | 87 |
| 14 | `14_GEO_and_AEO.md` | `GEO` | 81 |
| 15 | `15_DevOps_and_CI_CD.md` | `OPS` | 114 |
| 16 | `16_Reliability_and_DisasterRecovery.md` | `REL` | 115 |
| 17 | `17_Monitoring_and_Observability.md` | `OBS` | 119 |
| 18 | `18_Analytics_and_ProductMetrics.md` | `ANL` | 146 |
| 19 | `19_Cost_and_FinOps.md` | `COST` | 128 |
| 20 | `20_Release_and_LaunchReadiness.md` | `LAUNCH` | 133 |

### Backend — server and API checks (01–35)

Backend maintains the 35-domain inventory, including domain-specific AI service/API integration checks. A matching frontend file is **not** implied. Existing API-domain files remain in backend until separately reviewed.

| # | Filename | Checklist ID prefix | Domain total |
| ---: | --- | --- | ---: |
| 01 | `01_Requirements_and_Planning.md` | `REQ` | 83 |
| 02 | `02_LegalIssues.md` | `LEG` | 74 |
| 03 | `03_Architecture_and_CodeQuality.md` | `ARC` | 96 |
| 04 | `04_UI_UX_and_Usability.md` | `UX` | 103 |
| 05 | `05_Accessibility.md` | `A11Y` | 112 |
| 06 | `06_Internationalization_and_Localization.md` | `I18N` | 122 |
| 07 | `07_API_Design_and_Integrations.md` | `APID` | 120 |
| 08 | `08_Data_and_DatabaseManagement.md` | `DATA` | 158 |
| 09 | `09_Security.md` | `SEC` | 121 |
| 10 | `10_AI_Evaluation_and_Governance.md` | `AIG` | 130 |
| 11 | `11_AI_Model_Selection_and_Benchmarking.md` | `MODELS` | 134 |
| 12 | `12_AI_Data_Curation_and_Labeling.md` | `CUR` | 132 |
| 13 | `13_AI_Model_and_Dataset_Cards.md` | `CARDS` | 130 |
| 14 | `14_AI_FineTuning_and_Training.md` | `TRAIN` | 132 |
| 15 | `15_Prompt_Engineering_and_Versioning.md` | `PROMPT` | 132 |
| 16 | `16_RAG_and_Knowledge_Bases.md` | `RAG` | 128 |
| 17 | `17_AI_Agents_and_Tool_Orchestration.md` | `AGENT` | 141 |
| 18 | `18_AI_Inference_and_Serving.md` | `SERVE` | 132 |
| 19 | `19_Multimodal_AI_Quality.md` | `MULTI` | 134 |
| 20 | `20_AI_Human_Review_and_Escalation.md` | `HUMAN` | 132 |
| 21 | `21_AI_Evaluation_and_Regression.md` | `EVAL` | 136 |
| 22 | `22_AI_Red_Teaming_and_Guardrails.md` | `RED` | 136 |
| 23 | `23_MLOps_and_Model_Lifecycle.md` | `MLOPS` | 130 |
| 24 | `24_AI_Monitoring_and_Drift.md` | `DRIFT` | 132 |
| 25 | `25_Documentation_and_DeveloperExperience.md` | `DOC` | 122 |
| 26 | `26_Testing.md` | `TST` | 84 |
| 27 | `27_Performance_and_Scalability.md` | `PERF` | 106 |
| 28 | `28_SEO.md` | `SEO` | 87 |
| 29 | `29_GEO_and_AEO.md` | `GEO` | 81 |
| 30 | `30_DevOps_and_CI_CD.md` | `OPS` | 114 |
| 31 | `31_Reliability_and_DisasterRecovery.md` | `REL` | 115 |
| 32 | `32_Monitoring_and_Observability.md` | `OBS` | 119 |
| 33 | `33_Analytics_and_ProductMetrics.md` | `ANL` | 146 |
| 34 | `34_Cost_and_FinOps.md` | `COST` | 128 |
| 35 | `35_Release_and_LaunchReadiness.md` | `LAUNCH` | 133 |

### AI — AI-specific checks (01–22)

| # | Filename | Checklist ID prefix |
| ---: | --- | --- |
| 01 | `lists/AI/01_Requirements_and_Planning.md` | `REQ` |
| 02 | `lists/AI/02_LegalIssues.md` | `LEG` |
| 03 | `lists/AI/03_AI_Evaluation_and_Governance.md` | `AIG` |
| 04 | `lists/AI/04_Security.md` | `SEC` |
| 05 | `lists/AI/05_AI_Model_Selection_and_Benchmarking.md` | `MODELS` |
| 06 | `lists/AI/06_AI_Data_Curation_and_Labeling.md` | `CUR` |
| 07 | `lists/AI/07_AI_Model_and_Dataset_Cards.md` | `CARDS` |
| 08 | `lists/AI/08_AI_FineTuning_and_Training.md` | `TRAIN` |
| 09 | `lists/AI/09_Prompt_Engineering_and_Versioning.md` | `PROMPT` |
| 10 | `lists/AI/10_RAG_and_Knowledge_Bases.md` | `RAG` |
| 11 | `lists/AI/11_AI_Agents_and_Tool_Orchestration.md` | `AGENT` |
| 12 | `lists/AI/12_AI_Inference_and_Serving.md` | `SERVE` |
| 13 | `lists/AI/13_Multimodal_AI_Quality.md` | `MULTI` |
| 14 | `lists/AI/14_AI_Human_Review_and_Escalation.md` | `HUMAN` |
| 15 | `lists/AI/15_AI_Evaluation_and_Regression.md` | `EVAL` |
| 16 | `lists/AI/16_AI_Red_Teaming_and_Guardrails.md` | `RED` |
| 17 | `lists/AI/17_MLOps_and_Model_Lifecycle.md` | `MLOPS` |
| 18 | `lists/AI/18_AI_Monitoring_and_Drift.md` | `DRIFT` |
| 19 | `lists/AI/19_Cost_and_FinOps.md` | `COST` |
| 20 | `lists/AI/20_Analytics_and_ProductMetrics.md` | `ANL` |
| 21 | `lists/AI/21_GEO_and_AEO.md` | `GEO` |
| 22 | `lists/AI/22_Release_and_LaunchReadiness.md` | `LAUNCH` |

**Totals:** 4,215 unique checks across 91 populated scope files: 14 shared/root files (701 checks), 20 frontend files (684 checks), 35 backend files (1,118 checks), and 22 AI files (1,712 checks). Checklist IDs remain stable when file numbers change. Do not count repeated metadata, source lists, and release-gate text as checks.

## Current state and design decisions

- **Filename convention:** Two-digit, zero-padded prefixes are **frozen folder-local filename labels**, not stable domain IDs. Existing folders are currently contiguous, but new files append the next unused prefix and retired filenames may leave gaps; frontend has 20 general UI/client domain files, backend 35 server/API domain files, and root and case-sensitive `lists/AI/` retain their independent order. Match corresponding checklists across folders by **descriptive suffix and checklist ID prefix**, not by filename number. Keep exact checklist item IDs unchanged.
- **Last repository-guidance update:** 2026-11-15.
- **Security IDs:** SEC-009 now addresses session expiration, with new SEC-110–SEC-112 for rotation, logout revocation and recovery tokens. SEC-010 now addresses login brute-force, with SEC-113–SEC-115 for signup, recovery and verification-message abuse. No previous IDs were deleted. The full SEC domain spans 115 IDs across scope slices.
- **Verification:** Use `python3 skills/awesome-checklists/scripts/lint_repository.py` to check local Markdown targets **and #heading anchors**, required `Release gate` / `Trusted references and scope` sections, dated source metadata, ID uniqueness, ownership registry and source formatting. Both GitHub Actions workflows are disabled; run this and the unit tests locally.
- **Atomicity update:** Shared `SEC-006` now covers vetted authentication libraries; new `SEC-102` covers privileged MFA and `SEC-103` covers password hashing. Shared `SEC-017` now defines audit scope; new `SEC-104`–`SEC-109` separately address static analysis, secret scanning, dynamic testing, independent validation, remediation and evidence coverage. All previous IDs remain in place; total checks increased by eight. Other compound controls still require domain-specific editorial review, not naive automatic clause splitting. Generate a reproducible candidate list with `python3 skills/awesome-checklists/scripts/audit_compound_checks.py --output compound-candidates.json` and manually verify independently testable facets before assigning new IDs.
- **Prioritization:** The [Core 50](../../lists/references/core-50.md) is a documented, project-adjustable starter selection. The 50 Core checks retain manually curated P0/P1/P2 ratings. The other 4,165 IDs now display *provisional text-derived* starting tiers requiring manual risk review, not low-severity defaults. Do not infer a global severity label, auto-approve a release, or claim semantic deduplication from unique stable IDs.
- **Third-party skills:** Skill links in checklists are leads for further verification, not endorsements. Evaluate actual source, maintainer provenance, license, dependencies, permissions, pinned revisions, compatibility and safe execution before using them. Do not use GitHub star counts as a security-vetting proxy.
- **Review traceability:** Keep [CHANGELOG.md](../../CHANGELOG.md) current for changes to checks, IDs, priority metadata, scope moves, export behavior and release guidance. No review-record example supersedes project evidence or accountable human sign-off.
- **Scope split:** The checklist collection now contains **14 shared files in `lists/`**, **20 frontend files**, **35 backend files**, and **22 AI files**; **91 populated scope files** in total. Across them are **4,215 unique checks**: **701 shared**, **684 frontend**, **1,118 backend**, and **1,712 AI**. The 300 AI-domain frontend checks were consolidated into matching AI files without changing the stable checklist IDs; only frontend file prefixes 25–35 were renumbered to 10–20.
- **Scope classification:** Route by the actual accountable implementation/review surface, not merely a technical keyword or the domain's filename. Core API specification/contract, database schema, storage, migration, and data-platform operations are backend-led. Interface/API-consumer behavior, browser-local databases, UI/UX, accessibility, SEO, and GEO/AEO content/discovery checks are frontend-led, with editorial, legal, and analytics collaborators as appropriate. AI model, training, RAG, and agent-specific work—including their specialized frontend UX, administration, and client-facing evaluation checks—belongs under `lists/AI/` in domain-specific sections. Domain-specific server/API companion checks currently remain under `lists/backend/`. Organizational policy, cross-layer measurement and quality, privacy/legal decisions, release approval, and other genuinely cross-cutting work belongs in shared templates directly under `lists/` where a shared file exists. Cross-cutting ownership can still apply when a backend-/frontend-led domain has no root file; list the appropriate reviewers in project-specific notes. Do not duplicate a checklist ID across folders.
- **Structure:** Each numbered file now links to the shared review method and optional compliance crosswalk. Repeated `## Review details`, `## How to use`, and end-of-file warning blocks have been centralized to improve scanability; preserve domain-specific checklist criteria, `## Release gate`, and `## Trusted references and scope`. Domain release gates must still be evaluated across **all applicable scope slices**, never treated as independent sign-offs.
- **Missing files:** A domain missing from a folder has no checks for that scope; do not create an empty placeholder or leave numbering gaps. Its number may identify a different domain in another folder. `README.md` provides the project overview, entry points, usage guidance, and contribution invitation.
- Checklist IDs are stable references used in review notes and issue trackers. IDs should not be renumbered merely because new checks are added to earlier sections.
- **Do not add an `Evidence and exceptions` section or inline evidence table to the shared checklists.** This section was intentionally removed on 2026-11-12 to keep templates focused on actionable checks.
- Review evidence, N/A rationales, risk acceptances, and issue links belong in **project-specific review notes or an issue tracker**, keyed by checklist ID. Release-gate sign-off still requires sufficient evidence and reviewer approval.
- Existing checks are guided by cited primary/authoritative sources such as OWASP, W3C, OpenAPI/IETF standards, NIST, privacy regulators, and Google Search Central. Source references are starting points, not a universal compliance guarantee; validate dates, versions, availability, and jurisdiction.
- The repository's `README.md` is its reader-facing overview. Keep its scope links, counts, usage advice, limitations, and contribution guidance in sync with the maintained checklist inventory and repository practices.

## Domain ownership and routing examples

- **Backend primary:** `lists/backend/07_API_Design_and_Integrations.md` owns API contracts, provider integrations, versioning, and server-side API lifecycle. `lists/backend/08_Data_and_DatabaseManagement.md` owns database architecture, data stewardship, retention operations, migrations, constraints, data quality, and resilience.
- **Frontend primary:** `lists/frontend/04_UI_UX_and_Usability.md`, `lists/frontend/05_Accessibility.md`, and `lists/frontend/13_SEO.md`, and `lists/frontend/14_GEO_and_AEO.md` own their frontend checks. Retain `lists/frontend/07_API_Design_and_Integrations.md` for browser/API-client behavior and `lists/frontend/08_Data_and_DatabaseManagement.md` for data-oriented UI and IndexedDB/offline storage; these are not database-server controls.
- **Mixed-domain examples:** Keep cross-layer performance budgets in root `09_Performance_and_Scalability.md`, client performance in `lists/frontend/12_Performance_and_Scalability.md`, and backend throughput/scaling in `lists/backend/27_Performance_and_Scalability.md`. Shared service objectives, policy, release decisions, localization scope, and analytics governance remain in their corresponding root-domain files where populated.
- **Preservation:** Never create an empty root placeholder simply to have a file for every number. A domain is represented by its populated scope files, the inventory above, and globally stable checklist IDs. If an issue affects both client and server, make two new checks only when they have genuinely separate acceptance evidence; otherwise place the single shared requirement in a suitable root domain file.

