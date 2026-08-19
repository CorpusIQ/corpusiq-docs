---
title: "Misar.Blog MCP - Publish and Manage Blog Content from AI Agents"
description: "Misar.Blog MCP server with 23 tools for content operations: create and publish articles, manage series, query analytics, handle comments and reactions, manage newsletter subscribers and generate AI-assisted content"
category: Content & Publishing
stars: n/a (new listing)
added: 2026-08-19
source: "mcp.so GitHub issue #3643"
relevance: ★★
tags: [blog, publishing, content, series, analytics, comments, newsletter, remote-mcp, npm]
---

# Misar.Blog MCP

**Blog publishing from any MCP client — create and publish articles, manage series, query analytics, handle comments and reactions, manage newsletter subscribers, and generate AI-assisted content with 23 tools.** Available as a local npm server or a hosted streamable-HTTP endpoint, with an optional API key (the server answers `initialize` and `tools/list` unauthenticated and exposes a browser `login` tool).

```
Server type: Local (npm, stdio) or Remote (Streamable HTTP)
Auth: Optional API key (browser login tool included)
Endpoint: https://api.misar.io/blog/mcp
Package: npx -y @misarblog/mcp (v5.1.0, MIT)
Tools: 23 (each annotated readOnly/destructive/idempotent)
Pricing: Free tier available
Category: Content & Publishing
Built by: Misar AI
```

## Why This Matters for Operators

Content operators publish on a schedule, and the publishing flow is where schedule discipline dies: compose in one tool, paste into a CMS, track analytics in a third place, answer comments in a fourth. Misar.Blog moves the entire blog lifecycle into the agent session: an agent drafts, publishes, and updates articles, organizes series, pulls analytics, moderates comments, and manages newsletter subscribers — the full loop in one surface.

The tool-level annotations matter for agent safety: every tool declares whether it is readOnly, destructive, or idempotent, so an agent can reason about what a publish or delete will do before executing.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| Articles | Create, publish, and update articles and posts |
| Series | Manage article series and ordering |
| Analytics | Query post performance and readership analytics |
| Comments & reactions | Moderate comments and reactions |
| Newsletter | Manage newsletter subscribers |
| AI writing | AI-assisted content generation inside the workflow |

## Installation

```bash
npx -y @misarblog/mcp
```

Or add the remote server to any MCP client:

```json
{
  "mcpServers": {
    "misarblog": {
      "type": "http",
      "url": "https://api.misar.io/blog/mcp"
    }
  }
}
```

The API key is optional: `initialize` and `tools/list` answer unauthenticated, and the server exposes a browser `login` tool for interactive auth. For local stdio use, set `MISARBLOG_API_KEY` in the environment when a key is configured.

## Configuration

```json
{
  "mcpServers": {
    "misarblog": {
      "command": "npx",
      "args": ["-y", "@misarblog/mcp"],
      "env": { "MISARBLOG_API_KEY": "<optional>" }
    }
  }
}
```

Registry ID: `io.github.Misar-AI/misarblog-mcp`. MIT licensed, repository at `github.com/Misar-AI/misarblog-mcp`, platform at misar.blog.

## Business Relevance

- **Content operators** run the full publish loop (draft, publish, update) from the agent
- **SEO teams** manage series and track analytics without leaving the workflow
- **Community managers** moderate comments and reactions in the same surface
- **Newsletter owners** manage subscribers alongside the blog they promote
- **Automation builders** fold publishing into larger agent workflows via one endpoint

## Integration with CorpusIQ

CorpusIQ brings the measurement and money layer (GA4, Search Console, Stripe) while Misar.Blog brings the publishing execution layer. A content operator can run both in one agent session: CorpusIQ for traffic, search performance, and revenue attribution, Misar.Blog for drafting, publishing, and subscriber management — then close the loop from publish to traffic to revenue.

## Limitations

- New listing (Aug 2026), no track record; single-star repository
- Publishing targets the Misar.Blog platform, not WordPress or other CMSes
- Free tier scope not fully documented
- Hosted endpoint is a third-party dependency for remote use

## See Also

- [MisarMail MCP — Transactional Email and Campaigns](/hermes/mcp/servers/external/misarmail-mcp/)
- [MisarReach MCP — Outbound Sales and Lead Pipeline](/hermes/mcp/servers/external/misarreach-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
