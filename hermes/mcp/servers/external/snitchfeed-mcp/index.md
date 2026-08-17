---
title: SnitchFeed MCP
description: Intent-based keyword monitoring for LinkedIn, X, Reddit, Hacker News and Bluesky — social listening over MCP with OAuth and 33 tools for sales, marketing and product research.
category: Marketing
stars: n/a (new listing)
added: 2026-08-17
source: mcpservers.org
relevance: ★★★
tags: [social-listening, keyword-monitoring, lead-generation, linkedin, reddit, sales-intelligence, marketing-research, remote-mcp]
---

# SnitchFeed MCP

**Remote MCP server (Streamable HTTP, OAuth)** — SnitchFeed brings intent-based keyword monitoring to AI agents: 33 tools over LinkedIn, X, Reddit, Hacker News, and Bluesky, so an agent can watch for buying signals, competitor mentions, and industry keywords without a human refreshing dashboards. The vendor positions it for sales, marketing, product research, and reporting use cases.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser flow on first connect)
Endpoint: https://api.snitchfeed.com/mcp
Tools: 33 (social listening across LinkedIn, X, Reddit, Hacker News, Bluesky)
Pricing: account-based (not published on the setup page)
Category: Marketing
Built by: SnitchFeed (snitchfeed.com)
```

## Why This Matters for Operators

Social listening has historically meant either paying for an enterprise suite or wiring together brittle scrapers. SnitchFeed collapses that into one OAuth-secured MCP endpoint your agent can query directly: "what are people saying about X this week", "who is asking for a tool like ours on Reddit", "any new HN threads about our category".

**The differentiator is intent**: the monitoring is keyword-based but intent-filtered, so an agent surfaces the comment, thread, or post where someone is actively evaluating or complaining — the moments that turn into leads — rather than raw mention counts. Five-platform coverage (LinkedIn, X, Reddit, Hacker News, Bluesky) means the listening covers both professional and technical communities.

## Tools & Capabilities

The vendor publishes 33 tools; the setup page does not enumerate individual tool names (the live tool list is served from the endpoint on connection). Capability areas documented:

| Area | Purpose |
|---|---|
| Keyword monitoring | Intent-based monitoring across LinkedIn, X, Reddit, Hacker News, Bluesky |
| Platform queries | Per-platform feeds and mention lookup |
| Lead & signal surfacing | Sales, marketing, product research, and reporting use cases |
| Account & session | OAuth connection state and monitoring configuration |

## Installation

```bash
claude mcp add SnitchFeed --transport http https://api.snitchfeed.com/mcp
```

Vendor-published walkthroughs cover Claude (Desktop/Web), Claude Code, Cursor, ChatGPT, Windsurf, OpenAI Codex, and Antigravity.

## Configuration

```json
{
  "mcpServers": {
    "SnitchFeed": {
      "type": "http",
      "url": "https://api.snitchfeed.com/mcp"
    }
  }
}
```

First connect opens a browser to the SnitchFeed login; after granting access the client stores a token and reconnects automatically. Access tokens are valid for 1 hour and refresh automatically for up to 30 days before a reconnect is needed.

## Business Relevance

- **Sales teams** get intent signals from the communities where their buyers ask questions — before those buyers raise a hand on a website.
- **Marketing operators** can monitor competitor mentions and category keywords across five platforms from one agent prompt.
- **Product teams** can mine Reddit and HN threads for pain points and feature requests without leaving the research workflow.
- **Founders** get a standing brand-monitoring loop that reports on breakpoints instead of dashboards.

## Integration with CorpusIQ

SnitchFeed pairs with CorpusIQ's publishing and lead layers to close the listen-to-act loop. The social listening feeds intent leads into the lead pipeline (HubSpot CRM connector), while GA4 correlation shows whether mention spikes move sessions. On the publishing side it complements Postiz-managed channels: SnitchFeed listens for the conversations, the social cadence engine publishes into them, and YouTube/TikTok connectors measure the response. It also strengthens the organic discovery workflow — keyword monitoring surfaces the exact threads where a helpful-first answer belongs.

## Limitations

- Brand new — no track record yet; listing appeared August 17, 2026.
- OAuth-only — no API-key alternative published, so automation must hold a browser-authorized token.
- Tool-level documentation is thin; the 33 tools are described by capability area, not enumerated.
- Pricing is not published on the docs page — account plans only.
- Five platforms only; no TikTok, Instagram, or forum coverage beyond the listed set.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
