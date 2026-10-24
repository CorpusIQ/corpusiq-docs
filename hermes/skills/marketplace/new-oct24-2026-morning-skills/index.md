---
title: "New Skills - October 24, 2026 Morning"
description: "Skills.sh sweep (Oct 24 morning): 97 new skills, one publisher cluster from the trending board at 64.6K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct24-2026-morning-skills/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 24, 2026 Morning Sweep

Morning sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The same 20-query window (15 Hermes-focused plus the 5-query generic pass) served 886 unique skills with 0 failed queries: 97 NEW, 271 PARTIAL.

The NEW lane produced nothing above the guide floor for the eleventh consecutive fire, and its top row this time was kv0906/cc-skills premium-frontend-design at 1,372 installs. Publisher follow-ups on all three NEW sources above 1,000 installs stayed below the floor: kv0906/cc-skills at 2,109 combined across 40 listings, adamlipecz/esp32-firmware-engineer-skill at 1,321 as a single listing, and arjitj2/swiftui-design-principles at 1,316. Everything that converted came from the trending board, which served 483 entries across 52 sources.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected | 886 (0 failed queries) |
| NEW (not in catalog) | 97 |
| PARTIAL (source known, skill not cataloged) | 271 |
| New publisher guides | 1 (9 indexed listings, 64,574 combined installs) |
| Above-floor finds rejected | 0 |
| Zero-catalog audit | 45 PARTIAL sources at 100+; 0 uncovered in catalog/ recursive (731 markdown files); 0 converts |
| Board | Trending 483 entries / 52 sources; 51 covered, 1 uncovered, 1 convert |
| Marketplace count | 1,151+ to 1,152+ |

## New Publisher Guides

### 1. Solana Mobile Skills (64,574 combined)

**Source:** [solana-mobile/solana-mobile-skills](https://www.skills.sh/solana-mobile/solana-mobile-skills), 9 indexed listings, top skill `integration-privy` at 10,646; 8 stars; Apache-2.0; pushed 2026-10-21.

The Solana Mobile team's own agent skill set for Android development. Seven self-contained skills cover the path from an empty project to a published release: scaffolding and toolchain checks through the `solana-mobile` CLI, Mobile Wallet Adapter connect and send, Seeker Connect for Expo, Kotlin and web dapps, `.skr` domain resolution, Seeker Genesis Token gating, Privy login over Sign-In-With-Solana, and dApp Store release signing.

Beta tier. The repository is disciplined where it counts: CI validates every skill against the Agent Skills spec and the `plugin.json` manifest, the README states the portability rules the repo enforces, and each skill pushes detail into `references/` so activation stays cheap. The reservation is scale, not quality. Eight stars is a small community footprint, and the two listings that reach a signature, `solana-mobile-wallet` and `seeker-connect`, both carry Snyk W009 for direct money access while the other five pass all three auditors.

## Why This Fire Matters

The board continues to be the only lane that converts. The NEW lane has now been silent for eleven consecutive fires, and this morning it also produced the tell that makes the publisher follow-up mandatory: three sources looked like plausible converts on a single row of 1,300 to 1,400 installs and all three measured under 2,200 combined when queried by owner. A row is a sample, not a size.

The substantive find is a platform team shipping procedures rather than an SDK. Solana Mobile's skills check `package.json` before writing wallet code, because two client stacks coexist in this ecosystem with different provider props, hook return values and transaction construction. An agent that reads first cannot mix them. That single structural rule is worth more than most of the content in the file, and it is the pattern to look for when judging the next vendor suite.

## Cross-Reference Note

The coverage test excludes per-fire report pages (`!**/marketplace/new-*/**`), so a name stays NEW until a guide exists. The zero-catalog audit walked `catalog/` recursively (731 markdown files) and found 0 of the 45 PARTIAL sources at 100 or more installs without a page. `/popular` returned HTTP 404 again and `/skills` is a shell with no embedded skill JSON, so trending remains the only board that returns data.

---

*← [Skills Marketplace](/hermes/skills/marketplace) | [Skills Catalog](/hermes/skills/catalog) →*
*Powered by CorpusIQ*
