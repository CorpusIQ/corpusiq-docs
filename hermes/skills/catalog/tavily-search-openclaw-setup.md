---
title: Tavily Search — Web Search for OpenClaw Setup Guide
description: Setup guide for the tavily-search skill — AI-optimized web search for OpenClaw agents. Real-time search with source attribution, topic extraction, and structured results.
last_updated: 2026-07-08
---

# Tavily Search — Web Search for OpenClaw

**Publisher:** [framix-team](https://skills.sh/framix-team/openclaw-tavily) | **Installs:** 797 | **Category:** Search

Integrates the Tavily Search API into OpenClaw — purpose-built search for AI agents. Returns clean, structured results with source attribution, topic classification, and content extraction. Far better than raw Google scraping for agent consumption.

## Prerequisites

- OpenClaw installed and running
- [Tavily API key](https://tavily.com) (free tier: 1,000 searches/month)
- Node.js 18+
- `npx` available

## Installation

```bash
npx skills add framix-team/openclaw-tavily/tavily-search
```

## Configuration

Get your API key from [tavily.com](https://app.tavily.com) and configure:

```json
{
  "tavily": {
    "apiKey": "${TAVILY_API_KEY}",
    "searchDepth": "advanced",
    "maxResults": 10,
    "includeAnswer": true,
    "includeRawContent": false,
    "includeImages": false,
    "searchDomain": "general"
  }
}
```

```bash
export TAVILY_API_KEY="tvly-..."
```

| Setting | Default | Description |
|---------|---------|-------------|
| `searchDepth` | `advanced` | `basic` (fast) or `advanced` (comprehensive) |
| `maxResults` | `10` | Max results per search (1-20) |
| `includeAnswer` | `true` | Include AI-generated answer summary |
| `includeRawContent` | `false` | Include full page text (token-heavy) |
| `includeImages` | `false` | Include image results |
| `searchDomain` | `general` | `general` or `news` for time-sensitive queries |

## Capabilities

### AI-Optimized Search

- Searches across the web with a single API call
- Returns cleaned, structured results (no HTML noise)
- AI-generated answer synthesis from top results
- Source attribution with URLs and relevance scores

### Topic Extraction

- Classifies search results by topic
- Identifies key entities and relationships
- Groups related results for consumption

### Content Extraction

- Extracts clean text from result pages
- Removes ads, navigation, and boilerplate
- Returns structured content for agent reasoning

## CLI Reference

```
Command                       Description
──────────────────────────────────────────────
tavily-search <query>         Run a web search
tavily-search news <query>    Search recent news
tavily-search extract <url>   Extract content from URL
tavily-search topics <query>  Get topic breakdown
tavily-search answer <query>  Get AI-generated answer only
```

## Example Usage

```bash
# Basic search
tavily-search "latest Hermes agent updates 2026"

# News search (time-sensitive)
tavily-search news "OpenAI GPT-5 announcement"

# Extract content from a specific page
tavily-search extract "https://hermes-agent.nousresearch.com/docs"

# Get topic analysis
tavily-search topics "autonomous AI agent deployment patterns"
```

## CorpusIQ Use Cases

- **Market research:** Agent searches for competitor updates, industry trends, pricing changes
- **Content curation:** Gather sources for blog posts, social media content, newsletters
- **Lead research:** Research prospect companies before outreach
- **Technical research:** Search for solutions to agent-deployment problems
- **News monitoring:** Track mentions of CorpusIQ and ecosystem partners

## Troubleshooting

### API key not recognized

```bash
# Verify key is set
echo $TAVILY_API_KEY

# Test directly
curl -s "https://api.tavily.com/search" \
  -H "Content-Type: application/json" \
  -d '{"api_key":"'$TAVILY_API_KEY'","query":"test"}'
```

### Search returns empty

- Check `searchDomain` — `news` only returns recent content
- Try `searchDepth: basic` — `advanced` may be slower but more thorough
- Verify API key has quota remaining

### Rate limiting

```bash
# Check remaining quota
curl -s "https://api.tavily.com/usage" \
  -H "Content-Type: application/json" \
  -d '{"api_key":"'$TAVILY_API_KEY'"}'
```

Free tier: 1,000 searches/month. Upgrade for higher limits.

---

*← [Tavily Search Setup Guide](/hermes/skills/catalog/tavily-search-openclaw-setup/) | [Discovery Page](/hermes/skills/marketplace/new-june28-2026/) →*

*↑ [Skills Catalog](/hermes/skills/catalog/)*

---

*Part of the Hermes Skills Library — curated by CorpusIQ. Content remains attributed to original authors and repositories. [CorpusIQ](https://corpusiq.io) — one MCP endpoint, all your business tools.*
