# 09 — Security Checklist

> Assess confidentiality, integrity, availability, abuse resistance, and operational security proportionate to project risk.

> **Scope: Frontend-specific.** This file is one part of the 09_Security.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Application, API, and supply-chain security

- [ ] **SEC-047** `P1` Review dependencies and browser-delivered scripts for maintenance and supply-chain risk; test Subresource Integrity for applicable fixed external scripts/styles or document an appropriate alternative for dynamic resources.

## Secrets, encryption, and data protection

- [ ] **SEC-051** `P1` Use purpose-limited credential scopes and avoid unnecessary browser access to high-value tokens.
- [ ] **SEC-050** `P1` Confirm client-side bundles and source maps do not expose server secrets or sensitive configuration.

## Security scope and architecture

- [ ] **SEC-041** `P2` Map data flows for third-party scripts, SDKs, tracking tags, and embedded content.

## Frontend Checks

> Apply to browser-based, mobile-web, embedded, or other user-facing interfaces. Record N/A with reasons for headless services.

**Reference basis:** [OWASP Application Security Verification Standard (ASVS) 5.0](https://asvs.owasp.org/); [OWASP ASVS 5.0 control families (web frontend and API)](https://cornucopia.owasp.org/taxonomy/asvs-5.0); [NIST — Generative AI Risk Management Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence).

- [ ] **SEC-072** `P1` Verify contextual output encoding and safe DOM APIs prevent stored, reflected, and DOM-based XSS.
- [ ] **SEC-073** `P1` Review CSP coverage, nonce/hash use where appropriate, third-party script inventory, and unsafe-inline exceptions.
- [ ] **SEC-074** `P1` Ensure tokens and secrets are not embedded in HTML, JavaScript bundles, source maps, or public environment variables.
- [ ] **SEC-075** `P1` Verify Secure, HttpOnly, SameSite, expiry, and path/domain attributes for relevant cookies.
- [ ] **SEC-076** `P0` Check CSRF protection for cookie-authenticated state-changing actions and other applicable request forgery risks.
- [ ] **SEC-077** `P1` Validate safe navigation and redirect allowlists; prevent reverse-tabnabbing on external links.
- [ ] **SEC-078** `P1` Audit local/session storage, IndexedDB, caches, and service workers for sensitive information retention.
- [ ] **SEC-079** `P1` Verify frontend guards do not replace backend authorization; unauthorized API calls are rejected server-side.
- [ ] **SEC-080** `P1` Ensure user-supplied HTML, markdown, rich text, file previews, and URLs are sanitized and safely rendered.
- [ ] **SEC-081** `P1` Inspect third-party scripts, package lockfiles, and externally hosted assets for supply-chain risk.
- [ ] **SEC-082** `P1` Test clickjacking defenses and frame embedding policies appropriate to the application.
- [ ] **SEC-083** `P1` Check logout, account switch, back/forward cache, and browser history cannot display another user's protected information.
- [ ] **SEC-084** `P1` Confirm client errors, analytics beacons, and source maps do not leak access tokens, personal data, or private routes.

- [ ] **SEC-085** `P1` For media uploads or exports that may contain sensitive embedded metadata, inspect actual files for location, device, author, and other identifying EXIF or equivalent fields; minimize or remove such metadata unless needed and disclosed.

## Release gate

> **Common security sign-off:** Apply the [shared Security release gate](../05_Security.md#release-gate) to all relevant Security slices. Record one approval decision, with evidence or justified exceptions for this slice.

**Domain-specific approval rule:** Block release for exploitable critical/high findings without approved mitigation, missing authorization boundaries, exposed secrets, or unprotected sensitive data.

**Optional tools:** See the [separate security tooling catalog](../references/security-testing-tools.md); no third-party agent skill is required to satisfy this checklist.

## Trusted references and scope

The checks above are adapted into practical verification questions from these authoritative publications (not copied as standards text). Verify current versions and the project's scope before sign-off.

- [OWASP API Security Top 10 (2023)](https://api-security.owasp.org/editions/2023/en/0x11-t10/)
- [OWASP Application Security Verification Standard (ASVS) 5.0](https://asvs.owasp.org/)
- [OWASP ASVS 5.0 control families (web frontend and API)](https://cornucopia.owasp.org/taxonomy/asvs-5.0)

Guidance is risk-based and project-specific; sources do not replace testing or specialist review. Accessibility sources belong in the Accessibility domain; generative-AI risk profiles belong in the AI scope.

- [Apple Developer — Photos asset location](https://developer.apple.com/documentation/photos/phasset/location) — capture location as potentially sensitive embedded metadata.

- [MDN Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Subresource_Integrity) — external script and style integrity.

**Source review date:** 2026-11-15.
