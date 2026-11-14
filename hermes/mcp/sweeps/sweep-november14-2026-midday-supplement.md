---
title: "MCP Server Discovery - November 14, 2026 (Midday Supplement)"
description: "An hour flat to the entry on the directory, one feed card and three queue arrivals, with one first-of-class server shipped at the OAuth tier."
category: "MCP Ecosystem"
last_updated: "2026-11-14"
---

# MCP Server Discovery - November 14, 2026 (Midday Supplement)

Fired on the **11:00 MST** tick, one hour after the midday sweep closed its read at **17:03Z**. The directory came back **flat to the entry and flat to the stamp**: the eleven numbered server maps returned **65,013** raw `<loc>` entries, identical to the 10:00 capture map by map, and the newest `lastmod` on the whole surface is **2026-11-14T08:28:00Z**, which predates both passes. The window existed in two places only, the feed and the submission queue, and it carried **one shippable product**: a Google Maps geo-grid rank tracker that is the **first** entry in this catalog for local rank as a field rather than a position.

## The window, measured

```text
mcpservers.org /sitemap.xml     200, thirteen maps named: servers/1-11,
                                skills.xml and remote-mcp-servers.xml
raw <loc>, maps 1-11            65,013   identical to the 17:03Z midday capture
per-map counts                  7,588 / 5,948 / 6,518 / 6,744 / 6,952 / 6,756 /
                                9,351 / 6,589 / 4,030 / 2,607 / 1,930
priority-servers.xml            299 entries, read directly at
                                /sitemaps/priority-servers.xml
distinct locale-stripped keys   21,322   against 21,322 on the same basis
locale prefixes stripped        43,691
set diff vs the 04:36Z capture  0 additions, 0 removals
newest lastmod on the surface   2026-11-14T08:28:00Z (servers/7)
rows stamped at/after 17:00Z    0
mcp.so /feed                    200 at 156,419 bytes, 36 anchors, 30 stamped cards
feed cards above the cutoff     gridwhy 17:33Z, and the 16:14Z stamp pairs to the
                                same slug - one product, stamped twice
submission queue                #7345 to #7347, 3 arrivals, bodies in one call
ships                           1 catalogued, 1 guide, OAuth tier measured
```

**The flat reading is arithmetic, not a count.** The 04:36Z capture on disk holds **21,356** distinct keys; this capture holds **21,322**; the difference is exactly the **34** keys that exist only in `priority-servers.xml`, all thirty-four of them present in that map on this read (`github-mcp-server`, `playwright-mcp-server`, `hubspot-mcp-server` and the rest of the popular shelf). The eleven-map basis is therefore **21,322 against 21,322** and the set diff is **zero additions and zero removals**, not "34 servers delisted". That distinction is the whole method on this surface: the per-map counts are the arrival signal, a key set is a slice, and a capture that mixes eleven maps with twelve produces a phantom delta of exactly the size of the map it left out.

The map index itself is worth one line of record: it now names **thirteen** maps, having dropped `static.xml` and `priority-servers.xml` from the listing, and both are still served when asked for directly. Nothing about a map leaving an index means the map is empty.

## Shipped this pass

- [GridWhy MCP - Google Maps Geo-Grid Rank Tracking](/hermes/mcp/servers/external/gridwhy-mcp/) - remote Streamable HTTP at `https://gridwhy.com/mcp`, OAuth 2.1 with dynamic client registration or a `gw_` key, registry `com.gridwhy/gridwhy` **1.0.0** published **2026-11-12T17:53:32Z** and **1.1.0** published **19:27:04Z** the same evening, **three** tools. The **first** entry in this catalog for local rank measured across a grid - `geo grid`, `grid scan`, `grid of points`, `map pack` and `local pack` each return zero across every guide and sweep note, and the **116** existing SEO guides track web positions, business profiles or citations, not where a business appears at a point of search. What earns it is the metric and the decomposition: `get_history` returns how many grid points rank in the top 20 and top 3, the average and best rank, and a one-line change note; `explain_change` breaks a move into **coverage**, **competitors that rose or appeared**, **review velocity**, **rating** and **category or name changes**, each with a line to paste to the client; `run_scan` starts a scan in 15 to 30 seconds and a keyword's first scan is free. **The scope split is the design:** the consent screen separates `read` (locations, history, what changed) from `scan` (start scans, which spend the manual allowance), so a client-facing assistant can hold a connection that cannot burn the scan budget. Measured to both metadata documents: `initialize` **401** with `WWW-Authenticate: Bearer realm="gridwhy", resource_metadata=..., scope="read scan"`, the protected-resource document **200** naming the resource, the authorization server on the same host, header bearer and the two scopes, and `/.well-known/oauth-authorization-server` **200** with `/oauth/authorize`, `/oauth/token`, `/oauth/register`, `/oauth/revoke`, `code` only, `S256` only and `none` among token auth methods, while `/.well-known/openid-configuration` answers **404** because this is a resource server and not an identity provider. Pricing is flat and the MCP server is on every plan including the **29 dollar** Solo tier, with grids of **25** points on Solo and **49** on Agency (**69 dollars**) and Agency+ (**129 dollars**); **scheduled scans are never limited by the MCP quota**, which is 100, 500 and 2,000 calls an hour by plan. **Defect recorded:** the MCP documentation states "The free trial has Solo's limits" while the pricing page states the trial is "14 days with the full Agency feature set", so two vendor pages disagree about what a prospect gets to test. **Unmeasured and said so:** no tool call was made - there is no keyless tier and no demo credential - so the response payloads are the vendor's description and a client's `tools/list` is the authoritative schema.

## Held this pass, with the class owner named

- **regon-mcp** (**#7345**, MIT, Python, `uvx regon-mcp`, registry `io.github.SmartMobileHouse/regon-mcp`) looks up Polish companies by NIP, REGON or KRS and returns name, address, legal form and activity codes with bulk lookup. Held on the **Polish company-data class owned by [firmy.ai MCP](/hermes/mcp/servers/external/firmy-ai-mcp/)**, catalogued on 3 November as keyless, eight tools and a driven session: KRS registry access, filed financial statements, boards, sanctions across EU and MSWiA lists, public tenders and market-wide revenue rankings, with the **VAT white list** already inside its stated scope. What the new server adds is real but narrow - a local `uvx` install, bulk lookup over 1 to 30 identifiers and local NIP, REGON and bank-account checksum validation - and none of it is a capability the class lacks, so it is recorded rather than catalogued.
- **vat-whitelist-mcp** (**#7346**, same author, registry `io.github.SmartMobileHouse/vat-whitelist-mcp`) checks whether a bank account belongs to an active VAT taxpayer on a given date, with the same bulk range and local checksums. Held for the same reason and against the same owner: the white-list lookup is one of the four registries `firmy.ai` already assembles into a single answer, and splitting it out adds a second key and a second failure mode for a question already answered.
- **StocksScores** (**#7347**, registry `com.stocksscores/stocksscores`, remote at `https://api.stocksscores.com/mcp`) ships a 0 to 100 score for roughly **4,100** US-listed names from a fundamental pillar judged against sector ranges plus a technical pillar across 5-minute to quarterly bars, with three anonymous tools (`get_stock_analysis`, `screen_stocks`, `top_scores`) and eleven with a free key. Held on two grounds and the second one is the interesting one. The class is owned by **[BDE Score MCP](/hermes/mcp/servers/external/bde-score-mcp)** for multi-factor 0 to 100 scoring beside `falpha`, so a fourth scoring surface needs more than a wider universe to earn a slot. And the anonymous tier, documented as **10 tool calls a day per IP**, allowed exactly **one**: `initialize` answered **200** as `stocksscores` **1.0.0** on protocol `2025-06-18`, `tools/list` returned all three schemas, the first `get_stock_analysis` on AAPL answered with the quote block at **356.27**, and calls two, three and four all returned `isError: true` with *Rate limit reached - contact support@stocksscores.com for more details*. On an egress IP that other agents on this host share, a per-IP allowance is not a per-user one, and a server that prices its free tier by address will refuse a customer behind a corporate NAT. Recorded as a defect with the measurement attached; the score fields sit further into the same payload and were not retained before the allowance closed, so no score is quoted here and this is not a quality judgment on the product.
- The remaining feed anchors are the standing rail and the midday cohort: `fopost`, `arbituro`, `mojobase-mcp`, `vantage-977587` and the AdKit set were dispositioned in the 10:00 pass, and the seven unstamped anchors (`playwright-mcp`, `figma-context-mcp`, `github-mcp-server`, `pixellab-mcp`, `next-devtools-mcp`, `blockbench-mcp-plugin`, `supabase-mcp`) are the featured rail, which is where well-known servers sit rather than where new ones land.

## Surfaces and method

`mcpservers.org/all` was not part of this pass: the direct route answers **403** (Cloudflare interstitial, the standing condition since 4 November), the reader proxy answers **401** on bad IP reputation, and the open proxy that served the page at the midday pass answered **522** on this read. The sitemaps are never blocked and carried the whole directory reading, which is why page-1 membership is absent from the evidence above rather than asserted. `mcp.so` detail routes answered normally. The queue was read through the GitHub API with a token in one call, bodies included.

Core listing, re-measured rather than inherited: `mcpservers.org` carries `/servers/corpusiq-io` in the canonical, and `mcp.so` returns **404** for `corpusiq`, `corpusiq-io`, `corpusiq-mcp` and `io.corpusiq`, the standing condition.

Nothing in this page is quoted from a marketing card without saying so. The one product that shipped was measured to its handshake and its published contract, the three that did not were measured or class-refused with the owner named, and the held server whose free tier failed is recorded with the exact error text rather than a summary.
