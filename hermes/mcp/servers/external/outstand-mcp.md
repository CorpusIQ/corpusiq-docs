---
title: "Outstand MCP - CorpusIQ Docs"
description: "Setup and usage guide for Outstand MCP. Part of the Hermes resource directory. Category: Social Media Marketing."
last_updated: 2026-08-12
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/outstand-mcp/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# Outstand MCP

**Category:** Social Media / Marketing  
**Transport:** Remote Streamable HTTP  
**Auth:** TBD  
**Repository:** postproxy/postproxy-mcp (primary)  
**mcpservers.org:** https://mcpservers.org/servers/outstand-mcp  

## What It Does for Operators

Outstand MCP connects AI agents to social media platforms, enabling automated content publishing, engagement monitoring, and cross-platform social management. For business operators, this means AI agents can manage social presence across multiple platforms without manual intervention.

## Installation

```bash
# Via npx (if published)
npx -y @postproxy/postproxy-mcp
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "outstand": {
      "command": "npx",
      "args": ["-y", "@postproxy/postproxy-mcp"],
      "env": {
        "API_KEY": "your-api-key"
      }
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| Social media connect | Link AI agents to social accounts |
| Content publish | Cross-platform posting |
| Engagement monitor | Track replies, mentions, DMs |

## Operator Use Cases

1. **Automated social publishing** — Schedule and post content across X, LinkedIn, Bluesky from a single agent
2. **Engagement triage** — Monitor mentions across platforms and flag high-priority interactions
3. **Cross-platform analytics** — Aggregate social metrics into operator dashboards
4. **Brand monitoring** — Track brand mentions across social platforms
5. **Competitor social listening** — Monitor competitor social activity programmatically

## CorpusIQ Angle

Outstand MCP is a potential complementary tool for CorpusIQ's social media operations. It could serve as an alternative or supplement to Postiz for MCP-native agent workflows. Operators using CorpusIQ for business intelligence could pipe social engagement data directly into their analytics pipeline.

## Limitations

- New server, limited documentation
- Auth model unclear — may require per-platform OAuth
- Not yet widely adopted (new listing as of July 2026)
- Primary repo (postproxy-mcp) suggests proxy-based architecture — may have latency implications
