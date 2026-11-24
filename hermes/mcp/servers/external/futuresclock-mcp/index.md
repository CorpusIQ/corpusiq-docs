---
title: "Futures Clock MCP - China Futures Market Calendar"
description: "Free keyless answers on whether a China futures market is open, which trading day a night session belongs to, when a contract expires and what changed."
category: "Finance"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-24
source: "Submission chatmcp/mcpso #7990 filed 2026-11-24T15:02:31Z; a keyless initialize on https://mcp.futuresclock.com/mcp answering 200 as china-futures 0.1.0 with six tools; seven tool calls driven 2026-11-24 on SHFE, HKEX, CFFEX and LME; the vendor page futuresclock.com/en/mcp read the same day; the official source URLs each answer cites (shfe.com.cn, hkex.com.hk, lme.com)"
relevance: "★★★"
tags: [futures, china, market-calendar, exchange-holidays, contract-expiry, trading-sessions, reference-data, remote-mcp, keyless]
last_updated: "2026-11-24"
---

# Futures Clock MCP

**The question a trading desk asks before every order is not "what is the price" but "is this market open, and which trading day is this".** Futures Clock answers exactly that for China's futures markets and 24 other scopes: trading days, session hours, night-session attribution, contract expiry dates, and the rule changes and notices the exchanges publish. It returns no prices and runs no expiry engine, which is the point. It is a calendar and a paper trail, and every answer names the official document it came from.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.futuresclock.com/mcp
Auth:        none - free, no key, read-only (vendor states this on futuresclock.com/en/mcp)
Server name: china-futures 0.1.0, protocol 2025-06-18
Tools:       6 (trading_day, next_closure, trading_hours, contract_expiry,
             recent_rule_changes, recent_notices)
Pricing:     free
```

## What a keyless client actually gets

An `initialize` with no credential answers **HTTP 200** and six tools, so an operator can read the whole surface before deciding anything:

| Tool | The question it answers |
|------|------------------------|
| `trading_day` | Is this date a trading day on this exchange-local calendar, and which trading date does today's night session belong to? |
| `next_closure` | What is the next published exchange holiday or half-day? |
| `trading_hours` | Which sessions does this product trade, in which time zone, with what day offsets? |
| `contract_expiry` | What are the published last-trading and first-notice dates for a product and month? |
| `recent_rule_changes` | What margin, price-limit, position, fee, delivery or listing changes were published in the last 90 days? |
| `recent_notices` | What notices exist for an exchange and topic, inside at most 30 days? |

## The night-session answer, measured

The single most useful thing here is the attribution rule, because it is where cross-border teams get it wrong. Asking for SHFE on **2026-11-24** returned:

```
day:          open, is_trading_day true
night_session: civil_date 2026-11-24 -> trading_date 2026-11-25
source:        shfe.com.cn holiday calendar (official)
last_verified: 2026-09-29, valid_through 2026-12-31
data_version:  2026.10.22-rc.1, rights_status approved_public_reference
```

So the session that opens on the evening of the 24th is the **25th's** trading day. An agent that books a fill to the civil date is wrong by one day, and the answer here is not a guess: it carries the SHFE calendar URL, the verification date and the validity horizon.

The same call for **HKEX on 2026-12-25** returned `closed` with `reason: holiday`, `holiday.name_en: Christmas Day`, `name_zh: 圣诞节`, sourced to an HKEX participant circular PDF and dated `last_verified 2026-09-29`. Two markets, two time zones, two official sources, same envelope.

## Sessions with explicit day offsets

`trading_hours` on **shfe-cu** (沪铜, Copper) returned four sessions and, unusually, every open and close carries its own `day_offset`, `offset_unit` and `anchor`:

```
Day session    09:00 -> 10:15   offset 0 calendar-day, anchor trading-date
Day session    10:30 -> 11:30   offset 0 calendar-day, anchor trading-date
Day session    13:30 -> 15:00   offset 0 calendar-day, anchor trading-date
Night session  21:00 -> 01:00   open offset -1 business-day, anchor trading-date
```

The night session is expressed relative to the trading date rather than as a wall-clock range, which is why a client can compute "is it open right now" across a daylight-saving boundary in another market without hardcoding offsets. `weekly_pattern` was `[1,2,3,4,5]` and `valid_from` was **2026-07-06**, so the template carries its own effective date instead of pretending the schedule never changes.

## Expiry, from the exchange file

`contract_expiry` for **shfe-cu, month 202612** returned `exchange_symbol cu2612` with:

- `last_trading_day` **2026-12-15**, status `verified`, verified 2026-11-20, source `https://www.shfe.com.cn/data/busiparamdata/future/ContractBaseInfo20261120.dat`
- `first_notice_day` **null**, status `unknown`, reason `not_published`
- `estimated: false`, and a link to the contract page

The null is the honest part. The tool refuses to run an expiry engine and says so in its own description: an unpublished date stays unknown rather than being interpolated from a rule of thumb.

## Rule changes and notices, with the notice attached

`recent_rule_changes` for SHFE returned a dated record: on **20 November 2026** the exchange approved a state grain-reserve depot in Foshan, Guangdong as an aluminium delivery warehouse with **15,000 t** capacity and no regional premium, citing `shfe.com.cn/publicnotice/notice/202611/t20261120_834157.html`. That is a delivery-cost input a hedging operator needs, published with its own source link.

`recent_notices` for SHFE with `topic: margin` returned **no items**, and said why in machine-readable form: `requested_window 2026-11-19 to 2026-11-25`, `available_window 2026-11-11 to 2026-11-24`, `complete_window false`, status `unknown`. It also carries the Chinese disclaimer **以交易所官方文本为准** (the exchange's official text prevails) inside the payload, so a client cannot strip the caveat by accident.

## Where the coverage ends, measured

Two gaps were reproduced on 2026-11-24 and they matter for how you wire the tools:

1. **`next_closure` does not resolve Chinese exchanges.** SHFE and CFFEX both returned `value: null`, `status: unknown`, `status_reason: outside_coverage`, while **LME returned `2026-12-25, Christmas Day, closed`** from `lme.com` official trading-times. The tool's own description explains it: it matches the publisher's holiday market IDs directly, and a product slug or an exchange outside that list stays unknown. Use `trading_day` for Chinese calendars.
2. **A product slug on `trading_day` resolves the night session but not the day.** `exchange: shfe-cu` returned the correct night and incoming-night attribution with `scope: venue_calendar` and an empty `coverage` array, so `day.value` came back `null` with `status_reason: not_published`. Pass the exchange code (`SHFE`) when you need the day answer.

A smaller inconsistency worth knowing: `next_closure` cites `exchange-holidays-2027.json` and `-2028.json` in its citation block even while answering `outside_coverage`, so the citation is not evidence that a specific exchange is covered.

## What it is built on

The answers are an aggregation, and the payload says so in public: exchange calendars from **marketsopen.today** (CC BY 4.0), published notices from **chinaexchangecirculars.com**, and contract data as Futures Clock's own dataset **1.9.19** with a DOI in the citation. Coverage is limited by scope, stated per market: SHFE, INE, DCE, CZCE, GFEX and CFFEX for China, HKEX cash equities, SGX equity/FX/rates, plus LME, ICE, COMEX, CBOT, CME, NYMEX, EUREX, OSE, JPX, KRX, TWSE, BSE, SSE, SZSE, SGE, NB, SB and BMD.

## How to connect

Claude, Claude Code, Cursor or VS Code, no header and no key:

```
claude mcp add --transport http china-futures https://mcp.futuresclock.com/mcp
```

```json
{ "mcpServers": { "china-futures": { "url": "https://mcp.futuresclock.com/mcp" } } }
```

## Is a free calendar worth connecting?

Yes, if anyone in the business has to reason about a session boundary. The cost of getting it wrong is a mis-dated fill, a settlement booked to the wrong day, or a delivery notice missed because the exchange published it in Chinese on a Friday. The tool is free, keyless and citable, and its refusals are informative rather than silent: `outside_coverage` and `not_published` are answers a client can route on, which is more than most paid reference feeds give you.

## What this guide can and cannot certify

Verified on 2026-11-24: the keyless handshake, all six tool schemas, the SHFE trading-day and night-session answer, the HKEX holiday answer, the shfe-cu session template, the cu2612 expiry date and its exchange source file, one SHFE delivery-warehouse notice, and the two coverage gaps above. Not verified: any price, any assertion that a published notice is still current (the tool says published records are not current rules), and any exchange outside the 24 scopes.

## Verdict

The catalogue had price feeds and it had calendars for Western retail markets; it had nothing that answers "which trading day does this night session belong to" for a Chinese exchange with the exchange's own URL attached. **A market calendar that names its source is the cheapest insurance a cross-border desk can buy, and this one is free.**
