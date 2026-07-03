---
title: "dbridge MCP — Secure Natural Language SQL for AI Agents"
description: "Query databases with natural language, secured by column masking, row caps, and query limits. AI agents get SQL access without exposing raw data — security-first database MCP."
category: mcp
tags: [mcp-server, database, sql, security, postgresql, mysql, data-access, governance]
last_updated: 2026-07-02
---

# dbridge MCP Server ★ New (July 2 PM)

## Overview

dbridge MCP (`ugurcl/dbridge-mcp`) takes a fundamentally different approach to database MCP servers: security-first, not access-first. AI agents can query databases using natural language (translated to SQL under the hood), but every query is gated by column-level masking, per-query row caps, and configurable query limits. This addresses the #1 concern operators have about AI agents accessing databases — "what if the agent runs a `SELECT *` on a 500M-row table?" or "what if it sees PII columns?"

**Key advantage**: Natural language SQL with production-grade security guardrails — column masking, row limits, query budgets.

## Key Features

- **Natural language to SQL**: Describe what you need in plain English — dbridge translates to optimized SQL
- **Column masking**: Specify which columns are visible, masked, or hidden per table — PII and sensitive data never reach the agent
- **Row caps**: Per-query row limits prevent full table scans and runaway queries
- **Query limits**: Configurable query budgets per session — prevent resource exhaustion
- **Multi-database**: PostgreSQL, MySQL, and SQLite support
- **Explain mode**: Show the generated SQL and execution plan before running — transparency and trust

## Installation

```bash
# Clone and install
git clone https://github.com/ugurcl/dbridge-mcp.git
cd dbridge-mcp
npm install
npm run build

# Add to Hermes
hermes mcp add dbridge --command "node" --args "dist/index.js" --workdir "$(pwd)"
```

## Configuration

```json
{
  "mcpServers": {
    "dbridge": {
      "command": "node",
      "args": ["dist/index.js"],
      "workdir": "/path/to/dbridge-mcp",
      "env": {
        "DB_CONNECTION_STRING": "postgresql://user:pass@localhost:5432/mydb",
        "DBRIDGE_ROW_LIMIT": "1000",
        "DBRIDGE_MASKED_COLUMNS": "users.email,users.phone,orders.credit_card"
      }
    }
  }
}
```

## Business Relevance

- **Safe data access for non-technical teams**: Marketing, sales, and support teams can query databases without SQL knowledge — and without risk of exposing sensitive data
- **AI analytics without data exfiltration**: Column masking ensures PII, financial data, and trade secrets never leave the database in AI agent responses
- **Governed self-service BI**: Business operators get on-demand analytics from AI agents without waiting for data engineering to build dashboards
- **Audit-ready**: Every query is logged with the agent's identity, generated SQL, and row counts — compliance teams get a complete audit trail
- **Development acceleration**: Developers can explore database schemas and test queries through natural language during development

## Integration with CorpusIQ

dbridge MCP adds governed database access to CorpusIQ's analytics stack, complementing existing SQL tools (SIXTA Connect, PipeTable, Query Streams) and BI connectors (Google Analytics, Clamp Analytics). The security-first design aligns with CorpusIQ's governance model:

- **Governed queries**: Combine dbridge's column masking with CorpusIQ's pre-flight gate — queries are security-checked before they reach the database AND masked before results reach the agent
- **Cross-source intelligence**: AI agents can join CRM data (Attio), financial data (QuickBooks), and operational data (database) in a single query — with dbridge ensuring the database side is secure
- **Compliance**: Column masking + audit trail supports GDPR, HIPAA, and SOC 2 requirements for AI agent database access

## Limitations

- Self-hosted — requires Node.js runtime and database connectivity
- Database connection string management required (no remote proxy mode yet)
- Natural language translation quality depends on schema clarity
- Not a full database administration tool — focused on read queries with writes gated separately

## See Also

- [SIXTA Connect — SQL Review & Optimization](/hermes/mcp/servers/external/)
- [Query Streams MCP — Secure Database Access](/hermes/mcp/servers/external/)
- [PipeTable — DuckDB for Local Data](/hermes/mcp/servers/external/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
