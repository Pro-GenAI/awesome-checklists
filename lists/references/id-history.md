# Stable ID history and scope routing

**As of 2026-11-15:** Security has **121 active, unique IDs**, `SEC-001` through `SEC-121`, distributed across shared (**47**), frontend (**18**), backend (**50**) and AI (**6**) slices. IDs are **not required to appear in numerical order within a file**. They are inserted under relevant topical headings as the library grows; numerical gaps in one slice usually indicate controls owned by a different slice. For example, **SEC-007** is in the backend Security file, while **SEC-040** and **SEC-042** appear next to related architecture checks in the shared file. The [Security ID registry](security-id-registry.json) records every current SEC ID and its owning source file.

## Additions and clarifications

**2026-11-15 follow-up:** `SEC-009` now covers idle expiry, while `SEC-116` covers absolute session lifetime. `SEC-010` now covers password-guessing and `SEC-117` covers credential-stuffing tests. These are separate verifications with separate outcomes. Any earlier PASS covering a multi-part criterion must be reconsidered; no old ID was removed.


| Date | IDs | Change | Migration guidance |
| --- | --- | --- | --- |
| 2026-11-15 | SEC-118–SEC-121 and revisions to SEC-012–SEC-014 | Separated input-contract validation, database injection, command injection, unsafe deserialization, HTTP request smuggling, API replay and filesystem path containment; reused existing SEC-007/049/062/064/065/069/072/076 controls for overlapping surfaces. | Review new IDs individually. Historic PASS for SEC-012/013/014 does **not** transfer; earlier snapshots retain original source SHA. These edits are an editorial decomposition, **not** independent security validation. |
| 2026-11-15 | SEC-102, SEC-103 | Split authentication library, privileged MFA, and password hashing from original SEC-006 | Keep SEC-006 for vetted libraries; also review SEC-102 (MFA) and SEC-103 (password hashes). Earlier single `SEC-006` passes do not imply these checks passed. |
| 2026-11-15 | SEC-104–SEC-109 | Split scope, code scanning, secrets scanning, dynamic testing, validation, remediation and reporting from compound SEC-017 | SEC-017 now covers audit scope; related verifications each require independent evidence. |
| 2026-11-15 | SEC-116, SEC-117 | Split idle versus absolute session lifetime and password guessing versus credential stuffing from SEC-009 and SEC-010 | Require independent evidence for the new IDs; earlier PASS on the compound versions is not sufficient. |
| 2026-11-15 | SEC-110–SEC-112 | Split multi-part session lifecycle/recovery control SEC-009 | SEC-009 now covers session expiry; SEC-110 rotation, SEC-111 logout revocation and SEC-112 recovery token expiry/single-use and replay resistance require separate evidence. |
| 2026-11-15 | SEC-113–SEC-115 | Split multi-surface automated abuse defenses from SEC-010 | SEC-010 now covers login brute-force/credential stuffing; SEC-113 signup, SEC-114 recovery and SEC-115 verification-message abuse are separately testable. |

**Retired/deleted Security IDs:** none documented. **Reused IDs:** none. **Historical section order:** IDs may move between sections/files for scope clarity, but their meaning and reference remain stable as far as practical. Any later retirement, semantic change or owner move must be recorded here and in [CHANGELOG.md](../../docs/CHANGELOG.md) before release.

## Maintenance

Run `python3 skills/awesome-checklists/scripts/lint_repository.py` (local or on `main` push) to validate stable-ID uniqueness, the Security ID registry, source-file paths, priority markers, whitespace conventions, and internal links. Extend the registry intentionally when adding or moving a Security ID. **No pull request is required** for maintainers who have direct-write authorization; review/verification evidence is still expected. The repo's `P0/P1/P2` tiers are project-adjustable and many are provisional.
