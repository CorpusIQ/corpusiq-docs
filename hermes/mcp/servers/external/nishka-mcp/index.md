---
title: "Nishka MCP - Bulgarian Deadlines That Do the Arithmetic"
description: "Driven keyless: a 7-day deadline rolled over a Sunday and a holiday to 29.12.2026, and every fact served with its source URL and check date"
category: "Compliance / Public Data"
stars: "n/a (hosted service, registry app.nishka/nishka 0.2.0, data CC BY 4.0)"
added: 2026-11-13
source: "the submission queue entry #7263, the official registry record app.nishka/nishka 0.2.0 naming the remote https://nishka.app/mcp, and a keyless session on this host: initialize, tools/list and thirteen tools/call requests against the live endpoint"
relevance: ★★★
tags: [bulgaria, legal-deadlines, public-records, citations, compliance, municipal, keyless, mcp]
last_updated: "2026-11-13"
---

# Nishka MCP

**A deadline that lands on a public holiday is not a deadline, and no language model knows which Tuesday in December is the one after Christmas in a country it has never filed anything in.**

The Bulgarian Civil Procedure Code counts a period in days from the day *after* the event, ends periods in months and years on the corresponding date, and moves an end that falls on a non-working day to the next working day. Then a government decision can declare an extra day off in the middle of a tax year, which is exactly what happened on 2 January 2026 under a Council of Ministers decree published in the State Gazette. An assistant that answers from memory will give you a confident date and no arithmetic.

Nishka answers with the arithmetic shown, and attaches an official source URL and a check date to each fact it serves.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://nishka.app/mcp
Transport:   JSON-RPC 2.0 over HTTP, no session needed
Auth:        none for any of the eleven tools
Tools:       11, read from a live tools/list
Built by:    Nishka (nishka.app), Plovdiv
Registry:    app.nishka/nishka 0.2.0 (0.1.0 also published)
Licence:     Основа facts CC BY 4.0; attribution string served by about_osnova
Coverage:    120 Основа entries, 514 facts, four cities; four Извор sources
```

## The evidence tier

Everything below was measured on 2026-11-13 between 17:05Z and 17:25Z against the live endpoint, with no key and no account: `initialize` returned HTTP 200 as `ap...` on protocol `2025-06-18` with tools, resources and prompts, `tools/list` returned **11** tools, and **thirteen** `tools/call` requests were driven, each returning `isError: false` and a `structuredContent` block alongside the text. Nothing here is quoted from the vendor's submission text.

## Why This Matters for Operators

Two kinds of paper cost a small business real money: a filing deadline missed by one day, and a fee paid twice because nobody knew which counter charged what. Both are answered by a public body on a web page that was written for a citizen reading Bulgarian in a browser, not for an agent.

Nishka is the first surface this catalog carries that does the **statutory date arithmetic** and the **public-record lookup** in one place, for a jurisdiction the catalog had nothing on. The interesting part is not the coverage, which is small and says so. It is that every answer arrives with the source and the date it was checked, and at least one tool says plainly where its own knowledge stops.

## What It Actually Does

| Tool | What it answers |
|---|---|
| `srok_deadline` | Counts a legal period the way ГПК чл. 60 does, from a date plus an amount and unit of days, weeks, months or years |
| `srok_day` | Whether one date is a working day in Bulgaria, and the legal basis when it is not |
| `srok_year` | Every non-working weekday and every working Saturday in a year, 2020 to 2099, each with its basis |
| `search_osnova` | Searches 514 checked facts about public services in Plovdiv, Sofia, Varna and Burgas |
| `get_osnova_entry` | One entry with all its facts, each carrying its own source and check date |
| `about_osnova` | Coverage counts per city, the last check date, a content hash and the attribution string |
| `search_izvor` | Searches an index of primary official sources: State Gazette, parliamentary acts, public procurement |
| `get_izvor_document` | One source record with its stored excerpt and the first and last time Nishka saw it |
| `about_izvor` | Which sources are indexed, how many records each holds, and when each was last collected |
| `plovdiv_place_record` | What is known now about one Plovdiv street or quarter: outages, road works, notices, parking zone |
| `plovdiv_changes` | Item-level changes in Plovdiv's official sources since a given date, newest first |

Four cities, one of them covered at street level. That is a narrow product, and the tool is honest about the narrowness.

## Driving it: three windows

### The deadline that should not be a Friday

The clean case first. Fourteen days from Friday 13 November 2026:

```text
srok_deadline {from: 2026-11-13, amount: 14, unit: days}
-> counting starts 14.11.2026 (Saturday); day 14 is 27.11.2026 (Friday)
   last day: 27.11.2026 (Friday)
```

The same call in months shows the rule that matters:

```text
srok_deadline {from: 2026-11-13, amount: 1, unit: months}
-> 13.12.2026 (Sunday) is not a working day, so the period extends
   to 14.12.2026 (Monday).  last day: 14.12.2026
```

And the case with two hops, seven days from Sunday 20 December 2026:

```text
srok_deadline {from: 2026-12-20, amount: 7, unit: days}
-> counting starts 21.12.2026 (Monday); day 7 is 27.12.2026 (Sunday).
   27.12 and 28.12 are not working days (Sunday; the Christmas holiday of
   26.12 falls on Saturday), so the period extends to 29.12.2026 (Tuesday).
```

That last answer is the whole product in one line. A model asked the same question will usually roll a Sunday to Monday and stop, giving 28 December. The correct answer is the 29th, and it needs the holiday rollover rule stacked on top of the weekend rule.

### Where the tool says its own knowledge stops

Two years from 13 November 2026 resolves to 13.11.2028 (Monday) and then volunteers a limit:

```text
"Council of Ministers decisions on additional days off have not been checked
 for the whole period. Check whether the last day has been declared a holiday."
```

A calculator that names the part of the answer it cannot see is worth more than one that is fluent. The 2026 calendar proves the gap is real: it carries 2 January as a one-off non-working day for the adoption of the euro, under a decree that did not exist when the year began.

### The fee, the counter and the documents

`search_osnova` for address registration in Plovdiv returned one entry with a phrase most assistants never produce: no records found, do not assume contacts or deadlines, refer to the institution's official site. A second query hit, and the entry carries per-fact provenance rather than a page-level citation:

```text
where:     the ГРАО desk of the district administration for the address
           (District South: ul. Makedonia 73A, ground floor, 08:30-17:00,
           tel. 032 276 145)
documents: ID; application or address card; proof of ownership or use;
           the owner's written consent if you are not the owner;
           a notarised power of attorney if someone goes for you
fee:       1.02 EUR for a permanent-address certificate, 0.51 EUR for a
           current-address one; double for fast, triple for express
sources:   south-plovdiv.bg/civil-registration and the municipal fees
           regulation, checked 2026-10-14
```

Resident parking is the same shape and the kind of thing that gets paid twice: eligibility limited to one car per dwelling, an exclusion if the property already has a parking space, 7.67 EUR a month or 76.69 EUR a year including VAT, quoted to the article of the parking regulation and the annex of the fees regulation.

### The street record, with read times

`plovdiv_place_record` for ul. Ivan Vazov returned a record assembled from official sources with a **read time per source** rather than one timestamp for the page: outages read at 16:08:07Z, road works at 16:09:35Z, municipal notices at 16:07:15Z, and history kept since 04:07:14Z the same day. It reports no current notices, the paid parking zone with its four sources including the mayor's order as a PDF, and nearby everyday places from OpenStreetMap. The instruction printed in the answer is the right one: cite the notice's own URL and the record URL, with the read time.

## The hand check

The 7-day case was re-derived from the calendar the tool itself serves, not from a second model:

- 2026-12-20 is a Sunday, so counting starts Monday 21.12 and day 7 is Sunday 27.12.
- `srok_day(2026-12-24)` returned non-working, Christmas Eve, and the year list puts 25.12 on a Friday and 26.12 on a Saturday.
- With 26.12 on a Saturday, 28.12 is declared a non-working day under КТ чл. 154, ал. 2, which is the rollover rule that produces the second hop.
- The next working day after 27.12 and 28.12 is Tuesday 29.12.2026, which is what the tool returned.

Two independent answers agree, and both are checkable against the published calendar rather than accepted on trust.

## The defects and the friction, recorded

- **One declared source is empty.** `about_izvor` lists `plovdiv-council` (municipal council decisions) with **0 records** and no last date, beside `eop` with 796 and `dv` with 80. An agent that asks this tool what the council decided gets nothing and has no way to tell an empty source from an unsettled question.
- **The change feed can report a re-read as a change.** Items in `plovdiv_changes` since 1 November carry 13 November read times while the notice text refers to "tomorrow, 31 October" and "Saturday, 31 October". The item identity changed on re-read, not the street. Treat the change feed as a list of pages that moved, and open the notice before acting on it.
- **Coverage is one city deep and three cities thin.** 39 entries for Plovdiv, 37 Sofia, 23 Varna, 21 Burgas, and street-level records for Plovdiv only. The city filter is a real filter, not a suggestion, but a query outside the four cities answers with the same empty-set refusal as a genuine miss.
- **Facts are dated per fact, not per service.** The address-registration entry cites two sources both checked 2026-10-14, while `about_osnova` reports the collection as checked 2026-11-03. Both are true and they are not the same date.
- **Bulgarian-first.** Queries and answers are in Bulgarian, prices have moved to euro, and terms like ГРАО, ВиК and Синя зона are used without translation. That is correct for the jurisdiction and it means the surrounding agent has to carry the translation.

## Connecting it

Remote Streamable HTTP with no authentication, so there is nothing to provision:

```bash
claude mcp add --transport http nishka https://nishka.app/mcp
```

The registry record `app.nishka/nishka` **0.2.0** declares the same remote, and the vendor publishes an `agents.md` and a JSON output mode (`format=json`) on the record tools for callers that want to parse rather than read.

Attribution is a condition of the licence, not a courtesy: the facts are CC BY 4.0 and `about_osnova` returns the exact string to use, with a content hash that lets you tell two readings of the same collection apart.

## Questions this answers that a chat window alone cannot

### When is the actual last day to file?

Ask for the period and the event date, not for the deadline. The tool returns the start rule, the day count and the rollover chain, so the answer can be audited by someone who does not trust the assistant.

### Is this fee the same at every counter?

The public-service entries carry fees with the regulation and the annex that set them, including the multipliers for fast and express service. That is the difference between a price and a receipt.

### Which street is affected this week?

`plovdiv_place_record` and `plovdiv_changes` return the notice URL and the read time, so a claim about a closed lane or a water cutoff can be traced to the municipality's own page.

### Can I ship these facts in a product?

Yes, under CC BY 4.0 with the attribution string the server returns, and with the check date carried into your own output. The data is open; the discipline of keeping the date attached is what makes it usable.

## Verdict

Three stars, on the attribute this catalog keeps rewarding: **the answer can be checked**. The statutory arithmetic is shown step by step and reproduces by hand from the calendar the same server publishes, the facts carry per-fact sources and check dates, and the tool volunteers the one thing it cannot see.

The limits are the shape of the product: one jurisdiction, four cities, one city at street level, one declared source that returns nothing, and a change feed that reports page movement rather than real change. None of that is dishonesty, and all of it has to be carried by whatever agent uses it.

Not for you if you need a European public-record surface across borders. Very much for you if you file, register, pay or park in Bulgaria and want the date and the fee with the article attached.

See also: [Kuotia MCP](/hermes/mcp/servers/external/kuotia-mcp/) for Spanish tax deadlines with a refusal on the unverified quarter, [CalcBloc MCP](/hermes/mcp/servers/external/calcbloc-mcp/) for payroll arithmetic with IRS and FTB citations, and [Casus MCP](/hermes/mcp/servers/external/casus-mcp/) for French tax and legal text.
