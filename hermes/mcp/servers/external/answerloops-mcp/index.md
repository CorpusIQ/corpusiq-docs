---
title: AnswerLoops MCP - Community Support Knowledge Base
description: "Open-source AI support infrastructure for community-driven teams. The MCP server exposes knowledge base search, FAQ lookup, ticket listing and creation, and grounded answer generation over JSON-RPC, with org-scoped API keys and deflection-limit metering. Self-hostable, AGPL-3.0."
category: Customer Support
stars: 2
added: 2026-09-03
source: "mcpservers.org /all listing (answerloops/answerloops)"
relevance: ★★
tags: [customer-support, community, knowledge-base, tickets, self-hosted]
---

# AnswerLoops MCP - Community Support Knowledge Base for Agents

**Self-hosted MCP server (JSON-RPC over HTTP, org API keys)** - the agent-facing surface of AnswerLoops, an open-source AI support agent that answers repeat questions in Discord, Slack, Discourse, GitHub, Telegram and email from your own docs, and escalates the rest with a draft attached.

## Spec Block

| Field | Value |
|---|---|
| Server name | answerloops |
| Repo | github.com/answerLoops/answerLoops |
| Endpoint | POST /api/mcp (cloud: app.answerloops.com, or your self-hosted instance) |
| Transport | MCP JSON-RPC over HTTP |
| Auth | Org API key sent as the bearer Authorization header (keys use the al_live_ prefix) |
| Tools | search_kb, get_faq, get_tickets, create_ticket, generate_answer |
| Channels | Discord, Slack, Discourse, Circle, GitHub Issues and Discussions, Telegram, email, web chat, Google Chat |
| License | AGPL-3.0 |
| Pricing | Self-host for free; hosted app with billing |

## Why This Matters for Operators

Teams whose support lives in chat channels spend hours answering the same questions. AnswerLoops takes the first pass with a confidence gate: every draft is scored against the evidence it used, answers above your threshold post on their own, and everything else waits in a human queue with context attached. The MCP server exposes the exact same pipeline - knowledge base, FAQ, tickets and grounded answer generation - to any agent, so support intelligence is available in the tools your team already runs.

## Tools & Capabilities (5 tools)

| Tool | Purpose |
|---|---|
| search_kb | Semantic search across crawled docs, uploaded files, published KB articles, resolved tickets and connected GitHub repos |
| get_faq | Read the latest FAQ generated from resolved conversations |
| get_tickets | List tickets from the unified inbox (all channels in one ticket model) |
| create_ticket | Create a ticket through the same validation, dedup and SLA path every channel uses |
| generate_answer | Generate a grounded answer draft through the same confidence-gated pipeline as channel replies |

The same five operations are also available as a REST API with an OpenAPI schema (/api/agent/*), using the same API key.

## Installation

Self-host with Docker Compose (Next.js app, channel listener, PostgreSQL), then:

```json
{ "mcpServers": { "answerloops": { "url": "https://your-instance.example.com/api/mcp", "headers": { "Authorization": "Bearer al_live_..." } } } }
```

Cloud users point the url at https://app.answerloops.com/api/mcp.

## Configuration

Create an org API key in Settings → API Keys (owners and admins only - a key grants read access to the whole org's tickets and knowledge base plus metered AI spend). Optional expiry of 30/90/365 days. The plaintext key is shown once and cannot be recovered.

## Business Relevance

Built for software and API companies, open-source projects, course creators running paid communities, game studios with a player Discord, and DAOs. The knowledge-gaps view shows which questions the system still cannot answer, so documentation effort lands where it counts. Deflection-rate and SLA analytics ship with the dashboard.

## Integration with CorpusIQ

The knowledge-gap and FAQ views feed directly into CorpusIQ's content and product decisions: export unanswered-question themes to prioritize docs, and cross-check support deflection metrics against revenue data from CorpusIQ connectors to measure support ROI.

## Limitations

AGPL-3.0: running a modified version as a network service requires publishing your source. Not a Zendesk-style helpdesk - it targets chat-channel support. Young repo (created Aug 19, 2026, 2 stars). Anonymous tool enumeration returns an empty list; tools are documented in the vendor MCP guide.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Asyntai MCP - AI Support Agent for Websites](/docs/hermes/mcp/servers/external/asyntai-mcp)
- [imap-mcp - Read-Only IMAP Mailbox Operations for Agents](/docs/hermes/mcp/servers/external/imap-mcp)
- [BusyMail MCP - Human-Approval Email over MCP](/docs/hermes/mcp/servers/external/busymail-mcp)
