# 19 — Multimodal AI Quality Checklist

> Verify that AI features using images, audio, speech, video, documents, or combinations of modalities produce fit-for-purpose, safe, accessible, and properly grounded results. An AI model's claim to support a modality does not establish accuracy for a specific task, language, device, input quality, or deployment configuration.

> **Scope: Backend / API-specific.** This file is one part of the 19_Multimodal_AI_Quality.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## API Checks

- [ ] **MULTI-095** `P1` Enforce authenticated user, tenant, and resource authorization for each media upload, processing request, retrieval, and generated output.
- [ ] **MULTI-096** `P1` Validate actual file magic bytes, supported MIME types, codecs, sizes, duration, sample rates, and dimensions server-side.
- [ ] **MULTI-097** `P1` Reject corrupted, encrypted, unsupported, or oversized media with documented safe error states.
- [ ] **MULTI-098** `P1` Scan or sandbox untrusted file parsing and prohibit execution of embedded content or metadata-driven commands.
- [ ] **MULTI-099** `P1` Check supported modality fields and combinations against the exact deployed model endpoint and API schema.
- [ ] **MULTI-100** `P2` Record whether image resizing, frame sampling, audio transcoding, or PDF rendering changes model-visible evidence.
- [ ] **MULTI-101** `P1` Enforce approved upper bounds on media counts, frame rates, audio duration, token usage, retries, and costs.
- [ ] **MULTI-102** `P1` Validate signed media URLs, temporary file handles, upload destinations, and storage permissions before processing.
- [ ] **MULTI-103** `P1` Keep sensitive media, speaker identifiers, transcripts, and generated files out of broad-access logs and traces.
- [ ] **MULTI-104** `P1` Test that temporary and retained media are deleted or inaccessible after revocation, expiry, or account removal as required.
- [ ] **MULTI-105** `P0` Prevent cross-tenant access through caches, model sessions, media asset IDs, and provider-side storage references.
- [ ] **MULTI-106** `P1` Check video timestamps, frame IDs, transcript segment IDs, and stream event ordering against API contracts.
- [ ] **MULTI-107** `P1` Handle partial realtime transcription or audio generation without reporting unfinished text or playback as completed.
- [ ] **MULTI-108** `P1` Verify retries and cancellation do not duplicate downstream communications, actions, or billed jobs unnecessarily.
- [ ] **MULTI-109** `P1` Test simultaneous media uploads and processing for rate-limit fairness and bounded resource utilization.
- [ ] **MULTI-110** `P1` Protect model-generated structured responses, extracted metadata, and tool arguments with schema and authorization checks.
- [ ] **MULTI-111** `P1` Check input, output, and transformed-media provenance identifiers remain traceable across API processing steps.
- [ ] **MULTI-112** `P1` Test unsupported features such as diarization, timestamp outputs, and alternate media tracks with explicit documented fallbacks.
- [ ] **MULTI-113** `P1` Validate privacy, consent, data residency, and retention settings for external multimodal model providers.
- [ ] **MULTI-114** `P1` Run production-equivalent multimodal API contract, safety, quality, and overload tests before deployment.

## Release gate

- [ ] Every advertised modality, combination, language, file format, and input limit is supported by the exact deployed model/API/client configuration and correctly documented.
- [ ] Representative image/video, audio/speech, and supported cross-modal tasks pass predeclared factuality, fidelity, temporal alignment, and user-task quality criteria.
- [ ] Low-quality input, unsupported metadata, missing evidence, ambiguous media, streaming failures, and incomplete results trigger tested safe fallback, abstention, or clarification behavior.
- [ ] Important privacy, consent, source-use rights, synthetic-media disclosures, and data lifecycle requirements have appropriate qualified approval.
- [ ] Unsafe media content and embedded instructions cannot bypass independent access controls, moderation, tool authorization, or protected data boundaries.
- [ ] Required text alternatives, transcripts, captions, visual descriptions, accessible controls, and supported assistive-technology journeys have been checked for the actual content and applicable WCAG requirements.
- [ ] Production-equivalent API and frontend tests verify format validation, size limits, media handling, cancellation, latency/cost budgets, and safe completion or failure states.
- [ ] Accountable owners approve relevant versioned evaluation results, known modality gaps, remaining high-impact risks, rollback paths, and the exact release.

**Domain-specific approval rule:** Block release where critical media interpretation or synthesis is materially misleading, protected recordings or images can be exposed, unsafe embedded media instructions enable unauthorized actions, or necessary accessible alternatives are missing for a supported consequential workflow without approved mitigation. Passing individual modality benchmarks does not prove correct cross-modal reasoning or regulatory compliance.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#19_multimodal_ai_quality), not prerequisites or verification evidence.

## Trusted references and scope

The primary technical documentation and accessibility standards below inform project-specific verification. These sources cover different vendors and media modalities; use only the standards and provider features applicable to the deployed system.

- [OpenAI API — Images and vision](https://developers.openai.com/api/docs/guides/images-vision) — visual input formats, detail/resizing, cost, and limitations of image understanding and generation.
- [OpenAI API — File inputs](https://developers.openai.com/api/docs/guides/file-inputs) — PDF and document input capabilities, page-image processing, and model-specific constraints.
- [OpenAI API — Transcription overview](https://developers.openai.com/api/docs/guides/transcription) — file and realtime speech-to-text workflows and changing model availability.
- [OpenAI API — Realtime transcription](https://developers.openai.com/api/docs/guides/realtime-transcription) — partial/final transcripts, supported languages, latency/quality tradeoffs, and missing speaker or timing metadata.
- [OpenAI API — Realtime conversations](https://developers.openai.com/api/docs/guides/realtime-conversations) — streamed audio, voice activity detection, interruption, session state, and audio playback semantics.
- [OpenAI API — Text to speech](https://developers.openai.com/api/docs/guides/text-to-speech) — speech synthesis quality, voice and language support, disclosure obligations, and deprecated audio workflow limitations.
- [W3C WAI — Making Audio and Video Media Accessible](https://www.w3.org/WAI/media/av/) — captions, transcripts, visual description, and usable media-player accessibility.
- [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/) — relevant success criteria for non-text content, synchronized media, and accessible user interaction.
- [W3C WAI — Transcripts](https://www.w3.org/WAI/media/av/transcripts/) — descriptive transcripts and accessibility requirements by media type.
- [Amazon Bedrock — Choosing multimodal processing approaches](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-multimodal-choose-approach.html) — limitations and modality differences in multimedia indexing, audio extraction, and retrieval.
- [Amazon Bedrock — Multimodal knowledge base troubleshooting](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-multimodal-troubleshooting.html) — provider-specific file, query, data source, and reranking limitations.
- [NIST — Generative AI Profile (AI 600-1)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) — risk-based evaluation of misleading, unsafe, or harmful generative AI content.

**Applicability:** OpenAI vision, audio, transcription, and file-input capabilities differ by model, endpoint, and revision; verify current formats, quotas, metadata, and any deprecation dates instead of copying them across models. As of this source review, OpenAI documentation lists a February 26, 2027 shutdown for certain legacy transcription models and a January 6, 2027 shutdown for several legacy TTS models, so new deployments should check current alternatives. Amazon Bedrock multimodal indexing and retrieval are also workflow- and provider-specific; some modes do not search speech or support mixed text/image queries. WCAG 2.2 obligations depend on media type, live/prerecorded status, conformance level, and jurisdiction. NIST AI RMF guidance is voluntary and not a safety certification. Do not use automated visual or audio inference as unreviewed proof for consequential identity or health decisions.

**Source review date:** 2026-11-12.
