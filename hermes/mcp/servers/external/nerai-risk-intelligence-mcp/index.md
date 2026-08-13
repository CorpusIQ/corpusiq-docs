---
title: "NERAI Risk Intelligence MCP — Geopolitical grounding"
description: "Connect NERAI's geopolitical risk intelligence — 60 countries, calibrated forecasts, maritime chokepoint tracking, sanctions, and trade-control data"
category: mcp
tags: [mcp-server, risk-intelligence, geopolitics, supply-chain, compliance, procurement, trading]
source: mcp.so
discovered: 2026-08-11
stars: 0
author: NERAI BV
github: https://github.com/serkvay13/nerai-mcp
mcp_endpoint: https://nerai-mcp.neraicorp.workers.dev/mcp
transport: Streamable HTTP
auth: Bearer token (instant free key via POST /register)
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/nerai-risk-intelligence-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"

---

# NERAI Risk Intelligence MCP Server

**The geopolitical grounding layer for AI agents.** Your procurement, trading, or compliance agent knows your systems; it does not know the world. NERAI is the world, as a tool call — 60 countries, calibrated forecasts with published out-of-sample validation, maritime chokepoints with live AIS traffic, sanctions and trade-control data — every answer source-linked and dated.

## Why It Matters for Operators

For business operators managing international supply chains, procurement, or compliance, geopolitical risk is the silent variable that can destroy margins overnight. NERAI brings this risk layer directly into AI agent workflows:

- *"Which of these supplier countries deteriorated this month: Turkey, Kazakhstan, Egypt?"*
- *"What is the live vessel count in the Strait of Hormuz versus baseline?"*
- *"What changed in the UK and EU trade-control registers this week? Cite the legal instruments."*
- *"Compare the risk trajectory of Poland and Romania over the next 13 weeks."*
- *"Is this commodity subject to dual-use export controls in my jurisdiction?"*

This turns AI agents from system-only tools into world-aware operators — grounding every procurement decision, trade, or compliance check in current, validated geopolitical data.

## Technical Details

| Field | Value |
|-------|-------|
| **Transport** | Streamable HTTP (remote, no local process) |
| **Auth** | Bearer token — instant free key via `POST /register` |
| **Endpoint** | `https://nerai-mcp.neraicorp.workers.dev/mcp` |
| **Tools** | 16 tools across 5 layers: Country Risk, Foresight, Supply Chain, Maritime, Trade Controls |
| **Validation** | Published out-of-sample MASE 0.85–0.95, 61–67% directional accuracy across 4–52 week horizons |
| **Free tier** | 5 countries, 100 calls/month |
| **Pro tier** | €490/mo or €4,900/yr — all 60 countries, 100k calls |
| **Enterprise** | From €15,000/yr — HS-level commodity checks, reviewed precedent corpus, SLA |
| **Response contract** | Every response carries `_meta`: `as_of`, source, refresh cadence, and limitations — self-documenting audit trail |

## Setup

### Claude Desktop / Claude Code

```bash
# Get your free key first
curl -X POST https://nerai-mcp.neraicorp.workers.dev/register \
  -H 'content-type: application/json' -d '{"email":"you@company.com"}'

# Connect
claude mcp add nerai --transport http https://nerai-mcp.neraicorp.workers.dev/mcp \
  --header "Authorization: Bearer YOUR_KEY"
```

### Claude.ai (custom connectors)

Use the key-in-URL format for clients without header fields:
```
https://nerai-mcp.neraicorp.workers.dev/mcp/YOUR_KEY
```

### Any MCP Client

```json
{
  "mcpServers": {
    "nerai": {
      "type": "streamable-http",
      "url": "https://nerai-mcp.neraicorp.workers.dev/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_KEY"
      }
    }
  }
}
```

## Tool Layers

| Layer | Tools | Business Use |
|-------|-------|-------------|
| **Country Risk** | `list_countries`, `get_country_risk`, `compare_countries`, `get_causal_drivers` | Compare supplier country stability; identify risk drivers |
| **Foresight** | `get_forecast_desk` (re-scored every 2 days, Brier-tracked), `get_early_warning` | Anticipate changes before they impact supply chains |
| **Supply Chain** | `get_supply_chain_risk`, `get_commodities` | Map exposure across sourcing regions |
| **Maritime** | `get_maritime_corridors`, `get_live_chokepoint_traffic` (live AIS), `get_circumvention_corridors` | Monitor shipping routes and chokepoints in real-time |
| **Trade Controls** | `get_sanctions_overview`, `get_tradecontrol_changes`, `check_commodity_controls`, `find_enforcement_precedent`, `get_transaction_intelligence_status` | Verify compliance before transactions |

## For Business Operators

NERAI is built for the procurement, trading, and compliance operator who needs to make decisions in an uncertain world. Unlike generic risk reports that arrive weekly, this MCP server lets your AI agent check ground truth at decision time — whether that's re-ordering from a supplier in a deteriorating region, routing a shipment around a chokepoint, or verifying that a transaction doesn't trigger sanctions.

The free tier (5 countries, 100 calls/month) is sufficient for operators focused on a specific region. Pro unlocks the full 60-country dataset and 100k monthly calls — suitable for global supply chain operators. Enterprise includes human-reviewed enforcement precedents and commodity-level trade control checks.

**Key differentiator:** NERAI publishes its forecast validation scores (MASE 0.85–0.95). Unlike most risk providers who claim accuracy, NERAI proves it — ask your current vendor for their Brier score.

---

*Built and operated by [NERAI BV](https://neraicorp.com), Brussels. Contact: kagan@neraicorp.com*
