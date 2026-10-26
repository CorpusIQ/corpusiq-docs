---
title: "GPU Finder MCP - Live Cloud GPU Prices and Stock"
description: "Live GPU rental prices, stock and 12-month price history across 33 cloud providers and 96 models, with a cheapest-in-stock answer for each node size."
category: Infrastructure / Procurement
stars: n/a (free key, 60 operations a month)
added: 2026-10-26
source: "live MCP probe on gpufinder.dev/mcp (keyless initialize 200 as gpufinder a6, keyless tools/list 200 with 8 tools, tools/call 401 invalid_credential naming the free key path) + vendor site gpufinder.dev pricing page + mcpservers.org card"
relevance: ★★★
tags: [gpu-pricing, cloud-cost, procurement, ai-infrastructure, price-history, availability, finops]
last_updated: "2026-10-26"
---

# GPU Finder MCP

**A GPU hour is a commodity with a twelve times price spread, and almost nobody renting one knows what the cheapest in-stock offer was that day.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://gpufinder.dev/mcp
Transport:   JSON-RPC 2.0 over HTTP
Auth:        free API key as a Bearer token (60 operations a month), tools/list readable without one
Tools:       8, read from a live tools/list
Built by:    GPU Finder (gpufinder.dev)
Registry:    not checked in the sweep window
```

## Why This Matters for Operators

Anyone running inference, fine-tuning or rendering is buying GPU hours on a market that moves hourly. The vendor's own headline is the argument: eight H100s cost $15.46 an hour at one provider and $186.61 an hour at another, and the difference is not quality, it is which marketplace the capacity is listed on that hour. Capacity also disappears: a price list without stock is a brochure.

This is the procurement half of an AI budget that most teams keep in a spreadsheet named after the person who left.

## What It Actually Does

`initialize` returned HTTP 200 as `gpufinder` version `a6` on protocol 2025-06-18 with tools and `listChanged: false`. `tools/list` then returned **8 tools** keyless. A `tools/call` returned HTTP 401 `invalid_credential` with a message that states the commercial terms in the error itself: an API key is required, keys are free and include 60 operations a month, created at the developers page, and sent as a Bearer header.

| Tool | What it answers |
|---|---|
| `list_gpus` | Every tracked GPU model with VRAM, memory type, bandwidth, interconnect, provider and instance counts, and min/max hourly price |
| `list_providers` | Each cloud provider with GPU and instance counts, price range, egress cost per GB and free egress allowance, and last update time |
| `get_prices` | Every offer for one GPU model and node size: provider, instance type, region, GPU count, on-demand and spot price per whole node hour |
| `get_availability` | Day-by-day stock for one model over the last seven days, instances observed available against total |
| `get_price_history` | Month-by-month on-demand and spot price per provider for up to twelve UTC months |
| `get_market_snapshot` | The cheapest listed offer and the cheapest offer actually observed in stock, for one model and node size |
| `get_data_status` | Freshness: when collection last completed, and each provider's last success, last run, consecutive failures and last error |
| `get_usage` | The key's plan allowance, units used and remaining, and UTC reset times, without spending allowance |

The published site numbers at the probe: **33 providers compared, 24 availability APIs, 96 GPU models, data collected 43 minutes before the read**, with a worked example of 8x H100 running from $15.46/hr (Vast) to $186.61/hr (Azure), and a stale marker on one provider showing 30 hours since its last successful refresh and another showing the instance out of stock. That stale flag is the detail that makes the surface trustworthy: it reports its own decay per provider instead of blending it away.

## Limitations Recorded

- The free key allows 60 operations a month, which is enough for periodic checks and not enough to poll hourly; polling is a paid plan or an alert.
- Tool execution was not driven in this sweep because no key was created, so argument names come from the published schemas rather than from an executed call.
- Price coverage depends on which providers expose a public listing; on-demand and spot are separate fields and spot is not available everywhere.
- Storage, network egress beyond the stated per-GB figure, and commitments or reserved contracts are not modelled.
- Alerts are an email product on the vendor side, not an MCP tool.

## FAQ

### Does this rent GPUs?
No. It reads prices and stock and links out to the provider. Nothing is provisioned from the catalog.

### What does the market snapshot add over a price list?
Two numbers instead of one: the cheapest offer as listed, and the cheapest offer actually seen in stock over the window. A cheap listing with no availability is not a price you can pay.

### Is this the same as a cloud cost optimizer?
No. Cost optimizers read your existing bill. This reads the market before you commit, which is a different decision and happens earlier.

## See Also

- [Cloud cost and FinOps entries in the external catalog](/hermes/mcp/servers/external/)
- [CorpusIQ infrastructure connectors](/hermes/mcp/)
