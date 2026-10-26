---
title: "Apify Ultimate Scraper"
description: AI-powered web scraper covering Instagram, Facebook, TikTok, YouTube, LinkedIn, X/Twitter, Google Maps, Reddit, Airbnb, Yelp, and more. 13.6K+ installs. Lead generation, brand monitoring, competitor analysis.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/apify-ultimate-scraper-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
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

1. Call Actors with `apify actors call` (or the short form `apify call`), passing input inline with `-i '<json>'`
2. Add `-o` to print the dataset items, and `--json` only when you want the run record instead of the data
3. Read the Actor input schema before writing JSON: `apify actors info <actor> --input`

Actor names are store-scoped. Most of the widely used scrapers are published by third-party accounts, not by `apify`, so always resolve the exact `username/actor-name` first:

```bash
apify actors search "google maps scraper" --json
```

```bash
# Instagram profile details
apify actors call apify/instagram-scraper \
  -i '{"directUrls":["https://www.instagram.com/target_account/"],"resultsType":"details"}' \
  -o 2>/dev/null

# Google Maps lead generation
apify actors call compass/crawler-google-places \
  -i '{"searchStringsArray":["restaurants near me"],"locationQuery":"Austin, Texas","maxCrawledPlacesPerSearch":50}' \
  -o 2>/dev/null

# LinkedIn company data
apify actors call harvestapi/linkedin-company \
  -i '{"companies":["https://www.linkedin.com/company/target"]}' \
  -o 2>/dev/null

# Reddit subreddit scraping
apify actors call apify/reddit-scraper \
  -i '{"scrapeMode":"posts","startUrls":[{"url":"https://www.reddit.com/r/SaaS/"}],"maxPostsPerCommunity":100}' \
  -o 2>/dev/null
```

Every Actor name and input key above was checked against the Apify API on 2026-10-24. Names retire, so a `404 record-not-found` from `GET https://api.apify.com/v2/acts/<user>~<actor>` means the Actor is gone and the example needs a new one.

---

## Hermes Integration

For CorpusIQ growth operations:

### Lead Generation Pipeline
```bash
# Scrape a Shopify App Store category for merchant leads
apify actors call applora/shopify-appstore-scraper \
  -i '{"scrapeType":"category","categoryHandles":["analytics"],"maxPages":5}' \
  -o 2>/dev/null > leads-shopify.jsonl
```

`scrapeType` is required: `app`, `review`, `developer`, `category`, or `keyword`. For a merchant's own product catalog, use `pocesar/shopify-scraper` with `startUrls`.

One JSON object per line in the output, so `jq -s` reads the whole file as an array.

### Competitor Intelligence
```bash
# Monitor competitor social presence
apify actors call apify/instagram-scraper \
  -i '{"directUrls":["https://www.instagram.com/competitor1/","https://www.instagram.com/competitor2/"],"resultsType":"details"}' \
  -o 2>/dev/null
```

### Content Research
```bash
# Find trending AI content on Reddit
apify actors call apify/reddit-scraper \
  -i '{"scrapeMode":"posts","startUrls":[{"url":"https://www.reddit.com/r/artificial/"},{"url":"https://www.reddit.com/r/MachineLearning/"}],"maxPostsPerCommunity":200}' \
  -o 2>/dev/null > trending-content.jsonl
```

---

## Tips

- `apify actors call` runs the Actor remotely and waits; `apify actors start` returns immediately and is better for long jobs
- `-o` prints the dataset, `--json` prints the run record - both are stable across CLI versions
- The `2>/dev/null` redirect is useful because run logs go to stderr and break JSON parsing
- Confirm an Actor slug resolves before you publish it: `curl -s -o /dev/null -w '%{http_code}\n' https://api.apify.com/v2/acts/<owner>~<actor>` (200 means it exists, 404 means the slug is dead)
- Each platform has its own specific Actor - search Apify Store for the best one, and confirm it resolves before publishing it

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
