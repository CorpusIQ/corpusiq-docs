---
title: "Appbot MCP - App Review Intelligence for AI Assistants"
description: "Official beta MCP server from Appbot: connect ChatGPT, Claude, Cursor or OpenCode to your App Store and Google Play reviews, ratings, sentiment, topics and feature requests for natural-language product feedback analysis."
category: Data & Analytics
stars: "n/a (closed source)"
added: 2026-08-29
source: mcpservers.org /all
relevance: ★★
tags: [mcp-server, app-reviews, sentiment-analysis, product-feedback, app-store, google-play, oauth, remote-mcp]
---

# Appbot MCP

**Official MCP server from Appbot, the app review intelligence platform, currently in beta.** It connects AI assistants to your Appbot account so natural-language questions return structured customer feedback: reviews, ratings, sentiment, topics, custom topics, emotions, keywords, feature requests and historical trends across the App Store, Google Play and the other stores Appbot supports. Rather than raw review text, the assistant works from Appbot's pre-analyzed feedback intelligence.

```
Server type: Remote (OAuth connector)
Auth: OAuth against your Appbot account
Endpoint: https://api.appbot.co/mcp
Tools: Capability areas below (Appbot does not publish individual tool names for the beta MCP)
Pricing: Requires an Appbot account; the MCP feature adds no fee while in beta
Category: Data & Analytics / Product feedback
Built by: Appbot (appbot.co)
```

## Why This Matters for Operators

App reviews are the fastest feedback channel an app business has, and the slowest to mine: thousands of reviews across two stores, in dozens of languages, with the signal spread across star ratings, text and metadata. Appbot has run this analysis pipeline for over a decade; the MCP hands the structured result to an assistant, so a product manager asks for the top five feature requests of the last 60 days and gets a ranked list instead of a CSV export.

Because the analysis includes sentiment, topics and custom topics, the assistant can answer before-and-after questions about a release: whether the sync bug is fixed or still complained about, which complaint themes appeared after the update, and how sentiment moved against a competitor in the same window.

**A product team gets stakeholder-ready answers from review data without exporting, pivoting or building dashboards.**

## Tools & Capabilities

Appbot does not publish an individual tool list for the beta MCP; the live list is served from the endpoint after OAuth. The documented capability areas and example queries map to:

| Area | Capability |
|---|---|
| Review retrieval | Pull reviews by store, country, date range, star rating and keyword (for example, all 1- and 2-star reviews mentioning "sync" in the last 7 days) |
| Ratings and trends | Average rating by store and window, 1-5 star distributions, month-over-month and release-over-release trends, biggest rating-drop days |
| Sentiment and themes | Sentiment splits and shifts, top complaint topics by volume, clustered themes, reviews that mention a problem despite a high rating |
| Feature requests | Ranked feature requests per app and store over a window |
| Competitor tracking | Rating and sentiment comparisons against competitor apps, praise and complaint deltas |
| Release monitoring | Before-and-after release comparisons, new complaint theme detection, 48-hour negative-review spike flags |

## Installation

The Appbot MCP connects through your AI client's connector flow rather than a CLI. In ChatGPT, create a custom app under Settings - Apps - Advanced Settings - Create app, choose Server URL, enter the endpoint, select OAuth, and sign in with Appbot to authorize. The vendor publishes equivalent walkthroughs for Claude, Cursor and OpenCode; the feature is in beta and requires an Appbot account with connected apps.

## Configuration

```json
{
  "mcpServers": {
    "appbot": {
      "type": "http",
      "url": "https://api.appbot.co/mcp"
    }
  }
}
```

OAuth authorization binds the connection to your Appbot account, so the assistant only sees the review data for apps you already have connected there. On ChatGPT Workspace plans an admin must enable Developer Mode under Settings - Apps before custom apps can be created.

## Business Relevance

- **Product managers** turn review data into ranked feature requests and release-regression answers in natural language.
- **App marketers** watch sentiment and rating trends around each release and flag negative-review spikes.
- **Founders** compare their app against competitors on the reviews that mention both.
- **Support teams** surface the complaint clusters driving negative sentiment before tickets arrive.
- **QA and release teams** verify whether reported bugs are fixed or still complained about after each version.

## Integration with CorpusIQ

Appbot supplies the voice of the customer; CorpusIQ supplies the behavior behind it. A composed workflow: the assistant pulls the top complaint topics for the latest release from Appbot, then reads GA4 funnel drop-off and Shopify subscription churn through CorpusIQ connectors to see which complaints actually cost revenue, and finally joins the two in one thread to prioritize fixes by business impact rather than review volume. CorpusIQ's read-only behavioral data and Appbot's read-only feedback intelligence are complementary inputs to the same product decision.

## Limitations

- Beta feature: connection flows and capabilities may change without notice.
- No published tool names; capability descriptions come from the vendor's example-query docs.
- Requires an Appbot account with connected apps, which is a paid product; the MCP adds no fee while in beta.
- OAuth connector flow only: no API key mode or self-host option documented.
- Read-only by design; review responses and workflow actions stay in the Appbot dashboard.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [PreVibe MCP - SaaS Product Research and Validation for Agents](/hermes/mcp/servers/external/previbe-mcp)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
