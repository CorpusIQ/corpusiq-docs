---
title: "ListRiver MCP - US Business Registry Data as a Lead List"
description: "Three tools over official US state business registries: count a market free, then pull new LLCs by ZIP, NAICS and formation month."
category: Business Data & Sales
stars: "n/a (ListRiver-LLC/listriver-api, PyPI listriver-mcp 0.1.0, no stars reported)"
added: 2026-11-08
source: "mcpservers.org twelve-sitemap addition in the November 8 midday window; the official MCP registry record io.github.ListRiver-LLC/listriver 0.1.0 published 2026-11-03T13:24:59Z; the API documentation at listriver.com/api-docs; and the package itself, where a keyless initialize answered 200 with the full tool schemas and all three tool calls hit a documented key requirement"
relevance: ★★★★
tags: [business-data, lead-generation, state-registry, llc, new-business, naics, prospecting, us, remote-mcp-adjacent, stdio]
last_updated: "2026-11-08"
---

# ListRiver MCP

**Every lead list a business buys is a guess about who exists. ListRiver answers the question underneath it, from the filings those businesses already made: how many new LLCs were formed in this county last month, in this industry, reachable by phone.** The difference is provenance. A modelled contact database tells you who a vendor thinks is in business. A state business registry tells you what was filed, when, and under what name, with a county and a registered agent attached.

```
Server type: Local (stdio)
Package:     listriver-mcp 0.1.0 (PyPI)
Backend:     https://listriver.com/api/data.ashx (HTTPS GET, X-Api-Key header)
Auth:        LISTRIVER_API_KEY (free, 500 records a calendar month)
Registry:    io.github.ListRiver-LLC/listriver 0.1.0, active
Repository:  github.com/ListRiver-LLC/listriver-api (subfolder mcp)
Protocol:    2025-06-18
Tools:       3
Price:       free tier 500 records/month, then $50 to $450 a month
```

## What the package says about itself

Started with no API key configured, the stdio server completes `initialize` as **`ListRiver` 0.1.0** on protocol `2025-06-18` and returns its full `instructions` string, then lists all three tools with complete input schemas. Nothing is hidden behind the credential. The credential is only needed to spend records:

```json
{
  "ok": false,
  "status": 401,
  "error": "LISTRIVER_API_KEY is not set. Get a free key at https://listriver.com/Account/ApiSignUp.aspx and add it to this MCP server's environment."
}
```

That is the whole integration surface: an operator reads the schemas, decides against them, and only then goes and gets a key.

## The three tools, and the one design decision that matters

| Tool | What it answers | Costs records |
| --- | --- | --- |
| `list_states` | Which states are covered, with counts formed this month, this year and all-time | No. Free |
| `count_businesses` | How many businesses match a filter set, per state | No. Free |
| `search_businesses` | The actual records, up to 100 per call, cursor-paginated | **Yes, every record, every time** |

**`count_businesses` being free is the reason this server belongs in the catalogue.** In every other business-data server already catalogued, you learn the size of a market by paying for the pull, so a sizing question costs the same as a delivery question. Here an agent can ask "how many new HVAC contractors were formed in Maricopa County this quarter, and how many of those have a phone on file" and get a number for nothing. The worked sequence is a sizing loop that terminates before the budget does:

1. `count_businesses` with the broad filters. Free.
2. Narrow on `has_phone`, `has_email`, `naics`, `entity_type`, `formed_within`. Still free.
3. Only when the number is the one you want, `search_businesses` for the names.

## The filter surface

| Argument | Accepted values |
| --- | --- |
| `states` | Two-letter registration states, comma-separated (`FL`, `FL,TX`). Required with city, county or zip |
| `city` | Comma-separated city names |
| `county` | Comma-separated counties, optionally qualified (`FL:MIAMI-DADE`) |
| `zip` | 5-digit ZIPs or 3-digit prefixes (`33139,331`) |
| `naics` | NAICS prefixes, 2 to 6 digits (`23` construction, `722511` full code) |
| `entity_type` | `LLC`, `CORP`, `LP`, `LLP`, `NONPROFIT`, `OTHER` |
| `has_phone` / `has_email` | Only records with a phone or an email on file |
| `formed_within` | The current month or the N months before it. `0` for any formation date |
| `formed_from` / `formed_to` | Explicit `YYYY-MM` range, overriding `formed_within` |
| `limit` / `cursor` | 1 to 100 records per call, then the cursor from the previous answer |

Records carry address, county, registered agent, formation month and, where available, phone, email, website, EIN and NAICS industry.

## The parts the vendor is unusually honest about

Two statements in the server's own instructions are worth more than the tool list, because they are the two ways this surface can mislead a user.

**Coverage is partial and varies by state.** Phone, email, NAICS and county are present on only part of the records, and the split differs by state. The server tells the agent to run `count_businesses` with `has_phone` or `has_email` *before* promising a caller a phone list, rather than returning a thin list and letting the user discover the gap. An agent that skips that step will confidently report "here are your 400 leads" against a market where 60 of them have a number.

**The records carry a use restriction.** The data is licensed for the user's own business use and may not be used for credit, insurance, employment or housing decisions. That last set is the FCRA boundary, and it is the correct boundary: formation filings are public, but the moment a list becomes an input to a lending, underwriting, hiring or tenancy decision it is a consumer report. Recording this plainly is the difference between a tool an operator can use and a compliance incident waiting for a first use.

## Pricing, read off the vendor's documentation

- **Free:** 500 records per calendar month (UTC), one free key per person, temporary email addresses refused
- **Monthly:** $50 for 5,000, $100 for 12,000, $200 for 28,000, $450 for 75,000 records per billing period, cancel any time, unused records do not carry over
- **Prepaid:** $50 for 5,000, $75 for 7,500, $100 for 10,000, consumed after plan records, expiring 12 months after purchase
- **AWS Marketplace:** larger volumes billed on the AWS invoice, keys prefixed `lr_live_`

The record is the unit, not the call, and the server says so twice: every business returned counts each time it is returned. A retry loop, a re-run or a summary request that re-pulls the same fifty names spends another fifty records. Cursors exist precisely so a session continues a search instead of restarting it.

## Does this overlap anything already in the catalogue?

No, and the three nearest neighbours each miss a different thing.

[Corply](/hermes/mcp/servers/external/corply-mcp/) is a formation *service*: it files a Delaware C-corp for a founder. It does not return anyone else's records. [Leadbay](/hermes/mcp/servers/external/leadbay-mcp/) and [Vibe Prospecting](/hermes/mcp/servers/external/vibe-prospecting-mcp/) are proprietary scoring surfaces: the value is the model's lead score, and the underlying provenance is the vendor's. [firmy.ai](/hermes/mcp/servers/external/firmy-ai-mcp/) reads one national registry (Polish KRS) with revenue and sanction checks, which is deep on one country and silent on the US.

ListRiver is the US official-registry slice with a formation clock on it: **a business that was filed last month has no website to audit, no ad history to bid against and no competitor relationship yet.** That is a different prospecting moment from "enrich the company I already have", and it is the one thing this catalogue previously could not do for a US operator.

## What an operator actually asks

> "How many new roofing LLCs formed in Maricopa County in the last three months, and how many have a phone number on file?"

Three calls. The first two are free and answer the question. The third is the one that spends records, and you only run it once you know the number is worth it.

> "Which industries formed the most new businesses in Florida last month?"

`count_businesses` with `states=FL`, `formed_within=1` and successive `naics` prefixes, all free, until the distribution is clear.

> "Give me 200 newly formed e-commerce businesses in Texas with a website."

`count_businesses` first, because `has_email` and `has_phone` are the two switches that decide whether 200 is a number or a promise.

## Who should not use it

An operator who wants an enriched, scored, verified contact record with a job title and a direct dial. That is the Leadbay and Vibe Prospecting job, and this surface will look thin next to it because it is reporting a filing, not a profile. The two are complementary: ListRiver decides *who is new*, the enrichment layer decides *who to call first*.

## Limits recorded

- **A key is required to spend records.** The surface is fully readable without one, but no record comes back without a free key, so this entry rests on the schemas, the instructions and the vendor's documentation rather than a driven record pull.
- **US only.** State business registries are the source; there is no international coverage.
- **Partial enrichment.** Phone, email, NAICS and county are present on a subset of records, and the subset is state-dependent.
- **A use restriction the operator is bound by.** No credit, insurance, employment or housing decisions.
- **Repository metadata is thin.** The GitHub repository carries no star signal, so this entry is not resting on community adoption.

## Sources checked

- `https://listriver.com/api-docs` (HTTP 200, read 2026-11-08)
- `https://registry.modelcontextprotocol.io/v0/servers?search=listriver` (one active record, `io.github.ListRiver-LLC/listriver` 0.1.0, published `2026-11-03T13:24:59.336Z`)
- `uvx listriver-mcp` over stdio: `initialize` 200 as `ListRiver` 0.1.0 on protocol `2025-06-18`; `tools/list` returned three tools with schemas; `list_states` and `count_businesses` returned the documented 401 key requirement
- `https://mcpservers.org/servers/listriver-llc/listriver-api` (present in the twelve-sitemap canonical; the detail route answers 403 by edge policy, the standing condition since November 4)
