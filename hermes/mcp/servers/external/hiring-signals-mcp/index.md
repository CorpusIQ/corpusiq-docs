---
title: "Hiring Signals MCP - 208,350 Live Jobs From Career Sites"
description: "Live job postings scraped from Greenhouse, Lever and Ashby boards, with pay ranges, hiring velocity per company and a 100-credit free key, driven end to end."
category: "Business Data"
stars: "n/a (vendor-hosted; the public manifest and stdio client are at github.com/ThryveBaseline/hiring-signals-mcp, star count not measured this pass)"
added: 2026-11-27
source: "queue filing chatmcp/mcpso#8267 read on 2026-11-27; keyless initialize 200 as Hiring Signals 1.0.0 on protocol 2025-06-18 and a 4-tool tools/list at https://api-production-47e35dbb.up.railway.app/mcp; free key minted by POST /v1/keys and ten tools/call attempts driven the same day; catalog health read from get_status"
relevance: "★★★"
tags: [hiring-signals, jobs, sales-intelligence, company-data, ats, greenhouse, ashby, remote-mcp]
last_updated: "2026-11-27"
---

# Hiring Signals MCP

**Hiring is the one growth signal a company cannot hide. Headcount plans show up as job posts weeks before they show up in a press release, a funding announcement or a headcount chart, and the posts are public by law of the platform: every Greenhouse, Lever and Ashby board is a JSON document anyone can read. Hiring Signals does the collecting and puts a query surface in front of it, with pay ranges and a per-company velocity count, and it lets an assistant answer the question an operator actually asks, which is not "who is hiring" but "is this company about to spend money".**

```
Server type:  Remote (Streamable HTTP)
Endpoint:     https://api-production-47e35dbb.up.railway.app/mcp
Registry:     io.github.ThryveBaseline/hiring-signals
Auth:         optional X-API-Key; free key (100 credits, no card) via POST /v1/keys
Discovery:    initialize 200, 4-tool tools/list and get_status all keyless
Tools:        4 (get_status, search_jobs, company_hiring, get_credits)
```

`initialize` answers **200** at protocol **2025-06-18** as `Hiring Signals` **1.0.0**, and the server's own instructions block states the pricing model in one sentence: *"Get a free API key (100 credits, no card) by POSTing {'email': 'you@company.com'} to https://api-production-47e35dbb.up.railway.app/v1/keys, then send it as the X-API-Key header on this MCP connection."* That key minted in one call and returned `{"api_key": "hs_…", "credits": 100}`.

## What the catalog holds

`get_status` is free, needs no key and answers as a health document built for a monitor:

```json
{"ok": true, "open_jobs": 208350, "companies_hiring": 5069, "salary_pct": 29,
 "health": {"healthy": true, "last_sync_age_h": 7.87, "boards_ok": 5544, "boards_error": 0, "open_jobs": 208350}}
```

**208,350 open jobs across 5,069 companies on 5,544 boards, with zero boards in error and a sync under eight hours old.** The number that matters for planning is `salary_pct: 29`, because it says what the other tools can and cannot answer: **seven jobs in ten carry no pay range at all**, so a salary screen is a screen over 60,000 postings, not over 208,350, and a question phrased as "what does this role pay here" usually has no row behind it.

## Four tools, three of them free to call

| Tool | What it does | Cost |
|---|---|---|
| `get_status` | Catalog health: open jobs, companies, boards ok and in error, salary coverage, sync age | 0 credits, no key |
| `search_jobs` | Keyword, company, remote, salary and recency filters over the live corpus, with pay ranges and URLs | 1 credit per job returned; anonymous callers get a 5-job preview |
| `company_hiring` | Open roles, new in 7 and 30 days, closures in 30 days, remote share, top departments and top salaries for one board slug | 5 credits, key required |
| `get_credits` | Remaining balance for the key in the header | 0 credits |

The anonymous path is unusually generous for a paid data product and it is deliberate: the instructions say *"Without a key, get_status always works and search_jobs allows a small anonymous preview (5 jobs, 5 calls per IP per day) so directory health checks can succeed."* A five-job preview really is returned keyless, with `"anonymous": true` and `"credits_charged": 0`, and the rows are live: the first preview carried a RevenueCat posting with `posted_at` **2026-11-27T17:38:47Z**, roughly four hours before this pass read it.

## The credit arithmetic reproduces

Every balance was read back after the calls, so the charge model is checked rather than assumed:

| Step | Call | Credits | Balance |
|---|---|---|---|
| 1 | key minted | - | **100** |
| 2 | `company_hiring` stripe | 5 | |
| 3 | `company_hiring` revenuecat | 5 | |
| 4 | `search_jobs` q=designer, limit 3 | 3 | **87** |
| 5 | `search_jobs` q=barista, limit 3 | 3 | |
| 6 | `search_jobs` q=zzzzqqq | 0 | **81** |
| 7 | `search_jobs` remote + has_salary, limit 10 | 10 | **71** |

Two honest details sit in that table: a query that returns nothing costs nothing (`zzzzqqq` returned `count: 0` and `credits_charged: 0`), and the charge is per **row returned**, not per call, so `limit` is the price control.

## Hiring velocity, company by company

`company_hiring` is the tool that earns the entry, because it converts a list of open roles into two measurements an operator can act on: how fast a company is adding, and which department is being funded.

**Stripe** (`board: "stripe"`, Greenhouse): **767 open jobs**, **37 new in 7 days**, **237 new in 30 days**, `closed_last_30d` **0**, `remote_share` **0.15**, and the top departments read as the company's own internal codes, which is what a Greenhouse board exposes: `1185 Account Executives (EMEA)` at **50**, `1195 Account Executives (APAC)` at **28**, `5112 General University` at **25**, `8811 Product Design` at **14**, `8611 Security Analytics` at **13**. The story in those five rows is one sentence long: the funded department is sales.

**RevenueCat** (`board: "revenuecat"`, Ashby): **11 open jobs**, **1 new in 7 days**, **3 new in 30 days**, `remote_share` **1.0**, departments `Product` **4** and `Growth` **4** ahead of `Engineering` **2**, and a populated `top_salaries` list: Head of Sales **363,000**, Head of Customer Growth **259,000**, four separate Senior Product Manager roles at **230,000**, Senior Data Scientist **220,000**, Senior CRO Designer **205,000**. That mix - half the open roles in product and growth, at 205 to 363 thousand dollars - is a company buying retention and monetisation rather than engineering.

**The two boards disagree about pay data and that is the finding.** Stripe returned `top_salaries: []` with 767 open jobs; RevenueCat returned nine priced roles out of eleven. Greenhouse boards publish pay ranges in prose or omit them, Ashby boards carry them as fields, so `top_salaries` is a usable measurement on Ashby and silence on Greenhouse. An assistant that reads an empty list as "this company does not publish pay" will be right about the field and wrong about the company.

## Five defects recorded

**1. `remote` is not "fully remote".** Ten rows returned under `remote: true` with a salary all carried a named city: Palo Alto, Toronto, and one that reads literally `Florence (on-site)` with `remote: true` beside it. RevenueCat reads `remote_share: 1.0` with a listing whose location is `New York`. The flag means "not restricted to one office", so a caller filtering on it gets hybrid and city-bound roles mixed into a remote list, and any count built on the flag is an upper bound rather than a count of remote jobs.

**2. `closed_last_30d` reads zero on both boards.** Stripe with 767 openings and RevenueCat with 11 both answered `0`. A company that size closes roles every month, so the field is almost certainly measuring only closures the tracker itself observed - a job that disappears between two syncs - and the corpus is younger than the window. Read it as "no closure observed yet", never as "nobody left".

**3. An auth failure arrives as success.** `company_hiring` and `get_credits` without a key answer **HTTP 200** with `isError: false` and this payload: `{"error": "company_hiring requires an API key (5 credits). Get a free key: POST … then send X-API-Key."}`. The sentence is helpful to a human and wrong for a protocol client: an agent that branches on `isError` will treat a refused call as a completed one and may report a company's hiring picture as empty.

**4. The keyword filter matches text the response does not include.** `q: "designer"` returned *Senior Electrical Engineer - AI Accelerator Boards*, *Associate Product Manager* and *Designer Pleno*; `q: "barista"` returned *Personal Care Specialist (Full Time), Durango*, *Senior Key Account Management Drogerie (w/m/d)* and *Barista | Philadelphia*. One title in three contains the term, and a nonsense query returns zero, so the filter is applied to something - most likely the full description, which the response never shows. A caller cannot verify why a row matched, and should not treat `q` results as title matches.

**5. Ordering is recency, not relevance, and one bulk publisher fills the page.** Ten consecutive rows of a `remote`/`has_salary` query came from one employer, `jerry.ai`, posted between **18:06:47Z** and **18:09:42Z** - ten genuinely distinct requisitions pushed to the board in three minutes. That is not a duplicate defect: the `ext_id` values differ. It is an ordering property, and it explains defect 4 as well: with no relevance score, the query term only decides *whether* a row is in the set, and recency decides what the caller sees first.

## What this is for, and what it is not

It is a **growth and prospecting surface**: a customer list ranked by hiring velocity, a prospect's funded department, a competitor's expansion direction, a pay benchmark when the row exists. It is not a hiring tracker that sees closures, and it is not a salary survey at 29 per cent coverage.

For an operator reading business signals the honest use is the velocity pair - `new_last_7d` against `new_last_30d`. RevenueCat at 1 in 7 days against 3 in 30 is a company hiring steadily. Stripe at 37 in 7 against 237 in 30 is a company hiring at a rate that is accelerating, with the money going to account executives in EMEA and APAC.

## Frequently asked questions

### Can it see LinkedIn or Indeed?

No, and the vendor says so in the description and in the tool text: the corpus is built from companies' own career boards - Greenhouse, Lever and Ashby - which is why nothing here needs a login, a proxy or a scrape that breaks. The coverage consequence is real: a company that recruits only through an agency or a regional job board has no row.

### Is the free tier enough to evaluate it?

Yes for a first pass and no for a workflow. **100 credits is 100 job rows, or 20 company reads at 5 credits each**, and 100 rows is enough to see whether your own sales list returns real data. Note the cost shape before you rely on it: `search_jobs` with `limit: 50` costs 50 credits, so an accidental large page empties the free key.

### Does it replace a CRM connector?

No. It produces a signal - a company is hiring a sales team in EMEA - that belongs next to a CRM record, not in place of one. The pairing that makes sense is this server for the signal and a CRM connector for the account.

## See also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
