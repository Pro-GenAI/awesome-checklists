# 07 — Documentation and Developer Experience Checklist

> Verify that developers and operators can find accurate information, reproduce their local environment, understand API and system behavior, make changes safely, and maintain the product without relying on undocumented knowledge.

> **Scope: Shared / cross-cutting.** This file is one part of the 07_Documentation_and_DeveloperExperience.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](references/review-method.md) · [Optional framework crosswalk](references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Project documentation

- [ ] **DOC-001** `P2` Identify the documentation audiences, including new developers, maintainers, operators, integrators, and product users, and their top tasks.
- [ ] **DOC-002** `P1` Ensure the primary project entry point explains the product's purpose, supported scope, prerequisites, and where to get help.
- [ ] **DOC-003** `P1` Provide a clear path from the project entry point to installation, first successful use, contribution guidance, and deeper references.
- [ ] **DOC-004** `P1` Organize documentation so readers can find tutorials, task-oriented how-to guides, technical reference, and conceptual explanations where appropriate.
- [ ] **DOC-005** `P1` Name pages and headings using terms readers search for rather than internal team labels or ambiguous acronyms.
- [ ] **DOC-006** `P2` Assign an accountable owner and a review cadence to each critical documentation area.
- [ ] **DOC-007** `P1` Distinguish supported behavior, experimental features, deprecated features, and planned functionality explicitly.
- [ ] **DOC-010** `P1` Include expected results and success criteria for high-impact setup, configuration, or operational procedures.
- [ ] **DOC-011** `P1` Use accurate, runnable code and command examples with prerequisites and safe placeholder values.
- [ ] **DOC-012** `P1` Keep examples free of live credentials, sensitive customer data, unsafe defaults, and unapproved external endpoints.
- [ ] **DOC-013** `P1` Link related procedures and concepts near the point where readers need more context; avoid dead-end pages.
- [ ] **DOC-015** `P1` Use consistent terminology, units, file paths, configuration names, and formatting across related pages.
- [ ] **DOC-016** `P1` Write concise steps with explicit actions and observable outcomes; explain non-obvious risks before destructive operations.
- [ ] **DOC-017** `P1` Provide text alternatives, semantic headings, meaningful links, and accessible tables/images where documentation formats support them.
- [ ] **DOC-018** `P1` Keep changelogs or release notes accurate about changes that affect users, developers, or operators.
- [ ] **DOC-019** `P2` Document important functional limitations, environmental constraints, and compatibility considerations without marketing-only claims.
- [ ] **DOC-020** `P1` Review key guides with representative readers to confirm they can complete the intended tasks unaided.

## Developer setup and tooling

- [ ] **DOC-022** `P1` Provide a repeatable step-by-step setup from a clean workstation or development environment to a running local application.
- [ ] **DOC-023** `P2` Define where to obtain required repository access, test accounts, licenses, and development-only credentials without sharing secrets.
- [ ] **DOC-024** `P2` Maintain a safe example configuration file or documented variable inventory with descriptions and non-secret defaults.
- [ ] **DOC-025** `P2` Document dependency installation, lockfile usage, and any build artifacts or external services required to start development.
- [ ] **DOC-026** `P1` Offer a single obvious development start command or a clearly ordered equivalent set of commands.
- [ ] **DOC-028** `P1` Provide synthetic or approved nonproduction sample data and document how to seed and reset it.
- [ ] **DOC-029** `P1` Explain how to run unit, integration, contract, and end-to-end checks relevant to the project.
- [ ] **DOC-030** `P2` Document local formatting, linting, type-checking, and other quality commands, including how they match CI checks.
- [ ] **DOC-032** `P1` Explain how to test changes against external integrations safely, including mocks, sandboxes, and permitted test endpoints.
- [ ] **DOC-033** `P2` Document common environment-specific failures and proven troubleshooting steps with distinguishable symptoms.
- [ ] **DOC-034** `P1` Make errors from setup scripts actionable rather than returning an unexplained nonzero exit status.
- [ ] **DOC-035** `P1` Use pinned or declared tool versions, containers, or bootstrap tooling where it meaningfully reduces setup drift.
- [ ] **DOC-036** `P1` Test onboarding instructions periodically using a clean environment or an engineer unfamiliar with the project.
- [ ] **DOC-037** `P1` Clarify which tasks require elevated privileges and avoid recommending unnecessary broad permissions.
- [ ] **DOC-038** `P2` Describe required environment variables, build flags, feature flags, and the observable effects of toggling them.
- [ ] **DOC-039** `P1` Keep common development workflows discoverable through task runners, documented scripts, or a lightweight developer portal where useful.
- [ ] **DOC-040** `P2` Document how to validate changes locally before committing and how developers can interpret failing CI results.
- [ ] **DOC-041** `P2` Track time-to-first-success, recurrent setup blockers, or developer feedback to prioritize high-friction workflow improvements.
- [ ] **DOC-042** `P2` Define supported cleanup/reset commands so failed local experiments do not leave stale processes or contaminated test data.

## API and architecture documentation

- [ ] **DOC-043** `P1` Provide a current system context diagram or equivalent description of components, external dependencies, and trust/data boundaries.
- [ ] **DOC-044** `P1` Explain the responsibility and ownership of major modules, services, data stores, and integration points.
- [ ] **DOC-045** `P2` Document important architectural decisions, alternatives, constraints, and consequences in discoverable records.
- [ ] **DOC-046** `P1` Keep architecture descriptions synchronized with real implementation and clearly identify superseded diagrams or proposals.
- [ ] **DOC-047** `P2` Document critical data entities, source-of-truth boundaries, and meaningful consistency or transaction assumptions.
- [ ] **DOC-048** `P2` Describe operationally significant message flows, background jobs, event consumers, and failure-handling responsibilities.
- [ ] **DOC-050** `P1` Explain the intended stability, lifecycle, and compatibility policy for public or cross-team interfaces.
- [ ] **DOC-053** `P2` Describe authentication methods, scopes, authorization expectations, and how consumers obtain safe test credentials.
- [ ] **DOC-054** `P2` Document pagination, sorting, filtering, idempotency, and concurrency semantics where they affect client implementations.
- [ ] **DOC-056** `P2` Document rate limits, quotas, timeout behavior, retries, and recovery steps for unavailable dependencies.
- [ ] **DOC-060** `P1` Ensure interface examples are tested or generated from authoritative contracts so they do not drift from production.

## Maintenance and onboarding

- [ ] **DOC-064** `P1` Explain repository contribution conventions, required checks, expected review behavior, and issue/commit practices as applicable.
- [ ] **DOC-066** `P1` Provide a guided first contribution or safe starter task with prerequisites and completion criteria for new team members where useful.
- [ ] **DOC-067** `P2` Maintain current service ownership and escalation information for critical components and support contacts.
- [ ] **DOC-068** `P1` Keep operational runbooks for common failures, incident triage, restoration, and emergency actions where risk warrants them.
- [ ] **DOC-069** `P1` Verify runbooks contain prerequisites, authorized access paths, commands, expected outcomes, and stopping/rollback points.
- [ ] **DOC-070** `P1` Provide clear instructions for transferring ownership, rotating credentials, renewing certificates, and other time-sensitive maintenance tasks.
- [ ] **DOC-072** `P1` Keep a changelog or change-summary process for documentation, interface changes, and operational procedures.
- [ ] **DOC-073** `P1` Store documentation with a reviewable history and integrate its updates into relevant feature or release changes.
- [ ] **DOC-074** `P1` Use automated checks for broken links, formatting, stale code snippets, and site builds where tooling supports them.
- [ ] **DOC-075** `P1` Validate crucial examples or command sequences in CI or periodic manual checks, with documented coverage gaps.
- [ ] **DOC-076** `P2` Define versioning, archiving, and redirect policies to prevent obsolete guides from misleading current users.
- [ ] **DOC-077** `P1` Remove or clearly mark unsupported, duplicated, or superseded procedures and link to their replacements.
- [ ] **DOC-078** `P1` Set documentation review triggers for incidents, failed onboarding, recurring support issues, and product behavior changes.
- [ ] **DOC-079** `P1` Review and triage documentation feedback using owners, priority, and response targets.
- [ ] **DOC-080** `P1` Ensure critical internal knowledge does not exist only in personal chats, private laptops, or one unmaintained person's notes.
- [ ] **DOC-082** `P1` Measure discoverability, correctness, setup success, or support burden through appropriate feedback and task-based validation.

- [ ] **DOC-119** `P1` For projects accepting community contributions, provide discoverable participation and conduct expectations, a usable confidential reporting channel with named handling responsibility, and guidance for issues or pull requests appropriate to the project.

- [ ] **DOC-120** `P1` For public project entry points such as a README, identify the project and its current responsible maintainer or organization, provide a working canonical repository or homepage link, and explain the project’s purpose before lower-level implementation details.
- [ ] **DOC-121** `P1` Make usage, redistribution, and licensing terms discoverable from the README or project entry point; link the authoritative license or access policy rather than suggesting that public source availability alone grants reuse rights.
- [ ] **DOC-122** `P1` Ask a reviewer unfamiliar with the project to follow the README’s prerequisite, install, and first-use instructions from a clean supported environment; capture the actual result, hidden assumptions, broken links, and required fixes.

## Release gate

- [ ] Critical readers can discover the current getting-started, support, architectural, and operational documentation appropriate to their responsibilities.
- [ ] Setup and essential development, test, or build commands have been exercised successfully on a supported clean environment or have an approved, documented risk-based alternative.
- [ ] Public or cross-team API/interface references and associated runnable examples match the release candidate, with visible compatibility and migration guidance where relevant.
- [ ] Frontend component, accessibility, data-state, and deployment guidance is updated for affected UI features where applicable.
- [ ] Critical operational runbooks, ownership contacts, and incident escalation paths are accurate and available to authorized responders.
- [ ] Documentation errors affecting essential onboarding, safe operations, or integration are fixed, or have explicit authorized dispositions and tracked remediation.
- [ ] A named owner has reviewed documentation currency, broken links, and unresolved feedback for the exact release being approved.

**Domain-specific approval rule:** Block documentation/enablement sign-off when a critical setup cannot be reproduced, the documented interface contradicts deployed behavior, a destructive procedure is misleading, or essential operational steps or owners are missing without authorized mitigation. Passing this checklist does not substitute for testing, security, accessibility conformance, or legal review.

**Optional tooling:** [File-specific tool examples](references/optional-testing-tools-shared.md#07_documentation_and_developerexperience), not prerequisites or verification evidence.

## Trusted references and scope

These sources inform practical, verifiable documentation and developer-experience review tasks. They are not universal certification standards or verbatim rules for every software project.

- [Diátaxis — Documentation framework](https://diataxis.fr/) — organizing tutorials, how-to guides, reference, and explanation by reader need.
- [DORA — Documentation quality](https://dora.dev/capabilities/documentation-quality/) — documentation clarity, findability, reliability, and developer effectiveness.
- [Write the Docs — Docs as code](https://www.writethedocs.org/guide/docs-as-code/) — version control, review, automated tests, and shared documentation ownership.
- [Google developer documentation style guide](https://developers.google.com/style) — clear, consistent, audience-centered technical writing.
- [Google developer documentation — Code samples](https://developers.google.com/style/code-samples) — formatting, introducing, and explaining runnable code samples.
- [Microsoft Writing Style Guide — Code examples](https://learn.microsoft.com/en-us/style-guide/developer-content/code-examples) — task-focused, safe, tested code examples with expected results.
- [Microsoft Writing Style Guide — Writing for all abilities](https://learn.microsoft.com/en-us/style-guide/accessibility/writing-all-abilities) — clear, accessible language and alternative interaction guidance.
- [GitHub Docs — About README files](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) — project purpose, getting started, support, and repository discoverability.
- [GitHub Docs — Guidelines for repository contributors](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors) — documenting contribution workflows and expectations.
- [GitHub Docs — About CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) — repository ownership and review routing when used.
- [OpenAPI Specification v3.2.1](https://spec.openapis.org/oas/v3.2.1.html) — machine-readable descriptions of HTTP API operations and contracts.
- [W3C WAI — Headings](https://www.w3.org/WAI/tutorials/page-structure/headings/) — accessible document heading structure and navigation.

**Applicability:** Documentation types and review depth depend on project size, audience, release risk, language, and support model. GitHub-specific contributor features, CODEOWNERS, shared design systems, formal OpenAPI descriptions, and public API quickstarts are conditional; choose equivalent controls where appropriate. `README.md` in this checklist repository remains intentionally minimal and must not be changed without a separate request.

- [GitHub Docs — Adding a code of conduct](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project) — participation expectations and reporting.
- [GitHub Docs — Guidelines for repository contributors](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors) — discoverable contribution procedures.

- [ddbeck — README Checklist](https://github.com/ddbeck/readme-checklist/blob/main/checklist.md) — entry-point identity, usage terms, first-use walkthrough and reader-centered documentation (historical community guidance; apply conditionally).
- [GitHub Docs — About README files](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) — repository purpose, orientation and getting started.

**Source review date:** 2026-11-13.
