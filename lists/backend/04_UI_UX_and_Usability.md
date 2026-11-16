# 04 — UI, UX, and Usability Checklist

> Review whether the product helps people complete meaningful tasks with understandable navigation, predictable interactions, inclusive experiences, and evidence-based improvements. This focuses on product usability; complete the dedicated Accessibility, Testing, Security, and Performance checklists separately.

> **Scope: Backend / API-specific.** This file is one part of the 04_UI_UX_and_Usability.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## API Checks

- [ ] **UX-069** `P2` Document which API responses determine the user-visible state of each critical flow.
- [ ] **UX-070** `P1` Ensure user-facing loading, error, success, and no-results experiences are specified for expected API outcomes.
- [ ] **UX-071** `P2` Map validation failures to specific, understandable field messages without exposing internal stack traces or raw implementation codes.
- [ ] **UX-072** `P2` Define a consistent error representation so the frontend can distinguish authentication, permission, validation, rate-limit, and server failures.
- [ ] **UX-073** `P2` Specify user-facing behavior when a request times out, is cancelled, or returns after the user navigates away.
- [ ] **UX-074** `P1` Design retry and idempotency expectations to avoid confusing duplicate submissions or duplicate transactions.
- [ ] **UX-075** `P1` Provide predictable pagination, filtering, and sorting contracts that preserve user context as results change.
- [ ] **UX-076** `P1` Supply machine-readable availability or progress signals for asynchronous tasks when the user needs to track completion.
- [ ] **UX-077** `P1` Ensure API response fields provide the labels, help content, units, dates, and localization data required for accurate presentation.
- [ ] **UX-078** `P2` Document how stale, partial, or eventually consistent data should be communicated to users where material.
- [ ] **UX-079** `P2` Define ownership and fallback UX for third-party API failures, missing data, quotas, and service disruptions.
- [ ] **UX-080** `P1` Use stable public-facing identifiers and deep-link targets where API-driven navigation or sharing is required.
- [ ] **UX-081** `P1` Review API changes with frontend/consumer teams for user-visible regressions in wording, missing states, and workflow continuity.
- [ ] **UX-082** `P1` Keep authorization outcomes consistent with clear, recoverable user experiences while enforcing permissions on the server.

## Release gate

- [ ] Priority user journeys, target user groups, and expected outcomes are documented and have been reviewed with appropriate stakeholders.
- [ ] Representative usability evidence supports that users can complete critical tasks, including handling common errors and recovery paths.
- [ ] No unresolved, unaccepted usability issue blocks essential tasks, causes material confusion, or risks significant unintended consequences.
- [ ] Core navigation, forms, system feedback, and critical mobile/responsive experiences have been reviewed against agreed design and user needs.
- [ ] API and frontend user-experience dependencies are understood, with owners and documented treatment of failures, latency, and partial results where applicable.
- [ ] Responsible reviewers have recorded the decision and accepted risks in project-specific records.

**Domain-specific approval rule:** Block UX sign-off for unresolved critical-task failures, deceptive or materially misleading interface behavior, inaccessible core journeys awaiting required specialist review, or unknown user-impact risks lacking an accountable owner. UX approval does not substitute for accessibility conformance or production verification.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#04_ui_ux_and_usability), not prerequisites or verification evidence.

## Trusted references and scope

The checklist adapts the following authoritative user-experience, design, and accessibility guidance into observable project review questions. General design heuristics are not universal hard requirements; evaluate their suitability for the actual audience and context.

- [Nielsen Norman Group — 10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/) — feedback, consistency, user control, error prevention, recognition, and recovery.
- [GOV.UK Service Standard — Understand users and their needs](https://www.gov.uk/service-manual/service-standard/point-1-understand-user-needs) — evidence-driven problem framing.
- [GOV.UK Service Standard — Make the service simple to use](https://www.gov.uk/service-manual/service-standard/point-4-make-the-service-simple-to-use) — intuitive tasks and end-to-end usability.
- [GOV.UK Service Manual — Plan user research for your service](https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service) — inclusive research questions, participants, and iteration.
- [GOV.UK Service Manual — Using moderated usability testing](https://www.gov.uk/service-manual/user-research/using-moderated-usability-testing) — representative tasks and observational findings.
- [Nielsen Norman Group — Tree Testing: Evaluate Menu Labels and Categories](https://www.nngroup.com/articles/tree-testing/) — information architecture and findability testing.
- [U.S. Web Design System — Components](https://designsystem.digital.gov/components/) — established visual and interaction patterns.
- [GOV.UK Design System — Recover from validation errors](https://design-system.service.gov.uk/patterns/validation/) — clear messages, field recovery, and preservation of input.
- [W3C WAI — Form Instructions](https://www.w3.org/WAI/tutorials/forms/instructions/) — labels and accessible instructions.
- [W3C WAI — Validating Input](https://www.w3.org/WAI/tutorials/forms/validation/) — error guidance and accessible validation.
- [W3C — Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) — relevant accessibility success criteria, with detailed conformance review in `05_Accessibility.md`.

**Applicability:** Some practices are service-, platform-, or audience-specific. Do not treat GOV.UK's design-system implementation decisions as mandatory for unrelated products. Human usability evaluation is essential where risks or complexity warrant it; quantitative usability metrics require a suitable sample and method.

**Source review date:** 2026-11-12.
