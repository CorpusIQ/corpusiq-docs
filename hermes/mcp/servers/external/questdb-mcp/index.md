---
title: QuestDB MCP Server
description: Official QuestDB MCP — connects coding agents to a running QuestDB Web Console with tools for notebook cells, queries, and charts
category: Database
stars: n/a (official, new)
added: 2026-08-12
source: mcpservers.org
relevance: ★★
tags: [database, time-series, analytics, sql, questdb, stdio]
---

# QuestDB MCP Server

**Official MCP server from QuestDB** (`@questdb/mcp-server-questdb`, formerly `@questdb/mcp-bridge`). Connects coding agents (Claude Code, Codex, Cursor, OpenCode, Gemini CLI) to a running QuestDB Web Console: the agent gets tools to create notebook cells, run queries, and build charts. Every action executes in the browser against your already-established QuestDB session.

```
Server type: Local (stdio, npm)
Auth: Via your QuestDB Web Console session
Repo: https://github.com/questdb/mcp-server-questdb
Install: npx @questdb/mcp-server-questdb setup
Category: Database / Time-Series Analytics
```

## Why This Matters for Operators

QuestDB is one of the fastest time-series databases in the open-source ecosystem — used for market data, IoT telemetry, and event analytics. Its MCP bridge puts an agent inside the console you already run: ad-hoc queries become notebook cells, results become charts, all against your live session and permissions. No API keys to mint, no export pipeline to build — the agent works exactly where an analyst would.

## Tools & Capabilities

- **Notebook cells** — create and run cells in the QuestDB console
- **Queries** — execute SQL against your live database
- **Charts** — build visualizations from query results
- **Session-scoped** — executes in the browser against your established, authenticated QuestDB session
- **Version-pinned** — the wizard pins each agent config to the bridge version your console expects

## Installation

```bash
# Interactive wizard (recommended) — detects Claude Code, Codex, Cursor, OpenCode, Gemini CLI
npx @questdb/mcp-server-questdb setup
```

Or add manually to your MCP client config:

```json
{
  "mcpServers": {
    "questdb": {
      "command": "npx",
      "args": ["-y", "@questdb/mcp-server-questdb"]
    }
  }
}
```

If you're on an older console, run the matching version: `npx @questdb/mcp-server-questdb@<version> setup`. On an old `@questdb/mcp-bridge` install, run `npx @questdb/mcp-bridge upgrade` once to migrate configs.

## Configuration

Environment variables: `CONSOLE_ORIGIN` (your QuestDB Web Console URL) and `MCP_BRIDGE_PORT` can be overridden during setup or set directly. The wizard writes the pinned bridge version into each detected agent's config.

## Business Relevance

- **Data teams** get ad-hoc querying through an agent without exposing read/write database credentials — the agent inherits the console session
- **Analysts** can ask for a chart and get one, in the console the whole team already uses
- **Operators running QuestDB for market data or telemetry** get notebook-style exploration from any coding agent
- **Official + Apache-2.0** — vendor-maintained, audit-friendly

## Integration with CorpusIQ

QuestDB MCP covers the high-frequency, time-series end of the data spectrum where CorpusIQ's business-connector layer stops: CorpusIQ pulls structured business records (orders, invoices, ad spend), while QuestDB holds the event streams (sensor data, clickstreams, tick data). An agent can join the two views — operational records from CorpusIQ, time-series trends from QuestDB — to answer questions like "did the traffic spike convert into orders?" across both systems in one workflow.

## Limitations

- New package (0.3.0+ era); formerly published as `@questdb/mcp-bridge` — name migration may confuse old configs
- Requires a running QuestDB Web Console with an established session — not a standalone server
- Local stdio only — no hosted/remote endpoint
- Browser-session architecture means headless/CI usage depends on your console setup
- Tool surface is console-scoped: cells, queries, charts — not a general DB admin API

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
