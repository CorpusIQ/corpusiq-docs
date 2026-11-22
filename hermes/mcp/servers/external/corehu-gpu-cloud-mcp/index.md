---
title: "CoreHu GPU Cloud MCP - Priced GPU Hours, Gated"
description: "Six keyless tools pricing 1,999 free GPUs per hour and per country, plus a prepare-then-confirm rental flow where the agent can never spend without a yes."
category: "Infrastructure / Procurement"
stars: n/a (vendor-hosted)
added: 2026-11-22
source: "mcp.so submission queue #7803 on 2026-11-22T09:18:13Z; the official MCP registry record com.corehu/gpu-cloud, five versions from 1.0.0 at 2026-11-12T16:49:23Z to 1.1.3 at 2026-11-22T09:20:36Z; keyless initialize, tools/list, resources/read on two guide documents and seven tools/call requests on 2026-11-22"
relevance: ★★★★
tags: [gpu-pricing, cloud-cost, procurement, ai-infrastructure, finops, approval-gate, remote-mcp, keyless]
last_updated: "2026-11-22"
---

# CoreHu GPU Cloud MCP

**A GPU hour is a purchase, and the agent that recommends one usually cannot show the price, the stock or the difference between two providers before someone clicks.** CoreHu answers all three from a keyless endpoint, and then puts a five-minute confirmation in front of anything that spends money.

```
Server type: Remote (Streamable HTTP, two surfaces)
Endpoint:    https://corehu.com/api/mcp            public, read-only, no auth
             https://corehu.com/api/mcp/account    OAuth 2.1, rentals and machines
Tools:       6 public, 15 on the account surface
Handshake:   corehu-catalog 1.1.1 on protocol 2025-06-18
Registry:    com.corehu/gpu-cloud, latest 1.1.3 published 2026-11-22T09:20:36Z
Resources:   corehu://guides/renting, corehu://guides/billing, corehu://recipes
Prompts:     rent_gpu, compare_gpu_prices
```

## Why This Matters for Operators

AI infrastructure is now a recurring line in a small business budget, and the buying decision is made in the same chat window where the model was chosen. The public surface is enough to make it honestly: starting prices per model, free machines per country, a VRAM estimate for a stated job, and an hourly-to-monthly cost figure that reproduces by hand.

The second half is the reason this is a guide rather than a note. The account surface rents machines, and the vendor has built the refusal in: `prepare_rental` returns a price, a hold and a **confirmationId valid for five minutes**, and nothing is rented or charged until `confirm_rental` is called with it. The written instruction to the client is explicit - *"Show that summary to the user and wait for an explicit yes in the chat. Never confirm on your own."*

## Prices, Read Live

`get_gpu_prices` returned the full model list cheapest first on 2026-11-22, 8,628 characters of it. The floor and the popular card:

```text
Quadro P2000   0.07 USD/h
RTX 3060       0.13
RTX 2060       0.14
RTX 2070S      0.15
GTX 1080 Ti    0.16
RTX 3070       0.16
RTX 4060       0.20
RTX 3080       0.27
```

`get_gpu_availability` is the half a price list cannot give you: **1,999 free machines** at the time of the read, broken down by model and country. Three rows from the same response show how much the same silicon moves:

```text
A100        US   20 machines free   from 2.99 USD/h
A100 SXM4   US   29 machines free   from 0.88 USD/h
A100 PCIE   JP    9 machines free   from 0.77 USD/h
```

That is a **3.9x** spread for A100-class capacity in one catalog on one minute, and the A100 SXM4 row is cheaper per hour at a higher interconnect tier than the PCIE row in the United States. An agent that quotes one number without the country is quoting the wrong number.

`search_offers` on `RTX 4090` returned **165** offers, cheapest **0.72 USD/h** in Romania at a reliability of **0.997888**, then 0.76 in Poland and 0.79 in Vietnam - each with its own `offerId` and `rentUrl`.

## The Cost Figure Reproduces

`estimate_cost` on the RTX 4090 for **720 hours** returned **518.40 USD**, which is 0.72 x 720 exactly, from the cheapest free machine at that minute. The note shipped with it is the operator's caveat, not boilerplate: *"Estimate only … it is not a reservation and prices can change … a stopped machine still bills for its disk."*

`recommend_gpu` returns its arithmetic in a `basis` string, and it checks:

```text
workload llm_inference, modelSizeB 70, precision int4  -> neededVramGb 44
  basis: 70B parameters × 0.5 bytes (int4) + 20% and 2 GB for the KV cache
  (35 x 1.2 + 2 = 44.0, exact)

workload llm_inference, modelSizeB 8, precision fp16   -> neededVramGb 24
  basis: 8B parameters × 2 bytes (fp16) + 20% and 2 GB for the KV cache
  (16 x 1.2 + 2 = 21.2, rounded up to the next 24 GB card)
```

The first reproduces to the decimal; the second rounds to a card size, which is why an 8B fp16 job is quoted a 24 GB GPU rather than a 22 GB one. The estimate came back with a ready recipe too - the Ollama template, `ollama pull <MODEL>` after start, and the port-forward line for the API on 11434.

## The Refusals Are the Schema

Two calls were made wrong on purpose, and both were refused with the rule named rather than answered with a guess:

```text
recommend_gpu {workload: "serve a 70B LLM in int4"}
  -> -32602 Invalid option: expected one of
     "llm_inference" | "llm_finetune" | "training" | "image_generation" | "notebook"

estimate_cost {gpuModel: "RTX 4090"}          (hours omitted)
  -> -32602 Invalid input: expected string, received undefined at gpuModel
```

The first error lists the five accepted workloads; the second names the exact missing field. Both are the shape an agent can recover from without a human, which is the difference between a strict schema and a hostile one.

## The Rental Gate, Documented

The account surface was not driven, because renting a machine requires the user's own consent screen and this pass does not spend. What it does is documented in `corehu://guides/renting`, read from the server:

1. `prepare_rental` returns the exact hourly price, the amount held from the balance and a **confirmationId valid for five minutes**. Nothing is rented or charged.
2. Show that summary to the user and wait for an explicit yes.
3. `confirm_rental` returns a `reservationId`; `get_rental_status` is polled about once a minute, with startup usually **2 to 10 minutes**.
4. `stop_rental` when the work is done; a stopped machine keeps its disk and bills for it, `start_rental` resumes it.

The permission model behind it is finer than a single token scope. `rental:create` and `rental:control` are granted on the consent screen, and each machine then carries its own set - `read`, `control`, `delete`, `commands` - where delete is off unless the user ticked it for that machine. Refusals are named: `AGENT_MACHINE_PERMISSION_MISSING` changes nothing and returns a `userActionUrl`, `AGENT_LIMIT_EXCEEDED` means a user-set ceiling was hit (hourly price, machines at once, rentals per day). Billing follows the same discipline: per second from a prepaid balance, a `firstHoldUsd` hold released if a rental fails to start, and funds addable **only by the user in the browser** - the guide's last line is *"The assistant can never add funds or make payments."*

## Where It Sits in This Catalogue

[GPU Finder MCP](/hermes/mcp/servers/external/gpufinder-mcp/) already owns the price-intelligence half: **33** providers, **96** models, twelve months of price history, and a free key with **60** operations a month. CoreHu is the execution half of the same job - fewer models, no history, but no key, and a rental path behind an approval gate.

Read them as two different questions. GPU Finder answers *what has this card cost across the market*. CoreHu answers *what can I have in the next ten minutes, at what price, in which country, and what will the month cost* - and then refuses to spend until someone says yes.

## Limits, Stated

- **One vendor's capacity.** The 1,999 free machines, the prices and the reliability figures are CoreHu's own catalog, not a market index. Cross-provider comparison lives in GPU Finder.
- **No price history.** Every figure is a point in time, and the vendor says so in each response.
- **The public surface cannot rent.** Without the account connector, an assistant can search, price and estimate, then hand over a `rentUrl`.
- **Version drift.** The registry's latest record is **1.1.3** published 2026-11-22T09:20:36Z; the public catalog handshake still reports **1.1.1**. The guide records the surface it measured.
- **Reliability is a vendor metric.** `0.997888` on the cheapest RTX 4090 is CoreHu's own figure, not an independent uptime measurement.

## See Also

- [GPU Finder MCP - Live Cloud GPU Prices and Stock](/hermes/mcp/servers/external/gpufinder-mcp/)
- [MCP Server Discovery - November 22, 2026 (Night)](/hermes/mcp/sweeps/sweep-november22-2026-night)
