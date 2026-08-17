---
title: "Nexscope E-Commerce Skills — Shopify, Etsy, TikTok"
description: "nexscope-ai/ecommerce-skills — 121 skills, 126.1K installs. Cross-border e-commerce (62.2K), Shopify marketing/dropshipping, Etsy SEO, TikTok Shop research, eBay/Walmart/Amazon brand protection, PPC planning, email marketing for agents serving e-commerce operators."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/nexscope-ecommerce-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-14"
tags: ["hermes skill", "agent skill", "skill setup", "ecommerce", "shopify", "etsy", "tiktok shop", "growth"]
---

# Nexscope E-Commerce Skills — Setup Guide

**Source:** [nexscope-ai/ecommerce-skills](https://skills.sh/nexscope-ai/ecommerce-skills)
**GitHub:** [nexscope-ai/ecommerce-skills](https://github.com/nexscope-ai/ecommerce-skills)
**Skills:** 121 skills (126.1K combined installs)
**Category:** Growth Operations / E-Commerce
**First Seen:** August 14, 2026 afternoon sweep
**Quality Tier:** 🟢 Production (flagship `cross-border-ecommerce` at 62.2K installs)

The general-marketplace companion to the [Nexscope Amazon Skills](/hermes/skills/catalog/nexscope-amazon-skills-setup/) guide. Where the Amazon repo focuses on a single marketplace, this repo spans the full operator stack: Shopify, Etsy, TikTok Shop, eBay, Walmart, plus cross-border selling, dropshipping research, PPC planning, and email marketing. It is the largest single e-commerce skill library on skills.sh — 121 skills covering product research through post-purchase retention.

---

## Installation

```bash
npx skills add nexscope-ai/ecommerce-skills
```

No API keys required — the skills are markdown workflow packages. Marketplaces are reached through the agent's existing tools (browser automation, Postiz, MCP connectors).

## What It Provides

### Flagship

| Skill | Installs | Purpose |
|---|---|---|
| `cross-border-ecommerce` | 62.2K | Full cross-border selling playbook: market selection, logistics, localization, compliance |

### Research & Strategy (~700-1,100 each)

`dropshipping-product-research` (1.1K), `ecommerce-competitor-analysis` (820), `ecommerce-keyword-research` (803), `market-gap-analysis` (775), `tiktok-shop-product-research` (743), `tiktok-shop-trending-products` (690), `etsy-keyword-research` (681), `competitor-price-analysis` (744), `competitor-price-tracker` (672), `ecommerce-business-plan` (689), `ecommerce-growth-strategy` (860), `product-launch-strategy` (688), `product-review-analysis` (797).

### Platform Playbooks

- **Shopify:** `shopify-dropshipping` (702), `shopify-marketing` (700)
- **Etsy:** `etsy-seo` (856), `etsy-shop-setup` (718), `etsy-digital-products` (698), `etsy-product-description` (668), `etsy-competitor-analysis` (667)
- **TikTok Shop:** `tiktok-shop-listing-optimization` (671)
- **Amazon:** `brand-protection-amazon` (12) — cross-marketplace complement to the dedicated Amazon repo
- **eBay / Walmart:** `product-differentiation-ebay`, `profit-margin-calculator-walmart`, `brand-protection-ebay`, `brand-protection-walmart` (11-12 each)

### Marketing & Conversion (~700-770 each)

`ecommerce-ppc-strategy-planner` (709), `ecommerce-email-marketing-builder` (699), `ecommerce-marketing-strategy-builder` (765), `ecommerce-social-media-marketing` (760), `ecommerce-content-marketing` (749), `ecommerce-checkout-optimization` (713), `ecommerce-landing-page` (769), `product-title-optimization` (744), `product-page-seo` (742), `product-description-generator` (899), `ecommerce-branding` (702), `google-shopping-optimization` (675), `ecommerce-returns-management` (670), `brand-monitoring` (667).

## Quick Start

1. `npx skills add nexscope-ai/ecommerce-skills`
2. "Run cross-border-ecommerce analysis for a US seller expanding to EU: which markets, what logistics, what compliance"
3. "Find trending TikTok Shop products in the beauty niche this week"
4. "Audit this Shopify store's product pages for SEO and conversion"
5. "Draft a 5-email post-purchase sequence for a Shopify pet brand"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Operator intelligence** | E-commerce operators are a core CorpusIQ audience — these skills mirror the exact questions they ask us |
| **Inbound lead response** | Enrich e-commerce prospect replies with platform-specific recommendations (Shopify vs Etsy vs TikTok Shop) |
| **Content engine** | Generate help-first UGC/blog material on marketplace strategy from the same frameworks operators use |
| **Feature validation** | Cross-reference our connectors (Shopify, Amazon Seller, eBay, TikTok) with the research playbooks |

## Related

- [Nexscope Amazon Skills — E-Commerce Product Research Setup](/hermes/skills/catalog/nexscope-amazon-skills-setup/)
- [Apify Ultimate Scraper Setup](/hermes/skills/catalog/apify-ultimate-scraper-setup/)
- [Firecrawl Skills Setup](/hermes/skills/catalog/firecrawl-skills-setup/)

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
