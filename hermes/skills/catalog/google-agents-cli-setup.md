---
title: Google Agents CLI — Google's Official Agent Development Kit for Hermes
description: Build, evaluate, deploy, and observe AI agents with Google's ADK. 357K+ combined installs across 6 skills on skills.sh. Official Google agent infrastructure.
---

# Google Agents CLI — Setup Guide

**Source:** [google/agents-cli](https://skills.sh/google/agents-cli) (357K+ combined installs)
**Category:** Agent Infrastructure
**Quality Tier:** 🟢 Production

Google's official Agent Development Kit (ADK) — a complete workflow for building, scaffolding, evaluating, deploying, and observing AI agents. Six skills covering the full agent lifecycle. Production-grade, maintained by Google.

---

## Installation

```bash
# Install individual skills
npx skills add google/agents-cli --skill google-agents-cli-adk-code
npx skills add google/agents-cli --skill google-agents-cli-workflow
npx skills add google/agents-cli --skill google-agents-cli-eval
npx skills add google/agents-cli --skill google-agents-cli-scaffold
npx skills add google/agents-cli --skill google-agents-cli-deploy
npx skills add google/agents-cli --skill google-agents-cli-observability
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **google-agents-cli-adk-code** | 59.8K | Core ADK coding patterns — build agents with Google's framework |
| **google-agents-cli-workflow** | 59.6K | Define multi-step agent workflows with chaining and branching |
| **google-agents-cli-eval** | 59.5K | Evaluate agent performance with structured test suites |
| **google-agents-cli-scaffold** | 59.5K | Scaffold new agent projects from templates |
| **google-agents-cli-deploy** | 59.5K | Deploy agents to Google Cloud / Vertex AI |
| **google-agents-cli-observability** | 59.5K | Monitor agent runs with traces, logs, and metrics |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Google Cloud account** | Required for deploy and observability skills |
| **Python 3.10+** | Core runtime |
| **gcloud CLI** | For deployment workflows |

---

## Key Capabilities

### Agent Development (adk-code)
Full Google ADK development patterns — tool definitions, memory management, multi-turn conversations, streaming responses, and safety filters.

### Agent Workflows (workflow)
Chain agents together, define conditional branching, parallel execution, and human-in-the-loop checkpoints.

### Agent Evaluation (eval)
Structured eval harness — test datasets, metric definitions, regression detection, and A/B comparison between agent versions.

### Scaffolding (scaffold)
`adk init` equivalent — project templates, directory structures, config files, and CI/CD pipeline generation.

### Deployment (deploy)
Push agents to Vertex AI Agent Builder, Cloud Run, or GKE. Environment variable management and canary rollout support.

### Observability
OpenTelemetry-based tracing for agent runs, latency breakdowns by step, token usage tracking, and error rate dashboards.

---

## Quick Start

```bash
# Scaffold a new agent project
npx skills use google/agents-cli@google-agents-cli-scaffold

# Build the agent logic
npx skills use google/agents-cli@google-agents-cli-adk-code

# Define multi-step workflows
npx skills use google/agents-cli@google-agents-cli-workflow

# Evaluate before deploying
npx skills use google/agents-cli@google-agents-cli-eval

# Deploy to Google Cloud
npx skills use google/agents-cli@google-agents-cli-deploy

# Monitor in production
npx skills use google/agents-cli@google-agents-cli-observability
```

---

## Verification

```bash
npx skills list | grep google-agents-cli
```

---

## Notes

- Official Google product — actively maintained, frequent updates
- All 6 skills have near-identical install counts (~59.5K), indicating they're typically installed as a bundle
- Requires Google Cloud for deploy/observability skills; code/eval/scaffold work standalone
- Complements Hermes agent infrastructure for production deployment patterns
- Quality tier 🟢 Production: 357K+ combined installs, Google-maintained
