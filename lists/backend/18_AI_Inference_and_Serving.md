# 18 — AI Inference and Serving Checklist

> Verify that production AI inference is deployable, secure, performant, cost-bounded, and recoverable under realistic workloads. Serving improvements must be measured against user-visible quality and latency; faster execution or higher aggregate throughput does not by itself establish a release-ready system.

> **Scope: Backend / API-specific.** This file is one part of the 18_AI_Inference_and_Serving.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## API Checks

- [ ] **SERVE-093** `P1` Authenticate inference endpoints and authorize each user, tenant, model, and permitted operation independently of model responses.
- [ ] **SERVE-094** `P1` Validate request modality, schemas, encoding, context length, token limits, and file sizes before scheduling inference.
- [ ] **SERVE-095** `P1` Restrict supported model selection and tool capabilities using server-owned allowlists rather than caller-controlled arbitrary identifiers.
- [ ] **SERVE-096** `P1` Expose documented version, response-schema, input-limit, and compatibility behavior for every supported inference route.
- [ ] **SERVE-097** `P1` Test HTTP and streaming errors for invalid inputs, policy refusal, overload, timeout, provider failure, and canceled requests.
- [ ] **SERVE-098** `P1` Enforce per-user and per-tenant rate, concurrency, token, and spend limits before placing work on expensive serving queues.
- [ ] **SERVE-099** `P1` Apply quota isolation or fairness so one tenant's large requests cannot starve other authorized users.
- [ ] **SERVE-100** `P1` Validate partial streaming chunks and final completion indicators against published API contracts.
- [ ] **SERVE-101** `P1` Keep pending, partial, complete, and failed asynchronous inference job states distinct and retrievable by authorized clients.
- [ ] **SERVE-102** `P1` Use idempotency keys or authoritative reconciliation for retries that could trigger non-idempotent downstream effects.
- [ ] **SERVE-103** `P1` Ensure provider tokens, model registry credentials, private prompts, and sensitive output are not exposed in API diagnostics.
- [ ] **SERVE-104** `P1` Test cache isolation, expiration, deletion, and invalidation across accounts, authorization changes, and model promotions.
- [ ] **SERVE-105** `P1` Verify applied model version, provider, route, token usage, and safe request correlation are observable for incidents.
- [ ] **SERVE-106** `P1` Protect access to health, telemetry, debugging, model-loading, and administrative endpoints according to their sensitivity.
- [ ] **SERVE-107** `P1` Apply TLS and approved network controls between inference gateway, service mesh, model runtimes, and external providers.
- [ ] **SERVE-108** `P1` Test compatibility of batch, synchronous, and streaming clients with rollout and rollback behavior.
- [ ] **SERVE-109** `P1` Prevent model-generated structured outputs or tool calls from bypassing separate schema validation and authorization.
- [ ] **SERVE-110** `P1` Validate abort, timeout, and cancellation semantics free queued or running resources where feasible.
- [ ] **SERVE-111** `P1` Run representative production-equivalent API load and policy tests before deploying a new model or runtime.
- [ ] **SERVE-112** `P1` Confirm API behavior under cross-region failover, fallback model selection, and complete approved-capacity exhaustion.

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

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#18_ai_inference_and_serving), not prerequisites or verification evidence.

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
