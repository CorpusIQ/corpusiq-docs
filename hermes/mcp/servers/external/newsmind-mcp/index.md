---
title: "Newsmind MCP - RSS Semantic Search and News Digests for Agents"
description: "Hosted remote MCP server that connects RSS feeds to AI clients with semantic search, story clustering, keyword watches and scheduled email digests. 29 tools cover reading and briefing, full-text and semantic search, subscriptions, OPML import and export, and feed health. OAuth 2.1 in Claude, ChatGPT and Gemini; Bearer PATs for other clients; 14-day trial then from $24 per year."
category: Content & Research
stars: n/a (new listing)
added: 2026-08-21
source: "mcp.so GitHub issue #3670"
relevance: ★★
tags: [rss, news-monitoring, semantic-search, research, opml, digests, hosted-mcp, competitive-intel, feeds]
---

# Newsmind MCP

**RSS for AI assistants, hosted.** Newsmind connects your feeds to Claude, ChatGPT, Gemini and other MCP clients: semantic search over stories, clustering of related coverage, keyword watches with scheduled email digests, and OPML import so an existing reader setup moves over in one file. There is no local process; the client calls a hosted endpoint and Newsmind keeps the feeds synced.

```
Server type: Hosted remote (Streamable HTTP)
Endpoint: https://newsmind.app/mcp
Auth: OAuth 2.1 (automatic in Claude/ChatGPT/Gemini) or Bearer PAT (newsmind.app/auth/tokens)
Tools: 29
Pricing: 14-day free trial, then from $24/year
Registry: app.newsmind/mcp v0.13.0 (official MCP registry)
Built by: Newsmind (newsmind.app)
```

## Why This Matters for Operators

Monitoring is the operator's standing cost: competitors ship, regulators publish, customers complain in public, suppliers change terms. Newsmind collapses the collect-filter-read loop. Instead of a reader, bookmarks and a search tab, the agent can answer "cluster the coverage of our category from the last week, dedupe it, and brief me" or "watch for any story matching our competitor's product line and email me a digest each morning" without leaving the conversation.

The clustering tool is the differentiator. Where a plain RSS reader returns thirty versions of the same story from thirty outlets, Newsmind groups them, so a briefing step reads one cluster instead of thirty items. Watches with scheduled email digests move monitoring from the app into the inbox, where it competes fairly with everything else an operator reviews.

## Tools & Capabilities

The 29 tools group into six intentions, as described in the vendor submission:

| Intention | Capabilities |
|---|---|
| Read & brief | Read stories and brief digests from subscribed feeds |
| Search | Full-text and semantic search across the synced corpus |
| Cluster | Story clustering and dedupe of related coverage |
| Watch | Keyword watches with scheduled email digests |
| Subscribe | Feed subscriptions and OPML import/export |
| Health | Feed health checks and subscription status |

Exact tool names are documented in-app after signup; the hosted endpoint returns an OAuth 401 to anonymous probes, which is the expected gate, not a failure.

## Installation

Connect in Claude, ChatGPT or Gemini through OAuth 2.1: add `https://newsmind.app/mcp` as a custom connector and approve once. For other clients, create a Bearer personal access token at newsmind.app/auth/tokens:

```json
{
  "mcpServers": {
    "newsmind": {
      "url": "https://newsmind.app/mcp",
      "headers": {
        "Authorization": "Bearer nm_YOUR_TOKEN_HERE"
      }
    }
  }
}
```

Works on web, desktop and mobile clients because the state lives on Newsmind's side, not the client's.

## Configuration

Onboarding: sign up, import OPML from an existing reader (Feedly, Inoreader, most readers export it), or subscribe feed by feed. Watches are configured by keyword with a schedule per digest. The free trial covers 14 days of the full toolset; paid plans start at $24/year.

## Business Relevance

- **Competitive intelligence** teams watch product lines, pricing pages and hiring signals as feeds
- **Founders and GTM leads** get clustered briefings instead of thirty duplicate headlines
- **Research workflows** use semantic search over a synced corpus instead of guessing search syntax
- **Analysts** schedule digests to land in email, where review cycles already happen

## Integration with CorpusIQ

Newsmind is the outside-in layer to CorpusIQ's inside-out layer. CorpusIQ connectors deliver the internal numbers (Stripe, GA4, Ads, CRM); Newsmind delivers the external narrative around them: competitor launches, regulatory shifts, market commentary. An agent holding both can answer "what changed in our market this week, and what did it do to our numbers" in one session.

## Limitations

- Paid after 14-day trial (from $24/year); no permanent free tier
- The submitted GitHub repo (rdowty/newsmind) is not publicly reachable; guide relies on the vendor's own submission and registry listing (app.newsmind/mcp v0.13.0)
- OAuth path favors the big three assistants; other clients need a PAT
- Story corpus is limited to what feeds you subscribe; no web-wide search without feeds

## See Also

- [Webz.io News Search MCP - Global News Monitoring for AI Agents](/hermes/mcp/servers/external/webz-news-search/)
- [SnitchFeed MCP - Brand and Competitor Mention Tracking](/hermes/mcp/servers/external/snitchfeed-mcp/)
- [tube-bridge MCP - Self-Hosted YouTube Research and Transcript Corpora](/hermes/mcp/servers/external/tube-bridge-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
