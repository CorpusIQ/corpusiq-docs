---
title: "datamcp — Hosted MCP Gateway for PostgreSQL, MySQL & OpenAPI"
description: "Hosted MCP gateway that connects AI agents to PostgreSQL, MySQL, and OpenAPI endpoints. Server-side credentials, scoped access links, zero local setup."
source: datamcp.app
stars: 0
language: N/A (Hosted)
transport: Streamable HTTP
auth: API Key / scoped links
category: Database & Data Engineering
last_updated: 2026-07-21
---

# datamcp — Hosted MCP Gateway for Databases & APIs

**Database and API MCP gateway.** datamcp lets AI agents query PostgreSQL, MySQL, and any OpenAPI endpoint through a single hosted MCP server. Server-side credential management means no local database config. Generate scoped access links for team members.

## What It Does for Operators

- **PostgreSQL + MySQL MCP** — Query production databases through AI agents with server-side credentials
- **OpenAPI gateway** — Connect any REST API to your MCP client through datamcp's proxy
- **Scoped access links** — Generate read-only or table-specific links for different team members
- **Zero local setup** — No local database drivers, VPNs, or SSH tunnels. All connections managed server-side.
- **Audit trail** — Track which agent queried what, when.

## Installation

```bash
# No installation — hosted platform
# Sign up at datamcp.app, connect your databases
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "datamcp": {
      "type": "url",
      "url": "https://datamcp.app/docs"
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `query_postgres` | Execute read-only SQL queries on connected PostgreSQL databases |
| `query_mysql` | Execute read-only SQL queries on connected MySQL databases |
| `call_openapi` | Make requests to configured OpenAPI endpoints |
| `list_tables` | Discover database schema and table structures |
| `generate_link` | Create scoped access links for team members |

*Note: Tool names are approximate. Full documentation at datamcp.app/docs.*

## Operator Use Cases

1. **Data Analysts** — "What were our top 10 products by revenue last month?" → query directly from AI agent
2. **Engineering Teams** — Give AI agents read-only production database access for debugging
3. **Business Operators** — Connect Stripe/Shopify OpenAPI endpoints through datamcp for unified querying
4. **Agencies** — Generate scoped database access links for client reporting without sharing credentials

## CorpusIQ Angle

datamcp is complementary to CorpusIQ for operators who need direct database access. While CorpusIQ provides 36+ pre-built business connectors (QuickBooks, Shopify, HubSpot), datamcp gives operators the ability to connect custom databases and APIs that CorpusIQ doesn't natively support. Together: CorpusIQ for turnkey business data + datamcp for custom database/API access.

## Limitations

- Requires datamcp.app account and database connection setup
- Read-only queries (no write operations through MCP)
- Query performance depends on datamcp's proxy infrastructure
- New platform — uptime and reliability TBD
