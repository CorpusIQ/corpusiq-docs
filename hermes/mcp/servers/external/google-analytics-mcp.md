---
title: Google Analytics 4 MCP Server Integration Guide
description: AI-powered Google Analytics 4 access — pull reports, monitor realtime traffic, and manage GA4 properties directly from Hermes Agent. Built in Rust for performance.
category: mcp
tags: [mcp, google-analytics, ga4, analytics, reporting, web-analytics, marketing, hermes-agent]
last_updated: 2026-07-21
---

# Google Analytics MCP — Web Analytics for Hermes Agent

Google Analytics MCP connects your AI agent to Google Analytics 4 — run reports, monitor realtime traffic, and manage properties without opening the GA4 dashboard. Built in Rust for fast report processing.

## What It Does

Google Analytics MCP brings GA4 data into your agent workflow:

- **Report generation** — Run custom GA4 reports with dimensions and metrics
- **Realtime monitoring** — See active users, page views, and events happening right now
- **Property management** — List and manage GA4 properties and data streams
- **Audience insights** — Pull audience demographics, acquisition channels, and behavior flows
- **Conversion tracking** — Monitor goal completions and ecommerce events

## Quick Setup

### Prerequisites
- **Google Analytics 4 property** set up with data flowing
- **Google Cloud project** with Analytics Data API enabled
- **Service account** with Viewer access to your GA4 property
- **Rust toolchain** (`cargo build` required)

### Add to Hermes Agent

```bash
git clone https://github.com/codeChap/mcp-server-google-analytics
cd mcp-server-google-analytics
cargo build --release
```

```json
{
  "mcpServers": {
    "google-analytics": {
      "command": "path/to/mcp-server-google-analytics/target/release/google-analytics-mcp",
      "env": {
        "GA4_PROPERTY_ID": "properties/123456789",
        "GOOGLE_APPLICATION_CREDENTIALS": "/path/to/service-account-key.json"
      }
    }
  }
}
```

## Key Capabilities

| Tool | Description |
|------|-------------|
| `run_report` | Run a custom GA4 report with dimensions, metrics, date range, and filters |
| `get_realtime` | Get realtime active users, page views, and events |
| `list_properties` | List all GA4 properties accessible to the service account |
| `get_property` | Get property details including data streams |
| `run_funnel_report` | Analyze conversion funnel performance step-by-step |
| `get_audience_overview` | Demographics, geo, device, and acquisition channel breakdown |
| `get_page_metrics` | Page-level metrics: views, bounce rate, avg engagement time |
| `get_conversion_events` | List and count conversion events by name |

## Use Cases for Business Operators

### 1. Daily KPI Summary
Get your key metrics without opening a dashboard:

```
Agent prompt: "Give me yesterday's GA4 summary: users, sessions,
conversion rate, top 5 landing pages, top 3 traffic sources,
and revenue if ecommerce is tracking. Compare to the same day last week."
```

### 2. Campaign Landing Page Analysis
Check if your ad traffic converts:

```
Agent prompt: "I just launched a Google Ads campaign driving traffic
to /promo. Pull this page's metrics for today: entrances, bounce rate,
avg session duration, and conversion rate. How does it compare to
the site average?"
```

### 3. Content Performance Audit
Find what content actually works:

```
Agent prompt: "Show me the top 20 blog posts by organic traffic this month.
For each, show: page views, avg engagement time, and conversion rate.
Sort by conversions per 1,000 views. Flag any posts in the top 10
by traffic that have below-average conversion rate — those need CTAs."
```

### 4. Realtime Launch Monitoring
Watch a product launch or campaign go live:

```
Agent prompt: "We just sent the email blast at 10 AM. Monitor GA4 realtime
for the next 30 minutes. Alert me if active users spike above 500,
or if the /launch page error rate goes above 2%."
```

## Integration with CorpusIQ

Google Analytics MCP + CorpusIQ = complete analytics operations:

1. **CorpusIQ Google Ads connector** → correlate ad spend with on-site engagement
2. **CorpusIQ Search Console connector** → match organic queries to landing page performance
3. **CorpusIQ Stripe connector** → connect GA4 conversion events to actual revenue
4. **CorpusIQ CRM connector** → track lead quality from source → session → deal

This creates a single-pane view where your agent answers "which channel produces the highest-value customers?" by joining GA4 attribution data with Stripe revenue and CRM pipeline data.

## Pricing

- **Google Analytics MCP:** Open source (MIT), free
- **Google Analytics 4:** Free (standard properties), Analytics 360 for enterprise ($50K+/year)
- **Analytics Data API:** Free within quota limits (typically 50,000 requests/day for core reporting)

## Limitations

- GA4 API has daily quota limits — batch large historical pulls
- Realtime API has limited dimensions vs standard reports
- Service account setup requires Google Cloud Console access
- Rust build required
- Does not support Universal Analytics (UA) — GA4 only

---

*← [External MCP Catalog](/hermes/mcp/servers/external/) | [MCP Overview](/hermes/mcp/)*
