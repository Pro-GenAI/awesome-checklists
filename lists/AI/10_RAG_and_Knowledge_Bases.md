# 10 — RAG and Knowledge Bases Checklist

> Verify that retrieval-augmented generation (RAG) uses authorized, attributable, sufficiently fresh evidence; retrieves relevant passages; and produces answers whose factual claims can be checked against the source. Search relevance, answer quality, and access controls are separate requirements: improving one does not establish the others.

> **Scope: AI-specific.** This file is one part of the 10_RAG_and_Knowledge_Bases.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Knowledge ingestion and provenance

- [ ] **RAG-001** `P2` Inventory all knowledge sources, source systems, content types, document owners, and intended retrieval audiences.
- [ ] **RAG-002** `P2` Document the business purpose and allowed use of each corpus before ingesting it into an AI retrieval system.
- [ ] **RAG-003** `P1` Verify permissions, licenses, privacy notices, and contractual restrictions permit indexing, embedding, and sending content to selected providers.
- [ ] **RAG-004** `P2` Assign a steward and update contact to each authoritative source and significant dataset.
- [ ] **RAG-005** `P2` Record source identifiers, canonical URLs or document paths, titles, content versions, and last-updated timestamps where available.
- [ ] **RAG-006** `P2` Identify the source of truth when the same policy, specification, or product fact appears in several repositories.
- [ ] **RAG-007** `P2` Define which repositories, folders, collections, documents, and fields are in scope or excluded from indexing.
- [ ] **RAG-008** `P1` Apply source-side user, group, role, tenant, and document restrictions to the retrieval design.
- [ ] **RAG-009** `P1` Reject or quarantine content that exceeds permitted sensitivity, retention, licensing, or geographic processing constraints.
- [ ] **RAG-010** `P1` Validate ingestion connectors, file format support, parser behavior, and accepted document sizes against representative source files.
- [ ] **RAG-011** `P1` Check extraction quality for PDFs, scanned pages, tables, footnotes, headings, hyperlinks, and other structured content.
- [ ] **RAG-012** `P1` Measure ingestion failures, unsupported files, truncated content, missing text, and processing retries instead of silently dropping documents.
- [ ] **RAG-013** `P1` Preserve page, section, row, or anchor metadata needed to navigate back to a specific source passage.
- [ ] **RAG-014** `P1` Keep a traceable mapping from every indexed chunk to its original source item and content revision.
- [ ] **RAG-015** `P1` Capture source language, locale, effective date, authority, classification, and relevant metadata where available and permissible.
- [ ] **RAG-016** `P2` Define document deduplication, version precedence, superseded-content handling, and conflicting-source rules.
- [ ] **RAG-017** `P1` Configure incremental updates, full synchronization, and retry behavior according to each source's change frequency.
- [ ] **RAG-018** `P1` Ensure revoked access, source deletion, document expiration, and retention changes propagate to all retrievable copies.
- [ ] **RAG-019** `P1` Test the lag between a source update or deletion and its visibility in search, cache, and generated answers.
- [ ] **RAG-020** `P2` Define a safe quarantine and incident process for malicious, corrupted, or unauthorized indexed content.
- [ ] **RAG-021** `P1` Control access and retention for raw files, extracted text, embeddings, chunk metadata, and ingestion error reports.
- [ ] **RAG-022** `P2` Record ingestion pipeline, parser, embedding, and index versions so a problematic corpus can be reconstructed.

## Chunking, embeddings, and indexing

- [ ] **RAG-023** `P1` Choose a chunking strategy based on document structure, query patterns, retrieval quality, and model context constraints.
- [ ] **RAG-024** `P1` Evaluate fixed-size, structure-aware, parent-child, semantic, or no-chunking strategies only where supported and useful.
- [ ] **RAG-025** `P1` Test chunk boundaries against headings, tables, lists, code blocks, citations, and other semantically connected content.
- [ ] **RAG-026** `P1` Choose and measure chunk size and overlap so evidence is coherent without unnecessary duplicate context.
- [ ] **RAG-027** `P1` Check whether table rows, captions, and figure references retain the context required to answer realistic questions.
- [ ] **RAG-028** `P1` Prevent accidental merging of content with different access permissions, tenants, or retention policies into a shared chunk.
- [ ] **RAG-029** `P1` Preserve identifiers and access metadata across source files, document records, chunks, and embeddings.
- [ ] **RAG-030** `P1` Validate extraction and text normalization preserve units, dates, punctuation, technical identifiers, and multilingual meaning.
- [ ] **RAG-031** `P1` Select embedding models that support relevant languages, domains, passage lengths, and input types.
- [ ] **RAG-032** `P2` Record embedding model revision, dimensionality, preprocessing, tokenizer, and vector similarity settings.
- [ ] **RAG-033** `P1` Verify query and document embedding configurations are compatible for each active index.
- [ ] **RAG-034** `P1` Test long documents, very short snippets, duplicate texts, and near-duplicate passages for search quality.
- [ ] **RAG-035** `P2` Define index schema for text, vector fields, metadata filters, source locations, and document version.
- [ ] **RAG-036** `P1` Validate indexing completion status before marking newly added content available to users.
- [ ] **RAG-037** `P1` Check partial ingestion and failed embedding jobs for inconsistent or missing chunks.
- [ ] **RAG-038** `P1` Use scoped indexing and least-privilege credentials to prevent writers modifying unrelated tenant data.
- [ ] **RAG-039** `P1` Plan safe re-embedding and index rebuilds when embedding models or extraction strategies change.
- [ ] **RAG-040** `P1` Test index migration or blue-green index switching without serving mixed incompatible embeddings.
- [ ] **RAG-041** `P1` Measure index storage, vector counts, ingestion time, query cost, and performance against expected corpus growth.
- [ ] **RAG-042** `P2` Document index compaction, lifecycle, backup/restore dependencies, and retention for the selected search service.
- [ ] **RAG-043** `P1` Verify source removal deletes or invalidates associated vectors, text, and cache entries within the approved time bound.
- [ ] **RAG-044** `P1` Review index quality using representative queries before enabling a new chunking or embedding configuration.

## Retrieval and reranking

- [ ] **RAG-045** `P2` Define representative information needs and user queries, including precise identifiers, synonyms, ambiguity, and conversational context.
- [ ] **RAG-046** `P1` Create query-to-relevant-document or passage judgments for an authorized held-out evaluation sample.
- [ ] **RAG-047** `P1` Benchmark keyword, dense-vector, and hybrid retrieval where relevant instead of assuming one strategy is universally superior.
- [ ] **RAG-048** `P1` Measure retrieval recall at k, precision at k, ranking quality, and empty-result behavior with appropriate judgments.
- [ ] **RAG-049** `P1` Test exact-match retrieval for part numbers, legal references, codes, names, and other identifiers that embeddings may miss.
- [ ] **RAG-050** `P1` Test semantic retrieval for paraphrases, domain-specific language, multilingual questions, and concept matching.
- [ ] **RAG-051** `P1` Apply user and tenant authorization filters before protected content can be passed to the model, not merely masked in the UI.
- [ ] **RAG-052** `P1` Verify all query rewrites, expansions, multi-search branches, and reranking stages preserve the same access restrictions.
- [ ] **RAG-053** `P0` Test retrieval isolation against users with similar queries but different document permissions.
- [ ] **RAG-054** `P2` Define metadata filtering for source authority, date, product version, locale, and tenant when relevant to answers.
- [ ] **RAG-055** `P1` Evaluate whether source recency, quality, or authority boosting improves factual retrieval without hiding essential contrary evidence.
- [ ] **RAG-056** `P1` Check query rewriting and multi-turn search for incorrect carryover of previous user, tenant, or subject context.
- [ ] **RAG-057** `P1` Compare candidate-set size and reranking strategies against recall, precision, latency, and operating cost.
- [ ] **RAG-058** `P1` Verify rerankers receive only permitted content and do not cause unintended secondary disclosures.
- [ ] **RAG-059** `P2` Define thresholds and fallbacks for low-confidence, low-relevance, or no-result retrieval instead of always generating an answer.
- [ ] **RAG-060** `P1` Test duplicate chunks, near-duplicate documents, conflicting versions, and noisy passages in ranked results.
- [ ] **RAG-061** `P1` Ensure multi-source retrieval prioritizes authoritative content and handles unresolved conflicts explicitly.
- [ ] **RAG-062** `P1` Measure end-to-end retrieval latency, timeouts, index availability, and degraded search paths at realistic concurrency.
- [ ] **RAG-063** `P1` Limit top-k, query expansion, tool calls, and returned context to control token usage and denial-of-service risk.
- [ ] **RAG-064** `P1` Collect appropriately redacted diagnostics about query type, retrieved passage IDs, scores, filter outcomes, and reranking version.
- [ ] **RAG-065** `P0` Use controlled adversarial cases to verify malicious document text cannot change search permissions or trigger external actions.
- [ ] **RAG-066** `P1` Rerun relevance tests when corpus distribution, embedding model, search engine, ranking configuration, or query patterns change.

## Grounding, citations, and freshness

- [ ] **RAG-067** `P2` Specify when the system must answer only from retrieved evidence and when other authorized knowledge sources may be used.
- [ ] **RAG-068** `P1` Keep retrieved passages clearly separated from privileged instructions and label them as untrusted source content.
- [ ] **RAG-069** `P1` Test direct and indirect prompt injection embedded in documents, snippets, titles, metadata, and retrieved web content.
- [ ] **RAG-070** `P1` Require source-backed factual claims to reference retrievable evidence identifiers where the product promises citations.
- [ ] **RAG-071** `P1` Validate that a citation links to the particular source passage supporting the statement, not merely a thematically related document.
- [ ] **RAG-072** `P1` Test that cited evidence is visible or accessible to the requesting user with appropriate access controls.
- [ ] **RAG-073** `P1` Ensure generated answers distinguish verified source statements, reasoning or synthesis, and unsupported assumptions.
- [ ] **RAG-074** `P1` Measure answer groundedness, relevance, completeness, correctness, and evidence utilization on representative held-out tasks.
- [ ] **RAG-075** `P1` Include cases where retrieval finds no source, conflicting sources, outdated documents, or sources that do not answer the question.
- [ ] **RAG-076** `P2` Define abstention, clarification, escalation, or alternate search behavior for insufficient or contradictory evidence.
- [ ] **RAG-077** `P1` Do not fabricate source titles, URLs, page numbers, quotations, or verification status when metadata is unavailable.
- [ ] **RAG-078** `P1` Preserve document version, effective date, and source timestamp where staleness materially affects the decision.
- [ ] **RAG-079** `P1` Handle conflicting publication dates, superseded policies, and source revisions without silently mixing incompatible versions.
- [ ] **RAG-080** `P1` Set accepted freshness windows for time-sensitive facts and provide a safe mechanism to re-query or warn users.
- [ ] **RAG-081** `P1` Verify answers change appropriately after controlled source updates, document revocation, and reindexing.
- [ ] **RAG-082** `P1` Test whether model summaries omit essential qualifiers, footnotes, exceptions, or conditions in retrieved passages.
- [ ] **RAG-083** `P1` Check numerical, legal, financial, and other high-impact factual claims against exact authoritative passages where applicable.
- [ ] **RAG-084** `P2` Define evaluation thresholds for unsupported claims and incorrect citations separately from overall answer satisfaction.
- [ ] **RAG-085** `P1` Measure the impact of context ordering, truncation, chunk count, and conflicting context on generated output.
- [ ] **RAG-086** `P1` Verify structured citations and source references survive streaming, caching, and frontend rendering.
- [ ] **RAG-087** `P1` Disclose evidence limitations and encourage qualified review when retrieved documents cannot justify consequential decisions.
- [ ] **RAG-088** `P2` Document a recovery and correction process for discovered inaccurate, poisoned, expired, or misattributed answers.

## Frontend Checks

*Apply these client-side checks only when the AI feature has a user-facing or reviewer-facing interface. They remain part of this AI domain; the general frontend checklist inventory is separate.*

- [ ] **RAG-109** `P1` Make clear when an answer is generated from a knowledge base and when the system lacks sufficient supporting documents.
- [ ] **RAG-110** `P1` Show source titles, authors or publishers, dates, and accessible links where available and permitted.
- [ ] **RAG-111** `P1` Ensure each user-visible citation navigates to the cited document or specific supporting section when possible.
- [ ] **RAG-112** `P1` Distinguish relevant source references from verified evidence supporting a particular factual claim.
- [ ] **RAG-113** `P1` Explain when a source is unavailable, access-restricted, expired, or no longer part of the knowledge base.
- [ ] **RAG-114** `P1` Display document freshness, version, or effective-date warnings when these affect user decisions.
- [ ] **RAG-115** `P1` Provide comprehensible clarification or no-answer states for ambiguous queries and missing evidence.
- [ ] **RAG-116** `P1` Ensure users can inspect sources without exposing content they are not permitted to access.
- [ ] **RAG-117** `P1` Test source navigation, permissions, and deep links after login, account switching, or session expiration.
- [ ] **RAG-118** `P1` Prevent retrieved HTML, Markdown, file names, or snippets from injecting active scripts into the frontend.
- [ ] **RAG-119** `P1` Provide accessible headings, keyboard interaction, link text, and focus handling for citations and source panels.
- [ ] **RAG-120** `P1` Preserve citation-to-claim mapping while rendering markdown tables, lists, long answers, and streamed text.
- [ ] **RAG-121** `P1` Handle slow retrieval, partial answers, generation timeouts, and source-loading failures without implying results are final.
- [ ] **RAG-122** `P1` Communicate source conflicts or limitations rather than choosing one document without explanation.
- [ ] **RAG-123** `P1` Support long, multilingual, and mixed-script queries in relevant locales without losing retrieval context.
- [ ] **RAG-124** `P1` Make it easy to revise a query or report a wrong answer, broken citation, or outdated document.
- [ ] **RAG-125** `P1` Protect sensitive questions and retrieved snippets from accidental browser persistence, analytics, or error reports.
- [ ] **RAG-126** `P1` Explain that a citation does not alone guarantee the claim is correct or legally authoritative.
- [ ] **RAG-127** `P1` Verify frontend caches do not surface previous users' source snippets, answers, or permission-restricted results.
- [ ] **RAG-128** `P1` Review representative user journeys to assess whether evidence presentation supports accurate, independent judgment.

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

**Optional tooling:** [AI-scope testing examples](../references/optional-testing-tools-ai.md#10_rag_and_knowledge_bases), not prerequisites or evidence of PASS.

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
