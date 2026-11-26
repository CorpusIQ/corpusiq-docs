---
title: "MCP Server Discovery - November 25, 2026 (Evening)"
description: "A 736-key restamp with zero arrivals, one delisting and three ships: wholesale prices, a tracking checker and a four-bloc dossier cache."
category: "MCP Ecosystem"
last_updated: "2026-11-25"
---

# MCP Server Discovery - November 25, 2026 (Evening)

Fired on the **21:00 MST** tick, seventeen hours after the midday capture read the same surface and eight hours after the last build finished deploying. The directory did **not** grow in this window. It **restamped** 736 distinct listings, lost one, and the restamps are arithmetic rather than impression: every stamped key was already in the overnight baseline. The three ships came from the two-day cohort that the re-shard created, resolved through the official registry and driven end to end before a word was written.

## The window, measured

```text
mcpservers.org /sitemap.xml   17 maps named, 13 numbered server maps
raw <loc>, maps 1..13         37,695   against 37,806 at the midday read
  servers/1  ..... 4,114      servers/8  ..... 2,757
  servers/2  ..... 2,524      servers/9  ..... 2,543
  servers/3  ..... 2,944      servers/10 ..... 2,561
  servers/4  ..... 3,173      servers/11 ..... 2,484
  servers/5  ..... 3,263      servers/12 ..... 2,397
  servers/6  ..... 2,866      servers/13 .....   219
  servers/7  ..... 5,850      sum 37,695 exact
distinct keys per map         1,987 / 1,990 / 1,994 / 1,999 / 1,996 / 2,000 x7 / 219
  the 2,000 ceiling holds     servers/13 slipped 220 -> 219
union, distinct keys          24,185   (sum of the per-map distinct counts, exact)
priority-servers.xml          256 raw / 34 keys   (232 raw at the night read)
remote-mcp-servers.xml         15 raw /  1 key
union + priority              24,219
union + priority + remote     24,220
lastmod pairs, server maps    34,271   against 34,376 at the midday read
  at or after 09:06:09Z        1,098 rows collapsing to 736 distinct keys
  since the 17:00Z midday read   369 rows collapsing to 234 distinct keys
  newest stamp anywhere        2026-11-25T22:05:17Z
```

**The raw count fell by 111 and not one server arrived.** That is not a contradiction, it is the shard arithmetic again: `servers/13` slipped from 220 keys to 219 and the other twelve maps rebalanced their raw `<loc>` counts while holding their distinct key counts identical (`1,987 / 1,990 / 1,994 / 1,999 / 1,996 / 2,000 x7`). Distinct keys per map are the stable measure; raw `<loc>` entries are route variants, locale prefixes and duplicate submissions of the same slug, and they move whenever a map is rewritten.

## The 34 "arrivals" that were a baseline defect

The first diff of this pass reported **34 additions and 1 removal** against the overnight baseline. The additions were unconvincing on sight, because they were exactly the priority map:

```text
+ https://mcpservers.org/servers/ahrefs-mcp-server
+ https://mcpservers.org/servers/airtable-mcp-server
+ https://mcpservers.org/servers/github-mcp-server
+ https://mcpservers.org/servers/hubspot-mcp-server
+ ... 30 more, all in priority-servers.xml
priority-servers.xml                      256 raw / 34 distinct keys
false additions, as a set                 identical to those 34 keys
```

`github-mcp-server` is not a server that appeared this evening. It is one of the best-known entries in the ecosystem, it sits in the priority map, and the two baselines before this one both contain it:

| Baseline file | Keys | Contains `servers/github-mcp-server` |
| --- | --- | --- |
| `mcpservers_canonical_20261123_2102.txt` | 23,928 | yes |
| `mcpservers_canonical_20261124_0431.txt` | 23,928 | yes |
| `mcpservers_canonical_20261125_0431.txt` | 24,186 | **no** |

**The overnight pass wrote a baseline that lost the 34 priority-map keys, and every later diff inherited a 34-key phantom arrival.** Today's capture writes the union of the thirteen maps *and* the priority map, so the next pass starts clean. The lesson is the one this log keeps relearning in a new costume: **when a diff reports a suspiciously round cohort, check whether the cohort is a map.**

## Held, with the class named

Against the last baseline that carries the priority map (`20261123_2102`, 23,928 keys), the two-day cohort is **296 additions and 5 removals** - the re-shard's own population, most of which arrived during the November 25 03:00 pass. The five removals:

| Removed | Note |
| --- | --- |
| `whisper-sec/whisper-graph-mcp` | the only removal visible against yesterday's file too; matches `servers/13` losing exactly one key |
| `busygoat/turva-mcp` | same publisher as `erekola/turva-mcp`, which arrived in the same window; a slug move rather than a delisting |
| `naano-com-mcp`, `www-naano-xyz`, `www-orla-finance-en` | three route variants of two products, retired |

The additions were screened through the official registry before any endpoint was touched, and the holds are named by class rather than by count:

| Held | Reason |
| --- | --- |
| `apify-com-*` family, **15 entries in this window** | Apify actor wrappers on a shared Bearer token - cliqtomedia **5**, fabricablesteel **9**, plus one each from two other publishers; the class is already carried in this catalog and none is drivable from this egress |
| `yun87457-web/*` four | Apify-actor remotes with an `Authorization` header required |
| `1alexander-ai/ai-visibility-tracker` | registry `ai.1alexander/ai-visibility-tracker` requires OAuth 2.1 with dynamic registration or a `1at_` workspace key; the AI-visibility class is already carried here by geolint, LogNorm, Agitech and 1Alexander |
| `maxaeo` | both records gated (`ai.maxaeo/ai-visibility-api` wants an `Authorization` header, the npm package is local-first); same class |
| `quantisnow/sec-edgar-mcp` | registry **1.0.8**, remote `https://www.quantisnow.com/api/v1/mcp`, keyless per the record, but Cloudflare answers **403** to this egress; npm package `quantisnow` exists for a local stdio drive, which is the next pass's job |
| `retailvest/engine`, `opentickers`, `sortance`, `linkedmcp`, `postrippl`, `seocrawlermcp`, `expiryregister` | all initialize into an in-band **401** naming the credential path; OAuth or API-key grant required |
| `mambalabsdev` five, `yangzhenruan` seven, `mpp-*` eleven, `fmf-x402-workers-dev` family | repeat publisher fleets already held as classes in earlier passes; one endpoint per fleet is the rule before any are dispositioned |
| `chinaindustryintel` | **keyless and drivable, but the catalogue holds 3 articles and 2 companies** per its own `search_articles` payload, so a query for "battery" returns `total: 0`; a stub surface is not a guide |
| `geoseeer` | PyPI package only, local stdio, image geolocation; no remote surface to measure |
| `suppliers-net` sibling `nameideahub` | keyless, two tools, 3,000 surname records; real but no operator use case in this catalog |

## The three ships

All three are keyless, all three were driven on this pass, and each one carries a defect that the guide records rather than smooths.

**[Suppliers Net MCP - Wholesale Prices With the Seller and the Date](/hermes/mcp/servers/external/suppliers-net/)** has no gate at all: `initialize` **200** and a **4-tool** `tools/list` at `https://suppliers.net/mcp` (registry `io.github.Dragoonhawx/suppliers-net` **1.0.0**). The catalogue states itself as **24,681** current advertised prices from **427** sellers across **804** suppliers in eight states summing exactly (`266 + 222 + 156 + 74 + 56 + 15 + 10 + 5`). Twelve priced rows were driven on a beef query and the unit arithmetic reproduces on all twelve (`$7.09 / 5 kg = $1.418/kg`, `$11.50 / 3 kg = $3.8333/kg`, `$5.60 / 1.05 kg = $5.3333/kg`), ordered cheapest per kilo first across mixed pack sizes with the seller, the source URL and the `date_seen` on every row. Three refusals were measured and each names its own limit: `market_rates` returns `count: 0` until three verified suppliers list the same product, a nonsense query returns *"Suppliers Net does not guess a price"*, and a bogus category fails closed at `total: 0`. **One defect recorded:** `category` is matched against product text rather than the seller's category field, so `category: "Meat"` in NSW returns Claudio's Seafoods on the strength of *MUSSEL MEAT* and *Prawn Meat*, and `category: "Seafood"` returns a Pantry supplier, out of a 266-supplier state.

**[Qonvert MCP - Tracking Parameters Checked After Consent](/hermes/mcp/servers/external/qonvert-mcp/)** is the discovery-open tier split cleanly in two. An **18-tool** `tools/list` arrives without a key (registry `ai.qonvert/qonvert` **1.0.1**), and three of the eighteen run without an account: the tracking check, the connect guide and the free placement guidance. `check_marketing_tracking_url` names exactly which of the three core UTM parameters are missing from a supplied URL and reports click identifiers in a separate field, with the note that *"a missing identifier in this sample is not evidence of a tracking gap"* because the ad platform adds it at click time. The other fifteen need an OAuth grant and refuse in band, `get_project` returning **401** with *"Create a Qonvert account or sign in to connect your project and its sources."* **Three defects recorded:** `tools/list` answers **400** to a client pinning protocol `2025-06-18` and **200** to `2025-11-25`, which reads as a broken server rather than a version mismatch; `get_marketing_setup_guide` returns *"Invalid tool or arguments."* on **five of five** attempts including inputs built from its own schema, so a listed tool cannot succeed; and the free-guidance enums are `market: [ru, global]` and `goal: [visibility, feedback, discovery]`, so a US campaign falls outside the tool's scope and gets an empty list.

**[Prismintel MCP - Four-Bloc Triage of Cached Geopolitical Dossiers](/hermes/mcp/servers/external/prismintel-mcp/)** is a **two-tool** keyless read of a cache (registry `app.prismintel/triage` **1.0.0**) whose own instructions say *"Read-only, zero-cost access to cached PRISMINTEL multi-bloc dossiers."* One **51-source** dossier at a **68%** consensus index returned a three-part BLUF plus a bloc split of **39 / 29 / 20 / 12%** with tone scores **-15 / -10 / -55 / +5** and the omission each bloc makes, summing to 100. **The finding is freshness and it is arithmetic:** all **nine** theaters carried `is_expired: true` and `freshness: "archive"` at read time, the newest compiled **11.5 hours** earlier and the oldest **56.5 hours** earlier, while the same payload reported `status: CACHED_DOSSIER_AVAILABLE` - an agent branching on `status` presents a 30-hour-old analysis as current. Two further defects: the Hormuz dossier occupies two rows under one title (**68%** and **62%**, seventeen minutes apart), and `corpusSnapshotHash` is **16 hex characters** where a SHA-256 has 64. A restraint paragraph is the best thing in the payload: the dossier states what its evidence does *not* establish, in the same object as the claim.

## The push surfaces

**mcp.so** answered `/feed` **200** at **160,800** bytes with **43** `/servers/` links collapsing to **36** distinct slugs and **30** distinct stamps. The reader in this catalog was pointing at the singular `/server/<slug>` route and returned **zero** against a document that carries none of it; the plural pattern returns 36 distinct, which is the midday figure to the slug, so the feed kept its shape and the reader was wrong. Four cards sit above the previous top: **`print-pronto-data`**, **`teledirectmd-0266ca`** (10:01 PM), **`atono-d236de`** (09:08 PM) and **`zooop`** (08:54 PM), then **`urml`** at 11:00 AM as the oldest of the new group. None was drivable without a registry record. The `/submit` queue returned **200** at **61,042** bytes and **zero** `#NNNN` filing ids: the page is now an application shell with **298** hashed chunks, so the queue numbering that earlier passes read is no longer in the document and the queue is not a signal until a JSON route is found for it. The homepage carried no `slug` or `createdAt` payload for the same reason.

## Listings, re-measured

- **mcp.so**: `/servers/corpusiq-docs` → **200**, **857,169** bytes, **175** occurrences of `corpusiq`. The singular guesses stay **404** (`/servers/corpusiq` → 404, 23,986 bytes), which is the recorded shape and not a delisting.
- **mcpservers.org**: `/servers/corpusiq-io` → **403**, and the body is the Cloudflare interstitial, not a 404. Detail routes are edge-blocked by policy; our own mirror carries a fresh stamp in this capture.
- **Official registry**: the ships resolved through `registry.modelcontextprotocol.io`, which is now the fastest route from a slug to a real endpoint and its auth requirements, and the reason three candidates this pass could be dispositioned without opening a vendor page.

## What the pass says about the platform

Two movements and no arrivals is the honest reading. The directory restamped **736** distinct listings in seventeen hours and added none, one listing was retired, and the only cohort that produced anything drivable was the two-day population from the re-shard. **A stamp is a touch, not a birth:** 1,098 rows moved onto 736 keys that were all present in the baseline overnight, and the previous pass made the same measurement with a different cohort. The pattern to keep is the one that caught the 34 phantoms - **when a diff reports a round cohort, ask which map it came from** - because the alternative is a catalog that congratulates itself every evening on servers it documented in September.
