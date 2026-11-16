# 04 — UI, UX, and Usability Checklist

> Review whether the product helps people complete meaningful tasks with understandable navigation, predictable interactions, inclusive experiences, and evidence-based improvements. This focuses on product usability; complete the dedicated Accessibility, Testing, Security, and Performance checklists separately.

> **Scope: Frontend-specific.** This file is one part of the 04_UI_UX_and_Usability.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Information architecture and navigation


- [ ] **UX-018** `P2` Define a clear hierarchy for primary navigation, secondary navigation, page titles, and related content.
- [ ] **UX-021** `P1` Prefer plain, descriptive navigation labels over ambiguous icons or internal jargon.
- [ ] **UX-022** `P2` Identify the current location or step within the journey using visible headings, active navigation, or progress indicators as appropriate.
- [ ] **UX-025** `P1` Use breadcrumbs, local navigation, tabs, or search only where they genuinely aid findability for the content structure.
- [ ] **UX-026** `P1` Assess whether navigation depth and menu choices are manageable for the expected audience and tasks.
- [ ] **UX-031** `P1` Confirm navigation remains usable on small screens and with keyboard or assistive technology.
- [ ] **UX-032** `P0` Check that destructive, privileged, or irreversible actions are not confused with routine navigation.

- [ ] **UX-017** `P1` Organize features and content around user tasks and terminology instead of internal team or system structure.
- [ ] **UX-019** `P1` Make key destinations discoverable from likely entry points without requiring users to memorize a route.
- [ ] **UX-020** `P1` Use consistent labels for the same concept across menus, links, page titles, buttons, and help content.
- [ ] **UX-023** `P1` Give users an obvious way to return to a safe previous location or cancel a nonfinal action.
- [ ] **UX-024** `P1` Ensure the information hierarchy supports direct deep links, search-result entry, and page refresh where applicable.
- [ ] **UX-027** `P1` Use card sorting, tree testing, or equivalent task-based research when key categories or menu structures are uncertain.
- [ ] **UX-028** `P1` Check that search results, filtering, sorting, and category labels match user expectations for retrieval tasks.
- [ ] **UX-029** `P1` Provide meaningful empty results, alternative search suggestions, or recovery paths when content cannot be found.
- [ ] **UX-030** `P2` Define consistent behavior for internal links, external links, downloadable documents, and opening new contexts.

## Interaction and visual design


- [ ] **UX-037** `P1` Use buttons for actions and links for navigation consistently in the interface.
- [ ] **UX-048** `P1` Ensure color, motion, icons, and visual hierarchy do not carry essential meaning without alternative cues.
- [ ] **UX-049** `P1` Provide readable content with sensible line lengths, headings, spacing, and sufficient visual priority for important information.
- [ ] **UX-051** `P1` Review dialogs, notifications, and overlays for interruption cost, dismissal, focus, and recovery behavior.

- [ ] **UX-033** `P1` Use a consistent design language for spacing, typography, color, icons, feedback, and component behavior.
- [ ] **UX-034** `P1` Choose established interaction patterns when they satisfy user needs; document and test deviations from conventions.
- [ ] **UX-035** `P1` Make each page or step communicate its purpose, expected action, and what happens next.
- [ ] **UX-036** `P1` Make primary and secondary actions visually and verbally distinguishable without hiding necessary alternatives.
- [ ] **UX-038** `P1` Keep terminology grounded in users' language; explain uncommon concepts where they are essential.
- [ ] **UX-039** `P1` Provide visible, timely feedback for submitting, saving, processing, completing, and failing actions.
- [ ] **UX-040** `P1` Distinguish background work, slow responses, and completed actions so users do not mistakenly repeat operations.
- [ ] **UX-041** `P2` Show loading, empty, offline, unavailable, and error states that explain the condition and next step.
- [ ] **UX-042** `P1` Prevent errors through clear constraints, defaults, examples, and appropriately timed confirmation for harmful actions.
- [ ] **UX-043** `P1` Allow users to correct mistakes without re-entering unrelated information wherever practical.
- [ ] **UX-044** `P1` Use undo, edit, cancel, or confirmation patterns proportionate to the impact and reversibility of an action.
- [ ] **UX-045** `P1` Make forms ask only for necessary information and explain required fields, formats, and consequences.
- [ ] **UX-046** `P1` Keep labels and instructions visible when a field has a value; do not rely on placeholders as the only labels.
- [ ] **UX-047** `P1` Use actionable, specific error messages near the affected controls and a clear summary when appropriate to the flow.
- [ ] **UX-050** `P1` Test text expansion, zoom, localization, and varying content lengths for overflow or clipped actions.
- [ ] **UX-052** `P1` Avoid manipulative patterns, misleading urgency, preselected choices, or hiding important costs and consequences.

## Usability feedback and iteration


- [ ] **UX-062** `P1` Prioritize issues by user impact, task criticality, observed frequency, and remediation effort rather than visual preference alone.

- [ ] **UX-053** `P1` Create a usability study plan tied to specific research questions, user groups, and priority tasks.
- [ ] **UX-054** `P1` Use representative participants and realistic task scenarios rather than relying only on internal stakeholders.
- [ ] **UX-055** `P1` Observe participants attempting tasks without directing them through the intended interface.
- [ ] **UX-056** `P2` Record task completion, critical mistakes, points of hesitation, workarounds, and qualitative feedback.
- [ ] **UX-057** `P2` Define any quantitative usability metrics in advance, including how completion and abandonment are counted.
- [ ] **UX-058** `P1` Include appropriate assistive technology, accessibility, mobile, and low-confidence-user scenarios for the audience.
- [ ] **UX-059** `P1` Test prototypes or early implementations before expensive irreversible design decisions.
- [ ] **UX-060** `P1` Distinguish user statements from observed behavior and avoid overgeneralizing small exploratory samples.
- [ ] **UX-061** `P1` Capture each usability problem with reproduction context, affected journey, frequency or severity, and recommended follow-up.
- [ ] **UX-063** `P2` Assign owners and dates for fixing high-impact usability defects and for retesting changes.
- [ ] **UX-064** `P1` Verify revised designs address observed problems with new users or suitable follow-up evidence.
- [ ] **UX-065** `P2` Maintain feedback channels for live users and route recurring issues into product improvement work.
- [ ] **UX-066** `P1` Review funnels, abandonment, error/support trends, and user satisfaction together rather than using one proxy as proof of usability.
- [ ] **UX-067** `P2` Record what the team learned, which design decisions changed, and which assumptions remain untested.
- [ ] **UX-068** `P1` Establish a regular cadence for evaluating important journeys after major product, policy, or audience changes.

## User research and journeys


- [ ] **UX-001** `P2` Define the product's primary user groups, their goals, contexts, constraints, and most important tasks using documented evidence rather than assumptions.
- [ ] **UX-002** `P2` Describe primary and secondary personas or audience segments only where supported by user research, and distinguish assumptions from findings.
- [ ] **UX-003** `P1` Review support tickets, feedback, analytics, existing studies, or field observations to identify recurring user problems and unmet needs.
- [ ] **UX-004** `P1` Include new, returning, infrequent, and experienced users when identifying target journeys.
- [ ] **UX-005** `P2` Consider users with disabilities, assistive technologies, low bandwidth, shared devices, or limited digital confidence in research plans.
- [ ] **UX-006** `P2` Document end-to-end journeys, including preparation, entry points, off-platform steps, handoffs, and follow-up tasks.
- [ ] **UX-007** `P2` Identify top user tasks and their expected outcomes; prioritize them by user value, frequency, and risk.
- [ ] **UX-008** `P2` Map the current and proposed journey for critical tasks, including moments of confusion, waiting, abandonment, and rework.
- [ ] **UX-009** `P1` Review how users discover the service and understand what it does before signing in or submitting information.
- [ ] **UX-010** `P1` Validate critical workflow assumptions through interviews, contextual inquiry, prototypes, or task-based usability sessions.
- [ ] **UX-011** `P2` Define observable success criteria for each priority journey, including task completion and serious errors.
- [ ] **UX-012** `P2` Record accessibility, privacy, trust, and safety concerns surfaced during research, assigning them to responsible review domains.
- [ ] **UX-013** `P1` Ensure research prompts and tasks describe realistic goals without leading participants toward an intended answer.
- [ ] **UX-014** `P1` Gather feedback on alternative paths and exceptional circumstances rather than only the ideal happy path.
- [ ] **UX-015** `P1` Check that the experience makes sense when users pause, leave, resume, or return after an extended interval.
- [ ] **UX-016** `P2` Assign ownership and a review cadence to research findings, open questions, and unresolved journey problems.

## Frontend Checks


- [ ] **UX-083** `P1` Verify the main task is identifiable and its primary call to action is easy to locate on each key screen.
- [ ] **UX-084** `P1` Confirm responsive layouts work across supported devices, viewport sizes, orientation changes, and varying zoom settings.
- [ ] **UX-085** `P1` Check headings, landmarks, navigation, and grouping communicate the interface's structure without relying on visual styling alone.
- [ ] **UX-086** `P1` Verify labels, instructions, and help text remain visible and meaningful when inputs are populated.
- [ ] **UX-087** `P1` Check keyboard navigation, focus movement, and focus restoration across menus, dialogs, route transitions, and error states.
- [ ] **UX-088** `P1` Provide accessible names and appropriate text alternatives for meaningful controls, icons, images, and status feedback.
- [ ] **UX-089** `P1` Ensure error messages identify the affected field or action and provide a workable correction or recovery step.
- [ ] **UX-090** `P1` Check that client and server validation disagree neither silently nor through contradictory user messages.
- [ ] **UX-091** `P1` Verify field values and meaningful task progress are preserved after recoverable errors, page refreshes, or temporary connectivity losses where feasible.
- [ ] **UX-092** `P1` Display actual save/submission state and protect users from unintended repeat actions.
- [ ] **UX-093** `P1` Test back/forward navigation, deep linking, refresh, and session expiration for predictable journey continuity.
- [ ] **UX-094** `P1` Check touch target suitability, pointer alternatives, and interaction patterns on devices with touch or precise pointers.
- [ ] **UX-095** `P1` Honor reduced-motion preferences where motion is nonessential and avoid surprise animation or autoplay behavior.
- [ ] **UX-096** `P1` Check text enlargement, translations, right-to-left display, and long user-generated content for clipping and broken layouts where applicable.
- [ ] **UX-097** `P1` Keep overlays, banners, tooltips, and toast notifications from obscuring essential tasks or trapping focus.
- [ ] **UX-098** `P1` Measure user-perceived delay across key screens and show useful progress or skeleton states rather than misleading indefinite spinners.
- [ ] **UX-099** `P1` Confirm filtering, sorting, pagination, and search results communicate active controls and an understandable result count or empty state.
- [ ] **UX-100** `P1` Ensure privacy notices, pricing, confirmations, destructive-action warnings, and required disclosures are legible at the decision point.
- [ ] **UX-101** `P1` Verify assistive-technology announcements for asynchronous results, validation changes, and critical status updates with appropriate manual testing.
- [ ] **UX-102** `P1` Check representative browsers/devices for broken assets, console/runtime errors, horizontal scrolling, and inconsistent interaction states.

- [ ] **UX-103** `P1` For pages whose content users need to print or save as PDF, inspect the print preview on representative pages to ensure essential content remains readable, interactive-only controls are omitted appropriately, and important information is not clipped.

## Release gate


- [ ] Priority user journeys, target user groups, and expected outcomes are documented and have been reviewed with appropriate stakeholders.
- [ ] Representative usability evidence supports that users can complete critical tasks, including handling common errors and recovery paths.
- [ ] No unresolved, unaccepted usability issue blocks essential tasks, causes material confusion, or risks significant unintended consequences.
- [ ] Core navigation, forms, system feedback, and critical mobile/responsive experiences have been reviewed against agreed design and user needs.
- [ ] API and frontend user-experience dependencies are understood, with owners and documented treatment of failures, latency, and partial results where applicable.
- [ ] Responsible reviewers have recorded the decision and accepted risks in project-specific records.

**Domain-specific approval rule:** Block UX sign-off for unresolved critical-task failures, deceptive or materially misleading interface behavior, inaccessible core journeys awaiting required specialist review, or unknown user-impact risks lacking an accountable owner. UX approval does not substitute for accessibility conformance or production verification.

**Optional tooling:** [Frontend test examples](../references/optional-testing-tools-frontend.md#04_ui_ux_and_usability), not prerequisites or verification evidence.

## Trusted references and scope


The checklist adapts the following authoritative user-experience, design, and accessibility guidance into observable project review questions. General design heuristics are not universal hard requirements; evaluate their suitability for the actual audience and context.

- [Nielsen Norman Group — 10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/) — feedback, consistency, user control, error prevention, recognition, and recovery.
- [GOV.UK Service Standard — Understand users and their needs](https://www.gov.uk/service-manual/service-standard/point-1-understand-user-needs) — evidence-driven problem framing.
- [GOV.UK Service Standard — Make the service simple to use](https://www.gov.uk/service-manual/service-standard/point-4-make-the-service-simple-to-use) — intuitive tasks and end-to-end usability.
- [GOV.UK Service Manual — Plan user research for your service](https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service) — inclusive research questions, participants, and iteration.
- [GOV.UK Service Manual — Using moderated usability testing](https://www.gov.uk/service-manual/user-research/using-moderated-usability-testing) — representative tasks and observational findings.
- [Nielsen Norman Group — Tree Testing: Evaluate Menu Labels and Categories](https://www.nngroup.com/articles/tree-testing/) — information architecture and findability testing.
- [U.S. Web Design System — Components](https://designsystem.digital.gov/components/) — established visual and interaction patterns.
- [GOV.UK Design System — Recover from validation errors](https://design-system.service.gov.uk/patterns/validation/) — clear messages, field recovery, and preservation of input.
- [W3C WAI — Form Instructions](https://www.w3.org/WAI/tutorials/forms/instructions/) — labels and accessible instructions.
- [W3C WAI — Validating Input](https://www.w3.org/WAI/tutorials/forms/validation/) — error guidance and accessible validation.
- [W3C — Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) — relevant accessibility success criteria, with detailed conformance review in `05_Accessibility.md`.

**Applicability:** Some practices are service-, platform-, or audience-specific. Do not treat GOV.UK's design-system implementation decisions as mandatory for unrelated products. Human usability evaluation is essential where risks or complexity warrant it; quantitative usability metrics require a suitable sample and method.

- [MDN — Printing (CSS)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Printing) — printed page styling and print-preview testing.

**Source review date:** 2026-11-13.
