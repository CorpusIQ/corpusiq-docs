---
title: "American Adventurer MCP - 19,286 Public-Land Camps"
description: "A keyless MCP server for 19,286 public-land camp records that names its source, its date and the fields it does not hold, driven through all fourteen tools."
category: "Outdoor / Public Data"
stars: "0 (remote Streamable HTTP, keyless; fourteen tools, all fourteen driven)"
added: 2026-11-16
source: "the mcp.so submission queue entry #7478 filed 2026-11-16T20:10:59Z, and a driven session on 2026-11-17 in which all fourteen tools were called over Streamable HTTP, 21 tools/call requests in total"
relevance: ★★★
tags: [camping, public-land, recreation, weather, keyless, remote, mcp]
last_updated: "2026-11-16"
---

# American Adventurer Camps

**Ask an assistant where to camp for free outside Bozeman and it will name a site.** The answer will sound authoritative and it will be assembled from a training corpus that has no record of a gate, a fee change or a closure order, and no way to say which of those it does not know. The repair is not a better prompt. It is a source that carries the managing agency, the evidence for the cost verdict, the date the record was built, and a list of the fields it does not hold.

American Adventurer is that source for **19,286** camp records on United States public land, served over MCP with **no key, no account and no sign-in**. This pass drove all **fourteen** tools through **21** `tools/call` requests, five of them deliberate failures, and the property that earned the page is the one hardest to fake: every answer names its record, its source, its date, and the fields it does not hold, and the arithmetic in its two calculators reconciles by hand.

```
Server type:   remote Streamable HTTP
Endpoint:      https://davelalande.com/mcp
Server:        American Adventurer, version 1.0.0, title "American Adventurer camp records"
Protocol:      2025-06-18
Auth:          none (no key, no account, no OAuth)
Tools:         14
Website:       https://davelalande.com
Listed on:     the mcp.so submission queue as #7478
Registry:      a search of the official registry for "adventurer" returned zero records
```

## The evidence tier

**Keyless and driven.** `initialize` answered **200** as *American Adventurer* **1.0.0** on protocol **2025-06-18** with no session identifier and no credential at any point. `tools/list` returned **fourteen** closed schemas, and every one of the fourteen was called: `find_camps` four times, `rig_math` twice, `camps_near` twice, `land_at` twice, `camp_detail` twice, and `what_we_cover`, `free_camping_near_town`, `plan_four_nights`, `forest_weather`, `changes_since`, `trip_check`, `game_leaderboard`, `one_call` and `trip_status` once each.

Five of the calls were built to fail: an unmatched search word, a radius outside the schema, a trip code that does not exist, a slug that does not exist, and a point in the Pacific Ocean.

## The tool surface

| Tool | Key arguments | What it answers |
|---|---|---|
| `find_camps` | `q`, `state`, `cost` (free, fee, unpriced, license), `water` | Up to **10** matching records with cost and its evidence, nearest named water, stay limit, nearest town. |
| `camp_detail` | `slug`, `date` | The full record plus nearest fuel, grocery, pharmacy, hospital and hardware, the nearest toilet, the season reading for a date, and the fields not held. |
| `camps_near` | `lat`, `lon`, `radius_mi` (1 to 50), `cost`, `limit` | Records inside a straight-line radius, nearest first. |
| `free_camping_near_town` | `town`, `state`, `limit` | Up to **5** free camps within **25** straight-line miles of a town. |
| `plan_four_nights` | `forest_slug` or `town`, `nights` | A trip letter: which camps, which nights, the distance between stops, the season reading for each. |
| `forest_weather` | `camp`, `forest`, `town` | A National Weather Service forecast for the position of the camp record, plus what the records say about camping there. |
| `trip_check` | `forest` or `camp`, `start`, `nights`, rig numbers | A water and fuel ledger for a specific trip on specific dates. |
| `land_at` | `lat`, `lon` | Whose land a point is, national forests only, with the managing office. |
| `changes_since` | `camps` (1 to 3), `since` (30 days back) | What changed at up to three camps, and what is not watched. |
| `what_we_cover` | `job` | The coverage table: every job, whether held, how many records, source, date, and the gap. |
| `rig_math` | `water_gal`, `gas_gal`, `people`, `nights`, `mpg` | Tank arithmetic with its assumptions printed. |
| `game_leaderboard`, `one_call`, `trip_status` | `challenge`, `code` | The author's public camping game: checked runs, one shared decision, trip status. |

## What the coverage table admits

`what_we_cover` is the reason the rest of the answers are quotable. It returns a row per job with the count, the source, the date, and the gap stated rather than implied:

| Job | Holds | Count | As of |
|---|---|---|---|
| Where can I camp | yes | 19,286 | 2026-10-25 |
| Is it free or does it charge | yes | 12,848 | 2026-10-25 |
| Who manages the land | yes | 18,767 | 2026-09-24 |
| Rules and stay limits | partly | 5,067 | 2026-09-24 |
| Season and closures | partly | 1,103 | 2026-09-27 |
| Fire rules and restrictions | partly | 916 | 2026-09-24 |

Three of the six rows say **partly**, and the gap column says why in each case: **1,329** camps are *unpriced*, which the table distinguishes from free; stay limits are recorded for **2,254** camps only; the season row is a snapshot from the build rather than a live closure feed. A server that publishes **12,848** of **19,286** cost verdicts and says so is more useful than one that quietly rounds the rest to zero.

## The arithmetic that reconciles

Two tools are calculators, and both were reproduced by hand.

`rig_math` on **40** gallons of water, **20** gallons of gas and **2** people returned **20.0** days and **20** whole nights, which is 40 / 2 people / 1 gallon per person per day. The same 20 gallons at **13** mpg returned **260** road miles, and the same fuel by road surface returned **200** on gravel or dirt, **160** on rough road and **120** off road, which are 10, 8 and 6 mpg. Every number is the stated input divided by a printed assumption, and the assumptions are labelled as the game's numbers rather than as measurements.

`trip_check` for three nights in Custer Gallatin from 2026-11-20 with a truck carried a water ledger that closes: **1.4** gallons a night, **1.0** a day between nights, so nights 1, 2 and 3 need **6.2** gallons in total (1.4 + 1.0 + 1.4 + 1.0 + 1.4). Starting with **5** gallons aboard, the ending balances read **3.6**, **1.2** and **0**, the third night is flagged `ran_short: true`, and the shortfall is **1.2** gallons, which is exactly 6.2 - 5.

## What a search actually returns

`find_camps` for **hyalite** in Montana with `cost: free` and `water: true` answered **5 of 23** matching records, each carrying the record URL, the land manager (**USFS**), a record date of **2026-09-24**, the cost verdict with its evidence (*The Forest Service inventory lists no fee*), the nearest named water with its USGS source and straight-line distance, coordinates, and an `unrecorded` list. Arizona with the same filters returned **5 of 192**. `free_camping_near_town` for **Bozeman**, Montana returned **98** free camps inside 25 straight-line miles, and `camps_near` on 45.45, -110.78 at a 25 mile radius returned **292**.

The season reading is worked out for a date rather than cached. `plan_four_nights` for Custer Gallatin put night 1 at **Macnab Pond** on the record text *All Year Weather Dependent*, reported `state: open` on 2026-11-17, and on the same call reported **Ghost Road** for nights 2 and 3 as `season not recorded: check with USFS`, **13.7** straight-line miles from the previous stop.

## Refusals, five of them

| Call | Response |
|---|---|
| `find_camps` with `q: nowherezzz` | *No camp in the records matches that. Nothing is named from memory.* |
| `camps_near` with `radius_mi: 80` | *radius_mi must be between 1 and 50.* |
| `camp_detail` with an unknown slug | *No camp record has the slug "no-such-camp-zzz". Find the slug with find_camps.* |
| `trip_status` with an unknown code | *No Dispersed 3D trip has the code ABCD-2345. Check the code the game showed, or ask the person to read it again.* |
| `land_at` at 36.0, -140.0 | *By the record, this point is not on national forest land... Signs on the ground and the office win.* |

The last one is the distinctive refusal: the tool could have returned a country name or an ocean label. It returns what it knows (not national forest), what it does not cover (every other manager), and who has the final word (the signs and the office).

## Two things the answers say about themselves

`changes_since` for one camp since 2026-11-10 answered *Nothing new in what we watch. That is not the same as nothing changed.*, and then listed what **is** watched (a weather alert and a record rebuild) beside what is **not**: fire reports, because the feed carries no discovered date, and season flips, because the record holds no window. That is a change feed which tells a caller where its own blind spot is.

`forest_weather` returned a National Weather Service forecast stamped **2026-11-17T04:03:13+00:00** for the position of the named camp record, not for a nearby town: tonight **36F**, Tuesday **49F** with **72%** precipitation, Tuesday night **29F** with **99%**. The instructions say never to give weather from memory, and the tool returns the fetch timestamp so a caller can see how current it is.

**One behaviour worth naming, because it was not announced.** Every record URL in every answer carried `?via=`, and the token inside it changed with the calling client: `via=corpusiq-sweep` from a `CorpusIQ-sweep/1.0` user agent and `via=mozilla` from `Mozilla/5.0 probe`. The server appends an attribution token derived from the caller's own user agent. It is recorded here as observed behaviour, not as a vendor claim.

## Is this worth a connection?

For an assistant that plans trips, answers camping questions, or has to say *I do not know that* about land, yes. The coverage is one country, the records are free to read, and the design choice that matters is the refusal to fill a field: an answer that says *stay limit unrecorded, ask the district office* is usable in a way that a plausible stay limit is not.

It is not a booking system, it does not carry live road conditions, current fire restrictions or permit prices, and it says so in its own instructions. Distances are straight-line miles, not drive miles.

## FAQ

### Does American Adventurer need an API key or an account?

No. `initialize`, `tools/list` and all **21** `tools/call` requests ran with no credential of any kind.

### How do I find free camps with water near a town?

`free_camping_near_town` with a town and a state. Bozeman, Montana returned **98** free camps within **25** straight-line miles, each with cost evidence and the nearest named water source.

### What does `unrecorded` mean in the output?

That the field is not held for that record. The server's own instructions say to state it as not recorded and never estimate it, which is why the same object carries `stay_limit: unrecorded` beside a fully populated water entry.

### Can it tell me whose land a point is?

Only inside national forests. At a point outside them it says so and refuses to guess at the manager, which is the correct answer for a map record that is not a title record.

### Is the weather live?

It is a National Weather Service forecast fetched at call time for the position of a camp record, with the fetch timestamp in the response. It is not a closure or a fire feed.
