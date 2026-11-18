---
title: "MCP Server Discovery - November 17, 2026 (Evening)"
description: "A ten-hour window where a re-index wave carried 1,387 stamps over 600 listings, the feed supplied three cards, and four servers were catalogued."
category: "MCP Ecosystem"
last_updated: "2026-11-17"
---

# MCP Server Discovery - November 17, 2026 (Evening)

Fired on the **21:00 MST** tick, ten hours after the midday supplement closed. The canonical grew by **349** raw entries and **328** keys, almost all of it inside the new twelfth shard, the feed carried **three** cards, the queue carried **31** arrivals, and **four** servers ship: two keyless and driven, one installed from npm and driven in mock mode, and one measured to its OAuth gate.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          66,338   against 65,989 at the 18:07Z midday supplement
  servers/1..11               65,719   with server/11 alone moving 2,636 to 2,637
  servers/12                     619   against 271, the whole arrival of the window
distinct keys, twelve maps    22,440   against 22,151 retained from the 04:36Z capture
                                        (+328 additions, -39 absent)
lastmod >= 18:07Z              1,387 rows collapsing to 600 distinct listings
                                 273 of those already held before this window
mcp.so /feed                  200, 156,839 bytes, 44 anchors, 30 stamped cards,
                                 3 above the cutoff (21:47Z, 21:46Z, 21:44Z)
queue                          #7523 to #7553, 31 arrivals, no gaps
```

Three readings, and they tell different parts of one story. The raw entry count rose **349**, the distinct key set rose **328**, and the stamp count is four times the number of genuinely new listings, so a stamp on this surface is a re-index and not an arrival. The window's real content is a publisher fleet, and the holds below say which one.

## The feed

`mcp.so/feed` answered **200** at **156,839** bytes with **44** anchors, **30** stamp attributes and **37** distinct slugs. Three cards sit above the 18:07Z cutoff, all inside three minutes of each other:

| Stamp (UTC) | Slug | Disposition |
|---|---|---|
| 21:47 | `wireflow` | held, complete OAuth challenge, tool surface unmeasured |
| 21:46 | `verse` | held, 3D scene publishing, media-generation class dense |
| 21:44 | `signal-lab` | shipped |

The stamp format is still the `M/D/YYYY, HH:MM AM/PM` title attribute in UTC, now with `Submitted N minutes ago` as its display text. Any parser keyed on the display text returns zero cards; pairing each stamp to the nearest preceding `/servers/<slug>` anchor still works.

## What shipped

### Signal Lab MCP

Keyless and stateless at `https://signal-lab.qdt.ai/api/mcp`, *signal-lab-catalog* **1.6.0** on protocol **2025-06-18**, **26** tools, twelve driven. `catalog_info` reported **1,312** entries against the **1,112** the directory card advertises, and `list_filters` decomposed that into **1,260** datasets, **29** tools, **9** models, **9** recipes and **5** starter kits, with **1,236** badged Free, **49** Freemium, **26** Open Source and **1** Unofficial. The audit layer returned **50** servers for a *finance* query with a score, grade, pass label and report URL, and `get_trust_score` on a non-audited slug refused with the fix named. The trap is that filters AND: `crm` scoped to domain *Financial* returned zero.

### Edwin MCP

Keyless at `https://thebutler.network/api/mcp`, *edwin* **0.2.0**, six tools, eleven calls across four markets. The German television query returned three products whose offer list proves the model: Coolblue at **2,099**, Quelle at **2,119** and OTTO at **2,119** EUR with three separate `source_imported_at` stamps. Prices are feed snapshots and the server instructs the calling model never to call them live. Two defects are recorded: `min_price` at **300** EUR returned a **239** EUR product, and one soundcore product appears twice with two pids at the same price.

### SAP Business One MCP

Installed from npm at *@kodenova/sap-b1-mcp* **0.1.0** and driven over stdio with `SAPB1_MOCK=1`, nine read-only tools, six calls. The fixture ledger reconciles by hand: **8,000.00** plus **830.00** plus **4,500.50** equals the stated **13,330.50** total, and stock of **300** plus **40** equals **340** with available figures of **350** and **30**, which is in stock minus committed plus on order. `run_saved_query` is the security model in a tool: an unknown name is refused with the three administrator-registered queries listed.

### Laplace MCP

Auth tier at `https://gateway.laplacetec.com/mcp/`. The anonymous handshake returned **401** with a challenge naming `/.well-known/oauth-protected-resource/mcp/`, and that document answered **200** with resource, authorization server and four scopes. The product reconciles sales, contribution profit after COGS, channel fees and ad spend across Coupang, Naver Smart Store, Cafe24, Olive Young, Shopify and Amazon. The weak spot is the error tier: an invalid API key returns an empty 401 body.

## The wave, decomposed

The 327 arrivals outside the retained key set are not 327 products. They decompose as:

- **58** `apify-com` actor wrappers, a distribution class this catalogue holds.
- **60** `cotlet-dev-integrations` API wrappers plus **4** `cotlet-connect` connectors, a fleet already documented as one entry.
- **20** `gatavia-com` storefront slugs, **6** `tidybutton-com` tools, **5** `llpro-ai` slugs, **3** `ai-pick-tech` CAD plugins.
- **17** documentation mirrors, **2** vercel preview hosts, and one `-docs-mcp` cohort.
- The remainder a regional-SaaS and long-tail mix, none of which shipped.

## Holds, with the gate named

- **Wireflow** returned **401** with a complete OAuth challenge and a protected-resource route. A guide would be a credential promise, not a measurement.
- **Verse** publishes 3D scenes; the media-generation class is dense and no data surface is offered.
- **Survivor data** (**#7544**) publishes a paid x402 endpoint that answered **421 Invalid Host header** to three attempts, including one with the tunnel host set. A route that no client can reach is a defect worth recording, not a page.
- **GoCommerce** (**#7551**) is a self-hosted Go library with no hosted endpoint to probe.
- **Enigma** (**#7549**) is a local Rust binary in a covered memory class.
- **Sharpy** (**#7533**) is a macOS app helper with no remote route.
- **Treasury Risk Analyzer** (**#7523**) sits on the finance class already carried by TradingData and Kote Charts.

## Index repair

The November 17 night sweep had shipped its prose into the catalog index without its `## 🆕` heading, so the section rendered as a continuation of the previous one. This pass restores the header above it, in the same PR as the four new entries.

## Lessons recorded

- **A key extraction that takes one path segment silently merges owner/repo slugs.** The first pass of this sweep normalised every `/servers/<owner>/<repo>` URL to `<owner>` and reported **19,709** distinct keys against a retained **22,151**, a fall of 2,404 that reads as a purge. Joining every segment after `/servers/` returned **22,440**. The tell is a distinct count that falls while the raw count rises.
- **`r.jina.ai` refused every detail page at 401 bad IP reputation**, so mcpservers.org detail routes remain unreadable from this host and every candidate was resolved at its own endpoint or through the registry.
- **A mock mode is a shippable evidence tier.** The SAP server was installed and driven with no licence, no credential and no SAP connection, and every figure in its guide came from a real `tools/call`.
