# Evaluation & Observability — drop-in review checklist

<!-- SPDX-License-Identifier: CC0-1.0 -->
Copy these unchecked items into a project PR description or issue. Each item maps to a stable ID in the canonical library. Mark as complete **only after** recording project-specific evidence; a checkbox is not certification.

- [ ] **EVAL-023** — Version golden evaluation cases with expected outcomes. [Canonical check](../../lists/AI/15_AI_Evaluation_and_Regression.md). *Why:* Prevents silent test-dataset drift across prompt and model releases.
- [ ] **EVAL-047** — Use deterministic assertions for schemas, tool calls and refusals. [Canonical check](../../lists/AI/15_AI_Evaluation_and_Regression.md). *Why:* Catches contract failures that subjective model scores can miss.
- [ ] **EVAL-066** — Score retrieval relevance separately from groundedness and citations. [Canonical check](../../lists/AI/15_AI_Evaluation_and_Regression.md). *Why:* Prevents a good answer score from concealing retrieval regressions.
- [ ] **DRIFT-008** — Monitor end-to-end and time-to-first-output latency. [Canonical check](../../lists/AI/18_AI_Monitoring_and_Drift.md). *Why:* Finds queue, stream and orchestration slowdowns unseen by model metrics.
- [ ] **DRIFT-010** — Monitor billable tokens, requests and provider usage. [Canonical check](../../lists/AI/18_AI_Monitoring_and_Drift.md). *Why:* Detects unexpected spend and inefficient retries.

**Review record:** Target revision: `UNKNOWN` · Checklist source revision: `UNKNOWN` · Reviewer/approver: `UNKNOWN` · Evidence/exception links: `UNKNOWN`.

See [catalog.json](catalog.json) for machine-readable stage, contextual priority hint, severity and proposed integration signals. These are **not** pre-run checks or universal release gates.
