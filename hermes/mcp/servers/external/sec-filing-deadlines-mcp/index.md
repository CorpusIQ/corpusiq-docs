---
title: "SEC Filing Deadlines MCP - 10-K, 10-Q and Form 4 Due Dates"
description: "Computes SEC filing due dates for 10-K, 10-Q, 20-F, 11-K and Forms 3, 4, 5 from rule text, with holidays and extensions."
category: "Finance and Compliance"
stars: "n/a (hosted service; registry fr.amacunia/10-k-10-q-8-k-form-4-filing-deadlines, filing chatmcp/mcpso#8301, repository github.com/Marcoco27/public-company-filing-deadlines-mcp)"
added: 2026-11-28
source: "queue filing chatmcp/mcpso#8301 read on 2026-11-28T14:21:14Z; keyless initialize 200 as 'Public Company Filing Deadlines' 0.1.0 on protocol 2025-06-18, a 16-tool tools/list, and four tools/call attempts: the free sample, two free-trial calls (one with no arguments, one with the CIK only) and two paid routes that returned their x402 challenge"
relevance: "★★★"
tags: [sec, edgar, 10-k, 10-q, 8-k, form-4, filing-deadline, compliance, x402, finance]
last_updated: "2026-11-28"
---

# Public Company Filing Deadlines MCP

**Ask a finance team when the 10-K is due and the answer is a rule, not a date: sixty days after fiscal year end for a large accelerated filer, seventy-five for an accelerated one, ninety for the rest, moved to the next business day when the arithmetic lands on a weekend or a federal holiday, and extended only by a Rule 12b-25 notice filed in time. Every one of those steps is a place where a spreadsheet model quietly gets it wrong, and the cost of getting it wrong is a late filing on a public record. This server computes the date from the rule text, cites the text it used, and fingerprints the copy it read. It was driven for this entry rather than quoted from its filing.**

```
Server type:  Remote (streamable HTTP, hosted)
Endpoint:     https://filing-deadlines.amacunia.fr/mcp
Registry:     fr.amacunia/10-k-10-q-8-k-form-4-filing-deadlines
Auth:         none to list tools; answers are paid per call in USDC over x402
Free tier:    3 calls a day per caller, on form_10_k_due_date only
Tools:        16 - one free sample plus fifteen route tools
Cutoff:       17:30 America/New_York (22:00 for Form 4)
```

`initialize` answered **200** with no credential, naming itself `Public Company Filing Deadlines` **0.1.0** on protocol **2025-06-18**, and its instructions string states the design in one sentence: *"Each answer cites the official rule text, its address and its SHA-256 fingerprint."* `tools/list` returned **16** tools, every one carrying `readOnlyHint: true`, and the list is organised one question per tool rather than one tool with a form mode: due date, on-time verdict and late-notice timetable for each of 10-K, 10-Q, 20-F and 11-K, then 8-K, Form 3, Form 4 and Form 5 due dates, plus the Part III deadline for a 10-K that omitted it.

## What an answer looks like

The free sample, `form_10_k_due_date_example`, is a stored real answer and it is the cheapest way to judge the shape before paying for anything. For a fiscal year ending **2026-12-31** at an **accelerated** filer it returns `due_date` **2027-03-16**, `unadjusted_due_date` **2027-03-16**, `days_left` **115**, a `17:30` cutoff in `America/New_York`, and then four blocks a finance reader actually needs:

- **`period_end_basis` and `filer_category_basis`** - whether the input was taken from the question or read from EDGAR, so a projected date can never be mistaken for a filed one.
- **`scenarios`** - on a call where the category was read from EDGAR rather than given, all three categories are returned with the one that applies marked `applied: true`.
- **`caveats`** - coded, not prose, so a client can act on them: `ROUTE_NOTE`, `PERIOD_PROJECTED`, `PERIOD_ESTIMATED_52_53_WEEKS`, `CATEGORY_AS_OF_TODAY`, and `CALENDAR_AS_OF` which carries its own `as_of` date for the holiday list.
- **`source`** - six citations, each with a URL, a `sha256` and a `captured_on` timestamp: the Form 10-K general instructions from sec.gov, eCFR 17 CFR 240.12b-2 for the filer definitions, 17 CFR 240.0-3 for the business-day roll, the OPM federal holiday page, and a staff interpretation naming March 31 as the calendar-year due date.

## Driven, four calls

- **The arithmetic reproduces by hand.** Accelerated filer, `period_end` **2026-12-31**, seventy-five days later is **2027-03-16**, and `days_left` from the sample's own `computed_on` of **2026-11-21** is **115** - both exact.
- **A real company, the paid route's free trial.** Apple at CIK **320193**, padded by the server to `0000320193`, fiscal year ended **2026-09-26**, large accelerated filer: due **2026-11-25**, `days_left` **-3** on a `computed_on` of **2026-11-28**. Sixty days after 2026-09-26 is 2026-11-25, and a negative `days_left` is the honest answer for a deadline that has passed rather than an error.
- **The CIK-only path reads EDGAR and says so.** Passing only `cik: 320193` and no period end returned `period_end` **2027-09-25** with `period_end_basis` **`edgar_anniversary_estimated`**, an `alternate_period_end` of **2027-10-02**, `filer_category` **large_accelerated_filer** with basis **`edgar_current`**, due **2027-11-24**, `days_left` **361** - plus a `PERIOD_ESTIMATED_52_53_WEEKS` caveat, which is correct: 2026-09-26 fell on a Saturday, so the fiscal calendar is a 52-53 week year and the next period end is an estimate, not a fact.
- **All three filer categories are priced in one answer.** The same call returned large accelerated **2027-11-24** (`applied: true`), accelerated **2027-12-09** and non-accelerated **2027-12-27**. Those are the 60, 75 and 90 day counts off 2027-09-25 exactly - and the non-accelerated line carries `unadjusted_due_date` **2027-12-24** against a `due_date` of **2027-12-27**, because 25 December 2027 is a Saturday, so the observed holiday is Friday the 24th and the deadline moves to the following Monday. That single field pair is the reason to use this instead of a formula.

## Where the money is

Two of the four calls returned a payment requirement rather than an answer, and the shape is worth recording because this catalog had not carried an x402 **MCP** paywall with a published price list before. `form_4_due_date` and `form_8_k_due_date` both answered HTTP 200 with `isError: true` and a v2 challenge in `structuredContent`: **0.005 USDC**, `scheme: exact`, network `eip155:8453` (Base), asset `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`, payee `0xa1caaece13804f600df4affd88455395422d5eac`, a **300 second** payment window, and a `bazaar` extension that publishes the tool schema and a worked example with every listing. A client that reads only the `content` block gets one plain sentence naming the tool where the free trial lives; the machine-readable half is there for clients that pay automatically.

The published examples are themselves checkable, which is the point of a catalogue entry: Form 4 for a transaction on **2026-11-20** returns **2026-11-24** (two business days: Monday the 23rd, Tuesday the 24th), and Form 8-K item 2.02 for an event on **2026-11-20** returns **2026-11-27** - four business days that skip Thursday 26 November, Thanksgiving. A naive four-day count answers the 26th and is wrong.

## Two defects, both reproducible

1. **The schema says nothing is required; the runtime refuses a call for a missing parameter and does not name it.** `form_10_k_due_date` declares `"required": []`, so a client may legitimately call it with no arguments - and that call answers `isError: true` with *"Tool execution error: PARAMETER_MISSING: A required parameter is missing from the question."* The parameter that is actually needed is `period_end`, or `cik` to project one, and neither the schema nor the message says so. The same sentence hides both routes.
2. **The calendar is older than the calculation.** `computed_on` moves with the day of the call - 2026-11-21 on the stored sample, 2026-11-28 on the live calls - while `CALENDAR_AS_OF` stayed at **2026-11-21** on all three. For a business-day deadline that is the field that matters, and a reader has no way to tell from `days_left` alone whether a fresh SEC closing announced this week is in the list. The caveat text is honest about the boundary; the output would be stronger if `computed_on` and `as_of` were never allowed to diverge silently.

## Where it belongs

This is a **calendar** service, not a filings service - it does not read a 10-K, it tells you the day one is owed - and that is why it does not collide with the SEC filing-intelligence and filings-search servers already on this shelf. Pair it with a filings reader: the reader answers *what was reported*, and this answers *when the next one is due and whether the last one was late*. For an operator running a public company, a subsidiary with its own registrants, or a finance team building a compliance calendar, the useful part is the trio of caveat, basis and source on every row: the answer can be audited, and when the analyst disagrees with the date they can see which rule and which holiday list produced it.

```json
{
  "mcpServers": {
    "filing-deadlines": {
      "url": "https://filing-deadlines.amacunia.fr/mcp"
    }
  }
}
```

## Also worth knowing

### Which parts answer without paying?

Only one route tool does, `form_10_k_due_date`, with `free_trial: true`, at **three calls a day per caller** shared with the vendor's web route; every other tool returns its price. `form_10_k_due_date_example` is untimed and returns a stored answer computed on 2026-11-21, so a reader can see the full shape - caveats, scenarios, six citations with fingerprints - before deciding to pay. Payment is per call and only on success, the server is stateless between calls, and there is no account, no API key and nothing to revoke, which makes this one of the easier services in the catalogue to try and one of the harder ones to budget without a usage cap of your own.

The disclosure that matters for a finance workflow: the answers carry the statute, the date and a hash of the document read, so a reviewer can re-fetch the same eCFR section and compare. That is a stronger audit position than most compliance tools in this catalogue, and it is the reason this entry rests on the rule text rather than on the vendor's summary of it.
