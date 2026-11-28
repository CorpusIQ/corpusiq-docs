---
title: "Verified x402 MCP - A Directory of Machine-Payable APIs"
description: "An index of x402 endpoints where an agent pays per call in USDC: free to search and probe, with the payment challenge captured live."
category: "Agent Payments"
stars: "n/a (vendor-hosted; the public client is at github.com/verifiedx402/verified-x402-mcp, star count not measured this pass)"
added: 2026-11-27
source: "queue filing chatmcp/mcpso#8250 read on 2026-11-27; keyless initialize 200 as verified-x402 0.1.0 on protocol 2025-06-18, a 3-tool tools/list, and six tools/call attempts at https://verifiedx402.com/mcp the same day, including an unpaid recommend that returned the full x402 v2 challenge"
relevance: "★★★"
tags: [x402, agent-payments, usdc, api-directory, discovery, base, solana, remote-mcp]
last_updated: "2026-11-27"
---

# Verified x402 MCP

**The x402 protocol turns a paywall into a handshake: a client asks for a resource, gets HTTP 402 with a price in the body, pays in stablecoin and retries. It works without an account, a key or a card, which is the point - an agent can buy a call the way it makes any other request. What it does not solve is discovery: there is no DNS for paid APIs. Verified x402 is an index of them, with a verification record on each entry and a scored shortlist you can buy for half a cent, and it is the first machine-payment directory in this catalog.**

```
Server type:  Remote (Streamable HTTP, stateless - no Mcp-Session-Id returned)
Endpoint:     https://verifiedx402.com/mcp
Registry:     com.verifiedx402/directory 1.0.2
Auth:         none for search and check_endpoint; recommend costs 0.005 USDC on Base or Solana
Discovery:    initialize 200 and a 3-tool tools/list, fully keyless
Tools:        3 (search, check_endpoint, recommend)
```

`initialize` answers **200** as `verified-x402` **0.1.0** with no session header, so each call is independent - which matters for a paid tool, because a stateless server cannot tie a payment to a session and has to bind it to the call itself.

## Three tools, split into free and paid on purpose

| Tool | What it does | Price |
|---|---|---|
| `search` | Catalog search over endpoint URL, description, category, network and price, with verification status per row | Free, rate-limited |
| `check_endpoint` | Takes one public URL, makes a live request, and compares the payment challenge it gets with the stored record | Free |
| `recommend` | Ranks recently verified endpoints for a task, with price, scores and the latest verification evidence | **0.005 USDC** on Base or Solana |

The division is the design worth copying: **discovery and verification are free, and only the ranking opinion costs money.** An agent can enumerate the market, check whether an endpoint is alive and priced as advertised, and pay nothing; it pays five thousandths of a dollar when it wants the server to do the choosing.

## What a verified row looks like

`search` returns more per row than the tool description implies. One entry, read keyless:

```json
{"id": "38707c61d800cd635d7b2a2a26739750",
 "url": "https://api.onesource.io/standard/v1/exit/fee-forecast",
 "category": "weather", "source": "bazaar", "scheme": "exact",
 "network": "eip155:8453", "httpMethod": "GET",
 "price": {"atomic": "20000", "usd": 0.02},
 "bazaar": {"calls30d": 83, "uniquePayers30d": 83, "lastCalledAt": "2026-11-13T03:54:49Z"},
 "verification": {"status": "verified", "lastCheckedAt": "2026-11-25T07:11:25Z",
                  "httpStatus": 402, "latencyMs": 105},
 "score": {"uptime": 100, "priceHonesty": 100, "responseValidity": 60,
           "latencyScore": 100, "integrityScore": 100, "composite": 92, "samples": 1}}
```

Four things in that row are unusual and each is checkable. **`verification.httpStatus: 402`** means the checker actually made the request and got the payment challenge rather than a 200 from a cached page - a "live" badge that records the status code is worth more than one that records a date. **`price.atomic`** is given beside a derived `usd`, so 20000 atomic units on Base USDC is 0.02 dollars and the arithmetic can be verified by hand rather than trusted. **`bazaar`** carries Coinbase's own 30-day call and payer counts, which is a third-party demand signal rather than a self-report. And **`integrityExplanation`** is prose written to be quoted, including the honest case: *"Bazaar reports 83 calls and 83 unique payers over 30 days (payer/call ratio 1.000). Unique payer count is high enough that a low payer/call ratio is treated as retries, not wash trading."*

## The paid tool answers with a real payment challenge

`recommend` without payment returns **HTTP 200** and a JSON-RPC result whose `structuredContent` is a complete x402 v2 challenge - this is the whole protocol in one response:

```json
{"x402Version": 2, "error": "Payment required to access this tool",
 "accepts": [
  {"scheme": "exact", "network": "eip155:8453", "amount": "5000",
   "asset": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
   "payTo": "0xd1bac498a13228df83708c6ab2ff47561c915cc3", "maxTimeoutSeconds": 60},
  {"scheme": "exact", "network": "solana:5eykt4UsFv8P8NJdTREpY1vzqKqZKvdp", "amount": "5000",
   "asset": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
   "payTo": "6Pt95picj6WLazjZqT6ofhPx5T7M6fD44HyuKqREmzQV", "maxTimeoutSeconds": 60,
   "extra": {"feePayer": "BENrLoUbndxoNMUS5JXApGMtNykLjFXXixMtpDwDR9SP",
             "transactionVersions": [0, 1]}}]}
```

**Two rails, one price, and the buyer chooses.** 5000 atomic units of USDC is a half cent either way; Base is an EVM transfer and Solana is a signed transaction with the server acting as fee payer. Both carry a 60-second window, which forces a client to prepare the payment before it asks. The `amount` is a string, not a number, which is the correct shape for money and worth noting because a client that parses it as a float will round.

An agent that cannot sign for either rail - most of them today - reads this and stops, correctly, without spending anything and without learning a false capability.

## Verification refuses to read an outage as a price

`check_endpoint` on this server's own address, the most useful available test because the answer is known:

```json
{"url": "https://verifiedx402.com/mcp", "stored": false,
 "probe": {"live": false, "httpStatus": 522, "latencyMs": 32, "got402": false, "schemaValid": false,
           "error": "HTTP 522 is a temporary server error, not a payment challenge."}}
```

That is the right behaviour and a rare one: **a checker that treated any non-200 as a paywall would have scored a Cloudflare timeout as a working paid endpoint.** It also distinguishes `stored: false` - this URL is not in the catalog, so the probe stands alone - from a comparison against a record that does not exist.

## Five defects recorded

**1. The keyword match lands on the category, not on meaning.** `q: "weather"` returned an on-chain reserve's *exit fee forecast* as the first result, whose `category` field reads `weather`. The top hit for a plain weather query is not a weather API. Either the row is mis-categorised at ingest or `q` is matching the category label instead of the description, and from outside the two are indistinguishable - a caller should treat `q` as a filter on labels and read the `description` before paying.

**2. Parameterised route templates are published as callable endpoints.** With `status: "no_402"` the catalog returns rows such as `https://aisfleet.com/api/x402/v1/weather/stations/:network/:code/day` (**400**) and `https://quno-production.up.railway.app/v1/weather/point/:latlon` (**404**) - colon placeholders indexed as if they were addresses. An agent that takes a listing literally gets a client error and, on a pay-per-call rail, may pay before it does.

**3. USD price is not universal, so price filtering is partial.** The Base rows resolve `price.usd` (20000 atomic → 0.02 dollars); a Solana row returned `{"atomic": "5000", "usd": null}`. Because `max_price` filters on the derived field, a caller comparing rails or filtering by budget silently drops Solana listings rather than comparing them.

**4. The headline count cannot be checked from the API.** The filing claims **77,827 verified x402 APIs** as of 2026-11-27. `search` returns a `results` array and no total, so the figure is unverifiable through the tool surface - recorded as a vendor claim, not as measured.

**5. The default result set mixes dead endpoints into live ones.** Every row carries `verification.status` (`verified`, `stale`, `mismatch`, `no_402`, `down`, `unchecked`), and `no_402` rows - endpoints that answered but did not ask for payment - appear unless `verified=1` is set. The filter works when used; the default does not apply it.

## Why it belongs in this catalog

CorpusIQ's job is trusted answers, and the trust question changes shape when the assistant can spend. An x402 directory is the first surface here where **the price of a call is part of the answer**, and where a verification record tells you whether the price is real. The operator version of that is simple: before you let an agent buy data, you want to know which endpoints are alive, what they charge and who else is paying them. `calls30d` and `uniquePayers30d` answer the last one, and a `composite` score of 92 with `samples: 1` tells you how thin the evidence is.

## Frequently asked questions

### Do I need a wallet to use it?

No. `search` and `check_endpoint` are free and keyless, and they are the discovery half. A wallet is needed only to buy the ranking opinion, and to call any endpoint the catalog lists.

### Is the catalog the same as Coinbase's x402 bazaar?

The rows carry `source: "bazaar"` and a `bazaar` block with call counts, so the underlying catalog is Coinbase's. What this server adds is the verification pass, the scoring, and a rank-for-a-fee tool - which is the part to test rather than assume, since the ranking is the paid product.

### Can it tell me if an endpoint is overpriced?

It can show you the price and the demand. 83 calls and 83 unique payers over 30 days for a two-cent endpoint is a thin but genuine market, and comparing that against a half-cent endpoint with no payer count is a judgment the catalog gives you the ingredients for and does not make.

## See also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
