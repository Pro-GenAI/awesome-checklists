# Awesome Checklists [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![Awesome Checklists banner — frontend, backend, and AI review checklists](website/assets/awesome-checklists-banner.svg)

**Build with intention. Review with evidence. Launch with fewer blind spots.**

> A curated, evidence-oriented checklist library for production Generative AI, LLMOps, autonomous agents, and the supporting software needed to ship them safely.

**91 scoped checklists · 4,215 unique checks · 4 complementary review scopes**

Great products are rarely derailed by one spectacular mistake. More often, the problems are questions nobody asked, assumptions nobody tested, and responsibilities nobody owned.

**Awesome Checklists** helps teams ask those questions *before* they become expensive surprises. Use it to turn vague readiness discussions into structured, evidence-based reviews—without reinventing a process for every project.

**Short curated Awesome index:** [AWESOME.md](AWESOME.md) is the linted, phase-oriented selection; this README introduces the source library and agent skill; [DEVELOPMENT.md](DEVELOPMENT.md) contains technical and maintenance details.

## Contents

- [Production GenAI lifecycle](#production-genai-lifecycle)
- [Start with 25–50 checks](#start-with-2550-checks)
- [Agent skill for Codex and Claude Code](#agent-skill-for-codex-and-claude-code)
- [Explore the checklists](#explore-the-checklists)
- [How to use these checklists](#how-to-use-these-checklists)
- [Development and maintenance](#development-and-maintenance)

## Production GenAI lifecycle

These phase-oriented [drop-in PR/issue templates](checklists/README.md) complement, rather than replace, the existing 91 numbered source checklists. Each item links to its canonical stable ID and explains the failure mode it helps detect. `[PR Template]`, `[Security Audit]`, `[Eval Benchmark]`, and `[Runtime Guardrail]` are editorial navigation tags, not certifications or claims that a check was run.

### Prompt & Context Engineering

`[PR Template]` [Prompt and context checklist](checklists/prompt-context.md) — verify trust boundaries, strict output schemas, context-token budgets, truncation and injection resistance before a prompt or tool schema change. Source: [Prompt engineering and versioning](lists/AI/09_Prompt_Engineering_and_Versioning.md).

### RAG & Data Pipelines

`[Eval Benchmark]` [RAG and data checklist](checklists/rag-data.md) — prevent broken document chunking, incompatible embeddings, partial index swaps, unmeasured retrieval loss and stale/deleted vector data. Sources: [RAG and knowledge bases](lists/AI/10_RAG_and_Knowledge_Bases.md) and [AI evaluation](lists/AI/15_AI_Evaluation_and_Regression.md).

### Agent Safety & Runtime Guardrails

`[Runtime Guardrail]` [Agent safety checklist](checklists/agent-safety.md) — validate tool registry membership, operation-level permissions, prompt-injection defenses, handoff traces and partial-stream action boundaries. Sources: [Tool orchestration](lists/AI/11_AI_Agents_and_Tool_Orchestration.md), [red-teaming](lists/AI/16_AI_Red_Teaming_and_Guardrails.md) and [streaming inference](lists/AI/12_AI_Inference_and_Serving.md).

### Evaluation & Observability

`[Eval Benchmark]` [Evaluation and observability checklist](checklists/evaluation-observability.md) — catch regressions by keeping golden cases, schema and tool assertions, retrieval quality, user-visible latency and usage costs separate. Sources: [Evaluation and regression](lists/AI/15_AI_Evaluation_and_Regression.md) and [AI monitoring and drift](lists/AI/18_AI_Monitoring_and_Drift.md).

### Production Readiness

`[Security Audit]` [Production readiness checklist](checklists/production-readiness.md) — verify cold-start behavior, secrets scanning, quotas, dependency/container patching and rate-limit recovery before promoting a release. Sources: [Backend operations](lists/backend/30_DevOps_and_CI_CD.md), [performance](lists/backend/27_Performance_and_Scalability.md) and [inference serving](lists/AI/12_AI_Inference_and_Serving.md).

For Pro-GenAI implementation examples and where to apply these checks, see [development companions](DEVELOPMENT.md#pro-genai-implementation-companions).

## Start with 25–50 checks

**Do not attempt all 4,215 checks.** Start with the [Core 50 curated starter](lists/references/core-50.md) or the [25-check starter for each relevant scope](lists/references/minimum-viable-by-scope.md). You can also [generate a focused, UNKNOWN-first project review](lists/references/scoped-review-generator.md) rather than copying the entire source library.

Only the **Core 50 priority tiers** are individually curated; all other tiers are **provisional, text-derived suggestions**. The generator does **not use provisional P0/P1/P2 labels for selection ranking**. Determine project-specific severity from real threats, obligations, evidence and qualified human review. No independent field validation or external reviewer sign-off is claimed.

## Agent skill for Codex and Claude Code

**Use these checklists directly in your coding agent.** The [`awesome-checklists` agent skill](skills/awesome-checklists/SKILL.md) teaches Codex, Claude Code, and other Agent Skills-compatible tools to choose relevant reviews, retrieve revision-pinned checklist criteria, inspect real project evidence, and report actionable findings with stable IDs.

From the project you want to review, install the skill using the [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/Pro-GenAI/awesome-checklists --skill awesome-checklists -a codex -a claude-code
```

To install for just one agent, use `-a codex` or `-a claude-code`; add `-g` for a global installation. Discover the packaged skill without installing it with `npx skills add Pro-GenAI/awesome-checklists --list`. The CLI requires a supported Node.js release (currently Node.js 22.20+).

After installation, ask an agent: **“Review this app's release readiness using awesome-checklists; cite actual checklist IDs and evidence for each finding.”** Other examples: “Audit our API security and database controls,” or “Assess this RAG/agent implementation for evaluation and guardrail gaps.”

For source pinning, anonymous access, and skill fetch-helper internals, see [agent skill internals](DEVELOPMENT.md#agent-skill-internals-and-source-pinning).

## Why use this repository?

**What is new here—and what is not:** OWASP ASVS, NIST AI RMF, accessibility guidance and established release-readiness practices already cover many of these topics. The repository's contribution is a cross-scope synthesis with stable IDs, agent-assisted retrieval, bounded review generation and evidence-record conventions—not novel security standards or an independent certification. Its source files have not all received independent expert or field validation; low or high GitHub engagement is not a substitute for that evidence. See [authorship and validation limits](AUTHORSHIP.md).

- **Spot blind spots earlier.** Surface overlooked requirements, security risks, accessibility gaps, operational dependencies, and AI-specific failure modes.
- **Make reviews actionable.** Checks are written to prompt verification, not just agreement. Record evidence, ownership, exceptions, and follow-up work in your project's review records.
- **Create a shared language.** Stable checklist IDs make it easier to discuss findings across engineering, product, QA, security, and operations.
- **Start wherever you are.** Use relevant checks during discovery, implementation, release review, or post-launch changes—not only on launch day.
- **Adapt to your context.** Choose the scopes and checks that matter for your product, rather than treating every item as mandatory.

## Explore the checklists

All 91 numbered checklist files live in [`lists/`](lists/): shared checklists directly in `lists/`, and the other scopes in `lists/frontend/`, `lists/backend/`, and `lists/AI/`. The repository separates shared concerns from implementation-specific checks so that each review can focus on the right work. **AI-specific interface checks (including fine-tuning dashboards and agent interfaces) live under `lists/AI/` in their domain's `Frontend Checks` section**, rather than as separate AI-domain files under `lists/frontend/`. General frontend checks remain under `lists/frontend/`.

| Scope | Files | Checks | What it covers |
| --- | ---: | ---: | --- |
| **[Shared / cross-cutting](lists/)** | 14 | 701 | Planning, legal considerations, architecture, security, testing, reliability, operations, metrics, and launch decisions |
| **[Frontend](lists/frontend/)** | 20 | 684 | UI/UX, accessibility, browser/API integration, performance, SEO, operations, and release checks |
| **[Backend](lists/backend/)** | 35 | 1,118 | APIs, data management, services, infrastructure, security, operations, and applicable AI integrations |
| **[AI](lists/AI/)** | 22 | 1,712 | Model selection, training, RAG, agents, evaluation, guardrails, monitoring, and their AI-specific frontend integration checks |
| **Total** | **91** | **4,215** | |

*Counts reflect the repository's current inventory and may change as checklists evolve. Numbered filenames reflect the historical organization within each `lists/` folder; existing filename prefixes are frozen to preserve external links, and future gaps are allowed. Stable checklist IDs, not filename numbers, are the durable review references.*

For inventory validation commands, machine-readable exports, stable ID ownership, and source freshness, see [DEVELOPMENT.md](DEVELOPMENT.md).

### Begin with a smaller, risk-tiered review

For a first pass, use the [Core 50 starter review](lists/references/core-50.md): **12 shared, 12 frontend, 12 backend and 14 AI checks**, all drawn from existing stable IDs. Choose **only applicable** scopes and add checks for your system's architecture, threat model, industry, and intended release. It is a **starter set, not a certification or a universally sufficient minimum**.

The curated checks have contextual `P0` (potential release blocker), `P1` (important assurance) and `P2` (supporting/contextual) labels. **These 50 retain manually curated priorities**. The remaining **4,165 checks now have provisional text-derived P0/P1/P2 labels**, which require context-specific review; labels are not audited severity determinations or permission to skip a control. A reviewer must assign project-specific severity and review the applicable domain release gates.

For a real, evidence-linked example, see the [sample review of this repository](lists/references/example-review.md). The [agent-control overlap assessment](lists/references/overlap-review.md) distinguishes policy, enforcement and test evidence instead of silently deleting stable IDs. The reported **4,215** counts unique checklist IDs; it is **not a verified semantic-deduplication count**.

### Choose the review depth

| Review depth | Practical entry point | What it establishes |
| --- | --- | --- |
| **First pass** | [25 per scope](lists/references/minimum-viable-by-scope.md) or [Core 50](lists/references/core-50.md) | A bounded set of candidate risks, with all project results initially UNKNOWN |
| **Release review** | [Scoped 25–100-check generator](lists/references/scoped-review-generator.md), additional applicable controls, all release gates | A project-specific, evidence-backed go/no-go decision by an authorized reviewer |
| **Expanded audit** | Wider checklist selection, versioned primary requirements and independent testing | Deeper assurance for the actual system, not automatic certification from checklist completion |

No fixed number of checks guarantees readiness. Priorities outside the Core 50 are provisional; scope, architecture and threat model determine what must be reviewed.

### Good places to start

| If you're working on… | Open these checklists |
| --- | --- |
| **A new project** | [Requirements & planning](lists/01_Requirements_and_Planning.md) · [Architecture & code quality](lists/03_Architecture_and_CodeQuality.md) |
| **A product or release review** | [Security](lists/05_Security.md) · [Testing](lists/08_Testing.md) · [Release & launch readiness](lists/14_Release_and_LaunchReadiness.md) |
| **A user-facing application** | [Frontend UX & usability](lists/frontend/04_UI_UX_and_Usability.md) · [Accessibility](lists/frontend/05_Accessibility.md) |
| **An API or data platform** | [Backend API design](lists/backend/07_API_Design_and_Integrations.md) · [Data & database management](lists/backend/08_Data_and_DatabaseManagement.md) |
| **An AI-powered product** | [AI evaluation & governance](lists/AI/03_AI_Evaluation_and_Governance.md) · [RAG & knowledge bases](lists/AI/10_RAG_and_Knowledge_Bases.md) · [Agents & tool orchestration](lists/AI/11_AI_Agents_and_Tool_Orchestration.md) |

Browse the complete [lists/frontend/](lists/frontend/), [lists/backend/](lists/backend/), and [lists/AI/](lists/AI/) directories, or use [AGENTS.md](AGENTS.md) for the detailed domain inventory, stable ID conventions, and maintenance guidance.

## How to use these checklists

1. **Select the relevant scopes.** Start with applicable shared checks, then add frontend, backend, and/or AI checklists based on the actual components and risks of your project. Not every folder applies to every project.
2. **Create versioned project review records.** Keep the reusable source templates unchecked; preferably generate a project-specific UNKNOWN-first review and retain the pinned JSON catalog, source SHA, product revision, reviewers and evidence. If you copy Markdown, [compare upstream revisions](lists/references/downstream-update-guide.md) before reusing prior PASS decisions.
3. **Verify—don't assume.** Mark `[x]` only when a check has actually passed and supporting evidence has been recorded in your project's review notes, test artifacts, or issue tracker.
4. **Explain exceptions.** Keep failed or pending checks open. Document `N/A` with a reason, and track material issues or accepted risks with owners, deadlines, and the relevant stable checklist IDs.
5. **Review the release gates.** Evaluate each domain's release gate across all applicable scope files, with appropriate human approval. A repeated gate is not a separate approval.
6. **Revisit after meaningful changes.** New features, vendors, models, policies, markets, deployments, or incidents can invalidate yesterday's assumptions.

**A checked box should mean “we verified this,” not “we hope this is fine.”**

## Display the “Reviewed with awesome-checklists” badge

Projects that have **actually carried out and documented** an applicable awesome-checklists review can display a voluntary, **self-declared** badge in their own README. The larger badge includes a checkmark to indicate a checklist-based review—not approval, certification, or a verified passing result:

![Reviewed with awesome-checklists — badge preview](https://img.shields.io/badge/%E2%9C%93%20Reviewed%20with-awesome--checklists-168554?style=for-the-badge&labelColor=0C2946)

Copy this Markdown into your project's README (no badge hosting required):

```markdown
[![Reviewed with awesome-checklists](https://img.shields.io/badge/%E2%9C%93%20Reviewed%20with-awesome--checklists-168554?style=for-the-badge&labelColor=0C2946)](https://github.com/Pro-GenAI/awesome-checklists)
```

For a self-hosted SVG badge option, see [badge assets](DEVELOPMENT.md#self-hosted-review-badge).

> [!IMPORTANT]
> **This is a maintainer's self-declaration of having used the checklists, not an approval issued by Pro-GenAI or an independent audit.** The badge does not certify security, compliance, accessibility, AI safety, or release readiness. Display it only after relevant checks were evaluated and results, outstanding risks, and exceptions were documented. Include a link to the project's own review summary where appropriate, and update or remove the badge if its basis is no longer current.

## Important: a reference, not the final word

> [!WARNING]
> **These checklists are a starting point—not the ultimate, exhaustive, universally applicable, or authoritative source of truth.**
>
> They represent review prompts and practical references, **not official standards, certifications, legal advice, or a guarantee** of security, compliance, accessibility, reliability, AI safety, product quality, or release readiness.
>
> Requirements depend on your architecture, users, risk profile, industry, jurisdiction, and the versions of standards and tools you use. Some checks may be inapplicable; others may be missing, incomplete, or become outdated. Always verify important claims against current primary sources and involve qualified reviewers where needed.
>
> **Use professional judgment. Challenge the checklist. Never mistake checklist completion for proof that a system is safe or ready.**

## Development and maintenance

Repository architecture, ID registries, source pinning, export/generator commands, validation, CI, source provenance and technical implementation examples are documented in [DEVELOPMENT.md](DEVELOPMENT.md). For contribution requirements see [CONTRIBUTING.md](CONTRIBUTING.md), and for agent-maintainer instructions see [AGENTS.md](AGENTS.md).

## License

Original checklist text, editorial curation and documentation for which Pro-GenAI has sufficient rights are offered under [CC0 1.0 Universal](LICENSE) for low-friction reuse. Original Python and JavaScript source code, website tooling, automation scripts and reusable skill code remain under the [MIT License](LICENSE-CODE). Linked third-party standards, logos, trademarks, excerpts and separately attributed materials retain their respective rights; CC0 does not waive others' rights. Maintainers should confirm they have rights to apply CC0 to previously contributed material before merging this license change.

## Contributions and suggestions are encouraged

**Found a gap? Disagree with a check? Have a better reference or clearer way to verify something? We want to hear it.**

This collection is intended to improve through practical experience, constructive criticism, and fresh evidence. Suggestions are welcome whether they propose a new check, correct an existing one, clarify applicability, or remove a misleading requirement.

- **[Open an issue](https://github.com/Pro-GenAI/awesome-checklists/issues)** to propose an improvement or report an outdated, ambiguous, duplicated, or missing check.
- **Make the suggestion specific.** Include the relevant file and checklist ID (if any), the proposed change, why it matters, where it applies, and a current primary reference when possible.
- **Contribute or report a gap.** See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution and review procedures, or [AGENTS.md](AGENTS.md) for stable-ID conventions and local checks.
- **Small improvements count.** Clearer wording, corrected links, stronger caveats, and well-supported counterexamples make the collection more useful.

The goal is not to defend every existing item. **The goal is to make the questions better.**

---

**Use what helps. Question what doesn't. Contribute what is missing.**
