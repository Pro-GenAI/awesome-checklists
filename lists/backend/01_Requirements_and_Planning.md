# 01 — Requirements and Planning Checklist

> Verify that the project solves a validated problem, has measurable goals, clear scope, testable requirements, realistic delivery plans, and defined API/frontend requirements.

> **Scope: Backend / API-specific.** This file is one part of the 01_Requirements_and_Planning.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Dependencies and delivery plan

- [ ] **REQ-046** `P1` Dependencies and critical-path constraints are tracked, including API access, domain approvals, design assets, and vendor timelines.

## API Checks

- [ ] **REQ-058** `P2` List every planned API consumer, provider, integration purpose, trust boundary, and accountable owner.
- [ ] **REQ-059** `P2` Define the API's supported operations, resource names, identifiers, methods, and expected workflows before development.
- [ ] **REQ-060** `P2` Specify request/response contracts, required and optional fields, validation rules, types, examples, and error semantics.
- [ ] **REQ-061** `P1` Use an agreed machine-readable API description such as OpenAPI when suitable, with documented version and ownership.
- [ ] **REQ-062** `P2` Define authentication, scopes, object-level and role-based authorization requirements for each protected operation.
- [ ] **REQ-063** `P2` Specify data classification and fields permitted for each consumer; prohibit unintended sensitive-data exposure.
- [ ] **REQ-064** `P2` Document idempotency, timeouts, retries, pagination, quotas, and rate-limit expectations where relevant.
- [ ] **REQ-065** `P2` Define consistency, concurrency, and transactional behavior for conflicting or repeated state-changing requests.
- [ ] **REQ-066** `P2` Document versioning, deprecation, backwards compatibility, and consumer migration expectations.
- [ ] **REQ-067** `P2` Specify third-party API dependencies, contract limits, service-level expectations, cost, and fallback behavior.
- [ ] **REQ-068** `P2` Define webhook/callback ownership, event payloads, authenticity requirements, and failure handling when used.
- [ ] **REQ-069** `P1` Agree API acceptance examples and contract test ownership with both producer and consumer.
- [ ] **REQ-070** `P2` Define API observability requirements for metrics, failures, tracing identifiers, and data-safe logs.

## Release gate

- [ ] The scope, objective, target users, and success criteria have been reviewed and approved by the accountable product owner or sponsor.
- [ ] All release-critical requirements have unambiguous acceptance criteria, identifiable owners, and a feasible verification approach.
- [ ] High-impact assumptions, dependencies, external approvals, constraints, and delivery risks are resolved or have explicitly accepted, time-bound mitigation plans.
- [ ] API and frontend requirements are agreed by relevant consumer/provider and user-experience owners, or documented as genuinely not applicable.
- [ ] The delivery plan has an accountable owner, realistic milestones, a process for changes, and explicit readiness/sign-off responsibilities.

**Domain-specific approval rule:** Do not approve a release plan with undefined success criteria, conflicting critical requirements, unowned blocking dependencies, or unapproved material scope or risk decisions. A planning sign-off is not proof that implementation or release tests have passed.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#01_requirements_and_planning), not prerequisites or verification evidence.

## Trusted references and scope

The checklist translates the following primary guidance into project-planning verification tasks; it does not reproduce the referenced standards or imply formal certification.

- [NASA Systems Engineering Handbook — requirements definition](https://www.nasa.gov/reference/4-2-technical-requirements-definition/) — clear, traceable, feasible, verifiable requirements and design constraints.
- [NASA Systems Engineering Handbook — requirements quality and traceability](https://www.nasa.gov/reference/system-engineering-handbook-appendix/) — uniqueness, consistency, testability, and verification planning.
- [GOV.UK Service Manual — learning about user needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs) — evidence-based needs and traceability into delivery work.
- [GOV.UK Service Manual — performance metrics](https://www.gov.uk/service-manual/measuring-success/how-to-set-performance-metrics-for-your-service) — purpose, benefits, measurements, and iteration.
- [GOV.UK Service Manual — deciding on priorities](https://www.gov.uk/service-manual/agile-delivery/deciding-on-priorities) — transparent prioritization across features and other work.
- [The Scrum Guide (2020)](https://scrumguides.org/scrum-guide.html) — product goal, product backlog, and definition of done (use if relevant to the team's delivery method).
- [OpenAPI Specification 3.2.1](https://spec.openapis.org/oas/v3.2.1.html) — standard interface description for HTTP APIs (when applicable).
- [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/) — testable web accessibility criteria (when applicable).

**Applicability:** Requirements management practices vary with project size, industry, development method, and jurisdiction. Do not automatically impose Scrum or government-service requirements on other teams; tailor the controls to actual risks and users.

**Source review date:** 2026-11-12.
