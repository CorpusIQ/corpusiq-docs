---
title: Sqemo MCP - Database Schema Design and ERD Governance
description: MCP server for governed database design - introspect live databases, generate ERDs, name-check columns, detect schema drift, diff models and export SQL or DBML. Local .erd.json files work with no account. MIT.
category: Database & Data Engineering
stars: n/a (new listing)
added: 2026-09-09
source: mcpservers.org
relevance: ★★
tags: [database, erd, schema-design, sql, dbml, data-engineering, npm]
---

# Sqemo MCP

**Describe the work, get a governed schema** - Sqemo turns database design into an agent-friendly workflow: introspect a live database, build and diff entity-relationship diagrams, validate naming conventions, detect drift between model and reality, and export SQL (7 dialects) or DBML. Local `.erd.json` files need no account; cloud ERDs and Pro tools use `npx sqemo-mcp login`.

```
Server type: npm package (stdio)
Auth: None for local .erd.json files; npx sqemo-mcp login for cloud ERDs and Pro tools
Install: npm install sqemo-mcp (or npx sqemo-mcp)
Registry: io.github.sqemo/sqemo (Official MCP Registry)
License: MIT
Tools: 15
Built by: Sqemo (app.sqemo.com)
```

## Why This Matters for Operators

Schema drift is where data pipelines quietly die: the model says one thing, the production database another, and no one notices until a report breaks. **Sqemo gives agents the governance layer schema work usually lacks** - a dictionary of approved terms, naming checks, drift detection against the live database, and versioned ERDs that can be diffed like code. The agent proposes, the tool validates, and the operator reviews a governed change instead of a surprise migration.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `introspect_db` | Reverse-engineer a live database into a model |
| `create_erd` / `get_erd_overview` | Build and read entity-relationship diagrams |
| `diff_erds` | Compare two model versions |
| `check_db_drift` | Detect differences between the model and the live database |
| `check_naming` | Validate naming conventions against the dictionary |
| `list_domains` / `list_relationships` / `list_proposals` | Model contents and proposed changes |
| `search_dictionary` | Query the approved terminology dictionary |
| `generate_physical_name` | Derive physical names from logical ones |
| `export_sql` / `export_dbml` / `export_alter_sql` | Export DDL in 7 SQL dialects, DBML, or alter scripts |
| `auto_layout` | Arrange diagrams automatically |

## Installation

```bash
npm install sqemo-mcp
# or: npx sqemo-mcp
npx sqemo-mcp login    # only needed for cloud ERDs / Pro tools
```

## Configuration

```json
{
  "mcpServers": {
    "sqemo": {
      "command": "npx",
      "args": ["sqemo-mcp"]
    }
  }
}
```

Works with Claude Code, Claude Desktop, Cursor and any MCP client. The full agent walkthrough (every tool call, from plain-language request to governed schema) is at sqemo.com/docs/ai-walkthrough.
