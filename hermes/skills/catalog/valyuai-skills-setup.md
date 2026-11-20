---
title: "Valyu Search Skills - Web Search and Research APIs"
description: "Setup guide for valyuai/skills: 3.4K combined installs across 1 listing; a Valyu search API skill for search, answers, and deep research."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/valyuai-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "search api", "deep research", "content extraction"]
---

# Valyu Search Skills - Setup Guide

**Source:** [valyuai/skills](https://www.skills.sh/valyuai/skills) via skills.sh - 3.4K combined installs across 1 indexed listing; first seen Nov 19, 2026 (Nov 19, 2026 evening sweep)
**GitHub:** 25 stars, no LICENSE file in the tree (the README states MIT), `main` branch, last pushed 2026-01-21. One skill at `valyu-search/valyu-best-practices/SKILL.md` with a `references/` tree of recipes and integration guides plus a `scripts/` CLI wrapper.
**Category:** Real-time search, content extraction, and deep research API
**Quality Tier:** 🟠 Orange - no LICENSE file (the README states MIT); the single sampled verdict is Pass/Pass/Warn (Snyk).

valyuai/skills is a single-skill collection that turns the Valyu API into an agent toolkit. The one skill, valyu-best-practices, teaches an agent real-time search across web, academic, financial, healthcare, news, prediction-market, transportation, and patent sources, plus content extraction from URLs, AI answers with citations, and multi-step deep research reports.

The skill is structured around recipes: 14 search patterns, 6 content-extraction patterns, 4 answer-generation patterns, and 3 deep-research depth levels, plus 12 platform integration guides and a bundled `valyu` CLI wrapper. A Valyu API key from platform.valyu.ai is a prerequisite, with free credits on signup.

## Installation

```bash
npx skills add valyuAI/skills
```

The skill needs a Valyu API key to do anything useful. Get one at platform.valyu.ai (free credits on signup), then for developer use install the SDK:

```bash
npm install valyu-js
# or
pip install valyu
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| valyu-best-practices | 3,406 | Search 25+ data sources, extract clean markdown from URLs, get AI answers with citations, and run deep research reports through the Valyu API. |

All 1 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

For an agent, search is only as good as the source access behind it. Valyu aggregates web, arXiv and PubMed, SEC filings and stock data, clinical trials and drug labels, FRED and World Bank data, real-time news, prediction-market odds, transport, and patents behind one API, and this skill encodes the recipes to use each one correctly.

The value is in the recipes rather than raw API access. Search recipes cover academic, finance, news, healthcare, prediction markets, brand tracking, and multi-step workflows. Content recipes turn URLs into clean markdown with optional structured extraction, and the answer recipes add citations, which is what a research-facing agent needs to be answerable rather than plausible.

Deep research is the differentiator: three depth levels (fast around 5 minutes, standard around 15, heavy around 90) give an agent a bounded, awaitable research task instead of an open-ended crawl. For a Hermes agent doing literature review or competitive research, that is a concrete tool.

## Usage

| You say | What happens |
|---|---|
| "Search academic papers on transformer attention" | valyu-best-practices runs the academic-search recipe across arXiv and PubMed. |
| "Extract the key findings from this article" | The content recipe pulls clean markdown from the URL, optionally with a structured JSON schema. |
| "What are the latest developments in quantum computing?" | The answer recipe returns an AI-synthesized answer with citations. |
| "Track breaking news about this brand" | The brand-tracking recipe monitors news for the brand with date and country filters. |
| "Do deep research on the AI chip market" | The deep-research recipe creates an awaitable task at fast, standard, or heavy depth. |

## Verification

Confirm the skill landed in the agent skills directory after install, and probe the SKILL.md on the `main` branch before reviewing (returns 200):

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/valyuAI/skills/main/valyu-search/valyu-best-practices/SKILL.md
```

```bash
npx skills add valyuAI/skills --list
```

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| valyu-best-practices | Pass | Pass | Warn |

The sample covers the single indexed listing; it passes Gen Agent Trust Hub and Socket with a Snyk Warn.

## Limitations

- Snapshot data, verified Nov 19, 2026: 3,406 combined installs across 1 indexed listing; 25 GitHub stars; no LICENSE file; last pushed 2026-01-21. Counts drift over time.
- The README states MIT, but the repository tree carries no LICENSE file, so confirm licensing with Valyu before redistribution.
- A Valyu API key is a hard prerequisite; the skill is inert without one, and query volume consumes paid credits after the free tier.
- Everything ships as one skill, so there is no per-recipe install granularity; the full references tree comes along with the single SKILL.md.
- The last push is from January 2026, so the skill has not changed recently despite the active API behind it.

## Related

- [Tavily Search - Official LLM-Optimized Web Search CLI Setup](/hermes/skills/catalog/tavily-search-setup)
- [Brave Search Skills - Web Grounding for Agents](/hermes/skills/catalog/brave-search-skills-setup)
- [Exa Agent Skills - Neural Search API Setup](/hermes/skills/catalog/exa-labs-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Keep queries under 400 characters and split complex requests into several specific queries; the skill documents this as its own best practice.
- Use the answer recipe when you need citations, and the search recipe when you need the raw sources.
- Pick the deep-research depth by deadline: fast for quick lookups, heavy for a comprehensive report.
- Set up the API key in the environment before first use; every recipe assumes it is available.
- Use the content recipe for URL extraction rather than a general scraper; it returns clean markdown with optional schema-driven structure.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
