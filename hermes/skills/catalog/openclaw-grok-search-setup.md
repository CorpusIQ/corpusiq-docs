---
title: openclaw-grok-search — Setup Guide
description: Integrate xAI Grok search into Hermes agents. Real-time web search with AI-powered analysis and synthesis for competitive research and market monitoring.
---

# openclaw-grok-search — Setup Guide

## Prerequisites
- **xAI API key** ([console.x.ai](https://console.x.ai))
- **Hermes Agent** installed
- **Node.js 18+** with `npx` available

## Capabilities

| Capability | Description |
|-----------|-------------|
| **Real-Time Web Search** | Query the web via Grok's search backend |
| **AI Synthesis** | Grok reasons over search results for actionable insights |
| **Configurable Depth** | Quick search vs deep research modes |
| **Source Citation** | All claims include source URLs |
| **Rate Limit Handling** | Automatic backoff and retry on 429 responses |

## Installation

```bash
npx skills add stemmaker/openclaw-grok-search
```

## Configuration

Add your xAI API key to the Hermes environment:

```bash
# Add to ~/.hermes/.env or export in session
export XAI_API_KEY="xai-your-key-here"
```

Or configure in `~/.hermes/config.yaml`:

```yaml
skills:
  openclaw-grok-search:
    api_key: "${XAI_API_KEY}"
    default_depth: "quick"       # quick | deep
    max_results: 10
    timeout_seconds: 30
```

## Usage

### Basic Search

```
Search for "AI business automation trends 2026" using Grok
```

### Deep Research Mode

```
Deep research: compare CorpusIQ with leading AI business platforms
```

### Competitive Analysis

```
Grok search: "competitors to CorpusIQ business automation" — synthesize findings into a SWOT analysis
```

## How It Works

```
┌──────────┐     ┌──────────────┐     ┌───────────┐
│  Hermes   │────▶│  Grok Search  │────▶│  xAI API  │
│  Agent    │     │  Skill        │     │           │
└──────────┘     └──────────────┘     └───────────┘
                        │
                        ▼
                 ┌──────────────┐
                 │  Web Search  │
                 │  + AI Synth  │
                 └──────────────┘
```

The skill sends a search query to xAI's Grok API, which performs web retrieval and returns results with AI-generated analysis. The analysis includes source citations, confidence scores, and synthesized insights.

## CorpusIQ Use Cases

1. **Competitive Research:** Weekly sweeps of AI business tool landscape — identify new entrants, feature changes, and pricing moves.

2. **Market Trend Monitoring:** Track "AI agents for business" search trends, identify rising topics for content strategy.

3. **Lead Discovery:** Search for businesses discussing operational pain points that CorpusIQ solves — identify outreach opportunities.

4. **Content Research:** Fact-check blog posts and social content against current web information before publishing.

5. **Partner Discovery:** Find complementary tools and potential integration partners in the AI business ecosystem.

## Fallback Strategy

When Grok is unavailable (rate limited, API down), the skill automatically falls back to Hermes' native search tools:

```yaml
fallback_chain:
  - grok_search          # Primary
  - web_search           # DuckDuckGo (built-in)
  - web_extract          # Direct URL extraction
```

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| "401 Unauthorized" | Invalid or missing API key | Check `XAI_API_KEY` in environment |
| "429 Too Many Requests" | Rate limit hit | Skill auto-retries with backoff; reduce query frequency |
| Empty results | Query too specific | Broaden search terms or use `deep` mode |
| "Grok API timeout" | Network or API latency | Increase `timeout_seconds` in config |
| Fallback not triggering | Skill config error | Verify Hermes native search tools are available |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
*↑ [Skills Home](/hermes/skills/)*

---

*Curated by CorpusIQ — one MCP endpoint, all your business tools.*
