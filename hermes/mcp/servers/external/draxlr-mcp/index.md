---
title: "Draxlr MCP - SQL Dashboards and Queries for Agents"
description: "Remote MCP server that connects AI assistants to your SQL databases through Draxlr. Agents inspect schemas, run read-only SQL, work with saved queries and dashboards, and export results, with row-level security trimming every answer to the signed-in member's access."
category: Data & Analytics
stars: n/a (new listing)
added: 2026-09-11
source: mcp.so feed
relevance: ★★★
tags: [sql, dashboards, business-intelligence, analytics, read-only, remote-mcp]
---

# Draxlr MCP

**Remote MCP server (Streamable HTTP, OAuth)** - brings your Draxlr BI workspace into AI assistants. Draxlr connects to your SQL databases and runs the analytics layer; this MCP server exposes the connected databases, table schemas, saved queries and dashboards, so an agent can explore data, run read-only SQL, manage dashboards and export results under the same access rules as the Draxlr app.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (the client discovers it automatically)
Endpoint: https://api.draxlr.com/mcp
Capabilities: 6 documented groups (databases, queries, dashboards, widgets, exports, tenant awareness)
Databases: PostgreSQL, MySQL, MariaDB, PlanetScale, CockroachDB, YugabyteDB, SQL Server, Redshift, BigQuery, Supabase, ClickHouse, Databricks, Snowflake, Neon
Category: Data & Analytics
Built by: Draxlr
```

## What it does

| Capability | Detail |
|---|---|
| Inspect databases and schemas | List connected databases and inspect table schemas before querying |
| Run read-only SQL | The server writes and runs SQL against live data; write statements are refused, so exploration cannot change or delete anything |
| Saved queries | Create, update and run saved queries |
| Dashboards | List and read dashboards, and add queries to them as widgets |
| Exports | Export query results and dashboards to CSV or Excel |
| Row-level security | Every request runs with the exact access the signed-in member already has; two members can run the same query and get different rows, and dashboard-only members can read just their dashboards |

The vendor's listing describes these capability groups; exact tool names surface in the client on connect, since the endpoint is OAuth-gated and the live tool list is not publicly enumerable.

Row-level security makes the server practical for embedded, customer-facing analytics - paired with dashboard-only access, one shared dashboard becomes a per-customer view without exposing other rows or your underlying databases. The assistant signs in through Draxlr, never through your database credentials, so connection details never reach the AI or its model provider.

## Connection

1. Add the endpoint to any MCP client. Claude Code one-liner - `claude mcp add draxlr --transport http https://api.draxlr.com/mcp`
2. Authorize through the Draxlr OAuth flow when prompted.
3. Ask questions in plain English; the agent reads the schema, writes the correct SQL for your database, runs it read-only and hands the rows back.

## Verification (Sep 11, 2026 midday sweep)

Endpoint live-probed over JSON-RPC: anonymous initialize returned HTTP 401 with JSON-RPC error `-32001 "Authentication required"` - live and OAuth-gated as documented. The mcp.so listing carries the verified and featured badges, submitted by the Draxlr team, and the vendor's MCP feature page (draxlr.com/features/mcp-server) documents the endpoint, the read-only enforcement, the 14 supported database engines and the row-level security behavior.

## See Also

- [Sqemo MCP - Database Schema Design and ERD Governance for Agents](/hermes/mcp/servers/external/sqemo-mcp/)
- [SQL Server MCP - Multi-Instance DBA Console](/hermes/mcp/servers/external/sql-server-mcp/)
