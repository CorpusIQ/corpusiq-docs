---
title: ListingGood MCP
description: Amazon AI Recommendation Engine — AI-readiness and compliance checks, A9-tuned listing writing for US, UK, EU and JP, and POA suspension rescue over MCP.
category: E-Commerce
stars: n/a (new listing)
added: 2026-08-17
source: mcp.so
relevance: ★★
tags: [amazon, ecommerce, listing-optimization, ai-readiness, amazon-seller, marketplace, compliance, remote-mcp]
---

# ListingGood MCP

**Remote MCP server (Streamable HTTP, API key)** — ListingGood makes Amazon's own AI recommend your products: a hosted MCP server plus Claude/Cursor skills that score any listing for AI-readiness and compliance, rewrite copy tuned for A9 and AI shopping agents, and generate POA appeals for suspensions and takedowns. Built by DedeGroup, `github.com/DedeGroup/listinggood-skills`.

```
Server type: Remote (Streamable HTTP)
Auth: API key (Authorization: Bearer <key>)
Endpoint: https://listinggood.com/mcp
Tools: capability surface published via Overview (readiness score, compliance check, AI listing writing, POA rescue); live tool list served from the endpoint
Pricing: free tier — unlimited compliance & AI-readiness checks; paid from $10/mo for AI writing and POA generation
Category: E-Commerce
Built by: DedeGroup (listinggood.com)
```

## Why This Matters for Operators

Amazon is no longer searched only by customers — its AI shopping assistant and external agents like ChatGPT and Gemini now decide what gets recommended. A listing that converts a human shopper can still be invisible to the machines doing the recommending.

**ListingGood converts the new ranking game into a checkable metric**: one AI Recommendation Readiness Score for how likely Amazon's AI is to surface the product, plus a free compliance and AI-readability check that flags policy risks and copy the AI catalog cannot parse. Sellers and agencies stop guessing why a listing underperforms and get the top issues in order.

## Tools & Capabilities

The listing's About/Overview publishes these capabilities (no per-tool extraction yet — live tool list served from the endpoint):

| Capability | Purpose |
|---|---|
| AI Recommendation Readiness Score | One number for how likely Amazon's AI is to recommend the product |
| Compliance & AI-readability check | Policy-risk and AI-unreadable copy detection; free, zero token cost |
| AI listing writing | Titles, bullets, A+ descriptions tuned for A9 + AI catalogs, US/UK/EU/JP |
| Appeal & POA rescue | Suspension and takedown recovery frameworks |

## Installation

```bash
# Get a free API key first: https://listinggood.com/developers
claude mcp add listinggood --transport http https://listinggood.com/mcp --header "Authorization: Bearer <key>"
```

Works inside Claude Desktop, Cursor, and Windsurf; a free no-login scan is available at listinggood.com/scan.

## Configuration

```json
{
  "mcpServers": {
    "listinggood": {
      "type": "http",
      "url": "https://listinggood.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_KEY"
      }
    }
  }
}
```

## Business Relevance

- **Amazon sellers** get a readiness score and ranked fixes before spending on listing experiments.
- **E-commerce agencies** can audit every client listing for AI catalog compliance from one agent prompt.
- **Founders** validate listing quality pre-launch without an Amazon seller account (the free check works on title and bullets alone).
- **Marketplace operators** get a compliance check that is genuinely free — zero token cost, no signup for the scan.

## Integration with CorpusIQ

ListingGood pairs with CorpusIQ's Amazon Seller connector into a full listing lifecycle: the agent audits AI-readiness with ListingGood, then verifies the business result against Amazon Seller orders, inventory, and catalog data. Multi-marketplace operators can run the same readiness check alongside Shopify data, catching listings that convert in one channel and are invisible in the other. The compliance check also feeds the pre-flight discipline — AI-readability and policy risk become a gate before any listing change ships.

## Limitations

- Brand new — no track record yet; listing appeared August 17, 2026.
- No published tool list yet — capabilities are documented in prose; treat the live tool list as the source of truth after connecting.
- Paid writing plans start at $10/mo for the parts most operators will want (AI writing, POA generation).
- Amazon-only — no other marketplace coverage.
- Readiness scoring is the vendor's model of Amazon's AI — results should be validated against actual ranking changes over time.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
