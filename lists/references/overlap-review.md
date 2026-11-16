# Checklist overlap review — agent authority and approval controls

**Review date:** 2026-11-15; counts updated after the eight-security-check split. **Scope:** the reported pairs in [AI Agents and Tool Orchestration](../AI/11_AI_Agents_and_Tool_Orchestration.md), with related backend controls considered as implementation-specific counterparts. This is **not a semantic-deduplication audit of all 4,206 checks**.

| IDs | Different acceptance evidence | Decision |
| --- | --- | --- |
| `AGENT-033` vs `AGENT-034` | `033` defines the *untrusted-data boundary* for documents/tool results/agent messages; `034` demands *adversarial tests* of privilege escalation, exfiltration and goal redirection. | Retain both: design rule versus test evidence. |
| `AGENT-033` vs `AGENT-048` | `033` classifies external content as data; `048` requires independent code/infrastructure access controls rather than prompts, warnings or output filters. | Retain both: trust classification versus authority enforcement. |
| `AGENT-073` vs `AGENT-083` | `073` defines the *approval policy* and triggering risks; `083` requires *independent confirmation* for destructive/high-impact actions under that policy. | Retain both: policy definition versus runtime gate. |
| `AGENT-075` vs `AGENT-100` (backend) | `075` binds an approval to an immutable run/tool call/argument set; `100` verifies that binding through the backend API's approval surface. | Retain both when both runtime and API surfaces are in scope; evidence may be shared, but the attack surfaces differ. |

**Outcome:** No identified pair was merged; **zero existing IDs were removed**. The repository's current **4,215 check IDs** are unique in the mechanical inventory, **not proven semantically distinct controls**. The distinction matters when one domain is split across the AI and backend scope files.

**Tool-schema atomicity (2026-11-15):** `AGENT-026` now checks tool-name trust; `AGENT-137`–`AGENT-141` separately test schema types, required fields, allowed values, identifier format and payload size. The same dispatcher test suite may yield separate evidence, but these do not replace `AGENT-027` authorization or `AGENT-042` confused-deputy testing. [Acceptance fixtures](agent-testing-tools.md#tool-call-validation-matrix-agent-026137141) remain unperformed examples.

## Control, test and API-surface relationships

The following labels describe **acceptance evidence**, not a deduplication claim. Retain distinct IDs when they test different enforcement points; one artifact may be reused with separate assertions.

| ID(s) | Role | Distinct acceptance evidence |
| --- | --- | --- |
| `AGENT-033` | Design / trust-boundary control | External tool outputs and retrieved content cannot acquire instruction or authority status |
| `AGENT-034`, `AGENT-042` | Adversarial verification tests | Demonstrated injection or confused-deputy attempts, including trusted enforcement outcomes |
| `AGENT-048`, `AGENT-027` | Independent authorization controls | Actual tool/runtime authorization rejects untrusted instructions and unauthorized objects/tenants |
| `AGENT-073`, `AGENT-075` | Approval policy and binding controls | Policy defines approval obligations; binding ties one approval to a specific run/tool/argument set |
| `AGENT-083` | High-impact execution gate | A destructive or consequential action cannot proceed without the required independently validated confirmation |
| `AGENT-100` (backend) | API-surface verification | Backend endpoint rejects stale, spoofed, mismatched or unauthorized approval independent of model wording |
| `AGENT-046` | Single audit-event schema criterion | Records conform to the required actor/action/target/policy/outcome/correlation schema **and** redact protected fields; missing any field fails this one schema acceptance |
| `AGENT-109` (backend) | Backend trace/telemetry control | API traces are correlated and sanitize confidential payloads; related to, but not the same as, audit-event schema completeness |
| `AGENT-102` (backend) | API idempotency enforcement | API retries/replay cannot create unintended repeated external side effects; separate from approval-binding checks |

For `AGENT-046`, do **not** award partial PASS when one schema column is present but a redaction or correlation assertion is absent. Mark FAIL for observed violations, UNKNOWN for untested facets. For approval pairs, `AGENT-075` and `AGENT-100` can share the same test trace, but one examines the runtime binding and the other the backend API enforcement surface. Do not delete or repurpose stable IDs simply because a review uses one evidence artifact. Detailed scenarios appear in [agent-testing-tools.md](agent-testing-tools.md).

## Scope continuity

The [AGENT domain map](agent-domain-map.md) shows **141 contiguous IDs** split across [AI-specific and frontend checks](../AI/11_AI_Agents_and_Tool_Orchestration.md) and [backend API checks](../backend/17_AI_Agents_and_Tool_Orchestration.md#api-checks). The missing-looking `AGENT-095`–`AGENT-116` sequence is in the backend slice; none is retired. The [machine-readable contract](agent-domain-contract.json) is enforced by the repository source linter. It is a structural check, not a full semantic overlap audit.

**Duplicate statistics:** Exact duplicate stable IDs: **0**, under the current inventory's uniqueness checks. Independently confirmed semantic duplicates: **unknown** (not assessed across the library). Similar controls may intentionally require different implementation evidence. No independent semantic-duplicate count is claimed.

Future deduplication should include full-library semantic review, a mapping of old IDs to surviving IDs, downstream issue-link migration, check text comparison and documented release-gate impact. Never silently reassign or reuse an existing ID. When a single test artifact supports multiple distinct checks, reference the same artifact in project-specific evidence records rather than marking the checks passed automatically.
