---
title: Undercart MCP - Shopify Store Intelligence for Agents
description: "Query Shopify store intelligence from any MCP client: search 1M+ stores, pull profiles, tech stacks, ads and marketing emails."
category: E-commerce Intelligence
stars: n/a (new listing)
added: 2026-10-05
source: mcpservers.org /all (Oct 5, 2026 midday sweep)
relevance: ★★★
tags: [shopify, ecommerce, competitive-research, store-intelligence, ads, remote-mcp, oauth]
---

# Undercart MCP

**Remote MCP server (Streamable HTTP, OAuth)** - the official connector from Undercart that brings Shopify store intelligence into any MCP-compatible agent. Add one connector URL, sign in, and ask questions like "find beauty Shopify stores over $10M/yr that use Klaviyo" - no code to write.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (Google sign-in) or an X-API-Key header
Endpoint: https://undercart.co/api/mcp
Tools: 8 read-only (search, profile, technologies, lookalikes, ads, emails, categories)
Billing: metered in store lookups against a monthly plan quota
Data: enriched Shopify stores only; every result links back to the store's Undercart page
```

## Why This Matters for Operators

Competitive research for an e-commerce brand normally means opening forty storefronts by hand: what theme, which apps, what ads, what emails, how big are they really. Undercart has already enriched that layer, and this server makes it a question: filter stores by category, country, annual revenue, traffic rank and trend, catalog size and price, reviews, Shopify plan, theme, hiring signals, email cadence and installed apps - then pull the full profile, the app stack, the lookalikes, the actual ads running right now, and the captured marketing emails with their discount codes.

For a DTC operator, that turns the store explorer into a briefing: find the peer set, see what the peers run, and check what the category is actually sending and spending before planning the next launch.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `search_stores` | Filter enriched stores with the Store Explorer's filters: keywords, category, country, annual revenue, traffic rank and trend, top market, catalog size and price, reviews, Shopify plan, theme, hiring, email cadence, and apps installed, recently added or recently removed. Results are concise profiles ranked by estimated revenue |
| `get_store` | Full enriched profile by domain: revenue and order estimates, plan, category, country, founding year, catalog stats, technology stack, ad presence, traffic rank and year-on-year trend, top markets and social profiles |
| `list_store_technologies` | The detected app and technology stack grouped by category (email, reviews, subscriptions, analytics and more) |
| `find_similar_stores` | Peers in the same category and revenue band - competitive sets and lookalikes |
| `get_store_ads` | Per-platform ad presence (active, ad count, estimated spend) and the actual ads from the public ad library - headline, copy, CTA, landing page, first and last seen dates for Meta, Google and TikTok; MCP Apps clients render an ad gallery with image and video previews |
| `get_store_emails` | Captured marketing emails: subject, snippet, discount codes and send cadence |
| `get_store_email` | The full body of one captured email by id - plain text plus sanitized HTML on request (free) |
| `list_store_categories` | All store categories with store counts - the valid values for the category filter (free) |

## Installation

In your MCP client, add a remote connector named Undercart with this URL:

```
https://undercart.co/api/mcp
```

The client opens an Undercart sign-in over OAuth (Google account, then Allow access). Clients without OAuth can instead send an API key created under Settings, API keys as an `X-API-Key` header on requests to the same URL. Adding it inside a Claude organization rather than a personal account typically needs a Team or Enterprise plan and org-admin access.

## Business Relevance

- **Peer set in one question**: "US apparel stores between $1M and $5M in annual revenue that run Recharge" turns a day of browsing into a sentence.
- **Ad evidence, not guesswork**: the actual Meta, Google and TikTok ads a store runs, with first and last seen dates and estimated spend.
- **Email teardown**: subject lines, discount codes and send cadence from a store's captured campaigns.
- **Stack benchmark**: see which apps and technologies peers run before buying the next tool.
- **Lookalike discovery**: prospeecting starts from stores similar to a known winner, not a cold list.

## Integration with CorpusIQ

CorpusIQ reads a merchant's own revenue, traffic and ad accounts, read-only and cited. Undercart stays outside that boundary - it reads the public market of enriched Shopify stores, so an operator can pair "what is happening in my business" with "what is happening across the peer set" in one conversation, each answer linking back to its source.

## Limitations

- Read-only: no tool writes to any store or account.
- Only enriched stores are returned; dormant or unverified domains are never exposed, and a store with no published revenue estimate shows a preliminary revenue band instead.
- Every store-data tool call counts as one store lookup against the monthly plan quota - searches included - and free-text and category tools are the exceptions that do not count. Unlike the REST API (which charges a store once per month), MCP usage charges per call.
- When the cap is reached, tools return a monthly store limit message with the reset date.
- Hosted by Undercart and governed by its terms; a live POST initialize returns 401 unauthenticated, confirming it is auth-gated.

## FAQ

### What is Undercart?

A Shopify store intelligence platform: it enriches stores with revenue estimates, traffic trends, technology stacks, advertising presence and captured marketing emails, and exposes that through a web explorer, a REST API and this MCP connector.

### Does this server write anything?

No. All eight tools are read-only lookups against the enriched store database.

### How is usage billed?

Each store-data tool call counts as one store lookup against your monthly plan quota - searches included. `list_store_categories` and `get_store_email` are free, and a reached cap returns a clear message with the reset date.

### Which stores are searchable?

Enriched Shopify stores only; dormant or unverified domains are never exposed. Every result reports estimated revenue (annual before monthly) and links back to the store's Undercart page.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [BestAppify MCP - Shopify App Store Intelligence](/hermes/mcp/servers/external/bestappify-mcp)
