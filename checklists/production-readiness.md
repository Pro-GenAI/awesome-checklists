# Production Readiness — drop-in review checklist

Copy these unchecked items into a project PR description or issue. Each item maps to a stable ID in the canonical library. Mark as complete **only after** recording project-specific evidence; a checkbox is not certification.

- [ ] **PERF-024** — Test cold-start and warm-start runtime initialization. [Canonical check](../lists/backend/27_Performance_and_Scalability.md). *Why:* Catches failures hidden by warm developer machines or import-time side effects.
- [ ] **SEC-105** — Scan source, history and build artifacts for secrets. [Canonical check](../lists/05_Security.md). *Why:* Prevents exposed production credentials from reaching releases.
- [ ] **OPS-093** — Test API rate limits, upstream timeouts and quotas. [Canonical check](../lists/backend/30_DevOps_and_CI_CD.md). *Why:* Constrains runaway inference use and dependency overload.
- [ ] **OPS-032** — Keep base images and dependencies on a patch policy. [Canonical check](../lists/backend/30_DevOps_and_CI_CD.md). *Why:* Reduces known vulnerabilities in container and runtime supply chains.
- [ ] **SERVE-042** — Test provider throttling, backpressure and client retries. [Canonical check](../lists/AI/12_AI_Inference_and_Serving.md). *Why:* Prevents retry storms and unpredictable inference availability.

**Review record:** Target revision: `UNKNOWN` · Checklist source revision: `UNKNOWN` · Reviewer/approver: `UNKNOWN` · Evidence/exception links: `UNKNOWN`.

See [catalog.json](catalog.json) for machine-readable stage, contextual priority hint, severity and proposed integration signals. These are **not** pre-run checks or universal release gates.
