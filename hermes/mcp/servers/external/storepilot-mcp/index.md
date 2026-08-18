---
title: "StorePilot MCP - CorpusIQ Docs - CorpusIQ Docs"
description: "Run an app portfolio across Google Play and the App Store from one MCP server: vitals, reviews, earnings, and crash detection, 34 tools"
category: Commerce & E-Commerce
stars: n/a (new listing)
added: 2026-08-17
source: mcp.so GitHub issue #3607
relevance: ★★★
tags: [app-store, google-play, app-store-connect, aso, app-operations, vitals, stdio-mcp, open-source]
---

# StorePilot MCP

**Local MCP server (stdio, MIT, Python 3.11+) that runs a whole app portfolio across Google Play and the App Store from one install.** 34 tools cover both stores instead of one store or one app at a time: crash and ANR vitals compared against Google's own bad-behavior thresholds, Google's anomaly detections, installs, ratings, earnings, reviews, and portfolio-wide health. Published to PyPI as `storepilot`.

```
Server type: Local (stdio)
Auth: Google Play Console and App Store Connect API credentials (bring your own)
Install: pip install storepilot
Tools: 34 (Google Play + App Store Connect surfaces)
Pricing: Free, open source (MIT)
Category: App Portfolio Operations
Built by: sonlenef, repo github.com/sonlenef/storepilot-mcp
```

## Why This Matters for Operators

App operators live in two dashboards that refuse to talk to each other. StorePilot collapses Google Play and the App Store into one MCP surface, so a single agent can answer "which of my twelve apps had a crash-rate regression this week, and what are the reviews saying about it" without switching contexts or hand-copying numbers.

The vitals comparison is the useful part: instead of raw crash rates, StorePilot compares your apps against Google's own thresholds for bad behavior, so the answer is "this app is flagged" rather than "here is a number, good luck." Review triage across a portfolio becomes one query instead of twelve inboxes.

## Tools & Capabilities

| Capability | What it does |
|---|---|
| Crash/ANR vitals | Crash and ANR rates compared against Google's bad-behavior thresholds |
| Anomaly detection | Google's own anomaly detections surfaced per app |
| Installs and ratings | Download, rating, and engagement metrics per app and across the portfolio |
| Earnings | Revenue reporting from both stores |
| Reviews | Review reads for triage and reply workflows |
| Portfolio health | Portfolio-wide rollups and cross-app comparisons |

## Installation

```bash
pip install storepilot
storepilot --help
```

Requires Google Play Console API access and App Store Connect API keys, both configured via environment variables.

## Configuration

```json
{
  "mcpServers": {
    "storepilot": {
      "command": "storepilot",
      "args": []
    }
  }
}
```

## Business Relevance

- **Indie developers with multiple apps** replace two dashboards with one agent surface
- **Mobile growth teams** catch crash and ANR regressions before they hit ratings
- **Support and community leads** triage reviews across every app in one session
- **Finance stakeholders** pull earnings by app without login to either console
- **ASO analysts** join vitals, ratings, and reviews into one investigation loop

## Integration with CorpusIQ

StorePilot answers the store-side question (what is happening to my apps on Google Play and the App Store) while CorpusIQ answers the business-side question (what did those apps earn, bill, and cost across Stripe, QuickBooks, and GA4). The composed view: StorePilot surfaces a review spike and a vitals regression, and CorpusIQ shows whether revenue, churn, or support volume moved with them. Both are read surfaces, so neither grants write access to stores or ledgers.

## Limitations

- Brand new listing (Aug 17, 2026), no track record yet
- Requires StorePilot to hold your console and API credentials (review the code before connecting)
- Local stdio server: runs on your machine, not a hosted service
- Young project (1 star at discovery); expect rough edges and fast iteration
- Google Play and App Store only: no Huawei, Galaxy Store, or alternative marketplaces

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
