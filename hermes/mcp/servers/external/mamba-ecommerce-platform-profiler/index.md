---
title: "Mamba Ecommerce Platform Profiler MCP - Stack Detection"
description: "Detect the ecommerce platform, payment providers, subscriptions and catalogue size behind a storefront, with confidence and evidence per read."
category: E-commerce Intelligence
stars: n/a (npm package, MIT)
added: 2026-10-07
source: "chatmcp/mcpso issue #4868 (Oct 7, 2026 morning sweep)"
relevance: ★★
tags: [ecommerce, shopify, platform-detection, competitive-intelligence, apify, local-mcp, npm]
---

# Mamba Ecommerce Platform Profiler MCP

**Local MCP server (stdio, npm) - storefront stack detection** for any ecommerce domain: which platform it runs on, which payment providers load, whether it sells subscriptions, roughly how many products it lists, and which currencies and shipping destinations it serves.

```
Server type: Local (stdio), TypeScript, Node 18+
Auth: Your own Apify API token (APIFY_TOKEN)
Package: @mambalabsdev/mcp-ecommerce-platform-profiler (npm, MIT, v1.1.1)
Tool: profile_ecommerce_platform (single tool)
Registry: com.mambabuilt/mcp-ecommerce-platform-profiler
Pricing: Apify credits per domain analyzed
Cache: 7-day result cache (skipCache to force a fresh run)
Built by: Mamba Labs (part of the Mamba Labs GTM Suite)
```

## Why This Matters for Operators

Before quoting a replatform, scouting competitors or sizing a market, the first question is what a storefront actually runs: platform, payments, subscriptions, catalogue size. This server answers that from static reads - the homepage, the sitemap and optionally the public cart page - with confidence and evidence recorded per field rather than a bare label.

The honesty details matter: a storefront that reveals its platform only after JavaScript runs is reported as `not_extractable` rather than stamped with the nearest guess, a bot challenge is retried once from a residential exit instead of being recorded as a failure, and product counts carry their source (`products_json` or sitemap) and an exactness flag.

## Tools & Capabilities

| Tool | What the agent can do |
|---|---|
| `profile_ecommerce_platform` | One flat row per company: platform with confidence and evidence, payment providers, subscriptions, catalogue size estimate, currencies and shipping destinations |

Detected platforms include Shopify, WooCommerce, Magento, BigCommerce, Salesforce Commerce, Squarespace, Wix, PrestaShop and commercetools.

Key inputs:
- `company_domain` and `company_name`.
- `includeProductCount` (default true) - catalogue size estimate.
- `includePaymentProviders` (default true) and `checkCheckout` (default false) - reads the public cart page for providers that load there, never adding an item or starting a checkout.
- `escalateOnBlock` (default true), `skipCache`.

## Installation

```bash
npm i @mambalabsdev/mcp-ecommerce-platform-profiler
```

Or run it without installing via `npx` using the configuration below.

## Configuration

```json
{
  "mcpServers": {
    "mamba-ecommerce-platform-profiler": {
      "command": "npx",
      "args": ["-y", "@mambalabsdev/mcp-ecommerce-platform-profiler"],
      "env": { "APIFY_TOKEN": "your-apify-token" }
    }
  }
}
```

Get a token at console.apify.com/account/integrations. The server lists its tools without a token; the token is needed to run a lookup, and each call runs the Mamba Labs actor under your own Apify account. The same tools also ship in the umbrella `@mambalabsdev/mcp-gtm-suite` package.

## Business Relevance

- **Ecommerce operators:** check a competitor's stack, subscription setup and catalogue depth in one call.
- **Agencies:** pre-sales stack reads before quoting replatforming or migration work.
- **Investors and analysts:** profile a cohort of storefronts without opening a browser.
- **Partnership research:** see which payment and platform vendors a target storefront already loads.

## Integration with CorpusIQ

CorpusIQ shows the operator's own store numbers - revenue, orders, customers - from the inside. The Profiler adds the outside view: what the competitive set runs. Together: "how are we doing" from your systems, "what are they running" from the public web.

## Limitations

- Static reads only; a storefront that reveals its stack only under JavaScript returns `not_extractable` rather than a guess.
- Catalogue size is an estimate; check `product_count_exact` and `product_count_source`.
- Providers that load only inside a real checkout need `checkCheckout` on, which reads the public cart page as a plain HTTP request and never acts on it.
- Apify credits are consumed per lookup; results are cached for 7 days.

## FAQ

### What platforms can it detect?

Shopify, WooCommerce, Magento, BigCommerce, Salesforce Commerce, Squarespace, Wix, PrestaShop, commercetools and more; each detection carries confidence and evidence.

### Does it touch the checkout?

No. `checkCheckout` reads the public cart page as a plain read; it never adds an item, starts a checkout or submits anything.

### How accurate is the product count?

It is an estimate from the Shopify products endpoint where available and the sitemap otherwise; `product_count_exact` says whether it is exact.

## See Also

- [Mamba AI Tooling Detector MCP - AI Adoption Signals](/hermes/mcp/servers/external/mamba-ai-tooling-detector/)
- [Undercart MCP - Shopify Store Intelligence for Agents](/hermes/mcp/servers/external/undercart-mcp/)
- [GumroadDNA MCP - Gumroad Store Operations](/hermes/mcp/servers/external/gumroad-dna-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
