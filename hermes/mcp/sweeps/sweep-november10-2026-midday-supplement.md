---
title: "MCP Server Discovery - November 10, 2026 (Midday Supplement)"
description: "A flat canonical with 39 queue arrivals and two feed cards, where the two entries that earned guides price a truckload and a fertilizer bag"
category: MCP Ecosystem
added: 2026-11-10
last_updated: 2026-11-10
source: "the mcpservers.org sitemap index and its fifteen named maps (77,245 raw loc entries, 20,396 distinct server URLs after locale stripping), the mcp.so feed read cache-busted, the chatmcp/mcpso submission window #7061 to #7099, and the official MCP registry for candidate resolution"
tags: ["mcp server", "model context protocol", "discovery", "sweep", "november 2026"]
---

# MCP Server Discovery - November 10, 2026 (Midday Supplement)

Fired on the **11:00 MST** tick, one hour after the 10:00 MST midday pass and eight hours after the night sweep. The 10:00 pass shipped nothing, so this supplement owns only the delta: a submission that arrived after that window closed, and one feed card re-examined by driving it. The canonical came back set identical, the submission queue carried **39** arrivals, and the feed carried **two** cards. Both entries catalogued come from the two ends of the same idea: a price that is attached to a delivery address, once for a truckload of stone in Florida and once for a bag of DAP in a Kenyan county.

```text
Surfaces:    15 maps named by the index, 77,245 raw <loc> entries,
             43,433 locale prefixes stripped, 20,396 distinct server URLs
             (20,396 at the 04:32 MST night capture: 0 additions, 0 removals)
Feed:        144,738 bytes cache-busted, 30 cards, 2 above the night cutoff
Queue:       #7061 to #7099, 39 issues, no gaps, all arrivals
Catalogued:  2 servers, 2 guides
Crossref:    41 candidates, every hold given an owner or a reason
```

## The window, measured

The sitemap index answered **200** and now names **fifteen** maps rather than the thirteen the night pass read: `static.xml` with **822** entries, `priority-servers.xml` with **299**, `servers/1.xml` through `11.xml`, a `skills.xml` map with **12,579**, and `remote-mcp-servers.xml` with **15**. The skills map is new to the index and is not a server map, so the `/servers/` subset excludes it by construction and the canonical is unaffected by its arrival.

```text
servers/1.xml   7,588    servers/5.xml   6,952    servers/9.xml    4,031
servers/2.xml   5,948    servers/6.xml   6,756    servers/10.xml   2,603
servers/3.xml   6,518    servers/7.xml   9,351    servers/11.xml     451
servers/4.xml   6,744    servers/8.xml   6,588
priority-servers.xml  299      remote-mcp-servers.xml  15      static.xml  822
skills.xml         12,579  (excluded, not a server map)
```

**77,245** raw `<loc>` entries, **43,433** inline locale prefixes stripped before the subset was taken, **20,396** distinct server URLs. The night capture on disk holds **20,396** lines, so the set diff is **0 additions and 0 removals** once three slugs the baseline carried in `%23` fragment form are normalized to their `#` form (`ahmedkhaleel2004/gitdiagram`, `orcasecurity/orca-skills`, `podop29/shotpipe-mcp`); without that normalization the diff reports three phantom pairs, which is the encoding artifact this catalog has recorded before rather than a wave.

`mcpservers.org /all` answered **403** by edge policy, the standing condition since November 4, so the sitemap union carried the window alone.

The mcp.so feed was read twice, **144,705** bytes plain and **144,738** cache-busted, **30** cards parsed with the same set on both reads. Two cards sit above the night cutoff of `2026-11-10T06:46Z`, and both are today: `wegravel` at **14:05Z** and an `/agents/` card for `ez-image-to-image` at **12:16Z**. Timestamps are UTC inside the `title` attribute, so a run whose clock reads 11:00 MST is comparing against cards dated seven hours later than they look.

The submission queue carried **39** numbers from **#7061** to **#7099** with no gaps, every one an arrival. That is the largest single window since the November 8 wave, and it is dominated by two cohorts rather than by variety: a **Marcoco27** regulatory-deadline family of five, and a **mambalabsdev** Apify-actor fleet of five.

## The pass this one supplements

The 10:00 MST tick ran the midday sweep and left its record in the startup gate log as `T-NOV10-MCPDIR-1000`: the same canonical refresh from `/sitemap.xml` returning fifteen maps, **77,245** raw loc entries and **20,396** distinct server URLs set identical to the 04:32 MST baseline, `/all` at 403, the feed at **144,745** bytes with **2** cards above the `06:46Z` cutoff, and the submission window **#7061** to **#7084**, **24** arrivals, every one held with a class owner named. It shipped **0** guides, appended **0** stamps and made **0** commits, which is why the slot has no page of its own and why this one is a supplement rather than a midday report.

Two things were left open by that pass and are closed here. NuaSense (**#7089**) was filed at **17:21Z**, after that window closed, so it was never in front of it. And `wegravel` was held as one of the two feed cards with no reason recorded, so it was re-examined here rather than inherited: the endpoint was driven through all four of its tools, the arithmetic below is what came back, and the reversal of that hold is stated in the catalog index as well as in this page. A hold with no recorded reason is not a disposition, which is the same ruling this catalog applied on October 22 when a hold taken on a tool count was re-tested and shipped.

## Catalogued: two prices, two addresses

**NuaSense** is the first server here that describes the market around a farm rather than the farm itself. A keyless initialize answered **401** carrying a JSON-RPC error object (`-32001`), the protected-resource document names three scopes, `market:read`, `farm:read` and `alerts:write`, and the authorization-server metadata publishes a registration endpoint, so an MCP client can onboard itself while the account behind it still needs a verified phone. What makes it a guide rather than a hold is one refusal in its documentation: the soil-baseline dataset ships without pH, organic carbon or N, P and K because modelled values cannot support a fertilizer decision. In a product whose job is telling an operator what an input costs, publishing nothing where a guess would be plausible is the same instinct this catalog keeps rewarding.

**WeGravel** was driven end to end, seven calls across four tools, all keyless. `list_materials` returned its catalogue with slugs and selling units, `calculate_quantity` turned a 30 by 20 foot area at 4 inches into 7.41 cubic yards, 10 tons and an **orderQuantity of 13** with a declared 25 percent safety margin, and `get_prices` priced 7.4 cubic yards of crushed stone at ZIP 33139 at **$1,081.07**, against a full truck of 16.8 cubic yards at **$1,921.75**, which is $114.39 per cubic yard rather than $146.09. The server states that gap itself, in a note, and the gap is the operator insight: at the smaller order the truck is 27 percent of the unit price. `compare_prices` returned the same lens across materials, cheapest first, each row carrying a quote URL with the ZIP, material and quantity already in it, and a ZIP outside Florida returned `UnsupportedZipError` with the state code in the cause.

Records of the pass rather than claims: the `wegravel` hold from the 10:00 MST window is reversed on the measurement above, and that reversal is written into the catalog index entry as a class note so a later pass does not read the hold and the guide as a contradiction. Guides: [NuaSense MCP - East African Farm and Market Data](/hermes/mcp/servers/external/nuasense-mcp/) and [WeGravel MCP - Delivered Gravel Price by ZIP](/hermes/mcp/servers/external/wegravel-mcp/).

## Also identified this pass (not catalogued)

**The Marcoco27 regulatory-deadline family holds as a family.** Five arrivals in one window, `#7067` Biennial Update Sentinel for US motor carrier MCS-150 cycles, `#7068` Disaster Deadline Sentinel for county disaster and IRS relief postponements, `#7069` Sentinelle oppositions FR for creditor objections after a sale or merger, `#7070` Sentinelle phyto FR for pesticide authorisation grace periods, and `#7071` Sentinelle syndic FR for condominium mandate end dates. The class owner is already catalogued: [Sentinelle Creances MCP](/hermes/mcp/servers/external/sentinelle-creances-mcp/), added November 8, whose guide names the catnat sibling and states the shape, one register, one statutory clock, one x402 price per lookup. The two US items are the strongest of the five on substance, because the MCS-150 cycle and the 60-day IRS postponement are federal rules with penalties attached, and the transportation half of that ground is already held by [carrier-ledger-mcp](/hermes/mcp/servers/external/carrier-ledger-mcp/) on FMCSA carrier authority and insurance checks.

**The mambalabsdev fleet adds five** (`#7087` Dutch rental listings, `#7088` news article archive, `#7091` business PDF field extractor, `#7092` multi-platform social posts, `#7093` YouTube channel scraper), all one-tool npm packages wrapping Apify actors, on the standing Apify-actor hold class and the October 7 fleet ruling. Fifteen of the same publisher's items arrived in the night window; the fleet disposition is unchanged and the count now stands at thirty-eight across three waves.

**Class owners named, every remainder held.** Everything from **#7061** to **#7084** was already held by the 10:00 MST pass and is dispositioned here for the record, not re-litigated; the numbers above **#7084** are new to this window.  **Fortunest** (`#7062`) holds on household and portfolio finance against [Worthbase MCP](/hermes/mcp/servers/external/worthbase-mcp/), 28 tools for net worth, portfolios, cost bases and gains. **Foundingbird** (`#7074`) holds as a regional variant of company formation against [SparkLaunch](/hermes/mcp/servers/external/sparklaunch-mcp/) with its entitlement-gated incorporation cases and [Corply](/hermes/mcp/servers/external/corply-mcp/) forming Delaware corporations from chat. **LeftBlank Office** (`#7066`) holds on document production, closest to the print-ready export carried by CoDesign and Abyssale and to the Platemark data-to-files card that was evaluated and not catalogued on November 9. **Schedchie** (`#7064`), **Nimply** (`#7081`) and **Kreatix** (`#7097`) hold on the saturated social publishing class where Schedchie is itself already a named class owner. **WebGlazer** (`#7084`) and **Why Won't AI Mention My Product** (`#7090`) hold on the AI-visibility class carried by geolint, LogNorm and seo-with-rankspot. **buzzabout** (`#7077`) holds on social research beside SocialDataApi, Rizamo and Mostra. **OhSnap** (`#7078`) holds on uptime monitoring beside changedetection.io, Visualping and Cronitor. **Archipelago** (`#7079`) holds on agent memory beside PLUR, Azquo and KoalaFix. **Avasis**, **QuantBase** and **Forge Agent MCP** (`#7075`, `#7076`, `#7080`) hold on the x402 pay-per-call catalogue class with Warden MCP, Recta and nohumans.directory. **kalshi-fees** (`#7073`) and **crypto-exchange-fees** (`#7098`) hold on trading and crypto fee arithmetic, with the catalogued Kalshi MCP guide covering the exchange itself. **TradingAIHub** (`#7083`) holds as a directory of trading tools, a meta-directory rather than a data surface. **eda-agent** (`#7086`) holds on hardware design data, which this catalog disposed at BoardRepo as niche hardware development data even with six hundred tools for Altium, KiCad and EasyEDA in the reply. **IMALI Commander** (`#7082`) holds on developer tooling and the local-install tier. **CutVoke** (`#7085`) holds on media generation. **Spider** (`#7099`) holds on the scraping class. **Agents Hangout** (`#7061`) holds as agent-to-agent social infrastructure. **Pubroot** (`#7072`) holds on academic publishing. **The Outcome Layer** (`#7095`) holds as a consultancy's own product surface. **fotosize** (`#7065`) holds on the consumer utility class. **Bilkalkylen** (`#7096`) and **Föräldraledighetsplanen** (`#7094`), both from one author on Vercel hosts, hold as Swedish consumer finance and benefits planners rather than business surfaces. From the feed, `ez-image-to-image` holds on media generation and on being an agent card rather than a server listing, and `#7063` is a re-index request for the already-listed IntoDNS.ai rather than an arrival.

## Core listing check, measured

The four direct mcp.so detail slugs for CorpusIQ answer **404**, the recorded bare-slug failure rather than a delisting; `mcpservers.org /all` is the standing **403**; and the official registry still returns the four active `io.corpusiq/multi-source-mcp` records with **1.0.3** as the newest and the 40+ wording intact.

## Questions this pass answers

### What changed in the canonical at this gap?

Nothing. **20,396** distinct server URLs against **20,396** at the 04:32 MST capture, **0** additions and **0** removals, from **77,245** raw entries across the fifteen maps the index names. The apparent movement is an encoding artifact: three slugs the baseline stored with `%23` in place of `#` read as a removal and an addition each until both sides are normalized.

### Why are two price surfaces catalogued in one pass?

Because both attach a price to an address, and neither existed here before. One prices a truckload of stone delivered to a Florida ZIP and states the truck fee inside the unit price; the other prices an input in a named Kenyan county and refuses to estimate the one number a fertilizer decision depends on. Read together they are the same lesson from opposite directions: a price is only useful when you know what it is attached to.

## Counts

Canonical **20,396** against **20,396** with **0** additions and **0** removals from **77,245** raw loc entries across fifteen named maps, of which thirteen are server maps. Feed **144,705** and **144,738** bytes with **30** cards and **two** above the night cutoff. Queue **39** numbers, all arrivals. **41** candidates evaluated. One endpoint measured to the handshake plus protected-resource and authorization-server documents, one endpoint driven through **seven** calls across **four** tools. Two servers catalogued, two guides. Guide tree **1,138** directories before this pass and **1,140** after, **1,282** catalog entries before and **1,284** after.
