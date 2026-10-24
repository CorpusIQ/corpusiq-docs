---
title: "Apify Ultimate Scraper"
description: AI-powered web scraper covering Instagram, Facebook, TikTok, YouTube, LinkedIn, X/Twitter, Google Maps, Reddit, Airbnb, Yelp, and more. 13.6K+ installs. Lead generation, brand monitoring, competitor analysis.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/apify-ultimate-scraper-setup/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Apify Ultimate Scraper - Setup Guide

**Source:** [apify/agent-skills](https://skills.sh/apify/agent-skills/apify-ultimate-scraper) (13,600+ installs)
**Category:** Web Extraction / Data
**Quality Tier:** 🟢 Production

Universal AI-driven data extraction from ~100 Apify Actors across 15+ platforms. Purpose-built for lead generation, brand monitoring, competitor analysis, influencer discovery, trend research, content analytics, audience analysis, review analysis, and SEO intelligence.

---

## Installation

```bash
# Install Apify CLI
npm install -g apify-cli

# Authenticate
apify login
# OR: export APIFY_TOKEN=your_token_here
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Apify account** | Sign up at [console.apify.com](https://console.apify.com) |
| **API token** | Generate at console.apify.com/settings/integrations |
| **Node.js 18+** | Required for CLI |

---

## Key Capabilities

### Supported Platforms

Instagram, Facebook, TikTok, YouTube, LinkedIn, X/Twitter, Google Maps, Google Search, Google Trends, Reddit, Airbnb, Yelp, and 15+ more.

### Workflow Guides

| Task | Reference Workflow |
|---|---|
| Leads, contacts, emails, B2B | `lead-generation.md` |
| Competitor ads, pricing | `competitive-intel.md` |
| Influencer, creator discovery | `influencer-vetting.md` |
| Brand mentions, sentiment | `brand-monitoring.md` |
| Reviews, ratings, reputation | `review-analysis.md` |
| SEO, SERP, content, RAG | `content-and-seo.md` |

---

## Quick Start

### Three Rules for Every Command

1. Always pass `--json` for machine-readable output
2. Pass `--user-agent apify-agent-skills/apify-ultimate-scraper` for telemetry
3. Redirect stderr: `2>/dev/null` (stderr has progress messages that break JSON)

```bash
# Instagram profile details
apify actor run apify/instagram-scraper \
  --input '{"resultsType":"details","directUrls":["https://www.instagram.com/target_account/"]}' \
  --json 2>/dev/null

# Google Maps lead generation
apify actor run compass/crawler-google-places \
  --input '{"searchStringsArray":["restaurants near me"],"maxCrawledPlacesPerSearch":50}' \
  --json 2>/dev/null

# LinkedIn company data
apify actor run harvestapi/linkedin-company \
  --input '{"companies":["https://www.linkedin.com/company/target"]}' \
  --json 2>/dev/null

# Reddit community posts
apify actor run apify/reddit-scraper \
  --input '{"scrapeMode":"posts","communityNames":["SaaS","ecommerce"],"maxPostsPerCommunity":100}' \
  --json 2>/dev/null
```

Every Actor name and input key above was verified against the live Apify API on 2026-10-24. Actors are namespaced by their **owner**, which is not always `apify/` (the Google Maps scraper is `compass/crawler-google-places`). Search the [Apify Store](https://apify.com/store) for the canonical owner before running a new Actor, and check its input schema - field names differ per Actor.

---

## Hermes Integration

For CorpusIQ growth operations:

### Lead Generation Pipeline
```bash
# Scrape Shopify app store for merchant leads
apify actor run fatihtahta/shopify-app-store-scraper \
  --input '{"queries":["analytics"],"category":"store-management","limit":100}' \
  --json 2>/dev/null | jq '.[] | {name, url, rating}' > leads-shopify.json
```

### Competitor Intelligence
```bash
# Monitor competitor social presence
apify actor run apify/instagram-scraper \
  --input '{"resultsType":"details","directUrls":["https://www.instagram.com/competitor1/","https://www.instagram.com/competitor2/"]}' \
  --json 2>/dev/null
```

### Content Research
```bash
# Find trending AI content on Reddit
apify actor run apify/reddit-scraper \
  --input '{"scrapeMode":"posts","communityNames":["artificial","MachineLearning","SaaS"],"maxPostsPerCommunity":200,"communitySort":"hot"}' \
  --json 2>/dev/null > trending-content.json
```

---

## Tips

- Always use `--json` - stable across CLI versions
- The `2>/dev/null` redirect is critical for JSON parsing
- Check `references/actor-index.md` in the skill for the full Actor catalog
- Each platform has its own specific Actor - search Apify Store for the best one

---

## Troubleshooting

| Issue | Solution |
|---|---|
| Auth errors | Run `apify login` or set `APIFY_TOKEN` env var |
| Rate limiting | Apify handles proxies/rotations automatically |
| Empty results | Check input parameters - platform-specific schemas matter |
| JSON parse errors | Ensure `2>/dev/null` to strip stderr progress messages |

---

## See Also

- Apify Agent Skills Setup - Core Apify Agent Skills setup
- Firecrawl Agent Setup - Alternative structured extraction
- [Apify Store](https://apify.com/store) - Full Actor catalog
