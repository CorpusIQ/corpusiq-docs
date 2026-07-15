---
title: "Snowflake MCP — Data Warehouse Queries for AI Agents"
description: "Connect AI agents to Snowflake data warehouse via MCP. Query, explore schemas, manage warehouses, and analyze enterprise data through natural language."
category: mcp
tags: [mcp-server]
last_updated: 2026-07-15
---

# Snowflake MCP — Data Warehouse Queries for AI Agents

## What It Is

Snowflake MCP exposes Snowflake data warehouse operations over the Model Context Protocol. AI agents can run SQL queries, explore database schemas, manage virtual warehouses, and analyze enterprise data — all RBAC-aware with the user's own Snowflake permissions.

## Tools Available

| Tool | Description |
|------|-------------|
| SQL query execution | Run read-only or read-write queries through the agent |
| Schema exploration | List databases, schemas, tables, views, and columns |
| Warehouse management | Start, stop, resize, and monitor virtual warehouses |
| Query history | Review past queries, execution times, and credits consumed |

## Quick Start

```bash
npx -y mcp-snowflake-server
```

## Business Use Cases

1. Ad-hoc analysis: "What were our top 10 customers by revenue last quarter?"
2. Schema discovery: "Show me all tables in the sales schema with column definitions"
3. Cost management: "Which queries consumed the most credits this week?"

## Limitations

- Snowflake account required. RBAC applies — agent can only access what the authenticated user can. Write operations need explicit enablement.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connector Catalog](/hermes/mcp/connectors/)
