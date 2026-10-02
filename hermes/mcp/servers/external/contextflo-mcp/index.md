---
title: "Contextflo MCP - Governed Team Data Queries for Agents"
description: "Governed context layer from Contextflo: connect BigQuery, Snowflake, Postgres, Redshift, Databricks or ClickHouse (or upload a CSV) and let the whole team ask questions of live data and build auto-refreshing dashboards in chat, with table-level access control. Endpoint mcp.contextflo.com/mcp, live-verified."
category: Data & Analytics
stars: "n/a (hosted, no public MCP repo; org github.com/contextflo)"
added: 2026-08-30
source: "mcp.so feed (listed Jul 9, 2026; first evaluated Aug 30)"
relevance: ★★
tags: [mcp-server, analytics, bi, snowflake, bigquery, postgres, dashboards, governance]
---

# Contextflo MCP

**A governed context layer for team analytics in chat.** Contextflo connects your data warehouse to the AI tools your team already uses: hook up BigQuery, Snowflake, Postgres, Redshift, Databricks or ClickHouse (or upload a CSV), then ask questions of the real data and build live, auto-refreshing dashboards by chatting with Claude or ChatGPT over MCP. Table-level access control keeps agent access scoped.

```
Server type: Hosted (Streamable HTTP)
Endpoint: https://mcp.contextflo.com/mcp (anonymous initialize returns 401 Authentication required - live)
Auth: Contextflo account sign-in (OAuth flow; see the MCP client guides)
Sources: BigQuery, Snowflake, Postgres, Redshift, Databricks, ClickHouse, CSV upload
Access control: table-level permissions
Outputs: chat answers, live auto-refreshing dashboards
Docs: contextflo.com/docs (MCP client guides for Claude and ChatGPT)
Built by: Contextflo (contextflo.com)
```

## Why This Matters for Operators

Self-serve analytics has been stuck between "give everyone a BI tool nobody logs into" and "answer every question in SQL yourself". Contextflo's MCP picks a third lane.

First, **questions in chat, against real data.** The agent queries the connected sources directly - "what was last week's churn by plan tier" - instead of waiting for a dashboard request to land in the data team's queue.

Second, **governance is built in, not bolted on.** Table-level access control means the whole team can query without handing the agent a warehouse superuser. That is the difference between a demo and something you can actually roll out.

Third, **dashboards become a chat product.** Per the vendor's blog, live auto-refreshing dashboards get built by chatting - no Tableau, no drag and drop - and stay connected to the sources.

## Tools and Capabilities

Capability-level table from the vendor's docs; exact tool names require sign-in - the endpoint refuses anonymous enumeration (initialize returns a JSON-RPC 401 "Authentication required", which confirms liveness).

| Capability | Description |
|-----------|-------------|
| Ask data questions | Natural-language queries against connected warehouses and CSV uploads |
| Build dashboards | Live, auto-refreshing dashboards generated from chat, connected to the sources |
| Schema and table discovery | Work with the real table and schema names of your sources |
| Permission-scoped execution | Queries run against the table-level permissions granted to the workspace |

## Verification (Aug 30, 2026)

- Endpoint live-verified: anonymous initialize at mcp.contextflo.com/mcp returns JSON-RPC error -32001 "Authentication required" (liveness with sign-in auth, same class as the Taskfolk and Jitsu verifications)
- Vendor docs: contextflo.com/docs carries MCP client pages for Claude and ChatGPT naming the endpoint
- mcp.so listing (Jul 9, 2026) and vendor blog confirm the product surface; GitHub org exists with 0-star repos and no public MCP repo

## Notes and Caveats

- Hosted only: no self-host or stdio variant
- Young vendor: no public MCP repo, all public org repos are 0-star; treat as early adopter
- Sign-in required for everything past the endpoint check
- Warehouse credentials and table grants live in the Contextflo workspace - review their security model before connecting production data

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Sequel MCP - Google Search Console in Natural Language](/hermes/mcp/servers/external/sequel-mcp)
- [Data Studio Agent MCP - 70+ SQL & NoSQL databases for AI](/hermes/mcp/servers/external/data-studio-agent-mcp)
