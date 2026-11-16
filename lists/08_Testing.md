# 08 — Testing Checklist

> Verify expected functionality, quality, reliability, and release readiness using reproducible evidence.

> **Scope: Shared / cross-cutting.** This file is one part of the 08_Testing.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](references/review-method.md) · [Optional framework crosswalk](references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Requirements and test strategy


- [ ] **TST-001** `P1` User stories, acceptance criteria, and definition of done are documented and testable.
- [ ] **TST-002** `P1` Critical user journeys, business rules, edge cases, and negative cases are identified and prioritized by risk.
- [ ] **TST-004** `P1` Requirements and recent defect fixes are mapped to test cases or coverage evidence.
- [ ] **TST-005** `P1` Test environments and integrations reflect production sufficiently to make results meaningful.
- [ ] **TST-035** `P1` Prioritize a risk-based test matrix across roles, tenants, locales, feature flags, and affected integrations.
- [ ] **TST-036** `P2` Specify observable expected results and data setup/cleanup steps for every critical scenario.
- [ ] **TST-037** `P2` Define objective coverage targets, ownership for gaps, and procedures for exploratory testing.
- [ ] **TST-038** `P1` Confirm production-like test data has been anonymized or generated synthetically.

## Automated and component testing


- [ ] **TST-006** `P1` Unit tests exercise core logic, input boundaries, error handling, and regressions.
- [ ] **TST-009** `P1` Automated tests run in CI on the relevant changes and fail the build on critical failures.
- [ ] **TST-010** `P1` Tests are deterministic: flaky cases are diagnosed, quarantined with owners, or fixed.
- [ ] **TST-011** `P1` Test fixtures and synthetic data avoid exposing real customer secrets or personal information.
- [ ] **TST-039** `P1` Mutation, property-based, or fuzz testing covers high-risk parsers and business rules where useful.
- [ ] **TST-040** `P1` CI records test artifacts, failure traces, and flaky-test trends for reproducible triage.

- [ ] **TST-042** `P1` Contracts are checked for changes to required fields, nullability, and backward compatibility.

## Functional and end-to-end testing


- [ ] **TST-012** `P1` Onboarding, authentication, account recovery, and sign-out work where applicable.
- [ ] **TST-013** `P1` Primary create/read/update/delete or transaction journeys work from start to finish.
- [ ] **TST-014** `P1` User permissions and role-specific workflows behave correctly for allowed and denied operations.

- [ ] **TST-016** `P1` Search, filters, sorting, pagination, exports, notifications, and background jobs work where present.
- [ ] **TST-017** `P1` External integrations are tested for success, rate limits, retries, and unavailable dependencies.
- [ ] **TST-018** `P1` Critical journeys are retested after fixes; regression suites pass.
- [ ] **TST-043** `P1` Critical flows work for first-time, returning, expired-session, and restricted users.
- [ ] **TST-044** `P1` Parallel actions, duplicate clicks, and lost responses cannot create inconsistent transactions.

## Performance, resilience, and data integrity


- [ ] **TST-024** `P1` Response time, throughput, and resource usage meet documented performance budgets under realistic load.

- [ ] **TST-049** `P1` Representative synthetic monitoring and load tests include slow networks and constrained mobile devices.

## Release verification


- [ ] **TST-030** `P1` Builds, linters, type checks, and all required automated tests pass for the release candidate.
- [ ] **TST-031** `P0` Known defects are triaged by severity; no unaccepted release-blocking defect remains.
- [ ] **TST-034** `P1` Test results and sign-off are linked to the specific build or commit being released.
- [ ] **TST-052** `P1` Release notes identify affected systems, user-facing changes, and backward-incompatible behaviors.
- [ ] **TST-053** `P1` Failure-injection or controlled dependency-outage testing has been completed for high-risk paths.
- [ ] **TST-054** `P1` Monitoring thresholds, escalation contacts, and post-release observation windows are documented.

## Release gate


- [ ] All applicable high-priority checks above pass, or an authorized decision-maker has explicitly accepted and documented each residual risk.
- [ ] Failed items have tracked remediation, owners, and deadlines; material blockers remain blocked until resolved.
- [ ] Evidence links and the reviewer, review date, and final decision are recorded.

**Domain-specific approval rule:** Do not approve when critical flows, data integrity, access-control tests, or required recovery checks fail.

**Optional tooling:** [File-specific tool examples](references/optional-testing-tools-shared.md#08_testing), not prerequisites or verification evidence.

## Trusted references and scope


The checks above are adapted into practical verification questions from these authoritative publications (not copied as standards text). Verify current versions and the project's scope before sign-off.

- [OWASP Application Security Verification Standard (ASVS) 5.0](https://asvs.owasp.org/)
- [OWASP API Security Top 10 (2023)](https://api-security.owasp.org/editions/2023/en/0x11-t10/)
- [OpenAPI Specification 3.2.1](https://spec.openapis.org/oas/v3.2.1.html)
- [IETF RFC 9457 — Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html)
- [W3C — WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)
- [web.dev — Core Web Vitals](https://web.dev/articles/vitals)

Guidance is risk-based and project-specific; sources do not replace testing or specialist review.

**Source review date:** 2026-11-12.
