---
title: "MCP Server Discovery - November 19, 2026 (Midday Supplement)"
description: "Both directory surfaces flat to the entry in the hour, two feed cards filed inside it, and one supplier that issues a signed, expiring quote to an anonymous agent."
category: "MCP Ecosystem"
last_updated: "2026-11-19"
---

# MCP Server Discovery - November 19, 2026 (Midday Supplement)

Fired on the **11:00 MST** tick, one hour after the midday sweep closed at **17:12Z**. The canonical came back flat on every reading, the feed produced **two** cards inside the hour where it had produced three in the five and a half hours before it, and one of the two is a supplier-side quoting endpoint that answers an anonymous agent with a signed document.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          66,677   against 66,677 at the 17:12Z midday capture
  servers/1  ..... 7,588    held    servers/7  ..... 9,351    held
  servers/2  ..... 5,949    held    servers/8  ..... 6,590    held
  servers/3  ..... 6,518    held    servers/9  ..... 4,022    held
  servers/4  ..... 6,746    held    servers/10 ..... 2,608    held
  servers/5  ..... 6,954    held    servers/11 ..... 2,637    held
  servers/6  ..... 6,756    held    servers/12 ..... 958      held
priority-servers.xml          299 raw   held
remote-mcp-servers.xml         15 raw   held
lastmod rows at or after 17:12Z   0
mcp.so /feed                  200 at 156,532 bytes, 33 server cards,
                              30 stamps, 4 other-family anchors, 2 above cutoff
submission queue              #7667 only (17:55Z); #7649-#7666 were the midday window
```

Two readings agree and one of them is the stronger of the pair: the raw count is identical map for map, not merely identical in total, so the nine-entry rise the midday pass measured inside `servers/4` and `servers/12` did not continue. The `lastmod` scan returns **zero** rows above the cutoff, which is the same answer the midnight and midday passes recorded for their windows. A flat surface that three separate fields agree on is reported rather than narrated.

## The two feed cards

`tagli-branded-merchandise-promotional-products` at **17:58Z** and `universal-quant-tournament-mcp-0b557a` at **17:35Z**, both after the 17:12Z capture, both before this pass closed the read. The read carries **33** server cards and **30** stamps, paired anchor-to-nearest-following-stamp as the format now requires, plus four other-family anchors (`/agents/alyven-music`, `/agents/saascity-io`, `/agents/vindaris`, `/clients/rapidoddsapi`) that break any single-family pairing. Both slugs resolved through the official registry on the first query.

## What shipped

### [TAGLI MCP - A Signed, Expiring Merch Quote for an Agent](/hermes/mcp/servers/external/tagli-mcp/)

The vendor's own Streamable HTTP endpoint at `https://tagli.co.il/wp-json/tagli/v1/mcp`, *TAGLI B2B Autonomous Commerce MCP Server* **2.0.0** on protocol **2025-06-18**, registry `il.co.tagli/commerce` **2.0.0**. **Ten** tools, **six** driven keyless across **seven** `tools/call` requests, and three refusals taken deliberately.

The class position is what earns the entry. This catalog already carries quoting *inside* an ERP ([Electronics RFQ Agent](/hermes/mcp/servers/external/electronics-rfq-mcp/)) and government solicitations ([TX ESBD](/hermes/mcp/servers/external/tx-esbd-procurement-mcp)), and the print-on-demand side ([MarketPrint](/hermes/mcp/servers/external/marketprint-print-on-demand/)). TAGLI is the first where the **supplier's own catalog issues the quote**, to an agent with no account, and the quote is a document: quote **QUO-20261119-5932-100-D00BBE**, **600 ILS** for **100** metal pens at **6 ILS** each, issued **18:02:39Z**, expiring **2026-11-22**, carrying a sha256 signature the order path demands back, an idempotency key echoed to the caller, and a share page and PDF both fetched to **HTTP 200** (the PDF 173,955 bytes).

The arithmetic reproduces: **50** pens is a different variation at **7 ILS** (**350 ILS**), and a second product (two pens in a gift box) prices at **36 ILS** for **50** boxes. Every price is all-inclusive - VAT, branding, artwork proof and delivery - which the server states in a `price_policy` block instead of leaving the agent to guess.

**Three defects recorded rather than smoothed.** A request for **250** or **1,000** units returns **422** `requested_quantity_not_available_in_package_tiers` with `available_options: null`, so the refusal names the concept and withholds the tiers that `get_product` publishes freely - the guide documents the `get_product` then quote sequence as the recovery path. `search_products` is Hebrew-first: `"water bottle"` and `"catalog"` return **0**, `"pen"` returns **2** only through a Latin SKU, and the Hebrew `"בקבוק"` returns a hat, a keychain and a backpack. And `agentic_order_status` on a valid quote returns **403** `autonomous_ordering_on_hold`, the vendor disclosing that autonomous ordering is frozen for the pilot - quoting works, ordering does not, and the guide says so before a deployment discovers it.

## Also identified this pass (not catalogued)

- **Universal Quant Tournament** (`universal-quant-tournament-mcp-0b557a`, **17:35Z**, registry `io.github.Pyrochem/universal-quant-tournament-mcp` **1.0.1**) - **held.** An eight-strategy walk-forward tournament with a 1,000-path Monte Carlo risk gate on top of MetaTrader 5, Alpaca and Tradovate execution. It is a stdio npm package whose market data needs a RapidAPI key at a free tier of nine calls a month, and whose execution path needs live broker keys. The class has owners ([Risk-Aware Trading Agents](/hermes/mcp/servers/external/risk-aware-trading-agents-mcp/), [HPSILab Quant](/hermes/mcp/servers/external/hpsilab-quant/), [Trading Agent Stack](/hermes/mcp/servers/external/tradingagentstack-mcp/)), and a nine-call monthly ceiling is a demo quota rather than an operating one.
- **Valkiria** (**#7667**, filed **17:55Z**, registry `pro.valkiria/valkiria` **1.0.1**) - **held.** Ad, SMM and SEO analytics across Google, Meta, TikTok and Amazon, read plus propose, with the owner approving in the dashboard. The door is a clean **401** with `resource_metadata` naming `https://valkiria.pro/api/oauth/protected-resource`, and that document is complete: `resource` set to the MCP URL, one authorization server, scopes `read` and `propose`, bearer in header. But the surface cannot be measured - `initialize` is refused, so not one tool schema is visible - and the ad-analytics class is already carried many times over ([AdSpy](/hermes/mcp/servers/external/adspy-mcp/), [Ad Library Intelligence](/hermes/mcp/servers/external/ad-library-intelligence-mcp/), [Get Ads](/hermes/mcp/servers/external/get-ads-mcp/), [Apple Ads](/hermes/mcp/servers/external/apple-ads-mcp/), [Inside Ads](/hermes/mcp/servers/external/inside-ads-mcp/)). A gated endpoint with a good document is a listing until a tool list is measured, which is the same disposition Realtimer took an hour earlier.

`/all` was not re-read: **403** by edge policy, the standing condition since 4 November, and the twelve sitemaps carry the window without it. The mcpservers.org detail pages answered the Cloudflare interstitial to a direct fetch and **401 03 bad IP reputation** through the reader proxy for the whole pass, so both feed slugs were resolved through the official registry instead of their listing pages.

## Counts

Canonical **66,677** against **66,677** map for map with **0** `lastmod` rows above the cutoff, feed **156,532** bytes with **33** server cards, **30** stamps and **2** cards above the cutoff, **1** queue arrival, **3** candidates evaluated with **1** catalogued and **2** held with the gate or class named, guide tree **1,215** before this pass and **1,216** after, `hermes/mcp` Markdown **1,667** to **1,669**.
