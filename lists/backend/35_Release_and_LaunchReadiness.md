# 35 — Release and Launch Readiness Checklist

> Verify that a new product, service, or significant change is ready for controlled customer exposure, has an explicit go/no-go decision, and can be operated and supported safely after launch. This release-level checklist consolidates sign-offs from deeper reviews rather than duplicating all of their technical tests.

> **Scope: Backend / API-specific.** This file is one part of the 35_Release_and_LaunchReadiness.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Launch scope and ownership


- [ ] **LAUNCH-003** `P2` Document the launch date, deployment window, expected duration, time zone, and relevant change-freeze periods.
- [ ] **LAUNCH-006** `P2` Assign owners for each major dependency, external integration, vendor approval, or shared infrastructure change.
- [ ] **LAUNCH-019** `P1` Schedule explicit review points for go/no-go, initial deployment, traffic expansion, and post-launch acceptance.

## Production readiness


- [ ] **LAUNCH-022** `P1` Confirm release infrastructure and managed-service dependencies have named owners and documented support arrangements.
- [ ] **LAUNCH-024** `P1` Ensure production configuration, feature flags, and integration endpoints are reviewed for the actual deployment environment.
- [ ] **LAUNCH-025** `P1` Validate that required secrets, certificates, signing keys, and deployment identities are available without exposing them in build artifacts or logs.
- [ ] **LAUNCH-026** `P1` Confirm database migrations, backfills, data imports, and search-index builds are tested and sequenced with the release.
- [ ] **LAUNCH-027** `P2` Identify irreversible data or infrastructure changes and document safe alternatives to a naïve application rollback.
- [ ] **LAUNCH-034** `P1` Check relevant dependencies, including authentication, payments, messaging, CDN, DNS, and external APIs, against expected operating limits.
- [ ] **LAUNCH-133** `P1` For production email sent from a branded domain, confirm active sending/reply-to mailboxes, applicable SPF/DKIM/DMARC configuration and alignment, authenticated delivery to representative recipients, and monitoring of bounces or failed sends; apply receiver-specific bulk-sender requirements only when relevant.
- [ ] **LAUNCH-040** `P1` Verify capacity and budget for incident response, vendor support, increased traffic, and launch-day infrastructure scaling.

## Deployment and rollback


- [ ] **LAUNCH-044** `P1` Confirm required CI checks and previous environment promotions passed for the artifact being deployed.
- [ ] **LAUNCH-045** `P2` Document each deployment step, expected completion condition, accountable operator, and escalation point in a current runbook.
- [ ] **LAUNCH-046** `P1` Verify production deployment approvals and access controls match organizational policy and actual release risk.
- [ ] **LAUNCH-047** `P1` Ensure the release sequence accounts for dependent services, API consumers, workers, databases, queues, and background migrations.
- [ ] **LAUNCH-048** `P1` Check whether old and new application versions must coexist and test their data and API compatibility where relevant.
- [ ] **LAUNCH-049** `P1` Test environment-specific routing, traffic switching, DNS changes, and cache behavior before initiating deployment.
- [ ] **LAUNCH-053** `P2` Identify how deployment automation prevents overlapping or obsolete runs from overwriting an active release.
- [ ] **LAUNCH-054** `P1` Rehearse representative deployment failure scenarios and verify responders know how to halt promotion safely.
- [ ] **LAUNCH-060** `P1` Validate that migration progress, rollout health, and deployment logs are observable while the release is running.
- [ ] **LAUNCH-062** `P2` Record deployment decisions, traffic changes, feature-flag settings, and recovery actions against the release identifier.
- [ ] **LAUNCH-064** `P1` Verify that deployment credentials and production secrets are not exposed through scripts, logs, artifacts, or release communications.
- [ ] **LAUNCH-057** `P2` Define data reconciliation or compensating actions when rollback cannot undo schema changes or committed side effects.

## Post-launch verification


- [ ] **LAUNCH-065** `P1` Check the deployed artifact, feature-flag state, environment, schema revision, and active traffic routing against the approved release plan.
- [ ] **LAUNCH-069** `P1` Review service availability, API errors, tail latency, resource saturation, and queue health over the agreed observation window.
- [ ] **LAUNCH-073** `P1` Check incident reports, support contacts, social/customer feedback, and other signals that automated telemetry may miss.
- [ ] **LAUNCH-071** `P1` Validate data integrity, migration completion, record counts, and important business invariants after schema or bulk-data changes.

## API Checks


- [ ] **LAUNCH-085** `P2` Inventory public and internal API consumers affected by the launch and confirm communication owners for contract changes.
- [ ] **LAUNCH-086** `P1` Validate that the production API definition or contract version matches the approved release documentation.
- [ ] **LAUNCH-087** `P1` Run production-safe smoke requests for critical operations, authentication, authorization, and representative roles.
- [ ] **LAUNCH-088** `P1` Confirm old and new clients remain compatible during staged rollout, cached-client lifetimes, or documented migration windows.
- [ ] **LAUNCH-089** `P1` Verify expected response codes, validation errors, rate-limit behavior, and retry guidance in the target environment.
- [ ] **LAUNCH-090** `P1` Check that API gateway, ingress, DNS, TLS, and routing rules point to the intended service versions.
- [ ] **LAUNCH-091** `P1` Confirm production credentials, scopes, callback URLs, and third-party integration permissions are correct.
- [ ] **LAUNCH-092** `P1` Test representative webhook or event deliveries, signatures, acknowledgments, and duplicate-handling where applicable.
- [ ] **LAUNCH-093** `P1` Validate that database migration and schema evolution do not produce missing fields or failures for existing consumers.
- [ ] **LAUNCH-094** `P1` Check API idempotency for high-impact writes and ensure ambiguous timeouts do not produce duplicate customer actions.
- [ ] **LAUNCH-095** `P1` Verify health/readiness endpoints are accurate and do not expose protected internals or secrets.
- [ ] **LAUNCH-096** `P1` Review p95/p99 latency, error rate, and traffic composition for critical operations during initial exposure.
- [ ] **LAUNCH-097** `P1` Confirm monitoring can separate authentication failures, normal client errors, server faults, and overload throttling.
- [ ] **LAUNCH-098** `P1` Verify safe rollback or feature-disablement behavior for API consumers when a breaking change or side effect is detected.
- [ ] **LAUNCH-099** `P1` Ensure API documentation, SDK examples, changelogs, and deprecation notices reflect the deployed public contract.
- [ ] **LAUNCH-100** `P1` Check that logs and traces contain useful correlation identifiers while excluding sensitive request payloads and credentials.
- [ ] **LAUNCH-101** `P1` Test graceful handling when upstream dependencies, queues, or downstream providers are unavailable after launch.
- [ ] **LAUNCH-102** `P1` Confirm responsible consumer teams have a staffed escalation path for launch-day integration regressions.

## Release gate


- [ ] The release scope, exact artifact, target environment, deployment window, and accountable go/no-go owner are documented and agreed.
- [ ] Required technical, operational, security, privacy, accessibility, and business reviews are complete, with no unaccepted release-blocking findings.
- [ ] Production dependencies, migration prerequisites, secrets and access, capacity, monitoring, on-call coverage, and customer-support handoffs are ready for the intended launch.
- [ ] The rollout procedure has clear steps, audience/exposure controls, health thresholds, stop conditions, and safe recovery options, including treatment of irreversible changes.
- [ ] Critical API and frontend journeys are verified in production or an explicitly approved equivalent, with defined follow-up checks after live exposure.
- [ ] Stakeholder/customer communication plans, documentation, known limitations, and escalation channels are approved where applicable.
- [ ] A designated approver has recorded **Go**, **Go with authorized time-bound exceptions**, or **No-go** against the exact release and its residual risks.
- [ ] Post-launch observation, stabilization ownership, completion criteria, and remediation tracking are agreed before the release is declared finished.

**Domain-specific approval rule:** Block launch when essential user journeys are unverified, required sign-offs are missing, critical dependencies or support coverage are unready, the actual deployed artifact is unknown, or material deployment/recovery risks are unaccepted. A launch approval does not supersede legally required approvals or prove that all risks have been eliminated.

**Optional tooling:** [Backend-specific test examples](../references/optional-testing-tools-backend.md#35_release_and_launchreadiness), not prerequisites or verification evidence.

## Trusted references and scope

- [Gmail — Email sender guidelines](https://support.google.com/mail/answer/81126) — domain authentication and conditional sender rules.


The following primary sources informed these practical verification questions. Their detailed methods are adaptable rather than mandatory for every organization, and the links are not a claim of any formal launch certification.

- [Google SRE — Reliable Product Launches](https://sre.google/sre-book/reliable-product-launches/) — launch checklists, dependency review, capacity, operations, and coordinated readiness.
- [Google SRE — Launch Coordination Checklist](https://sre.google/sre-book/launch-checklist/) — release-day architecture, load, dependencies, reliability, and verification questions.
- [AWS Well-Architected — Operational readiness and change management](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/operational-readiness.html) — consistent prelaunch reviews, personnel, runbooks, change decisions, and support planning.
- [AWS Well-Architected — Operational Readiness Reviews](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/the-orr-tool.html) — tailored readiness checklists, escalation, event handling, and release quality.
- [AWS Well-Architected — Plan for unsuccessful changes](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_mit_deploy_risks_plan_for_unsucessful_changes.html) — recovery, rollback, feature-disablement, and response to failed releases.
- [AWS Well-Architected — Mitigate deployment risks](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/mitigate-deployment-risks.html) — deployment testing, phased exposure, feedback, and rollback.
- [Microsoft Azure Well-Architected — Operational Excellence checklist](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/checklist) — ownership, operations, monitoring, incident response, and safe deployment criteria.
- [Microsoft Azure Well-Architected — Safe deployment practices](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments) — progressive exposure, health gates, emergency changes, and rollback planning.
- [Google Cloud — Operational readiness and performance](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops) — readiness across workforce, processes, tools, governance, and service support.
- [GitHub Docs — Deployments and environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments) — protected deployment environments and approval mechanisms, when GitHub Actions is used.
- [OpenAPI Specification](https://spec.openapis.org/oas/v3.2.1.html) — versioned API contracts and interface documentation, when applicable.
- [Chrome for Developers — Service worker deployment](https://developer.chrome.com/docs/workbox/service-worker-deployment) — caching and compatibility considerations for service-worker-enabled web apps.

**Applicability:** The depth of review, number of approvals, exposure strategy, and stabilization period depend on customer impact, release type, team size, and applicable obligations. GitHub Actions protections and Workbox service-worker guidance are relevant only when those technologies are used. Reassess the launch plan after any substantial change to the candidate or target environment.

**Source review date:** 2026-11-13.
