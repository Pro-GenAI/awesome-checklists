# 07 — API Design and Integrations Checklist

> Verify that service interfaces have understandable contracts, predictable behavior, secure integration boundaries, maintained consumer compatibility, and workable fallback procedures. This checklist complements the separate Security, Testing, Data, DevOps, and Reliability reviews.

> **Scope: Backend / API-specific.** This file is one part of the 07_API_Design_and_Integrations.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## API architecture and contracts


- [ ] **APID-001** `P2` Define each API's business purpose, owner, intended consumers, and trust boundary.
- [ ] **APID-002** `P1` Choose synchronous HTTP, asynchronous events, or streaming based on consistency and latency needs.
- [ ] **APID-007** `P1` Apply correct HTTP safety and idempotency semantics for HTTP methods when applicable.
- [ ] **APID-012** `P2` Document validation, authentication, authorization, conflict, overload, and server-failure responses.
- [ ] **APID-017** `P2` Specify appropriate cache directives, validators, freshness, and private-data isolation.

- [ ] **APID-003** `P1` Separate public, partner, internal, and privileged operations with documented authorization policies.
- [ ] **APID-004** `P1` Keep a reviewed OpenAPI, AsyncAPI, or equivalent contract appropriate to the protocol.
- [ ] **APID-005** `P2` Validate implemented methods, routes, events, and message types against the published contract.
- [ ] **APID-006** `P1` Use predictable resource names, identifiers, and documented operation semantics.
- [ ] **APID-008** `P2` Specify accepted content types, content negotiation, and unsupported representation behavior.
- [ ] **APID-009** `P2` Define field types, required properties, nullability, defaults, and unknown-field behavior.
- [ ] **APID-010** `P2` Specify timestamp/time-zone, numeric precision, currency, Unicode, and locale semantics.
- [ ] **APID-011** `P1` Use explicit schemas for nested, polymorphic, and potentially large payloads.
- [ ] **APID-013** `P1` Adopt consistent structured errors such as RFC 9457 Problem Details where suitable.
- [ ] **APID-014** `P2` Define stable pagination, sorting, filters, and cursor behavior under data changes.
- [ ] **APID-015** `P2` Document write concurrency control, conditional updates, and lost-update prevention.
- [ ] **APID-016** `P2` Define retry, timeout, deduplication, and idempotency semantics for operations with side effects.
- [ ] **APID-018** `P2` Document file transfers, streams, and asynchronous job completion where provided.
- [ ] **APID-019** `P2` Define authentication schemes, scopes, tenant boundaries, and privileged roles.
- [ ] **APID-020** `P1` Review interface descriptions and executable examples together with the versioned release artifact.

## Consumer experience and lifecycle


- [ ] **APID-021** `P2` Document supported environments, API base URLs, versions, and contact channels.
- [ ] **APID-037** `P1` Distinguish internal service objectives from contractual API support guarantees.

- [ ] **APID-022** `P1` Provide a first-success quickstart using safe test credentials and current examples.
- [ ] **APID-023** `P1` Explain credential issuance, expiry, rotation, and least-privilege scope selection.
- [ ] **APID-024** `P2` Publish representative success, validation, denial, conflict, and throttling examples.
- [ ] **APID-025** `P2` Describe tenant, account, user, and resource identifier scopes clearly.
- [ ] **APID-026** `P2` Document quotas, rate limits, payload limits, and client concurrency expectations.
- [ ] **APID-027** `P1` Explain safe retries and handling of ambiguous timeouts without duplicate actions.
- [ ] **APID-028** `P1` Provide correlation identifiers and support details to diagnose reported errors.
- [ ] **APID-029** `P2` Document pagination traversal, cursor expiry, and stable ordering requirements.
- [ ] **APID-030** `P2` Maintain version-compatible SDKs and code samples where offered.
- [ ] **APID-031** `P1` Verify published code examples against a controlled environment before release.
- [ ] **APID-032** `P1` Explain optional response fields, extensions, feature negotiation, and tolerant parsing.
- [ ] **APID-033** `P1` Offer authoritative contract artifacts for consumer code generation and testing.
- [ ] **APID-034** `P2` Document deprecations, support windows, sunset dates, and migration steps.
- [ ] **APID-035** `P2` Specify asynchronous operation tracking, partial success, and delayed consistency.
- [ ] **APID-036** `P1` Provide representative test fixtures and sandboxes when integration risk warrants them.
- [ ] **APID-038** `P2` Track new-consumer onboarding failures, common integration complaints, and owners.
- [ ] **APID-039** `P1` Test a consumer's ability to find docs, authenticate, complete a task, and recover from failure.

## Third-party integrations


- [ ] **APID-042** `P1` Review provider scopes, API keys, data location, processing terms, and access rights.
- [ ] **APID-046** `P1` Authenticate webhook senders with the provider's supported signature or equivalent mechanism.
- [ ] **APID-047** `P2` Document webhook acknowledgment, retry, duplicate, ordering, and expiry behavior.
- [ ] **APID-052** `P1` Collect safe request, transaction, and provider correlation IDs for incidents.

- [ ] **APID-040** `P2` Inventory providers, data flows, ownership, criticality, terms, and escalation contacts.
- [ ] **APID-041** `P2` Document the intended fallback when a critical third-party integration is unavailable.
- [ ] **APID-043** `P1` Keep development and production credentials and callback destinations separate.
- [ ] **APID-044** `P1` Protect external credentials through approved secret storage and rotation procedures.
- [ ] **APID-045** `P1` Validate and constrain untrusted provider responses before use in business operations.
- [ ] **APID-048** `P1` Deduplicate repeated event deliveries using stable event IDs or business invariants.
- [ ] **APID-049** `P1` Set bounded timeouts, retries, backoff, concurrency limits, and circuit breaking.
- [ ] **APID-050** `P1` Exercise provider outages, slow responses, malformed payloads, and quota exhaustion safely.
- [ ] **APID-051** `P1` Reconcile ambiguous external outcomes against the local source of truth.
- [ ] **APID-053** `P1` Ensure third-party logs and error outputs do not expose unrelated personal data.
- [ ] **APID-054** `P1` Monitor vendor costs, rate limits, quotas, and usage anomalies.
- [ ] **APID-055** `P2` Track provider version changes, SDK support, deprecation notices, and schema drift.
- [ ] **APID-056** `P1` Validate untrusted URLs and callback redirects to mitigate SSRF and open redirects.
- [ ] **APID-057** `P2` Document incident handling, vendor status channels, emergency contacts, and exit options.
- [ ] **APID-058** `P1` Test critical integration scenarios in an authorized sandbox or equivalent controlled environment.
- [ ] **APID-059** `P1` Review any applicable privacy, licensing, cross-border data, or contract requirements.

## Versioning and compatibility


- [ ] **APID-060** `P2` Define a versioning and negotiation policy for each supported API and message interface.
- [ ] **APID-065** `P1` Support old and new API instances or clients coexisting during phased deployment.
- [ ] **APID-068** `P1` Coordinate database/schema evolution with legacy consumers and outstanding background jobs.
- [ ] **APID-069** `P2` Document caching and persisted-client behavior across API versions.
- [ ] **APID-075** `P1` Version and archive API schemas, SDKs, docs, and release artifacts consistently.

- [ ] **APID-061** `P2` Document which contract changes are considered breaking for each consumer category.
- [ ] **APID-062** `P1` Treat field removal, changed types, required inputs, and authorization changes as possible breaks.
- [ ] **APID-063** `P1` Review new enum values and response fields against consumers using closed-schema parsing.
- [ ] **APID-064** `P2` Specify compatibility rules for nullability, defaults, list order, errors, and pagination.
- [ ] **APID-066** `P1` Run a contract-diff check against supported production versions before release.
- [ ] **APID-067** `P1` Use consumer-driven or representative contract tests for important dependent clients.
- [ ] **APID-070** `P1` Announce deprecations with migration guidance and an approved notice period.
- [ ] **APID-071** `P1` Provide safe test environments and examples of required migration steps.
- [ ] **APID-072** `P1` Observe legacy version use where permitted before disabling old interfaces.
- [ ] **APID-073** `P2` Define an exception process for consumers unable to migrate before sunset.
- [ ] **APID-074** `P1` Test compatibility with independently updated vendor SDKs and external providers.
- [ ] **APID-076** `P1` Verify rollback does not leave previous clients incompatible with changed data.
- [ ] **APID-077** `P2` Define responses for unsupported and sunsetted versions and explain next steps.
- [ ] **APID-078** `P2` Assign owners to breaking-change investigations and outstanding compatibility debt.

## API Checks


- [ ] **APID-079** `P0` Test object-, function-, and property-level authorization, including tenant isolation.
- [ ] **APID-080** `P1` Validate inputs, uploads, query options, and request sizes at the trusted API boundary.
- [ ] **APID-081** `P1` Verify actual success and failure status codes and structured errors match contracts.
- [ ] **APID-082** `P1` Test repeated mutations and concurrent requests for idempotency and data integrity.
- [ ] **APID-083** `P1` Validate conditional requests or optimistic locking on sensitive concurrent edits.
- [ ] **APID-084** `P1` Test pagination with inserts, deletions, duplicate sort keys, and empty pages.
- [ ] **APID-085** `P1` Verify rate limits, quotas, overuse errors, and bounded resource consumption.
- [ ] **APID-086** `P1` Test cache headers, privacy boundaries, localization keys, and conditional responses.
- [ ] **APID-087** `P1` Verify cross-origin rules allow intended browser clients but not arbitrary origins.
- [ ] **APID-088** `P1` Test TLS and token audience, issuer, expiry, scope, and authorization checks.
- [ ] **APID-089** `P1` Reject webhook requests with invalid signatures or failed replay safeguards.
- [ ] **APID-090** `P1` Test duplicate, delayed, or out-of-order events without duplicate business side effects.
- [ ] **APID-091** `P1` Simulate upstream and downstream timeouts, malformed data, and partial outages.
- [ ] **APID-092** `P1` Check upload, download, asynchronous job, and streaming completion when applicable.
- [ ] **APID-093** `P1` Validate logs, traces, and error reports exclude credentials and sensitive payloads.
- [ ] **APID-094** `P1` Confirm contract tests and breaking-change checks are required by CI.
- [ ] **APID-095** `P1` Test compatibility across supported client versions and server rollbacks.
- [ ] **APID-096** `P1` Validate Unicode, date, monetary values, and locale metadata end-to-end.
- [ ] **APID-097** `P1` Verify third-party usage controls for cost, payloads, concurrency, and quotas.
- [ ] **APID-098** `P1` Confirm the production deployment identifies responsible API owners and escalation paths.
- [ ] **APID-099** `P1` Check public schema examples and SDK operations against production-equivalent behavior.

- [ ] **APID-120** `P1` For browser-driven form submissions that change state, evaluate Post/Redirect/Get (such as `303 See Other` after POST) or an equivalent safe navigation pattern; verify refresh/back navigation cannot accidentally repeat mutations and use server-side idempotency for consequential operations.

## Release gate


- [ ] Release-affected interfaces have accountable owners, current accessible contracts, and identified consumers and trust boundaries.
- [ ] Required authentication, authorization, schema conformance, error behavior, and core contract checks pass against the release candidate.
- [ ] Existing supported consumers remain compatible, or a reviewed migration plan and version coexistence strategy are in place.
- [ ] High-impact operations have safe retries, idempotency, concurrency, resource ceilings, and partial-failure handling where applicable.
- [ ] Critical third-party connections use approved credentials, validate untrusted data, and have tested recovery and escalation arrangements.
- [ ] Affected frontend workflows handle API errors, stale responses, caching, authentication, and phased rollouts safely.
- [ ] Published docs, support contacts, changelogs, and deprecation notices reflect the exact release.
- [ ] Material unresolved security, data-integrity, or compatibility risks have explicit authorized release decisions.

**Domain-specific approval rule:** Block sign-off for unauthorized cross-tenant access, unreviewed breaking changes for supported consumers, unsafe duplicate business side effects, or untested critical provider failure paths without accepted mitigation. This template does not certify security or protocol conformance.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#07_api_design_and_integrations), not prerequisites or verification evidence.

## Trusted references and scope


These primary standards and authoritative guidance inform the checks; use them only for relevant protocols and implementations.

- [OpenAPI Specification v3.2.1](https://spec.openapis.org/oas/v3.2.1.html) — machine-readable contracts for HTTP API operations and schemas.
- [AsyncAPI Specification v3.1.0](https://www.asyncapi.com/docs/reference/specification/v3.1.0) — machine-readable contracts for message-driven interfaces.
- [IETF RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — methods, statuses, content negotiation, and representation semantics.
- [IETF RFC 9111 — HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111) — freshness, validators, cache-control, and private response protection.
- [IETF RFC 9457 — Problem Details](https://www.rfc-editor.org/rfc/rfc9457) — structured error responses for HTTP APIs.
- [IETF RFC 9700 — OAuth 2.0 Security BCP](https://www.rfc-editor.org/rfc/rfc9700) — current OAuth security guidance for applicable deployments.
- [IETF RFC 6750 — Bearer Token Usage](https://www.rfc-editor.org/rfc/rfc6750) — bearer credential transport and error behavior.
- [OWASP API Security Top 10 (2023)](https://api-security.owasp.org/editions/2023/en/0x00-header/) — authorization, resource consumption, and integration threats.
- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12) — schema contracts and JSON validation.
- [CNCF CloudEvents](https://cloudevents.io/) — common metadata for event integrations where appropriate.
- [IETF RFC 8288 — Web Linking](https://www.rfc-editor.org/rfc/rfc8288) — link relations for API discoverability where applicable.
- [IETF RFC 9421 — HTTP Message Signatures](https://www.rfc-editor.org/rfc/rfc9421) — optional signed HTTP requests and webhook messages.

**Applicability:** OpenAPI 3.2.1 is for HTTP interface descriptions; AsyncAPI 3.1.0 is for message-driven interfaces; verify actual toolchain support. OAuth and bearer guidance applies only where those credential schemes are used. CloudEvents and HTTP message signatures are optional interoperability choices rather than universal webhook obligations. OWASP API Security Top 10 (2023) is risk guidance, not exhaustive certification.

- [MDN — 303 See Other](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/303) — safe browser redirect semantics after POST.

**Source review date:** 2026-11-13.
