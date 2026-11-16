# 17 — AI Agents and Tool Orchestration Checklist

> Verify that AI agents achieve bounded tasks through permitted tools, safe handoffs, controlled state, and meaningful human supervision. The model may propose plans and actions, but independent application controls must enforce access, approvals, budgets, and actual execution.

> **Scope: Backend / API-specific.** This file is one part of the 17_AI_Agents_and_Tool_Orchestration.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

> **Cross-scope ID map:** This API-specific section owns `AGENT-095`–`AGENT-116`. The [general AI agent controls](../AI/11_AI_Agents_and_Tool_Orchestration.md) contain `AGENT-001`–`AGENT-094` and the `AGENT-117`–`AGENT-141` AI-owned range (frontend `117`–`136`; tool-validation `137`–`141`). [Verified domain map](../references/agent-domain-map.md).

## API Checks

- [ ] **AGENT-095** `P1` Expose only the approved agent workflows and tool operations through authenticated, versioned API contracts.
- [ ] **AGENT-096** `P1` Require server-side authorization for starting, inspecting, resuming, canceling, and approving agent runs.
- [ ] **AGENT-097** `P0` Enforce resource and tenant isolation across run IDs, tool call IDs, checkpoint IDs, and conversation identifiers.
- [ ] **AGENT-098** `P1` Validate tool call arguments and all model-supplied routing metadata against trusted schemas.
- [ ] **AGENT-099** `P1` Test that agent API consumers cannot fabricate an approval or bypass a pending human decision.
- [ ] **AGENT-100** `P1` Check approval binding to current run, tool identity, precise arguments, and authenticated reviewer.
- [ ] **AGENT-101** `P1` Prevent untrusted callers from injecting serialized run state or editing pending approval decisions.
- [ ] **AGENT-102** `P1` Use stable idempotency keys and authoritative status checks to avoid repeated external actions after retry or resume.
- [ ] **AGENT-103** `P2` Define run lifecycle states including queued, running, waiting for approval, completed, failed, canceled, and partially completed.
- [ ] **AGENT-104** `P2` Document consistent API error states for invalid tools, policy denial, quota exhaustion, timeout, and unrecoverable failures.
- [ ] **AGENT-105** `P1` Enforce per-run limits on steps, token usage, tool calls, concurrency, wall-clock time, and cost.
- [ ] **AGENT-106** `P1` Apply per-tool rate limits, timeouts, permitted destinations, and network isolation independently of prompt instructions.
- [ ] **AGENT-107** `P1` Validate external API responses before returning them to an agent as tool results.
- [ ] **AGENT-108** `P1` Test nested agent handoffs and background tasks for preserved authorization and correct context filtering.
- [ ] **AGENT-109** `P1` Trace model, tool, guardrail, handoff, and approval events with correlation IDs without logging confidential payloads by default.
- [ ] **AGENT-110** `P1` Check that stream events and partial API results do not falsely report a tool action as executed before confirmation.
- [ ] **AGENT-111** `P1` Implement cancellation and stop procedures that reach queued tasks and active integrations when possible.
- [ ] **AGENT-112** `P1` Exercise failure and retry scenarios for payments, publishing, deletion, messaging, and other non-idempotent actions as applicable.
- [ ] **AGENT-113** `P1` Ensure connector secrets and delegated tokens are absent from API responses, error messages, and logs.
- [ ] **AGENT-114** `P1` Verify deployed tool inventories, versions, approval policies, and agents match the approved release configuration.
- [ ] **AGENT-115** `P1` Monitor excessive tool loops, anomalous privilege requests, denied calls, and unexpected outbound destinations.
- [ ] **AGENT-116** `P1` Test that deactivated users, revoked permissions, and expired delegations cannot resume privileged actions.

## Release gate

- [ ] The agent's business purpose, task boundaries, permitted tools, authorized user population, run limits, and responsible owners are documented and reviewed.
- [ ] Tool and connector inventory, least-privilege scopes, tenant boundaries, schema validation, and external execution/network restrictions have been tested against unauthorized access and tool misuse.
- [ ] Representative end-to-end tasks meet agreed outcome and severe-error criteria, including blocked objectives, malformed tool data, and adversarial indirect instructions.
- [ ] Routing and handoff tests confirm that specialist agents cannot gain extra privileges, improperly disclose context, or bypass normal approval and resource limits.
- [ ] High-impact tool calls require authenticated, action-specific human approval bound to exact parameters; rejected, expired, changed, or replayed approvals do not execute.
- [ ] Cancellation, shutdown, crash recovery, duplicate delivery, and partial external side effects have tested safe outcomes or a documented compensating/escalation procedure.
- [ ] API and frontend consumers can distinguish proposed actions from confirmed execution and handle pauses, refusals, errors, and partial completion safely.
- [ ] Monitors, alerts, incident response, execution traces, cost and throughput limits, and emergency tool revocation are operational with named responders.
- [ ] Material unresolved authority, user-harm, privacy, prompt-injection, or side-effect risks are resolved or have an explicitly authorized and time-bound disposition.

**Domain-specific approval rule:** Block sign-off if an agent can reach unauthorized data or tools, autonomously cross approved scope, execute material unapproved side effects, resume with forged authority, or replay irreversible actions without accepted controls. Passing the checklist does not imply that agents are infallible, that actions are exactly once, or that a specific security or regulatory certification has been achieved.

**Optional testing guidance:** [Agent test scenarios, evidence examples and vetted-tool cautions](../references/agent-testing-tools.md). Third-party tools are not required or approved by default.

## Trusted references and scope

The following primary and authoritative sources inform these practical review checks. Their SDK-specific details should be mapped to the actual framework and deployment environment rather than assumed to apply universally.

- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents) — workflows versus agents, composable orchestration, tool design, and task-scoped autonomy.
- [OpenAI Agents SDK — Overview](https://openai.github.io/openai-agents-python/) — agent loops, tools, handoffs, guardrails, sessions, and tracing.
- [OpenAI Agents SDK — Running agents](https://openai.github.io/openai-agents-python/running_agents/) — agent turn loop, execution and session configuration, errors, and recovery.
- [OpenAI Agents SDK — Handoffs](https://openai.github.io/openai-agents-python/handoffs/) — routing, structured handoff metadata, delegated context, and authorization boundaries.
- [OpenAI Agents SDK — Human in the loop](https://openai.github.io/openai-agents-python/human_in_the_loop/) — per-call approvals, trusted snapshots, resume integrity, and replay risks.
- [OpenAI Agents SDK — Tracing](https://openai.github.io/openai-agents-python/tracing/) — recording agent, tool, handoff, and guardrail operations.
- [MCP Specification 2026-07-28 — Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) — current stable tool discovery, schema handling and invocation; check actual negotiated protocol/SDK capabilities.
- [MCP Specification 2026-07-28 — Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index) — updated authorization and transport security requirements; apply to the negotiated implementation.
- [MCP Specification 2026-07-28 — Changes since 2025-11-25](https://modelcontextprotocol.io/specification/2026-07-28/changelog) — stateless core, changed connection/session semantics, metadata, auth and protocol compatibility.
- [OWASP — Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) — goal hijacking, tool misuse, identity abuse, memory poisoning, cascading failures, and rogue agents.
- [OWASP — Agentic AI Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) — agent-specific threat modeling and least-privilege mitigations.
- [NIST AI RMF Playbook — Manage](https://airc.nist.gov/airmf-resources/playbook/manage/) — risk treatment, human accountability, deployment decisions, and ongoing monitoring.
- [Microsoft Agent Framework — Tool approval](https://learn.microsoft.com/en-us/agent-framework/agents/tools/tool-approval) — tool-specific approval binding, human decisions, and safe resume mechanics.
- [Microsoft Agent Framework — Human-in-the-loop workflows](https://learn.microsoft.com/en-us/agent-framework/workflows/human-in-the-loop) — pause-and-resume workflow state, checkpoints, and interactive approvals.
- [OpenTelemetry — Generative AI attribute registry](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/) — agent/tool telemetry attributes and sensitive-content safeguards.

**Applicability:** MCP tool discovery is not permission to invoke every available function. The July 2026 specification supersedes November 2025; protocol versions can differ across installed SDKs and negotiated transports. Verify implementation behavior and authorization requirements against the negotiated version. Do not assume older protocol-level session or initialization behavior applies to 2026-07-28. OpenAI and Microsoft agent approvals must be implemented with server-owned decisions and current permission checks; resuming a previously approved run does not ensure exactly-once external side effects. OpenTelemetry conventions describe instrumentation but do not justify storing protected prompts or tool payloads. OWASP risk lists and NIST AI RMF practices support threat modeling and governance rather than certifying deployment safety. Anthropic's 2024 orchestration article carries an explicit notice that tooling has evolved.

**Source review date:** 2026-11-12; MCP stable specification and version-compatibility guidance checked 2026-11-15.
