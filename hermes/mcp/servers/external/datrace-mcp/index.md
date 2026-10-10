---
title: "Datrace MCP - Amazon Market Data for Your Agent"
description: "Amazon category, keyword and ASIN data in chat: 44 tools for demand, competition, rank and traffic, free during the beta period."
category: Commerce & E-Commerce
stars: n/a (new listing)
added: 2026-10-09
source: "mcpservers.org /all; carried hold re-checked at the October 9, 2026 evening sweep"
relevance: ★★★
tags: [amazon, e-commerce, market-research, keyword-research, asin, competitive-intelligence, oauth, remote-mcp]
---

# Datrace MCP

**Remote MCP server that opens Datrace's Amazon market data to your assistant** - category, keyword and ASIN intelligence for sellers, brand teams and agencies, answered in the conversation where the work already happens. Free to use throughout the beta period, and the prior sweep's strongest held candidate, re-checked and catalogued now.

```
Server type: Remote (Streamable HTTP at https://mcp.datrace.com/mcp)
Auth: OAuth (authorize Datrace from your client during setup; no API keys to copy)
Tools: 44, in four areas: category insight (16), keyword opportunities (5), rank and traffic (3), ASIN performance (20)
Data: 100M+ ASINs, 1M+ keywords and hundreds of thousands of categories
Pricing: Free during the beta period - 20,000 credits a month per account, capped at 7,000 a week, no payment method required
Category: Commerce & E-Commerce
Built by: Datrace (datrace.com; tool docs at datrace.com/en/docs)
```

## Why This Matters for Operators

Amazon research usually lives in a separate tool with its own exports: keyword workbooks, ASIN trackers and rank charts that somebody screenshots into a deck. Datrace moves that surface into chat - the category questions, the keyword gaps, the ASIN postmortems - so the research step disappears into the conversation that was already happening.

The four tool families follow the order sellers actually think in: **what is happening in this category, which keywords are underserved, where rank and traffic are moving, and how a single ASIN is performing.** That is the same flow as the manual workflow, minus the tab switching and the exports.

## Tools & Capabilities

| Area | What it covers |
|---|---|
| Category insight (16 tools) | Category demand, keyword concentration, product distribution and competitive movement |
| Keyword opportunities (5 tools) | Search volume, ABA rank, competition, bids, click share, conversion share and trends |
| Rank and traffic (3 tools) | Organic rank, sponsored rank, traffic share, price, reviews and BSR across time |
| ASIN performance (20 tools) | Traffic, sales, price, reviews, BSR history, variations and advertising changes |

## Installation

```bash
claude mcp add --transport http datrace https://mcp.datrace.com/mcp
```

Connect from ChatGPT with a custom connector (Settings, then Connectors and Advanced settings, then Create), or pick your client from Datrace's setup guides - it supports Claude, Claude Desktop, Claude Code, ChatGPT, Codex, Cursor, VS Code, Zed, Gemini CLI, Warp and Grok. Sign in and authorize via OAuth the first time.

## Configuration and Safety

- Access is per account through OAuth, so it can be granted and revoked at the account level.
- Calls spend credits; the beta includes 20,000 credits a month with a 7,000 weekly cap, and credit use varies by tool and returned data volume.
- Read-oriented research surface: the tools answer questions about the market rather than change your store.
- No payment method is required during the beta.

## Business Relevance

- **Amazon sellers** check category demand and keyword gaps before committing to a product or a campaign.
- **Brand owners** track where organic and sponsored rank moves over time without a dashboard sitting between them and the answer.
- **Agencies** pull competitor ASIN performance into client conversations the same day instead of at the next weekly export.
- **Product researchers** move from market opportunity to ASIN-level evidence inside one thread.

## Integration with CorpusIQ

Market data and business data answer different halves of the same question. Ask Datrace what the category is doing - demand, keyword gaps, competitor rank - then ask CorpusIQ for your own numbers from the connectors you already have: Shopify and Stripe for revenue and orders, GA4 for traffic, your ad accounts for spend. The category picture and your business picture land in one conversation, with each number traceable to its source.

## Limitations

- In beta: the tool set, credit limits and free pricing can change.
- Credit metering means heavy research sessions draw down the monthly allowance; the weekly cap keeps that predictable.
- Focused on Amazon marketplace data, not a general e-commerce analytics surface.
- Client support varies by assistant; the vendor maintains per-client setup guides because connector flows differ.

## FAQ

### Do I need a paid Datrace plan to use the MCP server?

No. The beta is free with 20,000 credits a month and no payment method; credits reset monthly and weekly use is capped at 7,000.

### What can the agent actually answer?

Category demand and competition, keyword opportunities with search volume and share metrics, rank and traffic movement over time, and ASIN-level performance including price, reviews, BSR history and advertising changes.

### Can the agent change anything in my Amazon account?

No. This is a market-data surface; the tools read Datrace's data rather than modify your store.

## See Also

- [SellerMate MCP - Amazon Ads Operations for AI Agents](/hermes/mcp/servers/external/sellermate-mcp/)
- [AMZ Vault MCP - Amazon Seller Central and Ads for Agents](/hermes/mcp/servers/external/amz-vault-mcp/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
