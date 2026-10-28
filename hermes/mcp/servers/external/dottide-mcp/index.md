---
title: "dotTide MCP - Read Only Numbers for Every Site"
description: "Search Console, GA4, Bing and store numbers for every site you run, across separate Google accounts, from one local read only server."
category: Analytics / SEO
stars: n/a (free, local, read only)
added: 2026-10-28
source: "submission #6274 on the chatmcp/mcpso tracker opened 2026-10-28T05:37:12Z with the nine tool names, the three prompts and the config block, plus the PyPI record for dottide 0.3.1 across three releases; local stdio, so no endpoint exists to probe"
relevance: ★★★
tags: [analytics, search-console, ga4, bing-webmaster, core-web-vitals, multi-site, read-only, local]
last_updated: "2026-10-28"
---

# dotTide MCP

**The reason an owner cannot answer a question across their own sites is not the data. It is that the data lives under three different Google logins, and every tool that reads it assumes one.**

```
Server type: Local (Python, stdio)
Install:     uvx dottide
Auth:        one Google service account, plus optional Bing key
Tools:       9 (sites, search_queries, traffic, opportunities,
             index_health, core_web_vitals, bing_queries,
             store_stats, discover)
Prompts:     3 (Weekly review, What to work on, Index check)
Writes:      none, every scope is read only
```

## Why This Matters for Operators

A portfolio is normal and the tooling is not. A company site, a product site and a side project end up under separate Google accounts because they were created at separate times by separate people, and the console that should compare them only shows one. The result is that the comparison happens in a spreadsheet someone rebuilds every month, or it does not happen.

dotTide's answer is structural rather than clever: one Google service account reads Search Console and GA4 for every site it has been granted, even when those properties sit under different Google accounts, and the same server also reads Bing Webmaster Tools, WordPress.org, Firefox Add-ons and GitHub stats. `discover` finds every property the key can read and writes the configuration, which removes the step where a human types property names wrong.

The second decision is the one that makes it adoptable: every scope is read only. No tool can change a site, Search Console, GA4 or Bing. That is a server you can hand to an agent without a permission argument.

## What It Returns, Verified

This is a local stdio server, so there is no endpoint to drive and no server-side tool list to confirm. What is verifiable is the package and the published surface.

`dottide` is on PyPI at 0.3.1 across three releases, installed with `uvx dottide`, MIT. The submission describes nine tools:

- `sites`, every configured site and whether Search Console, GA4 and Bing access works
- `search_queries`, clicks, impressions, CTR and position by query or page, with period comparison
- `traffic`, GA4 sessions by source and medium, with AI assistant referrals counted separately
- `opportunities`, queries in striking distance, pages and queries losing clicks, low click-through queries
- `index_health`, sitemap errors and the index status of the top pages
- `core_web_vitals`, real-user LCP, INP and CLS plus a lab run, from PageSpeed Insights
- `bing_queries`, Bing Webmaster Tools clicks, impressions and position by query
- `store_stats`, WordPress.org, Firefox Add-ons and GitHub numbers with no key
- `discover`, finds every property the key can read and writes the config

Three prompts ship with it: Weekly review, What to work on, and Index check. Those are the same three questions a small marketing team asks in a Monday stand-up, which is why the server is more useful than a dashboard here.

Two details are worth more than the tool count. AI assistant referrals are counted separately in `traffic`, which is the only way to see whether the assistant answer engines are sending anyone. And the Google credential plus any Bing key are kept in the operating system's secret store (macOS keychain, Windows Credential Manager, Linux Secret Service) rather than in a config file.

## Limits Worth Recording

- **Not driven, only read.** The submission body and the PyPI record are the evidence. No JSON-RPC call was executed, so tool names are as published and response shapes are unknown until first run.
- **Read only is a design claim, not an enforced sandbox.** The scopes are read-only by intent and the credential you supply decides what is actually possible. A service account with write access is still a service account with write access.
- **One service account, shared.** Every site the key can read becomes visible to the server, so scope the key to the properties you want an agent to see rather than to everything the organisation owns.
- **Google Analytics 4 only, and no warehouse.** There is no BigQuery path, no custom dimension modelling and no history beyond what the APIs return.
- **Store stats are public numbers.** WordPress.org, Firefox Add-ons and GitHub are read without a key because they are public, which means they are also not private performance data.

## Wiring It Up

```json
{
  "mcpServers": {
    "dottide": {
      "command": "uvx",
      "args": ["dottide"]
    }
  }
}
```

The setup guide for the service account is `github.com/dotbrainhq/dottide/blob/main/docs/google-setup.md`. Run `sites` first: it reports whether Search Console, GA4 and Bing access works per site, which separates a permissions problem from a data problem before any analysis starts.

## FAQ

### Can it read sites under different Google accounts?

Yes, that is the point. One service account is granted access to each property, so a portfolio spread across separate Google logins reads as one list.

### Does it write anything back?

No. Every scope is read only by design and no tool can change a site, Search Console, GA4 or Bing.

### Where are the credentials kept?

In the operating system's secret store: macOS keychain, Windows Credential Manager or Linux Secret Service, not in the MCP config file.

### Does it cover AI traffic?

Partly. GA4 sessions are broken out by source and medium with AI assistant referrals counted separately, which is the closest a log of referrals gets to assistant visibility.
