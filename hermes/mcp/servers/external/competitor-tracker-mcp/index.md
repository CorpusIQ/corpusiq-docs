---
title: "Competitor Tracker & Co. MCP — Integration Guide"
description: "Connect AI agents to Competitor Tracker & Co. for automated competitor website monitoring. Weekly crawls, change detection, and ranked changelogs directly in your AI workflows."
category: mcp
tags: [mcp-server, competitive-intelligence, competitor-monitoring, marketing, product-management]
last_updated: 2026-07-18
---

# Competitor Tracker & Co. MCP — Integration Guide

**Source:** mcp.so listing  
**Author:** Slobodan Stojanović (founder, Vacation Tracker — 35K+ users)  
**Transport:** Local stdio (MCP server)  
**Auth:** API key (Competitor Tracker & Co. account required)  
**Website:** [competitortracker.co](https://competitortracker.co)

## What It Does

Competitor Tracker & Co. watches your competitors' websites and tells you what changed. Every week it crawls their pricing, product, messaging, and corporate pages, detects the changes that matter, and files a tagged, ranked changelog.

The MCP server brings this competitive intelligence directly into your AI agent's conversation — instead of checking a dashboard, you ask your assistant "what changed with our competitors this week?"

The MCP server enables:
- **Product managers** to track competitor feature launches and pricing changes without manual monitoring
- **Marketing operators** to spot messaging pivots and positioning shifts instantly
- **Founders/CEOs** to maintain competitive awareness as a conversational habit, not a calendar task
- **Sales teams** to prepare competitive battle cards with fresh intelligence

## Why This Matters for Operators

1. **Competitive intelligence becomes a conversation:** Instead of a separate dashboard login, operators fold competitor tracking into their daily AI workflow.

2. **Structured, not noisy:** The tool detects, tags, and ranks changes — operators don't wade through raw crawls looking for signal.

3. **Proven founder:** Slobodan Stojanović built Vacation Tracker to 35K+ users. This is a founder who understands operator workflows.

4. **Weekly cadence:** Weekly rather than real-time monitoring reduces noise and matches the rhythm of strategic decision-making.

## Setup

### Prerequisites

- A Competitor Tracker & Co. account at [competitortracker.co](https://competitortracker.co)
- Competitor URLs configured in your dashboard
- Node.js 18+ (for local stdio server)

### Installation

The MCP server is likely distributed as an npm package. Install locally:

```bash
npm install -g @competitortracker/mcp-server
```

Or run directly with npx:

```bash
npx @competitortracker/mcp-server
```

### MCP Client Configuration

Add this to your MCP client's server configuration:

```json
{
  "mcpServers": {
    "competitor-tracker": {
      "command": "npx",
      "args": ["-y", "@competitortracker/mcp-server"],
      "env": {
        "CT_API_KEY": "your-api-key"
      }
    }
  }
}
```

For Claude Code:
```bash
claude mcp add competitor-tracker -- npx -y @competitortracker/mcp-server
```

For Hermes Agent (config.yaml):
```yaml
mcp_servers:
  competitor-tracker:
    transport: stdio
    command: npx
    args: ["-y", "@competitortracker/mcp-server"]
    env:
      CT_API_KEY: "${CT_API_KEY}"
```

### Usage

Once connected, ask your AI assistant:

- *"What changed with our competitors this week?"*
- *"Show me any pricing changes from [competitor] in the last month"*
- *"Compare our product messaging against our top 3 competitors"*
- *"Which competitor made the most significant product changes this quarter?"*
- *"Summarize the top 5 competitive moves I should be aware of"*

## Tools Available

Based on mcp.so listing data, Competitor Tracker & Co. provides:

| Tool | Description |
|------|-------------|
| `get_changelog` | Get the latest weekly changelog for all tracked competitors |
| `get_competitor_changes` | Get changes for a specific competitor within a date range |
| `get_pricing_changes` | Filter changelog to pricing-related changes only |
| `get_product_changes` | Filter changelog to product/feature changes only |
| `get_messaging_changes` | Filter changelog to messaging/positioning changes |
| `compare_competitors` | Side-by-side comparison of recent changes across competitors |
| `list_tracked_competitors` | List all competitors currently being tracked |

## Limitations

- **Website-only:** Tracks public website changes, not private product betas or internal strategy
- **Weekly cadence:** Not real-time — changes appear in the next weekly crawl
- **Page-level detection:** May miss subtle copy changes if the page structure is complex
- **Paid product:** Competitor Tracker & Co. is a commercial product (pricing TBD)

## Complementary Tools

- **Octolens MCP:** Real-time brand monitoring across 15+ social/news platforms for competitor mentions
- **TofuBofu AI Visibility MCP:** Measure competitor presence across AI platforms (ChatGPT, Claude, Gemini)
- **CrustAPI MCP:** Live Google Search for ad-hoc competitive research

---

*← [Back to External MCP Catalog](/hermes/mcp/servers/external/) | [Previous: TofuBofu AI Visibility](/hermes/mcp/servers/external/tofubofu-mcp/) →*
