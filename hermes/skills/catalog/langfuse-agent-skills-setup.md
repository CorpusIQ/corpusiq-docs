---
title: "Langfuse Agent Skills — LLM Observability Setup"
description: "langfuse/skills — 6 skills, 13.1K installs: LLM tracing, prompt management, and observability workflows from the Langfuse team."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/langfuse-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "llm", "observability", "langfuse"]
---

# Langfuse Agent Skills — Setup Guide

**Source:** [langfuse/skills](https://skills.sh/langfuse/skills)
**GitHub:** [langfuse/skills](https://github.com/langfuse/skills)
**Skills:** 6 skills · 13.1K total installs
**Category:** LLM Observability
**First Seen:** catalogued August 15, 2026 evening sweep
**Quality Tier:** 🟢 Production (official org — Langfuse, the LLM observability platform)

Langfuse's official skills teach agents to instrument LLM calls with tracing, manage prompts, and run observability workflows. For a multi-model operation like CorpusIQ — DeepSeek primary, Claude fallbacks, cost tracking — tracing is how you see where tokens and money actually go.

---

## Installation

```bash
npx skills add langfuse/skills
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Langfuse account** | Self-hosted or cloud, with API keys |
| **Langfuse SDK** | In the instrumented application |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| langfuse | 12.7K | Core tracing and observability |
| langfuse-observability | 217 | Observability patterns |
| langfuse-prompt-migration | 87 | Migrate prompts into Langfuse management |
| langfuse-api | 56 | API reference workflows |
| langfuse-cli | 1 | CLI usage |
| skill-creator | 4 | Skill authoring helper |

## Quick Start

1. Install: `npx skills add langfuse/skills`
2. Start with the core `langfuse` skill — it carries 97% of the suite's installs
3. Ask: "instrument my agent loop with Langfuse tracing and show cost per model"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Model cost tracking** | Trace every LLM call to attribute spend per model and task |
| **Agent debugging** | Full traces of multi-step agent runs instead of guessing where a loop degraded |
| **Prompt management** | prompt-migration to move prompts out of code and into versioned management |
| **Client observability** | Reference architecture for clients building LLM-powered products |

## Limitations / Verification

- Publisher-page install counts verified; individual skill audit pages were not fetched for this multi-skill suite
- The core skill dominates: observability, API, and CLI skills show sub-1K installs — treat as early content
- Requires a running Langfuse instance and SDK integration to be useful

```bash
npx skills add langfuse/skills   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
