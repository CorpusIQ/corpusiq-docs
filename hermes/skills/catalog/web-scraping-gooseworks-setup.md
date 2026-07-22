---
title: Web Scraping (Gooseworks) — Multi-engine scraping for Hermes Agent data extraction
description: Scrape websites, extract structured data, and automate browsers via Scrapegraph, Olostep, Riveter, Brand.dev, and Notte. 35+ installs from gooseworks-ai.
---

# Web Scraping (Gooseworks) — Setup Guide

**Source:** [gooseworks-ai/goose-skills](https://skills.sh/gooseworks-ai/goose-skills/web-scraping) (35+ installs)
**Category:** Engineering / Data Extraction
**Quality Tier:** 🔵 Community

Unified web scraping skill providing access to five specialized scraping engines through a single Gooseworks API gateway: Scrapegraph (AI-powered extraction), Olostep (high-volume batch scraping), Riveter (structured schema extraction), Brand.dev (brand assets and logos), and Notte (browser automation with CAPTCHA solving).

---

## Installation

```bash
npx skills add gooseworks-ai/goose-skills --skill web-scraping
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Gooseworks account** | API key from `npx gooseworks login` |
| **Credentials** | Stored at `~/.gooseworks/credentials.json` |
| **API base** | Default: `https://api.gooseworks.ai` |

---

## Key Capabilities

### Scrapegraph — AI-Powered Scraping
Natural language extraction with optional output schemas. Convert pages to markdown, crawl with AI extraction, search + scrape. Supports stealth mode for bot protection, JS rendering for SPAs, and pagination up to 100 pages.

### Olostep — Scalable Batch Processing
High-volume scraping, batch jobs, site crawling, URL discovery, and AI-powered answers from pages. Supports country-specific scraping, page interactions, and CSS selector removal.

### Riveter — Structured Schema Extraction
Define exact output schemas with field-level prompts and formats (number, JSON, URL, text, email, tag, date, boolean). Multi-URL extraction with chained tool calls (web_search, web_scrape, query_pdf, query_image).

### Brand.dev — Brand Asset Extraction
Extract logos, colors, fonts, design systems, and screenshots from any domain. AI-powered data extraction by company name, email, or ticker symbol.

### Notte — Browser Automation
Session-based scraping with CAPTCHA solving, proxy rotation, and autonomous AI agents for multi-step browser tasks.

---

## Quick Start

```bash
# Set up credentials
export GOOSEWORKS_API_KEY=$(python3 -c "import json;print(json.load(open('$HOME/.gooseworks/credentials.json'))['api_key'])")

# AI-powered extraction (Scrapegraph)
curl -s -X POST "$GOOSEWORKS_API_BASE/v1/proxy/orthogonal/run" \
  -H "Authorization: Bearer $GOOSEWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"api":"scrapegraph","path":"/v1/smartscraper","body":{"website_url":"https://example.com","user_prompt":"Extract all product names and prices"}}'

# Brand assets (Brand.dev)
curl -s -X POST "$GOOSEWORKS_API_BASE/v1/proxy/orthogonal/run" \
  -H "Authorization: Bearer $GOOSEWORKS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"api":"brand-dev","path":"/v1/brand/retrieve","query":{"domain":"stripe.com"}}'
```

---

## Verification

```bash
# Check skill installed
npx skills list | grep web-scraping

# Verify credentials exist
ls ~/.gooseworks/credentials.json

# Test API connectivity
curl -s -X POST "https://api.gooseworks.ai/v1/proxy/orthogonal/search" \
  -H "Authorization: Bearer $(python3 -c "import json;print(json.load(open('$HOME/.gooseworks/credentials.json'))['api_key'])")" \
  -H "Content-Type: application/json" \
  -d '{"prompt":"scrapegraph API endpoints"}'
```

---

## Notes

- Five specialized engines under one API gateway — pick the right tool for each task
- Scrapegraph is go-to for natural language extraction; Olostep for batch/volume; Riveter for structured data; Brand.dev for logos/branding; Notte for browser-heavy pages
- Supports CAPTCHA solving and proxy rotation (Notte, Scrapegraph stealth mode)
- All engines support async operations — start jobs, poll for results
- `npx gooseworks login` to set up credentials if `~/.gooseworks/credentials.json` doesn't exist
- Quality tier 🔵 Community: 35 installs, newer but comprehensive
