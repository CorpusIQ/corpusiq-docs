---
title: "lucid.page MCP — Publish Markdown Pages Instantly from Any Agent"
description: "Zero-config remote MCP server that turns Markdown into a beautifully typeset shareable page: publish anonymously without signup, update in place with revisions, list and delete owned docs, and bind pages into multi-chapter bundles. Free."
category: Content & Publishing
stars: n/a (new listing)
added: 2026-08-21
source: mcp.so
relevance: ★★
tags: [markdown, publishing, docs, share, agent-output, bundles, no-signup, remote-mcp]
---

# lucid.page MCP

**The missing "publish" button for AI agents — Markdown in, shareable page out, no account required.** lucid.page runs a hosted MCP endpoint where one tool call publishes Markdown as a typeset page and returns its URL. Anonymous publishing works with no signup and pages never expire by default; a free `lp_` API key adds ownership, updates with revision history, private docs, multi-chapter bundles and rate headroom.

```
Server type: Remote (Streamable HTTP)
Auth: None for anonymous publish; optional Bearer lp_ API key for owned docs
Endpoint: https://lucid.page/mcp
Tools: 7 (publish, update, get, list, delete, bundle, limits)
Pricing: Free; Pro adds analytics
Category: Content & Publishing
Built by: Bitgate (lucid.page)
```

## Why This Matters for Operators

Agents produce a constant stream of valuable text — research reports, recaps, changelogs, field notes — that dies in the chat window because sharing it means pasting into Docs or Notion by hand. **lucid.page gives the agent a publish action**, so "write up the competitor analysis and send me a link" becomes two tool calls and a clean URL a human can open on any device.

Anonymous publish returns a one-time claim token the human can use to claim the page into their account — the agent can publish freely without ever holding credentials that could edit anything it shouldn't.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `publish_doc` | Publish Markdown as a typeset page; returns the lucid.page URL. Anonymous works |
| `update_doc` | Replace a page's Markdown in place; every update kept as a revision |
| `get_doc` | Fetch the canonical Markdown source of a page |
| `list_docs` | List documents and bundles owned by the account, newest first |
| `delete_doc` | Permanently delete a page you own |
| `create_bundle` | Bind pages into a multi-chapter bundle with landing page and navigation (up to 200 chapters) |
| `get_limits` | Show the account matrix and plan status |

## Installation

```bash
claude mcp add lucid-page --transport http https://lucid.page/mcp
```

Works from any MCP client with no setup beyond the URL. For owned docs, add a free API key from the dashboard as a Bearer header.

## Configuration

```json
{
  "mcpServers": {
    "lucid.page": {
      "url": "https://lucid.page/mcp"
    }
  }
}
```

Optional auth: `Authorization: Bearer lp_…` from the lucid.page dashboard unlocks updates, private docs, bundles and 120 req/min. Anonymous publishes return a claim link to hand to a human.

## Business Relevance

- **Founders** get agent-written recaps and investor updates as shareable pages, not chat walls
- **Consultants and agencies** ship research reports to clients as clean links with revision history
- **Teams running always-on agents** collect outputs into owned, listed docs instead of logs
- **Anyone showing agent work** uses anonymous publish plus the claim-token flow — no credentials shared with the agent

## Integration with CorpusIQ

lucid.page is the delivery layer for CorpusIQ's analytical output: a CorpusIQ session that builds a monthly business recap (Stripe, QuickBooks, GA4) can publish it straight to a client-ready page, then hand over the link — one session from books to boardroom. For recurring reporting, the bundle tool turns per-month pages into a dated multi-chapter archive a client can navigate.

## Limitations

- Brand new (Aug 2026 listing), no track record yet
- Anonymous pages can't be updated later unless claimed or the publish used a key
- Revision history and private docs require an lp_ API key
- Hosted service — pages live on lucid.page's domain
- Pro analytics (views, referrers, countries) is a paid tier

## See Also

- [LiveSend MCP — Client Reports as Trackable Protected Links](/hermes/mcp/servers/external/livesend-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
