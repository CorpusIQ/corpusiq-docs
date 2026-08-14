---
title: "SEO GEO Claude Skills — 20-Skill SEO & Generative Engine Optimization Suite Setup for Hermes Agents"
description: "aaron-he-zhu/seo-geo-claude-skills — 20 skills, 126.6K installs. Backlink analysis (26.1K), keyword research, competitor analysis, technical/on-page SEO, GEO content optimization for AI answer engines, schema markup, SERP analysis, rank tracking, entity optimization."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/seo-geo-claude-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-14"
tags: ["hermes skill", "agent skill", "skill setup", "seo", "geo", "generative engine optimization", "content"]
---

# SEO GEO Claude Skills — Setup Guide

**Source:** [aaron-he-zhu/seo-geo-claude-skills](https://skills.sh/aaron-he-zhu/seo-geo-claude-skills)
**GitHub:** [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills)
**Skills:** 20 skills (126.6K combined installs)
**Category:** SEO / GEO / Content Operations
**First Seen:** August 14, 2026 afternoon sweep
**Quality Tier:** 🟢 Production (flagship `backlink-analyzer` at 26.1K installs)

A complete SEO and GEO (Generative Engine Optimization) toolkit — GEO being the newer frontier: optimizing content so AI answer engines (Perplexity, ChatGPT, Gemini) cite and surface it. Twenty skills cover the full loop from keyword research through rank tracking, with dedicated GEO content optimization, entity optimization, and schema markup generation. Complements the CorpusIQ docs SEO/AEO/GEO pass workflow.

---

## Installation

```bash
npx skills add aaron-he-zhu/seo-geo-claude-skills
```

The skills are workflow packages — pair them with your existing SEO data sources (Google Search Console, Ahrefs, Semrush connectors, Firecrawl SEO audit).

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| `backlink-analyzer` | 26.1K | Analyze backlink profiles: quality, relevance, toxic links |
| `seo-content-writer` | 7.6K | Write search-optimized content briefs and drafts |
| `keyword-research` | 6.8K | Find winnable keywords by intent and difficulty |
| `competitor-analysis` | 6.0K | Deconstruct competitor ranking strategy |
| `technical-seo-checker` | 5.6K | Crawl diagnostics: indexing, speed, structure |
| `on-page-seo-auditor` | 5.4K | Per-page optimization audit |
| `geo-content-optimizer` | 5.4K | Optimize content for AI answer engines |
| `content-quality-auditor` | 5.2K | Content depth and E-E-A-T review |
| `content-gap-analysis` | 5.1K | Find topics competitors cover that you do not |
| `meta-tags-optimizer` | 5.1K | Title/description optimization at scale |
| `internal-linking-optimizer` | 5.0K | Internal link architecture improvements |
| `schema-markup-generator` | 5.0K | JSON-LD structured data generation |
| `serp-analysis` | 4.9K | Decode SERP features and intent |
| `memory-management` | 4.9K | Persistent SEO context across sessions |
| `performance-reporter` | 4.8K | SEO KPI reporting |
| `content-refresher` | 4.8K | Refresh decaying content |
| `alert-manager` | 4.7K | Ranking/health alert workflows |
| `rank-tracker` | 4.7K | Position tracking workflows |
| `domain-authority-auditor` | 4.7K | Domain authority assessment |
| `entity-optimizer` | 4.7K | Entity-based optimization for semantic search |

## Quick Start

1. `npx skills add aaron-he-zhu/seo-geo-claude-skills`
2. "Run a technical SEO check on corpusiq.io and list blockers in priority order"
3. "Audit this page for GEO readiness — will an AI answer engine cite it, and why or why not"
4. "Generate schema markup for a docs page and a product page"
5. "Compare our content coverage against our top 3 competitors and list gaps"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Docs SEO/AEO/GEO pass** | `geo-content-optimizer` + `schema-markup-generator` extend the existing docs SEO pass (frontmatter, llms.txt, JSON-LD) |
| **GEO tracking** | `entity-optimizer` + `rank-tracker` feed the TimeToPost/GEO monitoring thesis from the MCP sweeps |
| **Content engine** | `content-gap-analysis` + `seo-content-writer` generate briefs for the help-first content pipeline |
| **Competitor teardown** | `competitor-analysis` + `backlink-analyzer` enrich connector data (Ahrefs/Semrush) with workflow structure |

## Related

- [Marketing Skills — Growth Tooling Setup](/hermes/skills/catalog/marketingskills-setup/)
- [Firecrawl Skills Setup](/hermes/skills/catalog/firecrawl-skills-setup/) — `firecrawl-seo-audit` workflow
- [OPC Skills — SEO GEO Setup](/hermes/skills/catalog/opc-skills-setup/)

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
