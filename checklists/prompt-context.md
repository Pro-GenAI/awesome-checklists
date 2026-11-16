# Prompt & Context Engineering — drop-in review checklist

Copy these unchecked items into a project PR description or issue. Each item maps to a stable ID in the canonical library. Mark as complete **only after** recording project-specific evidence; a checkbox is not certification.

- [ ] **PROMPT-006** — Separate trusted instructions from user and retrieved material. [Canonical check](../lists/AI/09_Prompt_Engineering_and_Versioning.md). *Why:* Stops external content from being promoted into privileged instructions.
- [ ] **PROMPT-039** — Validate structured model output and tool arguments with strict schemas. [Canonical check](../lists/AI/09_Prompt_Engineering_and_Versioning.md). *Why:* Prevents malformed or attacker-controlled fields from crossing execution boundaries.
- [ ] **PROMPT-031** — Budget system prompts, history, retrieval and output tokens. [Canonical check](../lists/AI/09_Prompt_Engineering_and_Versioning.md). *Why:* Avoids hidden context overflow and unbounded per-request cost.
- [ ] **PROMPT-032** — Test truncation and overflow against critical instructions and evidence. [Canonical check](../lists/AI/09_Prompt_Engineering_and_Versioning.md). *Why:* Detects silent loss of the policies or facts a response needs.
- [ ] **PROMPT-040** — Exercise direct and indirect prompt injection in authorized tests. [Canonical check](../lists/AI/09_Prompt_Engineering_and_Versioning.md). *Why:* Detects unexpected instruction following through tool or document content.

**Review record:** Target revision: `UNKNOWN` · Checklist source revision: `UNKNOWN` · Reviewer/approver: `UNKNOWN` · Evidence/exception links: `UNKNOWN`.

See [catalog.json](catalog.json) for machine-readable stage, contextual priority hint, severity and proposed integration signals. These are **not** pre-run checks or universal release gates.
