# 20 — AI Human Review and Escalation Checklist

> Ensure human involvement in AI-assisted decisions is meaningful, authorized, timely, and auditable. A review button, nominal human sign-off, or the ability to view model output does not establish independent oversight or prevent unauthorized downstream execution.

> **Scope: Backend / API-specific.** This file is one part of the 20_AI_Human_Review_and_Escalation.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## API Checks

- [ ] **HUMAN-093** `P1` Require authenticated and purpose-authorized API access to create, view, claim, approve, reject, and escalate review cases.
- [ ] **HUMAN-094** `P1` Enforce tenant, user, object, action, and reviewer-role authorization for every case and decision mutation.
- [ ] **HUMAN-095** `P1` Validate server-owned pending action identifiers and stored tool arguments rather than trusting replacements supplied by clients.
- [ ] **HUMAN-096** `P1` Bind decision records to immutable or version-checked proposed actions and reject stale approvals after material changes.
- [ ] **HUMAN-097** `P1` Use atomic transitions, concurrency controls, and replay protection for approvals consumed by resumed agent runs.
- [ ] **HUMAN-098** `P1` Require reauthorization and independent server-side policy checks before executing a reviewed tool call.
- [ ] **HUMAN-099** `P1` Ensure denied, timed-out, and expired review cases cannot be executed by a retry or alternate endpoint.
- [ ] **HUMAN-100** `P1` Test handoff and nested-agent approval paths for the same authority and policy checks as top-level actions.
- [ ] **HUMAN-101** `P2` Define explicit review states such as queued, assigned, waiting, escalated, approved, rejected, expired, and executed.
- [ ] **HUMAN-102** `P1` Keep API representations of approval, execution, partial completion, and actual external outcome distinct.
- [ ] **HUMAN-103** `P1` Validate role and policy changes invalidate relevant outstanding approvals and reviewer access.
- [ ] **HUMAN-104** `P1` Use scoped credentials, rate limits, idempotency controls, and resource budgets on review-related APIs.
- [ ] **HUMAN-105** `P1` Test server behavior for malformed decisions, duplicate submissions, stale browser sessions, and missing evidence.
- [ ] **HUMAN-106** `P2` Record safe audit identifiers for pending calls, decisions, reviewer authority, state transitions, and execution outcomes.
- [ ] **HUMAN-107** `P1` Prevent unauthorized exposure of private case content in logs, traces, response caches, webhooks, or exported review reports.
- [ ] **HUMAN-108** `P1` Protect review and appeal event delivery against spoofing, duplication, tampering, and out-of-order processing.
- [ ] **HUMAN-109** `P1` Ensure policy violations and serious incidents trigger trusted escalation or containment independently of the model.
- [ ] **HUMAN-110** `P1` Exercise graceful failure when reviewer identity, approval storage, or audit infrastructure is unavailable.
- [ ] **HUMAN-111** `P1` Validate integration contracts for external human-review vendors, including data-handling and permitted reviewer access.
- [ ] **HUMAN-112** `P1` Test production-equivalent end-to-end review, approval, rejection, timeout, cancellation, and recovery paths before release.

## Release gate

- [ ] Documented decision categories identify which AI outcomes require human intervention, specialist review, dual control, or immediate suspension according to impact and applicable law.
- [ ] Qualified reviewers have real access to the necessary evidence, time, training, authority, and accessible controls to approve, reject, change, escalate, or stop a decision.
- [ ] Review queues, prioritization, assignment, decision thresholds, staffing, expirations, and safe backlog/outage behavior have been tested under representative workload.
- [ ] Approval, denial, and override controls are bound to authenticated, authorized reviewers and the exact action parameters; stale, replayed, forged, and changed requests cannot execute.
- [ ] Significant decisions, reviewer disagreements, appeals, overrides, completed actions, and incident escalation are traceable with appropriate privacy, integrity, and retention safeguards.
- [ ] Human-review effectiveness and potential automation bias have been evaluated with representative benign, ambiguous, and high-impact cases, including false approvals and unjustified rejections.
- [ ] API and frontend pathways accurately distinguish proposals from confirmed effects and handle waiting, denial, timeout, failed resume, cancellation, and correction accessibly.
- [ ] A named risk owner has reviewed residual limitations, complaint/redress obligations where applicable, response runbooks, emergency halt mechanisms, and the exact release configuration.

**Domain-specific approval rule:** Block release if human review is legally or risk-required but the reviewer cannot independently challenge or stop outcomes; if unapproved, altered, or replayed actions can execute; if high-impact cases can be silently auto-approved during overload; or if mandatory records and escalation routes are unavailable. Human oversight must be proportionate and effective, not merely ceremonial.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#20_ai_human_review_and_escalation), not prerequisites or verification evidence.

## Trusted references and scope

The primary standards, laws, risk-management guidance, and implementation references below inform the checklist. Apply vendor features and legal requirements only where relevant to the particular application and deployment.

- [NIST AI RMF Playbook — Govern](https://airc.nist.gov/airmf-resources/playbook/govern/) — human-AI oversight roles, reviewer competence, accountability, and appeal/override processes.
- [NIST AI RMF Playbook — Manage](https://airc.nist.gov/airmf-resources/playbook/manage/) — risk-based incident handling, escalation, mitigation, and continuing oversight.
- [EU AI Act (Regulation 2024/1689) — Article 14 and Article 26](https://eur-lex.europa.eu/eli/reg/2024/1689) — risk-proportionate human oversight and deployer responsibilities for applicable high-risk systems; check current application dates.
- [EU GDPR (Regulation 2016/679) — Article 22](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) — rules on significant solely automated decisions and relevant human intervention or contestation safeguards where applicable.
- [OpenAI Agents SDK — Human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/) — review interruptions, parameter-bound tool approval, sticky-decision scope, secure resume and replay prevention.
- [OpenAI Agents SDK — Run state](https://openai.github.io/openai-agents-python/ref/run_state/) — durable paused-run state, serialized context, restoration risks, and approval integrity.
- [Microsoft Agent Framework — Tool approval](https://learn.microsoft.com/en-us/agent-framework/agents/tools/tool-approval) — approval-required tools, sessions, standing approvals, and middleware scope.
- [Microsoft Agent Framework — Human-in-the-loop workflows](https://learn.microsoft.com/en-us/agent-framework/workflows/human-in-the-loop) — workflow pause/resume, human decisions, and orchestration approval paths.
- [OWASP — AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) — high-impact action authorization, approval integrity, least privilege and incident handling.
- [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/) — accessible reviewer interfaces, input controls, focus, status messaging and navigation.
- [OECD — AI Principles](https://oecd.ai/en/ai-principles) — human-centred oversight, transparency, accountability, and risk management.
- [NIST AI RMF Playbook — Map](https://airc.nist.gov/airmf-resources/playbook/map/) — context and impact assessment that determines meaningful oversight requirements.

**Applicability:** The NIST AI RMF is voluntary. The EU AI Act imposes Article 14 oversight design requirements and Article 26 deployer obligations for applicable high-risk AI systems; its implementation and application dates require current, qualified legal review and are not identical for all AI products. GDPR Article 22 applies in specific circumstances involving solely automated decisions with legal or similarly significant effects, including exceptions and safeguards; not every AI suggestion triggers that article. OpenAI Agents SDK and Microsoft Agent Framework approval facilities have different behavior for reused/standing approvals, nested agents, saved state, and resumed tool calls. Their native controls must be supplemented with trusted application authorization, concurrency controls, replay prevention, and recovery of external side effects. WCAG 2.2 requirements depend on the applicable conformance target and governing accessibility law.

**Source review date:** 2026-11-12.
