---
title: "Data Studio Agent MCP — 70+ SQL & NoSQL databases for AI"
description: "Connect 70+ SQL databases (PostgreSQL, MySQL, SQL Server, ClickHouse, Snowflake, BigQuery) and NoSQL (Elasticsearch, MongoDB, DynamoDB) to AI agents via"
category: mcp
tags: [mcp-server, database, sql, nosql, postgresql, mysql, mongodb, elasticsearch, data-platform]
source: mcp.so
discovered: 2026-08-11
stars: 3
author: Geek Fun (Blankll)
github: https://github.com/geek-fun/data-studio-agent
mcp_endpoint: localhost (bridges via SqlKit + DocKit desktop apps)
transport: stdio (local)
auth: None (local-first, credentials never leave your machine)
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/data-studio-agent-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"

---

# Data Studio Agent MCP Server

**Let your AI coding agent securely access all your databases, in plain language.** Data Studio Agent is an open-source MCP server that gives AI agents direct, read-safe access to 70+ SQL databases (via SqlKit) and NoSQL stores (via DocKit) — local-first, enterprise-grade security, credentials never leave your machine.

## Why It Matters for Operators

For business operators managing data across multiple database systems, switching between SQL clients, dashboards, and schema explorers is the daily reality. Data Studio Agent collapses this into a single conversational interface:

- *"Show me the schema for our production PostgreSQL database"*
- *"What are the top 10 customers by revenue in the last quarter?"*
- *"Compare the user count in MongoDB last month vs this month"*
- *"Find all Elasticsearch indices with more than 1M documents"*
- *"Which tables in Snowflake haven't been queried in 30 days?"*

This is direct database interrogation from natural language — no SQL writing, no context-switching between tools, no exporting data to a separate analysis environment.

## Technical Details

| Field | Value |
|-------|-------|
| **Transport** | stdio (local process) — routes to SqlKit + DocKit bridges over localhost |
| **Auth** | None (local-first — credentials stay in SqlKit/DocKit desktop apps, never exposed to the MCP server) |
| **Install** | `npm install -g @geek-fun/data-studio-mcp` |
| **SQL databases** | 70+ via SqlKit: PostgreSQL, MySQL, SQL Server, Oracle, SQLite, DuckDB, ClickHouse, Snowflake, BigQuery, and more |
| **NoSQL databases** | Elasticsearch, OpenSearch, MongoDB, DynamoDB via DocKit |
| **Access model** | Read-only by default — write operations must be explicitly enabled |
| **Security** | Database drivers, SSH tunnels, and connection management live in desktop apps; MCP server only bridges to `127.0.0.1` |
| **Clients** | Claude Code, Cursor, Windsurf, OpenCode, Codex, Cline, Pi, Qoder, GitHub Copilot, any MCP client |
| **License** | Apache 2.0 |
| **Tools** | 79 tools across SQL + NoSQL backends |

## Setup

### Prerequisites

1. Install [SqlKit](https://github.com/geek-fun/sqlkit) (for SQL databases)
2. Install [DocKit](https://github.com/geek-fun/dockit) (for NoSQL databases)
3. Configure your database connections in each desktop app

### Install the MCP Server

```bash
npm install -g @geek-fun/data-studio-mcp
```

### Claude Desktop / Claude Code

```json
{
  "mcpServers": {
    "data-studio": {
      "command": "npx",
      "args": ["-y", "@geek-fun/data-studio-mcp"]
    }
  }
}
```

### Cursor / VS Code

```json
{
  "mcpServers": {
    "data-studio": {
      "command": "npx",
      "args": ["-y", "@geek-fun/data-studio-mcp"]
    }
  }
}
```

The MCP server auto-discovers running SqlKit and DocKit backends via port files — no additional configuration needed once the desktop apps are running with your connections configured.

## Architecture

```
AI Agent (Claude/Cursor/Codex)
    │
    ▼
Data Studio MCP Server (thin routing layer)
    │
    ├──► SqlKit bridge (127.0.0.1) ──► 70+ SQL databases
    │
    └──► DocKit bridge (127.0.0.1) ──► Elasticsearch, MongoDB, DynamoDB, OpenSearch
```

The MCP server is a thin routing layer. All database drivers, SSH tunnels, and connection management live in the desktop apps. Credentials never pass through the MCP server — they stay in SqlKit/DocKit where you configured them.

## For Business Operators

Data Studio Agent fills a critical operational gap: the distance between "I have a question about my data" and "I have the answer." Instead of finding the right SQL client, remembering connection strings, writing and debugging queries, and formatting results — you ask in plain language and get answers immediately.

**Security model:** Read-only by default is the right default for business operators. You can safely give AI agents database access knowing they can't modify data unless you explicitly enable write operations. Combined with local-first architecture (credentials never leave your machine), this is enterprise-ready from day one.

**Competitive context:** This is one of the broadest database coverage MCP servers available — 70+ SQL dialects plus the major NoSQL stores. For operators managing heterogeneous data environments, it eliminates the need for separate connectors for each database type.

---

*Open source (Apache 2.0). Built by [Geek Fun](https://www.geekfun.club/products/data-studio-agent/). npm: [@geek-fun/data-studio-mcp](https://www.npmjs.com/package/@geek-fun/data-studio-mcp)*
