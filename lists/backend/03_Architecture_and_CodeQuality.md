# 03 — Architecture and Code Quality Checklist

> Review design trade-offs, system boundaries, maintainable code, engineering reviews, decision records, and API/frontend architecture. This checklist evaluates structure and evolvability; it complements the dedicated Testing, Security, DevOps, and Performance files.

> **Scope: Backend / API-specific.** This file is one part of the 03_Architecture_and_CodeQuality.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Architecture and system boundaries

- [ ] **ARC-001** `P2` Document the system context, users, external systems, deployment environment, and critical data flows in diagrams or equivalent artifacts.
- [ ] **ARC-012** `P1` Check that cross-cutting concerns (identity, configuration, telemetry, caching) have consistent ownership without centralizing business rules in gateways.
- [ ] **ARC-015** `P2` Record deployment units, stateful/stateless components, environment boundaries, and independent release requirements.

## Code organization and maintainability

- [ ] **ARC-031** `P1` Keep database access, transactions, and schema evolution responsibilities explicit in the code structure.

## Architecture decisions and evolution

- [ ] **ARC-060** `P2` Specify transition strategies for changes to storage, queues, runtime, frameworks, or public contracts.

## API Checks

- [ ] **ARC-065** `P1` Make each API's ownership and business capability explicit; avoid endpoints that bypass intended domain boundaries.
- [ ] **ARC-066** `P1` Separate transport concerns from domain rules so the same invariants hold across different consumers.
- [ ] **ARC-067** `P2` Maintain a versioned, machine-readable API contract (such as OpenAPI for HTTP APIs) when appropriate.
- [ ] **ARC-068** `P1` Check that request/response models do not leak internal database schemas or framework-specific implementation details unnecessarily.
- [ ] **ARC-069** `P2` Document resource identity, ownership, operations, data representation, and error contracts consistently.
- [ ] **ARC-070** `P1` Design pagination, filtering, sorting, and partial updates with predictable, documented semantics when supported.
- [ ] **ARC-071** `P2` Define backward-compatibility expectations for fields, enums, nullability, status codes, and request behavior.
- [ ] **ARC-072** `P1` Make deprecations and migrations visible to consumers before removing widely used contracts.
- [ ] **ARC-073** `P2` Specify whether clients may retry writes and how idempotency is implemented where needed.
- [ ] **ARC-074** `P2` Document synchronous versus asynchronous operations, completion signals, polling, and event delivery when relevant.
- [ ] **ARC-075** `P2` Define timeouts, failure boundaries, throttling/quotas, and fallback behaviors between dependent services.
- [ ] **ARC-076** `P1` Check that shared API clients/SDKs encapsulate protocol details instead of spreading low-level calls across unrelated modules.
- [ ] **ARC-077** `P1` Ensure API gateway layers route, authenticate, and observe traffic without becoming the sole owner of domain logic.
- [ ] **ARC-078** `P1` Validate consumer/provider contract tests or compatibility checks are part of the change workflow.
- [ ] **ARC-079** `P2` Document API change owners, integration dependencies, and how breaking changes trigger release coordination.
- [ ] **ARC-080** `P1` Verify cross-tenant authorization and data access remain enforced in the responsible service rather than relying on frontend checks alone.

## Release gate

- [ ] Critical component boundaries, data ownership, public interfaces, and major failure/dependency paths are understood and reviewed by accountable engineers.
- [ ] Material architectural decisions are recorded, including alternatives, trade-offs, owners, and any unresolved risks.
- [ ] Changes affecting critical APIs or frontend architecture have documented compatibility and migration implications, with an approved path for affected consumers.
- [ ] The proposed code and structure have received the required engineering review, and no unresolved high-impact maintainability or design defect remains without documented acceptance by an authorized owner.
- [ ] All open architecture/code-quality blockers have named owners, dispositions, and follow-up dates in project-specific records.

**Domain-specific approval rule:** Block architecture approval for unowned critical interfaces or data, undocumented breaking changes, structural defects likely to invalidate core system guarantees, or unaccepted high-impact maintainability risks. Passing this review does not establish that functional, security, or operational testing has succeeded.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#03_architecture_and_codequality), not prerequisites or verification evidence.

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
