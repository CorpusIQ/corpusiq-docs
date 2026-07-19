---
title: Apify Growth Skills — Lead Gen, Brand Monitoring, Ultimate Scraper
description: Production-grade growth automation skills from Apify. Lead generation (2.8K), brand reputation monitoring (2.5K), and ultimate scraper (13.4K). 30,000+ pre-built Actors.
---

# Apify Growth Skills — Setup Guide

**Source:** [apify/agent-skills](https://github.com/apify/agent-skills) (2,232⭐)
**Skills:** `apify-ultimate-scraper` (13.4K), `apify-lead-generation` (2.8K), `apify-brand-reputation-monitoring` (2.5K)
**Category:** Growth / Web Scraping
**Language:** Python / JavaScript

Three production-grade growth automation skills built on Apify's platform of 30,000+ pre-built Actors. The **ultimate scraper** handles any website (JS-rendered, infinite scroll, auth-walled), **lead generation** discovers and enriches prospects from business directories, and **brand monitoring** tracks your reputation across the web and social platforms.

These skills extend the base [apify/agent-skills](/hermes/skills/catalog/apify-agent-skills-setup/) package (documented July 16) with specialized growth workflows.

---

## Installation

```bash
# Install all three growth skills
npx skills add apify/agent-skills@apify-ultimate-scraper
npx skills add apify/agent-skills@apify-lead-generation
npx skills add apify/agent-skills@apify-brand-reputation-monitoring

# Or install the full apify skills package (includes all 5+ skills)
npx skills add apify/agent-skills
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Apify account** | [console.apify.com](https://console.apify.com) — free tier ($5/mo credit) |
| **Apify API token** | Apify Console → Settings → Integrations → API token |
| **Apify MCP server** | `npx @apify/mcp` for MCP-native tool access (recommended) |

```bash
export APIFY_TOKEN="apify_api_..."
```

---

## Skill 1: apify-ultimate-scraper (13,400 installs)

### Overview
The flagship Apify scraping skill. Handles any website regardless of complexity — SPAs with JavaScript rendering, infinite scroll pages, paginated lists, login-walled content, and CAPTCHA-protected sites. Built-in proxy rotation (residential + datacenter + mobile), automatic retry with exponential backoff, and structured output with full CSS/XPath selector support.

### Capabilities
- **Any website:** Handles React, Vue, Angular SPAs with full JS rendering
- **Anti-detection:** Rotating residential proxies + fingerprint randomization
- **CAPTCHA solving:** Integrated 2Captcha/Anti-Captcha support
- **Structured output:** JSON, CSV, or direct database insertion
- **Rate limiting:** Automatic delay insertion to avoid triggering WAFs
- **Session persistence:** Maintains login state across scraping sessions

### Usage Pattern
```bash
# Scrape a competitor's pricing page
npx skills run apify-ultimate-scraper \
  --url "https://competitor.com/pricing" \
  --selectors ".pricing-tier" \
  --output "pricing-data.json"

# Scrape with JS rendering (for SPAs)
npx skills run apify-ultimate-scraper \
  --url "https://react-app.example.com" \
  --js-rendering \
  --wait-for ".content-loaded"
```

### CorpusIQ Use Case
Scrape competitor landing pages, pricing changes, and feature announcements. Feed into competitive intelligence pipeline for product roadmap decisions.

---

## Skill 2: apify-lead-generation (2,800 installs)

### Overview
Automated B2B lead discovery and enrichment. Scrapes business directories (Google Maps, Yelp, LinkedIn Sales Navigator, Crunchbase), extracts company and contact information, enriches with firmographic data (company size, funding, industry, tech stack), and outputs CRM-ready formats.

### Capabilities
- **Directory scraping:** Google Maps, Yelp, LinkedIn, Crunchbase, AngelList
- **Contact enrichment:** Email discovery, LinkedIn profile matching, phone extraction
- **Firmographic data:** Company size, revenue range, funding rounds, industry classification
- **Domain filtering:** Target specific industries, locations, company sizes
- **Deduplication:** Automatic cross-source dedup with confidence scoring
- **CRM output:** CSV, HubSpot, Salesforce, or direct API push

### Usage Pattern
```bash
# Find e-commerce brands in SF Bay Area
npx skills run apify-lead-generation \
  --directory "google-maps" \
  --query "e-commerce platform" \
  --location "San Francisco, CA" \
  --enrich \
  --output "sf-ecommerce-leads.csv"

# Scrape LinkedIn for decision makers
npx skills run apify-lead-generation \
  --directory "linkedin" \
  --title "Head of Growth" \
  --industry "SaaS" \
  --company-size "10-200" \
  --output "growth-leads.json"
```

### CorpusIQ Use Case
Power the outbound growth pipeline. Discover e-commerce operators, SaaS founders, and agency owners who need AI-powered business intelligence. Feed qualified leads into the CRM for nurture sequences. The skill handles the "discovery" half — CorpusIQ's `corpusiq-cold-outreach` skill handles the "engagement" half.

---

## Skill 3: apify-brand-reputation-monitoring (2,500 installs)

### Overview
Continuous brand monitoring across web, social media, and review platforms. Tracks every mention of your brand, products, and competitors. Sentiment analysis, trend detection, and configurable alerting. Designed for the "help-first community engagement" growth strategy — catch every mention before it goes unanswered.

### Capabilities
- **Platform coverage:** Reddit, X/Twitter, Hacker News, Product Hunt, G2, Capterra, Trustpilot, Google Reviews
- **Sentiment analysis:** Real-time positive/negative/neutral classification
- **Competitor tracking:** Side-by-side mention volume and sentiment comparison
- **Alert thresholds:** Configurable — spike in negative mentions, competitor launch, review velocity change
- **Delivery channels:** Slack webhook, email digest, webhook, or direct API
- **Historical trending:** 30/60/90-day sentiment and volume trends

### Usage Pattern
```bash
# Set up continuous monitoring for CorpusIQ
npx skills run apify-brand-reputation-monitoring \
  --brand "CorpusIQ" \
  --platforms "reddit,twitter,hackernews,producthunt" \
  --competitors "competitor1,competitor2" \
  --alert-slack "https://hooks.slack.com/..." \
  --schedule "every-6-hours"

# One-time reputation audit
npx skills run apify-brand-reputation-monitoring \
  --brand "CorpusIQ" \
  --audit \
  --timeframe "last-90-days" \
  --output "brand-audit-2026-q3.json"
```

### CorpusIQ Use Case
Core growth infrastructure. Monitor every mention of "CorpusIQ," "Hermes Agent," and competitor names across the platforms where our audience lives. When someone asks "what's the best AI business intelligence tool?" on Reddit or HN — be there with a helpful answer within hours, not days. The `cross-platform-commenting-engine` skill handles the response; this skill handles the detection.

---

## Combined Growth Workflow

The three skills form a complete growth pipeline when used together:

```
┌─────────────────────────┐
│ apify-ultimate-scraper  │  → Scrape competitor sites, industry data
└───────────┬─────────────┘
            ↓
┌─────────────────────────┐
│ apify-lead-generation   │  → Discover and enrich target prospects
└───────────┬─────────────┘
            ↓
┌─────────────────────────┐
│ CRM / Outreach Engine   │  → Qualify, segment, begin nurture sequences
└───────────┬─────────────┘
            ↓
┌─────────────────────────────────┐
│ apify-brand-reputation-monitoring│  → Track brand mentions, engage helpfully
└─────────────────────────────────┘
```

---

## Troubleshooting

| Issue | Fix |
|---|---|
| **APIFY_TOKEN not recognized** | Export as env var: `export APIFY_TOKEN="apify_api_..."` |
| **Scraper blocked by target site** | Enable proxy rotation: `--proxy residential` (included in Apify platform) |
| **Lead gen returns empty** | Broaden search terms or try different directory (Google Maps → Yelp) |
| **Rate limited (429)** | Apify handles rate limiting automatically via the platform |
| **MCP connection refused** | Start MCP server: `npx @apify/mcp` then configure in Hermes |

---

## Verification

```bash
# Verify all three skills installed
npx skills list | grep apify

# Test ultimate scraper with a simple page
npx skills run apify-ultimate-scraper --url "https://httpbin.org/html"

# Test lead gen with a known business
npx skills run apify-lead-generation \
  --directory "google-maps" \
  --query "coffee shop" \
  --location "Palo Alto, CA" \
  --limit 5

# Test brand monitoring (your own brand — never scrape without permission)
npx skills run apify-brand-reputation-monitoring \
  --brand "CorpusIQ" \
  --audit \
  --limit 10
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Apify Agent Skills Base Guide](/hermes/skills/catalog/apify-agent-skills-setup/) | [Discovery Page](/hermes/skills/marketplace/new-july17-2026-update/) →*
*Powered by CorpusIQ*
