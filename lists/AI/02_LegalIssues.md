# 02 — Legal Issues Checklist

> Identify legal, licensing, contractual, privacy, and regulatory questions early. This is an issue-spotting tool, not legal advice or a certification of compliance.

> **Scope: AI-specific.** This file is one part of the 02_LegalIssues.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Intellectual property and licensing

- [ ] **LEG-039** `P1` Review whether data aggregation, crawling, or embedding is permitted by original sources' rights and contractual terms.

## AI, content, and specialized risks (if applicable)

- [ ] **LEG-026** `P1` AI/data-provider terms permit the intended inputs, outputs, retention, training settings, and commercial use.
- [ ] **LEG-027** `P1` AI-generated or user-generated content has rules for ownership, moderation, disclosure, and complaints where needed.
- [ ] **LEG-028** `P1` High-impact or regulated AI uses are screened for applicable risk assessment, transparency, oversight, and testing duties.
- [ ] **LEG-047** `P2` Document AI provider roles, data retention, use for model training, and conditions for international transfers.

## Release gate

- [ ] All applicable high-priority checks above pass, or an authorized decision-maker has explicitly accepted and documented each residual risk.
- [ ] Failed items have tracked remediation, owners, and deadlines; material blockers remain blocked until resolved.
- [ ] Evidence links and the reviewer, review date, and final decision are recorded.

**Domain-specific approval rule:** Block release for missing mandatory licenses, unlawful personal-data practices, unlicensed critical assets, or unresolved material regulatory obligations. Require qualified legal sign-off when appropriate.

**Optional tooling:** [AI-scope testing examples](../references/optional-testing-tools-ai.md#02_legalissues), not prerequisites or evidence of PASS.

## Trusted references and scope

**2026 source update:** See the [AI source-currency watch](../references/ai-source-watch.md) for verified NIST/OWASP 2026 editions and the amended EU AI Act timeline. Use current official publications for applicability; source lists do not certify compliance.



The checks above are adapted into practical verification questions from these authoritative publications (not copied as standards text). Verify current versions and the project's scope before sign-off.

- [EU General Data Protection Regulation (Regulation 2016/679)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679)
- [UK ICO — What privacy information should we provide?](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/the-right-to-be-informed/what-privacy-information-should-we-provide/)
- [UK ICO — Cookies and similar technologies (guidance under review)](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/cookies-and-similar-technologies/)
- [European Data Protection Board — ePrivacy technical scope guidelines](https://www.edpb.europa.eu/documents/guideline/guidelines-22023-on-technical-scope-of-art-53-of-eprivacy-directive_en)
- [W3C — WCAG 2.2 Overview](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [NIST — Generative AI Risk Management Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)

These examples are issue-spotting checks. EU and UK sources do not automatically govern other markets; determine actual applicability and seek local legal counsel. Cookie and consumer-protection obligations can vary and guidance changes.

**Source review date:** 2026-11-12; primary AI framework timing checked 2026-11-15.
