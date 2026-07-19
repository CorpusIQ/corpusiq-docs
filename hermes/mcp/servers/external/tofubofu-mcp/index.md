---
title: "TofuBofu AI Visibility MCP — Integration Guide"
description: "Connect AI agents to TofuBofu for AI visibility scanning — measure how your brand appears across ChatGPT, Claude, Gemini, Perplexity, and Google AI Overviews."
category: mcp
tags: [mcp-server, ai-visibility, brand-monitoring, marketing, seo]
last_updated: 2026-07-18
---

# TofuBofu AI Visibility MCP — Integration Guide

**Source:** mcp.so listing (remote MCP server)  
**Author:** Arnav Neil / TofuBofu  
**Transport:** Remote MCP (Streamable HTTP)  
**Auth:** None required (free tier)  
**Website:** [tofubofu.com](https://tofubofu.com)

## What It Does

TofuBofu runs a free AI visibility scan for any B2B company, right inside your AI assistant. Ask it to scan a domain and it runs the questions real buyers ask across ChatGPT, Claude, Gemini, Perplexity, Google AI Overviews, and more — returning a concrete **Brand Visibility Score**, a share-of-voice breakdown, top coverage themes, source URLs, and a rank vs competitors.

Think of it as "SEO for AI platforms." As consumers shift from Google searches to asking AI assistants directly, knowing how your brand appears in AI responses becomes as critical as knowing your Google ranking.

The MCP server enables:
- **Marketing operators** to audit their AI brand presence in one conversation
- **Competitive intelligence** — see how competitors rank across AI platforms
- **Content strategy** — identify coverage gaps and themes for AI-optimized content
- **Zero-cost brand monitoring** — free tier, no API key, instant results

## Why This Matters for Operators

1. **AI is the new search:** ChatGPT alone has 400M+ weekly users. If your brand isn't visible when buyers ask AI assistants about your category, you're invisible to a growing segment of the market.

2. **First-mover advantage:** TofuBofu is the first MCP server for AI visibility measurement. Operators who adopt early get ahead of the curve while competitors are still optimizing for Google.

3. **Conversational workflow:** Instead of manually checking each AI platform, operators ask their AI assistant "scan our domain" and get a full report.

## Setup

### Prerequisites

- A B2B company domain to scan
- An MCP-compatible client (Claude, ChatGPT, Cursor, Hermes, etc.)

### MCP Client Configuration

Add this to your MCP client's server configuration:

```json
{
  "mcpServers": {
    "tofubofu": {
      "type": "http",
      "url": "https://api.tofubofu.com/mcp"
    }
  }
}
```

For Claude Code:
```bash
claude mcp add tofubofu https://api.tofubofu.com/mcp
```

For Hermes Agent (config.yaml):
```yaml
mcp_servers:
  tofubofu:
    transport: http
    url: https://api.tofubofu.com/mcp
```

### Usage

Once connected, ask your AI assistant:

- *"Scan corpusiq.io for AI visibility"*
- *"How does our brand appear on ChatGPT and Claude?"*
- *"Compare our AI visibility score vs our top 3 competitors"*
- *"What themes should we create content around for better AI visibility?"*

## Tools Available

Based on mcp.so listing data, TofuBofu provides:

| Tool | Description |
|------|-------------|
| `scan_domain` | Run a full AI visibility scan across ChatGPT, Claude, Gemini, Perplexity, Google AI Overviews |
| `brand_visibility_score` | Get the composite Brand Visibility Score (0-100) |
| `share_of_voice` | Platform-by-platform breakdown of brand mentions |
| `coverage_themes` | Top themes where your brand appears in AI responses |
| `competitor_rank` | Rank your brand vs competitors across AI platforms |
| `source_urls` | Source URLs backing each AI mention |

## Limitations

- **B2B-only:** Currently focused on B2B companies — consumer brands may get less useful results
- **English-first:** AI platform queries are in English; non-English brand presence may be underrepresented
- **Snapshot, not continuous:** Each scan is a point-in-time measurement, not ongoing monitoring (for continuous monitoring, pair with Octolens MCP)
- **New product:** TofuBofu appears to be an early-stage product — expect rapid iteration

## Complementary Tools

- **Octolens MCP:** Continuous brand mention monitoring across 15+ social/news platforms
- **Competitor Tracker & Co. MCP:** Weekly website change detection for competitive intelligence
- **CrustAPI MCP:** Live Google Search for traditional search visibility

---

*← [Back to External MCP Catalog](/hermes/mcp/servers/external/) | [Next: Competitor Tracker & Co.](/hermes/mcp/servers/external/competitor-tracker-mcp/) →*
