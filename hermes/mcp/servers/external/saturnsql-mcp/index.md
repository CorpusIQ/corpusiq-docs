---
title: "SaturnSQL MCP - Ask Your Database from Any Agent"
description: "Hosted database MCP for Claude, ChatGPT and Cursor: schema reads and row-limited SQL against your live connections, read-only by default."
category: Database & Data Engineering
stars: n/a (new listing)
added: 2026-10-08
source: "mcpservers.org /all (October 8, 2026 evening sweep)"
relevance: ★★★
tags: [database, sql, postgresql, mysql, bigquery, analytics, data-access, read-only, remote-mcp]
---

# SaturnSQL MCP

**Hosted MCP server that answers questions from your live database** - paste one URL, sign in, and your assistant reads schemas and runs row-limited SQL against the connections you already have in SaturnSQL. No local process, no connection string pasted into a config file.

```
Server type: Remote (Streamable HTTP at mcp.saturnsql.com/mcp)
Auth: OAuth sign-in with your SaturnSQL account, or a named API key for clients without OAuth
Tools: 6 - list_connections, get_schema, execute_query, run_saved_query, save_query, export_query_results
Engines: PostgreSQL, MySQL, Oracle, BigQuery, SQL Server, Redshift, ClickHouse, DynamoDB
Safety: read-only by default (single SELECT, WITH or EXPLAIN), row-limited execution, billing/users/settings rejected
Plan: Starter and up
Category: Database & Data Engineering
Built by: Panda Capital Oy Ab (saturnsql.com)
```

## Why This Matters for Operators

"How many customers have this feature enabled?" usually ends with someone exporting a CSV or filing a ticket to an analyst. This server makes the live database answer the question directly inside Claude, ChatGPT or Cursor, and it keeps the guardrails the team already configured: connections default to read-only, queries are row-limited, and the shared query library means an answer the AI saves is one the whole team can reuse.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `list_connections` | See which databases are available |
| `get_schema` | Read tables, columns and foreign keys |
| `execute_query` | Run row-limited SQL |
| `run_saved_query` | Run a query from the team's library |
| `save_query` | Write a result back to the team's library |
| `export_query_results` | Export a result to CSV |

## Installation

```bash
claude mcp add --transport http saturnsql https://mcp.saturnsql.com/mcp
```

```json
{
  "mcpServers": {
    "saturnsql": { "type": "http", "url": "https://mcp.saturnsql.com/mcp" }
  }
}
```

Setup takes about two minutes: connect the database in SaturnSQL, paste `mcp.saturnsql.com/mcp` into Claude, ChatGPT, Cursor or Claude Code, and approve access with your account. Claude and ChatGPT connect through their custom-connector flows; Cursor takes the URL in `mcp.json`.

## Configuration and Safety

- New connections default to read-only mode: every query must be a single SELECT, WITH or EXPLAIN statement, and results are row-limited by the same validated execution the SaturnSQL editor uses.
- Billing, users and account settings are rejected outright through the MCP surface.
- Queries your AI client saves join the team's shared library; queries the team saved are ones it can run.
- No local process and no connection string in a config file - access rides your SaturnSQL account, and the install checks the plan (Starter and up).

## Example Prompts

- "How many workspaces have Slack scheduling turned on, by plan?"
- "Which tables join to the orders table, and what does the schema say about statuses?"
- "Run the churn-report query from our library and summarize the last 30 days."
- "Export the top 100 accounts by MRR change to CSV."

## Integration with CorpusIQ

SaturnSQL reaches the data your product runs on; CorpusIQ reaches the systems your business runs on. Ask for the usage question from the database and the revenue, customers and pipeline picture from Stripe, Shopify or QuickBooks in the same conversation - product data and business data, one chat, every number sourced from the system that owns it.

## Limitations

- Requires a SaturnSQL account on the Starter plan or higher.
- Six tools and SQL access, not a BI builder - charts and dashboards stay in your existing tools.
- Read-only by default: writes depend on a connection created with write access in SaturnSQL.
- The MCP server is the reverse of SaturnSQL's built-in AI SQL editor (the editor puts AI inside SaturnSQL; this puts SaturnSQL inside your MCP client). Both hit the same data.

## FAQ

### Does it run queries automatically?

Your client decides when to call the tools, and most clients ask before a tool call. Queries are row-limited, and on a read-only connection every query must be a single SELECT, WITH or EXPLAIN statement.

### Which engines does it support?

PostgreSQL, MySQL, Oracle, BigQuery, SQL Server, Redshift and ClickHouse have dedicated setup pages, and DynamoDB connects the same way.

### Is this different from the built-in AI SQL editor?

Yes - the editor is AI inside SaturnSQL's own app; the MCP server puts SaturnSQL's database access inside Claude, ChatGPT, Cursor or Claude Code. Use whichever fits where you work; both hit the same connections.

## See Also

- [QuestDB MCP Server](/hermes/mcp/servers/external/questdb-mcp/)
- [SQL Server MCP - Multi-Instance DBA Console](/hermes/mcp/servers/external/sql-server-mcp/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
