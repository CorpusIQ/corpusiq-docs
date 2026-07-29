---
title: "Tableau MCP — Integration Guide"
description: Connect AI agents to Tableau Cloud/Server for BI queries, workbook access, and data visualization through MCP.
github: https://github.com/tableau/tableau-mcp
stars: 315
status: Official
transport: Remote Streamable HTTP
auth: Tableau Personal Access Token (PAT) or OAuth
category: Analytics & BI
added: 2026-07-29
---

# Tableau MCP — Integration Guide

## Overview

Tableau's official MCP server lets AI agents connect to Tableau Cloud or Tableau Server to query data sources, list workbooks and views, execute calculated fields, and retrieve visualization data. It's the second major BI platform to ship MCP (after Metabase on July 26), opening enterprise BI to agent-driven analysis.

For operators, this means: ask "what was Q2 revenue by region?" and your AI agent queries Tableau's semantic layer directly — no dashboard screenshots, no CSV exports, no context switching.

## Quick Start

### Prerequisites
- Tableau Cloud site or Tableau Server (2023.1+)
- Personal Access Token (PAT) with appropriate permissions
- Node.js 18+

### Installation

```bash
npx @tableau/mcp-server
```

Or add to your MCP client config:

```json
{
  "mcpServers": {
    "tableau": {
      "command": "npx",
      "args": ["@tableau/mcp-server"],
      "env": {
        "TABLEAU_SITE_URL": "https://your-site.tableau.com",
        "TABLEAU_PAT_NAME": "your-token-name",
        "TABLEAU_PAT_SECRET": "your-token-secret"
      }
    }
  }
}
```

### Authentication

Tableau MCP supports:
1. **Personal Access Tokens (PAT)** — Recommended. Create in Tableau Cloud/Server → My Account Settings → Personal Access Tokens.
2. **OAuth 2.0** — For multi-user deployments.

Token permissions determine what the AI agent can access. Start with read-only for data sources and workbooks.

## Tools

Tableau MCP exposes these tool categories:

| Tool | Description |
|------|-------------|
| `list_data_sources` | List all published data sources |
| `query_data_source` | Execute a query against a data source |
| `list_workbooks` | List all workbooks in the site |
| `list_views` | List views in a workbook |
| `get_view_data` | Retrieve underlying data for a view |
| `get_view_image` | Get a PNG image of a view |
| `run_calculated_field` | Create and evaluate a calculated field |
| `list_projects` | Browse projects/folders |
| `search_content` | Search across all content types |

## Business Operator Use Cases

### 1. Ad-Hoc Analytics
```
User: "Show me revenue by product line for Q2, compared to Q1"
Agent: [queries Tableau sales data source, computes YoY change, returns table + insight]
```

### 2. Pipeline Review
```
User: "What's our current sales pipeline by stage and rep?"
Agent: [queries CRM-published Tableau data source, returns breakdown]
```

### 3. KPI Monitoring
```
User: "Which regions are below forecast this month?"
Agent: [queries finance workbook, compares actuals vs forecast, flags underperformers]
```

### 4. Automated Reporting
Combine with cron or scheduled triggers to have AI agents pull Tableau data, analyze it, and push findings to Slack/email.

## Security Considerations

- **PAT scope matters:** Create purpose-specific tokens with minimum required permissions
- **Read-only first:** Start with read-only data source permissions, expand cautiously
- **No write tools (currently):** Tableau MCP is read-only — safe for production use
- **Network access:** Agent needs network access to your Tableau Cloud/Server instance
- **Audit trail:** All queries appear in Tableau's admin logs under the PAT owner

## Pricing

Tableau MCP is free and open source (MIT license). Requires an existing Tableau Cloud or Server license — no additional MCP-specific cost.

## Comparison: Tableau vs Metabase MCP

| Feature | Tableau MCP | Metabase MCP |
|---------|-------------|--------------|
| Stars | 315⭐ | 48,400⭐ (Metabase itself) |
| Official | ✅ | ✅ Built-in |
| Transport | Remote HTTP | Streamable HTTP |
| Query model | Data source queries | Semantic layer + raw SQL |
| Write tools | No | Yes (questions, dashboards) |
| Best for | Enterprise BI orgs | SMB/startup analytics |
| Pricing | Needs Tableau license | Needs Metabase instance |

Both complement CorpusIQ's business intelligence stack. Tableau for enterprises already invested in the platform; Metabase for teams building fresh.

## See Also

- [Metabase MCP Guide](/hermes/mcp/servers/external/metabase-mcp/) — Another BI platform with MCP
- [Stripe MCP Guide](/hermes/mcp/servers/external/stripe-mcp/) — Financial data via MCP
- [Tableau Developer Docs](https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api.htm)
