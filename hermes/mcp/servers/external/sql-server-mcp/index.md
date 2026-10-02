---
title: "SQL Server MCP - Multi-Instance DBA Console"
description: "Self-hosted MCP server for DBAs and consultants running dozens of SQL Server instances. Grouped connections live in one config file with hot reload, every response names the server that answered, and beyond queries the agent reads execution plans, index layouts and stored-procedure source."
category: Database & Data Engineering
stars: n/a (new listing)
added: 2026-09-11
source: mcpservers.org /all via r.jina.ai
relevance: ★★
tags: [sql-server, dba, database, execution-plans, indexes, multi-instance, self-hosted]
---

# SQL Server MCP

**Self-hosted MCP server (stdio, npm package)** - one MCP entry for every SQL Server you administer. Connections live in a single config file grouped by client or environment, hot-reloaded without restarting the agent, and every response says which server answered. Built for DBAs and consultants managing dozens of instances rather than a single database.

```
Server type: Self-hosted (stdio)
Package: @cevelas/mcp-sqlserver (npm, v3.0.0)
Install: npx -y @cevelas/mcp-sqlserver
Repo: github.com/cvelasquez/mcp-sqlserver
Category: Database & Data Engineering
Built by: cvelasquez (GitHub)
```

## Tools

| Capability | Purpose |
|---|---|
| Grouped connections | Connections by client or environment in one config file, hot-reloaded without restarting the agent |
| Query execution | Run queries with every response naming the server that answered |
| Execution plans | Retrieve and read query execution plans |
| Index layouts | Inspect index structures across instances |
| Stored procedures | Read stored-procedure source from any managed instance |

## Connection

1. `npx -y @cevelas/mcp-sqlserver` from Claude Code, Cursor or any MCP client, or install the package locally.
2. Configure the connection groups in the server's config file (grouped by client or environment).
3. Ask "show me the execution plan for the slowest query on the production group" - the response names the instance and the plan.

## Verification (Sep 11, 2026 night sweep)

Not live-probed (stdio package, no public endpoint). The npm registry resolves @cevelas/mcp-sqlserver v3.0.0 with the published description "MCP server for DBAs running dozens of SQL Server instances: grouped connections, plans, indexes" and the GitHub repo cvelasquez/mcp-sqlserver. The author-level mcpservers.org slug 404s while the /all listing carries the full description.

## See Also

- [mnemiq MCP - Tunable Text-to-SQL for Business Databases](/hermes/mcp/servers/external/mnemiq-mcp)
- [Sqemo MCP - Database Schema Design and ERD Governance for Agents](/hermes/mcp/servers/external/sqemo-mcp)
