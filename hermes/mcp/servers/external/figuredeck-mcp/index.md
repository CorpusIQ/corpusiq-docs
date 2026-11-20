---
title: "FigureDeck MCP - FHFA Loan Limits and Mortgage Math"
description: "A keyless calculator that returns the 2026 FHFA conforming limit for any of 3,235 counties and reproduces mortgage math to the cent."
category: "Real Estate / Mortgage Finance"
stars: "n/a (hosted vendor endpoint; no public repository)"
added: 2026-11-19
source: "the mcpservers.org sitemap map servers/12 (restamped 2026-11-19T18:10Z onward), the official MCP registry record com.figuredeck/conforming-limits 1.0.0 published 2026-11-19T02:56:42Z, a keyless initialize and full tools/list on 2026-11-19, seven tools/call requests across all three tools including three refusals, the vendor data file at figuredeck.com/data/conforming-limits-2026.json read to 3,235 records, and every figure in this guide reproduced by hand"
relevance: ★★★
tags: [mortgage, real-estate, conforming-loan-limits, fhfa, amortisation, affordability, dti, county-data, remote, keyless, no-auth, us]
last_updated: "2026-11-19"
---

# FigureDeck MCP

**A loan officer's first question is which limit applies in this county this year. This server answers it for all 3,235 counties, and then does the payment arithmetic to the cent.**

FigureDeck runs US mortgage calculators on its own site and exposes the same three surfaces over MCP. There is no account, no key and no session id: an anonymous `initialize` returns the tool list, and every number comes back with a citation string the caller is expected to repeat.

```text
Server type:   remote Streamable HTTP, stateless (no Mcp-Session-Id issued)
Endpoint:      https://mcp.figuredeck.com/mcp
Server:        figuredeck 1.0.0, protocol 2025-06-18
Registry:      com.figuredeck/conforming-limits 1.0.0, published 2026-11-19T02:56:42Z
Vendor site:   https://figuredeck.com/us/mortgage/conforming-limit/ (HTTP 200, 44,953 bytes)
Auth:          none
Tools:         3, all keyless, all with a published inputSchema AND outputSchema
Data:          https://figuredeck.com/data/conforming-limits-2026.json (HTTP 200, 477,662 bytes, 3,235 records)
```

## What the server says about itself

The `initialize` response carries an instructions string that states the product shape before any tool is called:

> Two kinds of answers: a table (2026 FHFA conforming loan limits for all 3235 US counties) and calculations (monthly payment, total interest, price supported by an income). Every number is exact and comes with a source you can cite. Amounts are US dollars.

That is a narrow claim, and the pass tested it rather than accepting it. All three tools publish an `outputSchema` beside their `inputSchema`, which is still rare enough in this catalog to be worth recording: a client can validate a response without guessing at field names.

## The three tools

| Tool | Arguments | Returns |
|---|---|---|
| `search_conforming_limits` | `county`, `fips` (takes precedence), `state`, `limit` 1-100 | baseline, matched, returned, truncated, per-county rows for 1 to 4 units, `as_of`, `source`, `citation` |
| `mortgage_payment` | `loan_amount`, `annual_rate_percent`, `term_years`, optional `monthly_tax`, `monthly_insurance`, `monthly_hoa` | monthly P&I, total interest, total paid, first-month interest and its share, months |
| `affordability` | `monthly_income`, `annual_rate_percent`, `term_years`, optional `monthly_debts`, `down_payment`, `dti_cap_percent`, tax, insurance, HOA | max housing budget, max P&I, max loan, max price, plus the same answer at 28, 36, 43 and 50 percent DTI |

## The county limit, and the ceiling above the ceiling

`search_conforming_limits` on Los Angeles County:

```json
{
  "baseline_limit": 832750,
  "counties": [{
    "fips": "06037", "county": "Los Angeles County", "state": "CA",
    "limit_1_unit": 1249125, "limit_2_unit": 1599375,
    "limit_3_unit": 1933200, "limit_4_unit": 2402625,
    "above_baseline": true
  }],
  "as_of": "2026-01-01",
  "source": "Federal Housing Finance Agency (FHFA) - Conforming Loan Limit Values for Calendar Year 2026 - All Counties"
}
```

The arithmetic behind that number is checkable in one step: **1,249,125 is exactly 1.5 times the 832,750 baseline**, which is the statutory high-cost ceiling. Reading the vendor's own data file as a second surface confirms the shape of the whole table:

```text
records            3,235
baseline_1_unit      832,750
ceiling_1_unit     1,249,125
at_baseline        3,075      (95.1 percent of counties)
above_baseline       160
max_1_unit         1,299,500
```

That last figure is the interesting one. Two Hawaii counties, Kalawao (FIPS 15005) and Maui (15009), sit at **1,299,500**, above the 1,249,125 ceiling, because the statute allows a higher cap in Alaska and Hawaii. The tool's `county` and `fips` routes return the same row for `06037` and the JSON agrees with both.

The 2, 3 and 4 unit multipliers are FHFA's published ratios rather than round numbers: 1,599,375 / 1,249,125 is **1.2804**, 1,933,200 is **1.5476** and 2,402,625 is **1.9234** of the one-unit limit, and the baseline row carries the same ratios at 1,066,250 / 1,288,800 / 1,601,750. A caller that multiplied by 1.25 would be wrong by thousands of dollars per county.

Three query shapes were measured:

- `state: "AZ"` returns **15 counties matched**, 5 shown because `truncated: true` and the default `limit` is 10, every one at the 832,750 baseline.
- `fips: "06037"` beside `county: "King County, WA"` returns **Los Angeles**, which is the schema's stated precedence and not a silent merge.
- `county: "Nowhere County, ZZ"` returns `matched: 0` with a usable explanation rather than an error, and that explanation publishes the distribution: *most US counties sit at the 832,750 baseline for 2026 (3075 of 3235); 160 high-cost counties are above it*.

## The payment, reproduced by hand

`mortgage_payment` on **450,000** at **6.5 percent** over **30 years**:

```text
monthly P&I            2,844.31
total paid         1,023,950.20
total interest       573,950.20
first-month interest   2,437.50   (85.7 percent of the first payment)
months                      360
```

Every field reproduces exactly with the standard annuity formula at r = 0.065/12, n = 360: payment **2,844.31**; 2,844.31 unrounded times 360 gives **1,023,950.20**; interest is that minus principal, **573,950.20**; the first month's interest is 450,000 times 0.005416667, **2,437.50**, which is **85.7 percent** of the payment. The server rounds the display text to whole dollars ("$2,844 a month", "$1,023,950") while returning cents in `structuredContent`, so a client that renders only `content` loses precision and a client that reads the structure does not.

A zero-rate control behaves the way an amortisation should rather than dividing by zero: 300,000 at 0 percent returns **833.333** a month, **300,000** total and **0** interest.

## Working backwards from income

`affordability` on **10,000** a month gross, at a **36 percent** cap, with **500** of existing debt, **80,000** down and **600** a month of tax, insurance and HOA:

```text
housing budget 3,600   = 36 percent of 10,000
minus debts      500
minus tax/ins/HOA 600
max monthly P&I 2,500
max loan     395,527.05
max price    475,527.05
```

The bands, all reproduced: 28 percent gives a loan of **268,958.39** and a price of **348,958.39**; 43 percent gives **506,274.62** and **586,274.62**; 50 percent gives **617,022.20** and **697,022.20**. The order of operations matters and the tool states it: the cap applies to gross income, existing debts come out next, then the carrying costs, and only the remainder is capitalised at the rate. A model that subtracted costs before applying the cap would overstate the price.

## Provenance, which is the real product

The data file names its own source chain, and the chain is the reason to trust the table:

```json
{"publisher": "Federal Housing Finance Agency (FHFA)",
 "dataset": "Conforming Loan Limit Values for Calendar Year 2026 - All Counties",
 "csv": "https://www.fhfa.gov/document/d/cll/fullcountyloanlimitlist2026_hera-based_final_flat.csv",
 "released": "2025-11-25", "retrieved": "2026-10-23"}
```

License is `public-domain` with the note that FHFA asks for attribution and that no endorsement be implied, and the file carries the sentence *This product uses FHFA data but is neither endorsed nor certified by FHFA*. Every tool response repeats a `citation` string pointing at the vendor page and the data file. For a number that ends up in a loan file, that is the difference between a reference and a guess.

## Defects, recorded rather than smoothed

Three, all measured:

1. **No validation on `loan_amount`.** A loan of **-100** returns `isError: false` with the text *"A $-100 loan at 6.5% over 30 years is $-1 a month in principal and interest. Over 0 payments you hand over $0"*, and a loan of **0** returns the same shape. A caller that passes an unset variable gets a confident answer instead of a refusal.
2. **The calculation tools mis-cite themselves.** `mortgage_payment` and `affordability` both return a `citation` pointing at the conforming-limits dataset and `figuredeck.com/data/conforming-limits-2026.json`, which have nothing to do with an amortisation. The arithmetic is right and the attribution is wrong, which is worse than no citation in a compliance context.
3. **`limit` above 100 is clamped silently.** `limit: 500` returned the 15 Arizona counties with no error and no note that the requested ceiling was ignored. The schema declares a maximum of 100, so a strict client would never send 500, and a loose one is not told.

One limit that is design rather than defect: the table is a single calendar year, `as_of` **2026-01-01**. A 2025 or 2027 limit is not available from this server, and `affordability` is a DTI cap model, not an underwriting decision.

## Add it to Hermes

```bash
hermes mcp add figuredeck --url https://mcp.figuredeck.com/mcp
hermes mcp test figuredeck
```

No OAuth, no key, no session. The first useful question to ask it is a county plus a price: *what is the conforming limit in Maricopa County, and what does a 400,000 loan at 6.25 percent cost a month.* Every number in the answer can be checked against the FHFA file the server cites, which is the whole point of pairing this table with a business-data agent.

## Why it earns a slot

The catalog's mortgage entries are brokers' rate feeds and property-search tools. This is the first entry that serves the federal limit table itself, county by county, with an arithmetic surface attached, and it does so without an account. For any operator touching US residential lending, title, appraisal or property investment, that is a reference layer rather than another opinion.
