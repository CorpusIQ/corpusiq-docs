---
title: "Firecrawl Skills — Official Web Scraping, Research &"
description: "Firecrawl's official skills ecosystem — firecrawl/cli (14 skills, 716K installs), firecrawl/skills (41 skills, 252K), firecrawl-workflows (16 skills, 493K), firecrawl/anydoc. Scrape, search, crawl, deep research, SEO audit, market research, and lead-gen workflows for any agent including Hermes."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/firecrawl-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-14"
tags: ["hermes skill", "agent skill", "skill setup", "web scraping", "firecrawl", "research", "seo"]
---

# Firecrawl Skills — Setup Guide

**Source:** [firecrawl](https://skills.sh/firecrawl/cli) — official publisher (4 skill repos)
**GitHub:** [firecrawl/cli](https://github.com/firecrawl/cli) · [firecrawl/skills](https://github.com/firecrawl/skills) · [firecrawl/firecrawl-workflows](https://github.com/firecrawl/firecrawl-workflows) · [firecrawl/anydoc](https://github.com/firecrawl/anydoc)
**Skills:** 72 skills across 4 repos (~1.47M combined installs)
**Category:** Web Scraping / Research / Growth Operations
**First Seen:** August 14, 2026 afternoon sweep
**Quality Tier:** 🟢 Production (official vendor skills, 5 skills above 57K installs)

Firecrawl — the web-scraping engine that already powers Hermes's `web_search` and `web_extract` backends — ships its own official skill ecosystem on skills.sh. Four repos turn raw Firecrawl API access into repeatable agent workflows: `firecrawl/cli` for programmatic scrape/search/crawl operations, `firecrawl/skills` for building scraping integrations, `firecrawl-workflows` for end-to-end research pipelines (deep research, market research, SEO audit, lead gen, competitive intel), and `firecrawl/anydoc` for converting documents to markdown.

---

## Installation

```bash
# Core CLI operations (scrape, search, crawl, map, parse, monitor, browser, interact)
npx skills add firecrawl/cli

# Build skills (scraping integration development + onboarding)
npx skills add firecrawl/skills

# Research workflows (deep research, market research, SEO audit, lead gen, competitive intel)
npx skills add firecrawl/firecrawl-workflows

# Any-to-markdown document conversion
npx skills add firecrawl/anydoc
```

Set the API key in the environment:

```bash
export FIRECRAWL_API_KEY="fc-..."
```

A free tier is available (trial credits); paid tiers add higher rate limits, concurrency, and advanced extraction (JSON schema output, `interact`, `monitor`).

## Prerequisites

| Requirement | Details |
|---|---|
| **Firecrawl API key** | `FIRECRAWL_API_KEY` env var — free tier available at firecrawl.dev |
| **Hermes Agent** | Any recent version; the skills are plain markdown workflows + CLI commands |
| **npx / Node.js** | For installing skills via `npx skills add` |
| **Hermes web tools (optional)** | Hermes's own `web_search` / `web_extract` are Firecrawl-backed via the Nous subscription — these skills add direct API control on top |

## What It Provides

### firecrawl/cli (14 skills, 716.0K installs)

| Skill | Installs | Purpose |
|---|---|---|
| `firecrawl` | 97.8K | Core Firecrawl operations: scrape, search, crawl, map, extract |
| `firecrawl-search` | 79.1K | Web search with Firecrawl's search API |
| `firecrawl-scrape` | 78.9K | Single-URL scraping with markdown/JSON output |
| `firecrawl-crawl` | 76.9K | Multi-page crawls with depth and path filters |
| `firecrawl-agent` | 76.8K | Agent-oriented usage patterns for the Firecrawl API |
| `firecrawl-map` | 76.5K | Site URL discovery (sitemap-style mapping) |
| `firecrawl-download` | 76.2K | Download page content/assets |
| `firecrawl-interact` | 61.6K | Browser-interaction scraping (clicks, forms, JS rendering) |
| `firecrawl-parse` | 47.7K | Structured extraction via JSON schema |
| `firecrawl-monitor` | 30.0K | Recurring page monitoring for changes |
| `firecrawl-browser` | 11.4K | Full browser session control for hard-to-scrape pages |
| `firecrawl-instruct` | 3.3K | Natural-language extraction instructions |

### firecrawl-workflows (16 skills, 492.8K installs)

End-to-end pipelines, each 30K+ installs: `firecrawl-deep-research` (32.6K), `firecrawl-research-papers` (31.8K), `firecrawl-website-design-clone` (31.5K), `firecrawl-market-research` (31.1K), `firecrawl-seo-audit` (30.8K), `firecrawl-knowledge-base` (30.7K), `firecrawl-dashboard-reporting` (30.6K), `firecrawl-workflows` (30.5K), `firecrawl-lead-gen` (30.5K), `firecrawl-lead-research` (30.5K), `firecrawl-shop` (30.4K), `firecrawl-qa` (30.4K), `firecrawl-competitive-intel` (30.4K), `firecrawl-knowledge-ingest` (30.4K), `firecrawl-company-directories` (30.4K), `firecrawl-demo-walkthrough` (30.4K).

### firecrawl/skills (41 skills, 252.5K installs)

Build-time skills for integrating Firecrawl into agent apps: `firecrawl-build-scrape` (58.1K), `firecrawl-build-search` (58.0K), `firecrawl-build-interact` (57.8K), `firecrawl-build-onboarding` (57.7K), `firecrawl-research-index` (18.1K), plus deploy/QA/tooling skills (vercel/netlify/render/cloudflare deploys, Notion integration, GitHub CI fixes, playwright, pdf, spreadsheet, screenshot).

### firecrawl/anydoc (1 skill, ~4K installs)

`convert-documents-to-markdown` — convert any document (PDF, docx, xlsx, images) to clean markdown for agent ingestion.

## Quick Start

1. `export FIRECRAWL_API_KEY="fc-..."` and `npx skills add firecrawl/cli`
2. "Scrape https://example.com/pricing and return the markdown"
3. "Search the web for 'AI agent platforms' and summarize the top 10 results"
4. "Run a deep research pass on multi-agent orchestration tooling, cite every claim"
5. "Map every URL on our competitor's site and flag pages mentioning pricing"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Competitive intel** | `firecrawl-competitive-intel` + `firecrawl-seo-audit` against competitor domains before feature/positioning decisions |
| **Market research** | `firecrawl-market-research` for operator pain-point mining — feeds the help-first content engine |
| **Lead research** | `firecrawl-lead-research` + `firecrawl-company-directories` to enrich cold-outreach targets with real site data |
| **Docs SEO** | `firecrawl-seo-audit` as a second opinion alongside the Search Console/Ahrefs/Semrush connector stack |
| **Knowledge ingest** | `firecrawl-anydoc` to convert partner PDFs/research into markdown for the GBrain vault |

## Limitations / Verification

- API-key based: usage is metered against your Firecrawl plan; monitor credit consumption on long crawls
- `interact` and `browser` consume more credits than plain scrape/search
- `monitor` requires a paid plan for recurring schedules
- Skills are agent-agnostic markdown — they work in Hermes sessions the same way as Claude Code

```bash
# Verify key works (free tier)
curl -s -H "Authorization: Bearer $FIRECRAWL_API_KEY" https://api.firecrawl.dev/v1/scrape \
  -d '{"url":"https://example.com","formats":["markdown"]}' -H "Content-Type: application/json" | head -c 300
```

## Related

- [Hermes web tools](https://hermes-agent.nousresearch.com/docs) — built-in Firecrawl-backed `web_search` / `web_extract`
- [Tavily Research Setup](/hermes/skills/catalog/tavily-research-setup/)
- [OSINT Skills — Open-Source Intelligence Suite Setup](/hermes/skills/catalog/osint-skills-setup/)
- [Firecrawl docs](https://docs.firecrawl.dev/)

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
