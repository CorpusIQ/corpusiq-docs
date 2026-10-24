---
title: "New Skills - October 23, 2026 Evening"
description: "Skills.sh sweep (Oct 23 evening): 99 new skills, one publisher cluster from the trending board at 146.7K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct23-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-10-23"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 23, 2026 Evening Sweep

Evening sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The same 20-query window (15 Hermes-focused plus the 5-query generic pass) served 886 unique skills with 0 failed queries: 99 NEW, 271 PARTIAL.

The NEW lane produced nothing above the guide floor for the tenth consecutive fire, and its top row this time was nodeops-app/skills createos at 1,679 installs. Everything that converted came from the trending board, which served 572 entries across 64 sources. Sixty-three of those 64 sources already had a catalog page. The single uncovered source was binance/binance-skills-hub, which the board showed as one row at 2,973 installs and which a publisher query sized at 146,680 combined installs across 35 listings. That is a 49x multiple, and it is why the publisher query runs on every uncovered source regardless of how small its board row looks.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected | 886 (0 failed queries) |
| NEW (not in catalog) | 99 |
| PARTIAL (source known, skill not cataloged) | 271 |
| New publisher guides | 1 (35 indexed listings, 146,680 combined installs) |
| Above-floor finds rejected | 0 |
| Zero-catalog audit | 47 PARTIAL sources at 100+; 0 uncovered in catalog/ recursive (730 markdown files); 0 converts |
| Board | Trending 572 entries / 64 sources; 63 covered, 1 uncovered, 1 convert |
| Marketplace count | 1,150+ to 1,151+ |

## New Publisher Guides

### 1. Binance Skills Hub (146,680 combined)

**Source:** [binance/binance-skills-hub](https://www.skills.sh/binance/binance-skills-hub), 35 indexed listings, top skill `square-post` at 30,544; 1,083 stars; no repository-level LICENSE while four skill directories ship their own MIT LICENSE.md; pushed 2026-10-23.

Binance's own skill marketplace for crypto. Two families sit in one repository. The first is an authenticated exchange surface: `binance-cli` reaches spot, USD-S and COIN-M futures, options, margin and portfolio margin, Convert, algo orders, sub-accounts, Simple Earn, VIP loans, P2P, fiat and payments, each documented as an endpoint table an agent can follow. The second is Web3 read work that needs no key: token security audits, wallet and holder snapshots, smart-money signals, trader leaderboards, tokenized-stock data and a `baw` wallet CLI that can also send, swap and stake.

Beta tier, and the reason is structural rather than cosmetic. Snyk fails thirteen of the 35 listings. The detail page for spot records HIGH risk W007, insecure credential handling, because the signing instructions require the `X-MBX-APIKEY` header and the secret key to build the signature, which puts key material into the agent's command path, with W009 direct money access recorded alongside. The Web3 read skills pass all three auditors. The guide covers all 35 listings, including the fourteen that are endpoint reference files inside the `binance` skill rather than installable directories.

## Why This Fire Matters

The board row and the repository size have drifted so far apart that the row is no longer a signal of anything. Binance showed as a 2,973-install row and is a 146,680-install publisher with 35 listings. The publisher query is the only step in this pipeline that measures the repository instead of the row, and it is now the single highest-yield step in the sweep.

The second pattern is worth naming: this is the second crypto exchange in the catalog to ship skills as endpoint tables plus a CLI, after OKX. That shape is winning inside regulated platforms because their API surface is already large and already documented, so a skill file is a thin, auditable layer over something that exists. It also concentrates risk exactly where auditors look, which is why both of those guides carry a lower tier than their install counts would suggest.

## Cross-Reference Note

The coverage test excludes per-fire report pages (`!**/marketplace/new-*/**`), so a name stays NEW until a guide exists. The zero-catalog audit walked `catalog/` recursively (730 markdown files) and found 0 of the 47 PARTIAL sources at 100 or more installs without a page, the tenth consecutive fire with no convert from that lane. `/popular` returned HTTP 404 again and `/skills` is a shell with no embedded skill JSON, so trending remains the only board that returns data.

---

*← [Skills Marketplace](/hermes/skills/marketplace) | [Skills Catalog](/hermes/skills/catalog) →*
*Powered by CorpusIQ*
