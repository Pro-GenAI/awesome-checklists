# 01 — Requirements and Planning Checklist

> Verify that the project solves a validated problem, has measurable goals, clear scope, testable requirements, realistic delivery plans, and defined API/frontend requirements.

> **Scope: Frontend-specific.** This file is one part of the 01_Requirements_and_Planning.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Frontend Checks

- [ ] **REQ-071** `P2` Identify all user roles, primary journeys, entry points, and device/browser support targets.
- [ ] **REQ-072** `P2` Specify navigation hierarchy, page states, deep-link behavior, and important content requirements before implementation.
- [ ] **REQ-073** `P2` Define acceptance criteria for forms, field validation, error recovery, confirmation, and prevention of duplicate actions.
- [ ] **REQ-074** `P1` Include explicit loading, empty, permission-denied, offline, timeout, and partially unavailable states in user flows.
- [ ] **REQ-075** `P2` Document applicable accessibility target (for example WCAG 2.2 AA) and include keyboard, assistive-technology, contrast, and focus requirements.
- [ ] **REQ-076** `P1` Plan responsive breakpoints and interaction behavior for keyboard, mouse, touch, and small-screen use.
- [ ] **REQ-077** `P2` Define localization needs including languages, time zones, dates, numbers, currencies, and directionality.
- [ ] **REQ-078** `P2` Identify authentication, account-switching, session-expiry, and protected-route experiences.
- [ ] **REQ-079** `P2` Specify frontend data needs and align each essential field or state to an API contract or other data source.
- [ ] **REQ-080** `P1` Set measurable frontend performance budgets or targets, including key page templates and devices.
- [ ] **REQ-081** `P1` Agree analytics events, meaningful conversions, privacy-consent dependencies, and responsible data owners.
- [ ] **REQ-082** `P1` Plan prototype/usability feedback with representative users before finalizing high-risk workflows.
- [ ] **REQ-083** `P2` Define content ownership for interface copy, help text, errors, legal notices, and accessibility labels.

## Release gate

- [ ] The scope, objective, target users, and success criteria have been reviewed and approved by the accountable product owner or sponsor.
- [ ] All release-critical requirements have unambiguous acceptance criteria, identifiable owners, and a feasible verification approach.
- [ ] High-impact assumptions, dependencies, external approvals, constraints, and delivery risks are resolved or have explicitly accepted, time-bound mitigation plans.
- [ ] API and frontend requirements are agreed by relevant consumer/provider and user-experience owners, or documented as genuinely not applicable.
- [ ] The delivery plan has an accountable owner, realistic milestones, a process for changes, and explicit readiness/sign-off responsibilities.

**Domain-specific approval rule:** Do not approve a release plan with undefined success criteria, conflicting critical requirements, unowned blocking dependencies, or unapproved material scope or risk decisions. A planning sign-off is not proof that implementation or release tests have passed.

**Optional tooling:** [Frontend test examples](../references/optional-testing-tools-frontend.md#01_requirements_and_planning), not prerequisites or verification evidence.

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
