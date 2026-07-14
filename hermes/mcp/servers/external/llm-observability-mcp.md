---
title: "LLM Observability MCP (LangTrace) — Open Source Monitoring for AI Agents"
description: "Open source LLM observability proxy. Drop-in for OpenAI, Anthropic, Gemini with request logging, cost tracking, and agent tracing. Self-host with Docker. MIT."
category: mcp
tags: [mcp-server, devops, llm, observability, monitoring, cost-tracking, agent-tracing]
last_updated: 2026-07-14
---

# LLM Observability MCP Server (LangTrace) ★ New (July 14)

Open source LLM observability and monitoring via MCP. A drop-in proxy for OpenAI, Anthropic, and Gemini that captures request logs, tracks costs, and traces agent workflows — all self-hosted with a single Docker command. MIT licensed.

**Source:** mcp.so (exact repo TBD — GitHub search API rate-limited)
**Submitted:** July 14, 2026

## Key Features

- **Drop-in proxy:** Works as a transparent proxy for OpenAI, Anthropic, and Gemini APIs — no code changes required
- **Request logging:** Full request/response capture for debugging and auditing
- **Cost tracking:** Per-agent, per-model, and per-request cost attribution
- **Agent tracing:** Trace multi-step agent workflows across LLM calls
- **Self-hosted:** One Docker command to deploy — data stays on your infrastructure
- **MIT license:** Permissive open source, no vendor lock-in

## Business Relevance

As operators deploy AI agents in production, observability becomes critical. You need to know:
- What is each agent calling and how much is it costing?
- Which prompts are consuming the most tokens?
- Are agents making redundant or expensive calls?
- How do multi-agent workflows trace end-to-end?

This MCP server brings production-grade LLM observability to any MCP-compatible agent environment. Essential for operators running AI agents at scale who need cost controls and debugging capabilities.

## Integration with CorpusIQ

Complements CorpusIQ's business data access by adding the observability layer operators need to run AI agents in production. Use CorpusIQ to pull business data and LangTrace to monitor the agents doing the pulling — full visibility into both data access and AI costs.

## Limitations

- Exact GitHub repo TBD (GitHub search API rate-limited as of July 14)
- Requires Docker for self-hosting
- Proxy approach adds latency (minimal for observability use cases)
