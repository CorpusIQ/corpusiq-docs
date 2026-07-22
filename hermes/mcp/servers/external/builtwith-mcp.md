---
title: BuiltWith MCP Server Integration Guide
description: Technology profiling for AI agents — discover what websites are built with. Find tech stacks, ecommerce platforms, analytics tools, and hosting providers for competitive research.
category: mcp
tags: [mcp, builtwith, technology-profiling, competitive-research, lead-gen, tech-stack, hermes-agent]
last_updated: 2026-07-21
---

# BuiltWith MCP — Technology Profiling for Hermes Agent

BuiltWith MCP connects your AI agent to the BuiltWith technology profiling database — find out what any website is built with. Identify tech stacks, ecommerce platforms, analytics tools, hosting providers, and hundreds of other technologies at scale.

## What It Does

BuiltWith MCP gives your agent the ability to profile any website's technology stack:

- **Technology lookup** — Discover every technology a site uses (200+ categories)
- **Ecommerce detection** — Identify Shopify, WooCommerce, Magento, BigCommerce, and custom carts
- **Analytics & marketing** — See what analytics, ad pixels, email tools, and CRMs are installed
- **Hosting & infrastructure** — Detect CDNs, DNS providers, SSL certificates, and hosting platforms
- **Competitive intelligence** — Profile competitor tech stacks at scale to identify trends

## Quick Setup

### Prerequisites
- **BuiltWith account:** Sign up at [builtwith.com](https://builtwith.com)
- **BuiltWith API key:** Available on paid plans

### Add to Hermes Agent

```bash
# Clone and install
git clone https://github.com/builtwith/builtwith-mcp
cd builtwith-mcp
npm install
```

```json
{
  "mcpServers": {
    "builtwith": {
      "command": "node",
      "args": ["path/to/builtwith-mcp/index.js"],
      "env": {
        "BUILTWITH_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

## Key Capabilities

| Tool | Description |
|------|-------------|
| `lookup_domain` | Get full technology profile for a domain |
| `lookup_technologies` | List all technologies detected on a site by category |
| `get_ecommerce_platform` | Identify the ecommerce platform and version |
| `get_analytics_tools` | List analytics, tracking, and marketing pixels |
| `get_hosting_info` | Detect hosting provider, CDN, DNS, and SSL issuer |
| `get_cms` | Identify content management system |
| `get_similar_sites` | Find sites using similar technology stacks |
| `search_by_technology` | Find sites that use a specific technology |

## Use Cases for Business Operators

### 1. Lead Qualification
Score prospects by their tech stack before outreach:

```
Agent prompt: "I have a list of 200 DTC brands. For each, check BuiltWith:
What ecommerce platform? Are they on Shopify Plus? What email tool?
What analytics? Score them 1-5 based on tech stack sophistication.
Priority targets: Shopify Plus + Klaviyo + triple-digit employee count."
```

### 2. Competitive Tech Stack Analysis
Map your competitors' technology choices:

```
Agent prompt: "Profile the top 10 competitors in our space. Build a matrix:
ecommerce platform, CMS, analytics, email, CRM, CDN, A/B testing tool.
What patterns do you see? Who's most technologically advanced?
Who's still on outdated platforms?"
```

### 3. Platform Migration Targets
Find companies on legacy platforms ready for an upgrade:

```
Agent prompt: "Find 50 US-based ecommerce sites still running Magento 1
or WooCommerce without a modern CDN. These are prime migration targets —
they have revenue (Magento) but their tech stack is holding them back."
```

### 4. Partnership & Integration Discovery
Identify integration opportunities:

```
Agent prompt: "Search BuiltWith for all sites using Klaviyo that DON'T
have a reviews widget. Cross-reference with Shopify stores doing
$10M+ revenue (via employee count proxy). These are integration
targets for our reviews plugin."
```

## Integration with CorpusIQ

BuiltWith MCP + CorpusIQ = complete market intelligence:

1. **CorpusIQ CRM connector** → enrich leads with tech stack data automatically
2. **CorpusIQ email connector** → find decision-maker emails for tech-profiled targets
3. **AI agent** → build targeted outreach lists: "Find all Shopify Plus stores using Klaviyo and Recharge, with 50+ employees, in the beauty vertical"
4. **CorpusIQ database connector** → store tech profiles for trend analysis over time

This turns competitive research from "manually check each competitor" to "profile 500 sites and give me the 20 best targets."

## Pricing

- **BuiltWith MCP:** Open source, free
- **BuiltWith API:** Plans start at $295/month (Basic), $495/month (Pro), $995/month (Team)
- **Free tier:** Limited lookups — sufficient for testing, not for production use

## Limitations

- BuiltWith API is paid — budget for production use ($295+/month)
- Technology detection is not 100% accurate — some sites obfuscate their stack
- API rate limits vary by plan — check your tier
- Does not provide traffic or revenue data — tech profiling only

---

*← [External MCP Catalog](/hermes/mcp/servers/external/) | [MCP Overview](/hermes/mcp/)*
