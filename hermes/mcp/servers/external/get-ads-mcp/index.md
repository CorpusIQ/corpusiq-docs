---
title: "Get Ads MCP - 388 Ad Platform Tools for AI Agents"
description: "Hosted remote MCP server connecting Google Ads, Meta Ads, TikTok Ads, Pinterest Ads, Snapchat Ads, Search Console and GA4 (plus Microsoft Advertising and Reddit Ads) to an AI assistant over one MCP URL. 388 implemented tools with free read-only access, organization-scoped accounts, and write tools that preview the change and apply nothing without confirm: true."
category: Marketing
stars: n/a (new listing)
added: 2026-09-15
source: "mcpservers.org /all page 3 + vendor page at mcpservers.org/servers/get-mcp-ads"
relevance: ★★★
tags: [google-ads, meta-ads, tiktok-ads, ga4, search-console, ad-operations, campaign-management, read-only-free, oauth, remote-mcp]
---

# Get Ads MCP

**Every ad account, one hosted MCP URL.** Get Ads MCP connects Google Ads, Meta Ads, TikTok Ads, Pinterest Ads, Snapchat Ads, Search Console and GA4 to an AI assistant through a single hosted endpoint, with 388 implemented tools across 9 documented sources. The free plan is read-only; paid plans add write tools that preview their change and apply nothing without `confirm: true`.

```
Server type: Remote (Streamable HTTP)
Auth: account selection ticked per source in the organization console
Endpoint: https://mcp.getmcpads.com/mcp
Tools: 388 across 9 sources (Google Ads, Meta Ads, TikTok Ads, Pinterest Ads, Snapchat Ads, Search Console, GA4, Microsoft Advertising 39 tools, Reddit Ads 50 tools pending clarification)
Pricing: free plan read-only; paid plans add preview-gated writes
Category: Marketing / Ad Operations
Built by: Get Ads (getmcpads.com)
```

## Why This Matters for Operators

Ad platforms ship excellent dashboards and terrible export paths, so reporting becomes a manual ritual of screenshots and CSVs, and optimization decisions get made a week after the data mattered. Get Ads removes the export step entirely: the assistant queries the accounts directly and answers "which campaign wasted budget this week" with the numbers in hand.

The governance model is the differentiator. A tool only answers for accounts the organization has ticked; any other identifier is refused, including accounts the underlying connection could otherwise reach. Write tools preview by default: without `confirm: true` the tool describes the change and applies nothing, and writes are refused entirely on the free plan. This is ad-account access with a blast radius the operator controls.

## Tools & Capabilities

| Source | Coverage |
|---|---|
| Google Ads | Campaigns, ad groups, ads, keywords, performance reporting |
| Meta Ads | Campaigns, ad sets, ads, insights |
| TikTok Ads | Campaigns, ads, reporting |
| Pinterest Ads | Campaigns, pins, reporting |
| Snapchat Ads | Campaigns, ads, reporting |
| Search Console | Queries, pages, performance |
| GA4 | Properties, reports |
| Microsoft Advertising | 39 tools, 20 write (sandbox validation supported) |
| Reddit Ads | 50 tools, 19 write (public callability pending Reddit clarification) |

Each connector also exposes a `*_get_setup_guide` tool that documents coverage, prerequisites and live-validation limits, so the agent reads the guide before claiming parity. Write tools are marked (write) and preview their change until confirmed.

## Installation

```bash
npx add-mcp 'https://mcp.getmcpads.com/mcp'
```

Select the authorized accounts per source in the Get Ads console; the free plan keeps everything read-only.

## Configuration

```json
{
  "mcpServers": {
    "getads": {
      "type": "http",
      "url": "https://mcp.getmcpads.com/mcp"
    }
  }
}
```

Account scoping is console-side, not key-side: the token only reaches the accounts the organization has ticked.

## Business Relevance

- **Performance marketers** get cross-platform reporting in one session instead of five dashboards.
- **Finance teams** get weekly budget-versus-spend answers without requesting exports.
- **Agencies** get per-client account scoping with read-only defaults for junior automation.
- **Founders** get campaign oversight in plain language, with writes gated behind explicit confirmation.

## Integration with CorpusIQ

Get Ads and CorpusIQ meet on the same platforms. CorpusIQ's Google Ads and GA4 connectors deliver ads and analytics data with full business context (revenue from Stripe, books from QuickBooks, pipeline from HubSpot). Get Ads adds the multi-platform breadth: TikTok, Pinterest, Snapchat and Microsoft Advertising alongside Google, with organization-scoped, confirm-gated writes. The composed workflow is a weekly review agent that reads performance through CorpusIQ and Get Ads in one session, then drafts the optimization list with previews rather than silently editing live campaigns.

## Limitations

- Writes require a paid plan and are preview-gated; the free plan is strictly read-only.
- Reddit Ads tools are implemented but not publicly callable pending Reddit clarification.
- Account scoping depends on the organization's console selections, which an admin must maintain.
- Commercial hosted service; no self-host option.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
