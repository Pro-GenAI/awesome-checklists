# 11 — DevOps and CI/CD Checklist

> Verify repeatable builds, trusted deployment artifacts, controlled infrastructure changes, safe rollout and rollback, and accountable software delivery. This checklist focuses on delivery systems; evaluate detailed functional tests, security, reliability, observability, and launch procedures in their own checklists as well.

> **Scope: Shared / cross-cutting.** This file is one part of the 11_DevOps_and_CI_CD.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](references/review-method.md) · [Optional framework crosswalk](references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Build and integration workflow


- [ ] **OPS-002** `P1` Ensure supported build commands execute in an isolated, repeatable environment without depending on a developer's workstation state.
- [ ] **OPS-003** `P1` Pin language runtimes, compilers, major build tools, and package-manager versions sufficiently to reproduce release builds.
- [ ] **OPS-004** `P1` Use dependency lockfiles or an equivalent deterministic resolution method where supported and enforce their consistency in CI.
- [ ] **OPS-005** `P1` Require the relevant compilation, lint, format, type, and unit-test checks to pass before accepting release candidates.
- [ ] **OPS-006** `P1` Run integration and contract checks against representative dependencies or controlled test doubles, according to risk.
- [ ] **OPS-008** `P1` Keep fast feedback checks early in pipelines and reserve slower end-to-end or nonfunctional jobs for appropriate stages.
- [ ] **OPS-009** `P1` Capture structured test reports, logs, and failed-job diagnostics with enough context to reproduce failures.
- [ ] **OPS-010** `P2` Record flaky, quarantined, and intermittently failing tests with owners, expiry or remediation plans, and visibility in CI.
- [ ] **OPS-011** `P1` Ensure build artifacts have immutable version identifiers, such as source commit, package version, and digest.
- [ ] **OPS-012** `P1` Build a release artifact once and promote the same artifact through later environments rather than rebuilding it with untracked changes.
- [ ] **OPS-013** `P2` Publish artifacts to an access-controlled registry or repository with retention and deletion policies.
- [ ] **OPS-014** `P1` Generate software bills of materials or comparable dependency inventories when required by project risk or supply-chain policy.
- [ ] **OPS-015** `P1` Generate and verify build provenance or artifact attestations to the organization's selected SLSA assurance target where appropriate.
- [ ] **OPS-016** `P1` Restrict workflow permissions, protect build signing keys, and avoid long-lived credentials in CI wherever a scoped alternative exists.
- [ ] **OPS-017** `P1` Pin third-party CI actions, tasks, and images to trustworthy immutable versions or digests where possible.
- [ ] **OPS-018** `P1` Keep untrusted contributions, external code, and test data from receiving privileged tokens or modifying trusted release artifacts.
- [ ] **OPS-019** `P1` Use caching without allowing stale, poisoned, or cross-trust-boundary caches to change the correctness of release builds.
- [ ] **OPS-020** `P2` Define parallel-job, cancellation, retry, and concurrency policies so obsolete runs cannot race or replace a newer release.

## Deployment and rollback


- [ ] **OPS-047** `P1` Protect production deployments against unintended triggers and concurrent or superseded runs.

- [ ] **OPS-053** `P1` Use expand/migrate/contract or another safe strategy for changes that cannot be instantly reverted.
- [ ] **OPS-054** `P2` Identify irreversible migrations or external side effects and plan forward fixes or compensating actions instead of assuming rollback is possible.
- [ ] **OPS-055** `P1` Test the documented rollback or roll-forward procedure for representative failure cases and required time limits.
- [ ] **OPS-056** `P2` Define explicit go/no-go metrics, alert thresholds, release observation windows, and who may halt a rollout.
- [ ] **OPS-058** `P1` Retain the prior known-good artifact and required configuration long enough for authorized recovery.
- [ ] **OPS-059** `P1` Verify that traffic shifts, feature flag changes, and rollback actions are auditable and bounded in scope.
- [ ] **OPS-061** `P1` Notify affected teams and downstream consumers of scheduled downtime or disruptive migrations where applicable.

## Delivery governance


- [ ] **OPS-065** `P1` Protect the release source and workflow definitions with repository access rules appropriate to project risk.
- [ ] **OPS-068** `P1` Use documented exception handling for blocked pipelines, bypass requests, and emergency releases with appropriate authorization.
- [ ] **OPS-069** `P1` Separate duties for high-risk operations if mandated by contracts, regulation, or organizational policy.
- [ ] **OPS-070** `P2` Maintain an on-call or escalation path for failed pipelines, unsuccessful deployments, and critical release regressions.
- [ ] **OPS-073** `P1` Check that improvements in delivery speed are not achieved by suppressing quality, security, or customer-impact signals.
- [ ] **OPS-076** `P1` Ensure emergency rollback and production access procedures can be executed when the main automation platform is unavailable.
- [ ] **OPS-077** `P2` Publish release notes or change summaries relevant to operators, support teams, and affected consumers.
- [ ] **OPS-080** `P1` Reassess delivery controls after major changes to service architecture, vendor platforms, compliance scope, or release frequency.

## Release gate


- [ ] The intended source revision builds successfully through a repeatable, reviewed pipeline and produces an identifiable immutable release artifact.
- [ ] Required test, contract, security, and infrastructure checks pass or have risk-appropriate and explicitly authorized exceptions.
- [ ] Production identities, secrets, environment settings, and deployment permissions are scoped, protected, and reviewed for the actual target.
- [ ] Deployment sequencing, health/readiness checks, compatibility constraints, and recovery or rollback procedures are documented and have been validated as appropriate to risk.
- [ ] API/frontend consumers, environment dependencies, and data migrations are compatible with the rollout, or an approved coordination plan prevents disruption.
- [ ] Release owners have observable go/no-go criteria, post-deployment checks, escalation paths, and project-specific records of the release decision.

**Domain-specific approval rule:** Block promotion when the artifact's identity or origin is unknown, mandatory pipeline gates fail without approval, production secrets/permissions are exposed, material backward-compatibility risks are unresolved, or a failed rollout cannot be safely stopped or recovered without an accepted and documented contingency.

**Optional tooling:** [File-specific tool examples](references/optional-testing-tools-shared.md#11_devops_and_ci_cd), not prerequisites or verification evidence.

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
