# Independent practitioner review and field-validation protocol

**Status: NOT STARTED / no external sign-off.** This protocol offers a reproducible way to assess the technical quality and usability of the checklist library. A passing source linter, an AI-generated draft, a repository self-review, stars, or a dated citation do **not** establish independent validation.

## Evidence to request before claiming a check is validated

1. Record the reviewer identity, qualifications, independence/affiliation, review date, checklist-source commit SHA, target project/release SHA, scope, environment and conflicts of interest.
2. For a cited standard, inspect the authoritative edition and exact relevant requirement; record publication/version, section identifier, source URL, date checked, and whether the checklist is fully aligned, partially aligned or unsupported.
3. For a testable control, state **one observable assertion**, applicable attack surface, setup, negative/positive test fixtures, expected and observed behavior, artifacts, exclusions and safe-test authorization.
4. Have a second reviewer reproduce a sample of results without relying exclusively on tool-generated verdicts. Mark source-content review separately from implementation PASS/FAIL/UNKNOWN/N/A.
5. Publish only redacted and consented findings. Keep raw logs, secrets, user data and private systems in the target team's secure evidence store; supply immutable references or checksums when appropriate.

## Suggested bounded pilot (unperformed)

| Pilot | Selected IDs | Actual evidence required |
| --- | --- | --- |
| Authentication/session app | SEC-009, SEC-010, SEC-110, SEC-111, SEC-116, SEC-117 | Clock-controlled idle/absolute session tests, revoked-token replay and throttling traces |
| Public web/API system | SEC-007, SEC-012, SEC-013, SEC-014, SEC-062, SEC-065, SEC-069, SEC-072, SEC-076, SEC-118–SEC-121 | Authorized test fixtures for permission, inputs, proxy parsing, replay, output encoding and injection/traversal |
| Agent-enabled application (only if applicable) | AGENT-033, AGENT-034, AGENT-075, AGENT-100, AGENT-102 | Adversarial prompts, independent authority denials, approval binding, API replay and idempotency traces |

Before each pilot, randomly sample additional checks from other relevant domains to avoid measuring only editor-selected examples. Use both a new reviewer and someone familiar with the system. Record time per check, ambiguity counts, applicability rate, false positive/false negative cases, missing evidence, overlap, defects found and remediation value. A **Core 50** review is a starter, not a sufficient independent audit. Do not run hostile security tests against systems without authorization.

## Result ledger to complete

| Field | Initial state |
| --- | --- |
| Independent reviewer(s) and affiliation | **UNASSIGNED** |
| Field-tested project and release | **NOT PROVIDED** |
| Checklist source SHA under assessment | **NOT PINNED** |
| Individually validated checks | **0 documented in this protocol** |
| Completed independent product reviews | **0 documented in this protocol** |
| Outstanding disagreement / risk acceptances | **UNKNOWN** |
| Release/certification decision | **NOT ISSUED** |

The ledger is a **blank evidence request**, not a claim that reviews were attempted or that zero reviews exist elsewhere. Add real signed entries only after the described work. For a narrower demonstration of evidence-linked statuses, use the [historical repository self-review](example-review.md); for ongoing control wording changes, see [Security ID history](id-history.md) and the [downstream change comparison](downstream-update-guide.md).
