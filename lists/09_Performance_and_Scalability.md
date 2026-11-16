# 09 — Performance and Scalability Checklist

> Verify that priority user experiences and services meet documented latency, throughput, capacity, and efficiency objectives at realistic demand. Separate browser metrics from backend metrics; avoid treating a single benchmark as production capacity proof.

> **Scope: Shared / cross-cutting.** This file is one part of the 09_Performance_and_Scalability.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](references/review-method.md) · [Optional framework crosswalk](references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Performance budgets and measurements



- [ ] **PERF-001** `P2` Define performance objectives for the most important user journeys and system operations, including measurement units and owner.
- [ ] **PERF-002** `P1` Set measurable budgets for latency, throughput, error rate, resource use, and user-perceived responsiveness appropriate to the product.
- [ ] **PERF-003** `P2` Specify response-time percentiles (such as p50, p95, and p99) instead of relying only on arithmetic averages.
- [ ] **PERF-005** `P2` Define acceptable latency and error behavior for steady-state traffic, peak periods, and anticipated growth.
- [ ] **PERF-006** `P2` Record baseline measurements for critical journeys and endpoints before major performance work.
- [ ] **PERF-007** `P1` Distinguish end-user elapsed time from server processing, queuing, network, rendering, and third-party dependency time.
- [ ] **PERF-008** `P1` Instrument enough spans, metrics, and structured events to identify the dominant latency contributor without exposing sensitive data.
- [ ] **PERF-009** `P1` Set meaningful service-level objectives or performance acceptance criteria where operationally appropriate.
- [ ] **PERF-010** `P2` Document the target test environment's differences from production and how each affects interpretation of results.
- [ ] **PERF-011** `P1` Use representative synthetic or anonymized datasets, including realistic record counts, sizes, and distribution.
- [ ] **PERF-012** `P2` Define performance regression thresholds and compare results against the same test methodology and environment.
- [ ] **PERF-013** `P2` Track performance by build or release version so regressions can be associated with changes.
- [ ] **PERF-014** `P1` Measure resource utilization and saturation alongside user-facing metrics to avoid celebrating throughput that harms reliability.
- [ ] **PERF-015** `P2` Document testing methods, tool versions, traffic models, warm-up periods, and statistical limitations for repeatability.
- [ ] **PERF-016** `P2` Assign an owner and due date for each material violation of a budget or service-level target.

## Release gate



- [ ] Performance budgets, workload assumptions, target cohorts, and accountable owners are defined for the release's critical journeys and endpoints.
- [ ] Representative baseline and relevant peak-load tests meet documented latency, throughput, error-rate, and saturation criteria, with acknowledged test-environment limitations.
- [ ] Major backend or database bottlenecks, cache behavior, and overload/recovery paths are measured and either addressed or accepted with authorized risk ownership.
- [ ] Applicable frontend routes have measured Core Web Vitals or equivalent user-centric measures, and critical interaction regressions have been reviewed.
- [ ] Expected peak/growth demand has a documented capacity plan, scaling constraints, monitoring signals, and safe response to saturation.
- [ ] No unresolved critical performance failure jeopardizes core tasks or overload recovery without an explicit, time-bound acceptance and mitigation plan.

**Domain-specific approval rule:** Block performance sign-off when material latency or capacity targets are missing, critical workflows breach agreed thresholds without approved mitigation, overload causes uncontrolled failure, or regressions remain unowned. Benchmarks and Web Vitals are context-dependent; meeting a public threshold is not a universal performance guarantee.

**Optional tooling:** [File-specific tool examples](references/optional-testing-tools-shared.md#09_performance_and_scalability), not prerequisites or verification evidence.

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
