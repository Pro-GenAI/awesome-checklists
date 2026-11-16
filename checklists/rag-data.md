# RAG & Data Pipelines — drop-in review checklist

Copy these unchecked items into a project PR description or issue. Each item maps to a stable ID in the canonical library. Mark as complete **only after** recording project-specific evidence; a checkbox is not certification.

- [ ] **RAG-023** — Select chunking using document structure and retrieval evidence. [Canonical check](../lists/AI/10_RAG_and_Knowledge_Bases.md). *Why:* Avoids slicing away relevant facts or merging unrelated passages.
- [ ] **RAG-033** — Verify query and document embedding settings are compatible. [Canonical check](../lists/AI/10_RAG_and_Knowledge_Bases.md). *Why:* Prevents invalid similarity scoring after model or index changes.
- [ ] **RAG-040** — Test index swaps without mixing incompatible embeddings. [Canonical check](../lists/AI/10_RAG_and_Knowledge_Bases.md). *Why:* Prevents partial migrations from serving inconsistent results.
- [ ] **RAG-046** — Maintain held-out query-to-passage relevance judgments. [Canonical check](../lists/AI/10_RAG_and_Knowledge_Bases.md). *Why:* Makes precision and recall regressions observable.
- [ ] **RAG-043** — Verify removed sources disappear from vectors and caches on time. [Canonical check](../lists/AI/10_RAG_and_Knowledge_Bases.md). *Why:* Prevents deleted or access-revoked material from resurfacing.

**Review record:** Target revision: `UNKNOWN` · Checklist source revision: `UNKNOWN` · Reviewer/approver: `UNKNOWN` · Evidence/exception links: `UNKNOWN`.

See [catalog.json](catalog.json) for machine-readable stage, contextual priority hint, severity and proposed integration signals. These are **not** pre-run checks or universal release gates.
