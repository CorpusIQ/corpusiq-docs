---
title: "Agent Capability Audit - the 4 must-install plugins test"
description: "A creator's 4 must-install plugin test for Hermes agents, audited against the CorpusIQ stack: cost control, model picker, goal management, agent bridge."
category: best-practices
tags: [hermes-agent, agent-capabilities, cost-control, model-routing, memory, mcp]
last_updated: 2026-10-30
canonical: "https://www.corpusiq.io/docs/hermes/best-practices/agent-capability-audit/"
robots: "index,follow"
---
# Agent Capability Audit - the "4 must-install plugins" test

*Last updated: 2026-10-30*

A popular Hermes-ecosystem creator published a checklist video: "Do not run Hermes
Agent another week without installing these 4 plugins first." The video names no
products - it names four **capabilities**. We transcribed the video and audited the
CorpusIQ stack against each one.

## The 4 capabilities (from the video)

1. **Live cost control** - monitors what the agent actually spends on model usage
   while it runs, so you find out before the bill arrives.
2. **Model picker** - switch models on the fly instead of being locked into the
   setup-time configuration: cheap models for grunt work, expensive ones when the
   task demands it.
3. **Goal management** - the agent holds objectives across sessions instead of
   thinking one conversation at a time.
4. **Agent bridge** - lets your agent hand work to your other agents instead of you
   copying context around manually. The same suite includes WhatsApp and Discord
   voice bridges.

## CorpusIQ stack mapping

| Capability | What we run | Verdict |
|---|---|---|
| Live cost control | Token-usage monitoring on every session plus cost attribution tracking across the fleet | Covered |
| Model picker | A model router with a cost ladder (cheap primary, escalation tiers for complex work) | Covered |
| Goal management | Semantic memory + session handoff + knowledge-graph notes so objectives persist across sessions | Covered |
| Agent bridge | MCP server for tool sharing across agents + email delivery for human-facing reports | Partial - no WhatsApp voice bridge (Hermes covers Discord voice channels natively) |

## Takeaway

The checklist is satisfied by Hermes-native capabilities (cost tracking, model
routing, persistent memory, MCP) - no third-party plugin is required to cover the
four categories. The one genuine gap versus the creator's suite is the **WhatsApp
voice bridge**: Hermes voice mode covers the CLI and live conversations in Discord
voice channels natively, so Discord is not a gap. The CorpusIQ fleet delivers its
agent-to-human output by email. If agent reach on WhatsApp becomes a priority, that
bridge is the addition to make.
