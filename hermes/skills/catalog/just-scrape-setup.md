---
title: just-scrape — AI-Powered Web Scraping CLI for Hermes Agents
description: Universal web scraping CLI with 244.9K+ installs. Search, scrape, extract structured data, crawl, and monitor web pages. Essential for Hermes agents doing web research, content extraction, and competitive monitoring.
---

# just-scrape — Setup Guide

**Source:** [scrapegraphai/just-scrape](https://skills.sh/scrapegraphai/just-scrape/just-scrape) (244.9K+ installs)
**Category:** Engineering / Web Scraping
**Quality Tier:** 🟢 Production

just-scrape is a CLI tool from ScrapeGraph AI that gives Hermes agents programmatic access to web search, page scraping, structured data extraction, multi-page crawling, and scheduled page-change monitoring. It's the Swiss Army knife for any agent that needs to interact with the open web — competitive research, content extraction, lead discovery, or documentation crawling.

---

## Installation

```bash
npm install -g just-scrape@latest
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | 18+ recommended |
| **SGAI_API_KEY** | ScrapeGraph AI API key — set as env var, in `.env`, or `~/.scrapegraphai/config.json` |
| **Credits** | Each operation consumes ScrapeGraph AI credits — check balance with `just-scrape credits` |

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **just-scrape** | 244.9K | Universal web scraping CLI for AI agents |

---

## Key Capabilities

### Search — Find pages on a topic
```bash
just-scrape search "hermes agent autonomous workflows" --num-results 5 --json
```
Use when you have no specific URL but need to discover sources.

### Scrape — Get page content
```bash
just-scrape scrape "https://example.com" --json
```
Extracts markdown, HTML, screenshots, links, images, summaries, or branding from a single URL. Perfect for competitive analysis and content research.

### Extract — Structured JSON from known URLs
```bash
just-scrape extract "https://example.com/products" \
  --prompt "Extract product names and prices" \
  --schema '{"products": [{"name": "string", "price": "number"}]}' \
  --json
```
AI-powered extraction with custom prompt and optional JSON schema for structured data.

### Crawl — Bulk extract site sections
```bash
just-scrape crawl "https://docs.example.com" --max-pages 50 --json
```
Crawls entire documentation sites, blogs, or product catalogs.

### Monitor — Track page changes over time
```bash
just-scrape monitor "https://example.com/pricing" \
  --interval 1h \
  --webhook "https://hooks.example.com/scrapegraph"
```
Schedule recurring scraping with optional webhook notifications when pages change.

---

## Quick Start for Hermes Agents

```bash
# 1. Validate setup
just-scrape validate

# 2. Check credits
just-scrape credits

# 3. Test search
just-scrape search "CorpusIQ AI business platform" --num-results 3 --json

# 4. Test scrape
just-scrape scrape "https://corpusiq.io" --format markdown --json

# 5. Test extract
just-scrape extract "https://news.ycombinator.com" \
  --prompt "Extract top 10 post titles and URLs" \
  --json
```

---

## Verification

```bash
# Verify CLI is installed
command -v just-scrape && just-scrape --version

# Verify API connectivity
just-scrape validate && echo "✓ API key valid"

# Verify credit balance
just-scrape credits
```

---

## Notes

- **Credit-based pricing**: Each operation consumes ScrapeGraph AI credits. Monitor with `just-scrape credits` before large crawls.
- **Alternatives**: For simple single-page scraping, Hermes' built-in `web_extract` tool may suffice. Use just-scrape when you need structured extraction, multi-page crawling, or scheduled monitoring.
- **API key**: Store `SGAI_API_KEY` in `~/.hermes/profiles/corpusiq/secrets/` alongside other API keys for consistent secret management.
- **Complementary skills**: Works well with `firecrawl`, `tavily-research`, and `web-scraping-gooseworks` for a complete web intelligence stack.
