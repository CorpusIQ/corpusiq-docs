---
title: "MCP Server Discovery - November 19, 2026 (Night)"
description: "A flat six-hour window on both directories, nineteen queue arrivals, and a tariff server that reads the schedule, the rulings and the paid rate."
category: "MCP Ecosystem"
last_updated: "2026-11-19"
---

# MCP Server Discovery - November 19, 2026 (Night)

Fired on the **03:00 MST** tick, six hours after the evening sweep closed at **04:05Z**. Both directory surfaces came back flat by measurement rather than by assertion, the feed carried one card above the cutoff, the submission queue carried nineteen arrivals, and one of them answers the half of a duty question this catalog had only ever answered from a calculator.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          66,668   IDENTICAL map for map to the 04:05Z capture
  servers/1  ..... 7,588     servers/7  ..... 9,351     sums to 66,668 exactly
  servers/2  ..... 5,949     servers/8  ..... 6,590
  servers/3  ..... 6,518     servers/9  ..... 4,024
  servers/4  ..... 6,744     servers/10 ..... 2,608
  servers/5  ..... 6,954     servers/11 ..... 2,637
  servers/6  ..... 6,756     servers/12 ..... 949
priority-servers.xml          299 raw,  34 distinct keys
remote-mcp-servers.xml         15 raw,   1 distinct key (clockwise)
distinct keys, twelve maps    22,720 against 22,720  = 0 additions, 0 removals
distinct keys, union basis    22,755  (twelve maps + priority + remote)
lastmod rows at or after the cutoff   0
mcp.so /feed                  200, 157,051 bytes, 30 stamps, 1 card above the cutoff
                              (kollguard 11/19 05:29 AM UTC)
submission queue              #7630 to #7648, nineteen arrivals, bodies in one call
```

Three readings agree: the raw counts are identical per map, the distinct key set did not move on the comparable twelve-map basis, and no `lastmod` row was stamped at or after the cutoff. A flat window is a finding here, not an absence of work.

## What shipped

One server, one guide, driven end to end without a credential.

- **[htsapi.dev](/hermes/mcp/servers/external/htsapi-mcp/)** at `https://htsapi.dev/mcp`, *htsapi* **1.0.0**, protocol **2025-06-18**, stateless with no session id issued, **eight** tools of which **seven** are keyless and were exercised across **eleven** `tools/call` requests. The registry record `dev.htsapi/mcp` **1.0.0** was published **2026-11-19T07:10:50Z**, twenty seconds before the queue entry was filed.

  The product is the other half of [Tariff Monitor](/hermes/mcp/servers/external/tariff-monitor-mcp/), which prices a stacked duty on ten-digit lines. htsapi serves the sources that decide the line: the schedule one level at a time (all **22** sections with no argument, **129** lines under three subheadings on **6404**), the legal notes verbatim (chapter 64's exclusions, the definition of rubber and plastics, the greatest-external-surface-area rule, the *sports footwear* limit), the CBP rulings corpus searchable by meaning (*led camping lantern* returned three rulings at **0.736** top similarity with each ruling's status and the product description CBP examined), the same corpus by code (**719** current rulings under **6403.99** against **1** moved away), and the Census paid rate (**10.5** percent statutory against **29.8 / 33.0 / 34.7** percent actually paid by Chinese importers on **6404.11** across three months).

  Four limits were recorded rather than smoothed: Chapter 99 lines are refused by `lookup_hts_code` with a pointer to `importers_paid`; an eight-digit code in `importers_paid` falls back to the **HS6** group with `rate_pct: null` and the numbers inside `months`; a heading carries no single rate; and `classify_product` refuses at one credit. The vendor's own legal posture is in the guide, including the CBP ruling about unlicensed classification beyond six digits.

## What was held

Eighteen candidates, each with the gate or the class owner named.

| Arrival | Held because |
|---|---|
| KollGuard (feed, 05:29Z) | read-only SOC 2, HIPAA and AI agent compliance workspace, class carried by ISMS Copilot |
| Enterprise Ego (#7648) | `401` with a complete protected-resource document and a `memory` scope, but an administrator must connect a company's Claude Enterprise, ChatGPT Enterprise or M365 Copilot, personal plans excluded, so no surface to measure |
| Dripod (#7646), Drisp (#7639) | one publisher, Drint, already dispositioned on its packaging-mockup entry; mockup renderers with watermark limits |
| Vitrine Studio (#7647) | App Store screenshot editor running inside a desktop app over stdio, Screenies precedent |
| Mirasim Computer Use (#7645) | computer-use class carried by ShadowCursor and Computer Use Turbo |
| network-xray (#7644) | read-only network-lab tooling for containerlab and netlab state files |
| Greenlit (#7643), Tare (#7642), Crumple (#7641) | one priberry publisher: vulnerability scanning (TrustScan class), FinOps spend analysis (costory, inferenceindexer), agent-security sandbox |
| Learn AI with Yaakov Tzedek (#7640) | dev-content class carried by PromptQuorum |
| Slim Chance (#7638) | consumer weight-trend statistics, wellness class |
| SanasiniAI (#7636) | OAuth over Shopee and TikTok Shop sellers, class covered by Nexscope and Trenz |
| unlam-mcp (#7635) | one-university LMS vertical |
| Adanos (#7634) | stock and ETF sentiment, covered by the filings and sentiment cohort |
| Strategy Lab (#7633) | Indian backtesting behind a per-user key, quant saturation carried by fAlpha and ValuEdge |
| Amberflip (#7632) | offline file conversion, RelayPDF precedent |
| KWeather (#7631) | Korean weather behind an API key, weather class |
| Vaaya (#7630) | agent wallet over 4,400 paid endpoints, x402 class carried by TollNode and AgentLedger |

KollGuard's detail route was read from the directory card rather than from the product, so it is recorded as a class hold rather than a driven evaluation. `/all` was not re-read: **403** by edge policy, the standing condition since 4 November.

## Counts

```text
canonical            66,668 against 66,668    0 raw change
distinct keys        22,720 against 22,720    0 additions, 0 removals
lastmod rows above cutoff             0
feed                 1 card above the cutoff, 0 shipped
queue                19 arrivals, 1 catalogued and 18 held
guides               1 added
```
