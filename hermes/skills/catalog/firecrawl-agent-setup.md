---
title: Firecrawl Agent — AI-Powered Structured Data Extraction
description: Autonomous data extraction that navigates complex sites and returns structured JSON. 73.9K+ installs. Use for pricing extraction, product listings, directory scraping, and any multi-page structured data extraction.
---

# Firecrawl Agent — Setup Guide

**Source:** [firecrawl/cli](https://skills.sh/firecrawl/cli/firecrawl-agent) (73,900+ installs)
**Category:** Web Extraction / Data
**Quality Tier:** 🟢 Production

AI-powered autonomous extraction agent. Unlike simple scraping, the Firecrawl Agent navigates complex multi-page sites, figures out where the data lives, and returns structured JSON. Takes 2-5 minutes per run. Part of the Firecrawl CLI ecosystem alongside `firecrawl-scrape`, `firecrawl-crawl`, and `firecrawl-search`.

---

## Installation

```bash
# Install Firecrawl CLI
npm install -g firecrawl

# Or run via npx
npx firecrawl agent "your query"
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Firecrawl API key** | Sign up at [firecrawl.com](https://firecrawl.com) |
| **Node.js 18+** | Required for CLI |
| **API key config** | `export FIRECRAWL_API_KEY=fc-...` or pass `--api-key` |

---

## Key Capabilities

### When to Use

- You need structured data from complex multi-page sites
- Manual scraping would require navigating many pages
- You want the AI to figure out where the data lives
- Extracting pricing tiers, product listings, or directory entries

### When NOT to Use

- Simple single-page extraction → use `firecrawl scrape` (faster, cheaper)
- Known URLs with fixed structure → use `firecrawl scrape` with extract schema
- Bulk crawling without structure → use `firecrawl crawl`

---

## Quick Start

```bash
# Extract structured data (waits for completion)
firecrawl agent "extract all pricing tiers from example.com" --wait -o pricing.json

# With JSON schema for predictable output
firecrawl agent "extract products" \
  --schema '{"type":"object","properties":{"name":{"type":"string"},"price":{"type":"number"}}}' \
  --wait -o products.json

# Focus on specific pages
firecrawl agent "get feature list" --urls "https://example.com/features" --wait -o features.json

# Pretty-print output
firecrawl agent "extract team members" --wait --pretty
```

---

## Options Reference

| Option | Description |
|---|---|
| `--urls <urls>` | Starting URLs for the agent |
| `--model <model>` | Model: `spark-1-mini` (faster) or `spark-1-pro` (smarter) |
| `--schema <json>` | JSON schema for structured output |
| `--schema-file <path>` | Path to JSON schema file |
| `--max-credits <n>` | Credit limit for this agent run |
| `--wait` | Wait for agent to complete (recommended) |
| `--pretty` | Pretty print JSON output |
| `-o, --output <path>` | Output file path |

---

## Hermes Integration

For CorpusIQ growth operations:

```bash
# Competitor pricing extraction
firecrawl agent "extract all pricing plans and features" \
  --urls "https://competitor.com/pricing" \
  --schema '{"type":"object","properties":{"tiers":{"type":"array","items":{"type":"object","properties":{"name":{"type":"string"},"price":{"type":"string"},"features":{"type":"array","items":{"type":"string"}}}}}}}' \
  --wait -o ~/corpusiq-brain/research/competitor-pricing.json

# Lead generation from directories
firecrawl agent "extract company name, website, and description for all listings" \
  --urls "https://directory.example.com/ai-tools" \
  --max-credits 50 --wait -o leads.json
```

---

## Tips

- Always use `--wait` to get results inline — without it, returns a job ID
- Use `--schema` for predictable, structured output — otherwise agent returns freeform data
- Agent runs consume more credits than simple scrapes — use `--max-credits` to cap spending
- For simple single-page extraction, prefer `firecrawl scrape` — faster and cheaper

---

## Troubleshooting

| Issue | Solution |
|---|---|
| `FIRECRAWL_API_KEY not set` | Export your key: `export FIRECRAWL_API_KEY=fc-...` |
| Agent timeout | Increase `--max-credits` or simplify the query |
| Schema mismatch | Ensure JSON schema is valid — test with `echo '{"type":"object"}' | jq` |
| No results | Try broader starting URLs — agent needs entry points to navigate from |

---

## See Also

- [Firecrawl Docs](https://docs.firecrawl.com) — Core Firecrawl CLI setup and configuration
- [[firecrawl-workflows-setup]] — Multi-step extraction workflows
- [Firecrawl Docs](https://docs.firecrawl.com) — Official documentation
