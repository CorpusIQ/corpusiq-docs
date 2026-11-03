---
title: "CorpusIQ Database Connectors - CorpusIQ Docs"
description: "SQL and NoSQL database connectors for CorpusIQ MCP. Query PostgreSQL, SQL Server, Azure Cosmos DB, and MongoDB through AI agents with read-only access."
category: mcp
tags: [corpusiq, mcp-connector]
last_updated: 2026-11-02
canonical: "https://www.corpusiq.io/docs/hermes/mcp/connectors/database/"
robots: "index,follow"

---

# CorpusIQ Database Connectors

## What It Is

CorpusIQ connects to operational databases, giving AI agents read-only query access. Agents can explore schemas, run SELECT-style queries, and analyze data for an answer without modifying the source system.

## Available Connectors

| Connector | Description |
|-----------|-------------|
| PostgreSQL connector | Direct SQL queries, table listing, schema inspection |
| Microsoft SQL Server connector | Direct SQL queries, table listing, schema inspection |
| Azure Cosmos DB connector | SQL queries, container listing, partition-aware queries |
| MongoDB connector | Document queries, collection listing |

## Quick Start

Add the connector through the [CorpusIQ dashboard](https://corpusiq.io/dashboard). Each connector authenticates with a connection string you control, set to a read-only database user.

## See Also

- [All Connectors](/hermes/mcp/connectors)
- [External MCP Servers](/hermes/mcp/servers/external)
- [CorpusIQ Docs](https://corpusiq.io/docs)
