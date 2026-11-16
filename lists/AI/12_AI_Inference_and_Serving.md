# 12 — AI Inference and Serving Checklist

> Verify that production AI inference is deployable, secure, performant, cost-bounded, and recoverable under realistic workloads. Serving improvements must be measured against user-visible quality and latency; faster execution or higher aggregate throughput does not by itself establish a release-ready system.

> **Scope: AI-specific.** This file is one part of the 12_AI_Inference_and_Serving.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Serving architecture and capacity

- [ ] **SERVE-001** `P2` Define the supported inference tasks, input modalities, expected users, deployment regions, and responsible service owner.
- [ ] **SERVE-002** `P1` Choose real-time, asynchronous, batch, streaming, or hybrid serving based on documented latency and completion requirements.
- [ ] **SERVE-003** `P2` Document whether inference uses a managed provider endpoint, self-hosted runtime, on-device model, or provider routing.
- [ ] **SERVE-004** `P2` Identify the approved model artifact or provider snapshot, tokenizer, runtime, and relevant prompt and safety configurations.
- [ ] **SERVE-005** `P1` Verify model weight, adapter, quantization, and runtime compatibility before loading the production artifact.
- [ ] **SERVE-006** `P2` Record GPU or accelerator type, CPU, memory, storage, interconnect, and regional capacity requirements for each deployment.
- [ ] **SERVE-007** `P1` Measure peak accelerator memory including model weights, temporary buffers, key-value caches, and realistic concurrent contexts.
- [ ] **SERVE-008** `P1` Validate readiness and liveness behavior during model downloads, compilation, initialization, warm-up, and degraded health.
- [ ] **SERVE-009** `P2` Document cold-start latency, scale-from-zero consequences, minimum warm capacity, and prewarming requirements where applicable.
- [ ] **SERVE-010** `P1` Size replicas, model instances, partitions, or parallel workers using measured request distributions and available resources.
- [ ] **SERVE-011** `P1` Evaluate tensor, pipeline, data, or expert parallelism only when the chosen runtime and hardware support them reliably.
- [ ] **SERVE-012** `P2` Define request routing across providers, model versions, hardware pools, and regions with explicit authority and fallback constraints.
- [ ] **SERVE-013** `P1` Set capacity reservations and autoscaling minima and maxima based on realistic peaks and provider quotas.
- [ ] **SERVE-014** `P1` Use suitable scaling signals such as queue depth, tokens per second, active sequences, or accelerator utilization when supported.
- [ ] **SERVE-015** `P1` Test scaling lag, resource provisioning, model startup, and warm-up against burst and sustained-load scenarios.
- [ ] **SERVE-016** `P2` Define ingress, egress, network isolation, credential scope, and regional processing controls for all serving components.
- [ ] **SERVE-017** `P1` Separate public, internal, tenant-specific, and privileged inference routes with appropriate authorization.
- [ ] **SERVE-018** `P1` Verify the serving stack accepts only approved model packages and rejects untrusted artifact paths or unsafe loading methods.
- [ ] **SERVE-019** `P2` Record deployment artifact digests, model aliases, container images, configuration, and ownership in the release manifest.
- [ ] **SERVE-020** `P1` Estimate baseline and peak operating costs, capacity costs, provider quotas, and the economics of reserved versus elastic serving.
- [ ] **SERVE-021** `P2` Document operating requirements for high availability, regional isolation, maintenance windows, and infrastructure dependencies.
- [ ] **SERVE-022** `P1` Test deployment reproducibility in a production-equivalent environment and reconcile running versions with the approved manifest.

## Latency and throughput

- [ ] **SERVE-023** `P2` Define application-specific p50, p95, and p99 latency, time-to-first-output, throughput, and task-success budgets.
- [ ] **SERVE-024** `P1` Measure end-to-end user latency separately from serving-only compute latency and provider network delay.
- [ ] **SERVE-025** `P1` Instrument queue wait, preprocessing, model prefill, decode, postprocessing, streaming, and downstream validation times where supported.
- [ ] **SERVE-026** `P1` Use realistic distributions of input tokens, output tokens, image sizes, audio duration, and concurrent requests in load tests.
- [ ] **SERVE-027** `P1` Report prefilling and decoding performance separately for autoregressive models where these dominate latency.
- [ ] **SERVE-028** `P1` Calculate tokens per second and successful requests per second with precise denominators and counting rules.
- [ ] **SERVE-029** `P1` Test minimum, typical, long-context, maximum-supported, and malformed request sizes against actual runtime limits.
- [ ] **SERVE-030** `P1` Benchmark steady-state, burst, ramp-up, and sudden-spike traffic, including cold starts and scale events.
- [ ] **SERVE-031** `P1` Measure latency under saturation and identify the throughput knee where queueing or error rates become unacceptable.
- [ ] **SERVE-032** `P1` Include real preprocessing, tokenization, retrieval, content filtering, and structured-output checks when testing total workload.
- [ ] **SERVE-033** `P1` Compare models, quantization, compilation, and optimization variants using equivalent datasets and acceptable task-quality thresholds.
- [ ] **SERVE-034** `P1` Test queue scheduling, request priorities, fairness, and starvation risk across long and short generations.
- [ ] **SERVE-035** `P1` Set bounded waiting time, admission control, and queue-length policies to avoid memory exhaustion under overload.
- [ ] **SERVE-036** `P1` Measure cancel/disconnect cleanup so abandoned requests stop occupying expensive resources where the runtime supports cancellation.
- [ ] **SERVE-037** `P1` Check autoscaling targets against token-based serving capacity rather than relying solely on generic CPU metrics where insufficient.
- [ ] **SERVE-038** `P1` Validate inference behavior under concurrent batches, multiple model instances, and shared accelerator resources.
- [ ] **SERVE-039** `P1` Use separate load profiles for interactive, batch, background, and high-priority requests where they share infrastructure.
- [ ] **SERVE-040** `P2` Record performance test hardware, software, runtime flags, model versions, warm-up, load-generator settings, and sample counts.
- [ ] **SERVE-041** `P1` Compare tail latency and cost per completed task before approving a change that raises aggregate throughput.
- [ ] **SERVE-042** `P1` Test provider rate limits, local overload thresholds, backpressure, and client retry behavior at expected peak demand.
- [ ] **SERVE-043** `P1` Validate performance metrics are traceable to exact model and serving configuration rather than mixed unlabelled deployments.
- [ ] **SERVE-044** `P1` Rebenchmark after model weights, context limits, batch scheduler, cache design, routing, or infrastructure change.
- [ ] **SERVE-045** `P1` Monitor inference quality alongside performance, because a faster but materially degraded response is not a successful optimization.
- [ ] **SERVE-046** `P2` Document realistic capacity headroom and response plans when forecast growth exceeds safe serving limits.

## Batching, streaming, and caching

- [ ] **SERVE-047** `P1` Select dynamic, static, continuous, sequence-aware, or no batching according to model state and supported serving-runtime behavior.
- [ ] **SERVE-048** `P1` Test maximum batch size, scheduler delay, and queue deadlines against both throughput gains and tail-latency budgets.
- [ ] **SERVE-049** `P1` Check that incompatible tensor shapes, modalities, model revisions, or request parameters are not incorrectly batched together.
- [ ] **SERVE-050** `P1` Verify stateful sequences retain correct request order and session isolation when sequence batching is used.
- [ ] **SERVE-051** `P1` Measure batching behavior with mixed prompt lengths and output sizes instead of only uniform synthetic payloads.
- [ ] **SERVE-052** `P1` Test fairness and priority behavior when short interactive requests compete with long batch generations.
- [ ] **SERVE-053** `P1` Ensure canceling a request in a batch does not corrupt or prematurely stop unrelated requests.
- [ ] **SERVE-054** `P1` Validate streamed text or media chunk ordering, framing, finalization markers, and partial-output semantics.
- [ ] **SERVE-055** `P1` Test streaming interruptions, client disconnects, network proxies, buffer behavior, and backpressure under load.
- [ ] **SERVE-056** `P1` Distinguish partial streamed content from accepted, complete, validated responses in API and user interfaces.
- [ ] **SERVE-057** `P1` Check tool-triggering or irreversible downstream actions are not authorized solely on partial unvalidated streamed output.
- [ ] **SERVE-058** `P2` Define which caches are allowed: response, embedding, tokenizer, prefix/KV, retrieval, or model artifact caches.
- [ ] **SERVE-059** `P1` Verify cache keys account for model, prompt, policy, tenant, permission scope, and other correctness-relevant versions.
- [ ] **SERVE-060** `P1` Prevent cache reuse from exposing protected prompts, responses, session histories, or retrieval context across tenants.
- [ ] **SERVE-061** `P1` Test cache hit, miss, eviction, warm-up, and invalidation behavior with changing permissions and model versions.
- [ ] **SERVE-062** `P1` Measure cache memory pressure and eviction effects on concurrent requests and long-context serving.
- [ ] **SERVE-063** `P1` Validate whether prefix caching improves prefill performance for the workload; do not assume it accelerates token generation.
- [ ] **SERVE-064** `P1` Review cache persistence, deletion, and data residency against retention and privacy requirements.
- [ ] **SERVE-065** `P1` Check speculative decoding, quantization, or other acceleration options against output quality and compatibility before enabling them.
- [ ] **SERVE-066** `P1` Ensure cached and uncached requests produce acceptable results and correct billing, usage, and attribution metadata.
- [ ] **SERVE-067** `P1` Handle batching and streaming errors so one malformed result does not leak or poison another user's output.
- [ ] **SERVE-068** `P2` Record scheduler, cache, batching, and streaming configuration in the deployment manifest for reproducible tests.
- [ ] **SERVE-069** `P1` Apply independent concurrency, output length, context size, and spend limits even when batching or cache optimizations are enabled.
- [ ] **SERVE-070** `P1` Test batch-job deduplication, checkpoint/restart, partial results, and resumable output for supported offline workloads.

## Fallbacks and operational resilience

- [ ] **SERVE-071** `P2` Specify service-level availability, recovery objectives, and acceptable degraded behavior for each critical inference journey.
- [ ] **SERVE-072** `P2` Identify failure dependencies including model providers, accelerators, storage, networking, authentication, retrieval, and moderation services.
- [ ] **SERVE-073** `P2` Define responses to provider outage, regional loss, model-load failure, OOM, resource exhaustion, and sustained queue overload.
- [ ] **SERVE-074** `P1` Use bounded retries with jitter/backoff and retry budgets that avoid multiplying inference costs or tool side effects.
- [ ] **SERVE-075** `P1` Return explicit overload, timeout, unsupported-input, quota, and temporarily unavailable states through appropriate contracts.
- [ ] **SERVE-076** `P2` Define circuit-breaker, admission-control, load-shedding, and provider failover behavior based on tested failure signals.
- [ ] **SERVE-077** `P1` Verify fallback models support required modalities, output schemas, languages, context length, and safety constraints.
- [ ] **SERVE-078** `P1` Ensure fallback routing does not bypass user authorization, data residency, consent, or approved processing providers.
- [ ] **SERVE-079** `P1` Test failure when a fallback has lower context capacity or different tokenization and formatting semantics.
- [ ] **SERVE-080** `P1` Recheck guardrails and tool permissions after model/provider switching rather than assuming a fallback inherits them.
- [ ] **SERVE-081** `P2` Define safe refusal or non-AI service alternatives when no approved model can complete a request.
- [ ] **SERVE-082** `P1` Test release canary, traffic shifting, rollback, and health gating using the actual serving mode and orchestrator version.
- [ ] **SERVE-083** `P1` Protect existing sessions, streaming responses, and batch jobs during rolling restarts and model replacement.
- [ ] **SERVE-084** `P1` Confirm the previous approved model artifact, runtime dependencies, and routing configuration can be restored when rollback is required.
- [ ] **SERVE-085** `P1` Test abrupt worker termination and recovery without duplicate payments, messages, or other model-driven external actions.
- [ ] **SERVE-086** `P1` Validate emergency disablement, provider credential revocation, and traffic drain under simulated incidents.
- [ ] **SERVE-087** `P1` Monitor safe service identifiers, model revisions, failure rates, accelerator memory, queue depth, throughput, and token usage.
- [ ] **SERVE-088** `P1` Configure alerts for service loss, tail-latency regression, excessive failures, unexpected billable usage, and critical guardrail outages.
- [ ] **SERVE-089** `P2` Maintain runbooks for capacity exhaustion, faulty model rollout, cache corruption, and provider-specific errors.
- [ ] **SERVE-090** `P2` Assign an on-call owner, escalation route, incident severity, and recovery decision authority to each critical inference service.
- [ ] **SERVE-091** `P1` Conduct a production-equivalent failure exercise and record corrective actions, evidence, and retest before launch.
- [ ] **SERVE-092** `P1` Retire unsupported or unsafe serving configurations with dependent-client notices, approved data disposal, and updated registries.

## Frontend Checks

*Apply these client-side checks only when the AI feature has a user-facing or reviewer-facing interface. They remain part of this AI domain; the general frontend checklist inventory is separate.*

- [ ] **SERVE-113** `P1` Measure user-perceived time to first meaningful content and total task completion, not only server inference latency.
- [ ] **SERVE-114** `P1` Clearly communicate loading, queued, generating, paused, timed-out, and failed inference states.
- [ ] **SERVE-115** `P1` Show streamed partial output as provisional until the required validation and safety checks complete.
- [ ] **SERVE-116** `P1` Preserve readable streaming order, focus behavior, and screen-reader announcements for dynamic generated content.
- [ ] **SERVE-117** `P1` Offer cancellation and retry controls that actually cancel or deduplicate server work when supported.
- [ ] **SERVE-118** `P1` Explain error and recovery paths for provider outages, rate limits, unsupported inputs, and model fallback.
- [ ] **SERVE-119** `P1` Check that fallback does not misleadingly promise the same model capabilities, language, or quality guarantees.
- [ ] **SERVE-120** `P1` Prevent model credentials, privileged endpoint configuration, and hidden prompt data from appearing in browser assets.
- [ ] **SERVE-121** `P1` Render generated markup, tool results, and attached output files safely without executable script injection.
- [ ] **SERVE-122** `P2` Maintain accurate completion or action-confirmation status when streams disconnect or clients reload.
- [ ] **SERVE-123** `P1` Verify that old browser tabs and cached frontend versions handle current inference schemas and model routing.
- [ ] **SERVE-124** `P1` Test representative mobile, slow-network, and high-latency journeys for progress visibility and usable timeouts.
- [ ] **SERVE-125** `P1` Validate responsive layouts for long outputs, multilingual text, tables, code blocks, and multimodal responses.
- [ ] **SERVE-126** `P1` Check user-accessible controls for maximum upload size, generation length, and cost-sensitive actions where relevant.
- [ ] **SERVE-127** `P1` Prevent browser caches or service workers from exposing another user's private AI responses after account changes.
- [ ] **SERVE-128** `P1` Ensure user feedback and error-reporting interfaces capture safe model/version context without unapproved prompt logging.
- [ ] **SERVE-129** `P1` Keep provenance, uncertainty, and citation indicators accurate after provider or model changes where relevant.
- [ ] **SERVE-130** `P1` Require proper confirmation for consequential external actions regardless of inference speed or streaming progress.
- [ ] **SERVE-131** `P1` Verify UI feature flags track approved model cohorts and support immediate safe disablement and rollback.
- [ ] **SERVE-132** `P1` Include important user-task and accessibility checks in serving release validation, not just inference throughput tests.

## Release gate

- [ ] The exact serving artifact, model/provider version, supported interface, deployment topology, data policy, and responsible owners are documented and approved.
- [ ] Capacity, startup/warm-up, saturation, autoscaling, cost, and resource-headroom tests meet the expected traffic envelope and agreed budgets.
- [ ] End-to-end p95/p99 latency, first-output latency where applicable, task success, and throughput pass predeclared criteria with production-like request lengths and concurrency.
- [ ] Batching, streaming, and caching configurations preserve tenant isolation, response correctness, state integrity, and downstream action safeguards where used.
- [ ] Authentication, resource authorization, per-tenant limits, request validation, model-package integrity, and network controls have passed security checks.
- [ ] Overload, provider outage, resource exhaustion, cancellation, fallback, regional fault, and rollback scenarios have tested safe outcomes.
- [ ] Relevant API and frontend consumers correctly handle model revisions, partial outputs, overload/error states, privacy controls, and degraded-capability messaging.
- [ ] Monitoring, on-call escalation, emergency disablement, approved failover, incident recovery, and any remaining risk acceptances are signed off for the exact release.

**Domain-specific approval rule:** Block release when inference can disclose protected cross-tenant content, invoke unapproved actions, exceed materially unbounded resource limits, fail to meet essential capacity or latency needs, or leave critical users without a tested safe outage/fallback path. Benchmark throughput is not a substitute for task quality, accessibility, compliance review, or service reliability.

**Optional tooling:** [AI-scope testing examples](../references/optional-testing-tools-ai.md#12_ai_inference_and_serving), not prerequisites or evidence of PASS.

## Trusted references and scope

The following primary runtime documentation, operational guidance, and security resources support the project-level review questions. Treat individual serving features as conditional on the version and deployment mode actually used.

- [NVIDIA Triton — Dynamic batching](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/batcher.html) — batching, queue delay, sequence behavior, latency-throughput tradeoffs.
- [NVIDIA Triton — Rate limiter](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/rate_limiter.html) — model-level scheduling priorities and resource admission limits.
- [NVIDIA Triton — Performance Analyzer](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/README.html) — concurrency/request-rate benchmarking and performance test setup.
- [vLLM — Serving configuration](https://docs.vllm.ai/en/latest/cli/serve/) — LLM serving parameters and scheduler, KV-cache, and request configuration.
- [vLLM — Automatic prefix caching](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/) — shared-prefix KV caching, workload-dependent prefill benefits, and cache limits.
- [vLLM — Production metrics](https://docs.vllm.ai/en/latest/usage/metrics/) — queue, throughput, token, and inference runtime observability.
- [KServe — Serving runtimes overview](https://kserve.github.io/website/docs/model-serving/predictive-inference/frameworks/overview) — model-serving architectures, autoscaling, routing, telemetry, and mode-specific capabilities.
- [KServe — Predictive inference canary rollout](https://kserve.github.io/website/docs/next/model-serving/predictive-inference/rollout-strategies/canary) — progressive traffic release and rollback; supported modes vary with KServe version.
- [Kubernetes — Horizontal Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) — resource/custom-metric scaling controllers and scale-up/scale-down behavior.
- [Amazon SageMaker AI — Real-time inference](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html) — managed serving endpoints, autoscaling, runtime configurations, and deployment constraints.
- [Google SRE — Handling overload](https://sre.google/sre-book/handling-overload/) — admission control, overload protection, client throttling, and graceful degradation.
- [OpenTelemetry — GenAI inference conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/client-inference.md) — model/provider identity, inference tracing, usage metrics, and opt-in sensitive-content capture.
- [OWASP API Security Top 10 (2023)](https://api-security.owasp.org/editions/2023/en/0x00-header/) — authorization, resource exhaustion, authentication, and API-side protection.

**Applicability:** Triton dynamic batching applies to supported workload/model types; batching may improve throughput while increasing queueing latency. vLLM prefix/KV caching principally helps shared-prefix *prefill*, not every workload's decode throughput, and cache isolation must be validated independently. KServe serving modes and canary APIs differ between releases; its documentation for standard versus serverless mode may lag implementation changes, so confirm the exact deployed version and feature gates. Kubernetes HPA alone does not guarantee capacity during long model cold starts. NVIDIA Perf Analyzer documentation notes that `genai-perf` is being deprecated in favor of `AIPerf`; check benchmark tool support. OpenTelemetry GenAI semantic conventions have moved to their own repository and remain subject to schema/version changes; prompt and response collection is sensitive and generally opt-in. OWASP's API risk list is guidance rather than certification.

**Source review date:** 2026-11-12.
