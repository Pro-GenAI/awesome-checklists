# 01 — Requirements and Planning Checklist

> Verify that the project solves a validated problem, has measurable goals, clear scope, testable requirements, realistic delivery plans, and defined API/frontend requirements.

> **Scope: AI-specific.** This file is one part of the 01_Requirements_and_Planning.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Goals and success criteria

- [ ] **REQ-008** `P1` Guardrail metrics capture potential negative effects, such as errors, abandonments, accessibility barriers, or unexpected cost.

## Release gate

- [ ] The scope, objective, target users, and success criteria have been reviewed and approved by the accountable product owner or sponsor.
- [ ] All release-critical requirements have unambiguous acceptance criteria, identifiable owners, and a feasible verification approach.
- [ ] High-impact assumptions, dependencies, external approvals, constraints, and delivery risks are resolved or have explicitly accepted, time-bound mitigation plans.
- [ ] API and frontend requirements are agreed by relevant consumer/provider and user-experience owners, or documented as genuinely not applicable.
- [ ] The delivery plan has an accountable owner, realistic milestones, a process for changes, and explicit readiness/sign-off responsibilities.

**Domain-specific approval rule:** Do not approve a release plan with undefined success criteria, conflicting critical requirements, unowned blocking dependencies, or unapproved material scope or risk decisions. A planning sign-off is not proof that implementation or release tests have passed.

**Optional tooling:** [AI-scope testing examples](../references/optional-testing-tools-ai.md#01_requirements_and_planning), not prerequisites or evidence of PASS.

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
