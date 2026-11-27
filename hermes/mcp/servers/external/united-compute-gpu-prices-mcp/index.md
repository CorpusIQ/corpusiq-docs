---
title: "GPU Cloud Prices MCP - What an H100 Hour Costs Right Now"
description: "Keyless live GPU pricing across 59 clouds, with a spot and on-demand split, per-offer timestamps, and a 4.4x spread on the same H100."
category: "Infrastructure"
stars: "n/a (vendor-hosted; open data mirror on GitHub, CC BY 4.0)"
added: 2026-11-26
source: "chatmcp submission queue #8191 filed 2026-11-27T18:51:35Z; official registry `ai.unitedcompute/gpu-prices` with remote https://unitedcompute.ai/mcp; driven on 2026-11-27 at the 21:00 MST tick with a keyless initialize, a 4-tool tools/list and eight tools/call requests across all four tools, including a negative GPU query and an AMD vendor filter; coverage read from the vendor's /llms.txt at 04:02Z"
relevance: "★★"
tags: [infrastructure, gpu, cloud-pricing, cost-management, capacity, ai-ops, keyless, read-only, open-data, streamable-http]
last_updated: "2026-11-26"
---

# GPU Cloud Prices MCP

**"What will a thousand GPU hours cost us" has no single answer, and an assistant that answers it from memory is quoting a price list that expired a year ago.** This server answers it from a live index: every 15 minutes it checks what one on-demand GPU costs per hour across 59 clouds and whether that GPU can actually be rented right now, and it answers with three different timestamps so a reader can tell a fresh price from a stale one. It needs no key, runs no writes, and returns the spread rather than an average, which is the part that decides a budget.

```
Server type:  Remote (Streamable HTTP)
Endpoint:     https://unitedcompute.ai/mcp
Auth:         none, no account, no key
Protocol:     2025-06-18, serverInfo united-compute 1.0.1
Session:      Mcp-Session-Id returned (uc1.eyJ...), stateless calls also accepted
Tools:        4, all read-only: search_gpu_offers, list_gpus, get_gpu, list_providers
Coverage:     1,044 offers, 76 GPU models, 59 clouds at 2026-11-27T04:02:34Z
Licence:      the underlying table is published as open data, CC BY 4.0
```

`initialize` answers **200** as `united-compute`, title *"United Compute GPU prices"*, version **1.0.1**, with `tools.listChanged: false` and no prompts or resources, so the whole surface is four read tools. Every payload carries `source`, `updated_at`, `stale` and `unit` before its rows, and each offer inside carries its own `checked_at`: a client can therefore print *this price was confirmed 18 seconds ago* rather than *this is the price*.

## The four tools

| Tool | Arguments | What comes back |
| --- | --- | --- |
| `search_gpu_offers` | `gpu`, `provider`, `cloud_type`, `pricing`, `region`, `min_vram`, `max_price` | matching single-GPU offers, cheapest first, each with price, stock level, regions and a rent link |
| `list_gpus` | `gpu`, `vendor`, `min_vram`, `in_stock_only` | one row per model with the cheapest price now, datacenter and community splits, and how many clouds have stock |
| `get_gpu` | `gpu`, an id or a name | specs plus every offer for that model, in stock and not available, separated |
| `list_providers` | none | every tracked cloud with its URL, marketplace and reseller flags, and offer counts |

`list_gpus` returned **71** models with stock against a vendor count of **76** tracked, which is the honest difference between *indexed* and *rentable this minute*. Filtering `vendor: "AMD"` narrowed it to **2**: `mi350x` from **$4.00** on CloudRift and `mi355x` from **$6.20** on Daytona. A nonsense query, `gpu: "nonsense-xyz"`, returned `count: 0` and an empty array rather than an error, which is the right shape for a filter that matched nothing.

## The same H100, five prices

This is the whole reason the surface exists. One call, `search_gpu_offers` with `gpu: "H100"` and `max_price: 2.50`, returned six rentable offers:

| Cloud | Type | Model | Price per GPU-hour | Stock | Regions |
| --- | --- | --- | --- | --- | --- |
| Clore.ai | community | H100 SXM | **$0.55** | low | Russia (RU) |
| Vast.ai | community | H100 SXM | **$1.7356** | medium | Germany, United States |
| Lium | community | H100 PCIe | **$2.20** | low | not stated |
| GPU.ai | datacenter, reseller | H100 PCIe | **$2.23** | high | ca-central, us-central |
| Fluence | datacenter | H100 SXM | **$2.4236** | high | eight countries |
| Hyperstack | datacenter | H100 PCIe | **$2.50** | medium | Canada |

**The cheapest rentable H100 in the index is $0.55 and the cheapest datacenter H100 is $2.4236, a 4.4x spread on a unit that every vendor calls an H100 hour.** The first price carries a jurisdiction a US operator cannot necessarily use, the second is a marketplace host with a *low* stock flag, and the third and fourth are PCIe cards rather than SXM. A client that quotes one number without its cloud, its type and its stock level has quoted nothing usable.

`get_gpu` on `h100-sxm-80gb` adds the split the list tool only summarises: **20 offers in stock of 33 total, across 18 providers**, cheapest `$0.55` community, `$2.4236` datacenter, `$0.4271` spot. The spot figure is worth the call on its own, because the same Clore card is `$0.4271` on spot and `$0.5500` on demand, and only the detailed call shows both.

## A cheaper question than an H100

`search_gpu_offers` with `min_vram: 48` and `max_price: 1.00` returned **20** rentable offers, and the cheapest three were **L40** cards: Lium at **$0.33**, Fluence at **$0.3644**, and GPU.ai at **$0.37**. For inference work that fits 48 GB, the answer to *what does a GPU hour cost* is a third of the H100 headline, and this is the tool shape that finds it: a VRAM floor and a price ceiling, not a model name.

## Where the answer is "sold out", and how it says so

`get_gpu` on `mi300x` is the case that separates an honest index from a price list:

```json
{"gpu": {"id": "mi300x-192gb", "cheapest_price_per_hour": null,
         "offers_in_stock": 0, "offers_total": 2, "providers_in_stock": 0},
 "offers_in_stock": [],
 "offers_not_available": [{"cloud": "OpenRelay", "price_per_hour": null,
                           "list_price_per_hour": 1, "in_stock": false}]}
```

**Null is not zero and `list_price_per_hour` is not a price you can pay.** The AMD MI300X is absent from every rentable list, the advertised dollar figure is preserved beside a null rentable price, and the flag says why. An assistant asked to compare MI300X against H100 gets *sold out, listed at $1.00* rather than a silent zero or a hallucinated number.

## Four defects, measured

1. **A region filter matches an offer, not a price.** `search_gpu_offers` with `region: "Europe"` and `gpu: "B200"` returned Lium at **$5.50** with regions `["France (FR)", "Israel (IL)", "United States (US)"]`. The offer is genuinely available in France, so the match is correct, but the row carries one price for three jurisdictions and no way to tell whether that price holds in the European one. Region is a list on the offer and a scalar in the result.
2. **`reseller` appears on some rows and not others.** GPU.ai offers carry `"reseller": true`; Clore, Vast, Lium, Fluence and Hyperstack offers carry no `reseller` key at all, while `list_providers` reports the flag for every cloud. A client filtering on the field treats *absent* and *false* differently depending on its language, and one of those readings is wrong for every non-GPU.ai row.
3. **A model id and its VRAM disagree.** `mi350x-288gb` reports `vram_gb: 294` while `mi355x-288gb` reports `288`. Either the id is stale or the VRAM is, and both are published in the same payload.
4. **The tracked-model count and the rentable count are different numbers with no reconciliation in the tool.** The vendor's `llms.txt` states **76** models and the tool returns **71** with stock, both accurate under their own definitions (the tool's `in_stock_only` defaults to true), but a client comparing the two without reading the default will report a disappearance that did not happen.

## What it costs

Nothing. The surface is free and keyless, the vendor asks only that the data be credited when it is shown, and the same table is published as a daily export plus full change history on GitHub under **CC BY 4.0**. The commercial edges are an Apify Actor and a RapidAPI listing for teams that need a paid provider, not a paywall on this endpoint. Not covered at all, and stated as such: multi-GPU-only machines, reserved and committed contracts, and serverless. A budget built from these numbers prices *one rentable GPU, on demand, today*.

## Add it to Hermes

```bash
hermes mcp add united-compute --url https://unitedcompute.ai/mcp
```

No header, no key, no environment variable. Quote `updated_at` and the per-offer `checked_at` with any price, keep `cloud_type` visible when comparing, and treat `null` as sold out rather than free.

## What does a GPU hour cost, and why is one number the wrong answer?

Because the distribution is wide and the cheap end carries conditions. On 2026-11-27 the index held an H100 SXM at **$0.55** on a community marketplace in Russia, a second at **$1.7356** on a marketplace with hosts in Germany and the US, and a datacenter H100 at **$2.4236** from a provider with capacity in eight countries, all confirmed within the same minute. The right output is the trio with its conditions attached: jurisdiction, cloud type, model variant and stock level. A single figure is a guess dressed as a quote.

## Why this one is in the catalogue

The operator question is a cost question, **what does a GPU hour cost us this month**, and it is the same class of question as *what does this supplier charge* or *what did this campaign spend*: answerable only from a live source with a date on it. It is keyless, read-only, four tools, and the payloads carry the freshness evidence that makes the number quotable. The cost discipline it demonstrates is the lesson to copy: every row states when it was checked, and the model separates an advertised price from a rentable one.

## See also

- [Octio MCP](/hermes/mcp/servers/external/octio-mcp/) for a pay-per-call market whose prices are public before payment, the same transparency pattern on the selling side.
- [External MCP Server Catalog](/hermes/mcp/servers/external/) for the full index.
