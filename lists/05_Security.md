# 05 — Security Checklist

> Assess confidentiality, integrity, availability, abuse resistance, and operational security proportionate to project risk.

> **ID order:** IDs are permanent references, not an ordered sequence. Later IDs appear next to their topical peers; SEC-007 belongs to the backend slice. [ID history and scope moves](references/id-history.md) explain additions and gaps.

> **Scope: Shared / cross-cutting.** This file is one part of the 05_Security.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](references/review-method.md) · [Optional framework crosswalk](references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Security scope and architecture

- [ ] **SEC-001** `P2` Assets, sensitive data, trust boundaries, external dependencies, and data flows are inventoried.
- [ ] **SEC-002** `P1` A threat model covers realistic attacker goals, entry points, misuse cases, and mitigation owners.
- [ ] **SEC-003** `P1` Data classification and environment-specific security requirements are documented.
- [ ] **SEC-004** `P1` Security owners, risk ratings, release criteria, and exception approvals are assigned.

- [ ] **SEC-040** `P2` Record API and browser attack surfaces including trust boundaries between client, identity provider, API gateway, and backend.

- [ ] **SEC-042** `P1` Set risk-based verification objectives using an explicitly selected ASVS level or equivalent benchmark.

## Identity and access management

- [ ] **SEC-006** `P1` Use maintained, vetted authentication libraries appropriate to the supported identity flows.
- [ ] **SEC-102** `P1` Enforce MFA for privileged accounts, including tested enrollment and recovery paths.
- [ ] **SEC-103** `P1` Where passwords are stored, verify salted adaptive password hashing with appropriate parameters; reject plaintext, reversible encryption, and fast general-purpose hashes.
- [ ] **SEC-008** `P0` Least privilege, role separation, service-account scopes, and periodic access reviews are applied.
- [ ] **SEC-009** `P1` Verify that server-enforced idle session expiration meets the documented risk-based inactivity limit.
- [ ] **SEC-116** `P1` Verify that absolute session lifetime is enforced server-side independently of user activity.
- [ ] **SEC-110** `P1` Rotate session identifiers after authentication and privilege changes; verify old session identifiers cannot be reused.
- [ ] **SEC-111** `P1` Revoke active server-side sessions on logout and verify invalidated sessions cannot access protected resources.
- [ ] **SEC-112** `P1` Make password-reset and account-recovery tokens expiring and single-use; test replay rejection.
- [ ] **SEC-010** `P1` Test that repeated login password-guessing attempts are limited by server-enforced, risk-based anti-automation controls.
- [ ] **SEC-117** `P1` Test that credential-stuffing attempts using known valid identifiers or breached-password combinations are detected or constrained.
- [ ] **SEC-113** `P1` Test signup and registration endpoints against automated account creation and abusive retry volumes.
- [ ] **SEC-114** `P1` Limit and test account/password-recovery initiation and verification attempts against abuse across accounts and networks.
- [ ] **SEC-115** `P1` Rate-limit and monitor verification email/SMS issuance and resend flows to mitigate automated spam and cost attacks.
- [ ] **SEC-011** `P1` Default, dormant, emergency, and vendor accounts are reviewed and restricted.
- [ ] **SEC-043** `P1` Require reauthentication or step-up assurance for high-risk operations where appropriate.
- [ ] **SEC-044** `P1` Revoke and expire compromised/rotated tokens; verify session invalidation across devices where supported.

## Application, API, and supply-chain security

- [ ] **SEC-012** `P0` Validate untrusted inputs against explicit server-side contracts at applicable trust boundaries.
- [ ] **SEC-118** `P0` Test that user-controlled values cannot alter database query structure through SQL or NoSQL injection.
- [ ] **SEC-119** `P0` Test that user-controlled values cannot alter shell or subprocess command execution.
- [ ] **SEC-120** `P1` Verify that untrusted serialized input cannot instantiate unauthorized object types or execute code.
- [ ] **SEC-016** `P1` Build/release pipelines restrict permissions, verify artifact provenance where feasible, and protect signing credentials.
- [ ] **SEC-017** `P2` Define a risk-based security-audit scope for the source, dependencies, configurations, and exposed runtime surfaces.
- [ ] **SEC-104** `P1` Run static security analysis suitable for the codebase and document actual coverage.
- [ ] **SEC-105** `P1` Perform secrets scanning of applicable current source, history, and build artifacts.
- [ ] **SEC-106** `P1` Perform authorized risk-based dynamic security or penetration tests on exposed interfaces when the threat model warrants them.
- [ ] **SEC-107** `P1` Independently reproduce and classify suspected security findings before reporting them as verified vulnerabilities.
- [ ] **SEC-108** `P2` Track confirmed security findings through owner assignment, remediation, and retesting.
- [ ] **SEC-109** `P2` Record the audit's tested surfaces, unverified surfaces, tool versions, and documented limitations.
- [ ] **SEC-018** `P1` Security fixes are regression tested and documented.

## Secrets, encryption, and data protection

- [ ] **SEC-020** `P0` Secrets are centrally managed, rotated when necessary, and scoped to their purpose.
- [ ] **SEC-021** `P1` Enforce HTTPS for production routes and sensitive data; verify TLS/certificates, a suitable HSTS policy for supported hosts, and absence of unsafe mixed content without treating HSTS preload as universally required.
- [ ] **SEC-023** `P1` Data collection, retention, masking, export, deletion, and backup access follow documented policy.
- [ ] **SEC-024** `P1` Logs, traces, analytics, and error reports exclude secrets and unnecessary personal data.

## Operational readiness and incident response

- [ ] **SEC-031** `P1` An incident response plan defines severity, contacts, containment, recovery, notification, and evidence handling.
- [ ] **SEC-032** `P1` Known vulnerabilities have remediation deadlines based on severity and exposure.
- [ ] **SEC-033** `P1` Vulnerability reporting and dependency/security update ownership are defined.
- [ ] **SEC-034** `P1` Business continuity, DDoS/availability protection, and disaster recovery match project risk.
- [ ] **SEC-035** `P1` Security alerts are routed to responders and can be meaningfully investigated.
- [ ] **SEC-054** `P0` Exercise suspected credential leak and compromised dependency response, including token rotation and customer notice decisions.
- [ ] **SEC-055** `P2` Record automated security test results and residual risk approvals against the release commit.

## Release gate

- [ ] The accountable reviewer records project-specific security release blockers from the threat model, mandatory obligations, material findings and applicable checklist evidence; provisional `P0`/`P1` labels alone do not determine go/no-go. Consider the applicable Core 50 suggestions and additional domain controls, and mitigate or explicitly authorize time-bound exceptions for material FAIL/UNKNOWN blockers.
- [ ] Failed items have tracked remediation, owners, and deadlines; material blockers remain blocked until resolved.
- [ ] Evidence links and the reviewer, review date, and final decision are recorded.

**Domain-specific approval rule:** Block release for exploitable critical/high findings without approved mitigation, missing authorization boundaries, exposed secrets, or unprotected sensitive data.

**Optional tools:** See the [separate security tooling catalog](references/security-testing-tools.md); no third-party agent skill is required to satisfy this checklist.

## Trusted references and scope

The checks above are adapted into practical verification questions from these authoritative publications (not copied as standards text). Verify current versions and the project's scope before sign-off.

- [OWASP API Security Top 10 (2023)](https://api-security.owasp.org/editions/2023/en/0x11-t10/)
- [OWASP Application Security Verification Standard (ASVS) 5.0](https://asvs.owasp.org/)
- [OWASP ASVS 5.0 control families (web frontend and API)](https://cornucopia.owasp.org/taxonomy/asvs-5.0)

Guidance is risk-based and project-specific; sources do not replace testing or specialist review. Accessibility sources belong in the Accessibility domain; generative-AI risk profiles belong in the AI scope.

- [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) — adaptive hashes.
- [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) — rotation, expiry, revocation.
- [MDN TLS security](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Transport_Layer_Security) — HTTPS, HSTS, mixed content.

**Source review date:** 2026-11-15.
