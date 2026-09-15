# Agent Capability Audit — the "4 must-install plugins" test

*Last updated: 2026-09-15*

A popular Hermes-ecosystem creator published a checklist video: "Do not run Hermes
Agent another week without installing these 4 plugins first." The video names no
products — it names four **capabilities**. We transcribed the video and audited the
CorpusIQ stack against each one.

## The 4 capabilities (from the video)

1. **Live cost control** — monitors what the agent actually spends on model usage
   while it runs, so you find out before the bill arrives.
2. **Model picker** — switch models on the fly instead of being locked into the
   setup-time configuration: cheap models for grunt work, expensive ones when the
   task demands it.
3. **Goal management** — the agent holds objectives across sessions instead of
   thinking one conversation at a time.
4. **Agent bridge** — lets your agent hand work to your other agents instead of you
   copying context around manually. The same suite includes WhatsApp and Discord
   voice bridges.

## CorpusIQ stack mapping

| Capability | What we run | Verdict |
|---|---|---|
| Live cost control | Token-usage monitoring on every session plus cost attribution tracking across the fleet | Covered |
| Model picker | A model router with a cost ladder (cheap primary, escalation tiers for complex work) | Covered |
| Goal management | Semantic memory + session handoff + knowledge-graph notes so objectives persist across sessions | Covered |
| Agent bridge | MCP server for tool sharing across agents + Telegram channel for human delivery | Partial — no WhatsApp/Discord voice bridges |

## Takeaway

The checklist is satisfied by Hermes-native capabilities (cost tracking, model
routing, persistent memory, MCP) — no third-party plugin is required to cover the
four categories. The one genuine gap versus the creator's suite is the **WhatsApp
and Discord voice bridge** layer; the CorpusIQ fleet currently delivers through
Telegram. If agent reach on WhatsApp/Discord becomes a priority, that layer is the
addition to make.
