# 27 — Performance and Scalability Checklist

> Verify that priority user experiences and services meet documented latency, throughput, capacity, and efficiency objectives at realistic demand. Separate browser metrics from backend metrics; avoid treating a single benchmark as production capacity proof.

> **Scope: Backend / API-specific.** This file is one part of the 27_Performance_and_Scalability.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Performance budgets and measurements


- [ ] **PERF-004** `P2` Identify production and representative test populations, workloads, regions, devices, network conditions, and data volumes.

## Backend throughput and capacity


- [ ] **PERF-024** `P1` Include cold-start and warm-start scenarios when runtime initialization or autoscaling affects latency.
- [ ] **PERF-025** `P1` Measure saturation of CPU, memory, disk I/O, network, thread pools, and connection pools where relevant.
- [ ] **PERF-026** `P1` Evaluate query execution plans and measured query timings for high-cost database reads and writes.
- [ ] **PERF-030** `P1` Test critical cache invalidation or stale-data conditions where optimization can affect correctness.
- [ ] **PERF-031** `P1` Measure queue depth, consumer lag, job duration, and retry volume for asynchronous workloads.
- [ ] **PERF-033** `P1` Verify expensive work is canceled or bounded when clients disconnect or request deadlines expire.

- [ ] **PERF-017** `P1` Model the mix of reads, writes, background work, and high-cost operations observed or forecast in real workloads.
- [ ] **PERF-018** `P1` Include authenticated roles, tenant sizes, object sizes, and representative query parameters in load profiles.
- [ ] **PERF-019** `P1` Execute a smoke test of the performance harness before conducting larger runs.
- [ ] **PERF-020** `P1` Test expected steady-state load and compare response times, throughput, and errors with agreed thresholds.
- [ ] **PERF-021** `P1` Test anticipated peak traffic and sudden bursts, including connection establishment and authentication overhead.
- [ ] **PERF-022** `P1` Run stress tests to identify the point at which latency, errors, or resource saturation exceed acceptable limits.
- [ ] **PERF-023** `P1` Run soak/endurance tests long enough to expose memory leaks, connection leaks, fragmentation, or accumulating queues.
- [ ] **PERF-027** `P1` Check indexing, query selectivity, pagination, and avoidance of unnecessary repeated queries in high-volume paths.
- [ ] **PERF-028** `P1` Measure transaction lock contention, deadlocks, and concurrency effects for write-heavy workflows.
- [ ] **PERF-029** `P1` Confirm caches have suitable keys, eviction/expiry rules, hit rates, and behavior during cold starts or failures.
- [ ] **PERF-032** `P1` Exercise timeouts, bounded retries, backpressure, rate limiting, and load shedding under dependency saturation.
- [ ] **PERF-034** `P1` Test graceful degradation and recovery after overload without indefinite backlog growth.
- [ ] **PERF-035** `P1` Measure performance of external dependencies and enforce contractual or permission limits during tests.
- [ ] **PERF-036** `P1` Compare production capacity forecasts with observed usage and prior load-test results.

## Client performance


- [ ] **PERF-041** `P2` Record page-load request count, transferred bytes, decoded resource size, and major blocking dependencies.
- [ ] **PERF-042** `P1` Measure time to first byte and the contribution of redirects, DNS, connection setup, and backend work to initial loading.

## Scaling and efficiency


- [ ] **PERF-063** `P1` Model the cost per request, transaction, active user, or job at expected and peak demand.

- [ ] **PERF-053** `P1` Estimate capacity needs using peak forecasts, observed growth, seasonal demand, and planned launches.
- [ ] **PERF-054** `P2` Document scaling units, bottleneck resources, quota limits, and the conditions triggering additional capacity.
- [ ] **PERF-055** `P1` Validate autoscaling thresholds and scale-out/scale-in behavior under realistic traffic changes when autoscaling is used.
- [ ] **PERF-056** `P1` Account for provisioning and warm-up delays so scaling begins early enough to protect user experience.
- [ ] **PERF-057** `P1` Check that stateless services can add or remove instances without losing essential user or workflow state.
- [ ] **PERF-058** `P1` Test load-balancer distribution, connection pooling, and uneven traffic/hot-key conditions.
- [ ] **PERF-059** `P2` Maintain headroom for expected failures or maintenance consistent with the service's availability objectives.
- [ ] **PERF-060** `P1` Evaluate regional latency and content delivery paths where users are geographically distributed.
- [ ] **PERF-061** `P1` Check that caches and CDNs improve latency without serving unauthorized, private, or misleadingly stale content.
- [ ] **PERF-062** `P1` Verify data partitioning, replication, and storage scaling strategies for projected dataset growth if applicable.
- [ ] **PERF-064** `P1` Compare right-sizing, caching, batching, compression, and concurrency tuning using measured outcomes.
- [ ] **PERF-065** `P1` Ensure background processing cannot starve customer-facing requests or saturate shared resources.
- [ ] **PERF-066** `P1` Test how system behavior changes when a dependency is throttled or unavailable, including backlog recovery.
- [ ] **PERF-067** `P1` Assess sustainable resource use, including idle overprovisioning and unnecessary repeated computation.
- [ ] **PERF-068** `P2` Define alerts for capacity exhaustion, budget violations, unusual resource growth, and deteriorating tail latency.
- [ ] **PERF-069** `P1` Review and update performance forecasts after release or major changes to user demand or architecture.

## API Checks


- [ ] **PERF-070** `P2` Document traffic profiles and budgets for each critical API endpoint, operation class, and consumer.
- [ ] **PERF-071** `P1` Measure p50, p95, and p99 latency together with requests per second and status-code distributions under representative load.
- [ ] **PERF-072** `P1` Test authorization and authenticated workloads instead of benchmarking only unauthenticated happy paths.
- [ ] **PERF-073** `P1` Include realistic payload sizes, nested objects, query combinations, and large-response cases in API benchmarks.
- [ ] **PERF-074** `P1` Validate that pagination, filtering, and sorting prevent unbounded response sizes and excessive database work.
- [ ] **PERF-075** `P1` Measure effects of serialization, compression, schema validation, and gateway middleware on response times.
- [ ] **PERF-076** `P2` Identify N+1 requests, excessive fan-out, and chained downstream calls on latency-critical operations.
- [ ] **PERF-077** `P1` Enforce and verify request deadlines, upstream timeouts, concurrency limits, and cancellation propagation.
- [ ] **PERF-078** `P1` Test rate limits, quotas, backpressure, and appropriate retry guidance under controlled overload.
- [ ] **PERF-079** `P1` Confirm that retries and idempotency do not amplify server load or duplicate expensive actions.
- [ ] **PERF-080** `P1` Benchmark bulk APIs, asynchronous jobs, and streaming endpoints using appropriate throughput and completion metrics.
- [ ] **PERF-081** `P1` Check connection pooling, keep-alive behavior, and TLS overhead where they materially affect workload capacity.
- [ ] **PERF-082** `P1` Verify API cache semantics, private response isolation, cache-key correctness, and safe invalidation.
- [ ] **PERF-083** `P1` Test sustained traffic to detect queue growth, memory retention, and connection exhaustion.
- [ ] **PERF-084** `P1` Ensure performance tests exclude non-owned third-party services unless permission and safe limits have been agreed.
- [ ] **PERF-085** `P1` Observe endpoint-level latency, error rates, saturation, and dependencies during staged releases.
- [ ] **PERF-086** `P1` Verify public API contract changes do not silently alter pagination limits, timeout behavior, or payload-size expectations.
- [ ] **PERF-087** `P1` Confirm heavy requests and expensive queries cannot exhaust shared capacity at the expense of other consumers.

## Release gate


- [ ] Performance budgets, workload assumptions, target cohorts, and accountable owners are defined for the release's critical journeys and endpoints.
- [ ] Representative baseline and relevant peak-load tests meet documented latency, throughput, error-rate, and saturation criteria, with acknowledged test-environment limitations.
- [ ] Major backend or database bottlenecks, cache behavior, and overload/recovery paths are measured and either addressed or accepted with authorized risk ownership.
- [ ] Applicable frontend routes have measured Core Web Vitals or equivalent user-centric measures, and critical interaction regressions have been reviewed.
- [ ] Expected peak/growth demand has a documented capacity plan, scaling constraints, monitoring signals, and safe response to saturation.
- [ ] No unresolved critical performance failure jeopardizes core tasks or overload recovery without an explicit, time-bound acceptance and mitigation plan.

**Domain-specific approval rule:** Block performance sign-off when material latency or capacity targets are missing, critical workflows breach agreed thresholds without approved mitigation, overload causes uncontrolled failure, or regressions remain unowned. Benchmarks and Web Vitals are context-dependent; meeting a public threshold is not a universal performance guarantee.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#27_performance_and_scalability), not prerequisites or verification evidence.

## Trusted references and scope


These actionable checks are informed by the following primary engineering and standards sources; they do not reproduce the source publications or imply certification.

- [AWS Well-Architected Framework — Performance Efficiency Pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/) — workload selection, load testing, resource efficiency, and continual improvement.
- [AWS Well-Architected — Performance process and culture](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/process-and-culture.html) — measurement, automated performance tests, and performance tuning.
- [Google SRE — Production Services Best Practices](https://sre.google/sre-book/service-best-practices/) — forecasting, measured capacity, and overload behavior.
- [Google SRE — Handling Overload](https://sre.google/sre-book/handling-overload/) — backpressure, throttling, and overload defenses.
- [Grafana k6 — Load Testing Websites](https://grafana.com/docs/k6/latest/testing-guides/load-testing-websites/) — realistic traffic profiles, backend versus browser testing, and test scope.
- [Grafana k6 — Automated Performance Testing](https://grafana.com/docs/k6/latest/testing-guides/automated-performance-testing/) — smoke, average-load, stress, spike, and soak test planning.
- [web.dev — Web Vitals](https://web.dev/articles/vitals) — LCP, INP, CLS, 75th-percentile thresholds, and field measurement.
- [web.dev — Learn Performance](https://web.dev/learn/performance/) — loading, code splitting, image loading, and client responsiveness.
- [OpenTelemetry — Metrics](https://opentelemetry.io/docs/concepts/signals/metrics/) — request latency, throughput, resource utilization, and telemetry cardinality.
- [PostgreSQL — Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) — query planning and database bottleneck analysis when PostgreSQL is used.
- [MDN — HTTP Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) — browser and shared cache semantics, freshness, and private responses.

**Applicability:** Apply web-specific metrics only to applicable web experiences. Current commonly used Core Web Vitals 'good' thresholds are LCP at or below 2.5 seconds, INP at or below 200 milliseconds, and CLS at or below 0.1, assessed at the 75th percentile of real-user page loads for mobile and desktop separately; verify current official guidance when reviewing. PostgreSQL, cloud-native autoscaling, CDN, and asynchronous queue checks apply only if the architecture uses them. Never perform high-volume tests against infrastructure or third-party services without authorization.

**Source review date:** 2026-11-12.
