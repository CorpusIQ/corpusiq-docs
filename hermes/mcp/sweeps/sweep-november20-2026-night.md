---
title: "MCP Server Discovery - November 20, 2026 (Night)"
description: "A flat six-hour window on both directories, seventeen arrivals across feed and queue, and three servers that turn unwritten rules into numbers."
category: "MCP Ecosystem"
last_updated: "2026-11-20"
---

# MCP Server Discovery - November 20, 2026 (Night)

Fired on the **03:00 MST** tick, six hours after the evening sweep closed at **04:05Z**. The directory came back identical to the entry on every reading, so the window's material arrived through the feed and the submission queue, and three of those arrivals answer questions this catalog had no owner for: how much of a page reads like a model, what a prediction market's rules said before they were rewritten, and how large a newsletter actually is.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          66,962   IDENTICAL map for map to the 04:05Z capture
  servers/1  ..... 7,588     servers/7  ..... 9,351     sums to 66,962 exactly
  servers/2  ..... 5,949     servers/8  ..... 6,590
  servers/3  ..... 6,518     servers/9  ..... 4,022
  servers/4  ..... 6,746     servers/10 ..... 2,608
  servers/5  ..... 6,954     servers/11 ..... 2,637
  servers/6  ..... 6,756     servers/12 ..... 1,243
priority-servers.xml          299 raw,  34 distinct keys
remote-mcp-servers.xml         15 raw,   1 distinct key
distinct keys, twelve maps    22,958   (prior pass printed 22,952 - see the basis note)
distinct keys, union basis    22,993   (twelve maps + priority + remote)
lastmod rows at or after the cutoff   0
mcp.so /feed                  200, 159,034 bytes, 34 anchors, 30 stamps
                              SIX cards above the cutoff, 0 shipped
submission queue              #7686 to #7696, eleven arrivals, bodies in one call
```

Three readings agree that the canonical did not move: every per-map count is identical to the 04:05Z capture, the twelve sum to the same total, and **zero** `lastmod` rows carry a stamp at or after the cutoff. `/all` was not re-read: **403** by edge policy, the standing condition since 4 November.

**Basis note.** This pass normalises server URLs to the path after the host and strips locale prefixes; that reading gives **22,958** distinct twelve-map keys where the evening pass printed **22,952**. Same raw entries, same per-map counts, so the six-key gap is a normalisation difference and is recorded as one - not as removals, and not as arrivals. The same applies to the union basis (22,993 here against 22,986 there).

**A stale-basis diff is not this window's delta.** Diffed against the union key set retained on disk from the 17:12Z midday capture, the current capture shows **+243 additions and 2 removals**. Those additions are the evening pass's own arrivals, already triaged and disposed in that pass, and one of the two removals (`ahmedkhaleel2004/gitdiagram`) pairs with its `%23` form (`...gitdiagram#use-gitdiagram-from-ai-agents`) present in the same capture. The window's own delta on this surface is therefore **0**, and the 243 is a record of what someone else already read.

## The feed, and the queue

Six feed cards above the cutoff, none of which survived a class check:

```text
site-insights-by-kkv-labs    11/20 07:38 AM UTC
xcortex                      11/20 07:31 AM UTC
rush-0e2e8c                  11/20 07:16 AM UTC
baseedge-labs-catalog        11/20 06:18 AM UTC
finewisdom-api-hub           11/20 04:53 AM UTC
speedyindex-mcp-server-...   11/20 04:33 AM UTC
```

The submission queue carried **#7686** to **#7696**, eleven arrivals with bodies read in one authenticated call. Three of the eleven earned a guide.

## What shipped

Three servers, three guides, all read-only and all driven without a credential.

- **[Lazynext AI Slop Checker](/hermes/mcp/servers/external/lazynext-ai-slop-checker-mcp/)** (**#7687**, filed 05:29Z) at `https://slop-checker.lazynext.com/mcp`, *lazynext-ai-slop-checker* **1.4.4** on negotiated protocol **2025-03-26**, **seven** keyless tools and a fixed corpus of **279 rules across 27 categories**, with npm `@lazynext/ai-slop-checker` **1.4.4** created **2026-11-19T07:41:35Z**. Driven across eight `tools/call` requests: a clean factual paragraph scores **0**; a 165-character filler paragraph scores **37 / 100, 6 matches** on two consecutive calls (determinism verified, not repeated); a 518-character version scores **59 / 100, 13 matches** across five categories; `scan_html` catches the design tell itself (`-webkit-background-clip:text`) beside the word `Unlock`; and `judge` returns **REVIEW** with all six craft-floor items honestly marked `unchecked` on a text scan. Two defects recorded: an **empty string scores clean**, so a length check must run before the score, and a `dir` argument on a hosted endpoint points at the server's filesystem, not the caller's.
- **[RulesWatch](/hermes/mcp/servers/external/ruleswatch-mcp/)** (**#7689**, filed 06:36Z) at `https://ruleswatch.com/api/mcp`, *ruleswatch* **1.1.0** on protocol **2025-06-18**, **five** read-only tools, registry `io.github.whosman/ruleswatch` **1.0.0**. This is the catalog's first record of prediction-market **rule edits**: a Kalshi Formula 1 market rewrote its entire resolution procedure on **2026-11-19T23:35:22Z** (**325** words added, **168** removed) with the Yes price at **0.500** before and **0.700** at the edit, and the tool returns both versions in full. A one-sentence clarification on a New York grocery-store market added **36** words (Yes 0.710 to 0.725 at it). Two limits recorded rather than smoothed: all ten of the newest unfiltered edits were end-date churn on esports markets (one market moved its end time **five times in 98 minutes**), and `get_rule_change` can return a `resolution` kind that the filter enum does not offer.
- **[Stackblade](/hermes/mcp/servers/external/stackblade-mcp/)** (**#7691**, filed 06:36:03Z) at `https://stackblade.app/api/mcp`, *stackblade* **1.1.0** on protocol **2025-06-18**, **five** keyless tools, registry `io.github.whosman/stackblade` **1.0.0**. **35** Substack categories with dated follower counts and board ranks. The measured point of the product: the Technology bestsellers board puts **388,534** followers at #1 and **1,241,686** at #3, because the board ranks paid subscribers rather than audience - and the rising board is a different population entirely (158,674 at #1). Three gaps recorded: `change_30d` returns **null** while `change_7d` is populated, the rank-event stream's newest entry is **2026-10-31** while follower events arrive to the hour, and `/categories`, the URL its own refusal message prints, answers **403** to a direct request from this host.

## What was held

Fourteen candidates, each with the gate or the class owner named.

**From the feed (six):**

- **Site Insights by KKV Labs** (`https://insights.kkvlabs.com/mcp`) - GA4, Search Console and Bing across every site a user manages behind one Google sign-in. The class is carried by this product's own read-only Google connectors and by the catalogued SEO analytics entries; a Google-OAuth wrapper over the same three sources adds no new surface here.
- **XCortex** (`https://xcortex.com/mcp/connect`) - a planner with ten tools, `401 invalid_token` with no challenge and no protected-resource document to read. Task and planning class, and the refusal is the weak tier.
- **Rush** (`https://api.phoenix.so/mcp`) - agent runs on cloud computers with a record and a cost per run, `401 AUTH_FAILED` in a plain JSON body with no `WWW-Authenticate`. Held on the discovery-only gate: nothing measurable without an account.
- **BaseEdge Labs Catalog** (`https://baseedgelabs.ai/mcp`) - keyless, four tools, TradingView strategy presets for futures and CFDs. Trading-strategy class, and the vendor's own disclosures state it is not investment advice.
- **Finewisdom API Hub** (`https://finewisdom.top/mcp`) - **102** keyless-listed tools over Douyin, Xiaohongshu, Weibo, Bilibili, Zhihu, Kuaishou, TikTok and 1688, priced per successful call at CNY 0.1 to 0.3 with **20** free calls on signup. Chinese platform data resale: a per-call billing surface rather than a business data source, and the cost model makes an agent's spend unbounded by construction.
- **SpeedyIndex Google Index Checker** (`https://mcp.speedyindex.com/mcp`) - bulk "is this URL in Google's index" checking without Search Console, `401 invalid_token` before any tool list. Closest miss of the pass: the job is real for anyone shipping backlinks, but no tool surface was readable without an account, so there is nothing to document beyond the gate.

**From the queue (eight):**

- **Google Trends and Google Jobs** (**#7686**) - two Apify actors behind `https://mcp.apify.com/?tools=...`, pay per result on an Apify account. Apify-actor distribution is a standing hold class: the product is the actor, and the directory listing is a transport.
- **Nuluvium** (**#7688**) - Robinhood Chain stock tokens traded through randomised order splitting, **testnet only and not audited** by the vendor's own statement. Held on both counts.
- **Curator Match** (**#7690**) - Steam curators ranked by the games they covered, with key-resale warning signs per curator. A real job for game studios, and the same author as two of this pass's ships; held as a vertical too narrow for a guide this cycle rather than on a gate.
- **Club Ladder** (**#7692**) - public chess ladders, a Lichess and chess.com rating converter and club discovery. Hobby class, same author.
- **Toledo Cleaning Price Estimator** (**#7693**) - keyless, four tools, ballpark cleaning prices for one metro area with every figure cited to Angi, HomeGuide, HomeAdvisor, Thumbtack, Care.com and BLS. A single-market brochure: the citations are honest, the scope is one city.
- **Sekrd** (**#7694**) - a security scanner for AI-built apps (Lovable, Bolt, Cursor, v0, Supabase and Firebase) that scans a live URL from the editor and returns prioritised findings. Interesting class, but the install path needs a `SEKRD_API_KEY` and the server ships stdio only, so no surface could be measured from this host this pass.
- **Bills AI** (**#7695**) - bank statement PDFs to CSV, OAuth against a Bills AI account, `401` with an explicit "sign in with OAuth or send an API key" body. Bank-statement parsing class, auth-gated.
- **SportStatsAPI** (**#7696**) - 3,400+ competitions across eleven sports, keyless on `list_sports` and `find_leagues` and per-call x402 beyond that. Sports data class, carried by the sports entries already catalogued.

## Counts

```text
canonical            66,962 against 66,962    0 raw change, 0 additions, 0 removals
lastmod rows above cutoff             0
feed                 200 at 159,034 bytes, 6 cards above the cutoff, 0 shipped
queue                11 arrivals, 3 catalogued and 8 held
feed holds           6, with the gate or class named
guides               3 added
```
