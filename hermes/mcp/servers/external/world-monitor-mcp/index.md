---
title: "World Monitor MCP - CorpusIQ Docs"
description: Live global-intelligence MCP server for AI agents — markets, geopolitical risk, supply chains, sanctions, energy, cyber threats and procurement, all source-grounded with freshness stamps.
category: Research
stars: n/a (new listing)
added: 2026-08-15
source: mcp.so
relevance: ★★★
tags: [geopolitical-intelligence, risk-monitoring, supply-chain, sanctions, market-data, procurement, macro-economics, remote-mcp]
---

# World Monitor MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1 or API key)** — World Monitor exposes its global-intelligence platform over MCP: 63 read-only tools spanning markets, conflicts, aviation, maritime activity, energy, climate, cyber threats, supply chains, sanctions, and procurement, all backed by hundreds of institutional and open-source providers with per-observation provenance and freshness metadata.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (first-connect browser flow) or API key
Endpoint: https://worldmonitor.app/mcp
Tools: 63 (read-only)
Pricing: Free tier + Pro (worldmonitor.app/pro)
Category: Research / Geopolitical Intelligence
Built by: koala73 (github.com/koala73/worldmonitor, AGPL-3.0)
```

## Why This Matters for Operators

Most agents can search the web, but search results do not give a stable operating picture. World Monitor normalizes hundreds of official, institutional, commercial, and open-source providers into consistent intelligence surfaces an agent can query with one tool call each — with `cached_at` and `stale` fields on every result so the agent can tell a current observation from a degraded snapshot.

**The differentiator is source-attributed, freshness-stamped, structured intelligence across every domain that breaks a supply chain** — chokepoint transit counts on a 10-minute cadence, OFAC sanctions lists, tariff trends, energy storage levels, maritime disruptions, and open procurement opportunities — plus server-side JMESPath projection on every tool so large responses get trimmed before they enter the model context.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `get_market_data` | Real-time equities, commodities, crypto, and FX quotes |
| `get_country_risk` | Composite Instability Index (0-100) plus component breakdown per country |
| `get_supply_chain_data` | Dry-bulk shipping stress, customs revenue flows, COMTRADE bilateral trade |
| `get_chokepoint_status` | Live maritime chokepoint vessel transit counts (10-min cadence) |
| `get_tariff_trends` | US tariff trends (HTS-coded), BigMac index, FAO Food Price Index |
| `get_sanctions_data` | OFAC SDN entities and per-country sanctions pressure scores |
| `get_procurement_opportunities` | Search open global public-procurement opportunities |
| `get_company_intelligence` | Per-company corporate intelligence from SEC EDGAR and market data |
| `get_country_macro` | IMF WEO indicators for ~210 countries |
| `get_energy_intelligence` | EIA petroleum stocks, electricity prices, gas storage, disruptions |
| `get_news_intelligence` | AI-classified geopolitical threat news and GDELT signals |
| `get_cyber_threats` | Malware IOCs, CISA known exploited vulnerabilities |
| `get_world_brief` | Citation-grounded world intelligence brief from the dashboard snapshot |
| `get_country_brief` | AI-generated per-country intelligence brief |
| `get_alert_digest` | Cross-domain rollup of everything that tripped a threshold today |
| `get_forecast_predictions` | AI-generated geopolitical and economic forecasts with scorecards |

## Installation

```bash
claude mcp add world-monitor --transport http https://worldmonitor.app/mcp
```

The first connect opens a browser OAuth authorization; the credential is reused afterward. Codex, Cursor, VS Code, and generic clients are covered by the vendor docs at worldmonitor.app/docs/mcp-overview.

## Configuration

```json
{
  "mcpServers": {
    "world-monitor": {
      "type": "http",
      "url": "https://worldmonitor.app/mcp"
    }
  }
}
```

Auth notes: OAuth 2.1 on first connect, or a World Monitor API key for headless agents. Every tool response carries `cached_at`/`stale` freshness fields, and every tool accepts JMESPath projection to shrink large payloads.

## Business Relevance

- **Procurement & supply-chain operators** get live chokepoint status, dry-bulk stress, tariffs, and open procurement opportunities in one query
- **Compliance & risk teams** get OFAC sanctions, country risk scores, and cyber-threat feeds with named sources
- **Finance & trading operators** get markets, prediction markets, country macro, and consumer-price intelligence with provenance
- **Founders watching macro exposure** get the world brief, forecast scorecards, and regional briefs without analyst subscriptions
- **Security teams** get CISA KEV, malware IOCs, and infrastructure outage status from one endpoint

## Integration with CorpusIQ

World Monitor is the outside-world layer that CorpusIQ's inside-the-business connectors lack. A composed workflow: use Stripe and QuickBooks connectors to map revenue exposure by country, then World Monitor's `get_country_risk` and `get_supply_chain_data` to score those same countries for instability and logistics stress. Feed Google Ads and Meta Ads connectors with `get_tariff_trends` and consumer-price data to reallocate spend away from softening markets. It also complements the catalogued NERAI Risk Intelligence server — World Monitor is the broader surveillance surface, NERAI the calibrated forecasting layer.

## Limitations

- Brand new listing — no long track record yet
- Commercial cloud service; source is AGPL-3.0 but the hosted endpoint is the product
- Pro tools (`search_intel_history`, `get_similar_events`, `get_intel_timeline`) are gated behind the Pro tier
- China macro is limited to official 12-series data; upstream gaps are declared in the tool docs
- AI-generated forecasts and briefs are model outputs — always check the source fields

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
