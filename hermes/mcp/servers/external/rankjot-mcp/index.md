---
title: "RankJot MCP - Real Google Rankings for AI Assistants"
description: "One-tool MCP server that makes live Google lookups instead of guesses: check_rank(domain, keyword, country) returns the domain's organic position, which page ranks, and the top 10 results in a single call. stdio via uvx rankjot-mcp with a RANKJOT_API_KEY; free accounts include 25 lookups a month. MIT, official MCP registry io.github.epolat/rankjot-mcp."
category: SEO
stars: open source (MIT)
added: 2026-09-14
source: "chatmcp/mcpso issue #4137 (Sep 14) + PyPI rankjot-mcp 0.1.0 verified"
relevance: ★★
tags: [seo, google-rankings, rank-tracking, keyword-tracking, stdio, pypi, mcp-stdio, open-source, mit, free-tier]
---

# RankJot MCP

**Real Google rankings as an MCP tool.** Ask your assistant "where does example.com rank for best running shoes in the UK?" and RankJot makes a live Google lookup instead of guessing. One tool, one job: the current organic position for a domain and keyword, the page that ranks, and the surrounding top 10 - so follow-ups like "who is above me?" need no extra call.

```
Server type: stdio (uvx rankjot-mcp)
Auth: RANKJOT_API_KEY environment variable
Install: uvx rankjot-mcp (PyPI rankjot-mcp 0.1.0, verified)
Registry: io.github.epolat/rankjot-mcp
Pricing: Free accounts include 25 lookups a month
License: MIT
Category: SEO
```

## Why This Matters for Operators

Rank tracking is usually a dashboard: a login, a project setup, a weekly email. RankJot makes it a question. The tool returns structured data an assistant can reason over:

- the domain's 1-based Google organic position (or `null` when it is not in the results checked)
- which of the domain's pages ranks
- the top 10 organic results, for immediate "who is above me" follow-ups
- the remaining monthly quota

Failures come back as data (an `error` field) rather than exceptions, so the assistant can explain what happened instead of dying mid-answer.

## Tool Reference

| Tool | Arguments | Returns |
|---|---|---|
| `check_rank` | `domain`, `keyword`, `country` (default `us`) | Position (1-based or null), ranking page, top 10 organic results, remaining quota |

## Installation

```json
{
  "mcpServers": {
    "rankjot": {
      "command": "uvx",
      "args": ["rankjot-mcp"],
      "env": { "RANKJOT_API_KEY": "rjk_your_key_here" }
    }
  }
}
```

Requires uv (for `uvx`) and a RankJot API key; free accounts include 25 lookups per month. The server is also published in the official MCP registry, so registry-aware clients can install it from the listing.

## Business Relevance

- **Founders** check whether the site actually ranks for the terms the business cares about, without a rank-tracker subscription.
- **Content teams** verify a new page's position days after publishing, in the same session where the page was planned.
- **SEO consultants** sample positions across client domains and countries on demand.
- **Ops leads** get a lightweight quota (25 lookups free per month) that is enough for spot checks and honest reporting.

## Integration with CorpusIQ

A ranking is a leading indicator; revenue is the lagging one. Connect CorpusIQ and the same assistant pairs RankJot positions with the business data behind them - GA4 sessions, Search Console clicks, Shopify orders, Stripe revenue - with source-cited answers, so "we moved from 14 to 6 for this keyword" can be followed immediately by "and here is what that traffic did". For teams that treat SEO as a growth channel rather than a vanity metric, the two answer the question together.

## Limitations

- **One tool, one engine**: Google organic positions only; no other search engines, no historical trend charts.
- **Quota-bound**: 25 lookups a month on the free tier.
- **New and minimal** (PyPI 0.1.0): a small utility, not a full rank-tracking platform.
- **Requires uv/uvx** and a RankJot API key in the client environment.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [Serp Sidekick MCP - Live SEO and AI-Visibility Data for AI Assistants](/hermes/mcp/servers/external/serp-sidekick-mcp/)
- [geolint MCP - AI Search Readiness Linter for Websites](/hermes/mcp/servers/external/geolint-mcp/)
