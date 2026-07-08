---
title: SIXTA Connect MCP Server Integration Guide
description: Zero-connection SQL analysis for PostgreSQL and MySQL — paste queries, get instant fixes from AI agents with SIXTA Connect MCP server
category: mcp
tags: [mcp, sixta, sql, database, postgresql, mysql, analysis, optimization, hermes-agent]
last_updated: 2026-07-08
---

# SIXTA Connect MCP — Zero-Connection SQL Analysis for Hermes Agent

DBRE-grade SQL analysis inside any MCP client. No connection strings, no install beyond the MCP server — just paste a query, EXPLAIN plan, migration, or error, and get named findings with severity, rationale, and ready-to-run fixes for PostgreSQL and MySQL.

## What It Does

SIXTA Connect brings database reliability engineering (DBRE) to AI agents without ever touching your production database:

- **SQL review** — Paste a query, get named findings (performance, anti-patterns, security)
- **EXPLAIN analysis** — Paste EXPLAIN output, get optimization recommendations
- **Migration review** — Paste schema migrations, get safety checks and improvement suggestions
- **Error diagnosis** — Paste a database error, get root cause analysis and fixes
- **Severity-ranked findings** — Each finding has severity, rationale, and ready-to-run fixes

## Quick Setup

### Prerequisites
- **No database credentials needed** — SIXTA works entirely on pasted content
- **No API key required** — Public service

### Add to Hermes Agent

```bash
# Streamable HTTP — connect and start analyzing
hermes mcp add sixta -- url https://sixta.dev/mcp
```

Or manual config:

```json
{
  "mcpServers": {
    "sixta": {
      "url": "https://sixta.dev/mcp",
      "transport": "streamable-http"
    }
  }
}
```

## Key Capabilities

| Tool | Description |
|------|-------------|
| `analyze_query` | Submit a SQL query for multi-faceted review — performance, anti-patterns, security |
| `analyze_explain` | Parse EXPLAIN/EXPLAIN ANALYZE output and surface optimization opportunities |
| `review_migration` | Check schema migrations for safety (locking, backfill, rollback) and best practices |
| `diagnose_error` | Diagnose PostgreSQL/MySQL errors with root cause analysis and fix suggestions |

## Use Cases for Business Operators

### 1. Pre-Production SQL Review
Before deploying a query to production, have your AI agent review it with SIXTA:

```
Agent prompt: "Review this query for performance issues. 
We run PostgreSQL 16 on RDS with 32GB RAM.
[ paste query ]"
```

### 2. Slow Query Optimization
When pg_stat_statements flags a slow query, paste the EXPLAIN output:

```
Agent prompt: "This query has gone from 50ms to 8s after our 
data volume doubled. Here's the EXPLAIN ANALYZE output. 
What should we change?"
```

### 3. Migration Safety Check
Before running a schema migration, get a safety review:

```
Agent prompt: "Review this migration for safety. We have 
12M rows in the users table and need zero downtime.
[ paste migration SQL ]"
```

### 4. Error Diagnosis
When your application logs a database error, diagnose it instantly:

```
Agent prompt: "Our app is throwing this PostgreSQL error. 
What's the root cause and how do we fix it?
ERROR: could not serialize access due to 
read/write dependencies among transactions"
```

## Integration with CorpusIQ

SIXTA Connect + CorpusIQ = complete database operations intelligence:

1. **CorpusIQ database connector** → query structure and schema from your actual PostgreSQL
2. **AI agent** → compose queries, review migration plans
3. **SIXTA Connect** → validate and optimize before execution

This gives operators a safe review layer between AI-generated SQL and production databases.

## Why Zero-Connection Matters

- **Security:** No credentials exposed to the MCP server — data never leaves your paste buffer
- **Compliance:** SOC 2 and GDPR friendly — the service sees only what you explicitly submit
- **Flexibility:** Works with any PostgreSQL/MySQL deployment (self-hosted, RDS, Cloud SQL, Aurora)
- **Speed:** No connection setup, no VPN configuration — paste and analyze instantly

## Pricing

Free public service. Check [sixta.dev](https://sixta.dev) for current status and any usage tiers.

---

*← [External MCP Catalog](/hermes/mcp/servers/external/) | [MCP Overview](/hermes/mcp/)*

*↑ [MCP Documentation](/hermes/mcp/)*
