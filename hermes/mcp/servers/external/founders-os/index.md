---
title: Founders OS MCP Integration Guide
description: Full setup guide for Founders OS — open-source MCP server connecting CRM, financials, tasks, and memory for founders and business operators
---

# Founders OS MCP — Integration Guide

**Open-source MCP server that puts your whole business inside Claude, Cursor, or any MCP client.** Connects CRM, financials, tasks, and long-term memory behind one server — ask a single question that reads across all your business systems.

> **GitHub:** [OurThinkTank/founders-os](https://github.com/OurThinkTank/founders-os) ⭐7 · **Last pushed:** July 4, 2026

## What It Does

Founders OS is a unified business interface for AI agents. Instead of connecting separate MCP servers for your CRM, task manager, financial dashboard, and knowledge base, Founders OS provides all of them behind a single MCP endpoint. Ask "Which clients are behind on payments and what tasks do I have with them?" and the agent queries across all connected systems.

## Key Capabilities

- **CRM Access** — Search and retrieve customer/lead records, deal stages, and contact history
- **Financial Overview** — Revenue, invoicing, payment status, and cash flow data
- **Task Management** — Create, read, update, and complete tasks across projects
- **Long-Term Memory** — Persistent knowledge store for business context, decisions, and notes
- **Cross-System Queries** — Single natural language question spans all connected systems

## Installation

```bash
# Clone and install
git clone https://github.com/OurThinkTank/founders-os.git
cd founders-os
npm install

# Or via npx (if published)
npx -y founders-os-mcp
```

## Hermes / Claude Desktop Configuration

```json
{
  "mcpServers": {
    "founders-os": {
      "command": "node",
      "args": ["path/to/founders-os/build/index.js"],
      "env": {
        "CRM_API_KEY": "your-crm-key",
        "FINANCIALS_API_KEY": "your-finance-key",
        "TASKS_API_KEY": "your-tasks-key"
      }
    }
  }
}
```

## CorpusIQ Use Cases

### 1. Daily Business Standup
```
"Give me a business standup: what's in my pipeline, any overdue invoices, 
and what tasks are due today?"
```
The agent queries CRM for pipeline, financials for overdue invoices, and tasks for due items — all in one prompt.

### 2. Client Health Check
```
"Show me all clients who haven't been contacted in 30+ days and have 
outstanding invoices"
```
Cross-references CRM contact dates with financial data to surface at-risk accounts.

### 3. Decision Support
```
"I'm considering raising prices for Plan B. Show me current Plan B customers, 
their usage patterns, and whether any have complained recently."
```
Combines CRM segmentation, usage analytics, and support history.

## Operator Value

| Use Case | Systems Queried | Time Saved |
|----------|----------------|------------|
| Daily standup | CRM + Finance + Tasks | 15-20 min/day |
| Client health check | CRM + Finance | 30+ min/week |
| Decision support | All systems | Hours per decision |

## Prerequisites

- Node.js 18+
- API keys for connected business systems
- MCP client (Claude Desktop, Cursor, Hermes, Windsurf)

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Server won't start | Check Node.js version (`node --version`), ensure npm install completed |
| CRM queries fail | Verify CRM_API_KEY is set and has read permissions |
| Cross-system queries slow | Systems respond sequentially; add timeouts for unresponsive connectors |

## Related Resources

- [External MCP Server Catalog](/hermes/mcp/servers/external/) — full curated catalog
- [CorpusIQ MCP Connectors](/hermes/mcp/connectors/) — 37+ native business data connectors
- [MCP Documentation](/hermes/mcp/)

---

*← [External MCP Catalog](/hermes/mcp/servers/external/) | [MCP Servers Home](/hermes/mcp/servers/) →*

*Guide created July 4, 2026. Based on Founders OS v0.x. Check [GitHub repo](https://github.com/OurThinkTank/founders-os) for latest updates.*
