# 01 — Requirements and Planning Checklist

> Verify that the project solves a validated problem, has measurable goals, clear scope, testable requirements, realistic delivery plans, and defined API/frontend requirements.

> **Scope: Shared / cross-cutting.** This file is one part of the 01_Requirements_and_Planning.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](references/review-method.md) · [Optional framework crosswalk](references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Goals and success criteria

- [ ] **REQ-001** `P1` The project problem statement identifies the user or business need, current pain point, and intended outcome without assuming a predetermined solution.
- [ ] **REQ-002** `P1` Target users, customer groups, service operators, and representative usage contexts are identified from research or documented assumptions.
- [ ] **REQ-003** `P1` Existing user research, analytics, support data, or comparable evidence informs the proposed solution.
- [ ] **REQ-004** `P1` Critical unvalidated assumptions are recorded with an owner, method of validation, and target review date.
- [ ] **REQ-005** `P1` Measurable product objectives and outcomes are agreed with accountable stakeholders.
- [ ] **REQ-006** `P1` Success metrics define units, baseline, target, measurement period, data source, and reporting owner.
- [ ] **REQ-007** `P1` Leading indicators and longer-term outcomes are distinguished so that activity is not mistaken for user value.
- [ ] **REQ-009** `P1` Target markets, supported languages, expected traffic, and launch constraints are written down.
- [ ] **REQ-010** `P1` Business, user, operational, and technical goals are prioritized when trade-offs arise.
- [ ] **REQ-011** `P1` Outcomes and metrics are reviewed with users or their representatives where feasible.
- [ ] **REQ-012** `P1` A minimum viable release hypothesis states what will be learned and what evidence would justify expanding or stopping the work.

## Scope and stakeholders

- [ ] **REQ-013** `P1` A named sponsor/product owner is accountable for the product goal and final scope decisions.
- [ ] **REQ-014** `P1` A stakeholder map includes users, delivery teams, support, operations, vendors, data owners, and affected business units.
- [ ] **REQ-015** `P1` Decision rights, review responsibilities, approvers, and escalation paths are explicit.
- [ ] **REQ-016** `P1` In-scope and out-of-scope capabilities are listed for the planned release.
- [ ] **REQ-017** `P1` The system boundary and adjacent business processes, including manual or offline steps, are documented.
- [ ] **REQ-018** `P1` Must-have, should-have, could-have, and deferred work are prioritized using consistent criteria.
- [ ] **REQ-019** `P1` The planned first release is small enough to validate important assumptions within the available time and resources.
- [ ] **REQ-020** `P1` Dependencies on other internal teams, procurement, vendors, or external approvals have named owners.
- [ ] **REQ-021** `P1` User groups with disabilities, low connectivity, limited digital literacy, or other access barriers are considered in scope decisions.
- [ ] **REQ-022** `P1` Regulated activities, contractual commitments, and relevant legal or policy review needs are flagged for specialist owners.
- [ ] **REQ-023** `P1` Data ownership, personal-data handling, hosting constraints, and third-party access are identified early.
- [ ] **REQ-024** `P1` Budget, staffing, platform constraints, and commercial commitments are explicit.
- [ ] **REQ-025** `P1` Stakeholder disagreements and scope trade-offs have documented resolutions or accountable escalation.
- [ ] **REQ-026** `P1` Scope changes follow a transparent impact-review and approval process.

## Requirements and acceptance criteria

- [ ] **REQ-027** `P1` Each requirement has a unique identifier, concise description, owner, priority, and source or rationale.
- [ ] **REQ-028** `P1` User needs are written independently from proposed implementation where feasible.
- [ ] **REQ-029** `P1` User stories or equivalent items map to one or more validated user needs or business objectives.
- [ ] **REQ-030** `P1` Functional requirements describe observable inputs, outputs, state transitions, and relevant business rules.
- [ ] **REQ-031** `P1` Non-functional requirements specify measurable performance, availability, security, privacy, accessibility, maintainability, and support needs as applicable.
- [ ] **REQ-032** `P1` Requirements clearly distinguish mandatory constraints from optional preferences.
- [ ] **REQ-033** `P1` Each requirement is necessary, feasible, internally consistent, and understandable to both stakeholders and implementers.
- [ ] **REQ-034** `P1` Vague terms such as 'fast', 'secure', 'intuitive', or 'scalable' are replaced with measurable or inspectable criteria.
- [ ] **REQ-035** `P1` Every priority requirement includes testable acceptance criteria, including expected positive behavior.
- [ ] **REQ-036** `P1` Important negative, boundary, failure, and recovery cases have acceptance criteria.
- [ ] **REQ-037** `P1` Roles, permissions, and tenant boundaries are specified for protected operations.
- [ ] **REQ-038** `P1` Required data fields, ownership, lifecycle, retention, import/export, and deletion behavior are described where relevant.
- [ ] **REQ-039** `P1` External system interfaces and data handoffs have explicit inputs, outputs, responsibilities, and error handling expectations.
- [ ] **REQ-040** `P1` Assumptions, unresolved questions, exclusions, and known conflicts are recorded with owners.
- [ ] **REQ-041** `P1` Priority requirements are traceable to acceptance tests, design decisions, or verification methods.
- [ ] **REQ-042** `P1` Stakeholders review and approve the current requirements baseline before major implementation or handoff.
- [ ] **REQ-043** `P1` Changes to baselined requirements record the reason, impact on scope/cost/schedule, approver, and dependent artifacts.

## Dependencies and delivery plan

- [ ] **REQ-044** `P1` The delivery plan has milestones with owners, approximate sequencing, and objective completion criteria.
- [ ] **REQ-045** `P1` Technical discovery, proof-of-concept work, and unresolved high-risk assumptions are scheduled early.
- [ ] **REQ-047** `P1` Tasks are sized for observable progress, with high-uncertainty work broken down or time-boxed.
- [ ] **REQ-048** `P1` Capacity assumptions, key roles, specialist access, and availability are checked against the roadmap.
- [ ] **REQ-049** `P1` Estimates distinguish evidence-based commitments from rough forecasts and show major uncertainties.
- [ ] **REQ-050** `P1` Risk registers document likelihood, impact, mitigation, owner, trigger, and review date for material risks.
- [ ] **REQ-051** `P1` The plan allows time for discovery, accessibility, security/privacy reviews, integration, migration, documentation, and operational handover.
- [ ] **REQ-052** `P1` Technical spikes or prototype findings are converted into decisions or revised requirements.
- [ ] **REQ-053** `P1` Delivery progress is reviewed against outcomes and completed work, not only task counts.
- [ ] **REQ-054** `P1` A regular feedback and prioritization cadence includes stakeholder demos or user validation where useful.
- [ ] **REQ-055** `P1` Change-control practices allow reprioritization while making impact on release commitments visible.
- [ ] **REQ-056** `P1` The planned release contains rollback, support, training, and communication ownership where applicable.
- [ ] **REQ-057** `P1` Agreed readiness and sign-off criteria identify who can block or approve proceeding.

## Release gate

- [ ] The scope, objective, target users, and success criteria have been reviewed and approved by the accountable product owner or sponsor.
- [ ] All release-critical requirements have unambiguous acceptance criteria, identifiable owners, and a feasible verification approach.
- [ ] High-impact assumptions, dependencies, external approvals, constraints, and delivery risks are resolved or have explicitly accepted, time-bound mitigation plans.
- [ ] API and frontend requirements are agreed by relevant consumer/provider and user-experience owners, or documented as genuinely not applicable.
- [ ] The delivery plan has an accountable owner, realistic milestones, a process for changes, and explicit readiness/sign-off responsibilities.

**Domain-specific approval rule:** Do not approve a release plan with undefined success criteria, conflicting critical requirements, unowned blocking dependencies, or unapproved material scope or risk decisions. A planning sign-off is not proof that implementation or release tests have passed.

**Optional tooling:** [File-specific tool examples](references/optional-testing-tools-shared.md#01_requirements_and_planning), not prerequisites or verification evidence.

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
