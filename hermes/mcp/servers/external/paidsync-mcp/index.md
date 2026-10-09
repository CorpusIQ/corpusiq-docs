---
title: "PaidSync MCP - Run Paid Advertising from Your Agent"
description: "Ad operations for agents: 630+ approval-gated tools across Google Ads, Meta, LinkedIn, Microsoft Ads, TikTok, GA4, GTM and more, one endpoint."
category: Advertising & Marketing
stars: n/a (new listing)
added: 2026-10-08
source: "mcpservers.org /all (October 8, 2026 evening sweep)"
relevance: ★★★
tags: [advertising, paid-media, google-ads, microsoft-ads, meta-ads, linkedin-ads, tiktok-ads, ga4, google-tag-manager, campaign-management, approval-gated, remote-mcp]
---

# PaidSync MCP

**Hosted MCP server that runs paid advertising from your assistant** - read, audit and change campaigns across fourteen ad, tag, analytics and feed platforms, with every write previewed by default or held for confirmation. 630+ tools behind one endpoint, free for 15 tasks a month, and a runtime that keeps the tool catalog out of the context window until it is needed.

```
Server type: Remote (Streamable HTTP at https://mcp.paidsync.ai/mcp)
Auth: OAuth 2.0 sign-in (dynamic client registration, PKCE) or an API key header
Tools: 630+ executable tools, lazily loaded (paidsync_context for discovery, paidsync_exec for calls)
Platforms: Google Ads, Microsoft Ads, Meta Ads, LinkedIn Ads, ChatGPT Ads, TikTok Ads, Snapchat Ads, Reddit Ads, Pinterest Ads, X Ads, Google Tag Manager, GA4, Merchant Center, Search Console (read)
Safety: dry_run previews on creates; confirm_destructive gates on deletes, budgets, pauses and uploads; applied changes logged with before/after account data
Pricing: Free for 15 tasks a month; Pro from $99/mo (600 tasks); Team from $249/mo; Done For You custom
Category: Advertising & Marketing
Built by: Advanced Technology Labs LLC (Wyoming) - Meta Business Partner and TikTok Marketing Partner; founder a Google Premier Partner
```

## Why This Matters for Operators

Every ad account leaks the same two ways: spend burns on what nobody watches, and budget stays on yesterday's winner because reallocating it means opening another dashboard. This server closes that gap in chat - audit an account's health, find wasted spend, pause the drifting campaigns, move the budget, and set up conversion tracking across GTM, GA4 and Google Ads in one request, with an approval step in front of every change. The follow-up question that normally needs three tabs ("did the Microsoft cut leak volume to Google, and did GA4 see the shift") runs in the same session.

## Tools & Capabilities

| Platform | Tools | Scope |
|---|---|---|
| Google Ads | 152 | Full read+write: campaigns, ad groups, keywords, ads, Performance Max, audiences, conversions, MCC |
| Microsoft Ads | 152 | Read+write: create Search and Performance Max campaigns (paused), copy campaigns, experiments, ad groups, RSAs, negatives, targeting, UET |
| Meta Ads | 83 | Full read+write: campaigns, ad sets, creatives, custom and lookalike audiences, pixels, lead forms |
| Google Tag Manager | 39 | Read+write: containers, tags, triggers, variables, workspaces, versions, publish |
| LinkedIn Ads | 34 | Read+write: campaign groups, campaigns as drafts, Sponsored Content ads, targeting, budgets |
| ChatGPT Ads | 28 | Read+write over an API key connection |
| GA4 | 26 | Read+write: reports, conversion events, audiences, dimensions, Ads linking, setup audits |
| Merchant Center | 16 | Read+write: feeds and product configuration |
| Snapchat Ads | 15 | Manage existing campaigns: budgets, bids, pause and enable |
| Reddit Ads | 14 | Manage existing campaigns |
| Pinterest Ads | 14 | Manage existing campaigns |
| X Ads | 14 | Manage existing campaigns |
| TikTok Ads | 13 | Manage existing campaigns: budgets, bids, advertiser switching |
| Search Console | 6 | Read: search analytics, query and page performance, index coverage |

Composite tools tie the stack together: `setup_google_ads_conversion`, `setup_ga4_event`, `setup_form_tracking` and `setup_ga4_conversion_tracking` create the GA4 event, build the GTM tag and trigger, and link the result to Google Ads in one prompt.

## Installation

```bash
claude mcp add --transport http paidsync https://mcp.paidsync.ai/mcp
```

```json
{
  "mcpServers": {
    "paidsync": { "type": "http", "url": "https://mcp.paidsync.ai/mcp" }
  }
}
```

claude.ai and Claude Desktop: Settings > Connectors > search PaidSync, or add a custom connector with the URL and sign in (works on every Claude plan). ChatGPT: Plugins > search PaidSync, or developer mode with the URL. Gemini (personal accounts): Connected Apps > custom app. Perplexity: custom connector (Pro and up). Copilot Studio: Tools > Model Context Protocol with OAuth 2.0 dynamic discovery. Cursor and Windsurf take the standard remote server JSON.

## Configuration and Safety

- Every apply waits for a check. In the PaidSync workspace, writes are approval cards by default and applied changes keep an Undo where the platform allows it. Over MCP, creates default to a `dry_run` preview and the destructive set (deletes, budget and pause tools, negative-list applies, editorial appeals, offline conversion uploads) refuses to run without `confirm_destructive`.
- Applied changes are logged, and the change log compares account-level results before and after each change.
- The context window stays light: `tools/list` returns a lean starter set and the full catalog is discovered at runtime through `paidsync_context` and executed through `paidsync_exec` (about 1-2k tokens of schemas instead of 25k+).
- Metering: one tool call is one task, whether it reads a report or updates a budget. Sessions can be revoked at any time.

## Example Prompts

- "Audit my Google Ads account and list the wasted spend from the last 30 days."
- "Pause every Microsoft Ads campaign whose CPA is above $70 in the last 14 days."
- "Move 20 percent of the LinkedIn budget to the campaigns with the best cost per lead this month."
- "Set up conversion tracking for the demo form across GTM and GA4, then link it to Google Ads."
- "Compare ROAS across Google, Meta and LinkedIn in one report, with the numbers from after my last budget change."

## Integration with CorpusIQ

PaidSync acts on the ad platforms; CorpusIQ keeps the business numbers behind them straight. Ask PaidSync for the spend picture and pause the losers, then ask CorpusIQ for revenue, customers and pipeline from Stripe, Shopify, HubSpot or QuickBooks in the same conversation - the ad action and the outcome it should move, one chat, no exports.

## Limitations

- Requires a PaidSync account; applying Google Ads changes needs the OAuth sign-in (an API key works for other platforms).
- Task-metered: 15 free tasks a month, then Pro from $99/mo; a report costs the same as a change.
- Campaign creation is platform-limited: full builds on Google, Microsoft (paused), Meta, LinkedIn and ChatGPT Ads; TikTok, Snapchat, Reddit, Pinterest and X are manage-existing only; on Microsoft it creates Search and Performance Max campaigns paused, and bid strategies stay in Microsoft Advertising.
- Three tools (the two offline conversion uploads and the UET tag key read) run only in Claude, because they carry hashed customer data or an access key (vendor-stated).
- Proprietary managed service - the GitHub repo is documentation, not source.
- Vendor-reported breadth: "the largest MCP tool catalog for advertising" is PaidSync's own claim; the tool totals above come from its published documentation (October 2026).

## FAQ

### Does the agent change live campaigns without asking?

Reads run straight away; writes preview by default (`dry_run`) and the destructive set needs `confirm_destructive` on every dispatch path. Over MCP the final human check is your client's own confirmation prompt, so review the preview before approving.

### How much does it cost to try?

Free: 15 tasks a month on all 14 platforms, no credit card. Paid plans start at $99/mo for 600 tasks; every plan covers every platform, with no per-account charge.

### Does it replace the ad platform UIs?

No. It covers campaign management, builds inside existing campaigns, reporting, audits and conversion tracking; a few things (some campaign types, bid strategy settings, attaching Performance Max audience groups on Microsoft) stay in the platform's own interface.

## See Also

- [Markifact Google Ads MCP - Approval-Gated Google Ads](/hermes/mcp/servers/external/markifact-google-ads-mcp/)
- [Get Ads MCP - 388 Ad Platform Tools for AI Agents](/hermes/mcp/servers/external/get-ads-mcp/)
- [Meta Ads MCP (Official)](/hermes/mcp/servers/external/meta-ads-mcp-official/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
