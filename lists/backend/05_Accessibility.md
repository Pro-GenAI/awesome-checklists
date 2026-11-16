# 05 — Accessibility Checklist

> Verify that essential product experiences are perceivable, operable, understandable, and robust for people using a range of input methods and assistive technologies. The intended standard and conformance level must be explicitly defined for each project.

> **Scope: Backend / API-specific.** This file is one part of the 05_Accessibility.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## API Checks

- [ ] **A11Y-076** `P2` Identify API response fields that supply accessible names, descriptions, error messages, language metadata, or media alternatives to user-facing interfaces.
- [ ] **A11Y-077** `P1` Ensure content APIs can provide meaningful alternative text or equivalent descriptions for informative media where the frontend needs them.
- [ ] **A11Y-078** `P1` Supply captions, transcripts, audio-description references, or other media accessibility resources when the product uses them.
- [ ] **A11Y-079** `P1` Provide structured validation errors with stable field references so clients can link corrections to the right controls.
- [ ] **A11Y-080** `P1` Distinguish authentication, authorization, not-found, rate-limit, and service failures so clients can communicate useful recovery instructions.
- [ ] **A11Y-081** `P1` Ensure API-generated messages are understandable, safe to announce, and localized or accompanied by localization keys when required.
- [ ] **A11Y-082** `P1` Provide machine-readable progress, completion, and failure states for asynchronous actions that users must monitor.
- [ ] **A11Y-083** `P1` Expose state, limits, required attributes, and allowable values needed to present dynamic forms or range widgets accessibly.
- [ ] **A11Y-084** `P1` Check that pagination, filtering, and dynamic response updates include enough metadata for accessible result-count and status feedback.
- [ ] **A11Y-085** `P2` Document timeouts, expiry, and renewal behavior so clients can warn users and preserve progress where feasible.
- [ ] **A11Y-086** `P1` Do not rely on color, glyphs, positional information, or undocumented codes as the only explanation in API-provided content.
- [ ] **A11Y-087** `P1` Review accessibility implications of API schema and content changes with client owners before rollout.
- [ ] **A11Y-088** `P1` Verify API-fed lists, tables, headings, and document metadata can be represented with appropriate semantic relationships.
- [ ] **A11Y-089** `P1` Provide stable content identifiers and ordering information needed for meaningful keyboard focus and updates when applicable.
- [ ] **A11Y-090** `P1` Keep accessibility-related fields and examples in the API documentation and contract tests where those fields are part of the public interface.

## Release gate

- [ ] The evaluation scope, target standard/version/level, supported environments, and accountable reviewer are recorded.
- [ ] Critical end-to-end workflows have been evaluated with keyboard access and appropriate assistive technologies, not only an automated scan.
- [ ] Required accessible names, semantic structure, focus management, alternatives to non-text content, and form error recovery have been verified where relevant.
- [ ] API-fed content and frontend components preserve accessibility information and handle asynchronous changes and errors accessibly where applicable.
- [ ] No unresolved accessibility issue blocks an essential task or applicable mandatory criterion without explicit review and an authorized, documented remediation decision.
- [ ] Findings, evaluation limits, responsible owners, retest outcomes, and final decision are documented in project-specific records.

**Domain-specific approval rule:** Do not claim WCAG conformance or legal compliance without an appropriately scoped assessment against all applicable criteria. Block release approval for unresolved barriers that prevent essential user tasks, or for unaccepted mandatory conformance failures; escalate jurisdiction-specific exceptions to qualified approvers.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#05_accessibility), not prerequisites or verification evidence.

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
