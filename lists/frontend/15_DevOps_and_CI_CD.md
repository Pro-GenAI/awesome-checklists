# 15 — DevOps and CI/CD Checklist

> Verify repeatable builds, trusted deployment artifacts, controlled infrastructure changes, safe rollout and rollback, and accountable software delivery. This checklist focuses on delivery systems; evaluate detailed functional tests, security, reliability, observability, and launch procedures in their own checklists as well.

> **Scope: Frontend-specific.** This file is one part of the 15_DevOps_and_CI_CD.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Frontend Checks

- [ ] **OPS-098** `P1` Produce versioned frontend artifacts with reproducible asset manifests and predictable configuration injection.
- [ ] **OPS-099** `P1` Verify the selected static, server-rendered, or hybrid deployment mode works in all supported target environments.
- [ ] **OPS-100** `P1` Test that entry points, deep links, and client-side routes resolve correctly after deployment and browser refresh.
- [ ] **OPS-101** `P1` Validate environment-specific public API base URLs, feature flags, and non-secret frontend configuration before promotion.
- [ ] **OPS-102** `P1` Ensure secrets or server-side signing credentials are never included in client bundles, static assets, or public source maps.
- [ ] **OPS-103** `P1` Validate asset fingerprinting, CDN cache headers, and invalidation so users do not receive incompatible versions of code and data.
- [ ] **OPS-104** `P1` Keep HTML caching compatible with the active JavaScript/CSS asset version and deployment strategy.
- [ ] **OPS-105** `P1` Coordinate frontend and API deployment compatibility so temporarily mixed versions still support critical workflows.
- [ ] **OPS-106** `P1` Check that new and old clients can handle planned API changes during progressive deployments.
- [ ] **OPS-107** `P1` Run post-deployment smoke checks for login, navigation, primary forms, and critical browser interactions.
- [ ] **OPS-108** `P1` Verify correct handling of staging versus production indexing, canonical tags, and robots directives for public sites.
- [ ] **OPS-109** `P1` Include targeted accessibility, visual regression, and browser compatibility checks in relevant delivery stages.
- [ ] **OPS-110** `P1` Validate service-worker updates, offline caches, and installed-app refresh paths where the product uses them.
- [ ] **OPS-111** `P1` Check that feature flags can disable risky frontend behavior without making the existing experience unusable.
- [ ] **OPS-112** `P1` Measure key page loading, runtime errors, and user interaction health during staged rollouts.
- [ ] **OPS-113** `P1` Ensure deployment and rollback do not leave users with broken in-progress forms, expired state, or inaccessible resources.
- [ ] **OPS-114** `P1` Verify frontend release errors and telemetry are correlated to the deployed version without logging personal data or credentials.

## Release gate

- [ ] The intended source revision builds successfully through a repeatable, reviewed pipeline and produces an identifiable immutable release artifact.
- [ ] Required test, contract, security, and infrastructure checks pass or have risk-appropriate and explicitly authorized exceptions.
- [ ] Production identities, secrets, environment settings, and deployment permissions are scoped, protected, and reviewed for the actual target.
- [ ] Deployment sequencing, health/readiness checks, compatibility constraints, and recovery or rollback procedures are documented and have been validated as appropriate to risk.
- [ ] API/frontend consumers, environment dependencies, and data migrations are compatible with the rollout, or an approved coordination plan prevents disruption.
- [ ] Release owners have observable go/no-go criteria, post-deployment checks, escalation paths, and project-specific records of the release decision.

**Domain-specific approval rule:** Block promotion when the artifact's identity or origin is unknown, mandatory pipeline gates fail without approval, production secrets/permissions are exposed, material backward-compatibility risks are unresolved, or a failed rollout cannot be safely stopped or recovered without an accepted and documented contingency.

**Optional tooling:** [Frontend test examples](../references/optional-testing-tools-frontend.md#15_devops_and_ci_cd), not prerequisites or verification evidence.

## Trusted references and scope

The following primary sources inform the verification questions above. Their platform-specific recommendations are conditional on the actual environment and risk profile; they are not claims that every project must use a particular provider or tooling.

- [DORA — Continuous delivery](https://dora.dev/capabilities/continuous-delivery/) — delivery automation, automated testing, and smaller reversible changes.
- [DORA — Test automation](https://dora.dev/capabilities/test-automation/) — pipeline quality gates and rapid feedback.
- [DORA — Loosely coupled teams](https://dora.dev/capabilities/loosely-coupled-teams/) — independent deployment and contract compatibility.
- [AWS — DevOps guidance: Continuous integration](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/continuous-integration.html) — repeatable builds and integration practices.
- [AWS — DevOps guidance: Continuous delivery indicators](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/indicators-for-continuous-delivery.html) — trusted artifacts, deployment automation, and quality assurance.
- [GitHub Docs — Security for GitHub Actions](https://docs.github.com/en/actions/how-tos/secure-your-work) — workflow hardening, pinned actions, artifact attestations.
- [GitHub Docs — Security hardening your deployments](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments) — OIDC-based cloud authentication and deployment credentials.
- [GitHub Docs — Deployments and environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments) — protected environments and conditional approval controls.
- [SLSA Specification v1.2](https://slsa.dev/spec/v1.2/) — software supply-chain assurance and build provenance; assurance levels are optional risk-based targets.
- [HashiCorp Terraform — State](https://developer.hashicorp.com/terraform/language/state) — infrastructure state, locking, and access controls when Terraform is used.
- [Kubernetes — Liveness, Readiness, and Startup Probes](https://kubernetes.io/docs/concepts/workloads/pods/probes/) — safe workload health and traffic readiness when Kubernetes is used.
- [OpenTelemetry — Signals](https://opentelemetry.io/docs/concepts/signals/) — logs, metrics, and traces for release verification.

**Applicability:** A small static website, an API service, a regulated platform, and a distributed system have different release risks. Adapt the controls accordingly. GitHub environment protection, DORA capabilities, SLSA levels, Terraform remote state, and Kubernetes probes do not apply unchanged to every project.

**Source review date:** 2026-11-12.
