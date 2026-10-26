---
title: "Nexscope MCP - Twelve Marketplaces, One Agent Connection"
description: "Twelve storefronts and 55 Amazon Ads tools behind one MCP endpoint: Amazon, TikTok Shop, Walmart, Temu, Ozon and Shopify data, metered per call."
category: Commerce & E-Commerce
stars: n/a (vendor API; nexscope-ai/nexscope-ecommerce-api has 17)
added: 2026-10-23
source: "mcp.so /feed page 1 (card posted 2026-10-23T09:27:21Z, submitted by nexscope-ai, marked verified and featured)"
relevance: ★★★
tags: [ecommerce, amazon, tiktok-shop, walmart, temu, ozon, shopify, etsy, marketplace-research, amazon-ads, product-data, keyword-research, remote-mcp, oauth]
last_updated: "2026-10-23"
---

# Nexscope MCP

**Amazon answers one question. TikTok Shop answers a different one. Nexscope puts both in the same response shape, so an agent stops comparing a marketplace to itself.**

```
Server type: Remote (Streamable HTTP) at https://api.nexscope.ai/mcp
Auth: OAuth 2.1 authorization code with PKCE S256, scope mcp:tools; API keys (Bearer nk-...) on the REST face
Live check: POST initialize without a token returned HTTP 401 {"error":"invalid_token","error_description":"Authentication is required."}
Tools: 235 tool pages in the vendor's public data directory, each with an API & MCP tab; 61 TikTok Shop, 91 Amazon, 13 Ozon, 11 Temu, 5 Walmart, 4 1688, 4 Etsy, 4 Google, 2 Shopify, 2 Shopee, 2 Mercado Libre, 1 eBay, plus patent and IP-risk classes
Pricing: Free 1,000 credits for 3 days (no card), Starter $29/mo with 30,000 credits, Growth $55 with 75,000, Pro $129 with 150,000; per-call costs published per tool
Vendor: Nexscope (nexscope.ai)
```

## Why This Matters for Operators

A seller running Amazon and TikTok Shop does not have one data problem, they have a joining problem. Amazon rank, TikTok Shop sales velocity and Walmart price history arrive from three tools with three definitions of a product, three ideas of what a category is, and three prices per API call. The comparison an operator actually wants, which listing is worth putting inventory behind this month, is the one nobody can run without a spreadsheet nobody maintains.

Nexscope's contribution is breadth under one meter. Twelve storefronts answer through the same MCP endpoint, the same credit balance and the same tool-naming convention, and the vendor publishes the credit cost of every individual tool rather than a plan-level promise. That makes an agent able to answer a cost question before it spends anything, which is the difference between a research agent and a metered surprise.

## What It Actually Does

The data directory is the product. Each tool is a page with its own parameters, response reference and per-call credit cost, and each carries an **API & MCP** tab, so the inventory can be read without an account.

The largest block is Amazon at 91 tools: product search, product detail, reviews, bestsellers, category and niche reads, and 17 keyword tools including **Amazon Keyword Intelligence** (weekly Amazon Brand Analytics search-term data) and **Opportunity Report by Keyword**. Inside that block sit 55 Amazon Ads and Sponsored Products tools: advertiser accounts, connected stores, report creation and retrieval, custom requests, and campaign, ad group, keyword, negative keyword, target and budget-rule management for Sponsored Products, Sponsored Brands and Sponsored Display.

TikTok Shop is the second block at 61 tools, and it is the one no other entry in this catalog covers for research: product search and discovery across 16 markets, top-selling product rankings by day, week, month and category, batch product detail with sales, price, rating and commission, new-product rank, seller search and seller detail, product videos and video ranking, video detail in bulk, download URL resolution, and livestream detail.

The rest is where the cross-marketplace claim is earned. Ozon and Wildberries keyword back-search takes up to 20 SKUs and returns volume, rank, exposure, competition and conversion. Shopify product query filters by price and sales. Walmart product detail carries price history and sales trend. Temu, 1688 (four tools), Shopee, Etsy, eBay, Mercado Libre and four Google tools round out the storefronts. Beside them the directory carries patent intelligence (15 tools), IP risk detection (6), TRO risk detection and design-registration research, which is the compliance half of the same sourcing decision.

A separate creative surface generates listing images and product videos from those same credits, with per-model costs published as credits per five seconds (Seedance 2.0 Fast 720p at roughly 550, Seedance 2.5 1080p at roughly 2,500, Wan 3.0 1080p at roughly 900, Kling V3 Omni 1080p at roughly 1,000).

## Installation

```bash
claude mcp add --transport http nexscope https://api.nexscope.ai/mcp
```

For Hermes:

```bash
hermes mcp add nexscope --url https://api.nexscope.ai/mcp
hermes mcp auth nexscope
```

The vendor's own path is a setup prompt copied from the connector section of `nexscope.ai/mcp` and pasted into a compatible client, which walks the account sign-in and authorization.

## Configuration

```json
{
  "mcpServers": {
    "nexscope": {
      "type": "http",
      "url": "https://api.nexscope.ai/mcp"
    }
  }
}
```

Headless agents can skip OAuth on the REST face: every run endpoint takes `Authorization: Bearer nk-...` with a key minted in the Nexscope account, for example `POST https://api.nexscope.ai/amazon/search`. The MCP endpoint itself is the OAuth one.

## What It Costs Per Call

The vendor publishes a base, a recent average and a range for each tool, which is the detail most data vendors leave out of the docs:

| Tool (MCP name) | Documented cost |
|---|---|
| `nexscope_amazon_search` | 21 credits base, recent average 30, range 16 to 32 |
| TikTok Shop product reviews | 38 credits / call |
| TikTok Shop product discovery | 15 credits / call, recent average 21 |
| TikTok batch product detail | 10 credits / call |
| TikTok new product rank | 10 credits / call |
| Walmart product detail | 29 credits base, recent average 41 |
| Shopify product query | 25 credits base, recent average 43, range 10 to 188 |
| Ozon keyword back search | 17 credits base, recent 47 |

At 30,000 credits a month on the Starter plan, the Amazon search tool is roughly a thousand calls and the Shopify query is closer to seven hundred, so the same plan buys very different amounts of work depending on the marketplace. Budget the tool, not the plan.

## Plans

| Plan | Price | Credits / month | MCP limits |
|---|---|---|---|
| Free trial | $0, 3 days, no card | 1,000 once | 1 request/s, 1 concurrent |
| Starter | $29 ($14.50 first month at 50% off), $348/yr | 30,000 | 3/s, 2 concurrent |
| Growth | $55 ($27.50 first month), $660/yr | 75,000 | 5/s, 4 concurrent |
| Pro | $129 ($64.50 first month), $1,548/yr | 150,000 | 10/s, 8 concurrent |

Subscription credits reset each cycle and do not roll over, annual plans are billed up front while credits still reset monthly, and data-only top-up credits cannot be spent on video or image generation. Free-trial video generation happens in the Nexscope app only, with no video API access on the trial.

## Integration with CorpusIQ

The pairing is a sourcing decision, not a report. CorpusIQ already answers what the operator's own store did: orders and inventory from Shopify or Amazon Seller Central, traffic and conversion from GA4, campaign spend from the ad connectors. Nexscope answers what the market is doing next to it: whether the same product is climbing on TikTok Shop, what the Ozon keyword set looks like for the same SKU, and what a Walmart price history says about a margin the operator is about to defend.

The sequence that earns its credits: pull the operator's own category and bestseller set from their own connector, run the equivalent marketplace read in Nexscope, and ask for the delta. Anything that touches a real product feed still belongs to the operator's own system, which is why read-mostly research against a metered credit balance is the right shape for this connection.

## Limitations

- **No tool call was made in this entry.** Every tool needs an OAuth connection to a Nexscope account with credits, and this sweep does not create accounts. The tool inventory, per-call costs and plan structure come from the vendor's public directory and pricing pages, and the liveness claim rests on the live 401.
- **RFC 9728 discovery is broken on the vendor side.** The `www-authenticate` header advertises `resource_metadata="https://api.nexscope.ai/.well-known/oauth-protected-resource/api/skill-api/v2/mcp"`, and that path returns HTTP 200 with a Kong error body (`{"code":99404,"msg":"No static resource .well-known/oauth-protected-resource..."}`) instead of a protected-resource document. Clients that require that document will fail to connect automatically. `https://api.nexscope.ai/.well-known/oauth-authorization-server` does return a full document (authorize, token, JWKS, revoke and introspect endpoints, `authorization_code` and `refresh_token` grants, `S256`, `client_id_metadata_document_supported: true`, scope `mcp:tools`), so manual configuration works.
- **The directory card is wrong about authentication.** mcp.so lists Authentication: None for this server; the endpoint requires a bearer token and returns 401 without one.
- **Credits are the real constraint, not the tool count.** Costs are per call and vary by an order of magnitude between tools, and the vendor states that final charges for ranged tools depend on the request.
- **This is vendor-sourced marketplace data.** Product, review and sales figures are Nexscope's readings of public storefronts, and every marketplace number should be treated as comparable within Nexscope over time rather than as an audited figure.
- **The account surface is the vendor's, not the operator's store.** These are market reads, not the seller's own Seller Central ledger; Amazon P&L and settlement belong to the account connectors already in this catalog.

## FAQ

### Is it free to try?

Free, but not keyless. The trial gives 1,000 credits for three days with no credit card and one MCP request per second, and the trial restricts video generation to the Nexscope app. There is no anonymous read tool, unlike most of the data servers in this catalog.

### How is this different from the Amazon entries already here?

Datrace, Pangolinfo, Webotee and AMZ Vault all read Amazon. AMZ Vault and Nova read the seller's own Seller Central and Amazon Ads with staged writes. Nexscope is the first entry built for cross-marketplace comparison: 61 TikTok Shop tools, plus Walmart, Temu, Ozon, 1688, Shopee, Etsy, eBay, Mercado Libre and Shopify, under one credit balance. If the question is "what did my own account do", the account-side entries are still the right tool.

### Can an agent change ad campaigns with it?

Yes, the Amazon Ads block includes campaign, ad group, keyword, negative keyword, target and budget-rule management. That is a write surface against a live ad account, so it should be connected read-only or kept behind an approval step; nothing in the vendor documentation describes staged changes or approval gates the way AMZ Vault and Nova do.

### Does it work for non-Amazon sellers?

That is the point of the entry. A TikTok Shop or Shopify-only seller gets the TikTok Shop, Shopify, Walmart, Temu and Ozon blocks without paying for an Amazon-shaped product, and the Amazon tools simply go unused.

## See Also

- [AMZ Vault MCP](/hermes/mcp/servers/external/amz-vault-mcp)
- [Nova Amazon MCP](/hermes/mcp/servers/external/nova-amazon-mcp)
- [Datrace MCP](/hermes/mcp/servers/external/datrace-mcp)
- [Pangolinfo Amazon Data MCP](/hermes/mcp/servers/external/pangolinfo-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
