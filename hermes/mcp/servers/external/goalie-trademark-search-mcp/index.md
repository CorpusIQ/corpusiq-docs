---
title: Goalie Trademark Search MCP Server
subtitle: 14M+ USPTO trademark records searchable from AI agents
source: mcp.so
github: https://github.com/goalie-mcp/goalie-trademark-search-mcp
created: 2026-07-23
category: IP/Legal
stars: 0
tags: [trademark, uspto, ip, legal, brand-protection, search]
---

# Goalie Trademark Search MCP Server

MCP server for searching **14M+ USPTO trademark records** directly from AI agents. Not a TSDR lookup — this is a dedicated trademark search tool optimized for agent workflows. Brand protection, competitive IP intelligence, and trademark clearance from any MCP-compatible client.

## What It Does

- **Trademark Search** — Query 14M+ USPTO records with keyword, owner, class, and status filters
- **Brand Clearance** — Check trademark availability before naming products
- **Competitive IP Intelligence** — Monitor competitor trademark filings
- **Portfolio Audit** — Review your own trademark portfolio status

## Business Operator Use Cases

| Use Case | Value |
|----------|-------|
| **Brand Clearance** | "Is 'QuantumFlow' trademarked in class 42?" → instant availability check |
| **Competitor Watch** | "Show me all new trademark filings by Stripe since January 2026" |
| **Portfolio Management** | "Which of our trademarks need renewal in the next 6 months?" |
| **Market Intelligence** | "What product categories is Notion expanding into based on recent filings?" |

## Installation

```bash
git clone https://github.com/goalie-mcp/goalie-trademark-search-mcp
cd goalie-trademark-search-mcp
npm install
```

## Configuration

Add to your MCP client config:

```json
{
  "mcpServers": {
    "goalie-trademark": {
      "command": "node",
      "args": ["path/to/goalie-trademark-search-mcp/index.js"]
    }
  }
}
```

## Tools Provided

- `search_trademarks` — Search 14M+ USPTO records with filters (keyword, owner, class, status, date range)
- `get_trademark` — Retrieve full record by serial number
- `check_availability` — Quick availability check for proposed marks

## Limitations

- **0 stars, brand new** — Created July 23, 2026. Unvetted.
- **USPTO only** — No international trademark databases (EUIPO, WIPO) yet.
- **Not TSDR** — This is a search tool, not the official USPTO Trademark Status & Document Retrieval system.
- **No legal advice** — Results are data, not legal opinions. Always consult trademark counsel.

## Operator Verdict

★★★ **High potential for DTC/e-commerce operators.** Trademark search is a recurring pain point for any business launching new products. Having it available from your AI agent eliminates the USPTO portal friction. Watch for international expansion and legal disclaimers before production use.
