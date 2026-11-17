---
title: "SpendCanary MCP - Free Google Ads Tools for Agents"
description: "Keyless, stateless Google Ads calculators over Streamable HTTP: eight tools, four driven, and the exact argument names the schema demands."
category: "Advertising / Google Ads"
stars: "0 (public repo spendcanary/mcp-free-tools, created 2026-11-15; eight tools, four driven)"
added: 2026-11-17
source: "the mcpservers.org sitemap shard servers/12.xml (slug spendcanary-com-mcp) and a driven session on 2026-11-17 in which initialize, tools/list and six tools/call requests answered over Streamable HTTP"
relevance: ★★★
tags: [google-ads, ppc, roas, cpc, wasted-spend, landing-page, keyless, remote, mcp]
last_updated: "2026-11-17"
---

# SpendCanary MCP

**Ask an assistant what a Google Ads budget really costs and it will give you a number it invented.** The daily budget is not the daily ceiling, the monthly ceiling is not thirty times the daily budget, and a search terms report is not a list of keywords you bid on. SpendCanary's MCP server answers those three questions from formulas rather than from prose, and it never touches your ad account, so the answer is the same whether you are signed in or not.

This is the cleanest shape a tool server can take: **keyless, stateless, no account, no stored input**, with the arithmetic printed next to the answer. Four of its eight tools were driven this pass, and two deliberately wrong calls returned schema errors that name the exact argument the tool wanted.

```
Server type:   remote Streamable HTTP, stateless (no Mcp-Session-Id issued)
Endpoint:      https://spendcanary.com/mcp
Server:        spendcanary-free-tools, version 1.1.0
Protocol:      2025-06-18
Auth:          none (no key, no account, no OAuth)
Tools:         8
Repository:    github.com/spendcanary/mcp-free-tools (0 stars, created 2026-11-15)
Listed on:     mcpservers.org, sitemap shard servers/12.xml
```

## The evidence tier

**Keyless and driven.** `initialize` answered **200** as *spendcanary-free-tools* **1.1.0** on protocol **2025-06-18**, with **no** session identifier returned and no credential at any point, which is the stateless form. `tools/list` returned **eight** tools with full input schemas, and four of them were called:

- `cpc` with spend **1,200** and clicks **400** answered **$3.00 per click** and echoed both inputs back.
- `roas` with revenue **10,000** and ad spend **2,500** answered **4.00x (400%)** and prompted for `margin_percent` to get a break-even figure.
- `daily_budget_max_spend` with a **100** daily budget answered **200** in one day and **3,040** in a month, naming the **2x** daily and **30.4x** monthly rules.
- `wasted_spend_from_search_terms` on a three-row CSV answered **47% of spend (127.60 of 269.60)** across **2** zero-conversion terms and named both, with clicks beside each.

**The schema is strict, and that is useful.** `roas` called with `sales` returned *revenue: Invalid input: expected number, received undefined*, and `search_partners_cost` called with `search_cost` and `partners_cost` returned the four names it actually wants: `google_search_cost`, `google_search_conversions`, `search_partners_cost`, `search_partners_conversions`. An agent that guesses argument names gets a named refusal rather than a wrong number.

**One integration trap, measured.** A POST with no `Origin` header was refused **403** from this host, and the same POST with `Origin: https://spendcanary.com` answered **200**. Any client that strips Origin has to be given one, or the connector looks broken when it is not.

## Tools & Capabilities

| Tool | Arguments it wants | What it answers |
|---|---|---|
| `check_ad_copy` | `platform` (google, meta), ad text | Character limits and common rejection reasons, per line |
| `daily_budget_max_spend` | `daily_budget` | The **2x** one-day ceiling and the **30.4x** monthly ceiling |
| `roas` | `revenue`, `ad_spend`, optional `margin_percent` | Return on ad spend, with break-even ROAS and profit when a margin is given |
| `cpc` | any two of `spend`, `clicks`, `cpc` | Cost per click, plus CPM and click-through rate when impressions are given |
| `search_partners_cost` | `google_search_cost`, `google_search_conversions`, `search_partners_cost`, `search_partners_conversions` | Cost per conversion on Search against Search Partners, and what partners add monthly |
| `wasted_spend_from_search_terms` | `csv` (a search terms report) | Spend on zero-conversion terms, the costliest terms, and the share of total |
| `check_landing_page` | a public URL | Mobile and desktop load, redirects, a way to call or buy, the Google tag |
| `google_ads_problem_trends` | problem, window | How often each wasted-spend problem appears in public Reddit posts |

Every answer opens with a one-line summary, then the detail, then exactly one link to the matching calculator or guide on the vendor's site, tagged with `utm_source=mcp`.

## Installation

```json
{
  "mcpServers": {
    "spendcanary": { "url": "https://spendcanary.com/mcp" }
  }
}
```

Claude Code: `claude mcp add --transport http spendcanary https://spendcanary.com/mcp`. In a client that asks for authentication, choose **no sign-in**; the server has no auth path to configure.

## Why This Matters for Operators

Paid search is the one budget line where a rounding error compounds monthly. Three of these tools answer questions that normally require either an agency or a spreadsheet: what the real monthly ceiling is, what share of spend went to searches that never converted, and what a cost-per-conversion comparison between Search and Partners implies. Because nothing is stored and no ad account is read, the answers can be pulled into a workflow that touches account data elsewhere without turning this server into a second copy of it.

## Questions operators ask

### Does it read my Google Ads account?

No. The instruction block states it plainly: the calculators work on numbers and text you provide, and the only tool with any outside input is the Reddit trend counter, which reads the vendor's own public counts. There is no OAuth flow to grant.

### Is the arithmetic checkable by hand?

Yes, which is why the numbers above are quotable. 1,200 divided by 400 is 3.00. 10,000 divided by 2,500 is 4.00. A 100 budget at twice the daily rate is 200, and at 30.4 times is 3,040. The wasted-spend answer reconciles both ways: 86.40 plus 41.20 is 127.60, and 127.60 over 269.60 is 47%.

### What does it not do?

It does not manage campaigns, change bids, read spend, or check a live account. It also does not verify that a search terms CSV came from Google rather than a spreadsheet, so the answer is only as good as the export behind it.

## Related

- [Google Ads MCP](/hermes/mcp/servers/external/google-ads-mcp) - the campaign-side surface this calculator set does not replace
- [Markifact Google Ads MCP](/hermes/mcp/servers/external/markifact-google-ads-mcp/) - approval-gated Google Ads writes
- [Ryze Google Ads MCP](/hermes/mcp/servers/external/ryze-google-ads-mcp) - hosted ads reporting
