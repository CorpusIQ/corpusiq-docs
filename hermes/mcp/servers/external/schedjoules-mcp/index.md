---
title: "SchedJoules MCP - Public and Holiday Calendars"
description: "Searches thousands of public calendars - holidays, school breaks, sports fixtures, dividend dates - and returns the next events with no key."
category: "Productivity / Calendar Data"
stars: "n/a (hosted vendor endpoint; no MCP wrapper published)"
added: 2026-11-20
source: "the mcp.so submission queue entry #7708 filed 2026-11-20T15:09:22Z, a keyless initialize the same hour, the full tools/list, and ten driven tools/call requests across five calendars (Netherlands public holidays, Dutch school holidays, Ajax fixtures, Prudential Financial dividend dates, and search queries for financial events and weather) plus four refusal paths"
relevance: ★★
tags: [calendars, holidays, school-holidays, sports-fixtures, dividends, scheduling, remote, keyless, free]
last_updated: "2026-11-20"
---

# SchedJoules MCP

**Every business that schedules people is guessing at the same dates: when schools close, when the fixture list lands, when a dividend is paid. This server reads those calendars instead of guessing.**

```text
Server type:   remote Streamable HTTP, keyless (no session id issued on initialize)
Endpoint:      https://www.schedjoules.com/mcp
Server:        schedjoules 1.0.0, title "SchedJoules calendars", protocol 2025-06-18
Vendor:        https://www.schedjoules.com (HTTP 200)
Auth:          none, public and read-only
Tools:         3, all read-only, all idempotent
```

## What the server is

SchedJoules has been selling calendar subscriptions to phone makers for years; this endpoint exposes the catalogue to an agent. The `initialize` response states the shape of the product before any tool is called:

> SchedJoules has thousands of public calendars: public and school holidays, sports teams and competitions, TV, weather, moon phases, financial events. Use `search_calendars` to find one, `get_upcoming_events` to see what is next on it, and `get_subscribe_link` when your user wants it in their own calendar. The event lists are a preview (at most 5 events in 60 days).

Two of those sentences are the whole design: the catalogue is large, and the read surface is a preview bounded to **five events inside sixty days**. The subscribe link is the product; the tool output is the trailer.

## The three tools

| Tool | Arguments | What comes back |
|---|---|---|
| `search_calendars` | `query` (1-100 chars, "one or two words work best") | up to **20** calendars with id, name, kind and country |
| `get_upcoming_events` | `calendar_id` (numeric, 1-12 digits) | at most **5** events in the next **60** days, plus `structuredContent` with the same events as objects |
| `get_subscribe_link` | `calendar_id` | the deep link that adds the calendar to the user's own calendar app |

Every response carries a `content` text block **and** a `structuredContent` object, so an agent can read prose or parse fields. The structured form is the better one: `{"title":"Christmas Day","start":"2026-12-25","allDay":true,"timeZone":null}` is unambiguous where the text is a bullet list.

## Holidays, measured

`search_calendars` for *netherlands holidays* returned **20** calendars - and the first six are the ones that matter:

```text
Public Holidays (Holidays, Netherlands)                id 50077
Public Holidays and Observances (Holidays, Netherlands) id 49733
School Holidays Middle (Holidays, Netherlands)          id 50079
School Holidays North (Holidays, Netherlands)           id 50078
School Holidays South (Holidays, Netherlands)           id 50080
Islam Holidays (Holidays)                               id 49753
```

`get_upcoming_events` on **50077** answers the question a planner actually asks:

```text
2026-12-25 (all day): Christmas Day
2026-12-26 (all day): Second Christmas Day
2027-01-01 (all day): New Year's Day
```

And on **50080**, the southern school region:

```text
2026-12-19 (all day): Kerstvakantie
```

Read those two together and the staffing answer falls out: the Dutch south starts its Christmas break on **19 December**, six days before the public holiday, so a rota built on the public holiday alone is short by a week.

## Fixtures and dividend dates

Sports calendars are scheduled with times, not all-day flags. Ajax (**29128866**) on 2026-11-20:

```text
2026-11-22 13:30 UTC  Ajax - ADO Den Haag
2026-11-26 17:45 UTC  Ajax - FC Thun
2026-11-29 13:30 UTC  Feyenoord - Ajax
2026-12-03 20:00 UTC  Ajax - FC Den Bosch
2026-12-06 13:30 UTC  Ajax - FC Utrecht
```

The financial calendars are the find this catalog did not have: a search for *financial events* returns **Financial Calendars** entries for Prudential Financial, Regions Financial, Capital One, Synchrony, Truist, Cincinnati Financial and Manulife, and `get_upcoming_events` on Prudential (**58726**) returns the dividend sequence:

```text
2026-11-24 (all day): Projected Ex-Dividend Date
2026-11-24 (all day): Projected Record Date
2026-12-10 (all day): Dividend Payment
2026-12-17 (all day): Projected Payment Date
```

The word *Projected* is in the event titles themselves, which is the honest part: the vendor is telling you which of the four dates the company has confirmed and which it has modelled.

### Can it tell me when the Dutch school holidays start?

Yes, and with the caveat that matters: the answer is region-specific. The Netherlands has three school-holiday calendars (north, middle, south) and they do not agree. Search by country, then pick the region your staff live in - the tool will not pick for you.

### Can it answer a full-year planning question?

No. The preview is capped at **five events inside sixty days**, so "all Dutch public holidays in 2027" cannot be read from `get_upcoming_events`. The full calendar is behind the subscribe link, which lands in the user's own calendar app - a deliberate product boundary rather than a bug, but it changes how an agent should use it: ask about the next two months, subscribe for the year.

## Where it stops

- **Search is keyword matching, not filtering.** The query *financial events* returned **FC Basel 1893**, **FC Luzern** and **Switzerland (Sports, Football)** inside the same twenty results - *financial* matched the Financial Calendars group and *events* matched events anywhere. A query for *weather* likewise returned ten TV shows named "Weather" alongside the one real City Weather calendar (**90730**). Treat the top of the list as a suggestion, not a filter.
- **The country word does not scope the results.** *netherlands holidays* returned Germany (Bayern, Hessen, Berlin, Niedersachsen), France (three school zones), Belgium (Flanders) and Australia (NSW) in the same page. The Dutch calendars sort first, so the ranking is doing the scoping, not the query.
- **Twenty is a hard cap, with no paging argument.** A broad query silently truncates at 20 with the text "(at most 20)".
- **The subscribe link is not an ICS URL.** It opens the SchedJoules app (App Store id **853708554**, Play package `com.schedjoules.sync`) which then writes into Google, Apple or Outlook. An agent cannot hand the user a feed URL, and a user without the app lands in a store.
- **Refusals are precise, which is worth noting.** An out-of-range id returns `calendar_id must be the number from search_calendars.`; an id that does not exist returns `There is no SchedJoules calendar with id 1. Use search_calendars to find one.`; an empty or missing query returns `Give a query: a team, a competition, a country or a kind of holiday.` All three come back with `isError: true` in a text block - readable by any client, no structured error code to parse.
- **No write surface at all.** Nothing here changes a calendar; the only side effect is the user tapping a link.

## What it costs

Nothing. The endpoint is public and read-only, no account and no key; the commercial model is the app subscription the link sells, which is the vendor's business, not the caller's.

## Add it to Hermes

```bash
hermes mcp add schedjoules --url https://www.schedjoules.com/mcp
hermes mcp test schedjoules
```

Then ask it the question an operations lead actually has: *when do schools in the south of the Netherlands close, and what is the next public holiday after that?* The answer is two calls and a subtraction, and it beats a web search that returns last year's calendar.

## Why it earns a slot

Scheduling content - rotas, promotions, deliveries, support cover - is decided on dates that live in someone's head or in a PDF that updates once a year. This server carries the same dates the phone vendors ship, dated, in a structured field, with the public-holiday, school-region and dividend variants kept separate instead of averaged into one. That is a small surface with a real job, and it is the first calendar-data entry in this catalog.
