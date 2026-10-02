---
title: Ryze Meta Ads MCP - Hosted Facebook Ads for Agents
description: Hosted Meta Ads MCP server from Ryze AI. Connects Claude, ChatGPT and Cursor to Facebook and Instagram ads with one OAuth sign-in. Twelve tools cover Insights reporting, Graph API reads, lead forms, Ad Library search and approval-gated campaign writes with no developer app required.
category: Marketing
stars: n/a (new listing)
added: 2026-09-05
source: mcpservers.org
relevance: ★★★
tags: [meta-ads, facebook-ads, advertising, instagram, insights, ad-library, oauth, streamable-http, remote-mcp]
---

# Ryze Meta Ads MCP

**Remote MCP server (Streamable HTTP, OAuth 2.0)** - a hosted Meta Ads connector from Ryze AI that turns Facebook and Instagram ad accounts into 12 agent tools with one Facebook sign-in. No Meta developer app, no Marketing API access token, nothing to install. The same endpoint also carries Google Ads, TikTok, GA4, Search Console and Shopify toolsets.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.0 (Facebook sign-in, tokens exchanged and refreshed server-side)
Endpoint: https://connector.get-ryze.ai/mcp
Tools: 12 (9 read, 3 write, approval-gated)
Pricing: Free to connect · Ads Autopilot $89/mo flat (optional)
Category: Marketing
Built by: Ryze AI
```

## Why This Matters for Operators

The self-hosted alternative is the developer route: create a Meta app, run through app review, obtain a Marketing API token, and babysit a local Python process. Ryze collapses all of that into a URL and a Facebook sign-in. **An operator can ask "which of my ads wasted the most money this month" and get the Insights breakdown inside a chat in about a minute.**

Write tools are approval-gated per tool, so an agent can propose a budget shift without being able to apply it silently. Deletes and archives run through a separate explicit tool, which makes accidental removal of a live campaign a two-step, human-approved operation. The same login also unlocks the Google Ads, TikTok, GA4, Search Console and Shopify toolsets, so one connection replaces six connectors.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `getAccountSummary` | Spend, impressions, CPM, CTR, conversions and ROAS for a date range on Meta's default attribution window |
| `listAdAccounts` | Every ad account the signed-in user can reach, with id, name and currency; call this first |
| `getCreative` | One creative by id: copy, media, links, object_story_spec and status |
| `listCreatives` | Creatives in an account, paged to avoid rate-limit flags on large accounts |
| `runRawInsights` | Reporting at account, campaign, ad set or ad level with breakdowns by age, gender, country, region, device, platform and placement, plus attribution windows |
| `runGraphRead` | Any Graph API node or edge: campaigns, ad sets, ads, creatives, audiences, targeting search, with pagination cursors followed automatically |
| Lead-form tools (2, read) | List the lead forms on a Facebook Page and export the leads each form collected, straight into the chat |
| Ad Library search (1, read) | Search Meta's public Ad Library by keyword or Page ID, filtered by country and active status, with a snapshot link per ad |
| Creative tooling (2, read) | Inspect any creative's copy, media and links; upload images by URL to get the image_hash a new ad needs |
| Write tools (3, approval-gated) | Create and update campaigns, ad sets, ads, creatives and budgets through per-tool approval; deletes and archives use a separate explicit tool |

## Installation

```bash
claude mcp add --transport http ryze https://connector.get-ryze.ai/mcp
```

Then run `/mcp` inside Claude Code to complete the Facebook sign-in. The vendor publishes per-client walkthroughs for Claude web, ChatGPT, Cursor and other MCP clients.

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

Auth notes: sign in with Facebook and pick a Ryze workspace. The hosted server exchanges and refreshes tokens server-side, so no developer app, access token or app review exists anywhere in the loop. One connection maps to one workspace.

## Business Relevance

- **Paid-social operators** get spend, CPM, CTR, conversions and ROAS on demand with breakdowns by age, gender, country, region, device and placement, no Ads Manager export dance.
- **Media buyers** read any Graph API surface - campaigns, ad sets, creatives, audiences and targeting search - through one natural-language interface.
- **Competitor monitoring** uses Ad Library search by keyword or Page ID to track what rival brands are running, filtered by country and active status.
- **Lead operations** pull lead-form submissions straight into the chat for follow-up and CRM entry.
- **Agencies** keep every write approval-gated per tool, so agent-driven changes stay human-signed.

## Integration with CorpusIQ

CorpusIQ reads the business - GA4, Shopify, Stripe and the rest of the 40+ connectors - while Ryze Meta Ads acts on the ads account. When a CorpusIQ dashboard shows a Meta campaign with rising CPM and falling ROAS, the operator hands the flagged dimensions to Ryze, which pulls the Insights breakdown, inspects fatiguing creatives and drafts an approval-gated budget or creative swap. The pattern is clean: CorpusIQ reads the business, Ryze acts on the ad account with the operator signing off each write.

## Limitations

- Write tools mutate live ad accounts; approval gates are a default, not a guarantee. Review every proposed change.
- Connections are workspace-scoped, so multi-client agencies reconnect per workspace.
- Requires a Claude plan with custom connectors (Pro or above) or a paid ChatGPT plan for connector support.
- Meta API rate limits still apply; the paged listCreatives design exists to avoid flagging large accounts.
- The optional Ads Autopilot tier ($89/mo) is where hands-off optimization lives; the free tier is reporting and gated writes only.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [Ryze Google Ads MCP - Hosted Ads Reporting for Agents](/hermes/mcp/servers/external/ryze-google-ads-mcp)
- [SellerMate MCP - Amazon Ads Operations for AI Agents](/hermes/mcp/servers/external/sellermate-mcp)
- [Tracetify MCP - SEO, GEO and Growth Reports for Agents](/hermes/mcp/servers/external/tracetify-mcp)
