---
title: "AgentGrown MCP - Search Console and GA4 for Agents"
description: "AgentGrown gives a coding agent its site's Google Search Console and GA4 data over MCP, with Google sign-in and daily sync."
category: Analytics & BI
stars: n/a (new listing)
added: 2026-09-29
source: "mcp.so server page (agentgrown.com)"
relevance: ★★★
tags: [seo, google-search-console, ga4, analytics, marketing, coding-agents, remote-mcp]
---

# AgentGrown MCP

**Your site's own search and analytics data, in the agent that writes the code.** AgentGrown connects a site's Google Search Console and GA4 accounts to a coding agent over MCP, syncs both sources daily, and lets the agent query clicks, impressions, CTR, position, sessions and conversions by query and landing page.

```
Server type: Remote (Streamable HTTP)
Auth: Google sign-in
Endpoint: https://agentgrown.com/mcp
Tools: Search Console queries, GA4 sessions and conversions, by query and landing page
Pricing: pay as you go, $10 free credit to start, failed calls free
Category: Analytics & BI
Built by: AgentGrown (agentgrown.com)
```

## Why This Matters for Operators

SEO and growth work breaks when the data lives in one tab and the person who can act on it lives in another. AgentGrown puts Search Console and GA4 data directly in the coding agent that ships the content, metadata and site changes, so the loop from ranking data to shipped fix no longer passes through a manual export.

For operators running content programs, that means the agent can see which pages lost clicks, propose the fix and apply it without a human copy-pasting a report into a prompt.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Search Console reads | Clicks, impressions, CTR and position by query and landing page |
| GA4 reads | Sessions and conversions for the same pages and queries |
| Daily sync | Both sources refreshed every day for the agent's next session |
| Site scoping | Each agent session is scoped to the sites you connected |

Tool names are served from the endpoint; the table reflects the vendor's published capability set.

## Installation

```bash
claude mcp add agentgrown --transport http https://agentgrown.com/mcp
```

Sign in with Google at agentgrown.com, connect your sites, and the daily sync starts. Setup docs live at agentgrown.com/docs.

## Configuration

```json
{
  "mcpServers": {
    "agentgrown": {
      "type": "http",
      "url": "https://agentgrown.com/mcp"
    }
  }
}
```

## Business Relevance

- **Content operators** let the agent see ranking deltas before proposing rewrites
- **SEO freelancers** give client-scoped agents direct access to each client's GSC and GA4
- **Founders** hand growth data to the same agent that edits the site, cutting report round-trips
- **E-commerce teams** connect conversion queries to landing pages without a BI ticket

## Integration with CorpusIQ

AgentGrown covers search and site analytics; CorpusIQ covers the revenue side of the same pages. Pair GSC and GA4 reads from AgentGrown with Stripe and Shopify revenue from CorpusIQ connectors to see which ranking pages actually convert, then have the agent act on that full picture.

For paid and organic comparison, combine AgentGrown organic data with the ad platform reporting in CorpusIQ connectors to split growth contribution by channel in one assistant session.

## Limitations

- Brand new listing, no track record yet
- No public repository or published tool catalog
- Google-only sources today, no Bing or alternative search data on the listing
- Data reads only; the agent cannot push changes back through GSC or GA4
- Pay-as-you-go pricing means heavy query workloads accrue cost

## FAQ

### What data does the agent actually get?

Daily-synced Google Search Console clicks, impressions, CTR and position plus GA4 sessions and conversions, queryable by query and landing page.

### Does it work with any coding agent?

The listing targets coding agents generally; any MCP client that can reach agentgrown.com/mcp and complete the Google sign-in flow can use it.

### What does it cost?

Pay as you go with no subscription. Every account starts with $10 of free credit with no card required, and failed calls are free.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
