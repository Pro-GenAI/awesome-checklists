# 13 — Multimodal AI Quality Checklist

> Verify that AI features using images, audio, speech, video, documents, or combinations of modalities produce fit-for-purpose, safe, accessible, and properly grounded results. An AI model's claim to support a modality does not establish accuracy for a specific task, language, device, input quality, or deployment configuration.

> **Scope: AI-specific.** This file is one part of the 13_Multimodal_AI_Quality.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Modality support and requirements

- [ ] **MULTI-001** `P2` Inventory the exact input and output modalities supported by each model, endpoint, client, and production workflow.
- [ ] **MULTI-002** `P2` Define the intended tasks and acceptable outcomes for image understanding, generation, audio, speech, video, and multimodal combinations actually used.
- [ ] **MULTI-003** `P2` Record the model/provider snapshot, modality capabilities, deployment region, and any feature-specific limitations for each route.
- [ ] **MULTI-004** `P2` Document supported file formats, codecs, dimensions, sample rates, durations, frame rates, and request-size limits for every applicable modality.
- [ ] **MULTI-005** `P2` Specify user populations, languages, scripts, accents, device types, and assistive-technology requirements relevant to the deployment.
- [ ] **MULTI-006** `P2` Define the task-specific quality, factuality, safety, latency, throughput, and cost thresholds before comparing variants.
- [ ] **MULTI-007** `P2` Identify consequential uses requiring specialist review rather than inferring medical, legal, biometric, or safety-critical accuracy.
- [ ] **MULTI-008** `P1` Distinguish capabilities that are native to a multimodal model from chained OCR, ASR, TTS, retrieval, and other processing components.
- [ ] **MULTI-009** `P2` Map media preprocessing, upload, storage, inference, postprocessing, playback, and deletion across the complete data flow.
- [ ] **MULTI-010** `P1` Verify media processing rights, licenses, speaker permissions, privacy notices, and any required user consent before collecting samples.
- [ ] **MULTI-011** `P2` Document how raw, transformed, compressed, cropped, sampled, or otherwise degraded inputs may change model-visible information.
- [ ] **MULTI-012** `P2` Specify whether the system may analyze metadata, EXIF, hidden document layers, timestamps, or only the actual media content exposed by its API.
- [ ] **MULTI-013** `P2` Define failure behavior for unsupported media, missing tracks, corrupt files, encrypted files, and media that exceeds provider limits.
- [ ] **MULTI-014** `P1` Set resource and token budgets for high-resolution images, long recordings, video frames, and repeated multimodal processing.
- [ ] **MULTI-015** `P2` Specify whether media input is ephemeral, retained for quality review, or used for model improvement under the applicable data policy.
- [ ] **MULTI-016** `P1` Establish source and generated-media provenance, attribution, and disclosure requirements where relevant to use and policy.
- [ ] **MULTI-017** `P2` Define expected behavior for ambiguous scenes, inaudible speech, incomplete frames, unknown speakers, and contradictory modalities.
- [ ] **MULTI-018** `P1` Treat audio/video content, embedded text, captions, and transcribed speech as untrusted data for instruction-following and tool use.
- [ ] **MULTI-019** `P2` Identify which downstream actions require validated evidence and human confirmation instead of relying on perception alone.
- [ ] **MULTI-020** `P2` Record fallback paths to accessible text, human support, alternate media formats, or non-AI features when a modality fails.
- [ ] **MULTI-021** `P2` Define versioned evaluation fixtures for single-modality tasks and paired or synchronized cross-modal tasks.
- [ ] **MULTI-022** `P2` Assign responsible product, engineering, accessibility, privacy, safety, and evaluation owners to supported multimodal workflows.

## Image and video quality

- [ ] **MULTI-023** `P1` Evaluate image understanding on representative photographs, screenshots, diagrams, charts, scans, and documents as applicable.
- [ ] **MULTI-024** `P1` Test small text, dense tables, rotated pages, blur, glare, shadows, occlusion, and low-resolution content.
- [ ] **MULTI-025** `P1` Measure OCR or visual text-extraction errors separately from factual reasoning errors made after extraction.
- [ ] **MULTI-026** `P1` Verify correct handling of multilingual and non-Latin text embedded in images where supported.
- [ ] **MULTI-027** `P1` Check that image orientation, cropping, resizing, tiling, and detail settings preserve task-critical evidence.
- [ ] **MULTI-028** `P1` Test object counting, spatial relationships, relative position, and coordinate-sensitive requests against ground-truth fixtures.
- [ ] **MULTI-029** `P1` Evaluate chart legends, units, axis labels, colors, line styles, and uncertainty when interpreting data visualizations.
- [ ] **MULTI-030** `P1` Verify generated descriptions distinguish visible evidence from guesses about identity, intent, location, or unseen events.
- [ ] **MULTI-031** `P1` Test refusal, abstention, or escalation when an image is insufficient to support a consequential conclusion.
- [ ] **MULTI-032** `P1` Check image generation and editing for prompt adherence, requested objects, composition, text accuracy, and preservation constraints.
- [ ] **MULTI-033** `P1` Assess generated images for unexpected additions, missing subjects, artifacts, distortions, and unsafe or misleading details.
- [ ] **MULTI-034** `P1` Evaluate unintended changes to protected visual attributes or user-supplied elements during requested image edits.
- [ ] **MULTI-035** `P2` Record image generation parameters, seeds where available, sizes, model versions, and variation across repeated outputs.
- [ ] **MULTI-036** `P2` Define appropriate provenance and AI-generation disclosure for synthetic images when required by product policy or law.
- [ ] **MULTI-037** `P1` Validate that image uploads and downstream outputs do not expose private EXIF/GPS metadata, visually inferred precise locations, or other unapproved file content. Where photo-geolocation is supported, test representative images **with and without geotags**, authorize the purpose and subjects as applicable, and restrict disclosure to an approved location granularity; removing EXIF alone is not sufficient.
- [ ] **MULTI-038** `P1` Test video ingestion against supported codecs, containers, duration, aspect ratio, variable frame rates, and audio tracks.
- [ ] **MULTI-039** `P2` Document how video frames are sampled and which events may be missed between sampled frames.
- [ ] **MULTI-040** `P1` Test temporal ordering, action recognition, scene transitions, continuity, and event start/end timing with labeled video clips.
- [ ] **MULTI-041** `P1` Check whether summaries correctly distinguish actions visible in frames from events inferred without supporting video evidence.
- [ ] **MULTI-042** `P1` Evaluate visual changes in the presence of camera motion, panning, zoom, cuts, low light, and motion blur.
- [ ] **MULTI-043** `P1` Verify synchronized audio and video references preserve the correct timestamp and source segment.
- [ ] **MULTI-044** `P1` Test long-form video behavior when the clip exceeds the effective frame, token, or context budget.
- [ ] **MULTI-045** `P1` Assess generated image or video safety with representative permitted and disallowed cases under the approved policy.
- [ ] **MULTI-046** `P1` Ensure downloaded, stored, or displayed visual media follows access controls, licensing, retention, and deletion rules.

## Audio and speech quality

- [ ] **MULTI-047** `P2` Define separate quality thresholds for speech recognition, translation, diarization, synthesis, and realtime conversation as applicable.
- [ ] **MULTI-048** `P1` Benchmark speech recognition against correctly transcribed reference audio using word or character error rate suited to the language.
- [ ] **MULTI-049** `P1` Test accents, dialects, code-switching, non-native speech, low-volume speakers, and regional pronunciation.
- [ ] **MULTI-050** `P1` Include real background noise, echo, reverberation, crosstalk, microphone variation, and telephony compression in evaluation audio.
- [ ] **MULTI-051** `P1` Test recognition of domain terminology, names, identifiers, dates, amounts, addresses, and negation that affect user outcomes.
- [ ] **MULTI-052** `P1` Measure empty, truncated, duplicated, reordered, and hallucinated transcript segments separately from overall transcription error rates.
- [ ] **MULTI-053** `P1` Verify language detection and explicit language hints behave correctly for supported languages and mixed-language conversations.
- [ ] **MULTI-054** `P1` Test actual availability of word timestamps, speaker labels, and confidence fields rather than assuming all transcription models return them.
- [ ] **MULTI-055** `P1` Evaluate speaker diarization with overlaps, interruptions, speaker changes, and unknown speakers where supported.
- [ ] **MULTI-056** `P1` Validate sample rate, channel layout, codec, clipping, loudness, silence detection, and resampling behavior for audio input.
- [ ] **MULTI-057** `P1` Test voice-activity detection or turn segmentation against pauses, short replies, hesitations, cross-talk, and non-speech sounds.
- [ ] **MULTI-058** `P1` Measure final transcript latency and partial-transcript corrections under realistic realtime connection conditions.
- [ ] **MULTI-059** `P1` Ensure partial ASR output is not treated as a verified final transcript for irreversible actions.
- [ ] **MULTI-060** `P1` Check speech translation for meaning preservation, negation, named entities, tone, and relevant professional terminology.
- [ ] **MULTI-061** `P1` Evaluate synthesized speech for intelligibility, pronunciation, pacing, pauses, naturalness, and supported-language quality.
- [ ] **MULTI-062** `P1` Check synthesized speech for unexpected content, omitted words, unstable pronunciation, and misleading emotional or speaker presentation.
- [ ] **MULTI-063** `P1` Confirm the selected synthetic voice has appropriate consent/rights and that AI-generated speech is disclosed where required.
- [ ] **MULTI-064** `P1` Test streaming audio playback for missing chunks, reordering, clipping, jitter, long pauses, and reconnection artifacts.
- [ ] **MULTI-065** `P1` Test conversational interruptions, barge-in, cancellation, and truncation so unplayed responses are not treated as heard or confirmed.
- [ ] **MULTI-066** `P1` Verify spoken audio and visible transcript or subtitles refer to the same actual turn and do not falsely claim exact timing when unavailable.
- [ ] **MULTI-067** `P1` Validate processing of long recordings, silence-only files, unsupported channels, and audio exceeding provider limits.
- [ ] **MULTI-068** `P1` Assess content safety and privacy for speech and audio, including inadvertent disclosure of background conversations.
- [ ] **MULTI-069** `P1` Test audio fallback to text input/output or accessible transcripts when microphone access, playback, or synthesis fails.
- [ ] **MULTI-070** `P1` Verify audio storage, playback logs, transcription retention, and speaker identifiers comply with approved access and deletion controls.

## Multimodal evaluation and accessibility

- [ ] **MULTI-071** `P2` Maintain a held-out, versioned evaluation set containing each supported modality and meaningful cross-modal combinations.
- [ ] **MULTI-072** `P2` Record evaluation inputs, expected outcomes, source rights, modality metadata, and reference judgments for every case.
- [ ] **MULTI-073** `P1` Create examples where image, speech, video, and text convey complementary information needed for the correct result.
- [ ] **MULTI-074** `P1` Test contradictory visual and spoken instructions and document which information should govern the response.
- [ ] **MULTI-075** `P1` Measure answer grounding to the actual relevant visual frame, audio segment, or document region instead of a related but insufficient source.
- [ ] **MULTI-076** `P1` Evaluate cross-modal temporal alignment, speaker-to-scene association, and event chronology when the task depends on synchronization.
- [ ] **MULTI-077** `P1` Check that text-only and single-modality baselines are compared fairly with multimodal results where useful.
- [ ] **MULTI-078** `P1` Report quality by input type, language, device quality, content difficulty, and other risk-relevant cohorts with sufficient sample sizes.
- [ ] **MULTI-079** `P1` Separate extraction failures, model reasoning failures, unsafe generation, input transport errors, and UI presentation defects.
- [ ] **MULTI-080** `P1` Use trained human reviewers or calibrated rubrics for subjective visual/audio quality and multimodal factual support.
- [ ] **MULTI-081** `P2` Document model-judge limitations and cross-modal evaluation bias rather than trusting one aggregate automated score.
- [ ] **MULTI-082** `P1` Repeat variable generation tests where needed and record versioned models, transforms, seeds, settings, and run identifiers.
- [ ] **MULTI-083** `P1` Test adversarial instructions embedded in images, audio transcripts, subtitles, and video frames using authorized benign fixtures.
- [ ] **MULTI-084** `P1` Verify that untrusted media content cannot elevate tool permissions, change system instructions, or access unrelated user data.
- [ ] **MULTI-085** `P1` Evaluate text alternatives for informative images and controls according to applicable accessibility requirements.
- [ ] **MULTI-086** `P1` Provide appropriate captions for synchronized audio/video, including necessary non-speech information where required.
- [ ] **MULTI-087** `P1` Provide transcripts, audio descriptions, or other media alternatives appropriate to the content and applicable WCAG level.
- [ ] **MULTI-088** `P1` Check that generated captions and transcripts are edited or verified where consequential accuracy or accessibility depends on them.
- [ ] **MULTI-089** `P1` Test caption timing, speaker labels, visual legibility, font scaling, and playback speed controls where provided.
- [ ] **MULTI-090** `P1` Verify keyboard operation, focus indication, accessible controls, and screen-reader labeling of media upload and playback experiences.
- [ ] **MULTI-091** `P1` Test multimodal use under poor network conditions and on assistive devices without losing critical state or accessibility information.
- [ ] **MULTI-092** `P1` Check harmful or misleading synthetic-media outputs and provenance/disclosure limitations as part of the actual product risk review.
- [ ] **MULTI-093** `P1` Measure time to first useful output, total completion, resource usage, and cost for each supported modality mix.
- [ ] **MULTI-094** `P1` Require qualified approval of significant quality, privacy, security, and accessibility shortcomings before release.

## Frontend Checks

*Apply these client-side checks only when the AI feature has a user-facing or reviewer-facing interface. They remain part of this AI domain; the general frontend checklist inventory is separate.*

- [ ] **MULTI-115** `P1` Clearly indicate which image, audio, video, and file types can be used and their actual current size and duration limits.
- [ ] **MULTI-116** `P1` Give users accessible upload, recording, preview, replacement, and removal controls before submission.
- [ ] **MULTI-117** `P1` Explain what media will be processed or shared with an external AI provider and request any required consent.
- [ ] **MULTI-118** `P1` Show meaningful recording, uploading, transcribing, generating, buffering, and completed states.
- [ ] **MULTI-119** `P1` Provide accessible and understandable error messages for malformed, unsupported, too-large, or disconnected media.
- [ ] **MULTI-120** `P1` Allow users to correct transcription errors and clarify visual interpretation before consequential external actions.
- [ ] **MULTI-121** `P1` Mark partial captions, provisional transcripts, and generated previews as unverified until finalized where appropriate.
- [ ] **MULTI-122** `P1` Provide required captions, text transcripts, audio descriptions, and alternative access to media content.
- [ ] **MULTI-123** `P1` Test keyboard, focus, screen reader, caption controls, and audio player behavior across supported platforms.
- [ ] **MULTI-124** `P1` Ensure generated alt text and captions are accurate enough for their purpose or provide a correction mechanism.
- [ ] **MULTI-125** `P1` Keep audio and visible transcript synchronized when possible and explain limitations where exact alignment is unavailable.
- [ ] **MULTI-126** `P1` Implement usable microphone and camera permission-denied states and alternatives to voice-only interactions.
- [ ] **MULTI-127** `P1` Handle interruption, pause, cancellation, playback stop, and session reconnection without duplicated or misleading completion.
- [ ] **MULTI-128** `P1` Display visual source thumbnails or source-time references only when the user is authorized to see them.
- [ ] **MULTI-129** `P1` Prevent unsafe rendering of user-supplied SVG/HTML or model-generated markup, scripts, and media links.
- [ ] **MULTI-130** `P1` Test responsive image, video, subtitles, long transcripts, and audio controls under text zoom and mobile layouts.
- [ ] **MULTI-131** `P1` Review multilingual, right-to-left, accented speech, and assistive-device behavior for the supported user population.
- [ ] **MULTI-132** `P1` Disclose AI-generated image, voice, or synthetic video when required and avoid implying it is human-authored or verified.
- [ ] **MULTI-133** `P1` Protect local previews, cached media, transcription history, and analytics against account switching and unauthorized sharing.
- [ ] **MULTI-134** `P1` Collect privacy-conscious user feedback on inaccurate recognition, missing captions, harmful outputs, and inaccessible workflows.

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

**Optional tooling:** [AI-scope testing examples](../references/optional-testing-tools-ai.md#13_multimodal_ai_quality), not prerequisites or evidence of PASS.

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
- [Privacy International — Nowhere to Hide?](https://privacyinternational.org/report/5736/nowhere-hide-privacy-risks-and-policy-implications-ai-geolocation/) — documented risk of inferring a photograph's sensitive location from visual cues even after removing GPS metadata.
- [UK ICO — Location data and privacy safeguards](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/online-tracking/guidance-for-consumer-internet-of-things-products-and-services/what-information-do-iot-products-use/) — jurisdiction-specific guidance on limiting location granularity, disclosure and processing.

**Applicability:** OpenAI vision, audio, transcription, and file-input capabilities differ by model, endpoint, and revision; verify current formats, quotas, metadata, and any deprecation dates instead of copying them across models. As of this source review, OpenAI documentation lists a February 26, 2027 shutdown for certain legacy transcription models and a January 6, 2027 shutdown for several legacy TTS models, so new deployments should check current alternatives. Amazon Bedrock multimodal indexing and retrieval are also workflow- and provider-specific; some modes do not search speech or support mixed text/image queries. WCAG 2.2 obligations depend on media type, live/prerecorded status, conformance level, and jurisdiction. NIST AI RMF guidance is voluntary and not a safety certification. Do not use automated visual or audio inference as unreviewed proof for consequential identity or health decisions.

**Source review date:** 2026-11-12. **Targeted image-geolocation privacy sources verified:** 2026-11-14; applicability depends on the data, use case and jurisdiction.
