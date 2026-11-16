# Agent Safety & Runtime Guardrails — drop-in review checklist

<!-- SPDX-License-Identifier: CC0-1.0 -->
Copy these unchecked items into a project PR description or issue. Each item maps to a stable ID in the canonical library. Mark as complete **only after** recording project-specific evidence; a checkbox is not certification.

- [ ] **AGENT-026** — Reject tool calls outside the trusted tool registry. [Canonical check](../../lists/AI/11_AI_Agents_and_Tool_Orchestration.md). *Why:* Prevents agent output from inventing executable capabilities.
- [ ] **AGENT-043** — Authorize high-impact tool actions in deterministic policy code. [Canonical check](../../lists/AI/11_AI_Agents_and_Tool_Orchestration.md). *Why:* Prevents model suggestions from bypassing user or service permissions.
- [ ] **AGENT-034** — Test injection attempts to redirect tools or reveal secrets. [Canonical check](../../lists/AI/11_AI_Agents_and_Tool_Orchestration.md). *Why:* Finds trust-boundary failures before delegating user authority.
- [ ] **AGENT-055** — Trace run and parent-child IDs across calls and handoffs. [Canonical check](../../lists/AI/11_AI_Agents_and_Tool_Orchestration.md). *Why:* Makes multi-agent failures and action provenance auditable.
- [ ] **SERVE-057** — Prevent irreversible actions from partial unvalidated streams. [Canonical check](../../lists/AI/12_AI_Inference_and_Serving.md). *Why:* Prevents streaming output from triggering premature side effects.

**Review record:** Target revision: `UNKNOWN` · Checklist source revision: `UNKNOWN` · Reviewer/approver: `UNKNOWN` · Evidence/exception links: `UNKNOWN`.

See [catalog.json](catalog.json) for machine-readable stage, contextual priority hint, severity and proposed integration signals. These are **not** pre-run checks or universal release gates.
