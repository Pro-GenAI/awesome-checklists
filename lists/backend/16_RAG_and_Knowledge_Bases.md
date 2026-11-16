# 16 — RAG and Knowledge Bases Checklist

> Verify that retrieval-augmented generation (RAG) uses authorized, attributable, sufficiently fresh evidence; retrieves relevant passages; and produces answers whose factual claims can be checked against the source. Search relevance, answer quality, and access controls are separate requirements: improving one does not establish the others.

> **Scope: Backend / API-specific.** This file is one part of the 16_RAG_and_Knowledge_Bases.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## API Checks

- [ ] **RAG-089** `P1` Enforce identity, role, tenant, and document permissions on every retrieval request before exposing text or embeddings.
- [ ] **RAG-090** `P1` Validate query text, metadata filters, collection IDs, source selectors, and requested result limits against server-side rules.
- [ ] **RAG-091** `P1` Prevent arbitrary caller-supplied index names, filters, or paths from bypassing allowed corpus boundaries.
- [ ] **RAG-092** `P1` Check vector, keyword, hybrid, and multi-query retrieval modes for equivalent authorization guarantees.
- [ ] **RAG-093** `P1` Ensure model generation never receives passages the current caller is not authorized to read.
- [ ] **RAG-094** `P1` Version and record embedding, indexing, ranking, query-rewrite, and generation configurations for each release.
- [ ] **RAG-095** `P1` Return stable source identifiers and passage-level citation metadata without disclosing protected source locations.
- [ ] **RAG-096** `P2` Document contract behavior for zero results, low relevance, unavailable sources, and conflicting evidence.
- [ ] **RAG-097** `P1` Provide structured answer confidence or groundedness indicators only when calibrated and meaningful.
- [ ] **RAG-098** `P1` Apply strict limits to query expansion, retrieval size, token budget, embedding requests, latency, and spend.
- [ ] **RAG-099** `P1` Validate and sanitize retrieved text before downstream rendering or tool use; do not treat retrieved instructions as authorized actions.
- [ ] **RAG-100** `P1` Test malicious document content for prompt-injection resistance and independent authorization of all model-proposed tools.
- [ ] **RAG-101** `P1` Protect embedding provider and search API credentials in trusted server components.
- [ ] **RAG-102** `P1` Test source deletion, revocation, and permission updates against retrievable chunks, responses, caches, and conversation context.
- [ ] **RAG-103** `P0` Prevent cross-tenant data leakage via embedding caches, search-result caches, response caches, and conversation memory.
- [ ] **RAG-104** `P2` Define retry/backoff and partial-degradation behavior for unavailable index, source system, or embedding service.
- [ ] **RAG-105** `P1` Measure API latency, search relevance, ingestion lag, failures, and cost using appropriate privacy-safe telemetry.
- [ ] **RAG-106** `P1` Test pagination, score thresholds, and metadata filters against their documented search API behavior.
- [ ] **RAG-107** `P1` Keep sensitive queries, retrieved passages, provider payloads, and citations out of broad-access logs and traces.
- [ ] **RAG-108** `P1` Run contract and regression tests for retrieval result formats and citation identifiers used by clients.

## Release gate

- [ ] Knowledge sources have accountable owners, approved permitted uses, provenance records, and documented inclusion/exclusion and retention policies.
- [ ] Ingestion, extraction, chunking, embeddings, indexing, and synchronization have been tested with representative source formats and update/delete scenarios.
- [ ] Retrieval enforces document, user, group, and tenant authorization before any protected passage is sent to the model or client; cross-tenant tests pass.
- [ ] Held-out relevance checks meet agreed recall, precision/ranking, identifier search, and latency thresholds for critical question types.
- [ ] Grounded answers meet predeclared factual support, citation accuracy, completeness, uncertainty, and abstention criteria; severe unsupported claims are resolved or accepted through an authorized process.
- [ ] Stale, revoked, conflicting, insufficient, and malicious source material triggers approved warnings, no-answer behavior, containment, or escalation rather than unauthorized disclosure.
- [ ] API and frontend integrations preserve safe source identifiers, access boundaries, evidence presentation, and usable recovery paths where applicable.
- [ ] A named owner approves the exact corpus/index/model configurations, remaining limitations, monitoring of freshness/quality, and incident response or rollback plan.

**Domain-specific approval rule:** Block sign-off if unauthorized content can be retrieved or disclosed, critical source revocations fail to propagate within approved bounds, harmful prompt injection enables unapproved actions, or high-impact answers present materially unsupported or incorrect citations without accepted mitigation. A plausible generated answer or clickable citation alone is not proof of source fidelity or legal compliance.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#16_rag_and_knowledge_bases), not prerequisites or verification evidence.

## Trusted references and scope

The primary technical references below describe common RAG patterns and specific vendor implementations. Their mechanisms and defaults are conditional, not universal requirements.

- [Microsoft Azure AI Search — RAG overview](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview) — retrieval architecture, chunking, security boundaries, multi-source retrieval, citation context.
- [Microsoft Azure Architecture Center — RAG solution design and evaluation](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide) — end-to-end architecture and distinct retrieval and answer-quality evaluation stages.
- [Microsoft Azure Architecture Center — Retrieval phase](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-information-retrieval) — hybrid search, relevant passage ranking, reranking, recall/precision tradeoffs, latency.
- [Microsoft Azure Architecture Center — LLM end-to-end evaluation](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-llm-evaluation-phase) — groundedness, completeness, relevance, correctness, and evaluation limitations.
- [Microsoft Azure Architecture Center — RAG prompt engineering](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-prompt-engineering) — source-grounding instructions, abstention, citations, handling conflicting documents.
- [Amazon Bedrock — Knowledge-base chunking](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html) — structure-aware chunking, metadata, and treatment of tables and multimodal content.
- [Amazon Bedrock — Knowledge-base metadata](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-metadata.html) — document and per-chunk metadata for search filters and provenance.
- [Amazon Bedrock — Data-source synchronization](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-data-source-sync-ingest.html) — source ingestion, synchronization, and operational failure handling.
- [OpenAI API — Retrieval guide](https://developers.openai.com/api/docs/guides/retrieval) — vector stores, file chunking, metadata filters, indexing status, and eventual deletion consistency.
- [OWASP — Vector and Embedding Weaknesses](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/) — injection, poisoning, tenant isolation, and sensitive information risks in RAG.
- [OWASP — LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) — trust boundaries for retrieved text and limits of prompt-only defenses.

**Applicability:** Azure AI Search, Amazon Bedrock, and OpenAI Retrieval support different indexing, chunking, metadata, and deletion behaviors; validate deployed service versions and settings rather than transferring defaults between vendors. Some retrieval operations and deletions can be eventually consistent. Embeddings and vector similarity are not a substitute for authorization. A high retrieval score, citation, or instruction to ground responses does not guarantee factual accuracy, privacy protection, or resistance to prompt injection. Never ingest protected content without the appropriate processing rights and scope.

**Source review date:** 2026-11-12.
