---
title: "Salesforce MCP — Integration Guide"
description: Connect AI agents to Salesforce CRM for accounts, contacts, opportunities, leads, cases, and custom objects through MCP.
github: https://github.com/smn2gnt/MCP-Salesforce
stars: 179
status: Community (not official Salesforce)
transport: Local stdio
auth: Salesforce OAuth 2.0 (Connected App)
category: CRM & Sales
added: 2026-07-29
---

# Salesforce MCP — Integration Guide

## Overview

The MCP Salesforce connector bridges AI agents to the world's largest CRM platform. Agents can query and manage accounts, contacts, opportunities, leads, cases, reports, and custom objects through the Salesforce REST API. Community-maintained by smn2gnt, this is the first dedicated Salesforce MCP server.

⚠️ **Not official Salesforce.** This is community-built. Salesforce has not (yet) shipped an official MCP server. Test thoroughly before production use.

For sales operators: AI agents can run pipeline reviews, update opportunity stages, log activities, and pull reports — all through natural language conversation.

## Quick Start

### Prerequisites
- Salesforce org (Enterprise, Unlimited, or Developer Edition)
- Connected App with OAuth 2.0 configured
- Python 3.9+

### Installation

```bash
pip install mcp-salesforce
```

Or from source:

```bash
git clone https://github.com/smn2gnt/MCP-Salesforce.git
cd MCP-Salesforce
pip install -e .
```

### MCP Client Config

```json
{
  "mcpServers": {
    "salesforce": {
      "command": "python",
      "args": ["-m", "mcp_salesforce"],
      "env": {
        "SF_CLIENT_ID": "your-connected-app-client-id",
        "SF_CLIENT_SECRET": "your-connected-app-client-secret",
        "SF_USERNAME": "your-salesforce-username",
        "SF_PASSWORD": "your-password-plus-token",
        "SF_INSTANCE_URL": "https://your-instance.salesforce.com"
      }
    }
  }
}
```

### Authentication

Uses Salesforce OAuth 2.0 Username-Password flow. Requires:
1. A Connected App in Salesforce Setup → App Manager
2. Enable OAuth settings with "Password" grant type
3. Add your security token to the password (Settings → Reset My Security Token)

**Alternative (more secure):** JWT Bearer flow — generate a certificate, upload to Connected App, use private key for auth. The MCP supports this via `SF_JWT_KEY` env var.

## Tools

Salesforce MCP exposes tools organized by standard object:

| Object | Read Tools | Write Tools |
|--------|-----------|-------------|
| **Account** | `query_accounts`, `get_account` | `create_account`, `update_account` |
| **Contact** | `query_contacts`, `get_contact` | `create_contact`, `update_contact` |
| **Opportunity** | `query_opportunities`, `get_opportunity` | `create_opportunity`, `update_opportunity` |
| **Lead** | `query_leads`, `get_lead` | `create_lead`, `update_lead`, `convert_lead` |
| **Case** | `query_cases`, `get_case` | `create_case`, `update_case` |
| **Task/Activity** | `query_tasks`, `get_task` | `create_task`, `complete_task` |
| **Report** | `list_reports`, `run_report` | — (read-only) |
| **Custom Objects** | `query_custom` | `create_custom`, `update_custom` |
| **SOQL** | `execute_soql` | — (read-only) |
| **Search** | `search_sosl` | — (read-only) |

`execute_soql` gives full read access to any object via SOQL queries — the most powerful tool. Agents can query any standard or custom object with relationship traversal.

## Business Operator Use Cases

### 1. Pipeline Review
```
User: "Show me all opportunities closing this month over $50K, grouped by stage"
Agent: [executes SOQL, returns pipeline table with stage, amount, close date, owner]
```

### 2. Activity Logging
```
User: "Log a call with Acme Corp — discussed Q3 renewal, they're interested in upgrading to Enterprise"
Agent: [finds Acme account, creates task with call details, updates opportunity notes]
```

### 3. Lead Qualification
```
User: "Pull all new leads from this week from the webinar campaign and score them"
Agent: [queries leads by source/date, returns ranked list by custom scoring criteria]
```

### 4. Report + Analyze
```
User: "Run the monthly sales forecast report and flag any reps below 80% of quota"
Agent: [runs forecast report, computes attainment %, highlights at-risk reps]
```

### 5. Account Research
```
User: "Before my call with Globex, show me their open opportunities, recent cases, and last 5 activities"
Agent: [pulls account 360 view across objects, returns briefing summary]
```

## Security Considerations

- **SOQL is powerful:** `execute_soql` can read any object the authenticated user can access. Review the Connected App's permission scope.
- **No write approval gates:** Unlike some MCPs, this server doesn't have built-in approval flows for writes. Consider wrapping in an approval layer for production.
- **API limits:** Salesforce has 24-hour API call limits. Heavy agent usage can exhaust them. Monitor via Setup → System Overview.
- **Field-level security:** The agent inherits the authenticated user's field-level security — it can't see fields the user can't.
- **Audit trail:** All changes appear in Salesforce's setup audit trail under the authenticated user.

## Pricing

- **Salesforce MCP:** Free, open source (MIT license)
- **Salesforce API access:** Included with Enterprise and Unlimited editions. Not available in Essentials or Professional without API add-on.

## Comparison: Salesforce MCP vs Attio MCP

| Feature | Salesforce MCP | Attio MCP |
|---------|---------------|-----------|
| Platform | Salesforce (enterprise CRM) | Attio (AI-native CRM) |
| Stars | 179⭐ | — (npm package) |
| Official | ❌ Community | ✅ Official |
| Object model | Standard + custom objects | Flexible object model |
| Query power | SOQL (very powerful) | API query |
| Best for | Enterprises on Salesforce | Startups/scaleups on Attio |

## Limitations

- **Not official:** Community-maintained — may lag behind Salesforce API changes
- **No Streaming API:** Doesn't support PushTopic or Change Data Capture events
- **Bulk operations:** No Bulk API 2.0 support — large data volumes use REST API limits
- **Einstein/AI features:** No integration with Salesforce Einstein for predictions

## See Also

- [Attio MCP Guide](/hermes/mcp/servers/external/attio-mcp-server/) — AI-native CRM alternative
- [Apollo.io MCP Guide](/hermes/mcp/servers/external/apollo-io-mcp/) — B2B contact enrichment
- [LinkedIn MCP Guide](/hermes/mcp/servers/external/linkedin-mcp-gtm/) — Social selling complement
- [Salesforce REST API Docs](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/)
