---
title: "Flash Props API MCP — Live Sports Betting Player Props Data"
description: "Flash Props API MCP server provides live sports betting player props data across NBA, MLB, NFL, NHL, NCAA, and soccer leagues. Unified format across all sports. Hosted remote server."
category: mcp
tags: [mcp-server, sports, betting, data, nba, nfl, mlb, nhl, ncaa, soccer]
last_updated: 2026-07-19
---

# Flash Props API MCP Server — Live Sports Props Data

Flash Props API is a hosted remote MCP server for live sports betting player props. It covers NBA, MLB, NFL, NHL, NCAA, and soccer in a unified format — one API for all major sports. Designed for agents that need real-time betting data without managing multiple sports-specific APIs.

**Source:** awesome-mcp-servers PR #9896 (discovered July 19, 2026)
**Category:** Sports / Data
**Author:** iFan6oy
**Repo:** https://github.com/iFan6oy/flash-props-api
**Status:** Active

## Why This Matters

Sports betting data is traditionally fragmented across league-specific APIs with different formats. Flash Props unifies them into a single MCP interface. For agents building betting models, arbitrage scanners, or sports analytics dashboards, this eliminates the integration tax of connecting to 6+ different data providers.

## Installation

```bash
# Remote MCP — no installation needed
# Connect directly via SSE endpoint:
# https://flash-props-api.example.com/sse
```

## Claude Desktop / Hermes Configuration

```json
{
  "mcpServers": {
    "flash-props": {
      "type": "sse",
      "url": "https://flash-props-api.example.com/sse",
      "env": {
        "FLASH_PROPS_API_KEY": "your-api-key"
      }
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `get_player_props` | Get current props for a specific player across sportsbooks |
| `list_games` | List today's games with available prop markets |
| `get_historical_props` | Retrieve historical prop lines and outcomes |
| `compare_books` | Compare prop lines across multiple sportsbooks |

## Supported Leagues

- NBA (National Basketball Association)
- MLB (Major League Baseball)
- NFL (National Football League)
- NHL (National Hockey League)
- NCAA (College Basketball & Football)
- Soccer (MLS, Premier League, Champions League)

## Authentication

Requires a Flash Props API key. Contact the author via the GitHub repo.

## CorpusIQ Relevance

Niche but high-value for operators in the sports betting and fantasy sports industries. Demonstrates the pattern of vertical-specific MCP data servers — a model CorpusIQ can replicate for e-commerce and DTC verticals.

## See Also

- [[sweeps/sweep-july19-2026]]
