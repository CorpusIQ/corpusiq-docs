---
title: "Markifact Google Ads MCP - Approval-Gated Google Ads"
description: "Markifact connects Google Ads to Claude, ChatGPT or any AI agent with approval-gated writes and multi-account reporting."
category: Advertising & Marketing
stars: n/a (new listing)
added: 2026-09-29
source: "mcpservers.org listing + markifact.com/google-ads-mcp"
relevance: ★★★
tags: [google-ads, paid-search, marketing, campaign-management, ppc, approval-gated, remote-mcp]
---

# Markifact Google Ads MCP

**Google Ads with a human in the loop on every write.** Markifact connects Google Ads to Claude, ChatGPT or any AI agent for campaign analysis, creation, keyword optimization and budget management, and every change waits for operator approval before it goes live.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth sign-in (also installable from the Claude directory at claude.ai/directory/markifact)
Endpoint: https://api.markifact.com/mcp/google-ads
Tools: reporting, account-structure audit, keyword optimization, bid and budget management
Pricing: vendor pricing (markifact.com)
Category: Advertising & Marketing
Built by: Markifact (markifact.com, github.com/markifact/google-ads-mcp)
```

## Why This Matters for Operators

Paid search is where AI assistance and operator risk collide hardest. An assistant that can see spend but cannot act is a reporting toy; one that can act without a gate is a budget incident. Markifact's approval-gated design splits the difference: the agent drafts, the operator approves, and nothing touches a live account without a human click.

That structure makes it safe to hand campaign hygiene work (negative keywords, bid adjustments, budget shifts) to an agent, which is where most accounts quietly leak money.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Cross-account reporting | Campaign, ad group, ad, keyword, search term, asset and conversion performance across accounts |
| Structure audit | Campaign settings, conversion tracking, keyword coverage, asset groups and account-level issues |
| Keyword optimization | Search-term analysis, wasted spend, negative keyword lists, match-type refinements |
| Bid and budget management | Bid and budget changes that wait for approval before going live |

The GitHub repository lists the full Google Ads operation set; every write operation is approval-gated.

## Installation

```bash
claude mcp add markifact-google-ads --transport http https://api.markifact.com/mcp/google-ads
```

Install Markifact from the Claude directory or ChatGPT marketplace and sign in, or use the hosted endpoint above with the same login.

## Configuration

```json
{
  "mcpServers": {
    "markifact-google-ads": {
      "type": "http",
      "url": "https://api.markifact.com/mcp/google-ads"
    }
  }
}
```

## Business Relevance

- **Performance marketers** hand negative-keyword and search-term hygiene to an agent
- **Agencies** audit client accounts for wasted spend without manual exports
- **Founders** get campaign oversight without learning the Google Ads UI deeply
- **Growth operators** run multi-account reporting from one assistant surface

## Integration with CorpusIQ

Markifact covers Google Ads; CorpusIQ connectors cover the rest of the attribution picture. Combine Markifact spend and conversion reads with CorpusIQ GA4, Stripe and Shopify data to reconcile ad spend against actual revenue, then let the agent propose the account changes that close the gap.

For Meta versus Google budget questions, pair the Markifact Google Ads and Meta Ads MCP servers with CorpusIQ cross-source connectors so one assistant session sees both paid channels next to web and revenue data.

## Limitations

- Writes are approval-gated, which is a feature and also a throughput limit
- Tool list is extensive but the full operation set is documented in the GitHub repository rather than the directory listing
- Google Ads only; Meta and other channels are separate Markifact servers
- Pricing is not disclosed on the directory listing

## FAQ

### Can the agent change campaigns without me?

No. Every write operation waits for your approval before it goes live, so the agent drafts and you decide.

### Which clients can use it?

Claude and ChatGPT install it from their directories, and any MCP client can use the hosted endpoint at api.markifact.com/mcp/google-ads with sign-in.

### Does it manage multiple accounts?

Yes. Reporting and optimization work across multiple Google Ads accounts from the same connection.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
