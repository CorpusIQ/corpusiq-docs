---
title: "Bright Data Agent Skills — Web Scraping & Research Setup"
description: "brightdata/skills — 22 skills, 26.9K installs: web scraping, search, SEO audit, competitive intelligence, and brand listening from the Bright Data team."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/brightdata-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "web scraping", "research", "seo"]
---

# Bright Data Agent Skills — Setup Guide

**Source:** [brightdata/skills](https://skills.sh/brightdata/skills)
**GitHub:** [brightdata/skills](https://github.com/brightdata/skills)
**Skills:** 22 skills · 26.9K total installs
**Category:** Web Scraping & Research
**First Seen:** catalogued August 15, 2026 evening sweep
**Quality Tier:** 🟢 Production (official org — Bright Data, the web data platform vendor)

Bright Data's official agent skills cover the full web-data lifecycle: scraping, search, SEO audits, competitive intelligence, brand listening, price comparison, data feeds, and a scraping browser debugger — the operational layer for agent-driven web research. Carried in the sweep queue for weeks; drafted now on publisher-page verification of 26.9K installs across 22 skills.

---

## Installation

```bash
npx skills add brightdata/skills
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Bright Data account** | API credentials for most skills |
| **Bright Data proxies** | For scrape and browser skills at scale |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| scrape | 10.7K | Structured web scraping |
| search | 7.3K | Web search via Bright Data |
| brightdata-cli | 1.9K | CLI interaction |
| seo-audit | 1.7K | SEO auditing |
| bright-data-best-practices | 1.7K | Platform best practices |
| bright-data-mcp | 956 | MCP server integration |
| agent-onboarding | 518 | Agent onboarding workflow |
| scraper-builder | 276 | Build custom scrapers |
| data-feeds | 267 | Feed-based data collection |
| competitive-intel | 226 | Competitive intelligence gathering |
| design-mirror | 222 | Mirror site designs |
| brd-browser-debug | 189 | Scraping browser debugging |
| brightdata-sdk | 160 | SDK usage |
| price-comparison | 139 | Price comparison scraping |
| scraper-studio | 121 | Scraper Studio workflows |
| brightdata-proxy | 105 | Proxy configuration |
| discover-api | 93 | Discovery API |
| live-research | 90 | Live research workflows |
| brand-listening | 89 | Brand mentions monitoring |
| brightdata-sdk-js / python-sdk-best-practices | 87 / 47 | SDK guidance |
| rag-pipeline | 82 | RAG data pipelines |

## Quick Start

1. Install: `npx skills add brightdata/skills`
2. Start with `scrape` and `search` — the highest-install pair
3. Ask: "scrape this site and run a competitive intelligence pass on the pricing table"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Research sweeps** | scrape + search as a resilient fallback when primary search backends degrade |
| **Competitive research** | competitive-intel and price-comparison for market analysis |
| **SEO work** | seo-audit pairs with our Ahrefs and Search Console connectors |
| **Brand monitoring** | brand-listening for CorpusIQ mentions across the web |

## Limitations / Verification

- Publisher-page install counts verified; individual skill audit pages were not fetched for this multi-skill suite
- Most skills require a paid Bright Data account with proxy allocation
- Scraping must respect robots.txt and site terms — the skills do not override that

```bash
npx skills add brightdata/skills   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
