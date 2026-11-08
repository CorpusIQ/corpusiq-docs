---
title: "MCP Server Discovery - November 8, 2026 (Midday Supplement)"
description: "Supplement pass one hour after the midday sweep: the sitemap canonical was set identical and the queue carried two arrivals, both catalogued."
last_updated: 2026-11-08
tags: ["mcp server", "model context protocol", "mcp discovery", "november 2026"]
---

# MCP Server Discovery - November 8, 2026 (Midday Supplement)

Fired on the **11:00 MST** tick, one hour after the midday pass that catalogued ListRiver. Two servers were catalogued, and neither came from the directories: the sitemap canonical came back **set identical**, the mcp.so homepage carried **no card above the previous stamp**, and both finds arrived in the submission queue inside that single hour. The window is a clean demonstration that the queue is a live surface in its own right rather than a second read of the feed.

## Surfaces read

| Surface | Result |
| --- | --- |
| mcpservers.org twelve-sitemap canonical | **20,018** distinct server slugs from **63,435** raw `<loc>` entries across **13** server maps, **set identical** to the 10:00 capture: **0 additions** and **0 removals** |
| mcp.so homepage | **188** `createdAt` occurrences and **115** distinct stamps, newest `2026-11-08T15:50:03.559Z` on both the plain and the cache-busted read: **0 cards** above the 10:00 stamp |
| chatmcp/mcpso issue window | **#6944** and **#6945**, two arrivals filed at `17:24:41Z` and `17:42:17Z`, both after the midday window closed at **#6943** |
| mcpservers.org `/all` and detail routes | **403** direct, the standing condition since November 4; not re-read this pass |
| Official MCP registry | Both arrivals resolved to active records |

The set-identical canonical is the arithmetic proof that nothing landed on the sitemap side between the two passes: same 20,018 slugs, same 63,435 raw entries, same thirteen maps, fetched fresh rather than carried. A one-hour gap on this surface has now produced an empty diff on every attempt this month.

## Catalogued

### Marsell MCP

A marketing platform that runs the month for one business, exposed as **126 tools** at `https://getmarsell.com/mcp`. A keyless `initialize` answers **200** as `marsell` **1.0.0** and returns an instruction block that is an operating manual rather than a pitch; `tools/list` returns every schema; `tools/call` returns the documented **401** naming the agent key. Fully documented, not driven.

The finding is the direction of the delegation. Every other marketing entry in this catalogue is a tool the assistant calls. Marsell is a client that calls the assistant back: `homework_list` assigns the jobs the platform cannot do because they need the owner's own logins, files or inbox, and some of those jobs the platform **verifies itself** before accepting them as done. `missions_next` returns one message at a time to be sent from the owner's own signed-in browser, word for word, with a refusal recorded rather than reworded. Facts and rules are separate stores, and `owner_fact_set` writes a correction that every plan, post and page reads first. Money is quoted before it is spent: `picture_price`, `series_quote`, `business_read_quote` and `get_tokens` all price the work ahead of the render.

Plans run **$49** a month for 200,000 tokens to **$799** for 3,600,000, annual at ten times monthly, extra tokens from **$1.80** down to **$1.50** per 10,000, ad spend and creator fees separate.

### Worth Leaving MCP

One keyless tool at `https://worthleaving.com/api/mcp` that answers what leaving on a date forfeits, what the next vest is worth and what a new offer has to beat. `initialize` **200** as `worth-leaving` **1.1.0**, registry record `com.worthleaving/verdict` published **four minutes** before the submission was filed.

The instruction is the entry: **never compute vest dates or dollar totals yourself.** Driven live with a two-grant scenario, it returned `take-it (77/100)`, a walk-away cost of **$62,500**, an offer threshold of **$230,000** a year pre-tax, an annual net gain of **$28,965** and the next vest worth waiting for on **2027-02-01** at **$12,500**, then sixteen numbered assumptions including that the date sent was in the past and that the comparison was money-only because no ratings were supplied. Share links carry rounded bands rather than figures. Free, per-IP rate limited, no inputs stored, US metros only.

## Held

No holds this pass. Every other item considered was already dispositioned in the 10:00 sweep, and the two arrivals are the whole window.

## Core listing check

Measured, not inherited. The fresh canonical carries `/servers/corpusiq-io` and `/servers/corpusiq/corpusiq-docs`. mcpservers.org `/all` is the standing 403 rather than a delisting. All four direct mcp.so slugs (`corpusiq`, `corpusiq-io`, `corpusiq-mcp`, `io.corpusiq`) answer **404**, so that listing remains absent.

**Glama changed shape this hour.** Both `/mcp/servers/corpusiq-io` and `/mcp/connectors/corpusiq-io` now answer **301** to a query page (`?query=author%3Acorpusiq-io` and `?query=namespace%3Acorpusiq-io`), which answers **200** and reports `corpusiq-io` matches. That is a routing change in the same class as the October 26 move, not a delisting: the detail page is no longer directly addressable and the listing is carried forward unverified at the card level, to be re-read on a later pass rather than recorded either way on a single redirect.

## Counts

Canonical **20,018** against **20,018** with **0** additions and **0** removals from **63,435** raw loc entries across thirteen maps; mcp.so **188** `createdAt` occurrences and **115** distinct stamps with **0** cards above the previous stamp; **2** queue numbers, both arrivals; **2** endpoints probed, both keyless **200** with full schemas, one **401** on `tools/call` and one driven to a live result; **2** servers catalogued and **2** guides; guide tree **1,121** directories before this pass and **1,123** after, **1,264** entries before and **1,266** after, **1,531** Markdown files under `hermes/mcp/` before and **1,534** after.

## Sources checked

- `https://mcpservers.org/sitemap.xml` and the thirteen server maps, fetched fresh (HTTP 200, 2026-11-08 11:00 MST)
- `https://mcp.so/`, plain and cache-busted, direct with a browser user agent (HTTP 200)
- `gh api repos/chatmcp/mcpso/issues/6944` and `/6945`
- `https://registry.modelcontextprotocol.io/v0/servers?search=getmarsell` and `?search=worthleaving`
- `https://getmarsell.com/mcp`, `https://docs.getmarsell.com/developers/mcp`, `https://getmarsell.com/pricing`
- `https://worthleaving.com/api/mcp`, `https://worthleaving.com/walk-away-cost`
- `https://mcp.so/server/<slug>` for the four CorpusIQ slugs, `https://glama.ai/mcp/servers/corpusiq-io` and `/mcp/connectors/corpusiq-io`
