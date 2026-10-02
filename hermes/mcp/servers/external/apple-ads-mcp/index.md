---
title: Apple Ads MCP - App Store Campaign Operations
description: "Local-first MCP server for the Apple Ads Platform API v1: typed read-only research tools plus receipt-gated App Store campaign operations, installed as a Go binary via Homebrew."
category: Marketing
stars: 3
added: 2026-08-29
source: mcpservers.org /all page 3
relevance: ★★
tags: [mcp-server, apple-ads, app-store, campaign-management, aso, search-ads, advertising, local-tools]
---

# Apple Ads MCP

**A local-first MCP server for the Apple Ads Platform API v1 that gives Codex, Claude, and other MCP clients typed tools to research, inspect, and safely operate App Store advertising accounts.** The server is read-only by default: credentials stay on the local machine, every account-scoped call names an explicit profile and ad account, and every mutation requires a preview plus a short-lived single-use receipt. Built in Go, distributed as a Homebrew binary.

```
Server type: Local (stdio) - Go binary via Homebrew
Auth: Apple Ads Platform API private key, stored locally by profile
Endpoint: n/a (local process; talks to Apple Ads Platform API v1 directly)
Tools: 24 (server_info, account_health, campaign/keyword/creative queries, receipt-gated operations)
Pricing: Free open source (MIT); Apple Ads spend is your own account
Category: Marketing / App Store Advertising
Built by: zelentsov-dev/apple-ads-mcp; MIT
```

## Why This Matters for Operators

App Store ad accounts are where a wrong bulk edit costs real money in minutes, which is why most tools hide write access behind a web console and nobody trusts an agent with it. Apple Ads MCP solves that with an explicit safety ladder: read-only research tools are always available, mutations go through a preview plus a single-use receipt, and every call scopes itself to an explicit profile and ad account so an agent can never silently touch the wrong account.

Because it runs locally against your own private key, no third party ever sees the credentials or the account data - a meaningful difference from SaaS connectors that proxy your ad accounts through their infrastructure.

**Safe App Store campaign operations with receipts, local credentials, and read-only-by-default posture.**

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `server_info` | Server and API version information |
| `auth_check` | Validate the local credential profile against Apple |
| `account_health` | Account-level health and eligibility readout |
| `ad_accounts_list`, `ad_account_get` | Enumerate and read ad accounts for the profile |
| `apps_search`, `apps_get`, `apps_eligibility` | Find apps to advertise and explain eligibility gaps |
| `campaign_inventory`, `campaigns_query`, `ad_groups_query`, `ads_query` | Read campaign structure and inventory |
| `keywords_query`, `negative_keywords_query`, `keyword_suggestions` | Keyword research and negative management |
| `creatives_query`, `shared_budgets_query` | Creative and budget reads |
| `app_locale_details`, `app_store_geo_search`, `supported_app_languages` | Locale and geo research |
| `operations_apply`, `operations_inspect`, `operations_verify` | Receipt-gated mutation pipeline (preview, inspect, commit) |

## Installation

```bash
brew install zelentsov-dev/tap/apple-ads-mcp
apple-ads-mcp config init
apple-ads-mcp auth doctor --profile production-read-only
```

Register with an absolute Homebrew path so desktop apps and IDE extensions do not depend on the shell PATH. Codex: `codex mcp add apple-ads -- "$(brew --prefix)/bin/apple-ads-mcp" serve --stdio`. Claude Code: `claude mcp add --scope user apple-ads -- "$(brew --prefix)/bin/apple-ads-mcp" serve --stdio`.

## Configuration

```json
{
  "mcpServers": {
    "apple-ads": {
      "command": "/opt/homebrew/bin/apple-ads-mcp",
      "args": ["serve", "--stdio"]
    }
  }
}
```

Profiles store the absolute path of an Apple Ads private key - the README explicitly warns never to paste the private key into a chat, issue, or repository. Start read-only, then enable writes per profile only when the receipt flow is understood.

## Business Relevance

- **App marketers** audit campaign structure and keyword coverage from chat without touching the Ads console.
- **Agencies** run per-client profiles with explicit ad-account scoping, cutting cross-account mistakes.
- **Indie developers** get ASO and Search Ads research locally with no vendor seeing their credentials.
- **Teams wary of agent writes** keep the read-only default and grant mutations through the receipt flow deliberately.

## Integration with CorpusIQ

Apple Ads MCP fills the paid-app-install gap in CorpusIQ's marketing data stack: CorpusIQ already pulls GA4 signup attribution and organic search visibility, and this server adds the App Store paid-acquisition surface - locally, so the ad account credentials never leave the operator's machine. A CorpusIQ workflow can cross-check Apple Ads keyword and campaign reads against GA4 conversion data from the CorpusIQ connectors, so the operator sees which paid App Store terms actually become signups, and keeps organic ASO and paid Search Ads in one analysis.

## Limitations

- Brand new - first sweep August 29, 2026; 3-star repo, single maintainer.
- Local binary only - no hosted endpoint, so remote/cloud agent runtimes need the binary installed where they run.
- Apple Ads Platform API v1 scope only; no web console features like Apple Ads Manager bulk tools.
- Write operations require learning the receipt flow - deliberate friction by design.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Otto MCP - Live Marketing Data and Website Operations in Chat](/hermes/mcp/servers/external/otto-mcp)
- [Google Ads MCP - Campaign Management for Agents](/hermes/mcp/servers/external/google-ads-mcp)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
