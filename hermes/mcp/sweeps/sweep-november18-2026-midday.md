---
title: "MCP Server Discovery - November 18, 2026 (Midday)"
description: "A canonical flat to the key set and a queue that carried all three ships: a landed-cost forwarder, an analytics case archive and a margin calculator."
category: "MCP Ecosystem"
last_updated: "2026-11-18"
---

# MCP Server Discovery - November 18, 2026 (Midday)

Fired on the **10:00 MST** tick, six and a half hours after the night sweep closed. The canonical moved by **four raw entries and zero keys**, the feed carried **five** server cards, and the queue carried **twenty-two** arrivals. All **three** ships came from the queue. The feed contributed nothing that survived a class check, which is the pattern this week: the delta is not where the material is.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          66,342   against 66,338 at the 14:01Z night capture
  per-map                     7,588 / 5,949 / 6,518 / 6,744 / 6,954 / 6,756
                              9,351 / 6,590 / 4,024 / 2,608 / 2,637 / 623
                              summing to 66,342 exactly
  movement                    servers/12 619 to 623, every other map held to the entry
priority-servers.xml          299 raw entries, 34 distinct keys not in the twelve maps
remote-mcp-servers.xml         15 raw entries, zero server keys
distinct keys, twelve maps    22,440  against 22,440 at the night capture
                              = 0 additions and 0 removals
union with priority map       22,474  on both captures
lastmod >= 2026-11-18T14:01Z  18 rows, 2 distinct listings, both inside the key set
                              (newest anywhere: 2026-11-18T14:17:14Z)
mcp.so /feed                  200, 157,495 bytes, 35 server anchors, 1 agents anchor,
                              1 clients anchor, 30 stamps,
                              5 server cards above the cutoff
queue                         #7578 to #7599, 22 arrivals, no gaps
```

The set diff is the measurement that matters and it is **zero on both sides**. The four extra raw entries are further URL forms under keys the index already holds, all four inside `servers/12`, the shard that has carried nearly every raw rise since it appeared on November 17. Reporting the raw count alone would have said the directory grew; the key set says it did not.

The `lastmod` scan corroborates it. Eighteen rows carry a stamp at or after the 14:01Z capture, they collapse to **two** distinct listings, and both are inside the key set this pass measured. A re-index, not an arrival.

## The feed, paired properly

Thirty stamps against thirty-five server anchors is the shape every pass since October has recorded: the newest cards first, then the featured rail. This read carries **two** non-server anchors as well - one `/agents/` card at 10:15Z and the `/clients/` sponsor card the night pass identified - and both sit inside the stamp sequence, so a pairing that assumes a single anchor family mislabels everything after them. Walking the document and attaching each stamp to the nearest preceding anchor of any family gives a clean sequence:

| Stamp (UTC) | Slug | Disposition |
|---|---|---|
| 16:50 | `mdexa` | held, dataset licensing rather than business data |
| 16:11 | `sofast` | held, static-site hosting for AI-built pages |
| 15:43 | `agenttrust-kye` | covered, `agenttrust-mcp` is already catalogued |
| 15:15 | `vedicdostvedicdost` | held, astrology |
| 14:07 | `suidasu` | held, AI-OCR for invoices and fax orders, on the dense document-extraction class |
| 10:15 | *(agents rail)* `saascity-io` | not a server card |
| 06:51 | `lake-meter-e05535` | already dispositioned at the night pass |
| 04:22 | *(clients rail)* `rapidoddsapi` | sponsor card, not a server |

Five server cards inside the window, none of them a ship. `suidasu` is the only one that was a real candidate - a Japanese AI-OCR service that reads invoices, fax order forms and handwritten reports - and it lands on the document-extraction class the catalogue has carried since the OCR entries, so it is held with the class owner named rather than catalogued on a card alone.

## What shipped

### [Global Shopaholics MCP - Landed Cost From a US Address](/hermes/mcp/servers/external/global-shopaholics-mcp/)

Keyless at `https://mcp.globalshopaholics.com/mcp`, *global-shopaholics* **1.0.0** on protocol **2025-06-18**, **seven** tools of which **five** were driven with no credential. The two `request_*` tools were left undriven on purpose: both open a human intake and neither is a read.

**The duty rule is the product.** A $400 German order returns an assisted-purchase fee of **20.00** on a stated 5%-with-$5-minimum basis, a duty and tax band of **79.80 to 139.78**, and the rule that produced it: 19% VAT, no VAT threshold at all, the €150 duty-free threshold **abolished on 1 July 2026** and replaced by a €3 per-category charge that expires on 1 July 2028. The same call for the UAE returns 5% VAT and a Dubai-only duty exemption for consignments under AED 1,000, roughly **$272**, from 3 August 2026. Germany 2026 is exactly the kind of fact a general model gets wrong, and here it arrives with the date it changed.

**A live quote needs the documented shape.** A UAE call passing `"weight": 2` at the top level instead of inside a `package` object returned `international_shipping: null` and a total of **275.63 to 289.41**. Supplying `package` for the same order produced DHL Express at **48.58** in 3 to 5 days and a total of **326.63 to 342.96** - **fifty-one dollars** between the two readings, with the wrong one looking finished. The tool does not declare `additionalProperties: false` and does not warn on an unknown key.

Also driven: `get_shipping_rates` on Nigeria at 5 kg (FedEx Intl. Connect Plus, **$174.68**, 7 to 10 days, resolving to a delivery date of 2026-12-02), on the United Kingdom at 2.5 kg, and on the country code `ZZ`, which refuses by name and points at the public calculator; `get_services_and_fees`, which publishes both plans with a `last_checked` date and a source URL each; and `track_shipment`, which returns four carrier links and flags its own carrier guess as `guessed_from_format`.

### [effectsize MCP - A Product Analytics Case Archive](/hermes/mcp/servers/external/effectsize-mcp/)

Keyless on the public route at `https://mcp.effectsize.io/mcp/public`, *effectsize-cases-public* **v0.4**, **two** tools and both driven. The search takes an abstract description of the decision, not keywords, and its own instructions tell the model to search before answering from general knowledge and to say so when the archive has no close case.

**The ranking is a candidate list, and it says so.** A checkout test with interference between arms returned **104** full matches from **365** candidates under `search_id a641c839dd6b`; a short-history forecasting question returned **52** from **306** under `0e4da0bbc879`. Both carry the same `snapshot` value, so the archive is versioned and two callers on the same day read the same corpus.

**The cards are the payload.** The Lyft card's problem section names the mechanism - riders and drivers share one pool of supply, so one user's treatment changes what another gets, and the independence assumption breaks - and its solution names the remedy: choose the randomisation unit to fit the interference, then wrap it in a pre-registered hypothesis, a Benjamini-Hochberg correction across many primary metrics, an experiment scheduler and a decision log. The Apple card answers the other half: randomise users but compute the metric per session and the rows of one user are correlated, so the standard formula understates the variance and asks for too few observations. Each card also declares whether its original can be fetched - Lyft's is marked `bot-blocked`, Apple's `open` - which is the difference between a citation and a wasted fetch.

**One defect recorded:** an unknown slug returns HTTP 200 with `isError` false and the error inline per card (`{"slug": ..., "error": "unknown slug"}`), so a client that renders only the content block shows an empty answer as if it were a result.

### [TrueMargin MCP - Cross-Border Margin Audit](/hermes/mcp/servers/external/truemargin-mcp/)

Local stdio from `github.com/yixuanrobot/truemargin-mcp`, *truemargin-1688-scout* **1.0.0**, **two** tools and both driven over line-delimited JSON-RPC with **nine** `tools/call` requests. The submission describes an installable package; **`truemargin-mcp` is not on PyPI**, and the README's `uvx --from git+...` path is the one that works.

**The waterfall is honest and reproduces to the cent.** `"Magnetic POV Neck Phone Holder | 24.99 | 180g | ¥18"` on TikTok Shop US gives landed COGS **8.22**, net **7.12**, margin **28.48%** and break-even ROAS **2.35**, every figure recomputed by hand from the published rate table: a 15% carton weight buffer onto **0.207** billed kg, **88** CNY/kg plus an **18** CNY registration fee for the battery-and-magnetic class, a **6.5%** customs buffer applied to the declared factory value rather than the retail price, 6% referral and 15% affiliate. A **6.99** phone case with a real **¥9** factory cost flips it to **KILL** at **-44.85%**.

**Two defects, both measured.** Without an override the tool **invents its inputs**: three unrelated products - earbuds, a kitchen scale, a soy candle - all returned retail **26.99**, factory **23.42** (which is `26.99 x 0.125 x 7.22`) and three confident `GO` verdicts. And the `verifiedFactories` array is **generated, not found**: names are the belt hub plus a fixed suffix, repurchase rates and years active come from an `md5` of the product title, and unit prices are the base cost times 0.96, 1.02 and 1.36. Because `audit_batch` reports that first synthetic tier rather than the supplied cost, a stated **¥18** comes back **17.28** and a stated **¥9** comes back **8.64** - both exactly 96% of input, so every SKU is flattered by about four percent of its factory cost.

## Also identified this pass (not catalogued)

Held with the class or the gate named. **Highseat** (**#7593**), web analytics with revenue attribution behind OAuth 2.1 and a workspace picker, held because the tool surface cannot be measured without an account; **Mdexa** (**#7596**, also the feed's newest card), dataset licensing facts for medical AI, a research register rather than a business data surface; **metri** (**#7591**), a calorie and macro diary, and **Verateca** (**#7595**), a supplement-label guide, both consumer health; **Kenoverse** (**#7590**), quiz and spaced repetition; **Wandria** (**#7594**), a trip planner on an account; **BounceLayer** (**#7588**), email verification, commodity class carried since the MailTester trio; **GigaMail** (**#7580**), mail sending; **api.zato.org** (**#7578**), x402 pay-per-call web and on-chain tools, payment-rail class; **AIClipMaker** (**#7583**), media generation; **SoundEdit** (**#7585**) and **Fidelia** (**#7584**), desktop audio apps whose servers are off until a person enables them; **Plinth** (**#7581**) and **Rendra** (**#7586**), publishing and documentation authoring; **Inkmap** (**#7575**); **ctxprune** (**#7599**), context compression for agents; **Human Use** (**#7587**), a device driver for a person, novel but with no business data; **DankMachine** (**#7592**), a meme soundboard; **movin.design** (**#7579**); **Dock** (**#7574**) carried from the night pass; and the **five**-item `mambalabsdev` fleet (**#7565**, **#7567**, **#7568**, **#7569**, **#7570**) recorded as one line per the standing publisher-fleet rule. **#7598** is a listing update for a catalogued product, not a candidate.

`/all` was not re-read: **403** by edge policy, the standing condition since 4 November, so page-1 membership is absent evidence rather than asserted.

## Listing verification

The four directories the tick names, re-measured rather than inherited:

```text
mcpservers.org   LISTED in the platform's own index, both forms present in the twelve-map
                 capture: /servers/corpusiq-io and /servers/corpusiq/corpusiq-docs
                 (m5.xml). Detail routes 403 by edge policy, so the sitemap is the evidence.
mcp.so           LISTED at /servers/corpusiq-docs, 200 at 856,686 bytes, nine corpusiq
                 hits; bare slugs corpusiq and corpusiq-io still 404 as recorded.
glama.ai         LISTED at /mcp/servers/CorpusIQ/corpusiq-docs, 200 at 231,071 bytes,
                 thirteen hits.
smithery.ai      registry returned 500 as a query-surface error and the marketing page
                 404 against live controls; NOT recorded as a delisting, not resubmitted.
Anthropic        NOT listed. scripts/anthropic_directory_watch.py exit 0, 1,159 pages,
                 zero hits.
```

## Counts

```text
canonical        66,342 against 66,338  (+4 raw, 0 keys)
distinct keys    22,440 against 22,440  = 0 additions, 0 removals
union            22,474 on both
lastmod          18 rows above the cutoff, 2 distinct listings, both held
feed             157,495 bytes, 5 server cards above the cutoff, 0 ships
queue            22 arrivals (#7578-#7599)
catalogued       3 with 3 guides
held             18 candidates with the class or gate named
guide tree       1,207 to 1,210 directories
```
