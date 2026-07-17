---
title: Firecrawl Workflows — Growth & Research Automation for Hermes
description: Install and use firecrawl/firecrawl-workflows (120K combined installs) for automated deep research, lead generation, market research, and SEO auditing from within Hermes agents.
---

# Firecrawl Workflows — Setup Guide

**Source:** [firecrawl/firecrawl-workflows](https://github.com/firecrawl/firecrawl-workflows) (120K+ combined installs)
**Category:** Growth & Research
**Languages:** TypeScript

Production-grade web research and growth workflows from Firecrawl. Four high-value workflows purpose-built for AI agents: deep research (multi-page synthesis with citations), lead generation (automated discovery and enrichment), market research (competitive landscape analysis), and SEO audit (technical and content analysis). All built on Firecrawl's infrastructure with rate limiting, proxy rotation, and JavaScript rendering.

---

## Installation

```bash
# Deep Research — multi-page research synthesis
npx skills add firecrawl/firecrawl-workflows@firecrawl-deep-research

# Lead Generation — automated lead discovery and enrichment
npx skills add firecrawl/firecrawl-workflows@firecrawl-lead-gen

# Market Research — competitive landscape analysis
npx skills add firecrawl/firecrawl-workflows@firecrawl-market-research

# SEO Audit — technical and content SEO analysis
npx skills add firecrawl/firecrawl-workflows@firecrawl-seo-audit

# Knowledge Base — build searchable knowledge bases from websites (bonus)
npx skills add firecrawl/firecrawl-workflows@firecrawl-knowledge-base
```

Verify:
```bash
npx skills list | grep firecrawl
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Firecrawl API Key** | Sign up at [firecrawl.dev](https://firecrawl.dev) — free tier: 500 credits/month |
| **Hermes Agent** | Any version |
| **Node.js** | 18+ |

Set API key:
```bash
export FIRECRAWL_API_KEY="fc-..."
```

---

## Workflow Details

### 1. firecrawl-deep-research (30.5K installs)

Multi-page research with automatic sub-question generation, source tracking, and structured output.

```bash
firecrawl-deep-research "What are the top MCP server frameworks in 2026?" \
    --depth 3 \
    --sources 10 \
    --format markdown
```

| Parameter | Default | Description |
|---|---|---|
| `--depth` | 2 | How many levels of follow-up questions |
| `--sources` | 5 | Minimum unique sources to gather |
| `--format` | markdown | Output format: markdown, json, or html |
| `--citations` | true | Include inline source citations |

**Output structure:**
```markdown
# Research: MCP Server Frameworks 2026

## Executive Summary
...

## Key Findings
1. **Finding one** with [citation](url)
2. **Finding two** with [citation](url)

## Detailed Analysis
...

## Sources
1. [Source Title](url) — Relevance: High
...
```

### 2. firecrawl-lead-gen (29.1K installs)

Automated lead discovery with domain filtering and contact enrichment.

```bash
firecrawl-lead-gen \
    --industry "e-commerce" \
    --company-size "10-200" \
    --role "CTO, VP Engineering" \
    --domains "shopify.com,bigcommerce.com" \
    --max-leads 50
```

| Parameter | Default | Description |
|---|---|---|
| `--industry` | (required) | Target industry |
| `--company-size` | any | Employee count range |
| `--role` | any | Target job titles |
| `--domains` | (optional) | Limit to specific domains |
| `--enrich` | true | Find email, LinkedIn, company data |
| `--max-leads` | 25 | Cap results |

**Output:** CSV with columns: Company, Contact Name, Title, Email, LinkedIn, Company Size, Funding, Tech Stack.

### 3. firecrawl-market-research (29.4K installs)

Competitive landscape mapping with feature comparison and pricing analysis.

```bash
firecrawl-market-research \
    --company "CorpusIQ" \
    --competitors "Glean, Notion AI, Mem, Tana" \
    --dimensions "features,pricing,positioning,gtm"
```

| Parameter | Default | Description |
|---|---|---|
| `--company` | (required) | Your company name |
| `--competitors` | (required) | Comma-separated competitor list |
| `--dimensions` | all | What to analyze |
| `--depth` | 2 | Research depth per competitor |

**Output structure:**
- Feature comparison matrix
- Pricing tier comparison
- Positioning/messaging analysis
- GTM strategy comparison
- Strengths/weaknesses per competitor

### 4. firecrawl-seo-audit (29.2K installs)

Technical SEO crawl with content gap analysis.

```bash
firecrawl-seo-audit https://corpusiq.io \
    --competitors "glean.com,notion.so" \
    --check "technical,content,backlinks"
```

| Check Type | What It Covers |
|---|---|
| **technical** | Broken links, redirects, metadata, schema, Core Web Vitals |
| **content** | Keyword gaps, thin content, duplicate content, readability |
| **backlinks** | Domain authority, referring domains, anchor text distribution |

---

## Hermes/CorpusIQ Relevance

### Growth Operations
- **`firecrawl-lead-gen`** automates prospect discovery for CorpusIQ outreach campaigns. Replace manual LinkedIn searches with automated, enriched lead lists.
- **`firecrawl-market-research`** feeds the product roadmap with competitive intelligence — feature gaps, pricing opportunities, and positioning insights.

### Research & Intelligence
- **`firecrawl-deep-research`** replaces hours of manual competitive analysis. One command produces a cited research report.
- **`firecrawl-seo-audit`** maintains corpusiq-docs' search visibility across 1,000+ pages.

### Integration Pattern

All workflows can be chained into automated research pipelines:

```bash
#!/bin/bash
# Weekly competitive intelligence pipeline
# Save to: ~/.hermes/profiles/corpusiq/cron/weekly-competitive-intel.sh

WEEK=$(date +%Y-W%V)
OUTDIR=~/corpusiq-brain/research/$WEEK
mkdir -p $OUTDIR

# 1. Market landscape
firecrawl-market-research \
    --company "CorpusIQ" \
    --competitors "Glean, Notion AI, Mem, Tana, Coda AI" \
    > $OUTDIR/market-landscape.md

# 2. Deep dive on top competitor
firecrawl-deep-research \
    "Glean AI enterprise search features pricing 2026" \
    --depth 3 --sources 15 \
    > $OUTDIR/glean-deep-dive.md

# 3. SEO gap analysis
firecrawl-seo-audit https://corpusiq.io \
    --competitors "glean.com" \
    > $OUTDIR/seo-gap-analysis.md

# 4. Import to GBrain for semantic search
cd ~/corpusiq-brain && gbrain import research/$WEEK/ --no-embed
```

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `FIRECRAWL_API_KEY not set` | Missing API key | Sign up at firecrawl.dev, export key |
| Rate limited (429) | Free tier limits | Upgrade or add delays between calls |
| Empty lead results | Too restrictive filters | Broaden `--industry` or remove `--domains` |
| Research too shallow | Low `--depth` | Increase to 3-4 for comprehensive coverage |
| SEO audit timeout | Large site | Add `--pages 100` to limit crawl scope |

---

## See Also

- [Firecrawl Skills](/hermes/skills/catalog/firecrawl/) — Core Firecrawl scraping and search skills
- [Apify Agent Skills](/hermes/skills/catalog/apify-agent-skills-setup/) — Alternative web scraping (30K Actors)
- [agent-browser](/hermes/skills/catalog/agent-browser-setup/) — Browser automation for custom scraping
