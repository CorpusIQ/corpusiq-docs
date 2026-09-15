---
title: Ryze Google Ads MCP - Hosted Ads Reporting for Agents
description: Hosted Google Ads MCP server from Ryze AI. Connects Claude, ChatGPT and Cursor to Google Ads with one OAuth login. Fourteen tools cover GAQL reporting, Keyword Planner research, recommendations and approval-gated campaign changes with no developer token required.
category: Marketing
stars: n/a (new listing)
added: 2026-09-04
source: mcpservers.org
relevance: ★★★
tags: [google-ads, advertising, gaql, keyword-planner, marketing-ops, oauth, streamable-http, remote-mcp]
---

# Ryze Google Ads MCP

**Remote MCP server (Streamable HTTP, OAuth 2.0)** - a hosted Google Ads connector from Ryze AI that turns a Google Ads account into 14 agent tools with one sign-in. No developer token, no Cloud project, nothing to install. The same endpoint also carries Meta Ads, TikTok, GA4, Search Console and Shopify toolsets.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.0 (Google sign-in, one Ryze workspace per connection)
Endpoint: https://connector.get-ryze.ai/mcp
Tools: 14 (8 read, 6 write, approval-gated)
Pricing: Free to connect · Ads Autopilot $89/mo flat (optional)
Category: Marketing
Built by: Ryze AI (2,000+ clients, 700+ agencies, $500M+ managed)
```

## Why This Matters for Operators

The alternative to this server is the developer route: apply for a Google Ads API developer token, stand up a Cloud project with an OAuth consent screen, run a local Python process and babysit a client_secret.json. Ryze collapses all of that into a URL and a Google sign-in. **An operator gets GAQL reporting, Keyword Planner data and Google's own recommendations inside a chat in about sixty seconds.**

Write tools are approval-gated by default, so an agent can propose a budget change without ever being able to apply it silently. Deletes run through a separate explicit tool that only accepts an item-by-item approved list. For agencies the server is MCC-aware: it discovers every accessible customer, maps a manager to its child accounts and passes loginCustomerId through, so one connection covers the whole book of business.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `getAccountSummary` | Spend, clicks, conversions, CPA and ROAS for a date range in one call |
| `getAccountHierarchy` | Manager to sub-account tree for an MCC |
| `listAccessibleCustomers` | Every Google Ads account the signed-in login can reach |
| `listConversionActions` | Conversion actions with status, category and counting settings |
| `listRecommendations` | Google's optimization recommendations with estimated impact |
| `applyRecommendation` | Apply recommendations by resource name (write, gated) |
| `dismissRecommendation` | Dismiss recommendations so Google stops resurfacing them (write, gated) |
| `generateKeywordIdeas` | Keyword Planner ideas with monthly volume from seed keywords or a URL |
| `generateKeywordHistoricalMetrics` | Volume, competition and bid ranges for a known keyword list |
| `runRawGaql` | Any GAQL query up to 10,000 characters against reporting resources |
| `runRawMutate` | Create or update campaigns, budgets, ad groups, criteria and assets (write, gated) |
| `runRawMutateDelete` | Remove resources on an explicit item-by-item approved list (write, gated) |
| `runRawCustomAudienceMutate` | Create or update custom audiences for targeting and PMax signals (write, gated) |
| `uploadImageAsset` | Push an image asset into the Asset Library for PMax and responsive display |

## Installation

```bash
claude mcp add --transport http ryze https://connector.get-ryze.ai/mcp
```

Then run `/mcp` inside Claude Code to complete the OAuth sign-in. The vendor publishes per-client walkthroughs for Claude web and desktop, ChatGPT developer mode, Cursor, Windsurf, VS Code and Gemini CLI.

## Configuration

```json
{
  "mcpServers": {
    "ryze": {
      "url": "https://connector.get-ryze.ai/mcp"
    }
  }
}
```

Auth notes: sign in with Google and pick a Ryze workspace. The hosted server brings its own Ads API access, so no developer token or client_secret.json exists anywhere in the loop. One connection maps to one workspace, so agencies with several client workspaces reconnect per workspace.

## Business Relevance

- **Paid-marketing leads** get campaign spend, CPA and ROAS pulled on demand and broken down by campaign in plain language, no Ads UI export dance.
- **Performance agencies** run MCC-aware reporting and pass loginCustomerId so one login serves every client account.
- **Media buyers** research keywords with real volume and bid-range data before the account manager opens a budget request.
- **Operator teams** keep every write approval-gated per tool, so agent-driven changes stay human-signed.

## Integration with CorpusIQ

CorpusIQ already exposes Google Ads as one of its 40+ read-only connectors, which is the right surface for financial and cross-system reporting. Ryze complements it on the action side. When a CorpusIQ dashboard flags a campaign with rising spend and falling ROAS, the operator hands the flagged dimensions to Ryze, which pulls the GAQL report, reads Google's recommendations and drafts an approval-gated budget or bid adjustment. The pattern is clean: CorpusIQ reads the business, Ryze acts on the ads account with the operator signing off each write.

## Limitations

- Write tools mutate live ad accounts; approval gates are a default, not a guarantee. Review every proposed change.
- Connections are workspace-scoped, so multi-client agencies reconnect per workspace.
- Requires a Claude plan with custom connectors (Pro or above) or a paid ChatGPT plan for connector support.
- The optional Ads Autopilot tier ($89/mo) is where hands-off optimization lives; the free tier is reporting and gated writes only.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [SellerMate MCP - Amazon Ads Operations for AI Agents](/docs/hermes/mcp/servers/external/sellermate-mcp)
- [Lifesight MCP - Unified Marketing Measurement and MMM](/docs/hermes/mcp/servers/external/lifesight-mcp)
