# 04 — Security Checklist

> Assess confidentiality, integrity, availability, abuse resistance, and operational security proportionate to project risk.

> **Scope: AI-specific.** This file is one part of the 04_Security.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## AI and agent systems (if applicable)

- [ ] **SEC-036** `P1` Untrusted prompts, retrieved documents, and tool outputs are treated as data, not instructions.
- [ ] **SEC-037** `P1` Agents have least-privilege tool access, scoped credentials, and approval for sensitive actions.
- [ ] **SEC-038** `P0` Prompt-injection, output handling, data exfiltration, and unsafe tool invocation are tested.
- [ ] **SEC-039** `P1` Model/provider retention settings and sensitive-data exposure have been reviewed.
- [ ] **SEC-056** `P1` Separate untrusted model content from privileged agent/tool instructions and constrain outputs before executable use.
- [ ] **SEC-057** `P1` Audit sensitive agent actions and require meaningful user authorization for irreversible operations.

## Release gate

> **Common security sign-off:** Apply the [shared Security release gate](../05_Security.md#release-gate) to all relevant Security slices. Record one approval decision, with evidence or justified exceptions for this slice.

**Domain-specific approval rule:** Block release for exploitable critical/high findings without approved mitigation, missing authorization boundaries, exposed secrets, or unprotected sensitive data.

**Optional tools:** See the [separate security tooling catalog](../references/security-testing-tools.md); no third-party agent skill is required to satisfy this checklist.

## Trusted references and scope

The checks above are adapted into practical verification questions from these authoritative publications (not copied as standards text). Verify current versions and the project's scope before sign-off.

- [OWASP API Security Top 10 (2023)](https://api-security.owasp.org/editions/2023/en/0x11-t10/)
- [OWASP Application Security Verification Standard (ASVS) 5.0](https://asvs.owasp.org/)
- [OWASP ASVS 5.0 control families (web frontend and API)](https://cornucopia.owasp.org/taxonomy/asvs-5.0)
- [OWASP GenAI LLM Top 10 (2026)](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) — current LLM-specific threats and mitigations for injection, unsafe output, sensitive disclosure, and tool misuse.
- [NIST — Generative AI Risk Management Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)

Guidance is risk-based and project-specific; sources do not replace testing or specialist review. Accessibility sources belong in the Accessibility domain; generative-AI risk profiles belong in the AI scope.

**Source review date:** 2026-11-15.
