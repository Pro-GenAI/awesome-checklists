# 07 — API Design and Integrations Checklist

> Verify that service interfaces have understandable contracts, predictable behavior, secure integration boundaries, maintained consumer compatibility, and workable fallback procedures. This checklist complements the separate Security, Testing, Data, DevOps, and Reliability reviews.

> **Scope: Frontend-specific.** This file is one part of the 07_API_Design_and_Integrations.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Frontend Checks

- [ ] **APID-100** `P2` Map critical browser journeys to the API calls, permissions, and expected errors they depend on.
- [ ] **APID-101** `P1` Verify client configuration uses intended API origins, versions, and production environment.
- [ ] **APID-102** `P1` Prevent secrets and privileged API credentials from appearing in public frontend assets.
- [ ] **APID-103** `P1` Use safe browser credential handling and documented CORS rather than permissive workarounds.
- [ ] **APID-104** `P1` Render API-supplied user content safely without injecting executable script or markup.
- [ ] **APID-105** `P1` Validate submitted field types and constraints, while retaining server-side authority.
- [ ] **APID-106** `P1` Handle validation, conflict, denied, expired-session, offline, and server errors distinctly.
- [ ] **APID-107** `P1` Bound client retries and guard against duplicate charges, messages, or submissions.
- [ ] **APID-108** `P1` Offer clear progress, cancellation, and resumption for long-running operations as relevant.
- [ ] **APID-109** `P1` Handle empty, partial, paginated, and stale data without misleading users.
- [ ] **APID-110** `P1` Invalidate user-specific caches after writes, role changes, account switches, and logout.
- [ ] **APID-111** `P1` Prevent private responses being reused across users, tenants, or browser cache contexts.
- [ ] **APID-112** `P1` Tolerate allowed additional response fields and enum extensions without crashes.
- [ ] **APID-113** `P1` Test old browser tabs and cached bundles during progressive API deployment.
- [ ] **APID-114** `P1` Validate upload/download sizes, content types, and understandable failure states.
- [ ] **APID-115** `P1` Test essential journeys under throttling, provider outages, and intermittent connectivity.
- [ ] **APID-116** `P1` Make API-related error feedback understandable and accessible to keyboard and screen-reader users.
- [ ] **APID-117** `P1` Correlate client and API diagnostics without exposing user secrets or protected payloads.
- [ ] **APID-118** `P1` Keep generated API client types and frontend mocks aligned with approved contracts.
- [ ] **APID-119** `P2` Document client support and deprecation windows and ensure migration UX is usable.

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

**Optional tooling:** [Frontend test examples](../references/optional-testing-tools-frontend.md#07_api_design_and_integrations), not prerequisites or verification evidence.

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

**Source review date:** 2026-11-12.
