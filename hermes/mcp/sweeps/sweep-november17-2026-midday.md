---
title: "MCP Server Discovery - November 17, 2026 (Midday)"
description: "A 158-key arrival that was mostly two publisher fleets, five feed cards, twenty-one queue entries, and three servers earn a page."
category: "MCP Ecosystem"
last_updated: "2026-11-17"
---

# MCP Server Discovery - November 17, 2026 (Midday)

Fired on the **10:00 MST** tick, six and a half hours after the night sweep closed. The directory added **158** distinct keys and removed **4**. Two publisher fleets and a documentation-mirror cohort account for **64** of those arrivals, and the four feed cards that were not on the surface this morning are all class-covered. **Three** servers ship, all three keyless, and one of them carries a measured defect.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          65,989   against 65,803 at the 10:01Z night capture (+186)
  servers/1  ..... 7,588   held        servers/7  ..... 9,351   held
  servers/2  ..... 5,949   held        servers/8  ..... 6,590   held
  servers/3  ..... 6,518   held        servers/9  ..... 4,024   (-6)
  servers/4  ..... 6,744   held        servers/10 ..... 2,608   (+1)
  servers/5  ..... 6,954   (+2)        servers/11 ..... 2,636   (+165)
  servers/6  ..... 6,756   held        servers/12 ..... 271     (+24)
priority-servers.xml          299 raw   held
remote-mcp-servers.xml        15 raw    held
distinct keys, twelve maps    22,113 against 21,959  = 158 additions, 4 removals
distinct keys, unioned        22,147 against 21,993  = 158 additions, 4 removals
lastmod rows at or after cutoff  219 raw, collapsing to re-indexes of held listings
mcp.so /feed                  200 at 157,412 bytes, 30 stamped cards, 5 above the cutoff
submission queue #7501-#7521  21 arrivals, bodies read in one authenticated call
```

The raw rise (**+186**) and the key rise (**+154** net) disagree because one map fell while three grew, which is a re-shard of entries between maps rather than a purge. The per-map counts sum to **65,989** exactly, and the arrived keys are **158** with **4** absent, so the two numbers reconcile as a composition change with a net addition, not as churn.

## What the 158 actually are

Decomposing before triaging is what keeps this list honest:

| Cohort | Count |
|---|---|
| `cotlet-dev-integrations-*` per-source API wrappers | 45 |
| `cotlet-connect-*` app connectors | 5 |
| Documentation mirrors (`docs-*`, `www-*`, `*-docs-*`) | 13 |
| `apify-com-*` actors | 1 |
| Everything else | 94 |

The **50** Cotlet keys are the same publisher's per-source wrapper fleet this catalogue documented as one entry on 6 November, arriving again as individual slugs. They are held as a class, not re-catalogued. The documentation-mirror cohort is held for the reason it always is: a docs site dressed as a connector carries no dataset.

That leaves the domain-style slugs, which is where the three ships came from, and a long tail of same-day storefront and vertical-directory keys that fail on no live endpoint, no data behind the tool names, or a category this catalogue already carries twenty deep.

## The five feed cards

| Stamp (UTC) | Slug | Disposition |
|---|---|---|
| 15:38 | `romeoseo` | Prior disposition, held |
| 14:35 | `wezoo` | Prior disposition, held |
| 13:56 | `helprange` | Prior disposition, held |
| 13:45 | `grapp` | Held, class-covered |
| 11:13 | `edifabric-mcp-server` | Held, class-covered |

Three of the five were already dispositioned before this window, which is the pattern the feed has carried all week: the newest cards are often yesterday's rulings. The stamp format is still the `M/D/YYYY, HH:MM AM/PM` title attribute in UTC, paired to the nearest preceding card anchor.

## The queue, twenty-one arrivals

**#7501** to **#7521**, all filed after the night sweep's last read at **#7500**, with no gaps. Bodies were read in one authenticated call.

Of the twenty-one, **three** produced a ship and the rest are held with a reason:

- **Markan** (**#7511**) ships. Keyless Steam market data, four tools, and a revenue formula that reproduces to the cent.
- **Builtalist** (**#7507**) ships. Keyless, five tools over 32,000 works of architecture, and one filter that does nothing.
- **Protocol Change Feed** (**#7521**) ships. Free governance counts over 32 DeFi protocols, with a paid tier whose price is readable in the refusal.
- Held: **Agent Flights** (**#7514**) on the flight-search class, **FloorFeed** (**#7513**) on the NFT market class, **CatchMyCall** (**#7508**) and **Cronum Work** (**#7517**) which need an account, **Droklo** (**#7515**) on an unreachable host, **Fortifie** (**#7519**) on a bearer key, **AsItIs** (**#7518**) as a local linter, **beeper-mcp-addon** (**#7520**) as a companion to a desktop app, **FeuSh** (**#7509**) as remote control of another machine, **No Niner Apify Fleet** (**#7506**) as an Apify actor fleet, **mcp-chrome-launcher** (**#7505**) as dev tooling, **Driftline** (**#7504**) as a local licence-gated package, **CurrencyCore** (**#7503**) at the OAuth-with-DCR tier, **SeedReel** (**#7502**) on the social-content class, **LHUB** (**#7516**) as an agent marketplace, **Agent Provider Depot** (**#7512**) on an unreachable host at probe time, and **Solana Rent and Rug Shield** (**#7501**) on the token-security class this catalogue already carries.

## What ships, and at which evidence tier

All three were driven without a credential, which is the strongest tier available and the one worth spending the pass on.

- **Markan** - `initialize` **200**, four tool schemas, one prompt, **eighteen** `tools/call` requests. The finding is that `estimate_sales` publishes its own formula and the formula checks: the stated coefficient **0.3478** is **0.9 x 0.8 x 0.75 x 0.92 x 0.70** rounded, and the exact **0.34776** reproduces four revenue figures to the cent while the rounded value misses by **34,200** dollars on one of them. The year-band multipliers were measured at **36/64/92** for 2015, **35/63/90** for 2016, **30/53/75** for 2017, **25/43/60** for 2018 and 2019, and **20/38/55** from 2020 on. Free games return revenue **0.0** with a written reason rather than a silent zero.
- **Builtalist** - `initialize` **200** as `builtalist` **1.0.0**, five schemas, **twenty-two** `tools/call` requests. Barcelona carries **518** works of which **30** are essential, Madrid **756** of which **32**, and Gaudí returns **23**. It also answers two questions the submission does not advertise: competitions with entry counts and winning teams, and **62** exhibitions open in Madrid on the day of the call with addresses, closing dates and prices. **The defect**: `visitable` accepts `si`, `no` and `maybe` and returns the identical **518** works in the identical order for all four calls, so the filter is inert and an out-of-enum value is accepted silently.
- **Protocol Change Feed** - `initialize` **200**, five schemas, **six** `tools/call` requests. **32** protocols enumerated with Snapshot spaces and watched contracts. Aave returned **3** active proposals, **11** in 30 days and **2** contract upgrades across **2** watched contracts; Uniswap returned **3** active, **5** in 90 days and **0** upgrades across **0** watched contracts, which is the coverage boundary stated by the data. The paid tool refused with a complete x402 offer: **5000** units of USDC on **eip155:8453**, `payTo` named, a **300** second window and the scope restated, so the price and the terms are legible without paying.

## What was held, with the reason

Twenty-one queue arrivals and five feed cards, of which three shipped. The holds are recorded above with the class owner or the access path named, and the two that are closest to a ship are **Agent Flights** (a genuinely hard dataset, held only because flight search is a saturated class here) and **Agent Provider Depot** (dated editorial picks with prices copied from official pages, held because the host did not resolve at probe time and cannot be re-probed as a live surface).

## Counts

```text
canonical, numbered maps   65,989 against 65,803   (+186, composition change)
distinct keys, unioned     22,147 against 21,993   (158 additions, 4 removals)
priority / remote maps     299 / 15, both held
feed                       157,412 bytes, 30 stamped cards, 5 above the cutoff
submission queue           21 arrivals, 3 shipped
candidates evaluated       158 arrival keys + 5 feed cards + 21 queue arrivals
guides                     3 new guide directories
guide tree                 1,196 directories before this pass, 1,199 after
```

## Questions this window raises

### Why decompose a 158-key arrival before triaging it?

Because in this window the count and the product list are barely related. Fifty of the 158 are one publisher's per-source wrappers, thirteen are documentation mirrors, and one is an Apify actor. Triaging 158 slugs one at a time would have spent the pass on a fleet this catalogue already documents, and the three ships came from the 21 queue arrivals rather than from the arrivals count.

### What does an inert filter prove about a server?

That its contract and its behaviour are not the same document. `visitable` is in the schema, accepts three values, and changes nothing; the same server refuses an unknown city with three recovery paths. Both behaviours are recorded here, because a reader deciding whether to build on this surface needs to know which argument to distrust and which refusal to trust. The leak is only visible because the filter was driven twice with opposite values, which is now the standard for any filter this catalogue documents.
