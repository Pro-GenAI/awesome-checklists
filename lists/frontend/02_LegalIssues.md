# 02 — Legal Issues Checklist

> Identify legal, licensing, contractual, privacy, and regulatory questions early. This is an issue-spotting tool, not legal advice or a certification of compliance.

> **Scope: Frontend-specific.** This file is one part of the 02_LegalIssues.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## User-facing terms and commercial obligations

- [ ] **LEG-043** `P1` Check material subscription/renewal terms, taxes, eligibility, and refund rules against the actual user interface and transaction records.

## Frontend Checks

> Apply to browser-based, mobile-web, embedded, or other user-facing interfaces. Record N/A with reasons for headless services.

**Reference basis:** [UK ICO — What privacy information should we provide?](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/the-right-to-be-informed/what-privacy-information-should-we-provide/); [UK ICO — Cookies and similar technologies (guidance under review)](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/cookies-and-similar-technologies/); [W3C — WCAG 2.2 Overview](https://www.w3.org/WAI/standards-guidelines/wcag/).

- [ ] **LEG-062** `P1` Verify privacy notices, terms, commercial disclosures, and legal contact details are visible, accessible, and current.
- [ ] **LEG-063** `P1` Confirm nonessential tracking/storage is gated by valid consent where required, and consent withdrawal actually changes frontend behavior.
- [ ] **LEG-064** `P1` Test the UI's consent preferences, rejection, accessibility, and audit record against applicable local rules.
- [ ] **LEG-065** `P1` Ensure legal terms, key pricing conditions, auto-renewal disclosures, and cancellation options are presented at the appropriate transaction stage.
- [ ] **LEG-066** `P1` Review forms, checkboxes, preselected options, misleading urgency, and cancellation friction for prohibited deceptive design patterns.
- [ ] **LEG-067** `P1` Check that user-request portals for access, correction, deletion, export, and withdrawal are findable and functional where required.
- [ ] **LEG-068** `P1` Evaluate frontend accessibility against the applicable legal framework and adopted WCAG benchmark; record remaining barriers.
- [ ] **LEG-069** `P1` Confirm required age or parental-consent flows are implemented and do not rely on unsupported age assertions.
- [ ] **LEG-070** `P1` Review displayed endorsements, testimonials, ratings, and AI disclosures for source support and local advertising rules.
- [ ] **LEG-071** `P1` Verify account recovery, deletion, and settings pages communicate important legal consequences accurately.
- [ ] **LEG-072** `P1` Ensure marketing preferences and unsubscribe controls reach the responsible backend systems and vendors.

## Release gate

- [ ] All applicable high-priority checks above pass, or an authorized decision-maker has explicitly accepted and documented each residual risk.
- [ ] Failed items have tracked remediation, owners, and deadlines; material blockers remain blocked until resolved.
- [ ] Evidence links and the reviewer, review date, and final decision are recorded.

**Domain-specific approval rule:** Block release for missing mandatory licenses, unlawful personal-data practices, unlicensed critical assets, or unresolved material regulatory obligations. Require qualified legal sign-off when appropriate.

**Optional tooling:** [Frontend test examples](../references/optional-testing-tools-frontend.md#02_legalissues), not prerequisites or verification evidence.

## Trusted references and scope

The checks above are adapted into practical verification questions from these authoritative publications (not copied as standards text). Verify current versions and the project's scope before sign-off.

- [EU General Data Protection Regulation (Regulation 2016/679)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679)
- [UK ICO — What privacy information should we provide?](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/the-right-to-be-informed/what-privacy-information-should-we-provide/)
- [UK ICO — Cookies and similar technologies (guidance under review)](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/cookies-and-similar-technologies/)
- [European Data Protection Board — ePrivacy technical scope guidelines](https://www.edpb.europa.eu/documents/guideline/guidelines-22023-on-technical-scope-of-art-53-of-eprivacy-directive_en)
- [W3C — WCAG 2.2 Overview](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [NIST — Generative AI Risk Management Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)

These examples are issue-spotting checks. EU and UK sources do not automatically govern other markets; determine actual applicability and seek local legal counsel. Cookie and consumer-protection obligations can vary and guidance changes.

**Source review date:** 2026-11-12.
