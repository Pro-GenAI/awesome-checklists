# 06 — Internationalization and Localization Checklist

> Verify that supported languages, writing systems, locales, and markets have functional and comprehensible end-to-end experiences. Internationalization makes a system adaptable; localization delivers language- and market-appropriate experiences. Translation alone is not sufficient.

> **Scope: Frontend-specific.** This file is one part of the 06_Internationalization_and_Localization.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Internationalized design


- [ ] **I18N-021** `P1` Keep user-facing strings in localization resources instead of hard-coding them into UI layouts or business logic.
- [ ] **I18N-031** `P1` Account for script-specific fonts, glyph coverage, fallback fonts, line height, and text rendering behavior.
- [ ] **I18N-033** `P1` Use responsive layouts and flexible spacing instead of fixed widths based on one language.
- [ ] **I18N-034** `P1` Support right-to-left base direction where required using semantic direction attributes and suitable layout conventions.
- [ ] **I18N-035** `P1` Use logical CSS properties or equivalent layout abstractions for start/end spacing, alignment, and positioning where appropriate.
- [ ] **I18N-037** `P1` Test punctuation, neutral symbols, numbers, placeholders, and inline code in mixed right-to-left/left-to-right text.
- [ ] **I18N-038** `P1` Distinguish icons that should mirror in right-to-left layouts from branding, media controls, numbers, and other icons that should not.
- [ ] **I18N-042** `P1` Test pseudo-localized long strings, accented characters, non-Latin scripts, and right-to-left simulations before linguistic QA.

## Translation and content quality


- [ ] **I18N-051** `P1` Detect missing keys, unapproved source-language fallback, obsolete translations, and untranslated UI elements in builds or tests.
- [ ] **I18N-056** `P1` Verify localized accessibility text, image alternatives, captions, and screen-reader descriptions convey the intended meaning.

## Locale-specific experience


- [ ] **I18N-075** `P1` Check local keyboard input, input methods, composition events, character selection, and paste behavior.
- [ ] **I18N-078** `P1` Make language-switcher options recognizable in their own language and script, not only in the current UI language.
- [ ] **I18N-063** `P1` Verify dates and times display with appropriate locale patterns and an explicit or inferable time zone.
- [ ] **I18N-064** `P1` Test timestamps around daylight-saving transitions, midnight, year boundaries, and other relevant calendar edge cases.
- [ ] **I18N-065** `P1` Use appropriately defined calendar systems and week-start conventions when supported, rather than assuming Gregorian dates and Monday/Sunday defaults.
- [ ] **I18N-066** `P1` Format monetary amounts with the correct ISO currency code or symbol, minor-unit precision, and localized separators.
- [ ] **I18N-067** `P1` Preserve exact monetary amounts and currencies in calculations while varying only localized presentation as appropriate.
- [ ] **I18N-068** `P1` Test decimal and grouping separators, native digits, negative values, percentages, and high-precision numbers.
- [ ] **I18N-069** `P1` Present measurement units and unit conversions that match supported market preferences without changing underlying values unexpectedly.
- [ ] **I18N-070** `P1` Validate address entry and display for local order, variable line counts, postal codes, regions, and optional fields.
- [ ] **I18N-071** `P1` Support culturally appropriate personal names, scripts, spacing, and name-order conventions without requiring first/last name where unnecessary.
- [ ] **I18N-072** `P1` Use suitable international telephone-number handling and do not infer physical residence solely from number prefix.
- [ ] **I18N-073** `P1` Review local payment methods, taxes, invoicing, and refund display with regional business/legal approvers where relevant.
- [ ] **I18N-074** `P1` Confirm sorting, filtering, case-insensitive search, and text matching behave as users of each language expect.
- [ ] **I18N-076** `P1` Verify mixed-script strings and bidirectional identifiers remain readable and do not mislead users about account or transaction details.
- [ ] **I18N-077** `P1` Test localized account creation, authentication, recovery, checkout, and other critical workflows end to end.
- [ ] **I18N-079** `P1` Preserve user's current task or equivalent content when switching language whenever a localized counterpart exists.
- [ ] **I18N-080** `P1` Test supported locales with realistic datasets, local addresses, names, currencies, time zones, and long translations.
- [ ] **I18N-081** `P1` Verify market-specific legal notices, price displays, eligibility restrictions, and support paths using qualified regional review.
- [ ] **I18N-082** `P1` Ensure missing translations and region-specific outages have a documented, understandable fallback experience.

## Frontend Checks


- [ ] **I18N-103** `P1` Set and update document or view language metadata correctly, including language changes within mixed-language content.
- [ ] **I18N-104** `P1` Apply appropriate base text direction for right-to-left pages and semantic direction isolation for user-generated snippets.
- [ ] **I18N-105** `P1` Verify every supported locale loads intended message catalogs, with visible review of missing or fallback strings.
- [ ] **I18N-106** `P1` Test language switching from deep links and authenticated flows without unexpectedly losing state.
- [ ] **I18N-107** `P1` Ensure responsive layouts tolerate long translations, localized number formats, and expanded buttons or navigation labels.
- [ ] **I18N-108** `P1` Check fonts and glyph fallback for every supported script, including combined marks, emoji, and complex shaping.
- [ ] **I18N-109** `P1` Verify text direction and logical spacing across dialogs, forms, tabs, menus, carousels, tables, and notifications.
- [ ] **I18N-110** `P1` Confirm keyboard focus order and visual reading order remain understandable in right-to-left and multilingual layouts.
- [ ] **I18N-111** `P1` Test labels, placeholders, form hints, validation messages, and errors using localized rather than hard-coded strings.
- [ ] **I18N-112** `P1` Render dates, prices, percentages, units, and relative times using approved locale-aware formatting libraries.
- [ ] **I18N-113** `P1` Show timezone or currency context when omission could cause materially wrong user decisions.
- [ ] **I18N-114** `P1` Test text input, IME composition, cursor motion, deletion, selection, and copy/paste in non-Latin scripts.
- [ ] **I18N-115** `P1` Verify sorting and search UI communicate the locale-sensitive behavior actually implemented by the backend.
- [ ] **I18N-116** `P1` Check translated image alternatives, captions, transcripts, and accessible announcements for meaning and completeness.
- [ ] **I18N-117** `P1` Make locale-specific content, downloads, help links, and external disclosures available where advertised.
- [ ] **I18N-118** `P1` Prevent language-specific scripts, fonts, or extra resource bundles from causing major unreviewed performance regressions.
- [ ] **I18N-119** `P1` Verify localized route metadata, canonical/alternate links, and indexing controls for public sites where SEO is relevant.
- [ ] **I18N-120** `P1` Test fallback behavior for unavailable locale bundles or broken translations without leaving critical controls unusable.
- [ ] **I18N-121** `P1` Review localized consent, payment, identity, safety, and error-recovery flows with qualified testers for launch markets.
- [ ] **I18N-122** `P1` Run pseudo-localization and representative manual linguistic checks in supported browsers and devices before release.

## Release gate


- [ ] The release has an approved matrix of supported locales, regions, relevant market-specific requirements, language selection behavior, and fallback rules.
- [ ] Critical user journeys are verified end to end in representative supported languages and scripts, including relevant right-to-left and non-Latin scenarios.
- [ ] Stored data and API contracts preserve Unicode text, timestamp/currency semantics, and required locale metadata without loss or unauthorized cross-locale leakage.
- [ ] Locale formatting, names/addresses, plural forms, sorting, and input methods have passed targeted tests appropriate to the supported market mix.
- [ ] High-impact translations (consent, payment, legal notices, safety instructions, and destructive actions where applicable) have qualified review and no unresolved misleading text.
- [ ] Frontend labels, layout, navigation, accessibility metadata, and fallback behaviors remain usable under translation expansion and missing-resource scenarios.
- [ ] Localization defects are tracked by locale and severity with accountable owners, retest evidence, and approval for any remaining exceptions.

**Domain-specific approval rule:** Block localization sign-off if a supported-market critical journey is unusable, payments/amounts or times are materially misrepresented, data is corrupted, or high-impact language/region requirements are misleading or unreviewed. A language being selectable is not evidence that it is ready for release.

**Optional tooling:** [Frontend test examples](../references/optional-testing-tools-frontend.md#06_internationalization_and_localization), not prerequisites or verification evidence.

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
