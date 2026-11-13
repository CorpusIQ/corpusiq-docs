---
title: "MCP Server Discovery - November 13, 2026 (Midday Supplement)"
description: "An hour where the sitemap and the feed were both flat, the queue carried nine arrivals, and two tools shipped on what they refuse"
category: "MCP Ecosystem"
last_updated: "2026-11-13"
---

# MCP Server Discovery - November 13, 2026 (Midday Supplement)

Fired on the **11:00 MST** tick, one hour after the midday pass closed at 17:03Z. Both discovery surfaces came back flat and the arithmetic of the previous row had to be corrected, so the window was entirely the submission queue: **nine** arrivals, of which two earned a guide and one of those earned it by publishing its own losing result.

## The window, measured

```text
mcpservers.org /sitemap.xml      200, fifteen maps named, twelve of them server maps
raw <loc> entries                64,823   identical to the 17:03Z midday capture
per-map counts                   priority 299 / 7,588 / 5,948 / 6,518 / 6,744 / 6,952 /
                                 6,756 / 9,351 / 6,589 / 4,029 / 2,606 / 1,443
newest lastmod                   2026-11-13T07:36:23Z  (usezn/zn, carried from the night read)
lastmod at or after 17:03Z       0 rows
distinct keys, locale-stripped   21,123   identical to the midday capture
mcp.so /feed                     200 at 156,078 bytes, 37 card anchors, 30 stamped cards
                                 0 above the cutoff; newest card assistant-24-7 at 14:43Z
submission queue #7284 to #7292  9 arrivals, no gaps
```

## A flat hour, and one row corrected

Both surfaces are unchanged from the pass one hour earlier, and the small discrepancy that remains is arithmetic rather than inventory.

The per-map counts are identical on all twelve maps except `servers/9`, which reads **4,029** here where the midday row printed **4,031**. That row's own per-map sum is 64,825 while its stated raw total is 64,823, so one of its two figures was two entries off. This capture resolves it: the twelve counts in the block above sum to **64,823** exactly, matching the raw `<loc>` total the midday pass stated and this pass re-read. Nothing arrived and nothing left; a per-map figure in the earlier row was carried two entries high.

The second reading supports the same conclusion. Distinct locale-stripped keys stand at **21,123** on both captures, and **zero** `lastmod` rows carry a timestamp at or after the 17:03Z cutoff, with the newest stamp on the whole surface still the `2026-11-13T07:36:23Z` entry the night pass first read. A refresh that added anything would have stamped it.

The feed is equally still: **156,078** bytes, **37** card anchors and **30** stamped cards in the `M/D/YYYY, HH:MM AM/PM` UTC form, with the newest at **14:43Z** - the same `assistant-24-7` card the midday pass dispositioned. At a one-hour gap the feed is purely the queue's public face, so no independent delta was expected and none appeared.

## The queue, nine arrivals

Read from #7284 to #7292 in one authenticated call, with bodies.

**Driven and shipped, two.**

**LogPulse** (`app.lovable.release-ripple-roadmap/logpulse`) - remote Streamable HTTP, keyless, **eleven** tools. The finding is the check: a deliberately non-conforming `CHANGELOG.md` came back with **1 error, 6 warnings and 1 tip**, each carrying a rule name and a line number, and a corrected copy with four findings auto-fixed. The defect is in that corrected copy - the date-format **error** survives it, so a pipeline that trusts the file ships something the same tool just called invalid. A live conversion of `sindresorhus/got` returned **100** releases and **40** breaking changes; the hosted changelog inventory, searched for six well-known products, returned **zero** records and two demonstration fixtures.

**Risk-Aware Trading Agents** (`io.github.jackson-cmd/risk-aware-trading-agents` **0.7.2**, MIT) - local stdio, installed with `uvx` and driven through **thirteen** calls. The finding is the referee: an `rsi2` experiment over 215 decision days returned **+6.1%** against SPY's **+10.6%**, an alpha of **-2.2%** a year and a **33%** probability that its Sharpe beats the index, and then a `leak_check` that reruns the strategy with every price and headline after three cut dates randomized - **65**, **119** and **173** decision days compared, identical decisions at all three, verdict pass. The frozen market is 719 trading days from 2024-01-02 to 2026-11-11, ships inside the package with a SHA-256 per record, and refuses a date outside its range.

**Held, with the owner named.**

**Mobster** (`dev.mobster/mobster`) is a **prior disposition**: the 7 November midday pass read it as iOS device control that needs macOS and `uv`, and a Mac with Xcode is not an MCP integration an operator installs from a chat client. **ZEUS Terminal** (`jackson-cmd/zeus-options-terminal`) comes from the same author as the shipped research harness and holds on a different ground: it answers only programs on the same computer, needs a self-hosted terminal running before the endpoint exists, and ships under **PolyForm Noncommercial 1.0.0**, so the licence rather than the capability decides it.

**The sixth wave of one publisher's fleet.** Five arrivals at 17:24Z to 17:33Z - `mcp-streaming-subscription-prices-by-country`, `mcp-tiktok-video-stats`, `mcp-amazon-top-reviews-scraper`, `mcp-private-company-funding-history` and `mcp-b2b-social-video-transcripts` - are one-tool Apify actors under the `mambalabsdev` namespace, each listing its tools without a token and needing an `APIFY_TOKEN` to call one. That is the standing Apify-actor ruling: 48 items across six waves from the same publisher, distribution rather than a data surface. The funding-history actor is the closest to business data and is the same company-funding slice already carried by the tracker class.

## 🆕 November 13, 2026 - Midday Sweep (1 New, 1 Guide)

A window flat to the raw count, every per-map count and the lastmod cutoff, where the delta came entirely from the queue and the feed - and the one guide shipped on a Bulgarian deadline chain reproduced by hand.

## 🆕 November 13, 2026 - Night Sweep (2 New, 2 Guides)

The previous pass in this series corrected the evening before it: the **1,817 keys** read as absent came back, all five named slugs were present in the following capture, and the per-map counts were established as the only reliable arrival signal on the mcpservers.org index.

## 🆕 November 12, 2026 - Evening Sweep (1 New, 1 Guide)

A composition change read correctly as a composition change, a Google Search Console calculator whose refusal was the finding, and one guide shipped at the keyless tier.
