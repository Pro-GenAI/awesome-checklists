# 11 — AI Agents and Tool Orchestration Checklist

> Verify that AI agents achieve bounded tasks through permitted tools, safe handoffs, controlled state, and meaningful human supervision. The model may propose plans and actions, but independent application controls must enforce access, approvals, budgets, and actual execution.

> **Scope: AI-specific.** This file is one part of the 11_AI_Agents_and_Tool_Orchestration.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

> **Atomicity update:** `AGENT-043` now covers consequential-action permissions only; independent human approval and enforcement are covered by `AGENT-073`, `AGENT-075`–`AGENT-078`, and `AGENT-083`. Prior `AGENT-043` PASS records must be reassessed against those IDs.

> **Tool input atomicity:** `AGENT-026` covers tool-name rejection only; `AGENT-137`–`AGENT-141` are adjacent separate checks for types, required fields, bounds, resource-ID format and payload sizes. [Evidence fixtures](../references/agent-testing-tools.md#tool-call-validation-matrix-agent-026137141) are examples, not completed testing. Older `AGENT-026` PASS reports require re-evaluation.

> **Cross-scope ID map:** The 22 `AGENT-095`–`AGENT-116` checks belong to the backend [API Checks](../backend/17_AI_Agents_and_Tool_Orchestration.md#api-checks) section, not this file. This file continues at `AGENT-117` for frontend checks. [Read the verified domain map](../references/agent-domain-map.md); no IDs were deleted.

## Agent goals and workflow

- [ ] **AGENT-001** `P2` Define the business task, intended user, expected outcome, and explicit stop conditions for each autonomous or semi-autonomous workflow.
- [ ] **AGENT-002** `P1` Determine whether a deterministic workflow, direct model call, or simple tool sequence would meet the need with lower risk than an agent.
- [ ] **AGENT-003** `P2` Document the boundaries between model-directed decisions and hard-coded workflow transitions.
- [ ] **AGENT-004** `P2` Identify an accountable owner for agent behavior, tool authority, service operations, and release approval.
- [ ] **AGENT-005** `P2` Map the permitted workflow states, transitions, termination paths, and externally visible side effects.
- [ ] **AGENT-006** `P2` Define what constitutes a successfully completed task, a partial result, an acceptable refusal, and an unrecoverable failure.
- [ ] **AGENT-007** `P2` List foreseeable misuse, ambiguous requests, unrealistic goals, and tasks the agent must not pursue.
- [ ] **AGENT-008** `P2` Document requirements for clarification, abstention, user confirmation, or qualified human escalation.
- [ ] **AGENT-009** `P1` Distinguish advisory outputs from actions that change external systems, send communications, or transfer value.
- [ ] **AGENT-010** `P1` Bound the agent's task scope to the authorized user's intent, target resources, and stated environment.
- [ ] **AGENT-011** `P2` Define which steps can safely execute automatically and which require deterministic checks or human intervention.
- [ ] **AGENT-012** `P2` Assign measurable thresholds for task completion, correctness, severe-error rate, and quality of the final artifact.
- [ ] **AGENT-013** `P2` Document model, instructions, tool definitions, memory behavior, orchestration library, and execution environment versions.
- [ ] **AGENT-014** `P1` Test the agent on representative multi-step tasks, including missing prerequisites and unexpected tool responses.
- [ ] **AGENT-015** `P1` Evaluate whether workflow decomposition into subtasks improves results without introducing harmful context or authority leakage.
- [ ] **AGENT-016** `P2` Define permitted specialist-agent roles and ensure their responsibilities are distinct and reviewable.
- [ ] **AGENT-017** `P2` Identify high-risk decisions, irreversible actions, and sensitive data transfers along the workflow.
- [ ] **AGENT-018** `P2` Document the sources of truth and validation required before an agent reports an external action as completed.
- [ ] **AGENT-019** `P2` Define how the agent detects a blocked task and stops instead of exploring unrelated targets or acquiring new permissions.
- [ ] **AGENT-020** `P1` For each enabled autonomous workflow, retain a versioned risk-acceptance record with testable acceptance criteria for user harm, cost, latency, availability, and operational burden, linked to supporting evidence.
- [ ] **AGENT-021** `P1` Provide a safe fallback to human or non-agent processing for unavailable models or prohibited tasks where necessary.
- [ ] **AGENT-022** `P1` Reassess agent suitability after changes to models, tool capabilities, connected accounts, customer populations, or workflow scope.

## Tools, permissions, and boundaries

- [ ] **AGENT-023** `P2` Inventory every callable tool and connector, including owner, purpose, provider, version, data sensitivity, and possible side effects.
- [ ] **AGENT-024** `P1` Classify tools by read-only, data-changing, externally communicating, privileged, and destructive capabilities.
- [ ] **AGENT-025** `P1` Allowlist the tools exposed to each agent role and workflow rather than giving every agent access to every integration.
- [ ] **AGENT-026** `P1` Reject tool calls naming tools absent from the trusted registry for the active workflow.
- [ ] **AGENT-137** `P1` Reject tool argument types that violate the server-owned input schema before invocation.
- [ ] **AGENT-138** `P1` Reject tool calls omitting fields required by the server-owned input schema.
- [ ] **AGENT-139** `P1` Reject tool argument values outside server-defined bounds or allowed enumerations.
- [ ] **AGENT-140** `P1` Reject tool resource identifiers that fail server-owned format and namespace validation.
- [ ] **AGENT-141** `P1` Reject tool calls whose argument payload exceeds the server-configured size limit.
- [ ] **AGENT-027** `P0` Enforce object-, tenant-, account-, and operation-level authorization in the tool implementation regardless of the model's instructions.
- [ ] **AGENT-028** `P1` Bind delegated access to the authenticated initiating user or an explicitly approved service identity and purpose.
- [ ] **AGENT-029** `P1` Use narrowly scoped and expiring credentials when supported; prohibit unnecessary shared administrative tokens.
- [ ] **AGENT-030** `P1` Validate token issuer, audience, scopes, expiry, and resource binding for applicable OAuth or MCP-connected services.
- [ ] **AGENT-031** `P1` Prevent an agent from discovering, registering, or invoking unapproved tools through a model-generated URL or description.
- [ ] **AGENT-032** `P1` Review connector endpoints and server identities before trusting dynamically discovered tool metadata.
- [ ] **AGENT-033** `P1` Treat retrieved documents, tool results, webpage text, and other agents' messages as untrusted data rather than new instructions.
- [ ] **AGENT-034** `P1` Test prompt injection that tries to call higher-privilege tools, reveal secrets, or redirect the original user goal.
- [ ] **AGENT-035** `P1` Constrain filesystem, shell, browser, code-execution, and network tools to approved sandboxes, paths, hosts, and resources.
- [ ] **AGENT-036** `P1` Enforce egress and execution limits outside the model for agents that can make network calls or run code.
- [ ] **AGENT-037** `P1` Use separate credentials and isolation for development, testing, staging, and production tool endpoints.
- [ ] **AGENT-038** `P1` Prevent agents from creating or forwarding credentials or accessing secrets outside the permitted task.
- [ ] **AGENT-039** `P1` Validate external tool results and reject malformed, oversized, incompatible, or untrusted outputs before downstream use.
- [ ] **AGENT-040** `P1` Ensure model-generated SQL, scripts, requests, and commands cannot bypass independent policy, parameterization, or sandbox checks.
- [ ] **AGENT-041** `P1` Review cross-tool data transfers for privacy, licensing, data residency, and user permissions.
- [ ] **AGENT-042** `P1` Test confused-deputy scenarios where an agent has broader authority than the initiating user.
- [ ] **AGENT-043** `P1` Enforce operation-specific permissions for consequential tool actions such as export, deletion, payment, or publishing, independently of any model-proposed approval.
- [ ] **AGENT-044** `P1` Implement tool-specific timeouts, resource ceilings, concurrency limits, and throttling to prevent runaway consumption.
- [ ] **AGENT-045** `P1` Check that denial or revocation of tool access takes effect in active and resumed workflows.
- [ ] **AGENT-046** `P1` Verify tool-action audit events conform to a documented schema containing actor, action, target, policy decision, outcome and correlation, with protected content redacted.
- [ ] **AGENT-047** `P1` Review tool inventory and permissions after provider changes, connector upgrades, policy changes, and new agent capabilities.
- [ ] **AGENT-048** `P1` Do not treat tool descriptions, system prompts, output filters, or human-friendly warnings as substitutes for enforceable access controls.

## Handoffs, state, and execution limits

- [ ] **AGENT-049** `P2` Define a documented routing policy for choosing between agents, specialists, and deterministic workflow steps.
- [ ] **AGENT-050** `P1` Restrict each handoff to approved destinations and validate any model-supplied destination or routing metadata.
- [ ] **AGENT-051** `P1` Reevaluate authorization before handoff side effects or delegated tool actions occur.
- [ ] **AGENT-052** `P1` Filter transferred conversation history and context to the minimum information the receiving agent is authorized to see.
- [ ] **AGENT-053** `P1` Test that tenant identity, user permissions, and consent boundaries survive multi-agent routing and nested agents.
- [ ] **AGENT-054** `P1` Distinguish model-generated handoff metadata from trusted server-side state and dependencies.
- [ ] **AGENT-055** `P1` Preserve stable workflow/run IDs, parent-child task IDs, and correlation identifiers across tool calls and handoffs.
- [ ] **AGENT-056** `P2` Define explicit maximum turns, tool calls, nested handoffs, wall-clock duration, token usage, and spend per run.
- [ ] **AGENT-057** `P1` Detect recursion, repetitive tool loops, oscillating handoffs, and lack of task progress before limits are exhausted.
- [ ] **AGENT-058** `P2` Ensure cancellation propagates to pending model calls, queued tool work, child agents, and other resources where feasible.
- [ ] **AGENT-059** `P1` Test the treatment of in-flight side effects when a run is canceled, times out, or loses its initiating session.
- [ ] **AGENT-060** `P1` Persist only necessary state and ensure session memories and checkpoints have documented retention and access policies.
- [ ] **AGENT-061** `P1` Keep serialized agent state and pending approvals in trusted storage with ownership, integrity, and replay protections.
- [ ] **AGENT-062** `P1` Verify that restoring a checkpoint does not grant permissions that were revoked after it was created.
- [ ] **AGENT-063** `P2` Document how concurrent agents coordinate shared state and prevent races, duplicate writes, or contradictory updates.
- [ ] **AGENT-064** `P0` Use operation identifiers and deduplication when retries or resumed workflows could replay non-idempotent tool calls.
- [ ] **AGENT-065** `P1` Test network interruptions, worker restarts, queue delays, and partial tool failures for recoverable continuation.
- [ ] **AGENT-066** `P2` Define what happens when an intermediate agent has completed work but the final synthesis or response fails.
- [ ] **AGENT-067** `P1` Prevent stale memory, wrong-user history, or previous-task instructions from contaminating a new task.
- [ ] **AGENT-068** `P1` Enforce input/output bounds and validation on messages sent between agents, including untrusted structured content.
- [ ] **AGENT-069** `P2` Record whether completed tool actions are confirmed from the authoritative service or only inferred by a model.
- [ ] **AGENT-070** `P2` Define a policy for partial completion, compensating actions, rollback, and escalation when workflows span systems without a shared transaction.
- [ ] **AGENT-071** `P1` Monitor per-run step count, handoffs, resource usage, failure patterns, retries, and unusual tool sequences.
- [ ] **AGENT-072** `P1` Test unsupported tasks and unreachable targets to ensure the agent stops within scope rather than improvising unsafe alternatives.

## Human approval and failure recovery

- [ ] **AGENT-073** `P2` Define the tool actions and risk conditions that require human approval before execution.
- [ ] **AGENT-074** `P1` Present an authenticated reviewer with the exact proposed action, target, affected records, and material consequences.
- [ ] **AGENT-075** `P0` Bind each approval to a specific run, pending tool call, immutable argument set, and authorized decision maker.
- [ ] **AGENT-076** `P1` Reject altered, expired, duplicated, forged, or unbound approval responses before any privileged action occurs.
- [ ] **AGENT-077** `P0` Revalidate current permissions and action arguments immediately before executing a previously approved tool call.
- [ ] **AGENT-078** `P1` Limit approval lifetime and scope; do not silently reuse blanket approval across different tools, accounts, or privilege contexts.
- [ ] **AGENT-079** `P1` Provide an explicit rejection path and ensure rejected actions never execute later because of stale state.
- [ ] **AGENT-080** `P2` Define the behavior when an approval request times out, the reviewer disconnects, or the user cancels the task.
- [ ] **AGENT-081** `P1` Keep pending approvals and approval records in trusted server-side storage rather than trusting client-supplied snapshots.
- [ ] **AGENT-082** `P1` Test approvals arising from nested or handed-off agents rather than only top-level calls.
- [ ] **AGENT-083** `P1` Require independent confirmation for destructive changes, external publication, payments, high-impact decisions, and other risk-defined actions.
- [ ] **AGENT-084** `P1` Ensure reviewers can inspect enough trusted context to challenge model assumptions without exposing unauthorized data.
- [ ] **AGENT-085** `P1` Show a clear difference between an approval request, an approved request, an action in progress, and a confirmed action.
- [ ] **AGENT-086** `P1` Design safe recovery when the application crashes after a side effect but before persisting completed run state.
- [ ] **AGENT-087** `P1` Use idempotency keys, authoritative status checks, and reconciliation for retried actions; do not assume approvals imply exactly-once execution.
- [ ] **AGENT-088** `P2` Document compensating actions and escalation contacts for partial failures that cannot be rolled back atomically.
- [ ] **AGENT-089** `P0` Provide a tested emergency stop that disables agent execution and revokes tools or credentials as appropriate.
- [ ] **AGENT-090** `P1` Test that emergency stops constrain already queued and independently running child tasks.
- [ ] **AGENT-091** `P2` Record approval, denial, execution, partial failure, and remediation events with safe identifiers for audit and incident review.
- [ ] **AGENT-092** `P1` Require agent-action reviewers to pass a documented scenario-based assessment of automation bias, tool side effects, and unverified model explanations before granting approval privileges.
- [ ] **AGENT-093** `P1` Provide an escalation path for ambiguous, disputed, or consequential outcomes requiring human judgment.
- [ ] **AGENT-094** `P1` Validate the complete approval/recovery flow in staging with failures, replay attempts, denied requests, and interrupted resumes.

## Frontend Checks

*Apply these client-side checks only when the AI feature has a user-facing or reviewer-facing interface. They remain part of this AI domain; the general frontend checklist inventory is separate.*

- [ ] **AGENT-117** `P1` Tell users when the system may perform actions using an AI agent and what its authorized capabilities are.
- [ ] **AGENT-118** `P1` Distinguish read-only assistance, suggested actions, and actual changes to external accounts or data.
- [ ] **AGENT-119** `P1` Show meaningful workflow progress and pending steps without inventing tool successes or completion states.
- [ ] **AGENT-120** `P1` Display the exact proposed action, destination, material data, and consequences before asking for approval.
- [ ] **AGENT-121** `P1` Provide explicit and accessible approve, reject, cancel, and request-changes controls for applicable actions.
- [ ] **AGENT-122** `P1` Do not preselect high-impact approvals or imply that a generic message grants unlimited future permission.
- [ ] **AGENT-123** `P1` Clearly indicate when approvals have expired, were rejected, or must be requested again because arguments changed.
- [ ] **AGENT-124** `P1` Test approval interfaces against stale browser tabs, duplicate clicks, disconnected sessions, and retries.
- [ ] **AGENT-125** `P1` Make it easy to inspect an authorized history of completed tool actions and their confirmed results.
- [ ] **AGENT-126** `P1` Provide understandable status for queued, in-progress, paused, partially successful, failed, and canceled runs.
- [ ] **AGENT-127** `P1` Prevent frontend state from being interpreted by the server as proof of authorization or completed execution.
- [ ] **AGENT-128** `P1` Protect pending approval details, tokens, and session context from other users and browser-account switches.
- [ ] **AGENT-129** `P1` Offer a visible stop or cancel control where workflows can continue or consume resources after the initial response.
- [ ] **AGENT-130** `P1` Communicate which actions may already have completed when cancellation or rollback is requested.
- [ ] **AGENT-131** `P1` Give users an appropriate way to correct mistakes, undo supported actions, or escalate irreversible outcomes.
- [ ] **AGENT-132** `P1` Ensure run updates, progress announcements, tool statuses, and approval dialogs work with keyboard and assistive technologies.
- [ ] **AGENT-133** `P1` Keep streaming outputs or agent plans clearly distinct from final verified results and authoritative external state.
- [ ] **AGENT-134** `P1` Safely render tool names, model-proposed arguments, retrieved text, and external service messages without script injection.
- [ ] **AGENT-135** `P1` Test localized approval language and high-impact confirmation text where multiple languages are supported.
- [ ] **AGENT-136** `P1` Provide a means to report harmful or unauthorized agent behavior with privacy-respecting diagnostic references.

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
