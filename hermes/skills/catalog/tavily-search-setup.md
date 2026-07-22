---
title: Tavily Search — Official LLM-Optimized Web Search CLI
description: Web search returning LLM-optimized results via the official Tavily CLI. Content snippets, relevance scores, domain filtering, and multiple search depths. 25.7K+ installs. The authoritative Tavily integration for Hermes agents.
---

# Tavily Search — Setup Guide

**Source:** [tavily-ai/skills](https://skills.sh/tavily-ai/skills/tavily-search) (25,700+ installs)
**Category:** Web Search / Research
**Quality Tier:** 🟢 Production

Official Tavily CLI for web search returning LLM-optimized results with content snippets, relevance scores, and metadata. Supports domain filtering, time ranges, and multiple search depths (ultra-fast to advanced). This is the authoritative Tavily integration — not the community OpenClaw wrapper.

---

## Installation

```bash
# Install Tavily CLI
curl -fsSL https://cli.tavily.com/install.sh | bash

# Login with API key
tvly login
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Tavily API key** | Sign up at [tavily.com](https://tavily.com) (free tier: 1,000 searches/month) |
| **curl** | For installer script |
| **tvly CLI** | Installed via the command above |

---

## Key Capabilities

### Search Depths

| Depth | Speed | Use Case |
|---|---|---|
| `ultra-fast` | <1s | Quick fact checks, definitions |
| `fast` | ~1s | General knowledge, news |
| `basic` (default) | ~2s | Balanced depth and speed |
| `advanced` | ~3-5s | Deep research, comprehensive coverage |

### Topics

| Topic | Best For |
|---|---|
| `general` (default) | Broad web search |
| `news` | Recent events, breaking stories |
| `finance` | Stock data, earnings, SEC filings |

---

## Quick Start

```bash
# Basic search
tvly search "quantum computing breakthroughs 2026" --json

# Advanced deep search with more results
tvly search "AI agent frameworks comparison" --depth advanced --max-results 10 --json

# Recent news only
tvly search "OpenAI announcements" --time-range week --topic news --json

# Domain-filtered search
tvly search "SEC filings" --include-domains sec.gov,reuters.com --json

# Include full page content in results
tvly search "react hooks tutorial" --include-raw-content --max-results 3 --json

# Exclude domains
tvly search "climate change" --exclude-domains wikipedia.org --json
```

---

## Options Reference

| Option | Description |
|---|---|
| `--depth` | `ultra-fast`, `fast`, `basic` (default), `advanced` |
| `--max-results` | 0-20 (default: 5) |
| `--topic` | `general` (default), `news`, `finance` |
| `--time-range` | `day`, `week`, `month`, `year` |
| `--include-domains` | Comma-separated domain list |
| `--exclude-domains` | Comma-separated domain list |
| `--include-raw-content` | Include full page content in results |
| `--json` | Machine-readable JSON output |

---

## Hermes Integration

For CorpusIQ growth operations, the Tavily workflow follows this pipeline:

```
search → extract → map → crawl → research
```

### Growth Use Cases

```bash
# Competitor monitoring
tvly search "CorpusIQ competitor AI business intelligence" --depth advanced --topic news --time-range month --json

# Market research
tvly search "business operators AI tools pain points" --depth advanced --max-results 10 --json

# Content research for social
tvly search "ecommerce analytics trends 2026" --time-range week --topic news --json

# Lead discovery
tvly search "shopify merchants looking for analytics" --depth advanced --json
```

---

## Tips

- Always use `--json` for machine-readable output (Hermes agents parse programmatically)
- Start with `basic` depth for exploration, escalate to `advanced` for final research
- Combine `--topic news` with `--time-range week` for trending content
- Tavily results are LLM-optimized — cleaner and more relevant than raw Google scraping

---

## Troubleshooting

| Issue | Solution |
|---|---|
| `tvly: command not found` | Re-run the install script: `curl -fsSL https://cli.tavily.com/install.sh \| bash` |
| Auth errors | Run `tvly login` and paste your API key |
| Rate limiting | Free tier: 1,000 searches/month. Upgrade at tavily.com |
| Empty results | Broaden query, reduce `--max-results`, or use `--depth advanced` |

---

## See Also

- Tavily Research Setup — Deep AI-powered research with citations
- Tavily Search OpenClaw Setup — Community OpenClaw wrapper (alternative)
- [Tavily Docs](https://docs.tavily.com) — Official API documentation
