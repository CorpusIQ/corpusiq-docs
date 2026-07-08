---
title: "Webotee Amazon MCP — Amazon Seller Intelligence for AI Agents"
description: "Connect Webotee Amazon MCP to Hermes Agent. Research Amazon products, analyze buy-box history, identify competing sellers, and discover under-competed niches. Built for Amazon sellers and ecommerce operators."
category: mcp
tags: [mcp-server, webotee, amazon, ecommerce, seller-intelligence, product-research, niche-analysis]
last_updated: 2026-07-08
---

# Webotee Amazon MCP Server ★ New (July 3)

## Overview

Webotee Amazon MCP (`webotee-amazon-mcp`) brings Amazon marketplace intelligence directly into AI agents. Research products, analyze buy-box dynamics, identify competing sellers, and discover under-competed niches — all from your AI assistant. Purpose-built for Amazon sellers, brand managers, and ecommerce operators.

**Key advantage**: Amazon seller research typically requires expensive tools (Jungle Scout, Helium 10) and manual data analysis. Webotee MCP makes this data queryable via natural language — "show me under-competed niches in home & kitchen with over $10K monthly revenue and fewer than 5 competitors."

## Key Features

- **Product research**: Search and analyze Amazon products by category, revenue, reviews, and rating
- **Buy-box history**: Track buy-box ownership changes across sellers over time
- **Competitor analysis**: Identify competing sellers, their pricing strategies, and market share
- **Niche discovery**: Find under-competed product niches with high demand and low competition
- **Brand intelligence**: Track brand presence, product portfolio, and category expansion
- **Pricing analysis**: Historical pricing trends and competitive price positioning
- **Hosted endpoint**: Remote MCP server at webotee.com

## Installation

```bash
# Add to Hermes (remote endpoint)
hermes mcp add webotee-amazon --url https://www.webotee.com/amazon-product-research-mcp

# Set API key
export WEBOTEE_API_KEY="your-api-key"
hermes mcp config webotee-amazon --env WEBOTEE_API_KEY
```

## Manual Configuration

```json
{
  "mcpServers": {
    "webotee-amazon": {
      "type": "sse",
      "url": "https://www.webotee.com/amazon-product-research-mcp",
      "headers": {
        "x-api-key": "${WEBOTEE_API_KEY}"
      }
    }
  }
}
```

## Prerequisites

1. **Webotee Account**: Sign up at [webotee.com](https://www.webotee.com)
2. **API Key**: Generate from Webotee dashboard
3. **Amazon Marketplace Knowledge**: Basic understanding of Amazon seller metrics (BSR, buy-box, etc.)

## Business Use Cases

1. **Product Opportunity Discovery**: "Find product niches in pet supplies with under 50 reviews on the top 3 listings and over $15K/month estimated revenue"
2. **Competitive Monitoring**: Track competitor buy-box ownership, pricing changes, and new product launches
3. **Brand Audit**: "Analyze my brand's Amazon presence — which ASINs are losing buy-box share and to whom?"
4. **Category Expansion**: "What categories adjacent to my current products show low competition and high demand?"
5. **Pricing Strategy**: Monitor competitor pricing patterns and adjust your pricing strategy based on real-time market data

## Business Relevance

Amazon's marketplace generates $500B+ in annual GMV but seller intelligence tools remain expensive and fragmented. Webotee MCP brings Amazon research into the AI-native workflow — operators running Amazon businesses can research products, monitor competitors, and discover opportunities without switching between Jungle Scout, Helium 10, Keepa, and Seller Central. For agencies managing multiple Amazon brands, this is a force multiplier.

## Limitations

- Amazon data is aggregated/estimated (not real-time API from Amazon directly)
- Coverage varies by marketplace (US marketplace is primary; international coverage growing)
- Niche analysis depends on data freshness — results may lag live marketplace by hours
- Requires Webotee subscription for API access
- Category taxonomy follows Amazon's structure — some niche categorization quirks

## See Also

- CorpusIQ MCP — for Shopify, QuickBooks, and cross-platform business data
- SEOforGPT MCP — for AI visibility and generative engine optimization
- SentiSense MCP — for market sentiment and trend intelligence
