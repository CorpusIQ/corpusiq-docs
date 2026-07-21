---
title: Tavily Research — AI-Powered Deep Research with Citations
description: Comprehensive AI-powered research that gathers sources, analyzes them, and produces cited reports. 14.1K+ installs. Takes 30-120 seconds. For comparisons, market analysis, and literature reviews.
---

# Tavily Research — Setup Guide

**Source:** [tavily-ai/skills](https://skills.sh/tavily-ai/skills/tavily-research) (14,100+ installs)
**Category:** Web Search / Research
**Quality Tier:** 🟢 Production

AI-powered deep research agent that gathers web sources, synthesizes findings, and produces structured reports with explicit citations. Part of the Tavily workflow pipeline: search → extract → map → crawl → **research**. Takes 30-120 seconds for comprehensive analysis.

---

## Installation

```bash
# Install Tavily CLI (if not already)
curl -fsSL https://cli.tavily.com/install.sh | bash

# Login
tvly login
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Tavily API key** | Sign up at [tavily.com](https://tavily.com) |
| **tvly CLI** | Installed via command above |
| **Research credits** | Research consumes more credits than search — Pro model requires paid plan |

---

## Key Capabilities

### When to Use

- Comprehensive multi-source analysis needed
- Comparison between products, frameworks, or strategies
- Market reports or industry landscaping
- Literature reviews with citations
- When quick searches aren't enough — you need synthesis

### When NOT to Use

- Quick fact-finding → use `tavily-search` instead
- Single-page extraction → use `tavily-extract`
- Known URL analysis → use `firecrawl scrape`

---

## Quick Start

```bash
# Basic research (waits for completion)
tvly research "competitive landscape of AI code assistants in 2026"

# Pro model for comprehensive analysis
tvly research "electric vehicle battery technology market analysis" --model pro

# Stream results in real-time
tvly research "AI agent frameworks comparison LangChain vs CrewAI vs AutoGen" --stream

# Save report to file
tvly research "fintech payment processing trends 2026" --model pro -o fintech-report.md

# Research with specific depth
tvly research "quantum computing commercial applications" --depth advanced
```

---

## Options Reference

| Option | Description |
|---|---|
| `--model` | `basic` (default) or `pro` (comprehensive, requires paid plan) |
| `--stream` | Stream results as they're generated |
| `--depth` | Research depth: `basic` or `advanced` |
| `-o, --output <path>` | Save report to file (markdown) |
| `--max-results` | Max sources to analyze |

---

## Hermes Integration

For CorpusIQ growth operations, Tavily Research is ideal for:

### Market Intelligence
```bash
tvly research "AI-powered business intelligence tools market landscape 2026" \
  --model pro -o ~/corpusiq-brain/research/ai-bi-landscape.md
```

### Competitive Analysis
```bash
tvly research "Compare CorpusIQ alternatives: features, pricing, target audience, strengths, weaknesses" \
  --stream -o ~/corpusiq-brain/research/competitive-analysis.md
```

### Content Research
```bash
tvly research "What problems do ecommerce operators face with data consolidation across Shopify, Meta Ads, and Google Analytics" \
  --model pro -o ~/corpusiq-brain/content/operator-pain-points.md
```

---

## Tips

- Research runs take 30-120 seconds — use `--stream` for progress visibility
- Pro model provides significantly more comprehensive analysis but requires paid Tavily plan
- Save reports to your knowledge base (GBrain) for persistent access
- Combine with `tavily-search` for initial exploration, then `tavily-research` for final synthesis

---

## Troubleshooting

| Issue | Solution |
|---|---|
| Pro model unavailable | Upgrade Tavily plan at tavily.com/pricing |
| Research timeout | Simplify the query or reduce depth |
| Empty citations | Broaden the research topic or use `--depth advanced` |
| Report too long | Use `-o` to save to file instead of stdout |

---

## See Also

- [[tavily-search-setup]] — Quick LLM-optimized web search
- [[tavily-search-openclaw-setup]] — Community OpenClaw wrapper
- [Tavily Docs](https://docs.tavily.com) — Official API documentation
