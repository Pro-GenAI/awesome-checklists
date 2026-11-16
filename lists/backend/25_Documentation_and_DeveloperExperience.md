# 25 — Documentation and Developer Experience Checklist

> Verify that developers and operators can find accurate information, reproduce their local environment, understand API and system behavior, make changes safely, and maintain the product without relying on undocumented knowledge.

> **Scope: Backend / API-specific.** This file is one part of the 25_Documentation_and_DeveloperExperience.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Project documentation

- [ ] **DOC-008** `P1` State which product, API, SDK, or documentation version each release-sensitive page describes.
- [ ] **DOC-009** `P2` Describe operating systems, runtimes, infrastructure, user roles, and other prerequisites before asking readers to follow steps.

## Developer setup and tooling

- [ ] **DOC-021** `P2` Document the supported development platforms, language/runtime versions, package managers, and essential tooling.
- [ ] **DOC-027** `P2` Document local database, queue, storage, emulator, or container dependencies and how to provision/teardown them where applicable.
- [ ] **DOC-031** `P2` Describe how to debug a common request or user journey using logs, breakpoints, traces, or diagnostic tooling.

## API and architecture documentation

- [ ] **DOC-049** `P1` Link architectural overviews to applicable runbooks, interface references, and deployment procedures without duplicating them unnecessarily.
- [ ] **DOC-051** `P2` Maintain a versioned API description, such as OpenAPI for applicable HTTP APIs, tied to actual deployed behavior.
- [ ] **DOC-052** `P2` Document endpoint/resource purposes, operations, request bodies, responses, and status codes for supported API versions.
- [ ] **DOC-055** `P1` Provide representative successful, failed, and edge-case request/response examples without sensitive data.
- [ ] **DOC-057** `P1` Explain webhook/event delivery, payload versions, signature verification, retries, and duplicate handling when used.
- [ ] **DOC-058** `P2` Publish SDK compatibility, supported language/runtime versions, and migration instructions where SDKs are offered.
- [ ] **DOC-059** `P2` Describe API changes, deprecations, breaking-change windows, and customer notification/support channels.
- [ ] **DOC-061** `P2` Identify which API and architectural references are internal-only versus safe for external publication.
- [ ] **DOC-062** `P1` Keep architecture and API ownership and change-request contacts easy to locate.

## Maintenance and onboarding

- [ ] **DOC-063** `P2` Document how to propose a change, report a bug, request support, or submit a documentation correction.
- [ ] **DOC-071** `P1` Explain how to deploy, roll forward, or revert a change at the level needed by authorized operators.
- [ ] **DOC-081** `P1` Check that documentation permissions are sufficient for intended readers but restrict secrets and sensitive infrastructure details.

## API Checks

- [ ] **DOC-083** `P1` Provide a maintained API quickstart that can obtain safe credentials and execute a first successful request in an allowed environment.
- [ ] **DOC-084** `P2` Identify every supported API base URL, environment, version, and how client authentication differs across them.
- [ ] **DOC-085** `P1` Make operation documentation match actual methods, paths, headers, required parameters, request bodies, and content types.
- [ ] **DOC-086** `P1` Explain security schemes, authorization scopes, token rotation, and safe credential storage for clients.
- [ ] **DOC-087** `P1` Provide request and response examples for success, validation failures, authorization denial, throttling, and service errors.
- [ ] **DOC-088** `P2` Document error formats with stable error codes, retryability, correlation IDs, and actionable client recovery guidance.
- [ ] **DOC-089** `P2` Describe pagination, cursor stability, filters, sorts, and response limits with examples where supported.
- [ ] **DOC-090** `P1` Explain rate limits and quota accounting, including relevant response headers and retry-after behavior when implemented.
- [ ] **DOC-091** `P2` Document whether writes are idempotent, how idempotency keys work, and what to do after ambiguous timeouts.
- [ ] **DOC-092** `P1` Explain concurrency controls, optimistic locking, conditional requests, or conflict resolution where applicable.
- [ ] **DOC-093** `P2` Describe webhooks, event subscriptions, delivery ordering, signatures, duplicate delivery, and retry rules when relevant.
- [ ] **DOC-094** `P1` Provide SDK installation and usage examples pinned or clearly matched to a supported API version when SDKs exist.
- [ ] **DOC-095** `P2` Publish data types, enum values, nullability, timestamps, monetary units, and encoding semantics needed for safe integrations.
- [ ] **DOC-096** `P1` Include warnings and examples for destructive operations, bulk exports, irreversible actions, or large payloads.
- [ ] **DOC-097** `P1` Keep OpenAPI or an equivalent contract synchronized with live service behavior and validate it before publication.
- [ ] **DOC-098** `P2` Define API versioning, deprecation timelines, migration steps, and contact paths for breaking changes.
- [ ] **DOC-099** `P1` Explain sandbox fixtures, test credentials, mocks, and rate-limited test procedures without requiring real customer data.
- [ ] **DOC-100** `P1` Test published copy/paste examples against a controlled environment with valid dependencies and current configuration.

## Release gate

- [ ] Critical readers can discover the current getting-started, support, architectural, and operational documentation appropriate to their responsibilities.
- [ ] Setup and essential development, test, or build commands have been exercised successfully on a supported clean environment or have an approved, documented risk-based alternative.
- [ ] Public or cross-team API/interface references and associated runnable examples match the release candidate, with visible compatibility and migration guidance where relevant.
- [ ] Frontend component, accessibility, data-state, and deployment guidance is updated for affected UI features where applicable.
- [ ] Critical operational runbooks, ownership contacts, and incident escalation paths are accurate and available to authorized responders.
- [ ] Documentation errors affecting essential onboarding, safe operations, or integration are fixed, or have explicit authorized dispositions and tracked remediation.
- [ ] A named owner has reviewed documentation currency, broken links, and unresolved feedback for the exact release being approved.

**Domain-specific approval rule:** Block documentation/enablement sign-off when a critical setup cannot be reproduced, the documented interface contradicts deployed behavior, a destructive procedure is misleading, or essential operational steps or owners are missing without authorized mitigation. Passing this checklist does not substitute for testing, security, accessibility conformance, or legal review.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#25_documentation_and_developerexperience), not prerequisites or verification evidence.

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

**Source review date:** 2026-11-12.
