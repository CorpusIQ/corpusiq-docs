---
title: PingCheck MCP — Status Page Monitoring for AI Agents
description: "Setup and usage guide for PingCheck MCP — Status Page Monitoring for AI Agents. Part of the Hermes resource directory."
last_updated: 2026-08-12
---

# PingCheck MCP — Status Page Monitoring for AI Agents

**Priority:** HIGH | **Category:** DevOps / Monitoring  
**Transport:** stdio (npx) | **Auth:** API key (optional for public pages)  
**Repository:** [Churman1113/pingcheck](https://github.com/Churman1113/pingcheck) (MIT)  
**Website:** https://pingcheck.cloud  
**Discovered:** July 27, 2026 (chatmcp/mcpso #3307)

## What It Does for Operators

PingCheck lets AI agents monitor infrastructure without opening a browser. Query any public status page with zero config — just pass a slug. With an API key, agents can manage monitors, get component-level uptime/response times, trigger on-demand re-checks, create components, and manage incidents.

**For operators running SaaS or ecommerce:** Your agent can now be your first responder — detecting incidents, creating status updates, and notifying stakeholders without human intervention.

## Installation

```bash
npx -y pingcheck-mcp
# Or with API key for private pages:
export PINGCHECK_API_KEY="pk_..."
npx -y pingcheck-mcp
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "pingcheck": {
      "command": "npx",
      "args": ["-y", "pingcheck-mcp"],
      "env": {
        "PINGCHECK_API_KEY": "pk_YOUR_KEY"
      }
    }
  }
}
```

## Tools (8)

| Tool | Auth | Description |
|------|------|-------------|
| `pingcheck_public_status` | None | Query any public status page by slug |
| `pingcheck_list_my_pages` | API key | List your monitored pages |
| `pingcheck_page_detail` | API key | Component-level uptime + response times |
| `pingcheck_check_now` | API key | Trigger on-demand re-check |
| `pingcheck_create_component` | API key | Add new monitored component |
| `pingcheck_delete_component` | API key | Remove component |
| `pingcheck_create_incident` | API key | Create incident report |
| `pingcheck_update_incident` | API key | Update/resolve incident |

## Operator Use Cases

1. **Automated incident response:** Agent polls `pingcheck_page_detail` every 5 min — if a component goes down, automatically creates an incident and posts to Slack
2. **Vendor reliability tracking:** Monitor your critical SaaS vendors' status pages (Stripe, Shopify, AWS) — agent alerts you before customers notice
3. **SLA compliance reporting:** Weekly agent pull of uptime data, auto-generated SLA report for client deliverables
4. **On-call handoff:** Agent creates incident, updates it through investigation, resolves it with timeline — complete incident record without manual logging
5. **Multi-site monitoring:** Operators with multiple storefronts/services use one agent to monitor all status pages from a single dashboard

## CorpusIQ Angle

**Complementary.** CorpusIQ monitors business health through financial/operational data. PingCheck adds infrastructure health monitoring. An operator could configure CorpusIQ to correlate revenue dips with infrastructure incidents — "Did the 3:14 PM revenue drop coincide with the payment gateway outage?"

## Limitations

- Free tier covers public status pages only
- Private monitoring requires paid API key (pricing TBD)
- Node.js >= 18 required
- New product — may lack integrations with major incident platforms (PagerDuty, Opsgenie)
