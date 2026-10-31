---
title: "MonitorBankRates MCP - Deposit and Loan Rate Benchmarks"
description: "Live US deposit and loan rate benchmarks across 8,000+ banks and credit unions, with institution health grades and HMDA lender rankings."
category: Financial Data
stars: n/a (free, no authentication)
added: 2026-10-31
source: "The mcp.so homepage recentServers block on 2026-10-31 at 14:37Z under the slug monitorbankrates, plus a keyless JSON-RPC initialize and tools list against https://mcp.monitorbankrates.com/mcp returning HTTP 200 with eight tools and their full input schemas, and two live tool calls measuring the national 12-month CD average at 3.0101 percent APY on 2026-10-31 across 4,107 institutions and 9,115 quotes, and the national high-yield savings average at 2.0501 percent APY across 271 institutions and 709 quotes"
relevance: ★★★
tags: [bank-rates, deposit-rates, cd-rates, treasury-ops, mortgage, hmda, institution-health, financial-data, keyless]
last_updated: "2026-10-31"
---

# MonitorBankRates MCP

**An operator's cash sits in a bank chosen once and reviewed rarely. This connector turns that account into a measured position: what the rate is today, what it moved in the last week, and how healthy the institution holding the money actually is.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.monitorbankrates.com/mcp
Auth:        none, keyless
Tools:       8 measured live
Cost:        free, attribution requested
```

## What it does

Eight tools over one dataset, and the dataset is the product: every published rate at more than 8,000 US banks and credit unions, recomputed daily rather than sampled.

- `get_best_rates` returns live quotes for one product, nationally, for a state or for a city with local branches first. Products cover CDs by term, savings, money market, checking, mortgages, refinance, home equity, HELOC, auto loans, personal loans and credit cards. Each row carries one best quote per institution with the health grade, minimum deposit, as-of date and a link.
- `get_average_rates` returns the national or state average for a set of keys, with the change over one week, one month and three months, the institution and quote counts, and a daily history.
- `search_institutions` and `get_institution` read the institution directory. The second one returns every deposit and loan rate tracked for one bank or credit union plus the health letter grade, star rating and **Texas ratio**, which is the non-performing-assets measure a treasury reviewer uses when a balance would sit past insurance limits.
- `get_mortgage_lenders` ranks lenders and brokers in a state or city by home loans closed in the latest federal **HMDA** data, with market share, approval share, median loan, programmes, headquarters and health grade.
- `calculate_loan` computes a payment at today's average rate or a rate you pass, for mortgage, refinance with monthly savings and breakeven months, home equity loan, HELOC with both the draw-period and repayment payments and the payment if the rate rises a point, and auto.
- `get_index` serves three proprietary indexes, the **Housing Affordability Index** where 100 means the median household exactly affords the median home at today's 30-year average, and the Home and Auto **Insurance Burden** indexes with state rankings and the cheapest insurer.
- `list_rate_keys` enumerates every accepted product key with its label, group and whether it is measured APY or APR.

## What this pass measured

A keyless `initialize` answered **HTTP 200**, `serverInfo` naming `MonitorBankRates` at version **1.2.0**, and `tools/list` returned all **eight** tools with their full input schemas, so this is a measured surface rather than a card description. Two calls were made:

- `get_average_rates` for `12-month` returned **3.0101** percent APY as of **2026-10-31**, computed across **4,107** institutions and **9,115** quotes, with `change_1w` of **+0.019** and an eight-day history from 2.9911 on 2026-10-24.
- The same call for `high-yield_savings` returned **2.0501** percent APY across **271** institutions and **709** quotes, with `change_1w` of **+0.0033**.

The response carries its own licence string, free to use with attribution and a link to the `url` field, and instructs clients to always show `as_of`. Every rows payload carries the source URL, so a cited number can be traced to the page that published it, which is the property that makes a rate quotable in a board deck at all.

## The operator decision this answers

A business holds operating cash because it needs it liquid, and then stops looking. The default state is that the balance stays at the bank that opened the account at a rate nobody renegotiated, and the money earns less for a year because the review never happens. This connector makes the review a single question with a dated answer: what is the national 12-month CD paying today, what did it pay last week, and which of the institutions offering more than that would a treasury reviewer accept on a Texas ratio.

The second decision is credit. A lender landscape ranked by federal closings, filtered by programme, is the difference between asking one bank for a rate and knowing which banks actually close loans in that state. `calculate_loan` then prices the choice, and the refinance calculator closes the loop by returning the breakeven in months rather than a monthly difference the operator has to interpret.

## Where it sits in this catalogue

The treasury entries already carried here read markets: macro series, Fed and Treasury public data, crypto treasury custody. This one reads the **deposit side of the balance sheet**, at institution level, which is a surface none of them covers. It also stands apart from the mortgage-rate read inside the stock research entries, which reports a rate environment, against this one which names the institutions, their health and their minimums.

## What this pass did not establish

The vendor site itself answered **HTTP 403** to every request from this host, including `/sitemap.xml`, behind Cloudflare, so no pricing page, coverage page or methodology note was read directly and the site being blocked to this crawler is recorded as a bot wall and not as an absence. `change_1m` and `change_3m` came back `null` on both series even though the tool documents them, so month and quarter change are unverified. Coverage claims, the 8,000-institution count and the daily recompute, come from the tool descriptions and the response `note` field rather than an independent audit, and whether the free keyless surface is a permanent term or a launch window is not stated anywhere this pass could read.

## FAQ

### Does it need an API key or an account?
No. `initialize` and `tools/list` answered 200 without credentials, and both `tools/call` requests returned data. The response asks for attribution and a link back to the source URL.

### Are the rates real time or cached?
Each series carries `as_of` and a `cached` flag. The two calls this pass made returned dated values for the current day, `cached: false`, with an eight-day daily history attached.

### Can it move money or open an account?
No. All eight tools are reads and calculators. Nothing in the surface opens an account, moves a balance or submits an application.

### Which products are covered?
CDs from three to forty-eight months and beyond by key, savings, high-yield savings, money market, checking, mortgages by term, refinance, home equity loans, HELOC, auto loans, personal loans and credit cards. `list_rate_keys` is the authoritative list.

### Is it any use outside the United States?
No. The dataset is US banks, credit unions, federal HMDA lender data and US state geography.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - the full catalogue this entry belongs to
- [Paidnice MCP - Accounts Receivable for Xero and QuickBooks](/hermes/mcp/servers/external/paidnice-mcp/) - the receivables side of the same finance stack
- [Backlane MCP - EU Marketplace Seller Ops for Agents](/hermes/mcp/servers/external/backlane-mcp/) - another operator surface keyed to a jurisdiction
