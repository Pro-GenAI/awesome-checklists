# Drop-in GenAI and agentic review templates

<!-- SPDX-License-Identifier: CC0-1.0 -->
These **five small task lists** make the existing [canonical review library](../../lists/AI/) convenient inside project pull requests and issues. Unlike the 4,215-ID source library, they are short entry points. Copy only applicable checks; record evidence and the target-project commit; keep **all checks unchecked by default**.

| Engineering phase | Copy into a PR/issue | Typical failure addressed |
| --- | --- | --- |
| Prompt & Context Engineering | [prompt-context.md](prompt-context.md) | Stops external content from being promoted into privileged instructions. |
| RAG & Data Pipelines | [rag-data.md](rag-data.md) | Avoids slicing away relevant facts or merging unrelated passages. |
| Agent Safety & Runtime Guardrails | [agent-safety.md](agent-safety.md) | Prevents agent output from inventing executable capabilities. |
| Evaluation & Observability | [evaluation-observability.md](evaluation-observability.md) | Prevents silent test-dataset drift across prompt and model releases. |
| Production Readiness | [production-readiness.md](production-readiness.md) | Catches failures hidden by warm developer machines or import-time side effects. |

The [JSON catalog](catalog.json) mirrors every checkbox by stable ID and concise action text and adds `severity`, `stage`, `priority_hint` and `automated_check`. All `severity` values require **project-specific judgment**. A populated `automated_check` is a suggested signal to wire into the *adopting project's* CI, not a command implemented here. Empty or missing evidence is **UNKNOWN**, not PASS.

Run `python3 scripts/validate_lifecycle_catalog.py` at repository root to check Markdown/JSON parity and resolve every ID to the canonical source. For exhaustive selection or JSON review export use the existing [scoped review generator](../../lists/references/scoped-review-generator.md) and [export tool](../../skills/awesome-checklists/scripts/export_checklists.py), not these shortlists.

**Reuse:** Copy Markdown to `.github/PULL_REQUEST_TEMPLATE.md`, an issue description, or an internal release review. Preserve the stable ID, the version of this source and links to actual tests. These templates are general guidance, not security, legal, or deployment sign-off.
