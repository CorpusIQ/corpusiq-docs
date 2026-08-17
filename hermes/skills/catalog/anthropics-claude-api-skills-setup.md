---
title: "Anthropic Claude API Skills — Official Claude API"
description: Anthropic's official Claude API skill — model IDs, pricing, streaming, tool use, MCP, caching, token counting. 52.6K installs. The definitive Claude API reference for agent development.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/anthropics-claude-api-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Anthropic Claude API Skills — Setup Guide

**Source:** [anthropics/skills](https://skills.sh/anthropics/skills) (52.6K installs)
**GitHub:** [anthropics/skills](https://github.com/anthropics/skills) (164,242 ⭐)
**Category:** AI / LLM Platform
**Quality Tier:** 🟢 Production

Anthropic's official skills repository — home of the Claude API reference skill. This is the authoritative source for Claude model IDs, pricing, parameters, streaming, tool use, MCP integration, prompt caching, and token counting. While the repo hosts only one skill on skills.sh, the GitHub repository (164K stars) is Anthropic's primary public skills distribution channel.

---

## Installation

```bash
# Core Claude API reference
npx skills add anthropics/skills --skill claude-api
```

> **Note:** This repo is Anthropic's official agent skills distribution. The GitHub repository at 164K stars hosts the full skill catalog for Claude Code, while skills.sh surfaces the `claude-api` skill as the entry point for API integration.

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **claude-api** | 52.6K | Claude API / Anthropic SDK — model IDs, pricing, params, streaming, tool use, MCP, agents, caching, token counting, model migration |

---

## 🔑 Why This Matters

### The Definitive Claude API Reference
This skill triggers before ANY Claude/Anthropic-related work — it intercepts queries about model selection, pricing, limits, caching, and API parameters, ensuring agents use current data rather than training-cutoff knowledge. It prevents common errors like outdated model IDs, incorrect pricing assumptions, and wrong parameter combinations.

### Automatic Trigger Rules
The skill activates when:
- Any form of "Claude" or "Anthropic" is mentioned (Fable, Opus, Sonnet, Haiku, `anthropic`, `@anthropic-ai`, `claude-*`)
- User asks about LLM pricing, model choice, limits, or caching
- Task involves agent, MCP, tool definitions, multi-agent, RAG, LLM-judge, or computer use
- Task involves generation, summarization, extraction, classification, rewriting, or NL conversation

### Smart Skip Logic
The skill skips itself when:
- Another provider is explicitly being worked on (OpenAI/GPT/Gemini/Llama/Mistral/Cohere/Ollama)
- Project codebase grep shows non-Anthropic provider imports

---

## Hermes Agent Use Cases

- **Model Selection**: Automatically determine the right Claude model for each task based on cost, capability, and context needs
- **Tool Use & MCP**: Reference for implementing function calling and MCP server integration in Hermes agents
- **Prompt Caching**: Optimize token costs by caching frequently-used system prompts and context
- **Streaming**: Implement streaming responses for real-time agent output
- **Token Counting**: Accurately estimate and track token usage for cost management

---

## Discovery Method

Publisher sweep via `npx skills find "api" --owner "anthropics"`. While `anthropics/knowledge-work-plugins` and `anthropics/claude-code` were previously catalogued (July 23-24 sweeps), the `anthropics/skills` repo itself — home of the `claude-api` skill at 52.6K installs — was not. The GitHub repository is Anthropic's primary skills distribution channel at 164K stars.

---

## Notes

- **164K GitHub stars** make this the most-starred skills repository documented — surpassing Google Skills (15K), HashiCorp (759), and Cloudflare (2.5K) combined
- The single `claude-api` skill at 52.6K installs on skills.sh undercounts the repo's actual impact — most users interact through GitHub directly
- This skill should be loaded as a reference skill rather than an active workflow — it's a knowledge base, not a task executor
- Critical for Hermes agents that use Claude as a backend model — ensures correct API usage, cost estimation, and feature availability
