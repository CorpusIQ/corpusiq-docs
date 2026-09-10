---
title: mnemiq MCP - Tunable Text-to-SQL for Business Databases
description: Open-source engine that answers natural-language questions over your own database with every pipeline stage - schema profiling, indexing, query generation, grounding - exposed as a setting you can read, change and measure.
category: Data & Analytics
stars: n/a (new listing)
added: 2026-09-09
source: mcpservers.org
relevance: ★★★
tags: [text-to-sql, business-intelligence, sql, database, analytics, self-hosted, open-source]
---

# mnemiq MCP

**Text-to-SQL you can tune to your database** (/NEM-ik/ - the m is silent) - an open-source engine that answers natural-language questions over your own database, built so that every stage between the question and the SQL is a setting you can read, change and measure. Run it on your own environment, on models you choose.

```
Server type: Self-hosted (open-source, Python via uv) - stdio or HTTP serve
Auth: None built in - runs inside your environment with your database credentials
Install: uv run mnemiq enrich / build / ask / serve --http
Endpoint: http://127.0.0.1:8080 when served over HTTP
License: Open source (github.com/agenticfabriq/mnemiq)
Built by: Agentic Fabriq
```

## Why This Matters for Operators

Generic BI tools answer canned questions; an LLM pointed at the raw database hallucinates table names. **mnemiq splits the difference honestly**: the pipeline - profile and describe the schema, index it for retrieval, generate grounded SQL, verify against the real database - is settings, not internals, and every answer shows the SQL it produced, the tables it read and how it grounded the response. Role-scoped queries (--roles analyst) mean the same engine answers finance questions and sales questions with the right guardrails. No accuracy number is claimed until it has been run on your database - which is exactly the right posture.

## Tools & Capabilities

| Command | Purpose |
|---|---|
| `mnemiq enrich` | Profile and describe your schema (~30s on a 4-table demo DB) |
| `mnemiq build` | Index the schema for retrieval (~2s) |
| `mnemiq ask "..."` | Natural-language query with the SQL, tables read and grounding shown in the answer |
| `mnemiq serve --http` | Serve the engine over HTTP at 127.0.0.1:8080 for MCP clients |
| roles (`--roles analyst`) | Role-scoped query access |

The engine exposes the major pipeline stages as settings - query mode (instant / deep / thinking), grounding sources and role policies are adjustable rather than hidden.

## Installation

```bash
git clone https://github.com/agenticfabriq/mnemiq.git
cd mnemiq
uv run python scripts/seed_demo.py      # optional demo database
uv run mnemiq enrich                    # profile + describe the schema
uv run mnemiq build                     # index it for retrieval
uv run mnemiq ask "how many customers are there by country?" --roles analyst
uv run mnemiq serve --http              # http://127.0.0.1:8080
```

## Configuration

Point your MCP client at the served HTTP endpoint (or run over stdio). Database credentials stay in your environment - the engine reads your schema and query results, and the grounding documents (docs/grounding.md) describe how answers are anchored to the database rather than to the model's memory.
