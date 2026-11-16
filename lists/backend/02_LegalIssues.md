# 02 — Legal Issues Checklist

> Identify legal, licensing, contractual, privacy, and regulatory questions early. This is an issue-spotting tool, not legal advice or a certification of compliance.

> **Scope: Backend / API-specific.** This file is one part of the 02_LegalIssues.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Intellectual property and licensing

- [ ] **LEG-010** `P1` Copyright/takedown, infringement complaints, and rights-request handling have an assigned process.

## Approvals and ongoing governance

- [ ] **LEG-050** `P1` Verify withdrawal, complaint, breach, and regulator-request workflows are tested and operational.

## API Checks

> Apply to API endpoints, client integrations, webhooks, or data feeds present in the project. Record N/A with reasons if none exist.

**Reference basis:** [EU General Data Protection Regulation (Regulation 2016/679)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679); [UK ICO — What privacy information should we provide?](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/the-right-to-be-informed/what-privacy-information-should-we-provide/); [UK ICO — Cookies and similar technologies (guidance under review)](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/cookies-and-similar-technologies/).

- [ ] **LEG-051** `P2` Inventory external, partner, internal, and third-party APIs and document personal data or regulated information transmitted by each.
- [ ] **LEG-052** `P1` Check API-provider terms, usage restrictions, data ownership, sublicensing, retention, and commercial redistribution rights.
- [ ] **LEG-053** `P2` Identify controller/processor or other applicable roles for data passed through API integrations; obtain required agreements.
- [ ] **LEG-054** `P1` Assess cross-border API data flows and whether safeguards, hosting restrictions, or notices are legally required.
- [ ] **LEG-055** `P1` Verify API retention, access, deletion, portability, and correction capabilities support applicable data-subject rights.
- [ ] **LEG-056** `P1` Check that publicly documented APIs and developer portals publish accurate license, attribution, acceptable-use, and usage-limit terms.
- [ ] **LEG-057** `P1` Confirm data returned to external API consumers is consistent with disclosed purposes and contractual restrictions.
- [ ] **LEG-058** `P1` Validate whether API logging, IP-address handling, tokens, and telemetry are personal data under relevant law.
- [ ] **LEG-059** `P2` Document notification, audit, breach reporting, and subprocessor obligations for API vendors and customers.
- [ ] **LEG-060** `P1` Assess legal and contractual constraints on webhooks, exports, bulk retrieval, and onward sharing of data.
- [ ] **LEG-061** `P1` For AI APIs, document training/retention controls, prohibited use cases, output rights, and service-specific disclosures.

## Release gate

- [ ] All applicable high-priority checks above pass, or an authorized decision-maker has explicitly accepted and documented each residual risk.
- [ ] Failed items have tracked remediation, owners, and deadlines; material blockers remain blocked until resolved.
- [ ] Evidence links and the reviewer, review date, and final decision are recorded.

**Domain-specific approval rule:** Block release for missing mandatory licenses, unlawful personal-data practices, unlicensed critical assets, or unresolved material regulatory obligations. Require qualified legal sign-off when appropriate.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#02_legalissues), not prerequisites or verification evidence.

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
