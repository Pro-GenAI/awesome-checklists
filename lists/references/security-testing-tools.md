# Optional security testing tools — review before execution

Tools are **optional examples**, not prerequisites, approvals, endorsements or proof of security. The **[shared review method](review-method.md)** governs evidence, human approval and responsible use. Evaluate author and license, exact pinned version, dependency/provenance, requested credentials, network and execution permissions, sandbox strength, data retention and operational safety. Prefer non-production systems and least privilege. **Do not run third-party agent skills automatically or on production data.**

The following suggestions were previously embedded in the four numbered Security scope files. They are preserved here for discoverability; their presence does **not** mean they were installed, run or independently verified for safety. Keep actual release criteria in the numbered checklists.

## lists/05_Security.md

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** secrets, authorization, dependency vulnerabilities, attack surfaces, and validation failures; include shared/cross-team controls where applicable.
- **Cross-stack:** [OWASP ZAP](https://www.zaproxy.org/) + [Gitleaks](https://github.com/gitleaks/gitleaks) + [Trivy](https://trivy.dev/latest/).
- **Optional source pin:** Cloudflare security-audit-skill is linked at upstream commit `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8` (checked 2026-11-15). This is a reproducible reference, **not** a security certification, installation requirement, or permission to run arbitrary target code. Humanly inspect the pinned revision before use.
- **Optional agent-led audit:** [Cloudflare security-audit skill](https://github.com/cloudflare/security-audit-skill/tree/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/skills/security-audit) provides a multi-phase workflow with coverage tracking, independent candidate verification, structured findings, and reporting. Before use, review its [requirements and safety constraints](https://github.com/cloudflare/security-audit-skill/blob/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8/README.md): full audits require compatible agent/sub-agent tooling, Node.js validators, and OS-enforced isolation for target-controlled execution. Do not run target-controlled tests without the prescribed sandbox, probe production/live services, or treat a machine-generated finding as independently confirmed.
- **Python:** [Bandit](https://bandit.readthedocs.io/) + [pip-audit](https://github.com/pypa/pip-audit) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [npm audit](https://docs.npmjs.com/cli/commands/npm-audit) to triage npm advisories, [Semgrep](https://semgrep.dev/) using reviewed security rules, and [ESLint](https://eslint.org/) with [eslint-plugin-security](https://github.com/eslint-community/eslint-plugin-security) to flag supported risky patterns. Save rule versions, findings and independent confirmation.
- **JavaScript:** [npm audit](https://docs.npmjs.com/cli/commands/npm-audit) for dependency advisories, [Semgrep](https://semgrep.dev/) for static security checks and [eslint-plugin-security](https://github.com/eslint-community/eslint-plugin-security) with [ESLint](https://eslint.org/). Jest is useful for existing application tests but is **not** itself a security scanner.
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

## lists/frontend/09_Security.md

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** secrets, authorization, dependency vulnerabilities, attack surfaces, and validation failures; include browser and client behavior where applicable.
- **Cross-stack:** [OWASP ZAP](https://www.zaproxy.org/) + [Gitleaks](https://github.com/gitleaks/gitleaks) + [Trivy](https://trivy.dev/latest/).
- **Python:** [Bandit](https://bandit.readthedocs.io/) + [pip-audit](https://github.com/pypa/pip-audit) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [npm audit](https://docs.npmjs.com/cli/commands/npm-audit) to triage npm advisories, [Semgrep](https://semgrep.dev/) using reviewed security rules, and [ESLint](https://eslint.org/) with [eslint-plugin-security](https://github.com/eslint-community/eslint-plugin-security) to flag supported risky patterns. Save rule versions, findings and independent confirmation.
- **JavaScript:** [npm audit](https://docs.npmjs.com/cli/commands/npm-audit) for dependency advisories, [Semgrep](https://semgrep.dev/) for static security checks and [eslint-plugin-security](https://github.com/eslint-community/eslint-plugin-security) with [ESLint](https://eslint.org/). Jest is useful for existing application tests but is **not** itself a security scanner.
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

## lists/backend/09_Security.md

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** secrets, authorization, dependency vulnerabilities, attack surfaces, and validation failures; include API and service behavior where applicable.
- **Cross-stack:** [OWASP ZAP](https://www.zaproxy.org/) + [Gitleaks](https://github.com/gitleaks/gitleaks) + [Trivy](https://trivy.dev/latest/).
- **Python:** [Bandit](https://bandit.readthedocs.io/) + [pip-audit](https://github.com/pypa/pip-audit) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [npm audit](https://docs.npmjs.com/cli/commands/npm-audit) to triage npm advisories, [Semgrep](https://semgrep.dev/) using reviewed security rules, and [ESLint](https://eslint.org/) with [eslint-plugin-security](https://github.com/eslint-community/eslint-plugin-security) to flag supported risky patterns. Save rule versions, findings and independent confirmation.
- **JavaScript:** [npm audit](https://docs.npmjs.com/cli/commands/npm-audit) for dependency advisories, [Semgrep](https://semgrep.dev/) for static security checks and [eslint-plugin-security](https://github.com/eslint-community/eslint-plugin-security) with [ESLint](https://eslint.org/). Jest is useful for existing application tests but is **not** itself a security scanner.
- **Container-specific tools:** [Docker Bench for Security](https://github.com/docker/docker-bench-security), [Trivy](https://trivy.dev/latest/), and authorized `docker inspect` / `docker info` checks can support—but cannot prove—host/daemon isolation and container configuration.
- **Node.js-specific:** [npm audit](https://docs.npmjs.com/cli/commands/npm-audit), [ESLint](https://eslint.org/), [eslint-plugin-security](https://github.com/eslint-community/eslint-plugin-security), [Semgrep](https://semgrep.dev/), and [OWASP ZAP](https://www.zaproxy.org/) can support review of unsafe execution, dependency scripts, and attack surfaces. Exercise failure recovery and session revocation in an authorized test environment; static scanners alone cannot prove correct behavior.
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

## lists/AI/04_Security.md

Choose tools appropriate to the project's stack and risks; automation supports evidence but does not approve the checklist.

- **Test focus:** secrets, authorization, dependency vulnerabilities, attack surfaces, and validation failures; include model and dataset behaviors where applicable.
- **Cross-stack:** [OWASP ZAP](https://www.zaproxy.org/) + [Gitleaks](https://github.com/gitleaks/gitleaks) + [Trivy](https://trivy.dev/latest/).
- **Python:** [Bandit](https://bandit.readthedocs.io/) + [pip-audit](https://github.com/pypa/pip-audit) + [pytest](https://docs.pytest.org/en/stable/); for pytest-based suites, run `python -m pytest -q`.
- **TypeScript:** [npm audit](https://docs.npmjs.com/cli/commands/npm-audit) to triage npm advisories, [Semgrep](https://semgrep.dev/) using reviewed security rules, and [ESLint](https://eslint.org/) with [eslint-plugin-security](https://github.com/eslint-community/eslint-plugin-security) to flag supported risky patterns. Save rule versions, findings and independent confirmation.
- **JavaScript:** [npm audit](https://docs.npmjs.com/cli/commands/npm-audit) for dependency advisories, [Semgrep](https://semgrep.dev/) for static security checks and [eslint-plugin-security](https://github.com/eslint-community/eslint-plugin-security) with [ESLint](https://eslint.org/). Jest is useful for existing application tests but is **not** itself a security scanner.
- **Evidence:** Save tool versions, configuration, test environment, fixtures, results, and links in project-specific review records using the existing checklist IDs. Expert review remains necessary where relevant.

## Maintenance and limitations

Check tool links and prerequisites against current upstream documentation before use. The repository lint workflow checks **internal** Markdown paths on every push and uses a **separate external-link audit** when explicitly requested; network errors and rate limits can make external link status inconclusive. Never treat a tool's green report as a signed security assessment.
