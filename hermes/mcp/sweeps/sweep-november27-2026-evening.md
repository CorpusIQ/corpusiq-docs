---
title: "MCP Server Discovery - November 27, 2026 (Evening)"
description: "A hundred duplicate rows pruned with no slug moving, two new feed cards, twenty-seven filings, two guides and a listing page no longer 403."
category: "MCP Ecosystem"
last_updated: "2026-11-27"
---

# MCP Server Discovery - November 27, 2026 (Evening)

Fired on the **21:00 MST** tick, **ten hours** after the midday capture, into a directory that lost entries without losing a single product. The thirteen numbered server maps returned **38,669** raw `<loc>` entries against **38,769** at the midday read, and the keyed union did not move at all: **24,830** against **24,830**, a set diff of **0 additions and 0 removals**. **One hundred raw rows disappeared across eleven maps while four maps gained, and the per-map distinct counts held on every capped shard.** That is duplicate pruning, not a slug change, and it is the first time this surface has taken entries away without changing the set of servers.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, 17 maps named, 13 numbered server maps
raw <loc>, maps 1..13         38,669   (midday read 38,769, -100)
  servers/1  ..... 4,080      servers/8  ..... 2,792
  servers/2  ..... 2,511      servers/9  ..... 2,584
  servers/3  ..... 2,948      servers/10 ..... 2,579
  servers/4  ..... 3,181      servers/11 ..... 2,515
  servers/5  ..... 3,345      servers/12 ..... 2,397
  servers/6  ..... 2,856      servers/13 .....   992
  servers/7  ..... 5,889      sum ............ 38,669 exact
distinct keys per map        1,987 / 1,990 / 1,994 / 1,999 / 1,996 / 2,000 x7 / 830
server-map distinct slugs    24,796
priority-servers.xml         254 raw / 34 keys   (midday 250 / 34)
remote-mcp-servers.xml        15 raw /  1 key
union of keyed slugs         24,830   (midday 24,830)
set diff vs 20261127_1100    +0 additions, 0 removals
lastmod rows, server maps    38,669 rows, 14,488 stamped
  at or after 11:52:23Z          468 rows, 377 distinct keys, 0 new to the baseline
  newest anywhere           2026-11-27T23:34:02Z
```

**The arithmetic of the hundred is the whole finding.** Eleven maps lost rows and two gained: **-40 / -14 / -9 / 0 / -11 / -22 / -10 / +1 / -32 / +1 / +18 / -27 / +45**, summing to **-100** exactly, while the distinct count inside every capped map stayed at its ceiling and `servers/13` stayed at **830**. Raw down and keys flat is the fourth shape this surface has produced in three days, after the 302-slug shard filling, the 736-key restamp wave and byte-stability: **whoever writes these maps is de-duplicating locale rows in place**, and a reader that diffs raw totals reports a directory that shrank by a hundred when it did not move. `servers/13`, which received 302 slugs this morning, both gained **45** raw rows and held its distinct count - the same pruning running on the new material.

The stamps agree that nothing arrived: **468** rows sit at or after the midday cutoff, they collapse to **377** distinct keys, and **not one of those keys is new to the stored baseline**. A restamp wave, with the newest stamp anywhere at **2026-11-27T23:34:02Z**.

## The feed turned over two cards, and one card the midday table missed

`mcp.so/feed` answered **200** at **158,176** bytes with **33** card anchors - **29** `/servers/` cards, **one** `/agents/` card and three navigation links - every listing card stamped. The page's anchor shape is unchanged from the night read (plural `/servers/`, stamps in a `title` attribute at minute resolution, body text reading *Submitted N hours ago*), which is worth stating because a second shape change in forty-eight hours would break the reader silently.

| Card | Stamp (UTC) | What it is | Disposition |
|---|---|---|---|
| `hypro` | 11/28 00:14 | Hypertro AS | Held, fitness vertical |
| `nutrinomist` | 11/27 21:36 | Anna Stroganova, nutrition | Held, nutrition vertical |
| `winly-mcp` | 11/27 16:03 | getwinly | Held, unclassified single tool |
| `magi-2-ai-video-api` | 11/27 13:04 | `/agents/` listing, video API | Out of scope, agent marketplace |

Two of those are genuinely above the midday top of **16:59Z** (`corsair`). **`winly-mcp` is not, and that is the interesting row:** it sits at **16:03Z**, inside the eleven-hour range the midday pass tabulated from **16:59Z** down to **10:55Z**, and its table carries ten cards where the range held eleven. A sibling pass dropped a card inside its own window. Tonight's read records it and the count is reconciled here rather than silently inherited.

## The queue carried twenty-seven filings

`chatmcp/mcpso` issues **#8246** to **#8273**, the newest filed at **2026-11-28T03:37:58Z**, read with titles and bodies. **#8252 is absent from the sequence**, which is a deletion or a transfer rather than a gap in the read: the API returned thirty consecutive records spanning #8273 down to #8243 with no other hole.

| Issue | Product | Disposition |
|---|---|---|
| #8246 | governed-warehouse-mcp (governed metrics over DuckDB, Ed25519 agent tokens, fail-closed SQL guard) | Held, local and Docker only |
| #8247 | Herobrain Minecraft builder | Held, gaming vertical |
| #8248 | FastQA (local stdio browser QA) | Held, local install |
| #8249 | QRSteward | Held, QR utility |
| #8250 | **Verified x402 directory** | **Catalogued** |
| #8251 | ClearCaption X tweet scraper (Apify) | Held, Apify-actor class |
| #8253 to #8256 | DirectAPI Labs five: Google Play leads, Shopify store leads, Telegram channels, US Federal Contracts and Grants, CVE and package security | Held, publisher fleet, and see the zero-key defect below |
| #8257 to #8260 | ClaudeRewrite, Kerno, NameOcean, Stets | Held, memory, domain and rewrite classes |
| #8261 to #8264 | Kerno, NameOcean, Varyz Teams, Nolavi Connect | Held with class named |
| #8265 to #8267 | **Hiring Signals**; Nolavi, NestLens | **Catalogued** plus two holds |
| #8268 to #8273 | Atmet WhatsApp, Tote, GoodComments, Does It ARM, Rubik roleplay, znk-mcp | Held, messaging, feedback and consumer verticals |

## Two guides

- [Hiring Signals MCP - 208,350 Open Jobs From Company Career Sites](/hermes/mcp/servers/external/hiring-signals-mcp/) - **four tools, free key, ten calls driven and the credit arithmetic reproduced.** `get_status` answers keyless with **208,350** open jobs across **5,069** companies on **5,544** boards, **0** boards in error, a sync **7.87 h** old, and the number that governs every other answer: `salary_pct` **29**. A free key minted by one POST with **100** credits and the balance read back at every step: **100 → 87** after a 5-credit company read, a second 5-credit read and a 3-row search, **→ 81** after two more searches, **→ 71** after a 10-row page, with a query that returns nothing charging **0**. `company_hiring` is the tool that earns the entry: **Stripe** at **767** open, **37** new in seven days and **237** in thirty, `remote_share` **0.15**, with the funded department visible in the board's own codes (`1185 Account Executives (EMEA)` 50, Product Design 14); **RevenueCat** at **11** open, **Product 4** and **Growth 4** against Engineering 2, and nine priced roles led by Head of Sales at **363,000** and Head of Customer Growth at **259,000**. **The two boards disagree about pay data and that is the finding:** Stripe returned an empty `top_salaries` with 767 openings while RevenueCat returned nine of eleven, because Greenhouse boards publish ranges in prose and Ashby boards carry them as fields. **Five defects recorded:** `remote` is true on city-bound postings including one that reads `Florence (on-site)` and on a board with `remote_share` 1.0 whose listings sit in New York; `closed_last_30d` reads **0** on both boards with 767 and 11 open, so the field measures only closures the tracker watched; an auth failure answers **200 with `isError: false`** and an `{"error": …}` text body, which a protocol client reads as success; `q` matches text the response never returns (`designer` surfaced an Electrical Engineer, `barista` surfaced a Personal Care Specialist, one title in three containing the term, and a nonsense query returning zero); and ordering is recency rather than relevance, so ten consecutive rows came from one employer pushing ten distinct requisitions in three minutes.
- [Verified x402 MCP - A Directory of Machine-Payable APIs](/hermes/mcp/servers/external/verified-x402-mcp/) - **the first machine-payment directory here, keyless, three tools, six calls driven.** `search` and `check_endpoint` are free; `recommend` costs **0.005 USDC** and, unpaid, returned a complete **x402 v2 challenge** inside a 200 JSON-RPC result: two rails at **5000 atomic** USDC, Base `eip155:8453` with a plain transfer and Solana with the server as fee payer, both on a **60-second** window, with the amount as a **string** rather than a float. Rows carry more than the description promises: `verification.httpStatus` **402** means the checker made the request and got the challenge rather than a cached page, `price.atomic` sits beside a derived `usd` (**20000 → 0.02**), and `bazaar` carries Coinbase's own 30-day demand (**83** calls, **83** unique payers) with an `integrityExplanation` written to be quoted. **`check_endpoint` on the server's own address is the best available test of the checker and it passed:** **522**, `got402: false`, *"HTTP 522 is a temporary server error, not a payment challenge"* - it refused to score an outage as a paywall. **Five defects recorded:** `q: "weather"` returned an on-chain reserve's exit fee forecast whose `category` field reads `weather`, so the match lands on the label rather than the meaning; parameterised route templates are published as callable endpoints (`.../stations/:network/:code/day` answering **400**, `.../point/:latlon` answering **404**); `price.usd` is **null** on a Solana row with `atomic: 5000` while Base rows resolve, so `max_price` silently drops one rail; the filed **77,827** API count is unverifiable because `search` returns no total; and the default result set mixes `no_402` dead entries into live ones unless `verified=1` is set.

## Also identified this pass (not catalogued)

- **DirectAPI Labs** filed five servers eight minutes apart (#8253 to #8256), a fleet shape held under the standing one-tool-per-actor ruling. One of the five was probed and the probe is why the fleet is held on evidence rather than on style: `https://whthpnd--us-federal-contracts-grants-api.apify.actor/mcp` answered **401 `api-token-missing`** to both `initialize` and `tools/list`, with the message *"This is a standby Actor. To use it, you need to pass your Apify API token."* The filing's own heading reads **Zero-key**, so the listing promises an open door the endpoint does not have. That is the same defect recorded on Outscraper this morning and on five other filings before it, and it is the reason a fleet is never catalogued from its descriptions.
- **governed-warehouse-mcp** (#8246) is the strongest hold of the queue and it is held on **address, not merit**: an Ed25519-signed JWT, a semantic layer that compiles metric requests, a fail-closed SQL guard on a read-only DuckDB, token scopes that decide which models and PII columns an agent may see, and an audit trail. It runs locally over stdio or in Docker and publishes no remote, so there is nothing to probe from outside. Recorded for the governance class owner, which in this catalog is the trust layer rather than a data vendor.
- **NameOcean** (101 tools, OAuth 2.1 with dynamic registration, domains, DNS, SSL, mail and uptime, with money-losing tools annotated destructive and a cart-and-checkout model so nothing spends) is held on the **domain-management class**, which the catalog already carries; the scope split is noted rather than new.
- **ClearCaption** and **FastQA** are held on address again: an Apify actor behind a bearer token and an `npx` stdio package. **Varyz Teams**, **Kerno**, **Atmet Chat for WhatsApp**, **NestLens**, **Nolavi Connect**, **Stets**, **Tote**, **ClaudeRewrite**, **GoodComments**, **Does It ARM**, **QRSteward**, **Herobrain**, **Rubii** and **znk-mcp** are held on carried classes or as consumer verticals, none reaching a driven tier this pass. The feed's **hypro** and **nutrinomist** are single-purpose consumer apps with no business system behind them, held on the vertical.

## Listings re-measured

- **mcpservers.org** `/servers/corpusiq-io` answered **200** at **76,266** bytes, title *"CorpusIQ MCP Server | Awesome MCP Servers"*, **55** `corpusiq` occurrences and no Cloudflare challenge. **The 403 interstitial recorded on this page since November 4 did not appear**, so the edge policy is not a constant and the previous three passes' wording (edge policy, not a delisting) held for the right reason and the wrong permanence. Recorded as measured, with the status change named.
- **mcp.so** `/servers/corpusiq-docs` answers **200** at **856,937** bytes with **175** `corpusiq` occurrences, against **857,333** at the midday read.
- **Official registry** `io.corpusiq/multi-source-mcp` carries **four** records, **1.0.0** to **1.0.3**, every one with a `streamable-http` remote at `https://mcp2.corpusiq.io/mcp`, titled **CorpusIQ** and described as *"Authenticated, user-scoped MCP connectors for 30+ business systems."*
- **Glama** answers **200** at **732,174** bytes with **596** `corpusiq` occurrences on the connector route.
- **Smithery** and the **Anthropic connectors directory** were not re-read this pass; the November 16 submission's status lives only in the portal and nothing is inferred from silence.
