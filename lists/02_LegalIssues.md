# 02 — Legal Issues Checklist

> Identify legal, licensing, contractual, privacy, and regulatory questions early. This is an issue-spotting tool, not legal advice or a certification of compliance.

> **Scope: Shared / cross-cutting.** This file is one part of the 02_LegalIssues.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](references/review-method.md) · [Optional framework crosswalk](references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Scope, ownership, and jurisdiction

- [ ] **LEG-001** `P1` The legal entity, product owner, operating countries, target audiences, and distribution channels are identified.
- [ ] **LEG-002** `P1` Applicable laws, regulators, age restrictions, and industry-specific obligations are mapped with qualified counsel where needed.
- [ ] **LEG-003** `P1` Responsibilities for legal approvals, recordkeeping, and periodic re-review are assigned.
- [ ] **LEG-004** `P1` Material legal assumptions, unresolved questions, and launch-blocking risks are documented.
- [ ] **LEG-035** `P2` Identify which entity is controller, processor, service provider, publisher, or platform for each data flow, as applicable.
- [ ] **LEG-036** `P2` Maintain a jurisdiction-specific compliance register with the responsible reviewer and review trigger.
- [ ] **LEG-037** `P1` Assess whether access for minors, accessibility obligations, or industry regulation changes the launch path.

## Intellectual property and licensing

- [ ] **LEG-005** `P1` Ownership or permission exists for source code, designs, branding, text, images, video, audio, and datasets.
- [ ] **LEG-006** `P1` Employee, contractor, and contributor agreements address IP ownership and confidentiality where needed.
- [ ] **LEG-007** `P1` Third-party and open-source licenses are inventoried, reviewed for compatibility, and notices/attributions are included.
- [ ] **LEG-008** `P1` Before adopting a product or app name, document a market-appropriate clearance search for confusingly similar registered, pending, and relevant unregistered marks and trade names, alongside domain/branding rights; escalate material conflicts for qualified review.
- [ ] **LEG-009** `P1` Restrictions on datasets, scraping, APIs, and model outputs are checked against contracts and applicable law.
- [ ] **LEG-038** `P1` Verify SDK, API, database, font, icon, and frontend package licenses including distribution and notice obligations.
- [ ] **LEG-073** `P1` For services hosting user-posted material that seek U.S. DMCA Section 512 safe-harbor protection, verify eligibility, a current Copyright Office designated-agent registration and public contact information, and appropriate notice/takedown and repeat-infringer procedures with qualified counsel.

## Privacy, personal data, and consent

- [ ] **LEG-011** `P1` Personal data categories, purposes, sources, recipients, storage locations, and retention periods are documented.
- [ ] **LEG-012** `P1` A lawful basis or other applicable justification is identified for each processing purpose.
- [ ] **LEG-013** `P1` Privacy notices accurately explain processing, sharing, user rights, contact channels, and material changes.
- [ ] **LEG-014** `P1` Cookie, tracking, analytics, advertising, and marketing-consent mechanisms meet applicable rules.
- [ ] **LEG-015** `P1` Data subject or consumer rights requests can be received, authenticated, fulfilled, and logged within required periods.
- [ ] **LEG-016** `P1` Processors and service providers have appropriate data-processing agreements and contractual controls where required.
- [ ] **LEG-017** `P1` International transfers, local hosting requirements, and cross-border safeguards are reviewed where applicable.
- [ ] **LEG-018** `P1` Data minimization, retention, deletion, and breach reporting obligations are assessed and operationalized.
- [ ] **LEG-019** `P1` Handling of children's or other sensitive personal data is approved under the applicable rules.
- [ ] **LEG-040** `P2` Map client-side identifiers, local storage, analytics pixels, server logs, API request bodies, third-party transfers, and passive browser requests to external font/CDN hosts or embeds that disclose IP addresses or other data; assess applicable notice and legal basis.
- [ ] **LEG-041** `P1` Assess whether a data protection impact assessment or equivalent risk review is required for high-risk processing.
- [ ] **LEG-042** `P1` Test that deletion and correction requests propagate to downstream processors and caches, subject to justified exceptions.

## User-facing terms and commercial obligations

- [ ] **LEG-020** `P1` Terms of service, acceptable-use rules, and any required disclaimers are accurate, accessible, and versioned.
- [ ] **LEG-021** `P1` Pricing, subscriptions, renewals, trials, taxes, refunds, cancellations, and required disclosures are legally reviewed.
- [ ] **LEG-022** `P1` Marketing claims, testimonials, comparisons, endorsements, and performance statements are supported and not misleading.
- [ ] **LEG-023** `P1` Consumer protection, accessibility, anti-spam, and platform-specific rules are reviewed for the intended markets.
- [ ] **LEG-024** `P1` Customer and vendor contracts cover liability, service levels, support, termination, confidentiality, and audit rights as appropriate.
- [ ] **LEG-025** `P1` Required policies and contact details are published and reachable at launch.
- [ ] **LEG-044** `P1` Confirm price, availability, and performance claims originate from current, approved data.
- [ ] **LEG-045** `P1` Verify that accessible versions of required contractual and privacy documents can be reached before consent or purchase.
- [ ] **LEG-074** `P1` For commercial marketing email in applicable markets, verify accurate sender and subject information, any required business postal address, a working opt-out mechanism, timely suppression across sending vendors, and distinct handling of transactional messages.

## AI, content, and specialized risks (if applicable)

- [ ] **LEG-029** `P1` Any regulated activity (for example health, finance, employment, education, or payments) receives specialist legal/compliance review.
- [ ] **LEG-030** `P1` Accessibility or consumer-facing statements do not promise compliance beyond what has been verified.
- [ ] **LEG-046** `P1` Evaluate automated decision-making and profiling transparency or review rights under relevant local law.
- [ ] **LEG-048** `P1` Require review of any claim implying government, regulator, or professional endorsement.

## Approvals and ongoing governance

- [ ] **LEG-031** `P1` Required licenses, registrations, filings, permits, and notices are in place before operating.
- [ ] **LEG-032** `P1` Regulatory, litigation, complaint, and contract escalation contacts are documented.
- [ ] **LEG-033** `P1` Legal review is completed for material product, data-flow, geographic, and vendor changes.
- [ ] **LEG-034** `P1` Open legal issues have owners, counsel input where appropriate, and approved remediation plans.
- [ ] **LEG-049** `P2` Record accountable legal owners for new APIs, vendors, cookies, marketing channels, countries, and AI features.

## Release gate

- [ ] All applicable high-priority checks above pass, or an authorized decision-maker has explicitly accepted and documented each residual risk.
- [ ] Failed items have tracked remediation, owners, and deadlines; material blockers remain blocked until resolved.
- [ ] Evidence links and the reviewer, review date, and final decision are recorded.

**Domain-specific approval rule:** Block release for missing mandatory licenses, unlawful personal-data practices, unlicensed critical assets, or unresolved material regulatory obligations. Require qualified legal sign-off when appropriate.

**Optional tooling:** [File-specific tool examples](references/optional-testing-tools-shared.md#02_legalissues), not prerequisites or verification evidence.

## Trusted references and scope

- [USPTO — Comprehensive clearance search](https://www.uspto.gov/trademarks/search/comprehensive-clearance-search-similar-trademarks) — relevant naming search scope.
- [U.S. Copyright Office — DMCA agent directory](https://www.copyright.gov/dmca-directory/) — conditional service-provider designation.
- [FTC — CAN-SPAM compliance guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business) — commercial email disclosures and opt-out.

The checks above are adapted into practical verification questions from these authoritative publications (not copied as standards text). Verify current versions and the project's scope before sign-off.

- [EU General Data Protection Regulation (Regulation 2016/679)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679)
- [UK ICO — What privacy information should we provide?](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/the-right-to-be-informed/what-privacy-information-should-we-provide/)
- [UK ICO — Cookies and similar technologies (guidance under review)](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/cookies-and-similar-technologies/)
- [European Data Protection Board — ePrivacy technical scope guidelines](https://www.edpb.europa.eu/documents/guideline/guidelines-22023-on-technical-scope-of-art-53-of-eprivacy-directive_en)
- [W3C — WCAG 2.2 Overview](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [NIST — Generative AI Risk Management Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)

These examples are issue-spotting checks. EU and UK sources do not automatically govern other markets; determine actual applicability and seek local legal counsel. Cookie and consumer-protection obligations can vary and guidance changes.

**Source review date:** 2026-11-13.
