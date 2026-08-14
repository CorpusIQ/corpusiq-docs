---
title: "New Skills — August 14, 2026 (Afternoon)"
description: "skills.sh afternoon sweep — 6 new publisher clusters with setup guides: Firecrawl official skills (1.47M installs, 4 repos), Nexscope E-Commerce (126K, 121 skills), SEO GEO Claude Skills (126K, 20 skills), n8n Skills (58K, 29 skills), Review Loop (24.6K, #1 hot)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-aug14-2026-afternoon/"
robots: "index,follow"
last_updated: "2026-08-14"
tags: ["hermes skill", "agent skill", "skill marketplace", "skills.sh"]
sweep_id: aug-14-2026-afternoon
new_publishers: 6
new_skills: 241
guides_drafted: 5
---

# New Skills — August 14, 2026 (Afternoon)

**Source:** [skills.sh](https://skills.sh) leaderboards + REST API multi-query sweep
**Date:** August 14, 2026 (afternoon)
**Result:** 6 new publisher clusters · 241 skills · ~1.8M combined installs · 5 setup guides

Sweep combined the hot (1H delta) and trending (24h) leaderboards with 20 API queries, cross-referenced 1,870 unique skills against the existing `hermes/skills/` tree. Five uncovered clusters with substantive Hermes value were guided; the morning sweep's coverage (Chrome DevTools MCP, Oh My Hermes) and prior guides (Caveman, Nexscope Amazon, Self-Improving Agent) were confirmed present and not duplicated.

---

## New Publisher Clusters (6) — 5 With Setup Guides

### 1. Firecrawl Official Skills — `firecrawl/*` (4 repos, ~1.47M installs)

The largest gap found this sweep. Firecrawl — the engine behind Hermes's own `web_search`/`web_extract` — publishes 4 official skill repos. `firecrawl/cli` (14 skills, 716K) covers core scrape/search/crawl/map/parse/monitor/browser operations; `firecrawl-workflows` (16 skills, 493K) ships end-to-end research pipelines (deep research, market research, SEO audit, lead gen, competitive intel); `firecrawl/skills` (41 skills, 253K) covers integration builds; `firecrawl/anydoc` converts documents to markdown.

**Setup guide:** [Firecrawl Skills Setup](/hermes/skills/catalog/firecrawl-skills-setup/)

### 2. Nexscope E-Commerce Skills — `nexscope-ai/ecommerce-skills` (121 skills, 126.1K)

The marketplace companion to the already-documented Amazon repo. Flagship `cross-border-ecommerce` (62.2K) plus Shopify/Etsy/TikTok Shop/eBay/Walmart playbooks, dropshipping research, PPC planning, email marketing — the general e-commerce stack for agents serving operators.

**Setup guide:** [Nexscope E-Commerce Skills Setup](/hermes/skills/catalog/nexscope-ecommerce-skills-setup/)

### 3. SEO GEO Claude Skills — `aaron-he-zhu/seo-geo-claude-skills` (20 skills, 126.6K)

Complete SEO + GEO (Generative Engine Optimization) toolkit: backlink analysis (26.1K), keyword research, technical/on-page audits, GEO content optimization for AI answer engines, schema markup, SERP analysis, rank tracking, entity optimization.

**Setup guide:** [SEO GEO Claude Skills Setup](/hermes/skills/catalog/seo-geo-claude-skills-setup/)

### 4. n8n Skills — `czlonkowski/n8n-skills` + official `n8n-io/skills` (29 skills, ~58K)

Workflow automation fluency for agents: design patterns, node configuration, MCP tool integration, JavaScript/Python code nodes, subworkflows, self-hosting, error handling. Community suite (15 skills, 48.4K) + official vendor skills (14 skills).

**Setup guide:** [n8n Skills Setup](/hermes/skills/catalog/n8n-skills-setup/)

### 5. Review Loop — `2dmurali/review-loop-skill` (1 skill, 24.6K)

Fastest-rising skill on the marketplace: #1 on the hot leaderboard with +399 installs in a single hour. A focused review → feedback → verify loop for code changes.

**Setup guide:** [Review Loop Skill Setup](/hermes/skills/catalog/review-loop-skill-setup/)

---

## Evaluated and Queued for Evening Sweep

| Skill / Cluster | Installs | Status |
|---|---|---|
| `herdr` (herdrdev/herdr) | 26.1K | Multi-agent orchestration ("herd" driver) — needs deeper Hermes compatibility check |
| `last30days` (mvanhorn/last30days-skill) | 32.0K | Growth/recap skill — purpose verification pending |
| `agent-config` (brianlovin/agent-config) | 13.3K (`simplify`) | Design-quality config suite — partial overlap with existing UI/UX guides |
| `stop-slop` (hardikpandya/stop-slop) | 10.4K | AI-slop content cleaner — pairs with anti-slop tooling already tracked |
| `web-access` (eze-is/web-access) | 15.6K | Web access skill — overlaps Hermes built-in web tools |
| `brightdata/skills` | 10.7K (`scrape`) | Bright Data proxy scraping — API-key gated |
| `langfuse/skills` | 12.6K | LLM observability — overlaps Hermes token/cost tooling |
| `agent-playbook` (zhaono1/agent-playbook) | 33.0K | Agent role suite — sibling of the documented charon-fan playbook |

---

## Installation

```bash
# Firecrawl official skills
npx skills add firecrawl/cli && npx skills add firecrawl/firecrawl-workflows
npx skills add firecrawl/skills && npx skills add firecrawl/anydoc

# E-commerce + SEO + automation + review
npx skills add nexscope-ai/ecommerce-skills
npx skills add aaron-he-zhu/seo-geo-claude-skills
npx skills add czlonkowski/n8n-skills
npx skills add 2dmurali/review-loop-skill
```

## Notable

- **Firecrawl** is the sweep's standout: official vendor skills for the exact engine Hermes already uses — first-party scraping workflows that extend built-in web tools with API-level control.
- **SEO GEO Claude Skills** lands directly on the docs SEO/AEO/GEO strategy — GEO optimization for AI answer engines is the same thesis CorpusIQ docs already ship.
- **n8n skills** target business operators — the core CorpusIQ audience — with MCP integration patterns that mirror the CorpusIQ connector protocol.
