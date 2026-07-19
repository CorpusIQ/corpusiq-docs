---
title: parallel-web/parallel-agent-skills — Web Intelligence for Hermes Agents
description: Install parallel-web/parallel-agent-skills@parallel-monitor (9.2K installs) for agent-native web search, content extraction, deep research, and data enrichment. Works with Claude Code, Cursor, Codex CLI, and GitHub Copilot.
---

# parallel-web/parallel-agent-skills — Setup Guide

**Source:** [parallel-web/parallel-agent-skills](https://github.com/parallel-web/parallel-agent-skills) (9.2K installs for parallel-monitor)
**Category:** Web Intelligence / Agent Tools
**Harnesses:** Claude Code, Codex CLI, Cursor, GitHub Copilot, Cline

Web search, content extraction, deep research, and data enrichment for AI coding agents. Built on [Parallel](https://parallel.ai) infrastructure. Provides agents with real-time web access for research, monitoring, and data gathering — without the overhead of managing browser instances.

---

## Installation

### Claude Code (Recommended for Hermes)

```bash
# Add the marketplace
/plugin marketplace add parallel-web/parallel-agent-skills

# Install the Parallel plugin
/plugin install parallel

# RESTART Claude Code before continuing!

# Setup CLI + auth
/parallel:parallel-cli-setup
```

### Skills.sh (Universal)

```bash
# Install all Parallel skills into any compatible agent
npx skills add parallel-web/parallel-agent-skills@parallel-monitor
```

### OpenAI Codex

```text
$skill-installer parallel-web/parallel-agent-skills
/parallel:parallel-cli-setup
```

Verify:
```bash
parallel-cli status
# Should show: Authenticated ✓, Balance: $X.XX
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **parallel-cli** | Install via skill setup or directly: `npm i -g parallel-cli` |
| **API Key** | Get from [parallel.ai](https://parallel.ai) — free tier available |
| **Hermes Agent** | Any version with Claude Code plugin support |
| **Funded Account** | Required for web extraction (pay-as-you-go) |

Install CLI if missing:
```bash
npm install -g parallel-cli
parallel-cli auth login
```

---

## Key Skills

| Skill | Installs | Purpose |
|---|---|---|
| **parallel-monitor** | 9.2K | Monitor websites for changes, trigger on conditions |
| **parallel-search** | Included | Web search with structured results |
| **parallel-extract** | Included | Content extraction from URLs |
| **parallel-deep-research** | Included | Multi-source research synthesis |
| **parallel-data-enrich** | Included | Enrich data with web sources |
| **parallel-cli-setup** | Included | One-time CLI install + auth setup |

---

## Common Workflows for CorpusIQ

### Competitive Monitoring

```bash
# Monitor competitor pricing pages for changes
/parallel:monitor \
  --url "https://competitor.com/pricing" \
  --check-interval 6h \
  --alert-on "price change" \
  --notify telegram

# Monitor competitor blog for new posts
/parallel:monitor \
  --url "https://competitor.com/blog" \
  --check-interval 24h \
  --alert-on "new article" \
  --extract-title-and-summary
```

### Market Research

```bash
# Deep research on a market segment
/parallel:deep-research \
  --topic "AI agent orchestration platforms 2026" \
  --sources 10 \
  --output market-research.md

# Search for specific intel
/parallel:search \
  --query "CorpusIQ competitors funding announcements 2026" \
  --max-results 15 \
  --output competitor-intel.json
```

### Content Research

```bash
# Extract content from multiple URLs for blog research
/parallel:extract \
  --urls "https://example1.com,https://example2.com,https://example3.com" \
  --format markdown \
  --output research-notes.md

# Enrich lead data with web sources
/parallel:data-enrich \
  --input leads.csv \
  --columns company_name,website \
  --enrich company_size,industry,funding \
  --output enriched-leads.csv
```

### Social Media Monitoring

```bash
# Monitor brand mentions (combined with web search)
/parallel:monitor \
  --search "CorpusIQ" \
  --sources web,news,social \
  --check-interval 12h \
  --output-dir ./brand-monitoring/
```

---

## Comparison: parallel-web vs Other Web Tools

| Feature | parallel-web | Firecrawl | agent-browser | Apify |
|---|---|---|---|---|
| **Web search** | ✅ Structured | ✅ Structured | ❌ (browser only) | ✅ via Actors |
| **Content extraction** | ✅ Parallel infra | ✅ Single-page | ✅ Accessibility tree | ✅ via Actors |
| **Monitoring** | ✅ Built-in | ✅ Built-in | ❌ Manual | ✅ via Schedules |
| **Deep research** | ✅ Multi-source | ✅ Workflows | ❌ | ✅ via Actors |
| **Data enrichment** | ✅ Built-in | ❌ | ❌ | ✅ via Actors |
| **Install base** | 9.2K | 120K | 553K | 2.5K |
| **Hermes integration** | Via Claude Code plugin | Via CLI/MCP | Via MCP | Via API |
| **Pricing** | Pay-as-you-go | Subscription | Free (OSS) | Pay-per-use |

**Recommendation:** Use parallel-web for monitoring and deep research. Use agent-browser for one-off interactive browsing. Use Firecrawl for bulk extraction. They complement each other.

---

## Integration with Hermes Agent

### Direct CLI Usage

```bash
# From Hermes terminal
parallel-cli search "hermes agent plugins" --max-results 10
parallel-cli extract "https://example.com" --format markdown
parallel-cli monitor --url "https://target.com" --interval 6h
```

### Via Claude Code Plugin

```bash
# Interactive within Hermes Claude Code session
/parallel:search --query "latest AI agent frameworks" --max 5
/parallel:deep-research --topic "agent memory systems comparison"
/parallel:monitor --url "https://competitor.com" --interval 12h
```

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `/parallel: command not found` | Plugin not installed | `/plugin install parallel` then restart |
| `parallel-cli: not found` | CLI not installed | `npm install -g parallel-cli` |
| `Authentication failed` | API key expired/missing | `parallel-cli auth login` |
| `Insufficient balance` | Account needs funds | Add funds at [parallel.ai](https://parallel.ai) |
| Monitor not triggering | Interval too long / URL changed | Check monitor status: `parallel-cli monitor list` |
| Timeout on extract | Page too large / JS-heavy | Increase timeout: `--timeout 30` |

---

## See Also

- [Firecrawl Workflows Setup](/hermes/skills/catalog/firecrawl-workflows-setup/) — Web scraping and SEO audits (120K installs)
- [agent-browser Setup](/hermes/skills/catalog/agent-browser-setup/) — Accessibility-tree browser automation (553K installs)
- [Apify Agent Skills Setup](/hermes/skills/catalog/apify-agent-skills-setup/) — Web scraping Actors
- [wshobson Agents Marketplace](/hermes/skills/catalog/wshobson-agents-setup/) — 94-plugin agent marketplace
