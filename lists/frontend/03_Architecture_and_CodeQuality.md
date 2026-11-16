# 03 — Architecture and Code Quality Checklist

> Review design trade-offs, system boundaries, maintainable code, engineering reviews, decision records, and API/frontend architecture. This checklist evaluates structure and evolvability; it complements the dedicated Testing, Security, DevOps, and Performance files.

> **Scope: Frontend-specific.** This file is one part of the 03_Architecture_and_CodeQuality.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Reviews and technical debt

- [ ] **ARC-043** `P1` Use automated formatting, linting, and static checks so reviewers focus on architectural and behavioral decisions.

## Frontend Checks

- [ ] **ARC-081** `P1` Choose client rendering, server rendering, static generation, or hybrid strategies based on content, performance, hosting, and interaction requirements.
- [ ] **ARC-082** `P1` Structure routes, layouts, components, and features with clear module ownership and predictable dependency direction.
- [ ] **ARC-083** `P1` Separate view rendering from business decisions and data-access details where this improves maintainability.
- [ ] **ARC-084** `P1` Keep reusable UI components focused and expose documented props, events, and accessible behaviors.
- [ ] **ARC-085** `P1` Use consistent design tokens and shared UI patterns instead of duplicating styling and interactions across screens.
- [ ] **ARC-086** `P2` Define where server-derived state, client state, form state, and cached data live; avoid competing sources of truth.
- [ ] **ARC-087** `P1` Centralize API client logic, request cancellation, error normalization, and response mapping appropriately.
- [ ] **ARC-088** `P1` Prevent leaked subscriptions, orphaned timers, repeated effects, and event listeners when components mount or unmount.
- [ ] **ARC-089** `P1` Use explicit loading, empty, stale, failed, and partial-success states across data-driven views.
- [ ] **ARC-090** `P1` Check route transitions, navigation history, account switching, and error boundaries for predictable state cleanup.
- [ ] **ARC-091** `P2` Consider route-level or component-level code splitting when measured startup costs justify it.
- [ ] **ARC-092** `P1` Assess bundle size, dependency footprint, rendering/hydration cost, and unnecessary client-side computation against project budgets.
- [ ] **ARC-093** `P1` Ensure essential UI content and interactions are not blocked by avoidable long dependency chains or large startup scripts.
- [ ] **ARC-094** `P1` Make semantic markup, keyboard support, and accessibility responsibilities part of component interfaces rather than one-off page patches.
- [ ] **ARC-095** `P1` Keep localization, theme, formatting, and responsive concerns reusable without embedding language or device assumptions in domain logic.
- [ ] **ARC-096** `P1` Confirm frontend authorization gates serve only as UX controls while backend services enforce access restrictions.

## Release gate

- [ ] Critical component boundaries, data ownership, public interfaces, and major failure/dependency paths are understood and reviewed by accountable engineers.
- [ ] Material architectural decisions are recorded, including alternatives, trade-offs, owners, and any unresolved risks.
- [ ] Changes affecting critical APIs or frontend architecture have documented compatibility and migration implications, with an approved path for affected consumers.
- [ ] The proposed code and structure have received the required engineering review, and no unresolved high-impact maintainability or design defect remains without documented acceptance by an authorized owner.
- [ ] All open architecture/code-quality blockers have named owners, dispositions, and follow-up dates in project-specific records.

**Domain-specific approval rule:** Block architecture approval for unowned critical interfaces or data, undocumented breaking changes, structural defects likely to invalidate core system guarantees, or unaccepted high-impact maintainability risks. Passing this review does not establish that functional, security, or operational testing has succeeded.

**Optional tooling:** [Frontend test examples](../references/optional-testing-tools-frontend.md#03_architecture_and_codequality), not prerequisites or verification evidence.

## Trusted references and scope

These checks interpret selected guidance into practical review questions; they are **not** direct quotations or a certification against any one framework.

- [Microsoft Azure Architecture Center — Architecture styles](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles) — choosing styles with explicit trade-offs and domain fit.
- [Microsoft Azure Architecture Center — Design for evolution](https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/design-for-evolution) — high cohesion, loose coupling, contracts, domain ownership, and controlled change.
- [AWS Well-Architected Framework — Operational excellence design principles](https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/oe-design-principles.html) — small reversible changes, failure anticipation, and iterative operational improvement.
- [AWS Prescriptive Guidance — Architectural decision records](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/) — documenting and communicating important architectural decisions.
- [AWS Prescriptive Guidance — ADR best practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/best-practices.html) — ownership, status, review cadence, and preserved decision history.
- [Google Engineering Practices — What to look for in a code review](https://google.github.io/eng-practices/review/reviewer/looking-for.html) — readability, complexity, design, correctness, and code health.
- [Google Engineering Practices — Small changes](https://google.github.io/eng-practices/review/developer/small-cls.html) — focused, reviewable, reversible changes.
- [OpenAPI Specification 3.2.1](https://spec.openapis.org/oas/v3.2.1.html) — machine-readable HTTP API contracts when applicable.
- [web.dev — Rendering on the web](https://web.dev/articles/rendering-on-the-web) — selecting frontend rendering approaches according to their trade-offs.
- [web.dev — Code-split JavaScript](https://web.dev/learn/performance/code-split-javascript) — modular JavaScript loading and startup responsiveness.

**Applicability:** Adapt check granularity to the project's size, language, architecture style, team, and risk. Independent deployment, event messaging, OpenAPI, and browser rendering are conditional—not mandatory for every project. Prefer simple designs that satisfy measured requirements.

**Source review date:** 2026-11-12.
