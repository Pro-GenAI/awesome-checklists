# Minimum viable review — 25 checks per scope

A bounded **first-pass review**, not a universal security baseline, comprehensive certification, or substitute for an appropriate risk and legal assessment. The source contains **4,215 unique IDs** across 91 files. Four independent 25-check suggestions make it possible to start within one scope without working through an entire domain.

The existing standard-library [scoped review generator](../../skills/awesome-checklists/scripts/generate_review.py) produces each shortlist deterministically. All outcomes begin **UNKNOWN**, not PASS; no test has been executed merely by generating a report.

| Scope | Command | Intended use |
| --- | --- | --- |
| Shared / cross-cutting | `python3 skills/awesome-checklists/scripts/generate_review.py --profile startup --scope shared --size 25 --output shared-25.md` | Shared security, planning, testing and launch questions |
| Frontend | `python3 skills/awesome-checklists/scripts/generate_review.py --profile startup --scope frontend --size 25 --output frontend-25.md` | User journeys, accessibility and browser-facing risks |
| Backend | `python3 skills/awesome-checklists/scripts/generate_review.py --profile startup --scope backend --size 25 --output backend-25.md` | APIs, authorization, data integrity and operations |
| AI | `python3 skills/awesome-checklists/scripts/generate_review.py --profile startup --scope AI --size 25 --output ai-25.md` | Model evaluation, RAG/agents and AI-specific safeguards (opt in when applicable) |

To focus specifically on agents, use `python3 skills/awesome-checklists/scripts/generate_review.py --scope AI --domain AGENT --size 25 --output agent-25.md`. These are **25 candidate general/agent and frontend IDs** from the AI scope; the separate [backend AGENT API slice](../backend/17_AI_Agents_and_Tool_Orchestration.md#api-checks) has **22** relevant IDs and should be reviewed when that API is deployed. It is deliberately not padded with unrelated checks merely to reach 25. See the [cross-scope AGENT ID map](agent-domain-map.md).

## Selection limitations

The starter profile uses existing IDs, core-curated tier context, provisional tiers and reproducible topical weighting. Selection is **not expert-derived risk prioritization** for your company or industry. It does not automatically include all applicable P0 items, legal obligations, launch blockers or external standards. Before acting, a reviewer must assign risk, add required checks and release gates, record each result with direct evidence, and obtain a separate authorized go/no-go decision.

For a larger project, repeat `--scope` options and use `--size 50` or `--size 100`. A small regulated product may have more mandatory controls than a 25-check starter can contain. See the [generator usage guide](scoped-review-generator.md), [review method](review-method.md), and [worked source-inspection review](example-review.md). The worked example is narrowly bounded, not an external product audit.

The generator does not alter the original unchecked templates or provide a badge/certification.
