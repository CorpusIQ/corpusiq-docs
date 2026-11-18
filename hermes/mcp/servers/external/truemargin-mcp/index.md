---
title: "TrueMargin MCP - Cross-Border Margin Audit"
description: "A landed-COGS waterfall that reproduces by hand, from a server whose verified factory tiers are generated from the product name."
category: "E-commerce / Finance"
stars: "0 (local stdio, python -m truemargin_mcp from github.com/yixuanrobot/truemargin-mcp; two tools, both driven; the PyPI package named in the submission does not exist)"
added: 2026-11-18
source: "the mcp.so submission queue entry #7589 filed 2026-11-18T13:00:09Z, and a driven session on 2026-11-18 running the server from source over JSON-RPC on stdio, with every figure reproduced by hand"
relevance: ★★
tags: [ecommerce, margin, unit-economics, landed-cost, 1688, sourcing, stdio, local, mcp]
last_updated: "2026-11-18"
---

# TrueMargin MCP

**Selling a unit for twenty-five dollars and buying it for three looks like a business until the freight, the tariff, the platform cut, the affiliate cut and the returns land on the same line.**

Cross-border unit economics is a waterfall problem: six deductions between the price and the profit, each one computed on a different base, and a seller who misses one of them discovers it at the end of the quarter. A calculator that lays out the waterfall is genuinely useful. What this server adds - and what makes it worth documenting rather than simply recommending - is that it does the arithmetic transparently and dresses a large part of its output up as research it did not perform.

```text
Server type:   local stdio (Python, standard library only)
Command:       python -m truemargin_mcp
Source:        https://github.com/yixuanrobot/truemargin-mcp  (MIT)
Server:        truemargin-1688-scout, version 1.0.0
Protocol:      negotiated down to 2024-11-05 from a 2025-06-18 offer
Tools:         2 (audit_crossborder_sku_margin, translate_1688_factory_query)
Author's apps: https://truemargin.aitruelabs.com  (web calculator)
               https://apify.com/aitruelabs/truemargin-1688-profit-scout
Listed on:     the mcp.so submission queue as #7589
```

## The evidence tier

Local process, driven end to end. The server was cloned and run from source with `python -m truemargin_mcp`; `initialize`, `tools/list` and **nine** `tools/call` requests were exchanged over line-delimited JSON-RPC on stdio. Both tools answered.

One install claim in the submission does not hold. The issue text describes `truemargin-mcp` as an installable package; it is **not on PyPI** - `uv pip install truemargin-mcp` fails with *not found in the package registry*. The README documents the real path, `uvx --from git+https://github.com/yixuanrobot/truemargin-mcp truemargin-mcp`, which works because the project has zero dependencies. The fix is one line in the submission, but a user who follows the queue text and not the README gets nowhere.

The protocol version is also worth recording: the server accepts a 2025-06-18 offer and answers with **2024-11-05**, the older of the two it supports. It works, and a client negotiating strictly could stall.

## The waterfall, and it reproduces to the cent

`audit_crossborder_sku_margin` takes a list of product strings, a sales channel, a shipping mode, an affiliate percentage, an expected refund rate and an ad CPA. Supplied with a real price and a real factory cost in its documented pipe form:

```text
"Magnetic POV Neck Phone Holder | 24.99 | 180g | ¥18"
channel tiktok_shop_us   shipping direct_packet_3pl   cpa 3.50
```

the reply is a complete deduction chain:

```text
retail                     24.99
factory unit               17.28 CNY  = 2.3934 USD at 7.22
china inland + QC           0.65      = 2.20/7.22 + 0.35
intl freight + tariff       5.17      = (0.207 kg x 88 + 18)/7.22 + 6.5% of factory
landed COGS                 8.22
platform referral           1.50      = 6%
creator affiliate           3.75      = 15%
refund / RTO loss           0.91      = 14% of a 75%-loss-on-return model
ad CPA                      3.50
net profit                  7.12
net margin                 28.48%
break-even ROAS             2.35
verdict                    GO
```

Recomputing that by hand from the published rate table gives **8.22 landed, 7.12 net, 28.48% and 2.35** - every figure to the cent. The billed weight is the parcel weight plus a 15% carton buffer, the freight uses 88 CNY/kg plus an 18 CNY registration fee for the battery-and-magnetic class, and a 6.5% customs buffer is applied to the declared factory value rather than the retail price. That last choice is the correct one and it is the one most spreadsheets get wrong.

Feed it a bad unit and the verdict flips, which is the test that matters:

```text
"Silicone phone case | 6.99 | 60g | ¥9"
landed COGS 4.66 · net -44.85% · verdict KILL
```

The engine, then, is real. Two defects sit on either side of it.

## Defect one: without an override it invents the inputs

Called the way the schema invites - a product name and nothing else - three unrelated products returned the **same** retail price and the **same** factory cost:

| Input | Retail | Factory CNY | Landed | Margin | Verdict |
|---|---|---|---|---|---|
| wireless earbuds, bluetooth 5.3 | 26.99 | 23.42 | 10.11 | 24.49% | GO |
| stainless steel kitchen scale | 26.99 | 23.42 | 4.65 | 28.25% | GO |
| scented soy candle, glass jar | 26.99 | 23.42 | 5.78 | 27.07% | GO |

26.99 is a hard-coded fallback retail price and 23.42 is `retail x 0.125 x 7.22` - a factory cost assumed to be 12.5% of whatever the retail price was assumed to be. Three products in three unrelated categories produce three confident `GO` verdicts built on two invented numbers. The schema's first documented usage is exactly this path: the `items` description lists "English product names" before it mentions the pipe form, so the natural call is the one that fabricates its own inputs.

## Defect two: the "verified factories" are generated, not found

The reply also carries a `verifiedFactories` array with supplier names, authenticity scores, repurchase rates, years active and MOQ ladders. Reading the source shows how each field is produced:

```text
supplierName      belt hub + a fixed Chinese suffix
repurchaseRate    28.0 + (md5(product title) mod 14)
yearsActive       5 + (md5(product title) mod 6)
authenticityScore computed from those same synthetic inputs
unitPriceCny      base cost x 0.96   (the second tier x 1.02)
ladder1000Units   base cost x 0.84
```

The function's own docstring calls them *"realistic, cluster-calibrated supplier benchmark profiles"* and *"verified"*. No lookup happens and no network call is made. A third entry is described as a *"1-Piece Dropship Reseller - Filtered Comparison"* and then screened out by a repurchase-rate threshold - a middleman filter applied to an entity that was never contacted.

**The consequence reaches the headline number.** Because `audit_batch` reports the first synthetic tier rather than the supplied cost, the factory cost you gave is never the factory cost you get back: a stated **¥18 returned 17.28** and a stated **¥9 returned 8.64** - both exactly 96% of the input. Landed COGS, margin and verdict are all computed on the discounted figure, which flatters every SKU by about four percent of its factory cost.

None of this makes the server useless. It makes it a **calculator** rather than a research tool, and the difference is worth stating plainly: the freight tables, the channel fee rates and the returned waterfall are honest and reproducible, and the supplier names, scores and repurchase rates are decoration.

## The second tool is real and narrower

`translate_1688_factory_query` turns an English product title into a 1688 search query and a GBK-encoded URL, with the industrial belt named and a QC checklist attached:

```text
"wireless earbuds bluetooth 5.3 with charging case"
 -> 无线 跨境专供 源头工厂 现货
    Shenzhen / Dongguan / Ningbo (Electronics & Mold Cluster)
    BATTERY_MAGNETIC
    s.1688.com/selloffer/offer_search.htm?keywords=%CE%DE%CF%DF%20...

"scented soy candle glass jar"
 -> Guangzhou / Shantou (Daily Chemical OEM Cluster)  ... after keyword match
```

The GBK percent-encoding is the substantive part. 1688's search endpoint expects the older Chinese encoding, and a UTF-8 query returns noise or nothing - a real obstacle that most English-language guides skip. The belt routing is a keyword match against a fixed rule table, so it is a lookup with a documented fallback rather than a synthesis, and the QC checklist that comes with it is genuinely useful for a first factory order.

### Can the margin model be trusted with real numbers?

Yes, within its own assumptions, and the assumptions are visible. Randomised refund loss at 14% of a 75% loss-on-return, a fixed 6.5% tariff buffer, and channel fees of 6% on TikTok Shop, 15% on Amazon FBA and 3.9% plus $0.40 on Shopify DTC are all stated in a readable rate table. Substitute your own refund rate and CPA and the waterfall tracks.

### Does the four percent discount need fixing before use?

It does, and it is one line. Until then, pass a factory cost already divided by 0.96 if you need the reported cost to match the real one, or read `landed COGS` knowing it is computed on the discounted figure.

## Sources

- Source: https://github.com/yixuanrobot/truemargin-mcp
- Web calculator: https://truemargin.aitruelabs.com
- Apify actor: https://apify.com/aitruelabs/truemargin-1688-profit-scout
- Submission: the mcp.so queue as #7589 on 2026-11-18
