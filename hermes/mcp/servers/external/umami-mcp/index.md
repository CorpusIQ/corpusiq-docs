---
title: "Umami MCP - Official Website Analytics for AI Agents"
description: "Official MCP server for Umami analytics: 23 read-only tools that answer questions about website traffic, pages, referrers, channels, events, goals, funnels, journeys, retention, attribution, revenue and Core Web Vitals. Connects to Umami Cloud or any self-hosted instance; every tool goes through the public API with the same user and team permissions as the web app."
category: Data & Analytics
stars: n/a (official npm package @umami/mcp; the Umami repo carries 25K+ GitHub stars)
added: 2026-09-15
source: "mcpservers.org /all page 3 + vendor page at mcpservers.org/servers/umami-mcp"
relevance: ★★★
tags: [web-analytics, pageviews, funnels, retention, attribution, core-web-vitals, umami, read-only, api-key, remote-mcp]
---

# Umami MCP

**The official analytics server for the privacy-first analytics platform.** Umami's MCP server lets Claude, ChatGPT, Cursor and other MCP clients answer questions about website traffic with 23 read-only tools that call the Umami API through the official `@umami/api-client`. The MCP server never talks to a database; every tool goes through the public API and the same user and team permission checks as the web app.

```
Server type: Remote (Streamable HTTP) on Umami Cloud or self-hosted; stdio via npx locally
Auth: Bearer API key (cloud: api_... key; self-hosted: umami_... key from Settings, API keys)
Endpoint: https://cloud.umami.is/mcp (cloud) or https://your-umami.example.com/mcp (self-hosted, set MCP_ENABLED=1)
Tools: 23, all read-only (websites, stats, traffic, metrics, events, sessions, funnels, goals, journeys, retention, attribution, revenue, Core Web Vitals)
Pricing: Umami Cloud plans; self-hosted is open source
Category: Data & Analytics / Web Analytics
Built by: Umami (umami.is), official package @umami/mcp
```

## Why This Matters for Operators

Umami is the analytics platform operators reach for when they want GDPR-light, cookieless tracking they can self-host, and its MCP server is the official bridge into agent workflows. Instead of exporting CSVs or building dashboard screenshots, the assistant answers the question directly: which channel converted, where the drop-off is, whether the new landing page moved Core Web Vitals.

The permission model is the trust story: the key is scoped to the same user and team permissions as the web app, every tool is read-only, and on self-hosted instances the endpoint is disabled by default until the operator flips `MCP_ENABLED=1`. Analytics access does not become analytics writes.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `list_websites` | Find the websites you can access (call first to get a websiteId) |
| `get_website_stats` | Pageviews, visitors, visits, bounce rate, duration plus previous period |
| `get_website_traffic` | Pageview/visit time series by minute, hour, day, month or year |
| `get_website_metrics` | Top pages, referrers, channels, countries, browsers, devices, UTM, events |
| `get_website_daterange` | Earliest and latest dates with recorded data |
| `get_realtime` | Visitors active right now |
| `get_events` / `get_event_stats` / `get_event_series` / `get_event_properties` | Tracked events, totals, time series and property values |
| `get_sessions` / `get_session` / `get_session_stats` | Session lists, a single session timeline, aggregate session stats |
| `list_funnels` / `run_funnel` | Saved funnels and conversion runs |
| `get_goals` | Saved goals with conversions, visitors and rate |
| `run_journey` | Most common visitor paths |
| `run_retention` | Cohort retention tables |
| `run_attribution` | First/last-click attribution for conversions |
| `get_revenue` | Revenue totals, series and breakdowns |
| `get_performance` | Core Web Vitals percentiles, trend and breakdown |

All tools are read-only. Dates are ISO 8601; results are paginated with a hard cap on page size.

## Installation

```bash
# Umami Cloud
claude mcp add umami --transport http https://cloud.umami.is/mcp

# Self-hosted: enable MCP_ENABLED=1, then point the client at your instance
claude mcp add umami --transport http https://your-umami.example.com/mcp
```

Set the authorization header with your key (`Authorization: Bearer api_...` on Cloud, `Authorization: Bearer umami_...` self-hosted; the `x-umami-api-key` custom header also works where supported). Browser login tokens are not supported.

## Configuration

```json
{
  "mcpServers": {
    "umami": {
      "type": "http",
      "url": "https://cloud.umami.is/mcp",
      "headers": {
        "Authorization": "Bearer api_your_key"
      }
    }
  }
}
```

For a local stdio setup: `npx -y @umami/mcp` with `UMAMI_URL` and `UMAMI_API_TOKEN` env vars. Revoke the key in Settings to disconnect access.

## Business Relevance

- **Operators running Umami already** get agent access with zero new infrastructure and read-only guarantees.
- **E-commerce teams** get funnels, retention and revenue attribution asked in plain language.
- **Agencies** get per-client websites behind team-scoped keys, so one assistant serves every client without cross-access.
- **Performance teams** get Core Web Vitals percentiles and breakdowns inside their workflow, not in a separate console.

## Integration with CorpusIQ

Umami reads site behavior; CorpusIQ reads the business outcome. The pair connects analytics to money: Umami's funnel and attribution tools show which channel and page drove the session, and CorpusIQ's Stripe connector shows whether it converted to revenue, while GA4 inside CorpusIQ provides the cross-check on acquisition. For a self-hosted, privacy-first stack, Umami MCP plus CorpusIQ's read-only connectors covers behavior and books in one agent session, with every number traceable to its source system.

## Limitations

- Read-only by design: no event creation, no site or funnel management through MCP.
- Requires an existing Umami deployment (Cloud subscription or self-hosted instance); the server adds no analytics of its own.
- Self-hosted endpoint disabled by default (`MCP_ENABLED=1` required) and key-gated.
- Tool results are paginated with a hard page-size cap; large date ranges need multiple calls.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
