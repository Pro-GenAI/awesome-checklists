# 03 — Architecture and Code Quality Checklist

> Review design trade-offs, system boundaries, maintainable code, engineering reviews, decision records, and API/frontend architecture. This checklist evaluates structure and evolvability; it complements the dedicated Testing, Security, DevOps, and Performance files.

> **Scope: Shared / cross-cutting.** This file is one part of the 03_Architecture_and_CodeQuality.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](references/review-method.md) · [Optional framework crosswalk](references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Architecture and system boundaries

- [ ] **ARC-002** `P1` Choose an architecture style based on actual domain complexity, scale, team capabilities, and non-functional requirements; record its alternatives and trade-offs.
- [ ] **ARC-003** `P2` Identify bounded contexts, business capabilities, and ownership for each major service or module.
- [ ] **ARC-004** `P2` Define clear component responsibilities so domain rules are not duplicated across unrelated layers.
- [ ] **ARC-005** `P1` Make dependency directions explicit and prevent accidental cycles between modules or services.
- [ ] **ARC-006** `P1` Check that component boundaries promote high cohesion and loose coupling rather than arbitrary microservice fragmentation.
- [ ] **ARC-007** `P2` Document public and internal interfaces, events, queues, storage boundaries, and integration owners.
- [ ] **ARC-008** `P1` Clarify which component owns each persistent data entity and who can modify its canonical state.
- [ ] **ARC-009** `P1` Review whether synchronous calls and distributed transactions are necessary, and account for latency or partial failures across boundaries.
- [ ] **ARC-010** `P2` Specify event delivery, ordering, duplication, and eventual-consistency assumptions for asynchronous communication when used.
- [ ] **ARC-011** `P2` Identify single points of failure and the architectural recovery or degradation strategies for critical user workflows.
- [ ] **ARC-013** `P1` Assess whether third-party products, managed services, or custom implementations reduce or increase complexity and operational burden.
- [ ] **ARC-014** `P1` Verify the architecture supports documented performance, availability, privacy, accessibility, and cost constraints without overengineering.
- [ ] **ARC-016** `P1` Limit unnecessary sharing of databases, mutable state, build artifacts, and privileged credentials between unrelated components.
- [ ] **ARC-017** `P1` Ensure architectural diagrams reflect the current implementation, not only an obsolete initial proposal.
- [ ] **ARC-018** `P2` Assign a technical owner to each critical component and dependency and document the escalation path for design changes.

## Code organization and maintainability

- [ ] **ARC-019** `P1` Group related functionality into coherent modules or packages with clear names and public interfaces.
- [ ] **ARC-020** `P1` Keep business logic separate from transport, persistence, framework glue, and presentation where this reduces coupling.
- [ ] **ARC-021** `P1` Ensure implementations expose only the minimum intended public surface; hide internal helpers and representation details.
- [ ] **ARC-022** `P1` Use language-appropriate naming, formatting, linting, and typing conventions consistently across the repository.
- [ ] **ARC-023** `P1` Keep functions, classes, and components focused enough for a reviewer to understand their responsibilities.
- [ ] **ARC-024** `P1` Replace unnecessary duplication with reusable abstractions only when they clarify actual repeated behavior.
- [ ] **ARC-025** `P1` Avoid speculative generalization, unused extension points, and abstractions that add more complexity than they remove.
- [ ] **ARC-026** `P1` Make exceptional behavior explicit using appropriate error types, return contracts, and structured recovery paths.
- [ ] **ARC-027** `P2` Document non-obvious invariants, concurrency assumptions, and *why* unusual code exists rather than narrating obvious syntax.
- [ ] **ARC-028** `P1` Check that configuration and environment-dependent behavior are separated from application logic and have safe defaults.
- [ ] **ARC-029** `P1` Make dependency injection and seams for external integrations practical enough for isolated testing.
- [ ] **ARC-030** `P1` Use immutable values or controlled state updates when they simplify reasoning about concurrent or asynchronous code.
- [ ] **ARC-032** `P1` Ensure new dependencies have a documented need, maintained version policy, and no unnecessary duplication of existing capabilities.
- [ ] **ARC-033** `P1` Provide concise development and build instructions so a new maintainer can locate entry points and reproduce a build.
- [ ] **ARC-034** `P1` Keep generated code, migrations, and build artifacts clearly distinguished from manually maintained source.
- [ ] **ARC-035** `P1` Use tooling or targeted refactoring to prevent unbounded module size, circular imports, and hidden coupling over time.

## Reviews and technical debt

- [ ] **ARC-036** `P1` Require an appropriate peer review or approved alternative for meaningful code changes, with high-risk changes receiving suitable specialist review.
- [ ] **ARC-037** `P1` Keep change sets small and self-contained where practical, including related tests and documentation.
- [ ] **ARC-038** `P1` Write change descriptions that explain what changed, why, user impact, and relevant migration or compatibility considerations.
- [ ] **ARC-039** `P1` Have reviewers examine overall design fit before focusing on line-level style concerns.
- [ ] **ARC-040** `P1` Review for correctness, readability, naming, unnecessary complexity, and conformity with established conventions.
- [ ] **ARC-041** `P1` Review concurrency, error paths, lifecycle/resource cleanup, and side effects where applicable.
- [ ] **ARC-042** `P1` Evaluate whether tests meaningfully cover the changed behavior; refer detailed test adequacy to the Testing checklist.
- [ ] **ARC-044** `P2` Record substantial reviewer disagreements, the resolution, and accountable decision-maker.
- [ ] **ARC-045** `P2` Track recurring defects or friction that indicate structural debt rather than applying only local patches.
- [ ] **ARC-046** `P2` Maintain a prioritized technical-debt backlog with impact, owner, mitigation, and expected remediation window.
- [ ] **ARC-047** `P1` Distinguish intentional short-term compromises from unnoticed complexity and preserve their rationale.
- [ ] **ARC-048** `P2` Identify high-change or high-defect modules and consider targeted decomposition or refactoring with measurable outcomes.
- [ ] **ARC-049** `P1` Ensure required changes to public contracts, dependency owners, and operational runbooks are captured in the same review cycle.
- [ ] **ARC-050** `P1` Confirm accepted review suggestions are applied or explicitly resolved before approval.
- [ ] **ARC-051** `P1` Review whether a change improves or degrades overall code health, not just whether its immediate feature works.

## Architecture decisions and evolution

- [ ] **ARC-052** `P1` Use an architecture decision record (ADR) or equivalent for material structural, technology, interface, and operational choices.
- [ ] **ARC-053** `P1` Capture the decision context, constraints, alternatives considered, chosen option, and expected consequences.
- [ ] **ARC-054** `P2` Record each material decision's status, date, owner, and affected components.
- [ ] **ARC-055** `P1` Make significant architectural assumptions and trade-offs discoverable to future maintainers.
- [ ] **ARC-056** `P1` Keep superseded decisions in history and link the replacement rather than silently rewriting past rationale.
- [ ] **ARC-057** `P1` Review architecture against observed change frequency, outages, cost, and developer feedback at an agreed cadence.
- [ ] **ARC-058** `P2` Define objective architecture fitness checks such as dependency-rule checks, contract checks, or measured performance constraints where appropriate.
- [ ] **ARC-059** `P1` Plan versioned interfaces and incremental migrations to reduce simultaneous changes across dependent components.
- [ ] **ARC-061** `P2` Document whether new components can be rolled back or replaced independently and the constraints on doing so.
- [ ] **ARC-062** `P1` Periodically reconsider if the selected architecture remains the simplest adequate approach for the current scale and team.
- [ ] **ARC-063** `P1` Retire unused modules, obsolete integrations, abandoned flags, and deprecated pathways through planned cleanup.
- [ ] **ARC-064** `P1` Link architecture follow-ups to owners, milestones, and observable completion criteria rather than leaving undocumented intentions.

## Release gate

- [ ] Critical component boundaries, data ownership, public interfaces, and major failure/dependency paths are understood and reviewed by accountable engineers.
- [ ] Material architectural decisions are recorded, including alternatives, trade-offs, owners, and any unresolved risks.
- [ ] Changes affecting critical APIs or frontend architecture have documented compatibility and migration implications, with an approved path for affected consumers.
- [ ] The proposed code and structure have received the required engineering review, and no unresolved high-impact maintainability or design defect remains without documented acceptance by an authorized owner.
- [ ] All open architecture/code-quality blockers have named owners, dispositions, and follow-up dates in project-specific records.

**Domain-specific approval rule:** Block architecture approval for unowned critical interfaces or data, undocumented breaking changes, structural defects likely to invalidate core system guarantees, or unaccepted high-impact maintainability risks. Passing this review does not establish that functional, security, or operational testing has succeeded.

**Optional tooling:** [File-specific tool examples](references/optional-testing-tools-shared.md#03_architecture_and_codequality), not prerequisites or verification evidence.

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
