# 05 — Accessibility Checklist

> Verify that essential product experiences are perceivable, operable, understandable, and robust for people using a range of input methods and assistive technologies. The intended standard and conformance level must be explicitly defined for each project.

> **Scope: Frontend-specific.** This file is one part of the 05_Accessibility.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Accessibility goals and target standard


- [ ] **A11Y-006** `P2` Identify supported browsers, operating systems, input devices, screen readers, zoom settings, and other assistive-technology combinations to evaluate.
- [ ] **A11Y-007** `P1` Include users with visual, auditory, motor, cognitive, speech, and multiple disabilities when planning representative research.

- [ ] **A11Y-001** `P2` Define the accessibility scope by product, platform, version, region, and critical user journey, including authenticated and error states.
- [ ] **A11Y-002** `P2` Identify the applicable accessibility standards, legal/contractual obligations, and target conformance level with qualified reviewers when needed.
- [ ] **A11Y-003** `P1` Adopt a documented baseline (for example WCAG 2.2 Level AA for applicable web content), including its Level A requirements.
- [ ] **A11Y-004** `P2` Map accessibility requirements to user stories, design acceptance criteria, and relevant WCAG success criteria where applicable.
- [ ] **A11Y-005** `P2` Assign accessibility ownership across product, design, content, engineering, QA, and third-party integrations.
- [ ] **A11Y-008** `P2` Inventory critical templates, components, documents, interactive widgets, media, and external services that need evaluation.
- [ ] **A11Y-009** `P2` Specify whether mobile apps, PDFs, kiosks, embedded content, and third-party experiences require a different evaluation standard or method.
- [ ] **A11Y-010** `P2` Define pass/fail rules and severity for barriers that prevent completion of important tasks, independently of cosmetic defects.
- [ ] **A11Y-011** `P2` Record known accessibility constraints, third-party dependencies, exceptions, accountable owners, and planned remediation in project-specific records.
- [ ] **A11Y-012** `P1` Include accessibility acceptance criteria in design and engineering reviews before implementation rather than only at release.
- [ ] **A11Y-013** `P1` Set requirements for accessible procurement and vendor-delivered components, documents, and services where applicable.
- [ ] **A11Y-014** `P1` Ensure any public accessibility statement or conformance claim is supported by an actual scoped assessment rather than a tool score.
- [ ] **A11Y-015** `P1` Plan a repeatable evaluation approach for changing flows, with a representative sample and an issue-resolution process.
- [ ] **A11Y-016** `P1` Establish an accessible way for users to report barriers and a responsible path to triage and respond.

## Semantic structure and keyboard use


- [ ] **A11Y-017** `P1` Use native HTML elements for buttons, links, forms, tables, and headings wherever their semantics match the function.
- [ ] **A11Y-019** `P1` Use a logical heading hierarchy and recognizable navigation, main-content, search, and other landmarks as relevant.
- [ ] **A11Y-021** `P1` Preserve meaningful reading order when CSS layouts, responsive rearrangement, or client rendering changes visual position.
- [ ] **A11Y-022** `P1` Ensure all functionality is available through a keyboard interface without requiring pointer-only gestures.
- [ ] **A11Y-024** `P1` Provide a visible keyboard focus indicator and check that fixed headers, dialogs, or overlays do not obscure it.
- [ ] **A11Y-025** `P1` Provide a mechanism to bypass repeated blocks such as global navigation where required.
- [ ] **A11Y-026** `P1` Ensure keyboard focus can move into and out of dialogs, menus, popovers, and composite widgets without traps.
- [ ] **A11Y-027** `P1` Implement keyboard behavior for custom widgets consistent with the relevant WAI-ARIA Authoring Practices pattern.
- [ ] **A11Y-029** `P1` Do not add redundant or contradictory ARIA attributes to native controls; use ARIA only when necessary and valid.
- [ ] **A11Y-034** `P1` Ensure focus order, route changes, and error-state transitions remain understandable when content is added dynamically.
- [ ] **A11Y-035** `P1` Make keyboard shortcuts discoverable and avoid interfering with native browser or assistive-technology shortcuts.
- [ ] **A11Y-036** `P1` Test that hidden, disabled, and offscreen controls are exposed or removed from focus and accessibility trees appropriately.

- [ ] **A11Y-018** `P1` Ensure page and view titles describe the purpose or topic of the current content.
- [ ] **A11Y-020** `P1` Ensure information and relationships expressed visually remain available as text or programmatic semantics.
- [ ] **A11Y-023** `P1` Verify tab order follows the intended interaction and does not produce confusing jumps or inaccessible controls.
- [ ] **A11Y-028** `P1` Expose accessible names, roles, values, expanded/selected/checked states, and state changes for interactive components.
- [ ] **A11Y-030** `P1` Use descriptive link and button labels whose purpose is clear in context, including image-only controls.
- [ ] **A11Y-031** `P1` Do not make essential instructions depend only on position, shape, color, orientation, or sound.
- [ ] **A11Y-032** `P1` Provide accessible alternatives to dragging gestures and avoid requiring complex multipoint gestures where not essential.
- [ ] **A11Y-033** `P1` Verify pointer target dimensions or adequate spacing meet the chosen WCAG target, with documented exceptions where allowed.

## Perceivable and understandable content


- [ ] **A11Y-041** `P1` Provide audio description or another permitted accessible alternative for important visual information in video as required.
- [ ] **A11Y-043** `P1` Ensure media-player controls, captions, volume, pause, and transcript access work with keyboard and assistive technology.
- [ ] **A11Y-044** `P1` Use sufficient text and non-text contrast under the chosen WCAG criteria and avoid conveying meaning through color alone.
- [ ] **A11Y-045** `P1` Allow text to resize and layout to reflow without loss of content or functionality within the applicable WCAG constraints.
- [ ] **A11Y-051** `P2` Identify input errors in text and communicate correction guidance that does not rely on color or visual position alone.
- [ ] **A11Y-053** `P1` Make navigation and component behavior consistent across related screens and predictable after input or focus changes.
- [ ] **A11Y-059** `P1` Ensure status messages and confirmations communicate important outcomes without depending solely on a fleeting visual notification.

- [ ] **A11Y-037** `P1` Provide concise alternative text for informative images that conveys their purpose or essential information.
- [ ] **A11Y-038** `P1` Mark purely decorative images appropriately so they do not create redundant assistive-technology announcements.
- [ ] **A11Y-039** `P1` Ensure charts, diagrams, and complex images have a textual explanation or alternative presenting equivalent essential information.
- [ ] **A11Y-040** `P1` Provide accurate captions for prerecorded video with meaningful audio, and live captions when required by the applicable level.
- [ ] **A11Y-042** `P1` Provide transcripts or other accessible alternatives for audio-only and other media where the chosen criteria require them.
- [ ] **A11Y-046** `P1` Support changes in text spacing without clipped labels, hidden actions, or lost relationships.
- [ ] **A11Y-047** `P1` Ensure content remains usable when users prefer portrait or landscape orientation unless a specific orientation is essential.
- [ ] **A11Y-048** `P1` Avoid uncontrolled audio, flashing, moving content, and animations that create safety risks or prevent concentration.
- [ ] **A11Y-049** `P1` Allow users to pause, stop, hide, or control auto-updating/moving content when required.
- [ ] **A11Y-050** `P1` Make visible labels, instructions, and required-field status understandable before users submit data.
- [ ] **A11Y-052** `P1` Preserve entered data and provide review, correction, or reversal mechanisms for high-impact submissions where the applicable criteria require them.
- [ ] **A11Y-054** `P1` Provide understandable page language and programmatic language changes for localized or multilingual content.
- [ ] **A11Y-055** `P1` Ensure instructional content and help are accessible without relying exclusively on images, hover, or inaccessible documents.
- [ ] **A11Y-056** `P1` Support accessible authentication without forcing a cognitive-function test when alternatives are required by WCAG 2.2.
- [ ] **A11Y-057** `P1` Keep persistent or repeated help mechanisms in a consistent order across relevant pages where required.
- [ ] **A11Y-058** `P1` Give users sufficient time to complete tasks and allow extension or adjustment of timed sessions when required.

## Assistive-technology evaluation


- [ ] **A11Y-062** `P1` Manually complete critical user journeys using keyboard-only navigation, including errors and recovery.
- [ ] **A11Y-063** `P1` Evaluate critical journeys with screen readers and supported browser/operating-system combinations.
- [ ] **A11Y-065** `P1` Test zoom, text resizing, text-spacing overrides, and narrow viewport reflow without loss of meaningful content.
- [ ] **A11Y-066** `P1` Check display contrast and focus indication using appropriate techniques and not only automated color sampling.

- [ ] **A11Y-060** `P2` Define a representative evaluation sample that includes complete processes, shared templates, key states, and higher-risk custom controls.
- [ ] **A11Y-061** `P1` Conduct automated accessibility scans across representative pages and components, recording tool versions and known limitations.
- [ ] **A11Y-064** `P1` Inspect the accessibility tree for accessible names, roles, state, descriptions, and hidden content of representative controls.
- [ ] **A11Y-067** `P0` Test forms for programmatic labels, descriptions, required fields, error association, and recovery after failed submission.
- [ ] **A11Y-068** `P1` Test dialogs, popovers, notifications, dynamic lists, route changes, and live regions with manual assistive-technology checks.
- [ ] **A11Y-069** `P1` Evaluate captions, transcripts, audio descriptions, and media-player controls when media is present.
- [ ] **A11Y-070** `P1` Include user evaluation with people with disabilities when feasible, particularly for critical or complex tasks.
- [ ] **A11Y-071** `P1` Inspect third-party widgets and embedded content in the complete user journey rather than assuming vendor conformance.
- [ ] **A11Y-072** `P1` Report each finding with applicable criterion, affected context, reproduction steps, user impact, and responsible owner in project-specific records.
- [ ] **A11Y-073** `P1` Retest remediated issues with the input methods and assistive technologies that originally exposed them.
- [ ] **A11Y-074** `P1` Review the representative sample and criteria after new components, workflows, content types, or platforms are introduced.
- [ ] **A11Y-075** `P2` Document assessment scope, methodology, limitations, evaluator, date, and conformance conclusion without claiming universal coverage.

## Frontend Checks


- [ ] **A11Y-091** `P1` Use semantic HTML and native controls by default, introducing ARIA only where native semantics do not meet the interface requirement.
- [ ] **A11Y-092** `P1` Provide appropriate document titles, visible headings, landmarks, skip links, and a meaningful DOM reading order.
- [ ] **A11Y-093** `P1` Verify every control has a useful accessible name and custom controls expose correct role, state, value, and relationships.
- [ ] **A11Y-094** `P0` Ensure keyboard-only users can operate all essential functions without focus traps or undiscoverable commands.
- [ ] **A11Y-095** `P1` Check logical focus movement and restoration after route transitions, modal dialogs, menus, errors, and removed content.
- [ ] **A11Y-096** `P1` Make keyboard focus visible and not obscured; verify focus styles across themes, overlays, and sticky elements.
- [ ] **A11Y-097** `P1` Verify meaningful alternative text for images; hide decorative images from assistive-technology output appropriately.
- [ ] **A11Y-098** `P1` Verify form labels, autocomplete purposes where applicable, instructions, required states, and error associations.
- [ ] **A11Y-099** `P1` Present error summaries and targeted corrections in text, including updates that screen readers can perceive.
- [ ] **A11Y-100** `P2` Announce asynchronous status changes through appropriate live regions or other accessible notification patterns without over-announcing.
- [ ] **A11Y-101** `P1` Provide keyboard-operable dialogs, tabs, menus, comboboxes, carousels, and sliders using appropriate interaction patterns.
- [ ] **A11Y-102** `P1` Check text and graphical contrast, text resize, text spacing, and reflow at the applicable WCAG thresholds.
- [ ] **A11Y-103** `P1` Ensure pointer targets, drag interactions, gestures, and hover/focus revealed content have accessible alternatives where required.
- [ ] **A11Y-104** `P1` Respect reduced-motion preferences and provide control over moving, flashing, auto-playing, or auto-updating content as appropriate.
- [ ] **A11Y-105** `P1` Check responsive behavior, orientation, zoom, touch, and voice-control interaction on the supported devices.
- [ ] **A11Y-106** `P1` Ensure critical help, authentication, checkout, and session timeout flows do not introduce avoidable cognitive barriers.
- [ ] **A11Y-107** `P1` Confirm language attributes, localization, directionality, and text expansion remain correct after dynamic rendering.
- [ ] **A11Y-108** `P1` Verify accessible data tables expose headers, captions where appropriate, and relationships rather than only visual grid formatting.
- [ ] **A11Y-109** `P1` Ensure video/audio playback controls, captions, transcripts, and descriptions are available and operable when relevant.
- [ ] **A11Y-110** `P1` Test screen-reader and keyboard interactions with client-side routing, hydration, form validation, and dynamic content updates.
- [ ] **A11Y-111** `P1` Prevent hidden or inactive content from remaining in the focus order, and do not hide active controls from accessibility APIs.
- [ ] **A11Y-112** `P1` Run automated plus manual regression checks for shared components and priority user flows before release.

## Release gate


- [ ] The evaluation scope, target standard/version/level, supported environments, and accountable reviewer are recorded.
- [ ] Critical end-to-end workflows have been evaluated with keyboard access and appropriate assistive technologies, not only an automated scan.
- [ ] Required accessible names, semantic structure, focus management, alternatives to non-text content, and form error recovery have been verified where relevant.
- [ ] API-fed content and frontend components preserve accessibility information and handle asynchronous changes and errors accessibly where applicable.
- [ ] No unresolved accessibility issue blocks an essential task or applicable mandatory criterion without explicit review and an authorized, documented remediation decision.
- [ ] Findings, evaluation limits, responsible owners, retest outcomes, and final decision are documented in project-specific records.

**Domain-specific approval rule:** Do not claim WCAG conformance or legal compliance without an appropriately scoped assessment against all applicable criteria. Block release approval for unresolved barriers that prevent essential user tasks, or for unaccepted mandatory conformance failures; escalate jurisdiction-specific exceptions to qualified approvers.

**Optional tooling:** [Frontend test examples](../references/optional-testing-tools-frontend.md#05_accessibility), not prerequisites or verification evidence.

## Trusted references and scope


These checks translate authoritative W3C materials into review questions; they are not a substitute for the full standard, its normative conformance rules, or professional evaluation.

- [W3C — Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) — normative success criteria and conformance requirements.
- [W3C WAI — What's New in WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/) — new focus, dragging, target-size, authentication, and help criteria.
- [W3C WAI — WCAG Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/) — technology-independent success criteria and supporting techniques.
- [W3C — WCAG Evaluation Methodology (WCAG-EM) 2.0](https://www.w3.org/TR/WCAG-EM/) — defining evaluation scope, sampling, assessment, and reporting; guidance, not additional WCAG requirements.
- [W3C WAI — ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) — accessible custom widgets, naming, states, and keyboard patterns.
- [W3C WAI — Accessible Names and Descriptions](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/) — appropriate control names and descriptions, with preference for native elements.
- [W3C WAI — Forms: Validating Input](https://www.w3.org/WAI/tutorials/forms/validation/) — accessible error messages, correction, and input validation.
- [W3C WAI — Images Tutorial](https://www.w3.org/WAI/tutorials/images/) — informative, functional, and decorative image alternatives.
- [W3C WAI — Planning Accessible Audio and Video Media](https://www.w3.org/WAI/media/av/planning/) — captions, transcripts, audio descriptions, and media controls.

**Applicability:** Web, native mobile, documents, kiosks, and embedded products can require distinct standards or evaluation methods. WCAG 2.2 Level AA is a suggested web baseline, not a declaration of universal legal applicability. WCAG-EM 2.0 was published in July 2026 and describes an evaluation process; it does not add normative success criteria.

**Source review date:** 2026-11-12.
