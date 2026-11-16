# 14 — Release and Launch Readiness Checklist

> Verify that a new product, service, or significant change is ready for controlled customer exposure, has an explicit go/no-go decision, and can be operated and supported safely after launch. This release-level checklist consolidates sign-offs from deeper reviews rather than duplicating all of their technical tests.

> **Scope: Shared / cross-cutting.** This file is one part of the 14_Release_and_LaunchReadiness.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](references/review-method.md) · [Optional framework crosswalk](references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Launch scope and ownership


- [ ] **LAUNCH-001** `P2` Record whether this is a first launch, major feature, migration, regional rollout, or routine release, and identify the exact product version and intended audience.
- [ ] **LAUNCH-004** `P1` Name one accountable release owner and a backup with authority to coordinate decisions during the launch.
- [ ] **LAUNCH-005** `P2` Identify required approvers across product, engineering, operations, security, privacy, legal, and customer support as applicable.
- [ ] **LAUNCH-007** `P2` Document the release's in-scope features, exclusions, known limitations, and dependencies on other releases.
- [ ] **LAUNCH-008** `P2` Identify target customer groups, tenants, geographies, languages, device classes, and eligibility rules for rollout.
- [ ] **LAUNCH-009** `P1` Agree measurable go/no-go criteria, the decision timestamp, and who has final authority to approve or stop the launch.
- [ ] **LAUNCH-010** `P2` Maintain a single release plan linking the source revision, immutable artifact, change summary, owners, milestones, and evidence locations.
- [ ] **LAUNCH-011** `P1` Confirm prerequisite product, design, requirements, quality, accessibility, security, privacy, and compliance reviews have been completed where required.
- [ ] **LAUNCH-012** `P2` Track material open defects and risks by severity, affected user journey, owner, mitigation, and approval status.
- [ ] **LAUNCH-013** `P1` Verify that blockers cannot be silently downgraded or waived without an authorized, traceable decision.
- [ ] **LAUNCH-014** `P2` Identify any legal, regulatory, contractual, procurement, or marketplace approvals required before customer exposure.
- [ ] **LAUNCH-015** `P1` Agree customer-facing terms, pricing, entitlements, data-use notices, and purchase or subscription behavior for launch where applicable.
- [ ] **LAUNCH-016** `P1` Plan internal announcements, customer notices, release notes, help-center changes, and stakeholder briefings with owners.
- [ ] **LAUNCH-017** `P2` Define launch-day support capacity, coverage hours, escalation contacts, and alternate communications channels.
- [ ] **LAUNCH-018** `P1` Confirm customer success, sales, billing, and support teams know what is changing and how to handle predictable questions.
- [ ] **LAUNCH-020** `P1` Agree a contingency plan for launch delay or cancellation, including who communicates changes to affected users and teams.

## Production readiness


- [ ] **LAUNCH-021** `P1` Verify the target production environment, domains, networking, DNS, TLS, regional placement, and access rights are provisioned for the intended release.
- [ ] **LAUNCH-023** `P1` Review projected initial traffic, launch-day spikes, storage growth, quotas, and capacity headroom against recent evidence.
- [ ] **LAUNCH-028** `P1` Verify backups, restore access, and recovery prerequisites for changes that could corrupt or delete critical data.
- [ ] **LAUNCH-029** `P1` Confirm essential monitoring dashboards and customer-impact signals are available to launch responders.
- [ ] **LAUNCH-030** `P1` Ensure critical alerts have tested routing to staffed responders during the release window.
- [ ] **LAUNCH-031** `P1` Check that health endpoints, synthetic probes, and critical transaction monitoring reflect actual user availability.
- [ ] **LAUNCH-032** `P1` Verify incident severity criteria, incident commander or equivalent role, and emergency escalation procedures are current.
- [ ] **LAUNCH-033** `P1` Confirm production runbooks for restart, safe degradation, service restoration, and vendor escalation are accessible.
- [ ] **LAUNCH-035** `P1` Verify support processes can handle account recovery, failed transactions, customer reports, and requests requiring manual intervention.
- [ ] **LAUNCH-036** `P1` Confirm required user and operator documentation, accessibility guidance, and help content are available in supported languages.
- [ ] **LAUNCH-037** `P1` Assess resilience to a dependency outage or partial rollout, with accepted mitigations for unresolved risks.
- [ ] **LAUNCH-038** `P1` Confirm production permissions and operational controls permit authorized emergency disablement or rollback without unnecessary privilege.
- [ ] **LAUNCH-039** `P1` Ensure analytics, business event capture, and conversion measurements are configured with applicable consent and data-use limits.
- [ ] **LAUNCH-041** `P1` Check that all known high-impact defects affecting critical user journeys have been retested or formally accepted by qualified owners.
- [ ] **LAUNCH-042** `P1` Perform a final readiness review for the intended environment and release scope rather than relying on outdated prior sign-offs.

## Deployment and rollback


- [ ] **LAUNCH-043** `P2` Record the exact source commit, immutable build artifact, version, configuration, and migration identifiers to be released.
- [ ] **LAUNCH-050** `P1` Use staged exposure, canary, blue/green, rolling release, or feature flags where the scope and risk justify them.
- [ ] **LAUNCH-051** `P2` Define initial traffic cohort, expansion steps, wait/observation intervals, and named approval for each promotion.
- [ ] **LAUNCH-052** `P1` Set measurable thresholds for error rates, latency, availability, transaction failures, and business guardrails that halt rollout.
- [ ] **LAUNCH-055** `P1` Keep a usable known-good artifact and required prior configuration available for recovery.
- [ ] **LAUNCH-056** `P1` Document tested rollback, traffic reversal, feature-disablement, and forward-fix options appropriate to the changed components.

- [ ] **LAUNCH-058** `P1` Confirm operations affecting user sessions, in-flight requests, queued jobs, and streams have safe draining or resumption behavior.
- [ ] **LAUNCH-059** `P1` Account for CDN, browser, service-worker, mobile-client, and API-version caching that may persist after server rollback.
- [ ] **LAUNCH-061** `P1` Establish a decision rule for switching from rollback to forward recovery when restoration may be unsafe.
- [ ] **LAUNCH-063** `P2` Define an emergency hotfix path with appropriately constrained approvals and retrospective review.

## Post-launch verification


- [ ] **LAUNCH-066** `P1` Run smoke tests in the production environment for critical user journeys immediately after the initial rollout.
- [ ] **LAUNCH-067** `P1` Verify account creation/login, authorization, primary transactions, and other essential flows appropriate to the product.
- [ ] **LAUNCH-068** `P1` Confirm that billing, payments, notifications, webhooks, and partner integrations behave as expected where present.

- [ ] **LAUNCH-072** `P1` Compare real traffic, feature adoption, key funnels, and business guardrails against the prelaunch baseline and forecast.
- [ ] **LAUNCH-074** `P1` Ensure analytics dashboards and events are actually receiving production data without forbidden personal information.
- [ ] **LAUNCH-075** `P1` Observe trial cohorts or canary groups independently before expanding the release to additional users or regions.
- [ ] **LAUNCH-076** `P1` Confirm error-budget or equivalent reliability considerations support further rollout where such policies exist.
- [ ] **LAUNCH-077** `P1` Verify localized experiences and critical assistive-technology user journeys in production if launch-specific changes affect them.
- [ ] **LAUNCH-078** `P1` Inspect public landing pages, downloads, deep links, indexing directives, and application entry points where relevant.
- [ ] **LAUNCH-079** `P1` Verify important third-party integration callbacks and external side effects rather than relying solely on internal health checks.
- [ ] **LAUNCH-080** `P2` Document whether all go/no-go thresholds remained satisfied during the observation and traffic-expansion stages.
- [ ] **LAUNCH-081** `P2` Define a post-launch acceptance time, accountable reviewer, and criteria for declaring the release complete.
- [ ] **LAUNCH-082** `P1` Keep enhanced monitoring, rollback access, and incident coverage in place until the agreed stabilization period ends.
- [ ] **LAUNCH-083** `P1` Create owned follow-up issues for deferred improvements, nonblocking defects, and observations discovered after launch.
- [ ] **LAUNCH-084** `P2` Record actual release outcomes, incidents, lessons, and any change to operational runbooks or future launch gates.

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

**Optional tooling:** [File-specific tool examples](references/optional-testing-tools-shared.md#14_release_and_launchreadiness), not prerequisites or verification evidence.

## Trusted references and scope


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

**Source review date:** 2026-11-12.
