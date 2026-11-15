---
title: "MCP Server Discovery - November 14, 2026 (Evening)"
description: "A ten-hour window in which the directory added 31 entries and three keys, the feed carried five cards, and four keyless servers were driven end to end."
category: "MCP Ecosystem"
last_updated: "2026-11-14"
---

# MCP Server Discovery - November 14, 2026 (Evening)

Fired on the **21:00 MST** tick, ten hours after the 11:00 supplement closed at 18:20Z. The canonical moved by **31** raw entries and **3** distinct keys, the feed carried **five** new cards, the queue **26** arrivals, and **four** servers ship. All four are keyless and all four were driven: this window did not contain a single OAuth-gated candidate worth writing from documentation alone.

## The window, measured

```text
mcpservers.org /sitemap.xml      200, fifteen maps named, twelve server maps
raw <loc> entries, maps 1-11     65,044   against 65,013 on the 17:03Z midday capture (+31)
per-map counts                   7,588 / 5,948 / 6,518 / 6,744 / 6,952 / 6,756 /
                                 9,351 / 6,590 / 4,030 / 2,607 / 1,960
per-map movement                 servers/8 6,589 to 6,590, servers/11 1,930 to 1,960 (+31),
                                 nine maps held to the entry incl. the corrected servers/9 4,030
distinct keys, locale-stripped   21,325   against 21,322 (+3)
priority-servers.xml             200 with 299 entries at /sitemaps/priority-servers.xml
                                 (not named by the index)
set diff, eleven maps plus priority   3 additions (mailpro-mcp, mojobase-mcp, oneiq-mcp),
                                 0 removals
lastmod rows at or after 18:00Z  114 rows, 51 distinct listings, newest 2026-11-14T20:10:41Z
mcp.so /feed                     200 at 156,313 bytes, 36 anchors, 30 stamped cards,
                                 5 above the cutoff, one slug on two stamps
submission queue #7348 to #7373  26 arrivals, no gaps, read with bodies in one call
```

## The canonical moved by three keys and one of them is a re-entry

The eleven numbered server maps returned **65,044** raw `<loc>` entries against the **65,013** the midday pass read at 17:03Z, and the **+31** sits entirely in two maps: `servers/8` moved from **6,589** to **6,590** and `servers/11` from **1,930** to **1,960**. The other nine maps, including the corrected `servers/9` at **4,030**, are identical to the entry. The eleven counts sum to 65,044 exactly, so nothing is double counted inside the capture.

The distinct locale-stripped key set read **21,325** against **21,322**, and `priority-servers.xml` answered **200** with **299** entries when read directly at `/sitemaps/priority-servers.xml`, which the sitemap index no longer names. Against the 04:36Z capture retained on disk, the like-for-like union of eleven maps plus priority gives exactly **3** additions and **0** absent keys:

| Slug | Disposition |
|---|---|
| `mailpro-mcp` | **unidentified**: the mcpservers.org detail route refused through the reader proxy at 401 on bad IP reputation, and mcp.so answers 404 for the slug |
| `mojobase-mcp` | the **Mojobase** held at the night pass pending a keyed session: a canonical slug for a catalogued product is an acquisition, not an arrival |
| `oneiq-mcp` | the **OneIQ** held on 13 November as read-only governed infrastructure context across VMware, Nutanix, Kubernetes and cloud |

Two of the three are products this catalog has already ruled on, arriving under a canonical slug. That is the third pass running in which a key delta on this surface was mostly slug acquisition.

**The 114 stamps are re-indexes.** At or after the 18:00Z cutoff, 114 `lastmod` rows collapse to **51** distinct listings, newest **2026-11-14T20:10:41Z** (`appcontrollabs/appcontrol-mcp-go`). The cohort is dominated by repositories this surface has stamped before: `builderio/agent-native`, `zambodotdev/zambo-mcp`, `hugo0/swarmmemo`, `audiojs/audio`, `sunglasses-dev/sunglasses`, `carrick-tools/carrick`, `fraisehq/fraise`. A stamp on this surface is a page re-read, and the per-map count is the arrival signal.

## The feed, five cards, one re-stamp

Read at **156,313** bytes with **36** anchors and **30** stamps in the `M/D/YYYY, HH:MM AM/PM` UTC form. Five cards sat above the 18:00Z cutoff:

| Slug | Stamp (UTC) | Handshake | Disposition |
|---|---|---|---|
| `cartesian-ecu` | 2026-11-15 03:03 | 401, *Sign in to your CARTESIAN account* | automotive flash checksum verification, a genuine vertical, held on access |
| `facet` | 2026-11-15 01:56 | 401, *sign in, or send a Facet API key as a bearer token* | the strongest hold of the window, see below |
| `social-fetch-d3f5b8` | 2026-11-14 21:32 | 401, `missing_bearer_token` with a remediation field | social-data class, held on access |
| `naturepedia-canonical-discovery-mcp-server` | 2026-11-14 20:14 | **200**, 3 tools | thin self-referential catalog behind x402, recorded thin |
| `hiapi-remote-mcp-73ef07` | 2026-11-14 19:32 | 401, *Missing Authorization header* | media-generation class, held |

**GridWhy appears twice on this read**, at 16:14Z and 17:33Z with one anchor between the stamps, which is the same single product stamped twice rather than two arrivals: this catalog catalogued it at the midday supplement and the double stamp is a re-stamp.

**Facet is the hold that deserves a later pass.** It describes itself as an autonomous model factory: its agent builds, evaluates, serves and maintains a small model for one narrow, repeated task. No entry in this catalog covers that slice, `model factory` and `fine-tune` both return zero, and the only reason it is not catalogued tonight is access: `initialize` on `https://facet.halfspacelabs.com/mcp` answers **401** with *unauthorized: sign in, or send a Facet API key as a bearer token*, with no protected-resource document named in the challenge. It is queued for a keyed or OAuth-tier pass rather than dismissed.

## The queue, 26 arrivals

Read in one authenticated call from **#7348** to **#7373**, with one gap in the numbering at #7361 that is a delete rather than a missing read, since the surrounding issues were all returned with bodies. Three of the 26 changed a disposition this catalog had already recorded, and none of them was an arrival:

- **#7368 PayStage** is a *listing update* to an existing entry, five tools shown and now nine, which is a surface change rather than a new product.
- **#7370 Axiocairn** is a **prior disposition**: *Axiocairn Research* was held in the saturated finance and market-data class on 13 November.
- **#7350 mcp-reportcard** restates the standing **CLI rather than a server** disposition, and its own body says so.

The remainder held by class with the owner named: **ATSPrep** (`#7355`, **19** keyless tools across resume critique, ATS keyword matching, cover letters, interview prep and LinkedIn fields, a substantive surface that loses only on class, where *Run it by* and *GenEdAI ModernCV* already sit); **HornLib** (`#7365`, keyless, eight French horn tools, hobbyist one-instrument vertical beside Thiri Chord Intelligence, and carrying the `mcprush.com` builder token in its instructions field); **Aidenix** (`#7360`) and **Atlas by Aidenix** (`#7359`) on the sales-data class owned by the Apollo, Coresignal and PeopleDataLabs entries; **PromptGuard** (`#7358`) on the class this catalog already covers with its own GLC PromptGuard guide; **Pomerado** (`#7369`, browser automation), **Toolkien** (`#7354`, MCP gateway), **repo-cartographer** (`#7349`, codebase mapping), **ACE Music** (`#7371`, media generation behind a `useapi.net` token), **AgentGas** (`#7356`) beside SaltCrate's Oracle on the x402 class, **myio-mcp** (`#7357`, Hungarian smart-home controller), **Splyt** (`#7364`, fitness tracker), the four **usocial.space** arcade servers (`#7362`), the **AIgorithmic Butterfly Effect** artwork (`#7372`) as a novelty, and **MCP Connect Lite for Odoo** (`#7348`), which needs a running Odoo instance before it can say anything about an Odoo surface; **BH Agent Debugger** (`#7351`) is Windows only.

## The four that shipped

**StackRates** (`https://stackrates.ai/mcp`, keyless, **5** tools, all five driven). Hosting prices read daily from providers' own pages, with the source, the read date, the term and the VAT note on every line, and the dataset published CC BY 4.0. The ordering finding: a 4 GB box in Germany under $10 a month ranks a **$4.97** Luxvps plan above a **$4.41** AlphaVPS plan, because the sort is the twelve month total and the AlphaVPS line carries **$10.05** of 19% VAT the other line does not state. Hetzner CPX32 came back at **$36.09** a month including **$0.60** for the IPv4 address against Vultr Regular 8GB at **$40.00** for the same 4 vCPU / 8 GB / 160 GB. `current_vps_offers` returned **8** offers and the sentence that **0** beat the cheapest regular plan over a year, with DreamHost's $8.99 for three months then $15.99 totalling **$170.88** in year one. `server_for_app` answers from **192** documented requirements, and one of them is n8n at **320 MB**, which fits a **$2.04** box on a twelve month term. **Defect:** unknown argument names are silently ignored, so a request using names the schema does not print returns an unfiltered answer with no error.

**CheckChinaTransit** (`https://checkchinatransit.com/api/mcp`, keyless, **8** tools, seven substantive). The first entry here for China's visa-free transit policy. A US passport returned eligible on both the 240 hour and 24 hour rules, an Indian passport returned *not on the 54-country list* with the 24 hour route named as the alternative, Singapore to Japan passed the third region test while Singapore to China to Singapore was refused as a round trip, and the three deadline tiers for a 2026-11-15 arrival reproduced by hand against the midnight rule: **2026-11-25 23:59**, **2026-11-21 23:59** and **2026-11-16 23:59**. The best string in the server is the TIMATIC phrase in the checklist tool, which prevents the refusal that actually happens, at check-in. **Two defects:** `lookup_china_transit_port_zone` returned the **identical** payload for `PVG`, `PEK` and the invalid `ZZZZ`, so the promised zones and ports do not exist; and the `instructions` field is a bare builder token, `mcprush.com-eec7a370865b13a747c4179c`, with no product text.

**Transformer.gg** (`https://transformer.gg/mcp/public`, keyless public tier, **1** tool, eleven calls). Prices one sponsored X post from a published curve anchored at **$50** for 1,000 followers, **$1,200** at 100,000, **$10,000** at 1,000,000 and **$25,000** at 5,000,000 or more, with a **0.75x** to **1.35x** adjustment. `levelsio` returned **$9,050** to **$13,600** with an **$11,325** midpoint, `elonmusk` **$19,950** to **$29,900**, and the two accounts inside one 1M to 5M band returned **$12,175** and **$25,825**, a factor of **2.1** apart that the published method cannot explain to a caller because the engagement inputs are not returned. **Two control results:** the *usual* figure is the exact midpoint of the range in all four rows, and every range is a fixed **1.5x** of its own floor, narrower than the multiplier window the method describes. **Defect:** a valid handle for an account that does not exist returns the same *That isn't an X handle* error as a malformed one.

**PaintColorMatcher** (`https://paintcolormatcher.com/api/mcp`, keyless, **8** tools, all eight driven). **11,249** official Sherwin-Williams, Benjamin Moore and Behr colors matched by CIEDE2000 rather than RGB distance. `#EAE6DF` returned Benjamin Moore **2108-70 Lacey Pearl** at delta **0.62**, Behr **MQ3-32 Cameo White** at **0.70** and Behr **BWC-06 Solid Opal** at **0.97**; `Agreeable Gray` resolved to **SW 7029** and found Behr **Cotton Grey HDC-NT-20** at **0.60**. The gallon estimator reconciles by hand: 52 by 9 minus two doors at 21 square feet and two windows at 15 gives **396** net, **792** over two coats, **2.11** gallons at **375** square feet per gallon, and **3** purchased with a touch up buffer. **Limit:** the sheen tool answered *Matte or Eggshell* for a kitchen with an appearance reason and no washability field.

## The control that matters most

The paint engine's claim is a formula, so the formula was rewritten independently in Python for this pass: sRGB to CIE Lab through D65, then CIEDE2000 with the G compensation, the hue averaging rules, S_L, S_C, S_H and the R_T rotation term.

| Pair | Server | Mine |
|---|---|---|
| `#D1CBC1` against `#CFC9BF` | Lab 81.9 / 0.33 / 5.72, delta **0.49** | Lab 81.90 / 0.34 / 5.71, delta **0.491** |
| `#EAE6DF` against `#e8e5df` | Lab 91.42 / 0.13 / 3.88, delta **0.62** | Lab 91.42 / 0.14 / 3.87, delta **0.627** |

Lab agrees to **0.01** and the distance to **0.007**, which is rounding on both sides. An engine that reproduces the standard to that tolerance is doing the work it claims, and the four guides in this pass each carry an arithmetic control of the same kind: the deadline tiers, the twelve month totals, the midpoint identity and this one.

## Counts

Canonical **65,044** against **65,013** (+31, two maps), distinct keys **21,325** against **21,322**, priority **299**, set diff **3 additions and 0 removals** on the eleven-map-plus-priority basis, **114** `lastmod` rows above the cutoff collapsing to **51** listings, **5** feed cards above the cutoff with **1** slug on two stamps, **26** queue arrivals, **4** servers catalogued and **4** guides, **20** candidates held with the class owner or the reason named, and **1** recorded unidentified rather than guessed.
