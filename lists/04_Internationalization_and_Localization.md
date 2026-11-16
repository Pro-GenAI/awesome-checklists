# 04 — Internationalization and Localization Checklist

> Verify that supported languages, writing systems, locales, and markets have functional and comprehensible end-to-end experiences. Internationalization makes a system adaptable; localization delivers language- and market-appropriate experiences. Translation alone is not sufficient.

> **Scope: Shared / cross-cutting.** This file is one part of the 04_Internationalization_and_Localization.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](references/review-method.md) · [Optional framework crosswalk](references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Language and regional requirements


- [ ] **I18N-001** `P2` List supported languages, scripts, regions, locales, and launch markets with a named owner for each supported experience.
- [ ] **I18N-002** `P2` Define language support independently from country, region, currency, and legal-market eligibility.
- [ ] **I18N-003** `P1` Use interoperable BCP 47 language tags for interfaces and content, including script or region subtags only where needed.
- [ ] **I18N-004** `P2` Document the default locale and explicit fallback chain for unsupported or incomplete translations.
- [ ] **I18N-006** `P1` Allow users to override automatically selected language without unnecessarily changing their account, location, or region.
- [ ] **I18N-007** `P1` Persist explicit language choices across sessions and devices where appropriate and authorized.
- [ ] **I18N-008** `P2` Describe how localized URLs, deep links, language-switching links, and redirects preserve the user's intended content.
- [ ] **I18N-009** `P2` Define availability when a feature, help resource, or legal document is not supported in the selected language.
- [ ] **I18N-010** `P2` Document which currencies, calendars, numbering systems, measurement systems, and time zones each product supports.
- [ ] **I18N-011** `P2` Identify markets requiring different pricing, taxes, payment methods, address fields, disclosures, or customer-support processes.
- [ ] **I18N-012** `P2` Specify the localization policy for customer-entered content, including whether it must remain in its original language.
- [ ] **I18N-013** `P2` Define behavior for mixed-language records and content containing multiple scripts.
- [ ] **I18N-014** `P1` Distinguish translation, transliteration, locale formatting, and cultural adaptation in requirements and review ownership.
- [ ] **I18N-015** `P2` Identify audiences with low literacy, multilingual needs, or assistive-technology requirements during market research.
- [ ] **I18N-016** `P2` Define the expected consistency of localization across web, mobile, transactional emails, documents, and support channels.
- [ ] **I18N-017** `P2` Document whether regional or language changes affect data storage, legal terms, service availability, or account eligibility.
- [ ] **I18N-018** `P1` Decide which data should be stored in locale-neutral form, such as timestamps, money amounts with currency, and identifiers.
- [ ] **I18N-019** `P2` Track rollout readiness for each supported locale separately rather than inferring readiness from the source language.
- [ ] **I18N-020** `P1` Reassess supported locale requirements after expanding to new markets, changing regional regulations, or adding major workflows.

## Internationalized design


- [ ] **I18N-022** `P1` Use stable, descriptive message keys and provide context for translators where wording could be ambiguous.
- [ ] **I18N-023** `P1` Avoid constructing sentences by concatenating independently translated fragments with fixed grammatical order.
- [ ] **I18N-024** `P1` Support variable placement, gender-sensitive wording, and cardinal/ordinal plural categories through an appropriate message formatting system.
- [ ] **I18N-025** `P1` Use locale-aware number, currency, unit, relative time, and date formatting rather than manually assembling locale-specific strings.
- [ ] **I18N-026** `P1` Separate stored values from presentation formatting to prevent localized display strings becoming authoritative application data.
- [ ] **I18N-027** `P1` Use Unicode-compatible encoding end to end, and declare UTF-8 or the appropriate Unicode encoding at system boundaries.
- [ ] **I18N-028** `P1` Preserve combining characters, emoji sequences, and scripts during input, validation, truncation, storage, and display.
- [ ] **I18N-029** `P1` Use Unicode-aware grapheme segmentation when limits or editing behavior are intended to reflect user-perceived characters.
- [ ] **I18N-030** `P1` Apply language-appropriate case folding, comparison, collation, and search rather than assuming ASCII rules work for every language.
- [ ] **I18N-032** `P1` Allow labels, buttons, fields, tables, and notifications to expand or wrap for translations of different lengths.
- [ ] **I18N-036** `P1` Isolate user-generated, numeric, Latin-script, or otherwise mixed-direction strings to prevent bidirectional text spillover.
- [ ] **I18N-039** `P1` Design forms for local names, address structures, phone numbers, postal codes, and different writing systems instead of enforcing one national format.
- [ ] **I18N-040** `P1` Ensure error messages, validation rules, and help text can be translated without weakening meaning or user safety.
- [ ] **I18N-041** `P1` Provide appropriate reading order, language metadata, and semantic structure for assistive technologies in multilingual views.

## Translation and content quality


- [ ] **I18N-043** `P1` Establish a localization workflow with designated source-content owners, translators, reviewers, and release responsibilities.
- [ ] **I18N-044** `P1` Create a maintained terminology glossary for product concepts, technical terms, feature names, and prohibited translations.
- [ ] **I18N-045** `P1` Provide translators with screenshots, message descriptions, placeholders, target audience, and surrounding interaction context.
- [ ] **I18N-046** `P2` Maintain consistent tone, product terminology, and reading level across localized pages and user flows.
- [ ] **I18N-047** `P2` Specify which strings must remain untranslated, such as technical identifiers, trademarks, code tokens, and certain legal names.
- [ ] **I18N-048** `P1` Review culturally sensitive examples, imagery, symbols, humor, gestures, and assumptions for each target audience.
- [ ] **I18N-049** `P1` Apply qualified human review to high-impact safety, medical, financial, legal, or contractual content where required.
- [ ] **I18N-050** `P1` Verify placeholders, markup, variables, and message-format syntax survive translation without changing their semantics.
- [ ] **I18N-052** `P1` Version translation catalogs with the related product release and preserve traceability to source changes.
- [ ] **I18N-053** `P2` Define whether machine translation may be used and what post-editing, confidentiality, and quality review it requires.
- [ ] **I18N-054** `P1` Review translated calls to action, form guidance, error handling, confirmations, and destructive-action warnings within complete user journeys.
- [ ] **I18N-055** `P1` Check localized help articles, onboarding emails, notification templates, transactional messages, and PDF/download content for consistency.
- [ ] **I18N-057** `P1` Check locale-specific links, contact information, customer-support channels, and references to services actually offered in that market.
- [ ] **I18N-058** `P1` Use native speakers or qualified reviewers for representative linguistic QA, including comprehension and idiomatic usage.
- [ ] **I18N-059** `P1` Test contextual ambiguity, grammatical agreement, pluralization, and short/long forms with representative real data.
- [ ] **I18N-060** `P2` Define the process and priority for correcting harmful, misleading, or culturally inappropriate translations.
- [ ] **I18N-061** `P2` Track translation completeness and unresolved quality issues by locale, feature, severity, and owner.
- [ ] **I18N-062** `P1` Recheck affected translations when terminology, design, pricing, legal content, or source strings change.

## Release gate


- [ ] The release has an approved matrix of supported locales, regions, relevant market-specific requirements, language selection behavior, and fallback rules.
- [ ] Critical user journeys are verified end to end in representative supported languages and scripts, including relevant right-to-left and non-Latin scenarios.
- [ ] Stored data and API contracts preserve Unicode text, timestamp/currency semantics, and required locale metadata without loss or unauthorized cross-locale leakage.
- [ ] Locale formatting, names/addresses, plural forms, sorting, and input methods have passed targeted tests appropriate to the supported market mix.
- [ ] High-impact translations (consent, payment, legal notices, safety instructions, and destructive actions where applicable) have qualified review and no unresolved misleading text.
- [ ] Frontend labels, layout, navigation, accessibility metadata, and fallback behaviors remain usable under translation expansion and missing-resource scenarios.
- [ ] Localization defects are tracked by locale and severity with accountable owners, retest evidence, and approval for any remaining exceptions.

**Domain-specific approval rule:** Block localization sign-off if a supported-market critical journey is unusable, payments/amounts or times are materially misrepresented, data is corrupted, or high-impact language/region requirements are misleading or unreviewed. A language being selectable is not evidence that it is ready for release.

**Optional tooling:** [File-specific tool examples](references/optional-testing-tools-shared.md#04_internationalization_and_localization), not prerequisites or verification evidence.

## Trusted references and scope


The following authoritative standards and guidance support these project-level review questions. Some are normative technical specifications; others are practical guidance and must not be treated as universal legal requirements.

- [W3C Internationalization — Quick Tips for the Web](https://www.w3.org/International/quicktips/) — language, encoding, translated strings, forms, navigation, and direction.
- [Unicode CLDR — Core specification (UTS #35)](https://www.unicode.org/reports/tr35/) — locale data, inheritance, locale identifiers, and language-aware operations.
- [Unicode CLDR — Numbers and currency formatting](https://www.unicode.org/reports/tr35/tr35-numbers.html) — locale-specific numbering, decimals, plural categories, and currency.
- [Unicode CLDR — Dates, time, and time zones](https://www.unicode.org/reports/tr35/tr35-dates.html) — locale-specific date and time formats and calendar behavior.
- [Unicode — Text Segmentation (UAX #29)](https://www.unicode.org/reports/tr29/) — grapheme clusters, words, and user-perceived character boundaries.
- [W3C Internationalization — How to use Unicode controls for bidi text](https://www.w3.org/International/questions/qa-bidi-unicode-controls) — directional isolation of mixed-script and user-supplied text.
- [IETF — RFC 5646: Tags for Identifying Languages](https://www.rfc-editor.org/rfc/rfc5646) — BCP 47 language and script/region subtags.
- [IETF — RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — HTTP content negotiation and Accept-Language where used.
- [ECMAScript — ECMA-402 Internationalization API](https://tc39.es/ecma402/) — JavaScript locale-sensitive formatting and locale matching.
- [MDN — Intl](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl) — practical runtime locale/date/number/collation APIs.
- [W3C WAI — Language of Page](https://www.w3.org/WAI/WCAG22/Understanding/language-of-page.html) — document language declaration and accessibility implications.
- [Google Search Central — Localized versions of your site](https://developers.google.com/search/docs/specialty/international/localized-versions) — locale-specific URL and alternate language annotations for indexed websites.

**Applicability:** Locale data and display conventions evolve. Unicode CLDR 49 was current at the November 2026 review, but applications must validate the library/runtime versions they actually ship. BCP 47 language tags do not encode all legal, currency, market, or user-preference requirements. RTL support, public search annotations, alternative calendars, and multi-language translation workflows are conditional on the product's supported audience and interfaces. Detailed WCAG conformance, SEO, and jurisdictional requirements belong in their dedicated checklists.

**Source review date:** 2026-11-12.
