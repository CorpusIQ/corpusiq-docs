---
title: TrueClicks MCP - PPC Audit Intelligence for Agents
description: "Hosted read-only connector to the TrueClicks PPC audit platform for Google, Microsoft and Meta Ads. Agents pull audit results and TrueClicks scores across every connected account, rank issues by wasted spend and severity, surface triggered performance alerts with the campaign-level numbers behind them, and check budget pacing against efficiency targets, all scoped to the signed-in user's accounts over OAuth."
category: Marketing
stars: n/a (hosted connector)
added: 2026-09-07
source: mcp.so feed
relevance: ★★★
tags: [ppc, google-ads, microsoft-ads, meta-ads, audit, budget-monitoring, ad-operations, remote-mcp]
---

# TrueClicks MCP - PPC Audit Intelligence for Agents

**Remote MCP server (Streamable HTTP, OAuth)** - a hosted, read-only connector from TrueClicks (trueclicks.com) that puts the platform's PPC audit and monitoring layer in front of an agent: the agent can ask questions across a whole portfolio of Google, Microsoft and Meta Ads accounts instead of clicking through them one at a time, and it sees only the accounts the signed-in TrueClicks user can already see.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser sign-in with the user's own TrueClicks login; per-user account scoping)
Endpoint: https://data.trueclicks.com/mcp
Tools: Read-only audit, score, alert, budget and performance queries across Google, Microsoft and Meta Ads accounts
Pricing: Requires an active TrueClicks account with at least one connected ad account
Category: Marketing
Built by: TrueClicks (trueclicks.com)
```

## Why This Matters for Operators

PPC account health decays between audits - budget wasted on broken tracking, alerts firing into inboxes nobody triages, and scores dropping silently while the team works on other things. TrueClicks MCP removes the latency: the agent reads the same audit results the platform computes, across every account at once, and explains what changed in plain English. Agencies use it to prep client calls and QA accounts before the client spots a problem; in-house teams use it to hold an agency accountable and to watch accounts they do not touch daily.

**The connector is strictly read-only: the agent can read and analyze data, but cannot change campaigns, budgets, bids or anything inside the ad accounts.** Each user authenticates with their own TrueClicks login, so the agent inherits exactly the account visibility that user already has.

## Tools & Capabilities

| Group | What the agent does |
|---|---|
| Portfolio audits | Pulls audit results across all connected accounts and ranks issues by wasted spend or severity |
| Score forensics | Explains why a specific account's TrueClicks score dropped, then lists the checks behind it |
| Performance alerts | Surfaces triggered alerts and shows the campaign-level numbers behind each one |
| Budget pacing | Checks budget pacing and efficiency targets, and flags accounts heading over or under |
| Task triage | Reviews open tasks by owner or account |
| Ad account queries | Queries campaign, keyword, search term and asset performance directly from Google, Microsoft and Meta Ads |

## Installation

Sign in to TrueClicks with an account that has at least one connected ad account, then add the endpoint to any MCP client that speaks Streamable HTTP.

```bash
claude mcp add trueclicks --transport http https://data.trueclicks.com/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "trueclicks": {
      "type": "http",
      "url": "https://data.trueclicks.com/mcp"
    }
  }
}
```

On first use the MCP client opens a browser window to sign in and authorize against TrueClicks; the connection is then reused for future sessions. The endpoint is OAuth-gated: an unauthenticated probe returns 401 with OAuth protected-resource metadata for the token endpoint.

## Business Relevance

- **PPC agencies** prep client calls and QA accounts portfolio-wide before issues surface in a client meeting.
- **In-house growth teams** watch accounts they do not touch daily and hold agency partners accountable with the same audit data.
- **Marketing operations** get budget pacing and efficiency flags without building dashboard exports.
- **Founders running paid acquisition** get senior-level first-pass diagnosis of wasted spend across Google, Microsoft and Meta.

## Integration with CorpusIQ

TrueClicks reads the health of paid-acquisition accounts; CorpusIQ reads the business those accounts feed. A composed workflow: the agent asks TrueClicks for accounts flagged over or under budget and the issues ranked by wasted spend, then pulls revenue evidence for the same window from CorpusIQ's Stripe, QuickBooks or GA4 connectors - so a wasted-spend finding is weighed against the revenue that account actually produced before anyone touches a campaign. Both systems keep the human as the operator: TrueClicks is read-only by design, and CorpusIQ connectors stay read-only too.

## Limitations

- New to this catalog (mcp.so listing, no public repo or star history to assess - hosted connector).
- Requires an active TrueClicks subscription and at least one connected ad account; the connector adds no data beyond what the platform already holds.
- Strictly read-only - no campaign, budget or bid changes are possible by design.
- Tool names are not published in vendor docs; the live tool list is served from the endpoint after OAuth sign-in (mcp.so's crawler reports no unauthenticated tools).
- Coverage is limited to the ad platforms TrueClicks supports (Google, Microsoft and Meta Ads).

## See Also

- [AdPlug LinkedIn Ads MCP - B2B Campaign Control for Agents](/hermes/mcp/servers/external/adplug-linkedin-ads-mcp)
- [Ryze Google Ads MCP - Hosted Ads Reporting for Agents](/hermes/mcp/servers/external/ryze-google-ads-mcp)
- [Ryze Meta Ads MCP - Hosted Facebook Ads for Agents](/hermes/mcp/servers/external/ryze-meta-ads-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
