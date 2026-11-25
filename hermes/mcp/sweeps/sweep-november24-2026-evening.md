---
title: "MCP Server Discovery - November 24, 2026 (Evening)"
description: "A canonical flat to the byte, and three ships from the feed and the queue: buyback economics, a translation workspace, and a changelog with a real OAuth chain."
category: "MCP Ecosystem"
last_updated: "2026-11-24"
---

# MCP Server Discovery - November 24, 2026 (Evening)

Fired on the **21:00 MST** tick, ten hours after the 18:00Z supplement stored its baseline. The directory did not move at all: the twelve numbered server maps returned the same **37,599** raw `<loc>` entries, the distinct key set is **23,892 on both bases** under one normalizer, and **not one** of **34,152** `lastmod` rows sits at or after the cutoff, the newest stamp being **17:53:49Z** in both captures. A platform that has not stamped a page in ten hours has not published one. All three ships came from the surfaces that do not depend on the sitemaps, the feed and the submission queue.

## The window, measured

```text
mcpservers.org /sitemap.xml   sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12         37,599   identical to the 18:00Z capture, per map
  servers/1  ..... 4,129     servers/7  ..... 5,878
  servers/2  ..... 2,527     servers/8  ..... 2,739
  servers/3  ..... 2,945     servers/9  ..... 2,606
  servers/4  ..... 3,200     servers/10 ..... 2,575
  servers/5  ..... 3,290     servers/11 ..... 2,509
  servers/6  ..... 2,891     servers/12 ..... 2,310     sum 37,599 exact
distinct keys, maps 1-12     23,892   identical to the 18:00Z capture
stored baseline key file     23,906   +14, all locale-form artefacts (see below)
lastmod, server maps         34,152 stamped rows
  at or after 18:00Z         0 rows
  newest stamp, both passes  2026-11-24T17:53:49Z
priority-servers.xml         252 raw   union after normalisation 23,927
remote-mcp-servers.xml        15 raw
mcp.so /feed                 200, 160,044 bytes, 44 anchors, 30 stamps
  cards above the cutoff     4
submission queue             #8005 - #8035, 31 filings
```

The like-for-like proof is arithmetic rather than a count. Both captures were re-parsed with **one** key function, and the set diff is **0 additions and 0 removals**. The stored baseline file reports **23,906** keys because the earlier extractor kept the locale prefix when it preceded `/servers/`, producing fourteen keys that read `de/servers`, `es/servers`, `fr/servers`, `hi/servers`, `id/servers`, `ja/servers`, `ko/servers`, `pt-BR/servers`, `ru/servers`, `th/servers`, `tr/servers`, `vi/servers`, `zh-CN/servers` and `zh-TW/servers`. Fourteen keys, no products, and a normalisation gap rather than a removal count.

## Shipped (3)

**WeightedShares** (#8035) at `https://weightedshares.com/mcp`, `weightedshares-sec-mcp` **1.0.0**, **keyless 200** with **five** tools, and all five driven. The answer it gives is the one a board deck leaves out. Apple's five-year window shows `cashBuybacksUsd 439,002,000,000` against `sbcExpenseUsd 58,211,000,000`, so standard FCF of **554,657,000,000** becomes **True FCF** of **496,446,000,000** at a **24.06%** margin, while the diluted count still falls **12.72%**. The control is independent: the FY2026 row's `86,390,000,000` of buybacks matches SEC `companyconcept` `PaymentsForRepurchaseOfCommonStock` for CIK **0000320193** to the dollar, and FY2025's `90,711,000,000` matches too. The screen is where the insight gets sharp: **GM** retired **-32.52%** of its shares in five years while stock compensation took **6.80%** of the buyback dollars, against **MSFT** at **46.26%**. Two gaps recorded: foreign issuers return nulls with a 20-F ADS notice rather than zeros, and a non-flagship window can end two fiscal years back (`TSM` reads `FY2019-FY2024`).

**Transept** (#8016) at `https://app.transept.ai/api/public/v1/mcp`, `transept` **1.0.0**, and the widest discovery surface of the day: keyless `initialize` **200** and a keyless `tools/list` returning **42** tools. Execution is gated, and the refusal is the defect worth recording: a JSON-RPC error **-32001** with the fix in the message (*"mint one under Settings -> Developer"*) and **no `content` block and no `isError` field**, so a client that renders only results shows nothing at all. The server's own instructions carry the design: documents split into blocks, workflows of translate and proofread steps, `run_estimate` free before `run_start` needs `confirm: true`, estimates that are ceilings with the unused reserve released, and review gates that answer `gate_pending` with a `finding_count`. `strings_reimport` returns `delta_block_ids` so a re-submitted corpus translates only what changed. MCP starts at **Lite, EUR 9 / USD 10** for 25,000 credits; a credit is one source word and Pro mode costs three.

**ReleasePad** at `https://pro.releasepad.io/mcp`, the window's second feed card, shipped on a complete OAuth chain rather than a driven tool list. `initialize` refuses **401** with `WWW-Authenticate: Bearer resource_metadata="https://pro.releasepad.io/.well-known/oauth-protected-resource"`, that document answers **200** with scopes **read** and **write**, and the RFC 8414 document on the same host answers **200** with dynamic registration, PKCE **S256**, refresh grants and `none` as a token-endpoint auth method. Two constraints recorded because they cost afternoons: the only response mode is **`query`**, and `/.well-known/openid-configuration` is a **404 HTML page**, so there is no OIDC layer. The catalogue value is the entitlement: **MCP access requires Pro at USD 35 a month per product**, the free plan has 20 posts and no MCP, and every post starts as a draft with read-only or full access chosen at consent.

### Why ship these three?

Because each answers a question the catalogue could not answer before, and each was measured rather than described. **No entry carried buyback-versus-stock-compensation arithmetic before this pass**, and none carried a filed-dollar control against SEC XBRL. **No entry carried a translation workspace** where a review step has a price and translation memory is a first-class tool. And no entry carried a **changelog** surface at all, which is the page every SaaS buyer reads before a demo.

### What did this pass not do?

No call was made inside Transept or ReleasePad, so neither returned schema is measured and both guides say so rather than implying a drive. The `lastmod` window is empty, so no arrival date could be triangulated against a stamp for anything in this window. And the feed detail routes answered **403** direct and **401** through the reader proxy for all four cards, so three cards were resolved through the official registry and the product pages instead of the directory page.

## Also identified this pass (not catalogued)

**AgentsRank** (feed, 23:58Z) is the most interesting hold: a keyless `initialize` **200** and **33** tools across an agent hub with job posting, worker search, reputation, messaging and a feed, at `https://agentsrank.ai/api/mcp`, registry `ai.agentsrank/agentsrank` at **2.1.0** through **2.4.0**. It holds on audience rather than quality: the catalogue's reader is a business operator hiring data and a worker marketplace for AI agents is a different market, and the surface it needs already exists as the agent-tooling lane. **Sports DataFeeds by Rolling Insights** (feed, 21:29Z) at `https://mcp.datafeeds.rolling-insights.com/mcp` answers **401** with a plain JSON-RPC body and **no `WWW-Authenticate`**, and sports data is carried by **Vublox Sports** and the keyless odds surface. **Energieausweis Express** (20:21Z) is held on the **EcoExperten Energieausweis** entry that already orders German energy certificates.

From the queue, thirty-one filings and the reasons recorded rather than ranked. **FilingSignal** (#8031) and **QuantisNow** both sit on SEC EDGAR, which `sec-edgar-mcp` already carries. **Kling AI** filed three times (#8024 and #8030 global, #8026 China) and video generation is carried by the ad-generation entries. The **BiteFoundry** fleet (#8027 Atlassian, #8028 Teams, #8029 Obsidian) is class-carried three ways by the Atlassian Rovo and Confluence entries, the Teams surface and the Obsidian vault entry. **SiteBrief** (#8023) reads website contacts, pricing and `llms.txt` and belongs to the company-enrichment class. **RoleSignal** (#8022) joins the hiring-intelligence class. **StackScope** (#8021) is already catalogued as `external/stackscope-mcp`. **AdPulse** (#8020) sits on ad-library intelligence. **AY Inbox** (#8019) is a hosted cold-email platform on the **Coldrig** and **Emailchaser** shelf, and **AY Rank** (#8018) on the saturated SEO and GEO audit class. **looot** (#8017) already carries `external/looot-mcp`. **Literess** (#8015) is class-carried by **Scrivener** and a second manuscript tool, and the vendor bundles it inside Transept where it appears as a tool rather than a server. **UniRoute Media** (#8033) joins the media-generation aggregators, **Kiko** (#8034) the creator-discovery class, **Soycasero** (#8009) the landlord ledger **Utleio** already owns, **Thastock** (#8007) and **Financial AI** (#8006) the stock-research and investment-intelligence classes, **Tesseract** (#8010) media generation, **ClickAndSay** (#8013) the visual website-feedback class, **UK Drops Feed** (#8012) collectibles retail, **VibeHub** (#8008) and **CursorMesh** (#8005) developer tooling, and **Been There** (#8011) an agent-only knowledge exchange with no operator surface. **Singularity Dot Com** (#8014) is a dating site for agents: recorded, not catalogued.

## Listings

Re-measured on the four surfaces this pass. **mcpservers.org LISTED**: `servers/corpusiq-io` and `servers/corpusiq/corpusiq-docs` both sit in `servers/5.xml` of today's capture, which is the evidence that matters because the detail page answers **403** by edge policy. **mcp.so LISTED**: `/servers/corpusiq-docs` answered **200** at **857,219** bytes with **10** corpusiq mentions. **Glama LISTED**: `/mcp/connectors/io.corpusiq/multi-source-mcp` answered **200** with **4** mentions. **Smithery LISTED** on the direct record route: `registry.smithery.ai/servers/<publisher>/Cprusiq` returned the record with `displayName CorpusIQ`. No submission was made, because nothing was unlisted.
