---
title: "MCP Server Discovery - November 26, 2026 (Midday)"
description: "A 309-slug ingestion wave in nineteen hours, three first-of-class ships and a consumer-spend panel that only speaks behind a sign-in."
category: "MCP Ecosystem"
last_updated: "2026-11-26"
---

# MCP Server Discovery - November 26, 2026 (Midday)

Fired on the **10:00 MST** tick into a directory that had been byte-stable for the night pass and then took the largest single wave this log has recorded in weeks: **309 new slugs in nineteen hours**, every one of them carrying a fresh `lastmod` stamp, against **534 restamps** of entries already held. The wave is mostly vendor pages rather than products, so the ships came from the queue and from the registry instead. Three are first of their class here, and the fourth is the first consumer-spending panel in the catalog, documented from its own specification because its endpoint does not answer without a sign-in.

## The window, measured

```text
mcpservers.org /sitemap.xml   17 maps named, 13 numbered server maps
raw <loc>, maps 1..13         38,150   against 37,695 at the 10:09Z night capture
  servers/1  ..... 4,115      servers/8  ..... 2,720
  servers/2  ..... 2,524      servers/9  ..... 2,559
  servers/3  ..... 2,950      servers/10 ..... 2,537
  servers/4  ..... 3,177      servers/11 ..... 2,511
  servers/5  ..... 3,319      servers/12 ..... 2,419
  servers/6  ..... 2,886      servers/13 .....   528
  servers/7  ..... 5,905      sum ............ 38,150 exact
distinct keys per map        1,987 / 1,990 / 1,994 / 1,999 / 1,996 / 2,000 x7 / 528
server-map distinct slugs    24,494   against 24,186 at the November 25 10:00 MST capture
priority-servers.xml         251 raw / 34 keys
remote-mcp-servers.xml        15 raw, site-level URLs that key to no slug
union of keyed slugs         24,528
```

The rise is not a shard shuffle. Diffing the key set against the stored November 25 midday capture gives **309 additions and 1 removal** (`whisper-sec/whisper-graph-mcp`), and the removal count is a single name, not a cohort leaving. `servers/13`, the shard that appeared at 220 entries on November 25, has grown to **528 entries and 528 distinct slugs**, which is a new shard filling rather than a re-shard.

## The stamps agree with the key delta, to the slug

That agreement is the proof this pass rests on. The server maps carry **34,651 `lastmod` pairs**, of which **1,262 rows fall at or after the night capture's newest stamp of `2026-11-25T22:05:17Z`**, collapsing to **843 distinct slugs**. Splitting those 843:

- **309 are the new arrivals**, exactly the key-set addition count.
- **534 are restamps** of entries already held, with the tell this log has recorded before: `awslabs/bedrock-kb-retrieval-mcp-server`, `browserstack/mcp-server`, `cycodehq/cycode-cli` and `Mastra/mcp-docs-server` each stamped **15 times** inside the same second.

Newest stamp anywhere in the capture: **`2026-11-26T10:55:14Z`**. So a window that looks like a shard drift in the raw count is a genuine ingestion wave, and the two independent measurements, stamps and key identity, land on the same 309.

## What the 309 actually are

This is a vendor-page wave, not a product wave, and the decomposition is the whole triage:

| Class | Count | Disposition |
| --- | --- | --- |
| Domain-form vendor pages with no repository | 214 | documentation and marketing surfaces, not products |
| Namespaced repositories | 95 | the only class worth probing, and mostly fleets |
| Pages whose slug carries docs, help, connect, blog or getting-started | 47 | documentation mirrors, no tool surface of their own |
| `rowhousesoftware` (auction and estate-sale software) | 18 | one publisher fleet, one product, held as a fleet |
| `dragonincjp-droid` compliance auditors | 5 | one publisher fleet of EU and US regulatory auditors, held as a class |
| `apify-com-cliqtomedia` actors | 5 | Apify actor distribution, the standing hold class |
| `mambalabsdev` actor wrappers | 5 | the standing fleet hold, already dispositioned in earlier passes |
| `iisakovbusiness-wq` German e-invoicing trio | 3 | DATEV, eRechnung and BMF, class carried by NormAPI and BeeL |

Nothing in the fleet classes was probed twice: the Apify and mambalabsdev classes are recorded holds, and the rowhousesoftware set is a single publisher whose items are print packs, ledgers and games for estate-sale operators rather than a business-data surface.

## The feed rotated two cards

`mcp.so /feed` answered **200** at **160,433 bytes**, 36 distinct slug anchors and 30 stamps, with **two cards in and two out** against the night capture:

- **In:** `wayvz-sms` stamped 11/26/2026 01:48 PM UTC (SMS delivery checks and sending across the Middle East and Africa, 401 with a `resource_metadata` challenge at `api.wayvzgroup.com/mcp`), and `cheso` stamped 11/26/2026 10:57 AM UTC (presentations, posters and video generation, OAuth, media and design).
- **Out:** `persado-mcp` and `1alexander-ai-visibility-tracker`, both already dispositioned by earlier passes, so the rotation is page movement and not a delisting.

Neither arrival was catalogued. `wayvz-sms` lands on the SMS and telecom class already carried by Mobile Text Alerts and the business-telephony entries, and `cheso` lands on media generation. The stamp format recorded on the night pass held: no seconds in the `title` attribute and `Submitted N hours ago` as the text, so a reader keyed on the older seconds form returns zero cards against a document carrying 30.

## The queue, forty filings

The chatmcp submission queue carried **#8141 to #8180**, forty filings from 09:15Z to 16:58Z, read with bodies in one authenticated call. Four are worth naming because they arrive with real data behind them:

- **#8157 ShelfXray** (`in.shelfxray/shelf-data`), quick-commerce shelf reads for Blinkit, Zepto and Swiggy Instamart. **Shipped.**
- **#8179 Leadgen ONRC Romania** (`com.adrianhomelab/leadgen-onrc`), the Romanian company registry with filings, VIES and public contracts. **Shipped.**
- **#8172 vigialegal.mx**, Mexican SAT 69-B, article 69 and the REPSE padrón, keyless with five Spanish-language tools, and a real country slot to fill on the supplier-compliance shelf. **Held** for the next pass: it is the strongest arrival of the window after the two ships and it deserves a driven guide rather than a paragraph.
- **#8171 Frostmailer**, domain deliverability scoring across six tools, and **#8170 StoreInspect**, Shopify store search, held on the delivery and store-directory classes these guides already carry.

The four filings at 09:29Z inside four seconds, `Svanja`, `VIPOutreach`, `Unspar` and `Chab`, are one publisher batch and were dispositioned as one line.

## Shipped: three with guides

**SEA Cold Chain** (`com.seacoldchain/markets`, keyless, 3 tools, all driven) is the first cold-chain capacity source in this catalog. Seven Southeast Asian markets, pallet positions printed as a floor, and two different shares that a summary must not conflate: Thailand reads `stated_share_pct` 42 against `coverage_pct` 81, and the guide prints both with what each measures. Vietnam 166 operating sites and 1,457,000 pallet positions at 98 percent coverage, Thailand 551 sites and 1,487,000 at 81 percent, Indonesia 515,000 at 21 percent. Lao PDR is formally `not_published` because a market under three sites would identify the buildings.

**ShelfXray** (`in.shelfxray/shelf-data`, keyless, 5 tools, all driven) brings quick-commerce shelf share to the catalog for the first time: brand ranks, store coverage, sponsored placements and price bands across three Indian platforms and two cities, under CC BY 4.0, cached to 2026-08-01 and honest about it on every response. Sleepy Owl in Bengaluru averages 98.17 percent coverage across six searches, and 25 of its 37 sponsored slots sit in one Zepto instant-coffee search. The Coffee benchmark in Delhi NCR puts Instamart at a median of 252 rupees with 643 sponsored slots among the top eight brands, against Zepto at 99 rupees with 176, and one cell, Zepto's 2.16-rupee minimum, does not survive a sanity check and is flagged rather than explained.

**Leadgen ONRC** (`com.adrianhomelab/leadgen-onrc`, keyless, 21 tools, seven driven) is the first Romanian registry surface here and the first that ties registry, filing, VIES and public procurement to one CUI. Dedeman SRL, CUI 2816464, returns fiscal 2025 revenue of 13,157,835,535 RON and 12,702 employees, which is 1,035,886.91 RON a head and a 12.429 percent net margin by hand, plus a VIES check with `nameMismatch: false` and three SEAP contracts totalling 18,377,193 RON where TRANSGAZ alone is 98.96 percent of the priced value. Two tools return empty payloads on a valid CUI and both are recorded as defects.

## Documented, not driven: the first consumer-spend panel

**American Spend** (`com.americanspend/insights`) refuses every unauthenticated call with a proper OAuth challenge, so the guide is written from the vendor's specification and says so. The endpoint is the first card-spending panel in this catalog: **2 billion transactions a month**, **$1.2 trillion** of annual consumer spend tracked, **150 million or more** monthly active accounts and **1 million** merchant locations, with BLS, Census, BEA and OECD series exposed beside the model for comparison. The chain verified live: a **401** carrying `resource_metadata` on the `/mcp` suffix, the protected-resource document **200** with identity scopes only, the authorization-server metadata **200** with `authorization_code`, `refresh_token` and PKCE **S256**. Twenty-three methods are documented across six groups, the free tier is 2,500 credits a month with no card, Pro is **$100 a month or $1,000 a year**, and ChatGPT is documented as coming soon rather than available.

## Also identified this pass (not catalogued)

- **CoreLoop directory** (`so.coreloop/directory`), keyless with seven tools, and its `search_businesses` returns an empty list for `coffee roaster`, `coffee` and `dentist` while the schema's `query` parameter is what those calls used. An undocumented `q` alias found one business, CoreLoop itself. Held as a directory with a broken primary filter rather than catalogued.
- **DemiSignal**, keyless DNS grading for DMARC, SPF, DKIM, BIMI and MTA-STS, three tools, and a genuinely current finding on our own domain: it flags `pct=25` in our DMARC record against **RFC 9989**, which no longer defines `pct`. Held because the email-authentication class is owned here by Powerdmarc and the deliverability entries.
- **Frostmailer** and **DemiSignal** duplicate each other on domain grading, which is why the class hold covers both.
- **justtranscribe** (401, API key plus vendor account), **cituna** (**-32001**, AI-visibility class saturated by geolint, LogNorm, SEOforGPT, OperStack and 1Alexander), **storeinspect** (401 with no `WWW-Authenticate`), **stellaframe** (401 plus `resource_metadata`, widget class), **viaondo** (401, travel-agency drafts), **svanja** (401, freelancer mail), **enterplace** (registry record with no remote), **treant** (self-hosted graph memory, no remote).
- The **DutyKit** keyless probe was re-run as a control and confirms the catalogued entry: seven tools, obligations for DE, LU and EU with 18 sources unchanged, and a live VIES check. A useful note for its guide: the argument names are German (`land`, `ust_id`, `rechnung`), so an English-language caller gets a pydantic validation error rather than a guess.
- **ShelfXray, SeaColdChain and Leadgen** were all reached from the queue or the registry rather than from `/all`, which has been refused at the edge since 4 November.

## Listings, re-measured

- **mcpservers.org:** LISTED. Both entries answer **200** directly today, `/servers/corpusiq-io` at 75,180 bytes with 55 mentions and `/servers/corpusiq/corpusiq-docs` at 93,203 bytes with 146, so the edge interstitial recorded in earlier passes is gone for this route.
- **mcp.so:** LISTED. `/servers/corpusiq-docs` answers **200** at **856,532** bytes with **175** corpusiq mentions.
- **Glama:** LISTED. The connector route answers **200** at 732,001 bytes with **596** mentions.
- **Smithery:** the registry API answered **500** `An unexpected error occurred` on the first attempt, the standing provider fault since November 23. No delisting is inferred from a provider error, and the direct record route was not re-read this pass.
- **Official registry:** `io.corpusiq/multi-source-mcp` carries four versions with **1.0.3** newest, all pointing at `https://mcp2.corpusiq.io/mcp`.
- **Anthropic directory:** `anthropic_directory_watch.py` exited **0** after scanning **1,227** pages across three surfaces with **0** hits, so nothing changed this pass and no listing is asserted here; the review state lives only in the vendor portal.

No submission was made this pass because nothing was unlisted.

## What the pass says about the platform

A 309-slug wave in nineteen hours with a stamp set that matches the key delta to the slug is the healthiest signal this log has carried in two weeks: the directory is ingesting again, and the ingestion is measurable. What it ingests, though, is mostly vendor pages, which is why a pass that finds 309 slugs can honestly ship three products and document a fourth. The rule that keeps this useful is unchanged: a slug is not a product until something answers, and the two best arrivals of the window came from the queue, not the wave.
