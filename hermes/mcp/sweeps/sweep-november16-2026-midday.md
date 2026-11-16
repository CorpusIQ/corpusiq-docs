---
title: "MCP Server Discovery - November 16, 2026 (Midday)"
description: "A flat directory, four feed cards and nineteen queue arrivals in which the only product that earns a page is decided by its own refusal messages."
category: "MCP Ecosystem"
last_updated: "2026-11-16"
---

# MCP Server Discovery - November 16, 2026 (Midday)

Fired on the **10:00 MST** tick, six and a half hours after the night sweep closed at 03:50 MST. The directory came back **flat to the raw count, flat to every per-map count**, the feed carried **four** cards, and the submission queue carried **nineteen** arrivals. **One** server ships, and it earns the page on the strength of its refusals rather than its feature list.

## The window, measured

```text
mcpservers.org /sitemap.xml      200, fifteen maps named, eleven numbered server maps
raw <loc>, maps 1-11 at 17:05Z   65,551   identical to the 03:50 MST night capture
per-map counts                   7,588 / 5,949 / 6,518 / 6,744 / 6,952 / 6,756 /
                                 9,351 / 6,590 / 4,030 / 2,607 / 2,466
distinct keys, locale-stripped   21,807   on the eleven-map basis, unchanged
priority-servers.xml             200 with 34 distinct keys
remote-mcp-servers.xml           200 with 15 entries and one new route (clockwise)
set diff, eleven maps            0 additions, 0 removals
mcp.so /feed                     200 at 157,281 bytes, 36 server links, 30 stamped
                                 cards, 4 above the 10:50Z cutoff
submission queue #7449 to #7467  19 arrivals, bodies in one authenticated call
```

## The count did not move, and the arithmetic says so

The eleven numbered maps returned **65,551** raw `<loc>` entries against **65,551** at the night capture, map by map, including the `servers/11` **2,466** that two prior passes had to reconcile. The per-map totals sum to 65,551 exactly. A set-identical canonical is a result and not an absence of work: it means the window's arrivals had to come from the feed and the queue, and they did.

**The one movement in the whole surface is outside the eleven maps.** The `remote-mcp-servers.xml` route, which usually carries a handful of entries and no product slugs, published **`clockwise`** under fourteen locale prefixes and one bare form, so a fifteen-URL rise in the union is **one** route and not fifteen listings. It is recorded here rather than counted as an arrival.

## The feed, four cards

Four cards sat above the 10:50Z cutoff, read from the `M/D/YYYY, HH:MM AM/PM` UTC stamp form:

| Stamp (UTC) | Slug |
|---|---|
| 15:47 | `salescloser` |
| 14:04 | `url2pin-mcp` |
| 13:44 | `funding-sales-signals` |
| 11:57 | `enhancv-resume-builder-job-search-8bfdaf` |

**Resume builders are a saturated class here** (Run it by and GenEdAI ModernCV already carry entries), and the other three are sales surfaces whose value is a workflow rather than a dataset. None ships.

## The queue, nineteen arrivals

**#7449** to **#7467**, filed between 11:04Z and 16:29Z, with bodies read in one authenticated call. The window is dominated by company-registry and rate-data surfaces, which are the two classes this catalog has ruled on most often:

- **APIEmpresas** (**#7449**) Spanish company data by CIF from BORME, keyless with an npm stdio package. Held on the company-registry class rather than on quality: the catalog already carries Reestr Reestrov for Russian registries and cvrradar arrived in the same window for Denmark, and a per-country registry expansion is a decision about scope, not about this server.
- **cvrradar** (**#7458**) Danish CVR register with owners, group structure and a credit rating. Same class, same reason.
- **RateSonar** (**#7452**) a dated archive of what Australian banks advertised since 2026-06-12, driven to a keyless `initialize`. Held on the rate-benchmark class owned by [MonitorBankRates](/hermes/mcp/servers/external/monitorbankrates-mcp/), which benchmarks deposit and loan prices, and by SafeRate beside it.
- **AIScoreboard** (**#7457**) AI model API prices with a source type and a check date on every line, keyless. Held on the pricing class, where Etuki was dispositioned on 15 November and the cost surfaces (inferenceindexer, cloudcostwise, seatledger) already cover it.
- **StrictScore** (**#7461**) states in its own submission that the API key ships with a US$99 a month enterprise plan, so the server cannot be used without paying. Not a keyless tier and not driven.
- **Improvado** (**#7456**), **Weeklane** (**#7459**), **Saymock** (**#7454**), **blitz.cloud** (**#7453**), **tossithere** (**#7451**) and **Taskthread** (**#7450**) all put an account, an OAuth sign-in or a workspace in front of the data, which is the account-gated class held throughout this week.
- **JanuaPort** (**#7464**) is a self-hosted Docker gateway with a closed core, and **JanuaPort Docs** (**#7465**) is a setup manual for it. The gateway class is covered and a setup manual is not a data surface.
- **Knowità** (**#7462**) is an Italian consultancy presenting its own method and services. Marketing surface, not data.
- **SLF Guardian** (**#7463**), **spm** (**#7455**) and **AI ELM** (**#7467**) are local or single-purpose: a package and command checker, a systemd and launchd service manager, and a phone-bridged OBD2 reader for one car.
- **Based Loans** (**#7466**) is a lending protocol on Base. The crypto surface stays held, consistent with the DeFi dispositions of the past two weeks.

## What ships

**[GoGiga](/hermes/mcp/servers/external/gogiga-mcp/)** (**#7460**), keyless, four tools, **23** `tools/call` requests across all four. First entry here for a live event listing in any country: concert, festival, tour and ticketing all returned zero across the guide tree. Kraków answered **522** concerts across **44** pages and the page arithmetic closes at 12 rows a page on every filtered call; one concert resolved to a primary seller at **od 129 zł** and a resale seller at **od 149,50 zł** flagged as resale, **15.9%** apart; and six wrong calls returned six sentences that name the problem, with the genre refusal printing the full enum so the model can correct itself. Two defects recorded rather than smoothed: the `price_max` filter returned **13** unpriced rows and one row at **109 zł** inside a 100 złoty cap, and `list_festivals` round-trips `type: tour` as **`trasa`**, a value outside its own enum.

## Also identified this pass

The `remote-mcp-servers.xml` route carried **clockwise** under fourteen locale prefixes and a bare form against a directory that is otherwise unchanged, so the fifteen-URL union rise is one route. The feed's four cards are three sales surfaces and one resume builder. Nineteen queue arrivals produced one ship, six account-gated holds, four class holds with the owner named, three local or single-purpose tools and one crypto protocol. `/all` was not re-read: it has answered **403** by edge policy since 4 November, so page-1 membership is absent evidence rather than corroborating evidence.
