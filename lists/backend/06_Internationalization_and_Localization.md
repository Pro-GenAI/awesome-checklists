# 06 — Internationalization and Localization Checklist

> Verify that supported languages, writing systems, locales, and markets have functional and comprehensible end-to-end experiences. Internationalization makes a system adaptable; localization delivers language- and market-appropriate experiences. Translation alone is not sufficient.

> **Scope: Backend / API-specific.** This file is one part of the 06_Internationalization_and_Localization.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Language and regional requirements

- [ ] **I18N-005** `P2` Define how initial language and locale are selected from user preferences, account settings, device settings, and request headers.

## API Checks

- [ ] **I18N-083** `P1` Accept and return Unicode text without loss or corruption across request, validation, database, and response boundaries.
- [ ] **I18N-084** `P2` Document the language and locale conventions for API inputs, outputs, errors, and localized display fields.
- [ ] **I18N-085** `P1` Use valid, consistently interpreted language tags in locale preferences and applicable resource metadata.
- [ ] **I18N-086** `P2` Define locale negotiation, fallback, and explicit override behavior where APIs provide localized messages or content.
- [ ] **I18N-087** `P1` Keep machine-readable errors and business identifiers stable across languages while supplying localized human-readable messages where relevant.
- [ ] **I18N-088** `P1` Preserve numeric precision, currency identity, units, and canonical timestamps independently of locale-specific display strings.
- [ ] **I18N-089** `P2` Specify timezone and offset semantics for all externally exchanged timestamps and date-only values.
- [ ] **I18N-090** `P1` Test ambiguous local times, daylight-saving changes, calendar boundaries, and date-only scheduling semantics as applicable.
- [ ] **I18N-091** `P1` Handle localized search, collation, comparison, and sorting consistently with documented backend behavior.
- [ ] **I18N-092** `P1` Validate names, addresses, phone numbers, and other user-entered fields without imposing inappropriate single-country ASCII patterns.
- [ ] **I18N-093** `P2` Define storage and transport size limits independently of UI character counts, considering UTF-8 byte length and grapheme clusters.
- [ ] **I18N-094** `P1` Ensure pagination and cursor ordering remain stable when locale-sensitive sorting or collation changes.
- [ ] **I18N-095** `P1` Test that API outputs and JSON serialization preserve combining marks, non-Latin characters, emoji, and mixed-script data.
- [ ] **I18N-096** `P1` Provide localized resource variants or content language metadata for content-oriented APIs where supported.
- [ ] **I18N-097** `P1` Guard against cache cross-contamination by locale, language, region, or entitlement when localized responses are cached.
- [ ] **I18N-098** `P1` Validate webhooks, exports, documents, and asynchronous jobs for multilingual payload consistency.
- [ ] **I18N-099** `P1` Include locale-relevant tests for input validation errors, rate-limit messages, and failure recovery.
- [ ] **I18N-100** `P2` Document and version changes to locale negotiation, formatting contracts, and localized enum display labels.
- [ ] **I18N-101** `P1` Ensure API telemetry can diagnose locale-specific defects without collecting unnecessary sensitive language or identity data.
- [ ] **I18N-102** `P1` Coordinate with clients on language fallback, localized content missing states, and supported regional operations.

## Release gate

- [ ] The release has an approved matrix of supported locales, regions, relevant market-specific requirements, language selection behavior, and fallback rules.
- [ ] Critical user journeys are verified end to end in representative supported languages and scripts, including relevant right-to-left and non-Latin scenarios.
- [ ] Stored data and API contracts preserve Unicode text, timestamp/currency semantics, and required locale metadata without loss or unauthorized cross-locale leakage.
- [ ] Locale formatting, names/addresses, plural forms, sorting, and input methods have passed targeted tests appropriate to the supported market mix.
- [ ] High-impact translations (consent, payment, legal notices, safety instructions, and destructive actions where applicable) have qualified review and no unresolved misleading text.
- [ ] Frontend labels, layout, navigation, accessibility metadata, and fallback behaviors remain usable under translation expansion and missing-resource scenarios.
- [ ] Localization defects are tracked by locale and severity with accountable owners, retest evidence, and approval for any remaining exceptions.

**Domain-specific approval rule:** Block localization sign-off if a supported-market critical journey is unusable, payments/amounts or times are materially misrepresented, data is corrupted, or high-impact language/region requirements are misleading or unreviewed. A language being selectable is not evidence that it is ready for release.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#06_internationalization_and_localization), not prerequisites or verification evidence.

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
