---
title: "Aayat AI MCP - Pay-Per-Use Data and Tools for Agents"
description: "Aayat AI bundles 160 pay-per-use tools behind one MCP endpoint: token safety checks, cited web search, page-to-Markdown, package safety and research."
category: Data & Analytics
stars: n/a (no public repo)
added: 2026-09-30
source: "mcp.so feed (Aayat AI)"
relevance: ★★
tags: [pay-per-use, x402, usdc, web-search, data-enrichment, keyless, remote-mcp, analytics]
---

# Aayat AI MCP

**One endpoint, 160 payable tools, no account.** Aayat AI runs a remote MCP server whose tools are metered per call instead of sold as a seat: crypto token safety and rug checks, web search with cited answers, page-to-Markdown conversion, up-to-date library docs, package safety checks, company research and UK/EU open data. Twenty calls a day are free, after which you pay per call with USDC over x402 or from prepaid credits. Failed calls are never charged.

```
Server type: Remote (Streamable HTTP)
Auth: None for the free tier; x402 (USDC) or prepaid credits for paid calls
Endpoint: https://aayatai.com/mcp
Tools: 160
Pricing: 20 free calls/day, then pay per call
Category: Data & Analytics
Built by: aayatai.com
```

## What it exposes

The live server advertises its tool list on request, including `token-safety` (honeypot and sell-tax testing, holder concentration, liquidity and locks, mint and freeze powers, proxy contracts) at $0.02 per call. The catalogue is grouped around research and verification work: web search that returns cited answers, a page-to-Markdown fetcher for feeding content into an agent, current library documentation so an assistant does not code against a stale version, package safety checks before an install, company research, and open data from UK and EU sources.

## Connecting

```
claude mcp add aayat-ai --transport http https://aayatai.com/mcp
```

The endpoint needs no key for the free tier, which makes it usable in an assistant without a billing setup. Once the free calls are spent, calls are settled either through x402 (an HTTP 402 payment handshake in USDC on Base) or from a prepaid credit balance.

## Notes

The 160-tool count is the catalogue size, not the number the server advertises in a single `tools/list` response, so clients that enumerate tools per request see a subset. Per-call pricing means an agent loop can spend real money: the free tier of 20 calls per day is the guardrail, and failed calls are not billed.

## See Also

- [Data enrichment MCP servers](/hermes/mcp/servers/external/)
- [Search and research MCP servers](/hermes/mcp/servers/external/)
