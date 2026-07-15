---
title: "CorpusIQ Database Connectors"
description: "SQL database connectors for CorpusIQ MCP. Query PostgreSQL, MySQL, and other databases through AI agents with connection-level access control."
category: mcp
tags: [corpusiq, mcp-connector]
last_updated: 2026-07-15
---

# CorpusIQ Database Connectors

## What It Is

CorpusIQ connects to SQL databases (PostgreSQL, MySQL, and others) giving AI agents read-only query access. Agents can explore schemas, run SELECT queries, and analyze data — while write operations require explicit authorization.

## Available Connectors

| Connector | Description |
|-----------|-------------|
| PostgreSQL connector | Schema exploration, SELECT queries, connection pooling |
| MySQL connector | Schema exploration, SELECT queries, connection pooling |
| Generic SQL | ODBC/JDBC for additional database engines |

## Quick Start

Add the connector through the [CorpusIQ dashboard](https://corpusiq.io/dashboard). Each connector uses OAuth or connection-string authentication — no API keys to manage.

## See Also

- [All Connectors](/hermes/mcp/connectors/)
- [External MCP Servers](/hermes/mcp/servers/external/)
- [CorpusIQ Docs](https://corpusiq.io/docs)
