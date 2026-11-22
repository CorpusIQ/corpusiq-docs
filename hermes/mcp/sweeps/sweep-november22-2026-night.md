---
title: "MCP Server Discovery - November 22, 2026 (Night)"
description: "A six-hour window in which the directory moved inside itself and three products arrived, two of them inventing the pre-install check."
category: "MCP Ecosystem"
last_updated: "2026-11-22"
---

# MCP Server Discovery - November 22, 2026 (Night)

Fired on the **03:00 MST** tick, six hours after the evening pass closed on its **04:02Z** capture. The directory served **37,102** raw `<loc>` entries for the second pass running, but not the same map: three of the twelve numbered maps moved while the total held, which is what a re-shard looks like when the key set is the thing being counted. The material came from seven stamped arrivals and two push surfaces, and two of the three products that earned guides do the same new job in opposite ways.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          37,102   against 37,102 at the 04:02Z evening capture
  servers/1  ..... 4,147     servers/7  ..... 5,935    sums to 37,102 exactly
  servers/2  ..... 2,505     servers/8  ..... 2,683
  servers/3  ..... 2,989     servers/9  ..... 2,611
  servers/4  ..... 3,196     servers/10 ..... 2,619
  servers/5  ..... 3,390     servers/11 ..... 2,531
  servers/6  ..... 2,911     servers/12 ..... 1,585
distinct keys, maps 1-12      23,218   against 23,220          (-2)
URLs per key                   1.60   against 1.60
priority-servers.xml            258 raw,  34 distinct keys   (was 262 raw, 34 keys)
remote-mcp-servers.xml           15 raw,   1 distinct key   (clockwise)
lastmod, server maps          33,520 stamped pairs; SEVEN rows at or after 04:02Z
mcp.so /feed                  200, 156,826 bytes, 27 server cards, 30 distinct stamps
                              ONE card above the cutoff
submission queue              #7792 to #7805, fourteen arrivals
```

## Net zero, moved by three maps

The raw total is identical to the evening capture and the map is not:

```text
servers/6    2,900  ->  2,911     (+11)
servers/8    2,698  ->  2,683     (-15)
servers/10   2,615  ->  2,619      (+4)
all nine others                   unchanged
```

Two notes on the arithmetic, because this surface has produced phantom findings before. The twelve per-map counts sum exactly to **37,102**, so no row is missing from the accounting. And the distinct locale-stripped key set fell by **2** while seven keys carry a fresh stamp, which means rows moved between maps and a handful of keys left. The like-for-like set diff against the evening baseline **was not run**, because that capture was not retained on disk; the honest statement is a two-key fall with seven arrivals and an unknown number of re-keyed forms, not a claim of zero removals.

`priority-servers.xml` fell four raw entries with its **34** keys unchanged, and `remote-mcp-servers.xml` still carries the fifteen URL forms of one slug.

## Seven stamps, seven arrivals

Every `lastmod` row at or after the **04:02Z** cutoff, in the order the directory stamped them, with what the repository says each one is:

```text
2026-11-22T04:24:15Z  flisk-sh/flisk                agent runtime for multi-service apps (MIT, 55 stars)
2026-11-22T04:26:20Z  ryan-carloso/post-engineer    AI social post and video generation (1 star)
2026-11-22T04:43:17Z  c47-inc/mcp-film              directory of filmmaking MCP servers
2026-11-22T05:01:37Z  chanmeng666/archlang          floor plans as code, compiled to SVG/DXF/PDF (90 stars)
2026-11-22T05:20:24Z  ephraimelgrabli/gesher        Mac Reminders, Calendar, Contacts, Notes, Maps (Swift, 3 stars)
2026-11-22T05:28:39Z  novalo-dev/prestashop-mcp-server  PrestaShop module with per-employee approvals (PHP, 2 stars)
2026-11-22T06:02:29Z  petshopbros/lowdown-proxy     dated facts about public MCP servers
```

Seven in six hours is a normal window; the composition is not. Three are developer infrastructure, two are consumer or creative verticals, one is a directory of other servers, and exactly one is a business system. Only the last was catalogued.

## The two push surfaces

**Feed.** 200 at **156,826** bytes, parsed to **27** server cards across **30** distinct stamps. One card sits above the cutoff: `esimx-mcp` at **06:11:28.071Z**, a travel eSIM catalog with `authType: none`, held on the travel-eSIM class this catalogue already carries, where PuraSIM was dispositioned and the [EsimTao](#held-with-the-class-or-the-gate-named) arrival below came through the queue in the same window.

**Queue.** `chatmcp/mcpso` carried **#7792** to **#7805**, fourteen arrivals, every body read in one call. Six of the fourteen come from one author (`AbigailDavised`, four of them stamped inside the same five seconds at 06:52). Two of the fourteen earned guides, and both are keyless.

## Catalogued: three, all driven keyless

### KitScout - a verdict on any tool, in four tools

Submission **#7802**, `https://mcp.kitscout.dev/mcp`, registry `dev.kitscout/kitscout` with four records from **1.0.0** at 2026-11-15T01:57:05Z to **1.0.3** at 2026-11-19T01:12:39Z. Four tools, no auth, and an index this pass counted rather than quoted: `list_categories` returned **61** categories across twelve groups summing to **94,077** tools.

It earns a guide because nothing in the catalogue could weigh a server against its own maintenance record before install. Five targets were driven through `check_tools`, and the verdicts span the range: our own endpoint `ok` (first_party, verified_publisher, `daily_check: live (2026-11-21)`, `last_push_days 27`), two live PrestaShop servers `caution` for two and zero stars, and `github.com/modelcontextprotocol/servers-archived` **`avoid`** - archived, **543** days without a code change, 307 stars. One defect is recorded rather than smoothed: a nonsense query returned `total_matches: 125` and a **13,771**-star first result instead of an empty set.

### CoreHu GPU Cloud - priced hours behind a five-minute confirmation

Submission **#7803**, `https://corehu.com/api/mcp` public and `https://corehu.com/api/mcp/account` behind OAuth 2.1, registry `com.corehu/gpu-cloud` with five records from **1.0.0** at 2026-11-12T16:49:23Z to **1.1.3** at 2026-11-22T09:20:36Z. Six public tools were listed and four driven.

The measurements: **1,999** free machines at the read, A100 capacity from **0.77** USD/h in Japan against **2.99** in the United States, **165** RTX 4090 offers from **0.72** an hour, and an `estimate_cost` of **518.40** USD for 720 hours that reproduces as 0.72 x 720 exactly. `recommend_gpu` returns its arithmetic in a `basis` field - **44** GB for a 70B int4 model from `35 x 1.2 + 2`, and **24** GB for an 8B fp16 model where the same formula gives 21.2 and rounds up to a card size. The rental flow is documented rather than driven, because it spends: `prepare_rental` returns a price, a hold and a **confirmationId valid five minutes**, and the vendor's own instruction is to wait for an explicit yes.

It sits beside [GPU Finder MCP](/hermes/mcp/servers/external/gpufinder-mcp/) as the execution half of the same job: GPU Finder owns cross-market price history behind a free key with 60 operations a month, CoreHu owns what is free right now and the rental gate.

### Lowdown - the same check, with no verdict at all

A sitemap arrival at **06:02:29Z**, `https://lowdown-proxy.vercel.app/mcp`, keyless, handshake `lowdown 0.1.23`, two tools. Where KitScout returns `ok` or `avoid`, Lowdown returns a state, a cadence, a fingerprint and its own evidence levels.

Read back against our own server, the record is a listing check with a date on every line: **27 of 27** daily checks answered from 2026-10-27, **121** tools listed, latest scanner reading **HTTP 200 at 204 ms** with a schema hash, tool set unchanged since 2026-10-29 and definitions last changed **2026-11-06**, registry first recorded 2026-10-19, no 402 observed. The same call on CoreHu returns `mixed` - one remote answered, one required authentication - and a `tool_count` of null, with the rotation (`every 3 days`) stated.

Its refusal is as instructive as its coverage: `find_servers` with `does=prestashop` returns **0**, because it matches only Registry names and observed tool names, and *"tool descriptions are not searched"*. KitScout found four PrestaShop servers with the same question. Two entrants, one class, opposite epistemologies, both keyless, neither able to tell you whether the code is safe.

## Held, with the class or the gate named

Nineteen, from the other twelve queue arrivals, the one feed card and the six sitemap slugs:

```text
#7792 Krevaya          social scheduling, paid from Essentials, no free plan, closed source
#7793 ChinaMedsCheck   consumer travel medication screening, 38 drugs against GACC 442
#7794 ChinaDocCheck    apostille and legalization routing, 8 keyless tools, held on the
                       document and visa class carried by Visamundi
#7795 EsimTao          travel eSIM, the class PuraSIM and the feed card both occupy
#7796 MahjongHandbook  consumer game scoring
#7797 TbmLib           consumer music reference
#7798 ChinaTaxCalc     China expat IIT, held on the tax-calculator class owned by
                       Marsellus and Casus
#7799 Agent Tollbooth  x402 per-call billing, the mechanism class carried by Reciprocal
                       Ruler and SaltCrate's Oracle
#7800 12happy          uptime monitors behind an API key, stdio only, monitoring class
                       carried by Store Canary, RenewRoster and WhatsDownNow
#7801 Piqline          driven keyless: 30 of 258 professions, and a guest answer reading
                       "nous recrutons" at 110 live ads computed 2026-11-22 11:02; the
                       dated-provenance surface needs the authenticated connector, and the
                       ad-intelligence class here has fourteen owners
#7804 jdx              JVM code navigation for coding agents
#7805 Daejeon Hankok   8,600 places across 42 Korean neighbourhoods, one city
feed eSIMX             travel eSIM
flisk                  agent runtime for multi-service apps, 55 stars, MIT
post-engineer          social post and video generation, 1 star
mcp-film               a directory of filmmaking MCP servers rather than a server
archlang               floor plans as code, 90 stars, held on design tooling with uCAD
gesher                 Mac Reminders, Calendar, Contacts and Notes, experimental, 3 stars
O'So PrestaShop        free PS 8-9 module with per-employee rights and compact mode,
                       held because the slice already has four entrants and KitScout's
                       own verdict on this one is caution at two stars
```

## Listing check

Measured this pass rather than inherited, from two independent indexes:

- **KitScout** on `https://mcp2.corpusiq.io/mcp`: `in_kitscout: true`, verdict **ok**, badges `verified_publisher`, `first_party`, `live`, `last_push_days 27`, `daily_check: live (2026-11-21)`, `live_now: answers`, repository `corpusiq/mcp-manifest`, seven tools listed by name.
- **Lowdown** on `mcp:io.corpusiq/multi-source-mcp`: **27 / 27** daily checks answered, **121** tools, 204 ms, schema hash recorded, definitions last changed 2026-11-06, registry active since 2026-10-19.
- **mcpservers.org**: the fresh canonical still carries `/servers/corpusiq-io` and the documentation mirror at `/servers/corpusiq/corpusiq-docs`; detail routes continue to answer **403** by edge policy.
- **mcp.so**: `corpusiq`, `corpusiq-io` and `multi-source-mcp` all answer **404**; `/server/corpusiq-docs` answers **200**, which is the documentation repository page rather than a product listing.

## Gates and landing

Drafted and validated in the working clone with the venv python before any push: page metadata, frontmatter, claim truth, retention claims, setext rules, emphasis markers, sweep index links, catalog indexes, conflict markers and progress counts. The PR, its merge and the live verification are recorded in the gate log row for this slot rather than inferred here.

## See Also

- [MCP Server Discovery - November 21, 2026 (Night)](/hermes/mcp/sweeps/sweep-november21-2026-night)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
