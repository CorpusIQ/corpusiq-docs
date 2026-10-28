---
title: "Receipts Index MCP - Which Businesses AI Names"
description: "A read-only record of which US local businesses AI engines name for fixed buyer questions, with row ids and dates free and row content sold per row."
category: Marketing / AI Visibility
stars: n/a (MIT client, CC-BY-4.0 data, x402 paid rows)
added: 2026-10-27
source: "live GET on https://api.receiptsindex.com/v1/index at 04:05Z on 2026-10-28 returning row_count 2714, first_date_utc 2026-07-29 and last_date_utc 2026-10-27 with a 100-row page, the repository mrcrtr1979-droid/namebeam-visibility-index pushed 2026-10-28T03:57:58Z, and the chatmcp/mcpso submission #6268 filed 2026-10-28T02:44:26Z naming the free and paid routes"
relevance: ★★★
tags: [aeo, ai-visibility, local-business, citations, measurement, x402, read-only, npm, dataset]
last_updated: "2026-10-27"
---

# Receipts Index MCP

**Everyone selling AI visibility sells a dashboard. This sells rows: one engine, one date, one buyer question, and the businesses the engine named with the sources it showed.**

```
Server type:  Local (stdio), npm package
Package:      npx -y receipts-index-mcp (MIT)
Data host:    https://api.receiptsindex.com
Auth:         none. Read only. Never pays, never signs
Free routes:  /v1/index, /v1/sample, /v1/manifest, /.well-known/x402
Paid routes:  /v1/row/{row_id} at 0.27 USDC, /v1/day/{date} at 1.81 USDC
Payment:      x402, USDC on Base
Coverage:     US local businesses, 2,714 rows, 2026-07-29 to 2026-10-27
Built by:     Carter Enterprise LLC (Namebeam)
```

## Why This Matters for Operators

The question a local business actually has about AI is not "am I visible". It is "when someone asks an assistant to recommend a plumber in this city, which plumbers does it name, and what did it cite". That question has a factual answer, and it is a row.

Each row in this index is one check on one engine on one UTC date against a fixed local buyer question. The row carries the businesses the engine named and the sources it showed. A time series of those rows is the only honest way to answer whether an optimisation worked, because the answer moves between engines and between weeks, and a single screenshot of a single answer proves nothing.

The design decision worth recording is that the index itself is published as an append-only record and the publisher's own repository describes the corpus as customer zero with losses included. A vendor that publishes the weeks it lost is making a different claim from one that only screenshots the wins, and it is the claim an operator can act on.

## What Was Verified Live

A plain `GET` on `/v1/index` returned HTTP 200 with the shape the submission describes, no key of any kind:

- `row_count` **2714**, `first_row_id` 1, `last_row_id` 2714
- `first_date_utc` **2026-07-29**, `last_date_utc` **2026-10-27**
- a page block with `limit` 100, `returned` 100 and `next_start` 101
- rows carrying only `row_id` and `date_utc`

That last line is the whole commercial design. The free routes give ids and dates. What the engine actually named, and which sources it showed, is behind the paid routes. The client tool `receipts_sample` fetches one real row labelled as a sample, and `receipts_pricing` reads `/v1/manifest` and `/.well-known/x402` so an agent can state the price of a row before a human decides to buy one.

A `POST` to the same path returns HTTP 405 `{"error":"method not allowed"}`. Recorded because it is the kind of detail that makes a naive JSON-RPC probe look like a dead endpoint when the endpoint is healthy and simply not an MCP server. This one is a local stdio client that calls plain HTTP GETs.

## The Money Path

The paid routes are priced per unit and paid on-chain: 0.27 USDC for one row, 1.81 USDC for one UTC day as read from `/v1/manifest` on 2026-10-27. There is no subscription and no account. That means an agent can look at a manifest, report a price, and stop, which is the correct ordering, because the server itself is documented as read-only and unable to pay.

At those prices a coherent measurement is not expensive and it is not free either: ninety days of rows at one row per engine per day is a real budget, and an operator should decide the question and the cadence before an agent starts buying.

## Limits Worth Recording

- **Two thousand seven hundred and fourteen rows over ninety days.** This is a small, young corpus from one publisher, not a measurement panel. Treat a single week as a sample and a trend as provisional.
- **US local businesses only.** The buyer questions are local recommendation questions in the United States. Nothing here answers B2B software visibility.
- **The content is paid.** Row ids and dates at no cost, the businesses named and the sources behind USDC. Verification in this pass covered the free surface only, and no payment was made.
- **One publisher, one methodology.** The engine list, the question set and the check cadence are the publisher's choices, and a competitor using a different question set will produce different rows. Comparability across vendors is not established.
- **x402 requires a wallet.** It is a different operational shape from a credit card, and it puts a spend-capable key on the agent's host if the payment is automated.
- **The name is a warning.** The repository is titled a visibility index for Namebeam, the publisher's own product, and describes itself as customer zero. That is honest, and it also means the incentive to make a favourable question set exists.

## Wiring It Up

```json
{"mcpServers": {"receipts-index": {
  "command": "npx",
  "args": ["-y", "receipts-index-mcp"]
}}}
```

Read `/v1/index` first to see how many rows exist on the dates in question, then call the pricing tool, then decide.

## FAQ

### What exactly is in a row?

One check on one engine on one UTC date for one fixed local buyer question, carrying the businesses that engine named and the sources it showed. The free route returns only the row id and its date; the businesses and sources are behind the paid route.

### Can an agent buy rows on its own?

Architecturally yes, if it holds a funded wallet, because x402 settles per request with no account. The server is documented as read-only and never paying, so the containment has to come from the wallet the agent is given or from an approval step in front of it.

### How much does a measurement cost?

0.27 USDC per row and 1.81 USDC per UTC day as published on 2026-10-27. A quarter of daily rows across several engines is a real line item, so fix the question set before spending.

### Why is this catalogued rather than dismissed as an early dataset?

Because the unit is right. A visibility claim that cannot be reduced to engine, date, naming and sources is unverifiable, and this is the only surface in the sweep window that publishes its rows in that shape, including the rows where the publisher was not named.
