# 09 — Security Checklist

> Assess confidentiality, integrity, availability, abuse resistance, and operational security proportionate to project risk.

> **Scope: Backend / API-specific.** This file is one part of the 09_Security.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Identity and access management

- [ ] **SEC-007** `P0` Authorization is enforced server-side on every protected object, action, and tenant boundary.
- [ ] **SEC-045** `P0` Test tenant isolation at query, storage, cache, and API response boundaries.

## Application, API, and supply-chain security

- [ ] **SEC-013** `P1` Test for HTTP request-smuggling and desynchronization at applicable proxy-to-backend boundaries.
- [ ] **SEC-014** `P1` Test replay resistance for high-impact, non-idempotent API operations when a repeated request could cause unintended effects.
- [ ] **SEC-121** `P1` Test that user-controlled filesystem paths cannot escape authorized directory boundaries.
- [ ] **SEC-015** `P1` Scan dependencies, lockfiles, images and build tools for known vulnerabilities and malicious packages; review unmaintained or unused dependencies and triage findings before release.
- [ ] **SEC-098** `P1` Before installing an AI-suggested or other new package, verify its exact name, authoritative registry, maintainer/provenance and approved version; reject invented or lookalike packages even if no CVE is reported.
- [ ] **SEC-046** `P2` Track APIs, versions, and public endpoints in an inventory with accountable owners.
- [ ] **SEC-048** `P1` Assess business-flow abuse (bulk purchases, scraping, automated signup) beyond simple request rate limits.
- [ ] **SEC-049** `P1` Confirm file handling enforces type, size, storage, malware scanning, and safe serving as applicable.
- [ ] **SEC-099** `P1` For archive/image/document processing, bound expanded size, pixels/pages, nesting, CPU, memory and processing time as applicable; test decompression bombs, giant images and malformed files in isolation.

## Secrets, encryption, and data protection

- [ ] **SEC-019** `P0` Scan current source, available Git history/branches, build artifacts, and logs for passwords, API keys, private keys, or tokens; revoke or rotate confirmed exposures and assess impact instead of assuming removal from the latest commit resolves a leak.
- [ ] **SEC-022** `P1` Sensitive data is encrypted at rest where warranted, with protected keys and defined rotation/backup.

## Infrastructure and deployment

- [ ] **SEC-025** `P1` Cloud identities, network boundaries, firewall rules, public storage, and database exposure are reviewed.
- [ ] **SEC-100** `P1` For private files and generated downloads, reject unintended public reads and authorize each object; where signed URLs are used, test scope, expiry and the bounded residual-access window following revocation.
- [ ] **SEC-026** `P1` Servers, containers, and runtime settings are hardened; unused services and debug features are disabled.
- [ ] **SEC-028** `P1` Infrastructure-as-code and deployment changes are reviewed, tested, and tracked.
- [ ] **SEC-052** `P1` Verify edge/CDN and API gateway controls match intended origin permissions and do not bypass application authorization.
- [ ] **SEC-027** `P1` Security headers, CORS, caching of sensitive responses, and cookie attributes are configured appropriately.
- [ ] **SEC-029** `P1` Backups are protected and restore procedures are tested.
- [ ] **SEC-030** `P1` Monitoring detects suspicious access, configuration drift, and high-risk failures.
- [ ] **SEC-053** `P1` Test cache headers and isolation for authenticated or user-specific API and HTML responses.

## Security scope and architecture

- [ ] **SEC-005** `P1` Production, staging, and development environments are appropriately isolated.

## API Checks

> Apply to API endpoints, client integrations, webhooks, or data feeds present in the project. Record N/A with reasons if none exist.

**Reference basis:** [OWASP API Security Top 10 (2023)](https://api-security.owasp.org/editions/2023/en/0x11-t10/); [OWASP Application Security Verification Standard (ASVS) 5.0](https://asvs.owasp.org/); [OWASP ASVS 5.0 control families (web frontend and API)](https://cornucopia.owasp.org/taxonomy/asvs-5.0).

- [ ] **SEC-058** `P0` Perform object-level authorization tests for manipulated IDs on every read, write, and delete endpoint (OWASP API1).
- [ ] **SEC-059** `P0` Test authentication token issuance, expiry, audience/issuer, signature validation, revocation, and replay resistance where relevant.
- [ ] **SEC-060** `P1` Verify field-level read/write authorization against over-posting, mass assignment, and excess property exposure (API3).
- [ ] **SEC-061** `P1` Verify function-level authorization for administrative and privileged methods (API5).
- [ ] **SEC-062** `P1` Enforce and test resource limits: rate, page size, payload size, timeouts, concurrency, and costly downstream calls (API4).
- [ ] **SEC-063** `P1` Test fake signup/trial, account recovery, verification-message, purchasing and payment-card-testing abuse; use risk-based friction, rate limits and payment-provider fraud controls as applicable (API6).
- [ ] **SEC-064** `P1` Test SSRF controls for URL-fetching endpoints and all outbound destinations (API7).
- [ ] **SEC-065** `P1` Validate request schemas and content types and reject unknown/unsafe fields as appropriate.
- [ ] **SEC-066** `P1` Check CORS allowlists, credentials, preflight behavior, and API security headers without treating CORS as authentication.
- [ ] **SEC-067** `P2` Inventory all active API versions and hosts; disable forgotten debug, staging, and deprecated endpoints (API9).
- [ ] **SEC-068** `P1` Validate and constrain third-party API data before trusting it; protect API keys and outbound authentication (API10).
- [ ] **SEC-069** `P1` Verify production errors (including 401/403/404) do not reveal raw stack traces, internal paths, credentials or debug details; retain restricted diagnostics tied to safe correlation IDs.
- [ ] **SEC-070** `P1` Ensure webhook authenticity, replay defenses, idempotency, and signature checking where used.
- [ ] **SEC-101** `P1` For paid checkout and entitlements, derive products, amounts and currency from trusted server data; verify payment-provider success and matching order details before fulfillment, including tampered-client and duplicate-callback tests.
- [ ] **SEC-071** `P1` Audit access-control decisions, significant privileged/admin state changes (actor, target, action, outcome), and abuse events with appropriate integrity and access controls, without storing secrets or unnecessary sensitive payloads.

- [ ] **SEC-086** `P1` Protect Docker daemon API endpoints and socket mounts: inventory access, restrict users and automation, and require authenticated SSH or mutual TLS for authorized remote access.
- [ ] **SEC-087** `P1` Evaluate rootless Docker or user-namespace remapping where supported, verifying UID/GID mapping, filesystem ownership, privileged exceptions, and actual host isolation.
- [ ] **SEC-088** `P1` Reject unnecessary privileged containers, host namespace sharing, and Docker socket passthrough; document and test narrowly approved exceptions.
- [ ] **SEC-089** `P1` Review effective Linux capabilities, seccomp restrictions, SELinux/AppArmor profiles, and privilege-escalation settings rather than relying only on a default image configuration.
- [ ] **SEC-090** `P1` Restrict container device passthrough and host filesystem mounts to essential, least-privilege paths, using read-only access where feasible and testing host-data exposure.
- [ ] **SEC-091** `P1` Enforce and exercise CPU, memory, PID and applicable I/O constraints for container workloads; measure behavior under resource exhaustion without assuming the defaults are safe.
- [ ] **SEC-092** `P1` Test container ingress/egress and inter-service isolation, exposed ports, and multi-tenant trust boundaries without relying on obsolete Docker link/ICC configuration.
- [ ] **SEC-093** `P1` Verify image origin and dependency integrity, approved image versions or digests, signature/attestation checks when supported, and patch/rebuild response to actionable vulnerabilities.

- [ ] **SEC-094** `P1` For Node.js services, test the policy for `uncaughtException`, unhandled promise rejections, and fatal runtime failures: capture non-sensitive diagnostics, stop serving on unrecoverable state, drain or terminate safely where possible, and verify an external supervisor restarts only after a clean recovery boundary.
- [ ] **SEC-095** `P1` For Node.js applications, review untrusted values that reach `eval`, dynamic module imports, `child_process`, regular-expression constructors, or filesystem paths; enforce explicit allowlists and safe path containment, and test command injection, traversal, and regular-expression denial-of-service cases.
- [ ] **SEC-096** `P1` For Node.js package installs and builds, audit dependency lifecycle and post-install scripts with the approved lockfile and CI pipeline; restrict script execution and build permissions according to risk and test that untrusted packages cannot obtain unnecessary secrets or network access.
- [ ] **SEC-097** `P1` For session-based Express or similar Node.js services, verify production session stores are durable and appropriately shared across replicas, sessions expire and are revoked server-side, and reverse-proxy trust and cookie security settings are correctly matched to actual TLS termination.

## Release gate

> **Common security sign-off:** Apply the [shared Security release gate](../05_Security.md#release-gate) to all relevant Security slices. Record one approval decision, with evidence or justified exceptions for this slice.

**Domain-specific approval rule:** Block release for exploitable critical/high findings without approved mitigation, missing authorization boundaries, exposed secrets, or unprotected sensitive data.

**Optional tools:** See the [separate security tooling catalog](../references/security-testing-tools.md); no third-party agent skill is required to satisfy this checklist.

## Trusted references and scope

- [GitHub Docs — Secret scanning](https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning) — full-history credential exposure.

The checks above are adapted into practical verification questions from these authoritative publications (not copied as standards text). Verify current versions and the project's scope before sign-off.

- [OWASP API Security Top 10 (2023)](https://api-security.owasp.org/editions/2023/en/0x11-t10/)
- [OWASP Application Security Verification Standard (ASVS) 5.0](https://asvs.owasp.org/)
- [OWASP ASVS 5.0 control families (web frontend and API)](https://cornucopia.owasp.org/taxonomy/asvs-5.0)

Guidance is risk-based and project-specific; sources do not replace testing or specialist review. Accessibility sources belong in the Accessibility domain; generative-AI risk profiles belong in the AI scope.

- [Primary guidance](https://docs.docker.com/engine/security/protect-access/) — current platform-specific configuration and validation.
- [Primary guidance](https://docs.docker.com/engine/security/rootless/) — current platform-specific configuration and validation.
- [Primary guidance](https://docs.docker.com/engine/security/userns-remap) — current platform-specific configuration and validation.
- [Primary guidance](https://docs.docker.com/engine/security/seccomp/) — current platform-specific configuration and validation.
- [Primary guidance](https://docs.docker.com/engine/security/apparmor/) — current platform-specific configuration and validation.
- [Primary guidance](https://docs.docker.com/engine/containers/run/) — current platform-specific configuration and validation.
- [Primary guidance](https://docs.docker.com/build/building/best-practices/) — current platform-specific configuration and validation.

- [Node.js — Process events and fatal exceptions](https://nodejs.org/api/process.html) — unhandled rejections, uncaught exceptions, and unsafe continuation after fatal failure.
- [Node.js — Child process](https://nodejs.org/api/child_process.html) — shell execution and untrusted input concerns.
- [Node.js — File system](https://nodejs.org/api/fs.html) — filesystem APIs and path handling.
- [npm Docs — Ignore scripts](https://docs.npmjs.com/cli/commands/npm-ci) — reproducible installs, lifecycle scripts, and install controls.
- [Express — Production security best practices](https://expressjs.com/en/advanced/best-practice-security.html) — secure sessions, production error handling, and deployment settings.
- [strong-node — historical Node.js security checklist](https://github.com/jesusprubio/strong-node/blob/main/README.md) — reviewed checklist topics; dated framework/plugin advice is not automatically adopted.

- [OWASP File Upload](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) — decompression and parser resource limits.
- [GitHub dependency review](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-dependency-changes-in-a-pull-request) — added-package vetting.
- [Stripe card-testing prevention](https://support.stripe.com/questions/how-do-i-prevent-card-testing-attacks?locale=en-GB) — payment abuse mitigations.
- [Stripe Checkout fulfillment](https://docs.stripe.com/payments/existing-customers?platform=web&ui=stripe-hosted) — confirmed server-side payment events.

**Source review date:** 2026-11-15.
