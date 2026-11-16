# 22 — Release and Launch Readiness Checklist

> Verify that a new product, service, or significant change is ready for controlled customer exposure, has an explicit go/no-go decision, and can be operated and supported safely after launch. This release-level checklist consolidates sign-offs from deeper reviews rather than duplicating all of their technical tests.

> **Scope: AI-specific.** This file is one part of the 22_Release_and_LaunchReadiness.md checklist. Apply the domain-wide release gate across all applicable scope files; each checklist ID remains unique.

> **Using this checklist:** [Review method, evidence requirements and priority interpretation](../references/review-method.md) · [Optional framework crosswalk](../references/compliance-crosswalk.md). Priorities below are **project-adjustable starting tiers**, not universal release or legal requirements.

## Launch scope and ownership

- [ ] **LAUNCH-002** `P2` Define the user and business outcomes required from the launch, including measurable success and guardrail metrics.

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

**Optional tooling:** [AI-scope testing examples](../references/optional-testing-tools-ai.md#22_release_and_launchreadiness), not prerequisites or evidence of PASS.

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
