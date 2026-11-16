# 26 — Testing Checklist

> Verify expected functionality, quality, reliability, and release readiness using reproducible evidence.

> **Scope: Backend / API-specific.** This file is one part of the 26_Testing.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Automated and component testing


- [ ] **TST-007** `P1` Integration tests verify database, queue, cache, and third-party interactions, including failures.
- [ ] **TST-008** `P1` API/contract tests verify schemas, validation, error codes, versioning, and compatibility.

## Performance, resilience, and data integrity


- [ ] **TST-025** `P1` Peak-load, concurrency, and rate-limit scenarios have measurable results where relevant.
- [ ] **TST-027** `P1` Database migrations, rollback plans, and data integrity constraints are tested on representative data.
- [ ] **TST-029** `P1` Telemetry identifies critical errors, latency, and failures without disclosing sensitive data.
- [ ] **TST-050** `P1` Reliability checks verify concurrency safeguards, queue replays, eventual consistency, and duplicate delivery where applicable.
- [ ] **TST-026** `P1` Timeouts, retries, circuit breakers, idempotency, and graceful degradation are verified.
- [ ] **TST-028** `P1` Backup/restore or disaster recovery procedures are exercised to the agreed recovery targets.
- [ ] **TST-051** `P1` Recovery tests verify that failed or partially completed writes do not corrupt data or leak sensitive state.

## Release verification


- [ ] **TST-032** `P1` Deployment, configuration, feature flags, and rollback/roll-forward steps are rehearsed.
- [ ] **TST-033** `P1` Staging smoke tests pass and post-deployment production smoke checks are assigned.

## API Checks


> Apply to API endpoints, client integrations, webhooks, or data feeds present in the project. Record N/A with reasons if none exist.

**Reference basis:** [OWASP Application Security Verification Standard (ASVS) 5.0](https://asvs.owasp.org/); [OWASP API Security Top 10 (2023)](https://api-security.owasp.org/editions/2023/en/0x11-t10/); [OpenAPI Specification 3.2.1](https://spec.openapis.org/oas/v3.2.1.html).

- [ ] **TST-055** `P1` Validate each documented endpoint, method, status code, required field, optional field, and example against the running API.
- [ ] **TST-056** `P1` Run positive and negative tests for authentication, expired credentials, user roles, cross-user objects, and cross-tenant boundaries.
- [ ] **TST-057** `P1` Check object-level and property-level authorization on read, update, list, and bulk endpoints.
- [ ] **TST-058** `P1` Test malformed JSON, invalid content types, missing/null/oversized values, Unicode, and unexpected fields.
- [ ] **TST-059** `P1` Confirm pagination, filtering, sorting, cursor handling, and empty/result-limit behavior under data changes.
- [ ] **TST-060** `P1` Exercise retry, timeout, cancellation, idempotency, and concurrency behavior for state-changing requests.
- [ ] **TST-061** `P1` Assert stable, actionable 4xx/5xx responses and structured error bodies if the project uses RFC 9457.
- [ ] **TST-062** `P1` Verify versioning and consumer compatibility, including deprecation notices and contract-diff checks.
- [ ] **TST-063** `P1` Check rate-limit and quota enforcement, appropriate 429 behavior, and documented retry guidance.
- [ ] **TST-064** `P1` Test batch jobs, async requests, webhooks/callbacks, and signature verification where applicable.
- [ ] **TST-065** `P1` Confirm error and debug responses never return credentials, internal stack traces, or unauthorized records.
- [ ] **TST-066** `P1` Measure high-traffic endpoint latency/throughput and recovery from upstream failures using realistic workloads.
- [ ] **TST-067** `P1` Verify API documentation, examples, and supported SDKs remain in sync with deployed behavior.

## Release gate


- [ ] All applicable high-priority checks above pass, or an authorized decision-maker has explicitly accepted and documented each residual risk.
- [ ] Failed items have tracked remediation, owners, and deadlines; material blockers remain blocked until resolved.
- [ ] Evidence links and the reviewer, review date, and final decision are recorded.

**Domain-specific approval rule:** Do not approve when critical flows, data integrity, access-control tests, or required recovery checks fail.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#26_testing), not prerequisites or verification evidence.

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
