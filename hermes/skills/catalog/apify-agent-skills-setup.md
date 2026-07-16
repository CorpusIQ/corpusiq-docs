---
title: Apify Agent Skills — Full Setup Guide for Hermes Agents
description: Install and use Apify's production-grade web scraping skills. 5 skills, 30K+ pre-built Actors, MCP-compatible. 2.2K+ GitHub stars.
---

# Apify Agent Skills — Setup Guide

**Source:** [apify/agent-skills](https://github.com/apify/agent-skills) (2,232⭐)
**Category:** Web Scraping / Automation
**Language:** Python

Production-grade web scraping and automation skills for AI coding agents. Drop these into any agent and get expert access to the Apify platform — scrape any site, build new Actors, Actorize existing code, generate output schemas, and integrate the Apify API. 30,000+ pre-built Actors covering social media, search, maps, real estate, reviews, and more.

---

## Installation

```bash
# Install all Apify agent skills
npx skills add apify/agent-skills
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Apify account** | [console.apify.com](https://console.apify.com) — free tier available ($5/month credit) |
| **Apify API token** | From Apify Console → Settings → Integrations → API token |
| **MCP server (optional)** | `npx @apify/mcp` for MCP-native tool access |
| **Hermes Agent** | Any version — skills load as instructions; MCP integration available |

Set environment variables:

```bash
export APIFY_TOKEN="apify_api_..."
# Optional: MCP config in ~/.hermes/config.yaml
```

---

## Key Capabilities

### Available Skills

| Skill | What It Does |
|---|---|
| **Scrape any site** | Built-in Actor selection across 130+ curated Actors (Instagram, Facebook, TikTok, YouTube, X, LinkedIn, Google Maps, Reddit, Yelp, Airbnb) plus automatic fallback to 30,000+ Store Actors |
| **Build new Actors** | Generate, debug, and deploy serverless Actors in JS, TS, or Python with official SDK patterns |
| **Actorize existing code** | Wrap any script, library, or CLI tool as a runnable Actor with input/output handling |
| **Generate output schemas** | Auto-derive dataset_schema.json, output_schema.json, key_value_store_schema.json from Actor source |
| **Integrate Apify API** | Call Actors programmatically from JS/TS or Python via apify-client or REST API |

### Supported Platforms (Curated Actors)

Social: Instagram, Facebook, TikTok, YouTube, X/Twitter, LinkedIn, Reddit
Maps: Google Maps, Apple Maps
Commerce: Amazon, eBay, Etsy, Alibaba
Reviews: Yelp, TripAdvisor, Google Reviews
Real Estate: Zillow, Airbnb, Realtor.com
Search: Google Search, Bing, DuckDuckGo

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Competitive intel** | Scrape competitor pricing, features, and reviews across platforms |
| **Lead generation** | Extract business listings from Google Maps, Yelp, LinkedIn |
| **Social monitoring** | Track brand mentions, follower growth, and content performance across platforms |
| **Market research** | Gather industry data, pricing trends, and customer sentiment at scale |
| **Content discovery** | Find trending content, hashtags, and creators in target niches |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| **APIFY_TOKEN not recognized** | Export as env var or add to `~/.hermes/config.yaml` under `env:` |
| **Actor timeout** | Increase timeout: `maxResults` and `maxConcurrency` in Actor input |
| **Rate limited by target site** | Use Apify's built-in proxy rotation (residential + datacenter proxies) |
| **MCP connection refused** | Start MCP server: `npx @apify/mcp` then configure in Hermes MCP settings |

## Verification

```bash
# Verify token works
curl -s "https://api.apify.com/v2/users/me?token=$APIFY_TOKEN" | python3 -m json.tool | head -5

# Verify skill installed
npx skills list | grep apify

# Quick test — list available Actors
curl -s "https://api.apify.com/v2/acts?token=$APIFY_TOKEN&limit=5" | python3 -c "import json,sys; d=json.load(sys.stdin); print([a['name'] for a in d.get('data',{}).get('items',[])])"
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Discovery Page](/hermes/skills/marketplace/new-july16-2026/) →*
*Powered by CorpusIQ*
