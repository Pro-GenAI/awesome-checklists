# 12 — Performance and Scalability Checklist

> Verify that priority user experiences and services meet documented latency, throughput, capacity, and efficiency objectives at realistic demand. Separate browser metrics from backend metrics; avoid treating a single benchmark as production capacity proof.

> **Scope: Frontend-specific.** This file is one part of the 12_Performance_and_Scalability.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Client performance


- [ ] **PERF-038** `P1` Measure Largest Contentful Paint (LCP), Interaction to Next Paint (INP), and Cumulative Layout Shift (CLS) for eligible web experiences.
- [ ] **PERF-043** `P2` Identify the actual LCP element and reduce bottlenecks in its discovery, fetch priority, and rendering.
- [ ] **PERF-044** `P1` Reduce unnecessary JavaScript execution, long main-thread tasks, and expensive event handlers affecting responsiveness.
- [ ] **PERF-046** `P1` Use efficient image formats, responsive sources, explicit dimensions, and appropriate compression for target devices.
- [ ] **PERF-048** `P1` Optimize font loading, subsets, fallbacks, and layout behavior to avoid unnecessary blocking or visual shifts.
- [ ] **PERF-049** `P1` Reserve space for images, ads, embedded media, and asynchronous UI to limit unexpected layout shifts.

- [ ] **PERF-037** `P2` Identify representative page templates and critical interactions for field and laboratory measurements.
- [ ] **PERF-039** `P1` Assess Core Web Vitals at the 75th percentile separately for mobile and desktop, using current recommended thresholds or explicit project targets.
- [ ] **PERF-040** `P1` Distinguish real-user field measurements from controlled laboratory results and investigate important disagreements.
- [ ] **PERF-045** `P1` Apply route- or feature-level code splitting when it measurably reduces critical startup work.
- [ ] **PERF-047** `P1` Defer below-the-fold media and third-party resources where doing so does not delay critical content.
- [ ] **PERF-050** `P1` Measure hydration and client-rendering cost for relevant server-rendered or hybrid pages.
- [ ] **PERF-051** `P1` Inspect network waterfalls to remove redundant requests and unnecessary render-blocking dependencies.
- [ ] **PERF-052** `P1` Verify that changes improving metrics do not remove required accessibility, usability, or essential functionality.

## Frontend Checks


- [ ] **PERF-088** `P1` Measure field LCP, INP, and CLS for key routes, segmented by device class and relevant user cohorts.
- [ ] **PERF-089** `P1` Compare lab performance under defined network and CPU throttling with observed real-user results.
- [ ] **PERF-090** `P1` Ensure the primary content and key action are visible without waiting for avoidable noncritical scripts.
- [ ] **PERF-091** `P1` Check that critical images, fonts, styles, and scripts are prioritized correctly during initial loading.
- [ ] **PERF-092** `P1` Use responsive images, modern formats, compression, and appropriate dimensions for content images.
- [ ] **PERF-093** `P1` Lazy-load below-the-fold assets where appropriate without lazy-loading essential above-the-fold content.
- [ ] **PERF-094** `P1` Limit initial JavaScript and remove unused packages or code that delays interaction.
- [ ] **PERF-095** `P1` Break up expensive main-thread work and optimize input, event handlers, and rendering paths affecting INP.
- [ ] **PERF-096** `P1` Avoid redundant hydration, cascading state updates, and large synchronous calculations in common interactions.
- [ ] **PERF-097** `P1` Reserve layout dimensions for delayed content and test dynamic banners, overlays, and font swaps for CLS.
- [ ] **PERF-098** `P1` Optimize CSS delivery and avoid unnecessary render-blocking work on important page templates.
- [ ] **PERF-099** `P1` Configure browser and CDN caching for fingerprinted immutable assets while keeping HTML and user-specific data appropriately fresh.
- [ ] **PERF-100** `P1` Verify service-worker caches and offline support do not leave users on incompatible or stale application versions.
- [ ] **PERF-101** `P1` Test on representative low-end mobile devices and constrained networks, not solely high-end desktop hardware.
- [ ] **PERF-102** `P1` Profile long lists, virtualized grids, charts, and heavy components for scrolling and input responsiveness.
- [ ] **PERF-103** `P1` Measure the performance impact of analytics, advertising, consent, embeds, and other third-party scripts.
- [ ] **PERF-104** `P1` Provide comprehensible progress and recovery states for slow API calls without disguising failures or blocking accessible interactions.
- [ ] **PERF-105** `P1` Check that performance optimizations preserve focus behavior, keyboard interaction, labels, and reduced-motion requirements.
- [ ] **PERF-106** `P1` Monitor browser runtime errors and release-specific performance regressions after deployment.

## Release gate


- [ ] Performance budgets, workload assumptions, target cohorts, and accountable owners are defined for the release's critical journeys and endpoints.
- [ ] Representative baseline and relevant peak-load tests meet documented latency, throughput, error-rate, and saturation criteria, with acknowledged test-environment limitations.
- [ ] Major backend or database bottlenecks, cache behavior, and overload/recovery paths are measured and either addressed or accepted with authorized risk ownership.
- [ ] Applicable frontend routes have measured Core Web Vitals or equivalent user-centric measures, and critical interaction regressions have been reviewed.
- [ ] Expected peak/growth demand has a documented capacity plan, scaling constraints, monitoring signals, and safe response to saturation.
- [ ] No unresolved critical performance failure jeopardizes core tasks or overload recovery without an explicit, time-bound acceptance and mitigation plan.

**Domain-specific approval rule:** Block performance sign-off when material latency or capacity targets are missing, critical workflows breach agreed thresholds without approved mitigation, overload causes uncontrolled failure, or regressions remain unowned. Benchmarks and Web Vitals are context-dependent; meeting a public threshold is not a universal performance guarantee.

**Optional tooling:** [Frontend test examples](../references/optional-testing-tools-frontend.md#12_performance_and_scalability), not prerequisites or verification evidence.

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
