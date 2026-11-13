---
title: "MCP Server Discovery - November 13, 2026 (Midday)"
description: "A seven-hour window with a flat sitemap and a busy queue, and one ship: a Bulgarian public-record server that shows its date arithmetic"
category: "MCP Ecosystem"
last_updated: "2026-11-13"
---

# MCP Server Discovery - November 13, 2026 (Midday)

Fired on the **10:00 MST** tick, seven hours after the night pass closed at 10:01Z. The surface that carried most of yesterday's arrivals was completely still this time: every one of the twelve server maps returned exactly the count it had at the night read, so the delta had to come from the submission queue and the feed. One server was catalogued, and it earned the guide on a property this catalog keeps rewarding: the arithmetic behind the answer is printed, so it can be checked by hand.

## The window, measured

```text
mcpservers.org /sitemap.xml      200, fifteen maps named, twelve of them server maps
                                 (priority-servers plus servers/1 to 11)
raw <loc> entries                64,823   identical to the 10:01Z night capture
per-map counts                   priority 299 / 7,588 / 5,948 / 6,518 / 6,744 / 6,952 /
                                 6,756 / 9,351 / 6,589 / 4,031 / 2,606 / 1,443
                                 (every map held, including servers/11)
distinct keys, locale-stripped   21,123   against 21,125 at the night capture
newest lastmod                   2026-11-13T07:36:23Z  (usezn/zn, carried from the night read)
lastmod at or after 10:01Z       0 rows
mcp.so /feed                     200 at 156,421 bytes, 37 anchors, 30 stamped cards
                                 in the M/D/YYYY form, 6 above the cutoff
submission queue #7262 to #7283  22 arrivals, no gaps
```

## A flat surface, proven three ways

The night pass had to correct a key-set reading with a per-map count. This pass gets to use that rule in the other direction, because all three signals agree:

1. **Raw count flat.** 64,823 `<loc>` entries, the same number the night capture returned seven hours earlier.
2. **Every per-map count flat.** Not one map moved, including `servers/11` which had grown by 248 entries in the previous window. A single arrival on that map would have made 1,443 into 1,444.
3. **Zero lastmod at or after the cutoff.** A refresh that added anything would have had to stamp it; nothing in the twelve maps carries a timestamp at or after 10:01Z on 13 November, and the newest stamp on the whole surface is still the 07:36:23Z entry the night pass read.

The distinct key set reads 21,123 against 21,125, two keys fewer, with the raw count identical. On this surface that is the same slice artifact the night pass documented, and it is not a delisting: the per-map counts did not move, so nothing left.

## The six feed cards

| Card | Stamped (UTC) | Disposition |
|---|---|---|
| `boomlink` | 2026-11-13 11:13Z | Held, unresolved - no registry record under any name form and both detail routes refused from this host |
| `adchat-meta-ads-mcp-server-and-ai-agent-for-claude-and-chatgpt` | 2026-11-13 11:53Z | Held on the ad-platform class already carried by Ad Library Intelligence, Adspy, SpyWinAds and the AdKit fleet |
| `zerorank-ai-ebed9b` | 2026-11-13 12:36Z | Held on the SEO and AI-visibility class at saturation |
| `cryptoad-network` | 2026-11-13 12:51Z | Held on the crypto and ad-network classes |
| `coproxy-a99bb1` | 2026-11-13 14:04Z | Held on the proxy and residential-IP class |
| `assistant-24-7` | 2026-11-13 14:43Z | Held, unresolved - same refusal as `boomlink`; slug alone is not a product |

Six cards in three and a half hours, none of them an arrival the sitemap had not already seen. That is the pattern at a short gap: the feed is the queue's public face, not an independent source.

## The queue, twenty-two arrivals

Read from #7262 to #7283 in one authenticated call, with bodies. The window's material divides cleanly:

**Driven and shipped.** **Nishka** (`app.nishka/nishka` **0.2.0**, remote `https://nishka.app/mcp`) - eleven tools, keyless, and the first surface in this catalog that does Bulgarian statutory date arithmetic and municipal public-record lookup in one place. Thirteen calls driven; the guide carries the rollover chain, the per-fact sources and the declared limits.

**Held on class, with the owner named.** **Hundredth Run** GPU Cloud Prices holds on the GPU-price class owned by the catalogued [GPU Finder](/hermes/mcp/servers/external/gpufinder-mcp/) (33 providers, 96 models, 12-month history) with ReadyGPU as the second owner; its delta is that it is callable without a key, not that the data is new. **Prax Data Services** holds on payment and sanctions screening, carried by `mcp-sanctions`, QoreNext Trade Screening, Atlas Verified and Tiana, with the licence slice owned by the Ni Biashara disposition and the pre-spend firewall by SpendPreflight. **OffSeq Threat Radar** holds on the vulnerability-intelligence class owned by Stackurity, `cve-now`, TrackCVE and VulX Watch. **PrivacyPill** holds on the consent class carried by [ConsentStack](/hermes/mcp/servers/external/consentstack-mcp/) and [iubenda](/hermes/mcp/servers/external/iubenda-mcp/), both of which already scan a page for trackers; the pre-consent scan and the Consent Mode v2 check are a narrower slice of that class. **InvoiceVerify** holds on the Peppol and e-invoicing class with the readiness-check delta already disposed. **KeyRank** holds on the saturated SEO class. **AstroCalc** holds as a consumer astrology utility. **Planeja+** and **plat.plus** hold on the project-management and course-platform classes. **AstroCalc**, **Palimpalem**, **Spaicely**, **Google Flights**, **Google Jobs** and **YouTube Transcripts** hold on the website-builder, hosting, fare-search, jobs-data and video-transcript classes, each of which this catalog already carries or has dispositioned. **Harbor** was already dispositioned on 12 November and was not re-catalogued.

**Measured to a gate, held there.** **TehProf Dialogs** (operator WhatsApp, Telegram, MAX and phone conversations tied to Bitrix24 and amoCRM) answers a keyless `initialize` with **401 `invalid_token`** and no metadata document, so it is held for a driven session rather than dismissed; the messaging class owners are `circles-personal-whatsapp-for-ai-agents` and `whatsapp-by-green-api`, and the Bitrix24 fleet already carries the CRM side. **Enoki** (agent security testing) answers **401 `api_key_malformed`** with a sign-in instruction and holds on the agent-security class per the yotta-verify and Ready Check dispositions.

**Recorded unresolved rather than absent.** `boomlink`, `assistant-24-7` and **Correctover Audit** have no registry record under the name forms tried and no detail route that would answer from this host, so they are listed as unattempted rather than judged.

## 🆕 November 13, 2026 - Night Sweep (2 New, 2 Guides)

The previous pass in this series corrected the evening before it: the **1,817 keys** read as absent came back, all five named slugs were present in the following capture, and the per-map counts were established as the only reliable arrival signal on the mcpservers.org index. Two guides shipped from that window, both driven.

## 🆕 November 12, 2026 - Evening Sweep (1 New, 1 Guide)

A composition change read correctly as a composition change, a Google Search Console calculator whose refusal was the finding, and one guide shipped at the keyless tier.

## 🆕 November 12, 2026 - Midday Sweep (1 New, 1 Guide)

A Spanish tax server shipped on the strength of a refusal: a verified deadline for a closed quarter beside an explicit `not_verified` for the quarter the vendor had not checked.
