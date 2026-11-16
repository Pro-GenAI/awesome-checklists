<!--lint disable awesome-github-->
<!-- GitHub repository metadata must gain the `awesome` and `awesome-list` topics via the About editor. The connector cannot mutate topics; this is a temporary, rule-specific waiver. All other awesome-lint rules remain enabled. -->
# Awesome Checklists [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A focused, curated entry point to evidence-based checklists for production Generative AI, LLMOps and autonomous-agent workflows. Each checklist maps back to existing stable control IDs; none is a certification or a claim that tests have passed.

## Contents

- [Prompt and Context Engineering](#prompt-and-context-engineering)
- [RAG and Data Pipelines](#rag-and-data-pipelines)
- [Agent Safety and Runtime Guardrails](#agent-safety-and-runtime-guardrails)
- [Evaluation and Observability](#evaluation-and-observability)
- [Production Readiness](#production-readiness)

## Prompt and Context Engineering

- [Prompt and context review](https://github.com/Pro-GenAI/awesome-checklists/blob/main/checklists/prompt-context.md) - Check instruction boundaries, strict output contracts, context budgeting and prompt-injection regressions before a new prompt release.

## RAG and Data Pipelines

- [RAG and data review](https://github.com/Pro-GenAI/awesome-checklists/blob/main/checklists/rag-data.md) - Validate document chunking, embedding compatibility, retrieval judgments, index migrations and deletion propagation before serving new corpora.

## Agent Safety and Runtime Guardrails

- [Agent safety review](https://github.com/Pro-GenAI/awesome-checklists/blob/main/checklists/agent-safety.md) - Test least-privilege tool access, permission enforcement, injection resistance, handoff traces and streamed action safety.

## Evaluation and Observability

- [Evaluation and observability review](https://github.com/Pro-GenAI/awesome-checklists/blob/main/checklists/evaluation-observability.md) - Track versioned golden cases, deterministic assertions, retrieval relevance, user-facing latency and model usage costs.

## Production Readiness

- [Production readiness review](https://github.com/Pro-GenAI/awesome-checklists/blob/main/checklists/production-readiness.md) - Check cold starts, secrets, rate limits, dependency patching and provider throttling before a rollout.

For the complete 91-file library, evidence requirements and review toolchain, see the [main documentation](../README.md). Apply each list to your own threat model and retain project-specific evidence.
