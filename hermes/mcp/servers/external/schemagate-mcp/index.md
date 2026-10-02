---
title: "schemagate MCP - Identity-Scoped Schema Selection"
description: "Open-source MCP server and Python library that selects the handful of tables an NL2SQL model actually needs and hides every table the caller is not allowed to read. Identity is applied before the model sees the schema, cutting prompt tokens 65-76 percent with Apache-2.0 licensing."
category: Database & Data Engineering
stars: n/a (new listing)
added: 2026-09-11
source: mcpservers.org /all via r.jina.ai
relevance: ★★
tags: [text-to-sql, schema-selection, access-control, database, postgresql, security, self-hosted]
---

# schemagate MCP

**Self-hosted MCP server (stdio or Streamable HTTP, Python)** - an identity-scoped schema gate for text-to-SQL. Before any SQL is written, schemagate picks the handful of tables the question needs and drops every table the caller's role cannot read - not ranked lower, absent. Same question, same person, with the payroll role the hr_compensation table appears; without it, it is gone from the prompt.

```
Server type: Self-hosted (stdio or Streamable HTTP)
Auth: Caller identity via --principal plus role
Package: schemagate (PyPI, Apache-2.0)
Install: pip install 'schemagate[mcp]'
Run: python -m schemagate.mcp_server (stdio) or SCHEMAGATE_MCP_TRANSPORT=streamable-http
DB drivers: postgres, oracle, mssql, mysql extras
Category: Database & Data Engineering
Built by: ashishsinha1602
```

## Tools

| Capability | Purpose |
|---|---|
| select (CLI/library) | Given a natural-language question, principal and role, return only the permitted, relevant tables and their DDL |
| catalog.json restrict | Declarative per-principal or per-role table restrictions |
| describe | Optional human-written table descriptions folded into the catalog |
| MCP server | The same selection logic exposed over stdio or Streamable HTTP for Cursor, Windsurf, Zed and other clients |
| studio | Local web page to type questions, switch roles and watch what reaches the prompt |

## Connection

1. `pip install 'schemagate[mcp]'` plus a driver extra (`schemagate[postgres]`, `[oracle]`, `[mssql]` or `[mysql]`).
2. Run the server: SCHEMAGATE_DATABASE_URL=postgresql://localhost/app python -m schemagate.mcp_server, or switch to streamable-http transport for a team endpoint.
3. Point the MCP client at the stdio command (python -m schemagate.mcp_server) and ask questions; caller roles flow in per request.

Measured on its bundled benchmark schemas the selector cuts prompt payloads 65-76 percent (Commerce 42 objects: 2,483 tokens down to 604) and the selector itself runs offline with no model call. A Vanna migration note ships for teams moving from run-time identity to schema-time identity.

## Verification (Sep 11, 2026 night sweep)

Not live-probed (self-hosted package). The PyPI package resolves; the README documents the MCP entry point, stdio and streamable-http transports, per-driver extras and the catalog config format. GitHub Actions CI badge green on the listing, and the author publishes a 1,789-case parity test between the JS demo selector and the Python library.

## See Also

- [mnemiq MCP - Tunable Text-to-SQL for Business Databases](/hermes/mcp/servers/external/mnemiq-mcp)
- [Sqemo MCP - Database Schema Design and ERD Governance for Agents](/hermes/mcp/servers/external/sqemo-mcp)
