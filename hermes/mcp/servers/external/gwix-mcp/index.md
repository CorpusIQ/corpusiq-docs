---
title: "GWIX MCP - Pay, Hiring and Workforce Data With Provenance"
description: "A labour-market data exchange as tools: median and percentile pay, job-ad volume, hiring demand, talent supply and turnover across countries, every figure carrying its source and release, with a keyless sample server to test first."
category: Business Operations
stars: n/a (credit-based, $250 free)
added: 2026-10-31
source: "The mcp.so homepage recentServers block on 2026-11-01 at 00:15Z under the slug global-wholesale-intelligence-exchange-gwix, filed 2026-10-31 at 18:49:44Z; JSON-RPC initialize, tools/list, get_data_status and get_pay against https://api.gwix.ai/mcp/sample; keyless 401 probes on https://api.gwix.ai/mcp and /v1/mcp; and HTTP reads on gwix.ai, gwix.ai/mcp and gwix.ai/pricing"
relevance: ★★★
tags: [labor-market, compensation-data, salary-benchmarks, hiring-demand, workforce, provenance, official-statistics, credit-pricing, sample-tier, remote-mcp]
last_updated: "2026-10-31"
---

# GWIX MCP

**Every operator makes pay decisions with a number someone remembers. This connector answers the same question from official statistics and job ads in the same response, with the source, the release and the period attached to each figure, so the number can be defended instead of repeated.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://api.gwix.ai/mcp          (OAuth or API key)
             https://api.gwix.ai/mcp/sample   (keyless, data 6 months behind)
Auth:        Bearer API key or OAuth on the live server; none on the sample
Tools:       27 on the sample surface, 13 documented on the public MCP page
Pricing:     $250 of free credits (5,000) for 12 months; packs from $500 to $2,000
Coverage:    247 countries claimed; sample covers US, UK and Germany
```

## What it does

The tool list is organised the way a compensation question actually arrives. A person asks about a job in a place, and one of the report tools answers in prose with charts: `salary_and_hiring_report`, `hiring_demand_report`, `labor_market_report`, `company_hiring_report`, `talent_supply_report`, `workforce_turnover_report`, `workforce_representation_report`, `pay_by_experience_level`, `pay_by_industry_or_setting`, `compare_pay_by_location` and `explain_pay_figures`. Then there are the decision tools, `job_offer_check` for judging an offer against the market and `get_job_summary` for the fast headline, and beneath them the builder tools that return rows rather than prose: `get_pay`, `get_postings`, `find_id`, `describe_id`, `job_title_lookup`, `map_occupation_code`, `list_dimensions`, `list_periods`, `get_fx_rates`, `get_data_status`, `read_guide` and `get_account_usage`.

`tools/list` on the sample returned **27** tools in 37,580 bytes, so the surface here is measured rather than quoted. `read_guide` is the tool most catalogues lack: it serves the definitions, the sample minimums and the wording rules, which is how a caller learns that a row with too few ads is suppressed instead of being read as zero.

## What this pass measured

The live endpoint answered a keyless `initialize` with **HTTP 401**, JSON-RPC error `-32001`, message `Authentication required: sign in with OAuth or send a GWIX API key as a Bearer token.` A second probe on `/v1/mcp` returned a different 401 shape, an RFC 7807 problem body with `code: unauthorized` and a `request_id` of `gwx_req_3111842cfb933878`, which means the public API and the MCP server sit on different routers and both require a credential. The vendor publishes a keyless sample at `https://api.gwix.ai/mcp/sample`, and that is where the measurements come from: `initialize` returned **HTTP 200** in 0.22 seconds, `protocolVersion` `2025-06-18`, `serverInfo` name `gwix`, and its own instructions state the terms plainly: no sign-in, data lagged about six months, a few questions a day.

`get_data_status` for the US returned `status: "operational"`, `release: "2026-W41"`, `last_complete_week: "2026-04-12"`, no degraded endpoints, and a sample block stating `lag_months: 6`, `history_start: "2024-10-14"`, and coverage as "United States, United Kingdom and Germany; all occupations combined, job families and 25 common occupations; and the specialist roles within those occupations; market level (no company or industry splits); data lagged 6 months."

`get_pay` for SOC **47-2111** (Electricians) in metro `mtr_midland_tx`, quarterly, 2026-Q1, returned in 0.26 seconds with a period running 2025-12-29 to 2026-03-29, `coverage_status: "covered"`, `ads_with_pay: 74`, and percentiles of **p10 38,215, p25 48,368, p50 66,781, p75 76,526 and p90 94,694** USD per year. That median is the same figure GWIX publishes in its own free sample answer on the homepage for the same occupation, place and quarter, which makes this a verified surface rather than a plausible one: the server reproduces the number the vendor advertised.

The metadata is where the trust argument lives. Periods are defined as "13-week quarters of whole Monday to Sunday weeks, ending on the last Sunday on or before the quarter's last day". Currency handling is explicit: values are computed in each country's currency and converted at the period average, with `fx_rate` returned per row so the local figure can be recovered. The occupation crosswalk routes every code to US SOC 2018 and states that a partial match covers only part of the SOC and that "each SOC is a separate row set, never pooled".

`job_offer_check` failed. The call returned a CloudFront **504** gateway timeout after 30.07 seconds. The row-level tools answered in under 0.3 seconds and the generative report path did not, which is the cost structure of this class of server: the data reads are cheap and fast, the written analysis is the slow and expensive half.

## The containment worth reading twice

The sample tier is bounded in three directions at once and says so: six months of lag, three countries, and a fixed slice of occupation granularity with no company or industry splits. That is enough to test definitions and output shapes and not enough to make a live compensation decision, which is the correct shape for a free tier on a data product.

The second containment is provenance on every row. Percentiles arrive with `ads_with_pay`, `coverage_status`, `fx_rate`, the crosswalk basis, the period definition and the dataset's `last_complete_week`, and the licence line on the site asks for the source to travel with the figure. A pay number without an ad count and a release date is an anecdote; this returns the ingredients that let a reviewer reject it.

## The operator decision this answers

Three decisions, in ascending order of consequence. What to offer a new hire, which is the `job_offer_check` question and the one most often answered by a single data point from a friend. What a role costs in a second location, which is `compare_pay_by_location` and decides whether a team is built in one metro or two. And whether the market for a role is tightening, which is `get_postings` volume plus `change` over time, and is the difference between hiring now and restructuring the work.

The reason official statistics alone are not enough is the same reason job ads alone are not: BLS tells you what people are paid and job ads tell you what employers are asking to pay, and the gap between them is where an operator either gets a bargain or loses a candidate. GWIX returns both in one response, which is the only way that gap gets computed rather than argued about.

## Where it sits in this catalogue

The hiring entries here are job boards and applicant tooling, and none of them is a statistics exchange:

- [Jobyap MCP](/hermes/mcp/servers/external/jobyap-mcp/) and the other job surfaces find candidates and roles, which is supply and demand in listings rather than pay percentiles from official surveys.
- [Foundrole MCP](/hermes/mcp/servers/external/foundrole-mcp/) and the recruiting entries work the pipeline, not the benchmark.
- The company and financial intelligence entries read filings and revenue, not workforce composition.
- The payroll entries compute what a named employee is paid; GWIX says what the market pays for the role.

The distinction worth stating: a payroll connector tells you what you spent, a job board tells you who is available, and this tells you what the market rate is with the evidence behind it. Only the third one settles an argument about a raise.

## What this pass did not establish

Everything about the live surface is documentation. The 27-tool list is the sample's, the live server answered 401 to two different probes, and no credential was issued, so `ask_gwix`, the report tools, `get_account_usage` and the credit accounting are unmeasured. `job_offer_check`, the tool closest to a decision, returned a 504 rather than an answer, so the report-generation path is unverified in this pass.

The economics are read from the pricing page and not observed: credits are set by the rows returned and the credits per row by the complexity of the analysis behind them, calls returning no data are free, a row costs the same whether one source or several supply it, and every response is supposed to show credits used and remaining balance. What a typical question costs in credits is the number an operator needs and this pass could not produce it.

Also unverified: the 247-country coverage claim (the sample states three countries and the site says coverage is live for pay, hiring demand, companies, occupations and workforce statistics with financial and economic sources to follow), whether the six-month sample lag is a launch arrangement or permanent, and whether a partially matched occupation code can silently narrow a benchmark, which the metadata says it cannot because each SOC is a separate row set but which a live multi-code call would prove.

## FAQ

### Does it need an API key?
The live server does: `https://api.gwix.ai/mcp` returned 401 with an OAuth-or-key challenge on the first request. The sample server at `https://api.gwix.ai/mcp/sample` needs nothing, and answers a few questions a day with data about six months behind.

### Is the sample good enough to quote a number?
Not for a live decision. It is good enough to test definitions, tool shapes and crosswalk behaviour, and the median it returns for a published example matches the vendor's own published figure, which is what makes the surface verifiable.

### What does it cost?
$250 of free credits, 5,000 of them, valid 12 months, with 20 free Ask GWIX answers and no card. Packs are $500 for 10,000 credits, $1,500 for 50,000 and $2,000 for 100,000. Credits are set by the rows you receive and the complexity behind each row, and calls that return no data are free.

### Where does the pay data come from?
Official statistics and job ads, held as separate series. The free sample answer on the vendor site shows both for one occupation and place: the BLS OEWS median of about $59,530 for May 2025 against a GWIX job-ad median of $66,781 for 2026-Q1, roughly 12 percent above. The row-level tool returns the advertised series with its ad count, and the metadata carries the period definition and the release.

### Why did a report tool time out?
`job_offer_check` returned a CloudFront 504 after 30 seconds while the row tools answered in under a third of a second. Written analysis is the expensive path; plan for a client timeout of at least 60 seconds on the report tools, or call the row tools and write the paragraph yourself.

### Can it answer a question about a private company's headcount?
Not on the sample tier, which states market level only with no company or industry splits. The live surface lists a `company_hiring_report`, and its scope is documented rather than measured here.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - the full catalogue this entry belongs to
- [Jobyap MCP](/hermes/mcp/servers/external/jobyap-mcp/) - roles and candidates rather than pay benchmarks
- [MonitorBankRates MCP](/hermes/mcp/servers/external/monitorbankrates-mcp/) - the same provenance discipline applied to deposit rates
- [Fonciq MCP](/hermes/mcp/servers/external/fonciq-mcp/) - the other entry here that names what it cannot see
