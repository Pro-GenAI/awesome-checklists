# Historical ideas and maintenance backlog

**Candidate ideas only** — not approved scope or requirements. Consult [AGENTS.md](../../AGENTS.md) and [CONTRIBUTING.md](../../CONTRIBUTING.md) before promoting any note to a checklist. This section preserves earlier suggestions; it does not confer permission to execute third-party tools or create new controls without evidence.

## Suggested future maintenance and expansion

- All 35 domain basenames are represented across the scopes (not every folder), but only 15 have a root copy. Add new checks when requested (including online-content updates), preserving primary scope ownership, stable IDs, cross-folder uniqueness, domain-wide release gates, and authoritative sources.
- AI-specific controls occupy a **folder-local** sequence under `lists/AI/` (01–22); AI-specific frontend integration checks now live under each AI file's `## Frontend Checks`, while the existing server/API companion checks remain in `lists/backend/`. Avoid overlap with `lists/AI/03_AI_Evaluation_and_Governance.md`.
- Add checks only where meaningful gaps are identified; prioritize API schema evolution, test observability, frontend accessibility, and project-specific risk.
- Recheck trusted-source links and revisions periodically; update source review dates only after genuine re-verification.
- If needed, propose project-specific usage examples or automation in separate, explicitly requested work rather than modifying template structure by default.

## Suggested testing-tool appendices (2026-11-12)

All **91 current numbered checklist files** include a `## Suggested testing tools` appendix: 14 root, 20 frontend, 35 backend, and 22 AI files. The appendices provide domain-specific testing focus, links to cross-stack tools, language-specific Python, TypeScript, and JavaScript options, example suite commands, and project-specific evidence-recording guidance. These are **optional tool recommendations**, not new checklist items or a substitute for specialist review, standards verification, or release-gate sign-off. Adapt each recommendation to the project's architecture and verify the tool's maintenance and applicability before adoption.

**Maintenance entry — 2026-11-12:** Appended recommended testing tools to every populated scope checklist, preserving all 4,129 unique checklist IDs, checkbox states, scope assignments, existing trusted references, source review dates, and domain-wide release gates. No new check IDs were introduced. `README.md` remains intentionally minimal.

## AI skills for checklist verification (2026-11-12)

**Maintenance entry:** Appended `## Suggested AI skills for verification` to all **107 numbered scope checklists** (15 root, 35 frontend, 35 backend, 22 AI). Each file now links to **three relevant Agent Skills `SKILL.md` files** and gives a checklist-ID-based, evidence-first review workflow. At the time of the original 107-file split this was **321 skill placements** (now 92 files, 276 placements), drawn from **74 distinct skill files in 16 GitHub repositories**. Source skill paths were verified against the repositories' `main` trees. Only repositories with **at least 1,000 stars** in the GitHub API snapshot on **2026-11-12** were selected. Counts are repository-wide, not per-skill ratings; star counts are a popularity heuristic, not a trust, licensing, security, or accuracy endorsement.

| Repository | Stars at review |
| --- | ---: |
| [`mattpocock/skills`](https://github.com/mattpocock/skills) | 322,608 |
| [`obra/superpowers`](https://github.com/obra/superpowers) | 316,578 |
| [`anthropics/skills`](https://github.com/anthropics/skills) | 193,495 |
| [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) | 116,378 |
| [`coreyhaines31/marketingskills`](https://github.com/coreyhaines31/marketingskills) | 59,899 |
| [`wshobson/agents`](https://github.com/wshobson/agents) | 42,437 |
| [`github/awesome-copilot`](https://github.com/github/awesome-copilot) | 41,073 |
| [`vercel-labs/agent-skills`](https://github.com/vercel-labs/agent-skills) | 33,937 |
| [`openai/skills`](https://github.com/openai/skills) | 28,705 |
| [`google/skills`](https://github.com/google/skills) | 24,012 |
| [`trailofbits/skills`](https://github.com/trailofbits/skills) | 8,150 |
| [`remotion-dev/skills`](https://github.com/remotion-dev/skills) | 6,895 |
| [`cloudflare/skills`](https://github.com/cloudflare/skills) | 3,349 |
| [`microsoft/skills`](https://github.com/microsoft/skills) | 3,198 |
| [`daymade/claude-code-skills`](https://github.com/daymade/claude-code-skills) | 1,524 |
| [`rampstackco/claude-skills`](https://github.com/rampstackco/claude-skills) | 1,063 |

**Usage and scope:** These optional skills can help an appropriately configured AI agent propose and investigate checks; **they have not been installed, executed, or proven to satisfy the checklists**. Read each skill and its dependencies before giving an agent codebase or network access; limit privileges and independently validate outputs with tests and qualified reviewers. A project-specific copy should map findings, uncertainties, failures, and N/A rationales to the **original stable checklist IDs**. The reusable template checkboxes, all **4,129 existing unique IDs**, release gates, source-review dates, and original reference sections remain unchanged. Existing `## Suggested testing tools` appendices and the deliberately minimal `README.md` are preserved. Re-verify links and stars on subsequent maintenance rather than treating this snapshot as permanent.

## Reference-only warning policy (2026-11-12)

**Maintenance entry — 2026-11-12:** Appended a final `## Important warning: reference only` section to all **107 numbered checklists** (15 root, 35 frontend, 35 backend, and 22 AI). Every warning states that the checklist is a **starting point, not definitive, exhaustive, or the ultimate authority**; it does not guarantee safety, quality, compliance, accessibility, security, or launch readiness. Reviewers must adapt guidance to each project's risks and jurisdiction, verify current primary references, perform independent testing, and obtain appropriate expert review and approvals. Treat the warning as required final text in future checklist maintenance, after any tools or AI-skills appendices. All **4,129 original checklist IDs**, unchecked states, source-review dates, existing sections, and release gates remain unchanged. `README.md` remains intentionally minimal.
