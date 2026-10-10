---
title: "LangSmith Skills - LLM Evaluation & Tracing Setup"
description: "Setup guide for langchain-ai/langsmith-skills - 14.4K combined installs. Official LangSmith skills for tracing, datasets, and evaluation engineering."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/langsmith-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "langsmith", "llm observability", "evals", "tracing"]
---

# LangSmith Skills - Setup Guide

**Source:** [langchain-ai/langsmith-skills](https://www.skills.sh/langchain-ai/langsmith-skills) via skills.sh - 14.4K combined installs across 5 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [langchain-ai/langsmith-skills](https://github.com/langchain-ai/langsmith-skills) (160 stars, MIT; branch main, pushed 2026-10-02; nonstandard layout: `config/skills/<name>/SKILL.md`)
**Category:** LLM Evals / Observability
**Quality Tier:** 🟢 Production - official LangChain; MIT; active Oct 2026; Snyk Warn on two sampled skills - see Security

LangSmith Skills is an official suite from the LangChain team for observing and evaluating LLM applications with LangSmith. The five indexed skills cover trace querying and export, evaluation datasets built from real traces, custom evaluator engineering, LangSmith Custom Apps, and online evaluators for production traffic. With 160 GitHub stars and 14.4K combined installs across five indexed listings on skills.sh, it is a focused, single-purpose companion to the wider LangChain skills ecosystem.

It is a sibling of langchain-ai/langchain-skills (see the [LangChain Agent Skills setup guide](/hermes/skills/catalog/langchain-skills-setup)): langchain-skills is for building and improving agents with LangChain, LangGraph, and Deep Agents, while langsmith-skills is for observing and evaluating what those agents do. The skills live in a nonstandard location, `config/skills/<name>/SKILL.md`, and several ship with Python and TypeScript helper scripts. A natural workflow is trace first, then dataset, then evaluator.

---

## Installation

Prerequisites: Node.js for the `npx skills` CLI, plus a LangSmith API key. Install all five skills into the current project:

```bash
npx skills add langchain-ai/langsmith-skills --skill '*' --yes
```

Install for all projects:

```bash
npx skills add langchain-ai/langsmith-skills --skill '*' --yes --global
```

Claude Code users can install it as a plugin instead:

```bash
/plugin marketplace add langchain-ai/langsmith-skills
/plugin install langsmith-skills@langsmith-skills
```

The bundled install script works for Claude Code and Deep Agents CLI only. From a clone of the repo:

```bash
./install.sh --global
./install.sh --deepagents --global
```

After installation, set your API keys so the helper scripts and the agent can reach LangSmith:

```bash
export LANGSMITH_API_KEY=<your-key>
export OPENAI_API_KEY=<your-key>
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| langsmith-evaluator | 4,764 | Creating custom evaluators for scoring LLM outputs (includes helper scripts) |
| langsmith-trace | 4,724 | Querying and exporting LangSmith traces (includes helper scripts) |
| langsmith-dataset | 4,629 | Generating evaluation datasets from real traces (includes helper scripts) |

The remaining 2 indexed listings range from 71 to 261 installs.

## Why This Matters for Hermes Agents

LLM applications fail in ways that only traces reveal: wrong tool choices, silent regressions between model versions, and drift after prompt edits. An agent that can query traces, turn them into datasets, and codify checks as evaluators closes that loop without a human relaying data between tools. That trace-dataset-evaluator cycle is a multi-step workflow agents handle well, and this suite ships helper scripts so the agent starts from working code rather than blank files. The skills are official and MIT-licensed, which keeps adoption friction low for internal projects. Any agent that supports skills.sh installs can use them, including Claude Code, Cursor, Windsurf, Goose, and Deep Agents CLI.

## Usage

| You say | What happens |
|---|---|
| Find the traces from last night's failed agent run | langsmith-trace queries and exports the matching traces for inspection |
| Turn 50 good production traces into an evaluation dataset | langsmith-dataset builds a reusable dataset from the selected traces |
| Write an evaluator that checks whether answers cite sources | langsmith-evaluator creates the evaluator and its helper scripts |
| Set up an online evaluator for production traffic | langsmith-online-eval-engineering designs, tests, and attaches online evaluators |
| Build a Custom App to review flagged runs | langsmith-custom-apps builds, replicates, verifies, and shares the app |
| Export a week of traces for offline analysis | langsmith-trace exports the traces for local analysis |

## Verification

Confirm the install landed:

```bash
npx skills list | grep langsmith
```

A local install places the skills where your coding agent reads them; the repo's own sources live at `config/skills/<name>/SKILL.md`. Review a skill's instructions before installing it - this raw file is served straight from the repo's main branch:

```bash
curl -sL https://raw.githubusercontent.com/langchain-ai/langsmith-skills/main/config/skills/langsmith-trace/SKILL.md | head -40
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| langsmith-evaluator | Pass | Pass | Warn |
| langsmith-trace | Pass | Pass | Warn |
| langsmith-dataset | Pass | Pass | Pass |

## Limitations

- The project is in early development; the README warns that APIs and skill content may change.
- Snyk reports Warn on two of the three sampled skills (langsmith-evaluator and langsmith-trace); review those pages before production use.
- Nonstandard layout: skills live under `config/skills/<name>/SKILL.md` rather than a top-level skills directory, which is unusual and worth knowing when you inspect the install.
- The bundled install script supports Claude Code and Deep Agents CLI only; other agents should use the `npx skills` path.
- A LangSmith API key is required before the skills can do anything useful.


- Snapshot data, verified Oct 10, 2026: 14,449 combined installs across 5 indexed listings; 160 GitHub stars; MIT; last pushed 2026-10-02. Counts drift over time.

## Related

- [LangChain Agent Skills - Memory, RAG, Persistence & Middleware Setup](/hermes/skills/catalog/langchain-skills-setup) - sibling suite for building LangChain and LangGraph agents
- [Deep Agents Memory - LangChain Persistent Memory Setup](/hermes/skills/catalog/deep-agents-memory-setup) - persistent memory patterns for Deep Agents
- [OpenAI Agents Python Skills - Multi-Agent Setup](/hermes/skills/catalog/openai-agents-python-skills-setup) - skills for a different agent framework
- [Datadog Agent Skills - Observability & Monitoring Setup](/hermes/skills/catalog/datadog-agent-skills-setup) - broader observability coverage alongside LangSmith
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Set LANGSMITH_API_KEY (and a model provider key) before your first request; the helper scripts read them from the environment.
- Work the cycle in order: export traces with langsmith-trace, build a dataset from them, then codify checks as evaluators.
- Install globally with `--global` when building across multiple projects, or keep it local for a single repo.
- Re-run `./install.sh --force` after pulling repo updates to refresh skill content in place.
- Check the security pages for langsmith-evaluator and langsmith-trace specifically, since those carry the two Snyk warnings.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
