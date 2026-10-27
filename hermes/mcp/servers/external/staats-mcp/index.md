---
title: Staats MCP - Cookieless Web Analytics for Agents
description: Cookieless web analytics that your agent reads in conversation - traffic, referrers, funnels and deploy-tagged before and after comparisons with proactive anomaly surfacing.
category: Data & Analytics
stars: n/a (new listing)
added: 2026-09-02
source: mcp.so
relevance: ★★
tags: [analytics, cookieless, web-analytics, funnels, privacy, remote-mcp]
last_updated: "2026-10-24"
---

# Staats MCP

**Remote MCP server (Streamable HTTP, API key)** - cookieless web analytics with no dashboard, built by Mr Violets. You connect Staats to your agent once, and the analytics arrive in the conversation you are already having about the code. Fourteen tools cover traffic, referrers, funnels and journeys, deploy-tagged before-and-after comparisons, stored site context, and proactive anomaly surfacing.

```
Server type: Remote (Streamable HTTP)
Auth: Account key (per-account, covers every site)
Endpoint: https://api.staats.ai/functions/v1/mcp
Tools: 14 (site context, overview, query, funnel, journeys, annotations, comparisons)
Pricing: Free tier 10,000 events/month, no card required
Category: Data & Analytics
Built by: Mr Violets (staats.ai)
```

## Why This Matters for Operators

Analytics dashboards answer questions nobody asked; agents answer questions you ask. Staats moves the analytics into the workflow where the decisions happen - the agent that ships code or content also reads its effect, without switching tools.

Three ideas separate it from a GA4 wrapper. **Deploy measurement: the agent tags each deploy with its commit and routes, then `compare_around` reports before-and-after traffic with statistical honesty.** Site memory: the stored site context tells every future session what the site is for and what each funnel step means. And proactivity: anomalous days, first-time referrers and page surges are surfaced, not queried for.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `get_site_context` / `update_site_context` | Read and maintain what a site is for: goals, audience, events, funnel meaning |
| `get_overview` | Visitor and pageview totals versus the prior period, top pages, referrers, daily series |
| `what_changed` | Statistically unusual days, referrer surges, page-share jumps, with annotations |
| `query` | Break visitors, pageviews or events down by path, referrer, UTM, device, browser, country |
| `funnel` | Ordered conversion funnel across up to 5 pageview or event steps |
| `journeys` | Discovered routes grouped into sequences, busiest first |
| `record_annotation` / `list_annotations` | Mark deploys and changes on the site timeline |
| `compare_around` | Before and after impact of a recorded annotation, per route when recorded |
| `list_sites` / `create_site` / `delete_site` | Site management with ready-to-paste ~1.5KB script tags |
| `portfolio_overview` | Visitors and pageviews for every site on the account |

## Installation

```bash
claude mcp add --scope user --transport http staats https://api.staats.ai/functions/v1/mcp/YOUR_ACCOUNT_KEY
```

## Configuration

```json
{
  "mcpServers": {
    "staats": {
      "type": "http",
      "url": "https://api.staats.ai/functions/v1/mcp/YOUR_ACCOUNT_KEY"
    }
  }
}
```

Create a free account at staats.ai, copy the account key, and one key covers every site on the account. The agent can create sites and install the tracker tag itself.

## Business Relevance

- **Founders** get traffic and funnel answers in the same conversation where changes are decided
- **Content operators** see what changed after each publish without opening an analytics tool
- **Product teams** measure deploy impact per route with before-and-after honesty
- **Agencies** monitor client sites from one account with a portfolio overview

## Integration with CorpusIQ

Staats reads website behaviour; CorpusIQ reads business outcomes. An agent composing both can answer the question analytics dashboards never close: did the traffic change actually change the money. Staats reports the deploy or campaign before-and-after, then CorpusIQ's Stripe and GA4 connectors confirm whether conversions and revenue moved with it. For an operator testing landing pages, the loop is concrete: ship, annotate, compare traffic in Staats, and verify revenue in CorpusIQ before calling the test.

## Limitations

- Brand new listing with no track record yet
- Free tier capped at 10,000 events per month
- Privacy-first counting means daily-rotating visitor identity, so multi-day journeys undercount
- Event-level analytics only; no session replays or heatmaps
