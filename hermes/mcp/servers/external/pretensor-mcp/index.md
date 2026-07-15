---
title: "Pretensor MCP — Knowledge Graphs from Database Introspection"
description: "Integration guide for pretensor-ai/pretensor. Kuzu-backed schema graph from live DB introspection with MCP tools for AI retrieval."
category: mcp
tags: [mcp-server, knowledge-graph, database, schema, business-intelligence, hermes-agent]
last_updated: 2026-07-15
mcp_server: pretensor-ai/pretensor
stars: 5
source: mcpservers.org
---

# Pretensor MCP — Knowledge Graphs from Database Introspection

**Repository:** [pretensor-ai/pretensor](https://github.com/pretensor-ai/pretensor)
**Stars:** 5 ★ (early stage)
**Category:** Database / Business Intelligence
**License:** Unknown
**Last Updated:** 2026-07-13

## What It Does

Pretensor introspects live databases and builds a Kuzu-backed knowledge graph representing the schema, table relationships, and data architecture. AI agents can then query this graph via MCP tools to understand data models, discover connections, and retrieve precomputed context without running raw SQL against production databases.

### Tools Provided

| Tool | Description |
|------|-------------|
| `introspect_database` | Scan a database and build/refresh the knowledge graph |
| `query_schema` | Query the knowledge graph for table/column/relationship info |
| `find_relationships` | Discover foreign key and logical relationships between tables |
| `get_table_context` | Get full context for a table: columns, types, relationships, row counts |
| `search_columns` | Search for columns by name across all tables |
| `generate_erd` | Generate entity-relationship diagram from graph |
| `export_graph` | Export knowledge graph as JSON/Cypher for external tools |

## Why This Matters for Business Operators

Most business operators have no documentation for their database schemas. Pretensor solves the "what data do we actually have" problem — it reads the database, builds a graph, and lets AI agents answer questions like:

- "Which tables have customer email addresses?"
- "What's the relationship between orders and subscriptions?"
- "Which columns are never queried? (candidate for archival)"
- "Map our Stripe schema to our internal accounting tables"

This transforms database exploration from a SQL-heavy manual process into a conversational interaction.

## Setup for Hermes Agent

### Prerequisites

- Python 3.10+
- Access credentials for target databases (PostgreSQL, MySQL, SQLite supported)
- KuzuDB (bundled with pretensor)

### Step 1: Clone and Install

```bash
cd ~/mcp-servers
git clone https://github.com/pretensor-ai/pretensor.git
cd pretensor
pip install -r requirements.txt
```

### Step 2: Configure Database Connection

Create `~/.pretensor/config.yaml`:

```yaml
databases:
  production:
    type: postgresql
    host: localhost
    port: 5432
    database: corpusiq_production
    user: pretensor_readonly
    password: ${DB_PASSWORD}
  analytics:
    type: postgresql
    host: analytics-db.internal
    port: 5432
    database: corpusiq_analytics
    user: pretensor_readonly
    password: ${ANALYTICS_DB_PASSWORD}

graph:
  storage: ~/.pretensor/graphs/
  auto_refresh_hours: 24
```

**Security note:** Use a read-only database user. Pretensor only needs schema introspection privileges.

### Step 3: Build Initial Graph

```bash
python -m pretensor build --database production
# Output: Graph built: 47 tables, 128 relationships, 892 columns
```

### Step 4: Register with Hermes

```bash
hermes mcp add pretensor -- python -m pretensor.mcp_server
```

Or via `~/.hermes/config.yaml`:

```yaml
mcp_servers:
  pretensor:
    command: python
    args:
      - -m
      - pretensor.mcp_server
    env:
      PRETENSOR_CONFIG: /home/hermes/.pretensor/config.yaml
```

### Step 5: Verify

```bash
hermes mcp list | grep pretensor
```

## Use Cases

1. **AI-assisted schema exploration:** "Show me all tables related to billing" → graph query
2. **Data lineage tracking:** "Where does the `customer_lifetime_value` field come from?"
3. **Cross-database mapping:** "How does our Stripe schema map to our internal orders table?"
4. **Onboarding acceleration:** New developers/analysts query the graph instead of reading SQL files
5. **Technical debt discovery:** Find orphaned tables, unused columns, redundant indexes

## Comparison: CorpusIQ DB Connector vs Pretensor

| Feature | CorpusIQ DB Connector | Pretensor MCP |
|---------|----------------------|---------------|
| **Purpose** | Run SQL queries | Schema understanding |
| **Output** | Query results | Knowledge graph |
| **Use case** | Data retrieval, reporting | Schema exploration, documentation |
| **Security** | Read-only SQL execution | Schema-only introspection |
| **Complementary?** | Yes — they solve different problems | |

**Verdict:** Pretensor is complementary. Use CorpusIQ DB Connector for running queries; use Pretensor to understand what to query. Together they give agents both the map and the ability to navigate.

## Limitations

- Early stage (5★) — expect rough edges and limited DB support
- Read-only schema introspection — cannot modify schemas
- Large schemas (1000+ tables) may have slow initial graph builds
- No support for NoSQL databases (MongoDB, DynamoDB)
- KuzuDB dependency — adds complexity vs. pure-Python solutions
- No query result caching — repeated queries hit the graph, not the DB

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `Connection refused` | Verify DB is accessible from Hermes host; check firewall rules |
| `Permission denied` | Use a read-only DB user; Pretensor only needs `INFORMATION_SCHEMA` access |
| `Graph build timeout` | For large schemas, increase `GRAPH_BUILD_TIMEOUT` env var |
| `KuzuDB error` | Clear graph storage: `rm -rf ~/.pretensor/graphs/*` and rebuild |

## Related Guides

- [CorpusIQ Database Connector](/hermes/mcp/connectors/database/) — SQL query execution
- [SPM Structured Project Memory](/hermes/mcp/servers/external/spm-structured-project-memory/) — Project-level memory graphs
- [Coding Agent PM MCP](/hermes/mcp/servers/external/coding-agent-pm-mcp/) — Project management via MCP
