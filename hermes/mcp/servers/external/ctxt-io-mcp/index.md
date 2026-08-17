---
title: "ctxt.io MCP - CorpusIQ Docs"
description: Auto-expiring share links over MCP — turn agent-produced diffs, logs, reports and HTML into links that expire on their own, with read-back and delete tools. No account, no API key, free for links up to one day.
category: Developer Tools
stars: n/a (new listing)
added: 2026-08-16
source: mcpservers.org
relevance: ★★
tags: [sharing, pastes, links, agent-output, productivity, stateless]
---

# ctxt.io MCP

**Stateless sharing server (Streamable HTTP, no auth)** — ctxt.io turns anything an agent produces — diffs, logs, reports, HTML — into a shareable link that expires on its own, and lets the agent read it back later. No account, no API key, nothing to install. Client-side packaging (Claude Code plugin, Codex plugin, the `/share` skill) is open source.

```
Server type: Hosted remote (Streamable HTTP, stateless)
Auth: None
Endpoint: https://ctxt.io/mcp
Tools: create_context, read_context, delete_context
Pricing: Free (TTL up to 1 day) · Pro $1 per 30-day link with custom name and password
Category: Developer Tools
Built by: github.com/ctxt-io/ctxt-agents (registered io.ctxt/mcp)
```

## Why This Matters for Operators

Agents produce a lot of output that has to get to a human: deployment summaries, comparison tables, audit write-ups. Pasting it into chat loses formatting; emailing files creates a trail nobody manages. ctxt.io gives the agent a share link with an expiry policy — 5 minutes for a scratch answer, 8 hours for a workday handoff, 30 days for a permanent record — and the `delete_token` closes the loop.

The visual-output feature is the sleeper: `format=html` accepts self-contained HTML with inline CSS and SVG, scripts stripped server-side, so an agent can produce a styled report or chart and hand over a rendered link instead of markdown. The $1 Pro path is itself interesting — the tool result carries an ACP (Agentic Commerce Protocol) block and an enrolled agent platform can complete the purchase programmatically with a Stripe Shared Payment Token, one of the cleanest agentic-payment implementations in this catalog.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `create_context` | Share content (up to 4MB) as an expiring link — text, markdown, code, or rendered HTML |
| `read_context` | Fetch a link back as markdown, text, or HTML |
| `delete_context` | Destroy a link using its `delete_token` |

TTLs: 5m, 30m, 1h, 8h, 1d (free) or 30d (Pro). Every paste URL has robot-readable twins — append `.md`, `.txt`, or `.json` for structured fetch.

## Installation

```bash
claude mcp add --transport http ctxt https://ctxt.io/mcp
```

Or add the plugin (`/plugin marketplace add ctxt-io/ctxt-agents`, then `/plugin install ctxt@ctxt`), which ships a `/share` command and a skill that teaches the agent when to share and how to produce good HTML output. Codex: `codex mcp add ctxt --url https://ctxt.io/mcp`. Claude Desktop: Settings → Connectors → Add custom connector → `https://ctxt.io/mcp`.

## Business Relevance

- **Ops handoffs** — agent-generated summaries as links with sane expiry instead of chat-paste
- **Report delivery** — styled HTML reports render in the browser with no file exchange
- **Audit hygiene** — links die on their own, so yesterday's draft does not linger in inboxes
- **Agent pipelines** — one agent's output becomes the next agent's `read_context` input

## Integration with CorpusIQ

ctxt.io is the delivery envelope for CorpusIQ's analytical output: a CorpusIQ-driven report (revenue recaps, pipeline summaries, connector health) becomes a rendered HTML link with an 8-hour expiry, shared to a stakeholder channel, and read back by the next session's agent. The combination keeps sensitive business numbers out of permanent chat history — the link expires, the transcript does not.

## Limitations

- Bearer-accessible by design — anyone with the URL can read it until expiry; password protection is Pro-only
- Content is stored in plain form at rest (password protection is an access gate, not encryption)
- Free links cap at 1-day TTL; longer retention costs $1 per link
- Creating pastes outside MCP is a Terms violation — automation belongs in the MCP surface

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
