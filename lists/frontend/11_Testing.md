# 11 — Testing Checklist

> Verify expected functionality, quality, reliability, and release readiness using reproducible evidence.

> **Scope: Frontend-specific.** This file is one part of the 11_Testing.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Requirements and test strategy


- [ ] **TST-003** `P1` A test plan identifies environments, devices, browsers, roles, test data, owners, and exit criteria.

## Functional and end-to-end testing


- [ ] **TST-045** `P1` Deep links, refreshes, browser navigation, and interrupted workflows preserve valid state.
- [ ] **TST-015** `P1` Form validation, empty states, duplicate submissions, timeout states, and helpful errors are tested.

## Experience, accessibility, and compatibility


- [ ] **TST-020** `P1` Supported browsers, operating systems, and input methods have been checked.
- [ ] **TST-021** `P1` Keyboard navigation, focus visibility/order, labels, contrast, and screen-reader paths are tested against the project's accessibility target.
- [ ] **TST-023** `P1` Localization, formats, time zones, Unicode, and right-to-left layouts are tested where applicable.
- [ ] **TST-046** `P1` Accessibility tests cover zoom/reflow, text resizing, error identification, and visible focus.
- [ ] **TST-047** `P1` Screen-reader and keyboard-only smoke tests are performed by a human on critical journeys; automated scans are not the sole evidence.
- [ ] **TST-048** `P1` Touch interactions, tap-target sizes, orientation changes, and reduced-motion preferences are checked where applicable.
- [ ] **TST-019** `P1` Layouts and interactions work on supported mobile, tablet, and desktop viewports.
- [ ] **TST-022** `P1` Loading, success, error, and offline/degraded states are understandable to users.

## Automated and component testing


- [ ] **TST-041** `P1` Component tests exercise loading, state transitions, error boundaries, and event handling.

## Frontend Checks


> Apply to browser-based, mobile-web, embedded, or other user-facing interfaces. Record N/A with reasons for headless services.

**Reference basis:** [OWASP Application Security Verification Standard (ASVS) 5.0](https://asvs.owasp.org/); [W3C — WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/); [web.dev — Core Web Vitals](https://web.dev/articles/vitals).

- [ ] **TST-068** `P1` Verify initial rendering and hydration on representative pages, including direct navigation and refresh.
- [ ] **TST-069** `P1` Test navigation, back/forward history, route guards, and not-found views for valid and invalid URLs.
- [ ] **TST-070** `P1` Check forms for client/server validation agreement, keyboard submission, error summaries, and duplicate-submit protection.
- [ ] **TST-071** `P1` Check loading, success, empty, offline, timeout, and partial-data states with meaningful recovery actions.
- [ ] **TST-072** `P1` Verify keyboard order, visible focus, labels, semantic landmarks, accessible names, and screen-reader announcements.
- [ ] **TST-073** `P1` Test contrast, text resizing, 200% zoom, responsive reflow, touch targets, and reduced-motion behavior against the chosen WCAG target.
- [ ] **TST-074** `P1` Test images, fonts, media, and responsive layout across defined browser/device support.
- [ ] **TST-075** `P1` Inspect console errors, network failures, unhandled promises, and hydration mismatches in representative sessions.
- [ ] **TST-076** `P1` Measure real-user or representative LCP, INP, and CLS against documented performance targets.
- [ ] **TST-077** `P1` Ensure frontend state does not expose other users' records after account switching, back navigation, or cache restoration.
- [ ] **TST-078** `P1` Check long content, translated text, right-to-left layouts, time zones, date/currency formats, and assistive technology where relevant.
- [ ] **TST-079** `P1` Verify user-facing analytics, alerts, and error handling do not disclose personal information or secrets.

- [ ] **TST-080** `P1` Exercise essential mobile/client workflows across Wi-Fi-to-cellular handoffs, loss and restoration of connectivity, captive portals, metered links, and background/foreground transitions; verify retries do not silently duplicate actions or lose unsent changes.
- [ ] **TST-081** `P1` For location-dependent features, test permission denial, revocation, approximate-only access, disabled location services, unavailable fixes, and re-granting access; provide usable fallback states without assuming precise location.
- [ ] **TST-082** `P1` For apps using audio or video capture/playback, test incoming-call and other system interruptions, headphone/Bluetooth route changes, and app backgrounding; verify pause, resume, and user-visible media state remain consistent.
- [ ] **TST-083** `P1` For installable native apps, test a clean installation and upgrades from each supported prior release with persisted data, pending offline operations, and changed permissions; verify migrations and recovery do not silently discard user work.

- [ ] **TST-084** `P1` Where baseline content or critical workflows must work without JavaScript, test with scripting disabled or blocked; otherwise verify an understandable, accessible fallback rather than silently blank or misleading screens.

## Release gate


- [ ] All applicable high-priority checks above pass, or an authorized decision-maker has explicitly accepted and documented each residual risk.
- [ ] Failed items have tracked remediation, owners, and deadlines; material blockers remain blocked until resolved.
- [ ] Evidence links and the reviewer, review date, and final decision are recorded.

**Domain-specific approval rule:** Do not approve when critical flows, data integrity, access-control tests, or required recovery checks fail.

**Optional tooling:** [Frontend test examples](../references/optional-testing-tools-frontend.md#11_testing), not prerequisites or verification evidence.

## Trusted references and scope


The checks above are adapted into practical verification questions from these authoritative publications (not copied as standards text). Verify current versions and the project's scope before sign-off.

- [OWASP Application Security Verification Standard (ASVS) 5.0](https://asvs.owasp.org/)
- [OWASP API Security Top 10 (2023)](https://api-security.owasp.org/editions/2023/en/0x11-t10/)
- [OpenAPI Specification 3.2.1](https://spec.openapis.org/oas/v3.2.1.html)
- [IETF RFC 9457 — Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html)
- [W3C — WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)
- [web.dev — Core Web Vitals](https://web.dev/articles/vitals)

Guidance is risk-based and project-specific; sources do not replace testing or specialist review.

- [Android Developers — Read network state](https://developer.android.com/develop/connectivity/network-ops/reading-network-state) — network handoff, captive portal, and connectivity callbacks.
- [Android Developers — Request location permissions](https://developer.android.com/develop/sensors-and-location/location/permissions) — location permissions and approximate access.
- [Apple Developer — Handling audio interruptions](https://developer.apple.com/documentation/AVFAudio/handling-audio-interruptions) — audio interruption handling.
- [Apple Developer — App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) — app usability and testing before submission.

- [Chrome for Developers — Disable JavaScript](https://developer.chrome.com/docs/devtools/javascript/disable) — evaluate no-script functionality or graceful fallback where applicable.

**Source review date:** 2026-11-13.
