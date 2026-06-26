---
title: MentionsAPI MCP Server Integration Guide
description: Track brand mentions across AI platforms (ChatGPT, Claude, Gemini, Perplexity, Google AI) with MentionsAPI MCP server for Hermes Agent
category: mcp
tags: [mcp, mentionsapi, brand-monitoring, geo, ai-visibility, hermes-agent]
last_updated: 2026-06-26
---

# MentionsAPI MCP — AI Brand Monitoring for Hermes Agent

Track your brand's presence across every major AI platform from a single MCP server.

## What It Does

MentionsAPI monitors your brand mentions, search rankings, and citations across:

- **ChatGPT** — brand mentions in ChatGPT responses
- **Claude** — Anthropic Claude citations
- **Gemini** — Google Gemini references
- **Perplexity** — Perplexity AI citations
- **Google AI Overviews** — AI-generated search results
- **AI Mode** — Google AI Mode results
- **Bing Copilot** — Microsoft Copilot mentions

For operators investing in **GEO (Generative Engine Optimization)** and **AEO (Answer Engine Optimization)**, this is essential visibility infrastructure.

## Quick Setup

### Prerequisites
- **MentionsAPI account:** Sign up at [mentionsapi.com](https://mentionsapi.com) (first $1 credit free)
- **API key:** Available in your dashboard after signup

### Add to Hermes Agent

```bash
# Install via npx
hermes mcp add mentionsapi -- npx -y @mentionsapi/mcp

# Or configure manually in hermes config:
```

```json
{
  "mcpServers": {
    "mentionsapi": {
      "command": "npx",
      "args": ["-y", "@mentionsapi/mcp"],
      "env": {
        "MENTIONSAPI_KEY": "your-api-key"
      }
    }
  }
}
```

### Authentication
MentionsAPI uses API key authentication. Set `MENTIONSAPI_KEY` environment variable in your MCP client config.

## Key Capabilities

| Tool | Description |
|------|-------------|
| `search_mentions` | Search for brand mentions across AI platforms |
| `track_keywords` | Monitor specific keyword rankings in AI responses |
| `get_citations` | Retrieve citation data for your brand across platforms |
| `competitor_analysis` | Compare your AI visibility against competitors |

## Use Cases for Business Operators

### 1. GEO Monitoring Dashboard
Monitor how your brand appears in AI-generated answers. As AI search becomes the dominant discovery channel, this is the equivalent of 2010-era SEO rank tracking.

```
Agent prompt: "Check our MentionsAPI for 'CorpusIQ' mentions across all platforms this week"
```

### 2. Competitor AI Visibility
Track competitor AI citations to identify gaps in your own GEO strategy.

```
Agent prompt: "Show me competitor AI visibility scores and where they're being cited vs us"
```

### 3. Content Gap Analysis
Identify which queries send traffic to competitors but not you, then brief your content team.

### 4. Crisis Monitoring
Set up automated checks for negative brand mentions in AI responses.

## Integration with CorpusIQ

Pair MentionsAPI with CorpusIQ's analytics connectors (GA4, Search Console) for a complete picture:

1. **MentionsAPI** → tracks AI-platform visibility
2. **GA4** → tracks organic traffic from AI platforms
3. **Search Console** → tracks which queries trigger AI Overviews

Together they give you the full AI-visibility-to-conversion funnel.

## Pricing

Pay-as-you-go pricing with $1 free signup credit. No monthly minimums. Pricing scales with query volume.

---

*← [External MCP Catalog](/hermes/mcp/servers/external/) | [MCP Overview](/hermes/mcp/)*

*↑ [MCP Documentation](/hermes/mcp/)*
