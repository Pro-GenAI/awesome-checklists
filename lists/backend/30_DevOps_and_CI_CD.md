# 30 — DevOps and CI/CD Checklist

> Verify repeatable builds, trusted deployment artifacts, controlled infrastructure changes, safe rollout and rollback, and accountable software delivery. This checklist focuses on delivery systems; evaluate detailed functional tests, security, reliability, observability, and launch procedures in their own checklists as well.

> **Scope: Backend / API-specific.** This file is one part of the 30_DevOps_and_CI_CD.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Build and integration workflow


- [ ] **OPS-001** `P2` Define which source changes trigger build, test, package, and deployment workflows, including changes to shared libraries and infrastructure.
- [ ] **OPS-007** `P1` Fail the pipeline on required quality gates instead of logging failures while reporting success.
- [ ] **OPS-021** `P2` Document how developers run key CI checks locally and how pipeline changes are reviewed and tested.
- [ ] **OPS-022** `P1` Review pipeline duration, failure causes, and feedback quality regularly, with tracked improvements.

## Infrastructure and environments


- [ ] **OPS-024** `P2` Describe infrastructure in version-controlled, reviewable configuration or infrastructure-as-code wherever suitable.
- [ ] **OPS-025** `P1` Use code review and an explicit plan/diff before applying material infrastructure changes.
- [ ] **OPS-026** `P1` Protect infrastructure state with appropriate remote access controls, locking, backups, and encryption where the chosen tool requires it.
- [ ] **OPS-028** `P1` Use short-lived, least-privilege deployment identities and segregate production permissions from lower environments.
- [ ] **OPS-031** `P1` Detect infrastructure drift between declared and deployed state and record its resolution.
- [ ] **OPS-032** `P1` Ensure container base images, runtime environments, and third-party dependencies follow an update and patching policy.
- [ ] **OPS-033** `P1` Scan infrastructure definitions or deploy manifests for high-risk misconfigurations using relevant tools.
- [ ] **OPS-035** `P2` Define network boundaries, ingress/egress rules, identity dependencies, and necessary service connectivity.
- [ ] **OPS-040** `P1` Protect environment-specific domains, DNS, TLS certificates, CDN settings, and routing configuration through a controlled process.
- [ ] **OPS-041** `P2` Document how deployment pipelines access protected environments, including human approvals where law, risk, or policy requires them.
- [ ] **OPS-042** `P1` Set environment cost and retention boundaries, and periodically remove abandoned infrastructure.
- [ ] **OPS-023** `P2` Inventory environments and their purpose, ownership, region, critical services, and lifecycle.
- [ ] **OPS-027** `P1` Keep provider credentials, tokens, certificates, and encryption keys out of source, build output, and shared job logs.
- [ ] **OPS-029** `P1` Separate development, test, staging, and production data and access according to risk, with no accidental production-data copies.
- [ ] **OPS-030** `P1` Manage configuration differences deliberately, documenting feature flags, endpoints, quotas, and secret references by environment.
- [ ] **OPS-034** `P1` Set capacity and resource requests, limits, autoscaling policy, and quota expectations for critical workloads when applicable.
- [ ] **OPS-036** `P1` Verify environment provisioning and teardown are repeatable and do not leave unmanaged resources or credentials.
- [ ] **OPS-037** `P1` Ensure managed databases, caches, queues, and storage have documented ownership and configuration baselines.
- [ ] **OPS-038** `P2` Define lifecycle, startup, readiness, and liveness behavior for workloads so traffic is not sent to unready instances.
- [ ] **OPS-039** `P1` Use health checks carefully to avoid restart loops or cascading failures during dependency outages or high load.
- [ ] **OPS-043** `P1` Ensure backup, restore, and recovery prerequisites are identified and handed to the reliability review owner.

## Deployment and rollback


- [ ] **OPS-044** `P2` Define the deployment sequence, prerequisites, affected systems, and responsible operator for each production release.
- [ ] **OPS-045** `P1` Make application deployment steps automated and repeatable, with documented manual interventions only where justified.
- [ ] **OPS-046** `P2` Identify the exact immutable artifact, configuration revision, migration version, and source commit being deployed.
- [ ] **OPS-048** `P1` Use progressive rollout, rolling update, blue/green deployment, canary, or feature flags when the risk warrants gradual exposure.
- [ ] **OPS-050** `P1` Run appropriate smoke checks against the deployed artifact in the target environment before broad promotion.
- [ ] **OPS-051** `P1` Require critical pre-deployment quality/security checks and dependency compatibility checks before production traffic changes.
- [ ] **OPS-052** `P2` Document whether database and schema changes support both old and new application versions during rollout.
- [ ] **OPS-057** `P1` Ensure a failed deployment stops further promotion and reports the failure to the release owner.
- [ ] **OPS-060** `P1` Confirm secrets and credentials are not exposed by deployment logs, shell traces, generated manifests, or failed jobs.
- [ ] **OPS-062** `P2` Define post-deployment verification for critical transactions, business workflows, and dependent integrations.
- [ ] **OPS-063** `P2` Record the outcome of each deployment, including version, operator or automation, changes, and rollback status.
- [ ] **OPS-049** `P2` Define expected startup, readiness, warm-up, and connection-draining behavior before routing traffic to a new version.

## Delivery governance


- [ ] **OPS-064** `P2` Define who can change CI configuration, approve production promotions, and access deployment credentials.
- [ ] **OPS-066** `P1` Require review and traceable approval for consequential workflow, environment, or deployment-policy changes.
- [ ] **OPS-067** `P2` Record change history linking request or issue, reviewed source revision, build artifact, approval, and deployed version.
- [ ] **OPS-071** `P2` Assign owners and review schedules for runner images, build dependencies, deployment infrastructure, and automation maintenance.
- [ ] **OPS-072** `P2` Define and measure delivery performance indicators such as deployment frequency, change lead time, change failure, and recovery time with consistent definitions.
- [ ] **OPS-074** `P1` Assess reliability and cost of CI runners, artifact storage, and test infrastructure against project needs.
- [ ] **OPS-075** `P2` Document incident investigation and follow-up for recurring build, infrastructure, or deployment failures.
- [ ] **OPS-078** `P1` Review operational documentation and ownership after adopting new release tools or changing infrastructure architecture.
- [ ] **OPS-079** `P1` Retire unused deployment jobs, stale credentials, obsolete environments, and unsupported build workflows.

## API Checks


- [ ] **OPS-081** `P1` Build and deploy API services with reproducible artifacts and known version identifiers.
- [ ] **OPS-082** `P1` Validate deployed API schemas against their approved OpenAPI or equivalent contract where one exists.
- [ ] **OPS-083** `P1` Run consumer/provider contract tests in CI for public or cross-team API changes according to compatibility risk.
- [ ] **OPS-084** `P1` Detect breaking changes to fields, validation, authentication requirements, errors, and versioned endpoints before promotion.
- [ ] **OPS-085** `P1` Verify deployment ordering and compatibility when API providers and consumers release independently.
- [ ] **OPS-086** `P1` Run smoke checks for authentication, authorization boundaries, and critical API workflows in the target environment.
- [ ] **OPS-087** `P1` Include health and readiness endpoints that represent the service's ability to receive traffic without exposing sensitive internals.
- [ ] **OPS-088** `P1` Set and verify ingress, gateway, service-discovery, and routing configurations for each API environment.
- [ ] **OPS-089** `P1` Ensure API and worker rollouts respect in-flight requests, message consumption, and graceful shutdown behavior.
- [ ] **OPS-090** `P2` Define and test retry/idempotency expectations before shifting traffic between API versions.
- [ ] **OPS-091** `P2` Document API version changes, deprecation periods, and consumer notification responsibilities in release procedures.
- [ ] **OPS-092** `P1` Validate database migration compatibility with both prior and new API versions throughout the rollout.
- [ ] **OPS-093** `P1` Configure API rate limits, upstream timeouts, and quotas consistently across deployment environments where applicable.
- [ ] **OPS-094** `P1` Monitor critical endpoint latency, error rates, and traffic during canaries or post-release observation.
- [ ] **OPS-095** `P1` Verify third-party integration credentials, webhook routing, callback addresses, and network permissions in the target environment.
- [ ] **OPS-096** `P1` Confirm API logs, traces, and health diagnostics are safe for production and do not capture sensitive request payloads unnecessarily.
- [ ] **OPS-097** `P1` Exercise API rollback or forward recovery without leaving consumers on an unsupported contract.

## Release gate


- [ ] The intended source revision builds successfully through a repeatable, reviewed pipeline and produces an identifiable immutable release artifact.
- [ ] Required test, contract, security, and infrastructure checks pass or have risk-appropriate and explicitly authorized exceptions.
- [ ] Production identities, secrets, environment settings, and deployment permissions are scoped, protected, and reviewed for the actual target.
- [ ] Deployment sequencing, health/readiness checks, compatibility constraints, and recovery or rollback procedures are documented and have been validated as appropriate to risk.
- [ ] API/frontend consumers, environment dependencies, and data migrations are compatible with the rollout, or an approved coordination plan prevents disruption.
- [ ] Release owners have observable go/no-go criteria, post-deployment checks, escalation paths, and project-specific records of the release decision.

**Domain-specific approval rule:** Block promotion when the artifact's identity or origin is unknown, mandatory pipeline gates fail without approval, production secrets/permissions are exposed, material backward-compatibility risks are unresolved, or a failed rollout cannot be safely stopped or recovered without an accepted and documented contingency.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#30_devops_and_ci_cd), not prerequisites or verification evidence.

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
