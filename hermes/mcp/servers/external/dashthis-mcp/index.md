---
title: "DashThis MCP - Marketing Reports in Chat"
description: "Read your agency dashboards from any assistant: live KPI values, any period, PDF exports and comment writes over OAuth."
category: Marketing Analytics
stars: n/a (new listing)
added: 2026-10-09
source: "mcpservers.org /all pages 1-5 (October 9, 2026 night sweep)"
relevance: ★★★
tags: [marketing, reporting, dashboards, agencies, analytics, kpi, client-reporting, oauth, remote-mcp]
---

# DashThis MCP

**The MCP connector for DashThis, the marketing reporting platform agencies run on** - your assistant lists your dashboards, reads the current value of their widgets for the dashboard's own period or any other, exports a dashboard to PDF for a client, and writes your commentary into a comment box when you ask it to.

```
Connector type: Added from your AI assistant's connector directory (Claude, ChatGPT, GitHub Copilot, Gemini and n8n guides published); OAuth sign-in with your normal DashThis login
Data: 30+ connected sources inside DashThis before the AI sees anything - Google Analytics 4, Google Ads, Search Console, Meta Ads, LinkedIn (Pages and Ads), Bing Ads, Ahrefs, YouTube and more
Reads: Dashboard list with name, group and data source; current widget values; the dashboard's reporting period by default, or any period you name
Writes: Comment boxes only, and only when you ask; it asks before replacing an existing comment and never deletes a dashboard, widget or data source
Exports: Turns a dashboard into a PDF and returns a link, ready to hand to a client
Pricing: The connector is included on every DashThis plan; free trial available
Category: Marketing Analytics
Built for: Agencies and marketing teams reporting to many clients (DashThis reports 18k+ users and 122+ countries)
```

## Why This Matters for Operators

Agency reporting has a last-mile problem: the numbers live in dashboards, but the questions ("which clients' sources are erroring?", "what were sessions last month on the SEO dashboard?", "write this month's recap into the client's comment box") arrive in chat. This connector closes that mile without moving the numbers anywhere new - the metrics are still collected and calculated inside DashThis first, so answers stay consistent with the dashboard a client will see, and the per-client isolation and white-labeling the agency already set up keep holding.

## Capabilities

| Task | What the connector does |
|---|---|
| Find dashboards | Lists the dashboards in the account and tells them apart by name, group and data source |
| Read values | Pulls the current values of a dashboard's widgets; defaults to the dashboard's own reporting period, or a period you name such as last 30 days or last month |
| Export | Turns a dashboard into a PDF and returns a link so a client-ready report can be shared from chat |
| Write commentary | Puts the agreed recap into a comment box on a dashboard for one of its periods, asking before replacing an existing comment |
| Confirm connection | Checks which DashThis account the assistant is connected to before it answers |

Reading and exporting leave dashboards as they are; no dashboard, widget or data source is ever deleted through the connector.

## Installation

Add DashThis as a connector inside your AI assistant and sign in with your normal DashThis login - the connection is secured with OAuth, so no API key or password is pasted anywhere. Step-by-step guides are published for Claude, ChatGPT, GitHub Copilot, Gemini (and Antigravity) and n8n; any client that supports connector or remote MCP settings works the same way. Where you need write access, approve the "Create and change dashboards and data" scope when connecting. Connections are listed under MCP in the DashThis left menu, with last-active times and a reconnect option.

## Configuration and Safety

- OAuth sign-in; the connector only ever sees the DashThis account you connected.
- Reads, exports and the connection check run without scope prompts; writes are limited to comment boxes and happen only when asked.
- A connection created before comment support shipped needs a reconnect to gain the comment scope.
- Notes and current limitations are published at help.dashthis.com/mcp-notes/limitations.
- No public stand-alone endpoint URL is documented; connection is by directory/OAuth.

## Example Prompts

- "Which of my dashboards have a source error right now?"
- "What were the sessions last month on the SEO dashboard, and how does that compare with the month before?"
- "Export the client's monthly dashboard as a PDF and give me the link."
- "Write this recap into the comment box on that dashboard for October: strong organic growth, paid flat, fix the broken conversion tag."

## Integration with CorpusIQ

DashThis answers "how did marketing perform"; CorpusIQ answers "what did the business do about it". Ask DashThis for the channel numbers, then ask CorpusIQ for revenue, customers, pipeline and spend from Stripe, Shopify, HubSpot or QuickBooks in the same conversation - the marketing picture and the business outcome side by side, no exports in between.

## Limitations

- The connector is a DashThis-side integration: capabilities track DashThis's published scope (dashboards, widgets, PDF export, comments), not a general DashThis API surface.
- Data sources must already be connected inside DashThis; the connector does not add new sources.
- Writes are limited to comments; dashboards, widgets and data sources cannot be created or changed through the connector today.
- No public endpoint URL is documented; setup happens from the assistant's connector directory with a DashThis sign-in.
- Feature set is vendor-stated (DashThis help centre and MCP pages, October 2026).

## FAQ

### Does it change my dashboards?

No. It reads and exports; the only write is a comment box, only when you ask, and it confirms before replacing a comment that is already there.

### Which assistants can use it?

Claude, ChatGPT, GitHub Copilot, Gemini (and Antigravity) and n8n have published setup guides; any client that supports connectors or remote MCP settings works the same way.

### Do my clients see anything new?

No. Metrics are still collected and calculated inside DashThis with the same per-client isolation and branding; answers in chat are built from the live values on your dashboards.

## See Also

- [Sitegoalie MCP - WordPress Operations for Agencies](/hermes/mcp/servers/external/sitegoalie-mcp/)
- [Draxlr MCP - SQL Dashboards and Queries for Agents](/hermes/mcp/servers/external/draxlr-mcp)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
