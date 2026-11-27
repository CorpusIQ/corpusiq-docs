---
title: "Weights & Biases Skills - ML Experiment Tracking and Tracing"
description: "wandb/skills - 3.1K combined installs: Weights & Biases' official agent skills for ML experiment tracking and Weave/AgentLens tracing."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/wandb-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "weights and biases", "ml tracking", "weave", "agent tracing"]
---

# Weights & Biases Skills - Setup Guide

**Source:** [wandb/skills](https://www.skills.sh/wandb/skills) via skills.sh - 3.1K combined installs across 5 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 evening sweep)
**GitHub:** [wandb/skills](https://github.com/wandb/skills) - 76 stars, Apache-2.0 license, last pushed Nov 24, 2026, main branch; five skills under skills/<name>/SKILL.md, each with reference docs and Python helper scripts.
**Category:** ML Experiment Tracking and Agent Tracing (Weights & Biases)
**Quality Tier:** 🟠 Orange - 5 of 5 listings sampled: ten Pass, four Warn, and one Snyk Fail across 15 verdict cells (agentlens-tracing-instrument carries the Fail).

wandb/skills is Weights & Biases' official collection of agent skills for training models and building agents on the W&B platform, published under the Apache-2.0 license. The suite splits into two halves: model training (logging metrics, tracking experiments, analyzing runs, tuning hyperparameters) and agent building (tracing agentic apps, classifying traces into failure modes, evaluating models on labeled datasets, running online evaluations).

The centerpiece is wandb-primary, a broad skill covering W&B runs, Artifacts, Weave traces, Reports, Workspaces, Automations, Sweeps, Launch, and Agent Lens. Four focused skills wrap specific surfaces: wandb-eval-tables for EvalTable previews, wandb-autoresearch for bounded training research through W&B Launch, and weave-instrument plus agentlens-tracing-instrument for adding tracing to Python and TypeScript agents.

## Installation

The README documents a single skills-CLI command that installs the whole suite into the agent's skills directory:

```bash
npx skills add wandb/skills
export WANDB_API_KEY=<your-key>
```

A single skill can be installed with `npx skills add wandb/skills --skill <name>`. The `npx skills` utility targets major coding agent CLIs; add `--global` to install for all projects or `--agent <name>` to target a specific agent. The helpers are validated against recent SDK floors (Python >=3.13, wandb >=0.28.1, wandb-workspaces >=0.4.4, weave >=0.52.41); older SDKs expose some methods as unimplemented stubs.

## What It Provides

skills.sh publishes per-skill install counts for all 5 indexed listings; all five appear below.

| Skill | Installs | Use For |
|---|---|---|
| wandb-primary | 1,852 | broad or mixed W&B work: runs, artifacts, Weave traces, Reports, Workspaces, Automations, Sweeps, Launch, and Agent Lens |
| wandb-eval-tables | 419 | convert W&B Table artifacts into non-destructive, verified EvalTable previews with typed columns |
| wandb-autoresearch | 409 | run bounded, evidence-driven training research through W&B Launch with readiness checks and serial trials |
| weave-instrument | 221 | add Weave tracing to Python or TypeScript agents and LLM applications |
| agentlens-tracing-instrument | 221 | add Forge AgentLens tracing to Python or TypeScript agents |

No indexed listing falls below 200 installs; all 5 appear above.

## Why This Matters for Hermes Agents

Weights & Biases is a leading platform for ML experiment tracking and agent tracing, and this suite encodes its operational workflows into skills an agent can run directly. wandb-primary is the general entry point: it resolves broad or mixed W&B questions, so an agent does not need to know which surface (runs, Weave, Reports, or Sweeps) holds the answer. The focused skills each carry a reference layer plus Python helpers, turning advice into executable commands rather than prose. wandb-autoresearch is genuinely agent-native: it runs bounded, evidence-driven training research through W&B Launch, smoke-testing real jobs and persisting resumable state so a coding agent can autonomously tune a workload. weave-instrument and agentlens-tracing-instrument cover the tracing side, instrumenting model calls, tools, and agent turns in Python or TypeScript. The repo also ships Skill Bench, an eval harness that benchmarks each skill against task categories, so the skills are engineered and measured for non-interactive use.

## Usage

| You say | What happens |
|---|---|
| What is going on in my W&B project | Uses wandb-primary for a broad project overview across runs and Weave traces |
| Instrument my agent with Weave | Uses weave-instrument to trace model calls, tools, and agent turns |
| Turn this W&B Table into an eval table | Uses wandb-eval-tables to plan, type, batch, and verify a non-destructive EvalTable preview |
| Research a training hypothesis autonomously | Uses wandb-autoresearch to run bounded serial trials through W&B Launch |
| Add Forge AgentLens tracing to my agent | Uses agentlens-tracing-instrument to trace agent turns and subagents |
| Tune my hyperparameters | Uses wandb-primary Sweeps helpers to launch and compare sweep runs |

## Verification

Confirm the README and representative skill bodies resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/wandb/skills/main/README.md | head -60
curl -sL https://raw.githubusercontent.com/wandb/skills/main/skills/wandb-primary/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/wandb/skills/main/skills/wandb-autoresearch/SKILL.md | head -40
```

All three URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Fail verdict noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| wandb-primary | Pass | Warn | Pass |
| wandb-eval-tables | Pass | Pass | Warn |
| wandb-autoresearch | Pass | Warn | Warn |
| weave-instrument | Pass | Pass | Pass |
| agentlens-tracing-instrument | Pass | Pass | Fail |

Across the 5 sampled skills there are 10 Pass, 4 Warn, and 1 Fail cells. All five pass the Gen Agent Trust Hub; one skill (agentlens-tracing-instrument) carries a Snyk Fail.

## Limitations

- Snapshot data, verified Nov 26, 2026: 3,122 combined installs across 5 indexed listings; 76 GitHub stars; Apache-2.0 license; last pushed Nov 24, 2026. Counts drift over time.
- All five skills are marked experimental in the README's Available Skills table.
- The skill helpers require recent SDK floors (Python >=3.13, wandb >=0.28.1, weave >=0.52.41); older SDKs expose some methods as unimplemented stubs.
- agentlens-tracing-instrument carries a Snyk Fail verdict in the sample, so review it before production use.
- Installation supplies instructions, not application dependencies or credentials; an active W&B API key is still required.

## Related

[PyTorch Agent Skills - Contributor Workflow Suite](/hermes/skills/catalog/pytorch-agent-skills-setup) | [ModelStudio Skills - Alibaba Video and Data Tools](/hermes/skills/catalog/modelstudio-skills-setup) | [Scenario Labs Skills - Custom Model Training Setup](/hermes/skills/catalog/scenario-labs-skills-setup) | [Datadog Agent Skills - Observability & Monitoring Setup](/hermes/skills/catalog/datadog-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with wandb-primary for broad or mixed W&B questions; it routes to the focused skills for specific surfaces.
- Install a single skill with `npx skills add wandb/skills --skill <name>` when you only need one surface.
- Pin the SDK floors (Python >=3.13, wandb >=0.28.1, weave >=0.52.41) rather than relying on whatever is already installed.
- Use wandb-autoresearch for autonomous training hypotheses; it persists resumable research state across runs.
- Re-check the security pages on skills.sh for agentlens-tracing-instrument, which carries the sample's single Fail.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
