---
title: "Dealport MCP - 28M US Companies Behind a Free Preview"
description: "A keyless buy-box preview over 28M US private company records, with every paid record behind an OAuth 401 and a published rate card."
category: "Business Data"
stars: "n/a (vendor-hosted; no public MCP repository)"
added: 2026-11-26
source: "chatmcp submission queue #8211 filed 2026-11-27T00:24:53Z; official registry `com.dealport/dealport` (domain verified) with remote https://app.dealport.com/api/mcp; driven on 2026-11-27 at the 21:00 MST tick with a keyless initialize, a 41-tool tools/list, six preview_companies calls, resources/list, a resources/read of dealport://rate-card and a paid-tool 401 header capture; prices read from the vendor's own /llms-full.txt and the rate-card resource"
relevance: "★★★"
tags: [business-data, company-records, market-sizing, owner-contacts, oauth, pay-per-record, rate-card, projects, outreach, us-companies, streamable-http]
last_updated: "2026-11-26"
---

# Dealport MCP

**A buy-box question has two halves and assistants usually answer only the second one: how many companies match the profile, and who owns them.** Dealport answers the first half for nothing and without an account. It indexes 28M+ US private operating businesses and commercial and multifamily properties from state corporate registries, UCC filings, Medicare and CMS cost reports, state health and trade licences, SEC Form ADV, and NYC property and mortgage records, and its `preview_companies` tool sizes any filter combination at `$0.00` with five sample records. The paid half, per-company records at a penny and owner contacts at nine cents, sits behind an OAuth wall that is announced properly.

```
Server type:  Remote (Streamable HTTP)
Endpoint:     https://app.dealport.com/api/mcp
              https://app.dealport.com/api/mcp/   trailing slash also answers
Protocol:     2025-06-18, serverInfo Dealport 1.0.0
Auth:         none for initialize, ping, tools/list, prompts/*, resources/*,
              and preview_companies (IP rate-limited at 20 calls a minute)
              OAuth 2.1 (PKCE, dynamic client registration) or a dp_live_ key
              for the other 40 tools
Tools:        41, read from a keyless tools/list
Resources:    5 playbooks and dealport://rate-card, both keyless
Registry:     com.dealport/dealport
Billing:      plain USD pay-as-you-go, $5.00 of free balance on a new account
```

`initialize` answers **200** at protocol **2025-06-18** as `Dealport` **1.0.0** with `tools`, `prompts` and `resources` all declaring `listChanged`, and an `instructions` block that states the commercial order of operations in one sentence: *"Start with preview_companies ($0.00) to size any buy-box before calling search_companies."* That is the rare case of a paid surface that publishes the cheap call first.

## The 41 tools, and the five that matter to a business question

The full catalogue is documented by the vendor and was read back from a keyless `tools/list`. What matters outside a deal team is a smaller set:

| Tool | Rate | What it answers |
| --- | --- | --- |
| `preview_companies` | `$0.00` | matching count plus five sample companies for any US state, county, city, industry, revenue or headcount filter |
| `search_companies` | `$0.01` per fresh company | the same filters, returning records (`$0.00` on a repeat inside 30 days) |
| `get_record` | `$0.01` per record | one company by UUID or one NYC building by BBL, every fact with its basis, date and numbered source |
| `find_owner` / `find_contact` | `$0.09` per hit, `$0.00` on a miss | the human principal behind a company, with direct phones and emails |
| `what_changed` | `$0.00` | weekly ownership, leadership, headcount, licence and filing diffs on watched companies |
| `research_company` | `$0.50` per company | an async cited investigation, `$0.00` on a repeat inside 30 days |
| `avery_reach_out` | `$0.02` per email sent | blind double-opt-in owner outreach through Dealport's agent |

The rest are workspace machinery: Projects, playbooks, rubric annotations, stage and touch logging, anti-collision blocklists, HMAC-signed watch webhooks, and the Avery funnel. A workspace pays per company per month to watch, which is the only subscription-shaped charge in the card.

**The rate card is a resource, not a web page.** `resources/read` on `dealport://rate-card` answered **200** keyless with `"billing_model": "plain_usd"` and a per-action table, and `resources/list` returned the five playbooks (`buy-box-sourcer`, `monday-watchlist-check`, `pre-call-partner-brief`, `departing-rep-continuity`, `b2b-commercial-gtm`) as portable Markdown. A client can therefore read the price of an action before it takes one, without a session and without a credential, which is the cleanest cost story in this catalogue.

## One state, driven six ways

`preview_companies` is the only call an unauthenticated client can spend, so it was called six times on 2026-11-27 and the shape of the answer is the finding.

```text
{"state": "OH"}                          -> 10,000  matching_count_more: true
{"state": "TX", "counties": ["Harris"]}  -> 10,000  matching_count_more: true
{"state": "OH", "cities": ["Cincinnati"]}-> 10,000  matching_count_more: true
{"name_starts_with": "Ace"}              -> 10,000  matching_count_more: true
{"state": "ZZ"}                          ->      0  matching_count_more: false
{"state": "OH", "naics": ["722511"]}     -> isError: true, "search_too_broad"
```

The samples prove the filters are applied. Ohio returns `PORTER PRECISION PRODUCTS COMPANY` (51 employees, a `$12M` to `$18M` revenue band, independent) beside `DEER CREEK HONEY FARMS, LTD.` and `OKI FURNITURE FAIR LLC`; Harris County returns trucking sole proprietors and a 2,298-employee staffing firm; Cincinnati returns `UC Health` at 7,601 employees and `THE CINCINNATI REDS LLC` at 150; and `Ace` returns five companies actually named ACE across WA, MN, NY, NH and AZ.

**What does not move is the count.** Every filter shape that matched anything returned exactly **10,000** with `matching_count_more: true`, including a three-letter name prefix that cannot describe ten thousand US companies. The number is a cap with an honest flag, but it is not a size, so the `tam_gate_passed: true` beside it is decided on a truncated value. An agent asked *"how big is this market"* will answer *"more than ten thousand"* for Ohio, for one Ohio city, and for every business whose name starts with Ace.

## Five defects, measured

1. **`matching_count` saturates at 10,000 and stops discriminating.** Four different filter shapes returned the same capped total while the samples visibly narrowed, so the one number the free tier exists to produce cannot be used to compare two buy-boxes. The honest fix is a second field carrying the true count, or a per-filter narrowing that the cap does not hide.
2. **An invalid state code is a clean zero.** `state: "ZZ"` returned **200**, `matching_count: 0`, an empty sample, and `tam_gate_passed: false`, with no error and no message. **"No companies match"** and **"you typed a state that does not exist"** are different answers, and only the first should reach a user.
3. **`industry` is null on a third of the sample rows.** Two of five Ohio records and two of five Harris County records carry `"industry": null` while the trucking records carry `"Trucking"`. A sector filter built on that column silently drops records, and a client that prints "industry: not recorded" is closer to the truth than one that prints an empty string.
4. **The sizing filter is the one that errors.** `naics` alone returned `isError: true` with *"That search took too long. Add an industry, or a narrower revenue or headcount range."* The message is honest and the advice is correct, but the tool advertised for sizing a market refuses the industry code most operators would size it with.
5. **Bands carry their basis inside the string.** `employee_band` reads `"51 (filed)"` and `revenue_band` reads a dollar range written with a typographic dash, and the two are not comparable types: one is a count with a provenance suffix, the other a range. A parser that splits on the dash gets a range, a parser that splits on the parenthesis gets a number, and neither gets both without a rule.

A sixth note that is not a defect: `remaining_balance_usd` is **null** on every keyless call. That is *not signed in*, not *no balance*, and a client that renders it as `$0.00` tells the operator their account is empty when they have no account.

## The paid wall is announced properly

The other 40 tools answer **401** with a standard challenge:

```text
POST https://app.dealport.com/api/mcp      tools/call search_companies
HTTP 401
www-authenticate: Bearer error="invalid_token",
                  error_description="No authorization provided",
                  resource_metadata="https://app.dealport.com/.well-known/oauth-protected-resource"
{"error": "invalid_token", "error_description": "No authorization provided"}
```

A protected-resource document, an error code, and a plain JSON body: a compliant MCP client can discover the credential path, open the OAuth flow with dynamic registration and PKCE, and retry, which is the difference between a paid surface and a paywall. `preview_companies` stays free on the same endpoint, so the first contact costs nothing and the gate is met only when a record is actually wanted.

## What it costs, in the vendor's own numbers

New API accounts start with **$5.00** of free balance. A fresh company record is **$0.01**, a repeat read inside 30 days in the same workspace is **$0.00**, an owner or contact hit is **$0.09** with misses free, a company research is **$0.50**, a background project run is **$0.05** per record, and an Avery email is **$0.02** per send. Watching costs **$0.05** per company per month. The shape to notice is that the expensive actions are the ones that produce a person rather than a record: a hundred companies cost a dollar, a hundred owner contacts cost nine.

## Add it to Hermes

```bash
hermes mcp add dealport --url https://app.dealport.com/api/mcp
```

Nothing else is needed for `preview_companies` and the rate card. Add a key only when records or owners are wanted:

```yaml
mcp_servers:
  dealport:
    url: https://app.dealport.com/api/mcp
    headers:
      Authorization: "Bearer ${DEALPORT_API_KEY}"
```

Treat `matching_count: 10000` as *at least ten thousand*, quote `matching_count_more`, and never compare two buy-boxes on a number that is capped for both. Read `dealport://rate-card` before spending, and read `remaining_balance_usd: null` as an unauthenticated call.

## Does Dealport work without an account?

Yes, for everything except records and owners. `initialize`, `ping`, `tools/list`, `prompts/*`,
`resources/*` and `preview_companies` answer with no credential at all, the rate card is readable
as a resource, and the other 40 tools answer a standard **401** carrying a
`resource_metadata` pointer to the protected-resource document, so a client can open the OAuth
flow itself. The free half is a real half: a buy-box can be sized and five sample records read
before anyone signs in.

## Why this one is in the catalogue

The operator question it serves is the one every market-sizing conversation starts with, **how many US businesses actually match this profile**, and it answers it with cited public filings rather than with an estimate. The free preview means an assistant can do the first half of a market study for nothing, and the vendor's own instruction string tells it to do exactly that before spending. The rate card as a machine-readable resource is the pattern worth copying across this catalogue.

## See also

- [Leadgen ONRC Romania MCP](/hermes/mcp/servers/external/leadgen-onrc-mcp/) for the same job in another jurisdiction: company records by fiscal identity rather than by geography.
- [External MCP Server Catalog](/hermes/mcp/servers/external/) for the full index of business-data surfaces.
