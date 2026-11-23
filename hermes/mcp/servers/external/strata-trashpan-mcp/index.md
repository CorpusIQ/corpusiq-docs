---
title: "STRATA MCP - Sealed Data Streams Priced Per Call"
description: "One hundred and eighteen tools over sixteen data streams, with a free inventory probe and a paid floor at 0.006 USDC per call."
category: "Data & Analytics"
stars: n/a (vendor-hosted)
added: 2026-11-23
source: "mcp.so feed card stamped 2026-11-23 06:01 (UTC) for slug strata-trashpan-b2a-clean-data-mcp-server; keyless initialize, tools/list, one free probe_inventory and two refused paid calls on 2026-11-23"
relevance: ★★★★
tags: [data-marketplace, x402, provenance, kyb, japan-public-data, tenders, remote-mcp]
last_updated: "2026-11-23"
---

# STRATA MCP

**Remote MCP server (Streamable HTTP, two tiers)** - a data marketplace operated by andQ Inc. (Japan, corporate number 6010001269339) presenting **118 tools** across sixteen streams: Japanese company registry deltas, real-estate auctions, tenders, patents, EDINET financial filings, domain and email stacks, ATS jobs, Google Trends and more. The first floor is free and answers inventory questions. The second floor costs **0.006 USDC** a call over x402, or an Apify pay-per-event, or an API key.

```
Server type: Remote (Streamable HTTP), free probe tier + paid data tier
Endpoint:    https://strata.andque.com/mcp
Server:      trashpan-recycle-mcp 2.0.0, protocol 2024-11-05
Tools:       118, of which probe_inventory is free and documented as the entry point
Paid floor:  0.006 USDC per call on Base mainnet, or Apify pay-per-event, or X-MCP-API-Key
Author:      andQ Inc., Japan, corporate number 6010001269339
```

## Why This Matters for Operators

Buying a data feed usually means a sales call, a contract and a monthly minimum before anyone can see whether the data is any good. This server inverts that: the free call tells you what the stream holds, when it was last checked, how many times it has changed and what the current record hash is, and the paid call is a micropayment an agent can make on its own. That is a different purchasing model from every other data source in this catalogue, and it is the reason the entry exists.

The second reason is provenance. The probe returns a sealed record with a Merkle root, the date of the seal batch, and a claim that the data is first-party or openly licensed rather than scraped. For a compliance or KYB workflow, a source that publishes its own seal and licence status is materially easier to defend than one that does not.

## Measured Behaviour

Three calls were driven on 2026-11-23.

### The free floor: an inventory probe with a sealed record

`probe_inventory()` answered keyless with:

```json
{"ok":true,"handshake":"b2a_mcp_free_probe_v1","tier":"free_1st_floor",
 "streamId":"domain-lookup","targetKey":"domain:cloudflare.com","recordExists":true,
 "currentHash":"0623a84a123e5a9c67dcf5000dce4e7fbfb75c758b86131466094f04a55f2127",
 "firstSeenAt":"2026-11-07T04:53:31.529Z","lastCheckedAt":"2026-11-23T05:02:42.984Z",
 "lastChangedAt":"2026-11-21T12:26:33.924Z","checkCount":6,"changeCount":3,
 "freshWithin24h":true,"cacheTtlSeconds":86400,
 "source_license":"commercial_resell_ok","sealStatus":"tapp_rekor_sealed",
 "tappSeal":{"batchDateJst":"2026-11-23","merkleRootSha256":"eaea5afab0b1c0de7937f2b41cbc1071882619948973617ddebae161eb47f270"}}
```

Read as a data buyer: the stream existed on **2026-11-07**, has been checked **6** times, has changed **3** times, last changed on **2026-11-21**, was fresh within 24 hours of the call, and the record is sealed into a Rekor batch dated **2026-11-23**. That is a due-diligence answer before any money moves, which is what most feeds charge for.

The three badges it carries are specific and checkable claims: first-party or open government licensing with resale allowed, a zero-PII observation architecture, and a Sigstore Rekor timestamp.

### The paid floor: a refusal that explains itself

`domain_lookup(domain="corpusiq.io")` and `jp_company_kyb_registry_delta(query="トヨタ")` both answered with `isError: true` and the same structured refusal:

```json
{"ok":false,"error":"MCP_2ND_FLOOR_PAYMENT_OR_KEY_REQUIRED",
 "requestedTool":"domain_lookup","streamId":"domain-lookup",
 "messageEn":"You can check inventory for free first using probe_inventory ... To fetch full structured data immediately ... use: (1) x402 Base Mainnet USDC Paywall ... | $0.006 USDC, (2) Apify Store Pay-Per-Event ..., or (3) provide a valid X-MCP-API-Key header"}
```

Three payment paths, a price, and the free alternative in the same message. The refusal names the stream and the tool, so a client can route around it or complete the purchase deliberately.

### The breadth, by stream name

The 118 tools are not variants of one job. A sample of the names shows the shape: `jp_court_real_estate_auctions`, `jp_company_kyb_registry_delta`, `jp_giteki_tenders_intel`, `jp_edinet_financial_macro_feed`, `jp_patent_saas_b2a_delta`, `jp_real_economy_geospatial_feed`, `jp_healthcare_hospitals_directory`, `cisa_kev_threat_ai_status`, `ats_jobs`, `google_trends`, `domain_lookup`. Japanese public and commercial data dominates, with a few non-Japanese streams attached.

## Defects and Limits

- **Only the probe is free.** The data itself is behind a paywall by design, so this entry cannot be judged on returned data the way a keyless read can. What was verified here is the inventory floor, the price, the payment paths and the 118-tool surface.
- **The protocol version is old.** `initialize` reports **2024-11-05** rather than 2025-06-18. It works with a current client, but the server is negotiating an older revision, which usually means the tool schemas follow the older conventions.
- **A refusal arrives with an HTTP error status.** Both paid attempts returned status 401 alongside a valid JSON-RPC result carrying `isError: true`. Clients that treat any 401 as an authentication failure will not read the payment menu, which is the useful part of the answer.
- **The name does not describe the product.** The listing slug is about clean data and the server identity is `trashpan-recycle-mcp`, while the tool surface is a Japanese business-data marketplace. Judge it by the tool list.

### Does it need a key?

For the probe, no: `initialize`, `tools/list` and `probe_inventory` answered keyless on 2026-11-23. For data, yes: USDC over x402, an Apify event, or an API key issued by the operator.

### Is the paid data worth 0.006 USDC a call?

That is a fraction of a cent, roughly one two-hundredth of a dollar, and the free probe is what lets you decide: check the stream's change count and last-checked date first, then buy one call to see the record shape. The model rewards a buyer who probes before paying.

### What does the seal actually prove?

It proves the record was committed into a dated Merkle batch whose root is published, so a later change to the same record can be shown to differ from this one. It does not prove the underlying data is accurate, and the licence badge is a claim about source terms rather than a legal opinion.

## See Also

- [Business and public-records data sources in the external catalogue](/hermes/mcp/servers/external/)
- [Sweep report for November 23, 2026 (night)](/hermes/mcp/sweeps/sweep-november23-2026-night)
