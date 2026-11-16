# Core 50 — risk-based starter review

This **curated set of 50 existing checklist IDs** is a starting point for a small review, **not a universal minimum, compliance standard, or release approval**. It samples 12 shared, 12 frontend, 12 backend and 14 AI checks. Select only applicable scopes, add checks for your architecture/threat model, and evaluate the full domain release gates. Omitting a check here does not downgrade its importance.

**Priority is contextual, not intrinsic severity.** `P0` = potential release blocker if applicable and unmitigated; `P1` = important risk review; `P2` = contextual/supporting verification. A qualified reviewer must adjust tiers for the product, jurisdiction, and threat model. These 50 have **manually curated** starting tiers. All other numbered checks now display **provisional, text-rule-derived** tiers; do not assume those estimates reflect product risk or that any P2 check can safely be skipped.

Machine-readable curated selection: [core-50.json](https://github.com/Pro-GenAI/awesome-checklists/blob/main/lists/references/core-50.json). Generate the full checklist inventory as JSON with `python3 skills/awesome-checklists/scripts/export_checklists.py --output checklists.json` from the repository root. The export includes all visible tiers plus a `priority_basis` field; the Core 50 use `curated-core-50`, and other checks use `provisional-text-triage`.

**Offline wording triage (not validation):** Run `python3 skills/awesome-checklists/scripts/audit_compound_checks.py --core-only --output core-50-compound-candidates.json` from the repository root to identify possible multi-assertion Core 50 checks. The heuristic can miss ambiguity or flag harmless wording; it does not assign severity, prove atomicity, replace independent review, or mark any check as PASS.

Review each applicable check with `PASS` / `FAIL` / `UNKNOWN` / `N/A`, linking evidence and recording decisions outside these unchecked source templates. Suggested order is `P0`, `P1`, then `P2`; this ordering never substitutes for full risk scoping.

## Shared (12 checks)

| Tier | Checklist ID | Verification prompt |
| --- | --- | --- |
| P2 | [`SEC-001`](../05_Security.md) | Assets, sensitive data, trust boundaries, external dependencies, and data flows are inventoried. |
| P1 | [`SEC-002`](../05_Security.md) | A threat model covers realistic attacker goals, entry points, misuse cases, and mitigation owners. |
| P0 | [`SEC-008`](../05_Security.md) | Least privilege, role separation, service-account scopes, and periodic access reviews are applied. |
| P0 | [`SEC-012`](../05_Security.md) | Validate untrusted inputs against explicit server-side contracts at applicable trust boundaries. |
| P0 | [`SEC-020`](../05_Security.md) | Secrets are centrally managed, rotated when necessary, and scoped to their purpose. |
| P1 | [`SEC-024`](../05_Security.md) | Logs, traces, analytics, and error reports exclude secrets and unnecessary personal data. |
| P1 | [`TST-002`](../08_Testing.md) | Critical user journeys, business rules, edge cases, and negative cases are identified and prioritized by risk. |
| P1 | [`TST-018`](../08_Testing.md) | Critical journeys are retested after fixes; regression suites pass. |
| P0 | [`TST-031`](../08_Testing.md) | Known defects are triaged by severity; no unaccepted release-blocking defect remains. |
| P2 | [`LAUNCH-010`](../14_Release_and_LaunchReadiness.md) | Maintain a single release plan linking the source revision, immutable artifact, change summary, owners, milestones, and evidence locations. |
| P1 | [`LAUNCH-052`](../14_Release_and_LaunchReadiness.md) | Set measurable thresholds for error rates, latency, availability, transaction failures, and business guardrails that halt rollout. |
| P1 | [`LAUNCH-056`](../14_Release_and_LaunchReadiness.md) | Document tested rollback, traffic reversal, feature-disablement, and forward-fix options appropriate to the changed components. |

## Frontend (12 checks)

| Tier | Checklist ID | Verification prompt |
| --- | --- | --- |
| P2 | [`A11Y-002`](../frontend/05_Accessibility.md) | Identify the applicable accessibility standards, legal/contractual obligations, and target conformance level with qualified reviewers when needed. |
| P1 | [`A11Y-023`](../frontend/05_Accessibility.md) | Verify tab order follows the intended interaction and does not produce confusing jumps or inaccessible controls. |
| P1 | [`A11Y-063`](../frontend/05_Accessibility.md) | Evaluate critical journeys with screen readers and supported browser/operating-system combinations. |
| P0 | [`A11Y-067`](../frontend/05_Accessibility.md) | Test forms for programmatic labels, descriptions, required fields, error association, and recovery after failed submission. |
| P0 | [`A11Y-094`](../frontend/05_Accessibility.md) | Ensure keyboard-only users can operate all essential functions without focus traps or undiscoverable commands. |
| P2 | [`A11Y-100`](../frontend/05_Accessibility.md) | Announce asynchronous status changes through appropriate live regions or other accessible notification patterns without over-announcing. |
| P1 | [`A11Y-103`](../frontend/05_Accessibility.md) | Ensure pointer targets, drag interactions, gestures, and hover/focus revealed content have accessible alternatives where required. |
| P0 | [`UX-032`](../frontend/04_UI_UX_and_Usability.md) | Check that destructive, privileged, or irreversible actions are not confused with routine navigation. |
| P2 | [`UX-041`](../frontend/04_UI_UX_and_Usability.md) | Show loading, empty, offline, unavailable, and error states that explain the condition and next step. |
| P1 | [`UX-044`](../frontend/04_UI_UX_and_Usability.md) | Use undo, edit, cancel, or confirmation patterns proportionate to the impact and reversibility of an action. |
| P1 | [`UX-090`](../frontend/04_UI_UX_and_Usability.md) | Check that client and server validation disagree neither silently nor through contradictory user messages. |
| P0 | [`SEC-076`](../frontend/09_Security.md) | Check CSRF protection for cookie-authenticated state-changing actions and other applicable request forgery risks. |

## Backend (12 checks)

| Tier | Checklist ID | Verification prompt |
| --- | --- | --- |
| P0 | [`SEC-007`](../backend/09_Security.md) | Authorization is enforced server-side on every protected object, action, and tenant boundary. |
| P0 | [`SEC-019`](../backend/09_Security.md) | Scan current source, available Git history/branches, build artifacts, and logs for passwords, API keys, private keys, or tokens; revoke or rotate confirmed exposures and assess impact instead of assuming removal from the latest commit resolves a leak. |
| P0 | [`SEC-045`](../backend/09_Security.md) | Test tenant isolation at query, storage, cache, and API response boundaries. |
| P0 | [`SEC-058`](../backend/09_Security.md) | Perform object-level authorization tests for manipulated IDs on every read, write, and delete endpoint (OWASP API1). |
| P0 | [`SEC-059`](../backend/09_Security.md) | Test authentication token issuance, expiry, audience/issuer, signature validation, revocation, and replay resistance where relevant. |
| P1 | [`SEC-062`](../backend/09_Security.md) | Enforce and test resource limits: rate, page size, payload size, timeouts, concurrency, and costly downstream calls (API4). |
| P1 | [`SEC-064`](../backend/09_Security.md) | Test SSRF controls for URL-fetching endpoints and all outbound destinations (API7). |
| P2 | [`APID-005`](../backend/07_API_Design_and_Integrations.md) | Validate implemented methods, routes, events, and message types against the published contract. |
| P0 | [`APID-079`](../backend/07_API_Design_and_Integrations.md) | Test object-, function-, and property-level authorization, including tenant isolation. |
| P1 | [`APID-082`](../backend/07_API_Design_and_Integrations.md) | Test repeated mutations and concurrent requests for idempotency and data integrity. |
| P2 | [`DATA-023`](../backend/08_Data_and_DatabaseManagement.md) | Test migrations against representative data volumes, versions, constraints, indexes, and realistic schema history. |
| P1 | [`DATA-148`](../backend/08_Data_and_DatabaseManagement.md) | Demonstrate point-in-time recovery to a selected timestamp or log position using a valid base backup and complete incremental/log chain; reconcile recovered business records with the agreed recovery objective. |

## AI (14 checks)

| Tier | Checklist ID | Verification prompt |
| --- | --- | --- |
| P0 | [`AGENT-027`](../AI/11_AI_Agents_and_Tool_Orchestration.md) | Enforce object-, tenant-, account-, and operation-level authorization in the tool implementation regardless of the model's instructions. |
| P1 | [`AGENT-034`](../AI/11_AI_Agents_and_Tool_Orchestration.md) | Test prompt injection that tries to call higher-privilege tools, reveal secrets, or redirect the original user goal. |
| P1 | [`AGENT-048`](../AI/11_AI_Agents_and_Tool_Orchestration.md) | Do not treat tool descriptions, system prompts, output filters, or human-friendly warnings as substitutes for enforceable access controls. |
| P2 | [`AGENT-058`](../AI/11_AI_Agents_and_Tool_Orchestration.md) | Ensure cancellation propagates to pending model calls, queued tool work, child agents, and other resources where feasible. |
| P0 | [`AGENT-064`](../AI/11_AI_Agents_and_Tool_Orchestration.md) | Use operation identifiers and deduplication when retries or resumed workflows could replay non-idempotent tool calls. |
| P0 | [`AGENT-075`](../AI/11_AI_Agents_and_Tool_Orchestration.md) | Bind each approval to a specific run, pending tool call, immutable argument set, and authorized decision maker. |
| P0 | [`AGENT-077`](../AI/11_AI_Agents_and_Tool_Orchestration.md) | Revalidate current permissions and action arguments immediately before executing a previously approved tool call. |
| P0 | [`AGENT-089`](../AI/11_AI_Agents_and_Tool_Orchestration.md) | Provide a tested emergency stop that disables agent execution and revokes tools or credentials as appropriate. |
| P0 | [`RAG-053`](../AI/10_RAG_and_Knowledge_Bases.md) | Test retrieval isolation against users with similar queries but different document permissions. |
| P0 | [`RAG-065`](../AI/10_RAG_and_Knowledge_Bases.md) | Use controlled adversarial cases to verify malicious document text cannot change search permissions or trigger external actions. |
| P1 | [`AIG-005`](../AI/03_AI_Evaluation_and_Governance.md) | Classify the system by potential impact and likelihood of harm using a documented, project-appropriate risk methodology. |
| P0 | [`AIG-025`](../AI/03_AI_Evaluation_and_Governance.md) | Set explicit acceptance thresholds, review rules, and responsible approvers for high-impact outcomes. |
| P0 | [`RED-057`](../AI/16_AI_Red_Teaming_and_Guardrails.md) | Enforce user, tenant, role, scope, resource, and destination permissions in trusted execution code for every consequential tool call. |
| P2 | [`RED-089`](../AI/16_AI_Red_Teaming_and_Guardrails.md) | Record significant findings with owners, severity, mitigation, user impact, and validated retest evidence in project-specific records. |

## Before declaring readiness

Do not treat this selection as completion of the full library. Verify relevant domain release gates, non-selected high-risk controls, incident and failure paths, and required regulatory/organizational approvals. The selection is maintained by manual review; changing a source ID or its meaning requires updating the JSON and running the export tests.
