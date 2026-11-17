---
title: "MCP Server Discovery - November 17, 2026 (Night)"
description: "A new twelfth sitemap shard delivered 151 listings with zero removals, two feed cards arrived, seven queue entries filed, and six servers earn a page."
category: "MCP Ecosystem"
last_updated: "2026-11-17"
---

# MCP Server Discovery - November 17, 2026 (Night)

Fired on the **03:00 MST** tick, six hours after the evening sweep closed. The directory grew a **twelfth numbered sitemap shard** carrying **151** new listings and **zero** removals, the feed carried **two** cards, and the submission queue carried **seven** arrivals. **Six** servers ship, three of them driven end to end without a credential.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, fifteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-11          65,556   identical to the 05:06Z evening capture, map for map
servers/12.xml                NEW shard, 247 raw entries, 151 English keys, all new
raw <loc>, numbered total     65,803   (+247, the whole rise inside the new shard)
static.xml / priority-servers 822 / 299, both held
distinct keys, locale-stripped 21,993  against 21,842 retained = 151 additions, 0 removals
locale prefixes present       de, es, fr, hi, id, ja, ko, pt-BR, ru, th, tr, vi, zh-CN, zh-TW
mcp.so /feed                  200 at 157,125 bytes, two cards above the cutoff
submission queue #7493-#7500  7 arrivals, bodies read in one authenticated call
```

## The arrival was a shard, not a wave

The eleven numbered maps that carried this catalogue to date returned **65,556** raw `<loc>` entries, identical to the evening capture and summing exactly to it map for map: **7,588**, **5,949**, **6,518**, **6,744**, **6,952**, **6,756**, **9,351**, **6,590**, **4,030**, **2,607** and **2,471**. The movement sat entirely in a map that did not exist at the evening read: **`servers/12.xml`**, **247** raw entries, of which **151** are English server keys and **151** are new to the retained set.

That is the cleanest diff this surface has produced in a week: **151 additions and 0 removals**, every addition inside one shard, no locale re-sharding to disentangle and no per-map drift to explain. The previous two passes had to argue their way to a small number through locale forms and duplicate rows; this one does not.

## What the 151 actually are

The shard is not a curated batch. Reading the keys, the shape is publisher-driven:

- **Per-source tool wrappers.** One vendor publishes multi-source scraper wrappers in families; the largest single cohort in the shard is a pricing-data vendor's per-source connectors, one key per data source.
- **Documentation mirrors.** A dozen keys read as `docs-<vendor>-com-...` or `www-<vendor>-cn-...`, which are documentation sites dressed as connectors rather than data surfaces.
- **Vertical directories.** Storefront-builder add-ons, agent marketplaces and regional listing sites, none of which carry a dataset.
- **Genuine products, a minority.** Six of the 151 survived triage and are catalogued below. Eleven more were held with the class owner named in the index, and the remainder fail one of three tests: no live endpoint, no data behind the tool names, or a category this catalogue already carries twenty deep.

## The two feed cards

| Stamp (UTC) | Slug | Disposition |
|---|---|---|
| 07:12:56 | `vizbl` | **Ships.** Ecommerce AR: OAuth with dynamic client registration, 40+ tools split read / write / destructive |
| 04:43:17 | `calderflow` | **Ships.** Diagrams as an MCP App: ten chart tools, handshake open, calls keyed |

## The queue, seven arrivals

**#7493** to **#7500**, all filed after the evening sweep's last read at **#7492**. Bodies read in one authenticated call.

- **ShopSavvy** (**#7496**) ships, and is the pass's strongest find: keyless, **fifteen** tools, **three** driven, **25** offers on one barcode and a **$53** spread between retailers on the same day.
- **VideoDB** (**#7500**) replaces `videodb-director` and answers **401** with `invalid_token`; video indexing is class-covered here and the arrival is a replacement rather than an addition.
- **Tintloom** (**#7498**), **BunCho** (**#7497**) and **Server4Agent** (**#7495**) each return **401** with a sign-in sentence naming the product, which is the OAuth tier held all week.
- **pilotfish** (**#7493**, **#7494**) ships as an open MCP and a managed variant from one repository; the managed half is a hosted proxy over the open one, and the class is agent tooling rather than data.

## What ships, and at which evidence tier

**Three keyless and driven.**

- **ShopSavvy** - `initialize` **200** as *shopsavvy* **2.0.0**, **fifteen** tools, three driven: search returned **20 of 72** matches, offers returned **25** retailer offers from **$38.22**, and history returned **Walmart $142.98** beside **Crate & Barrel $89.99** on the same day. Two defects recorded: dozens of *No historical data available* retailer rows including obvious catalogue noise, and a duplicate Walmart series.
- **SpendCanary** - `initialize` **200** as *spendcanary-free-tools* **1.1.0**, **eight** tools, four driven, stateless with no session id. CPC **1,200 / 400** answered **$3.00**; ROAS **10,000 / 2,500** answered **4.00x**; a **100** budget answered **200** daily and **3,040** monthly; a three-row search terms CSV answered **47%** of spend on two zero-conversion terms. Two wrong-argument calls returned the exact schema names it wanted. One integration trap measured: a POST with no `Origin` header is refused **403** and the same POST with an Origin answers **200**.

**Three at the documented tier, with the schema measured where the server allows it.**

- **CalderFlow** - handshake **200** as *calderflow* **0.1.0**, **ten** chart tools with required arguments read from live schema, `resources/list` serving a `ui://calderflow/chart-<id>` resource typed `text/html` (the MCP Apps pattern), `prompts/list` returning **-32601**, and `tools/call` returning `isError: true` with its three named credential paths.
- **Vizbl** - endpoint refused an anonymous handshake at **403**; endpoint, transport, OAuth-with-DCR flow and the 40+ tool surface read from the vendor's connector documentation, including the rule that a read-only connection does not list write tools and that try-on generation is not exposed in chat.
- **Trenz** - endpoint answered **401**, so the fifteen-plus research, create, publish and measure tools are quoted from the vendor's MCP documentation across **15** TikTok Shop markets.
- **app2email** - endpoint answered **401**; the protocol claim (**five** revisions from 2024-11-05 to 2026-07-28) and the twenty tool sets with their counts are read from the vendor's MCP reference, including the **Approvals** set whose `approve_send` is a gate inside the surface and a sandbox key that sends nothing to WhatsApp.

## Held this pass (with the reason)

`thriftyowl-money` was held by the previous pass and is carried as held. From the queue: **VideoDB** as a replacement over a covered class, **Tintloom**, **BunCho** and **Server4Agent** on their sign-in sentences, and **pilotfish** as agent tooling. From the shard, the held classes are documentation mirrors, storefront-builder add-ons, agent marketplaces, x402 settlement surfaces and publisher fleets whose keys describe a wrapper rather than a dataset.

## Counts

```text
canonical, numbered maps   65,803 against 65,556   (+247, a new shard)
distinct keys, unioned     21,993 against 21,842   (151 additions, 0 removals)
static / priority maps     822 / 299, both held
feed                       157,125 bytes, 30 stamped cards, 2 above the cutoff
submission queue           7 arrivals, 1 shipped
candidates evaluated       151 shard keys + 2 feed cards + 7 queue arrivals
guides                     6 new guide directories
guide tree                 1,190 directories before this pass, 1,196 after
```

## Questions this window raises

### Why is a new sitemap shard the whole delta?

Because the directory publishes in fixed-size shards. When one fills, the next URL goes into a new file rather than extending an existing one, so a shard's first appearance is the exact size of the batch behind it. Here that is **247** raw entries and **151** English keys, and the eleven maps that already existed came back identical to the evening capture, which is what makes the diff readable as **151 additions and 0 removals** rather than as background churn.

### What does a 403 on a detail route prove?

Nothing about the listing and everything about the edge. `mcpservers.org` returns **403** to detail pages from this host while the sitemaps stay open, so a page-level read is absent evidence rather than a delisting. Every candidate in this pass was resolved at its own endpoint instead: a **200** handshake, a **401** with a sign-in sentence, or a documented surface read from the vendor.

