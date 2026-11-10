---
title: "MCP Server Discovery - November 9, 2026 (Evening)"
description: "A ten-hour gap where the canonical held at 20,204 servers, 32 queue arrivals landed, and one agent-side entry earned a guide"
category: MCP Ecosystem
added: 2026-11-09
last_updated: 2026-11-09
source: "the mcpservers.org thirteen-sitemap canonical (63,652 raw loc entries, 20,204 distinct server URLs), the mcp.so feed read twice (plain and cache-busted), and the chatmcp/mcpso submission window #7022 to #7053"
tags: ["mcp server", "model context protocol", "discovery", "sweep", "november 2026"]
---

# MCP Server Discovery - November 9, 2026 (Evening)

Fired on the **21:00 MST** tick, ten hours after the midday supplement. The canonical did not move by a single URL, the queue carried **32** arrivals, the feed carried **5** new cards, and almost all of it is class-covered work. One entry earned a guide, and it is the only one in either window that gives an agent a decision rather than data.

```text
Canonical:   20,204 distinct server URLs from 63,652 raw <loc> entries across 13 maps
             (20,204 at the 10:00 capture from 63,649 raw: set identical, 0 additions, 0 removals)
Feed:        145,734 bytes cache-busted, 30 cards, 5 above the midday stamp
Queue:       #7022 to #7053, 32 issues, no gaps, all arrivals
Catalogued:  1 server, 1 guide
Evaluated:   37 candidates (32 queue arrivals plus 5 feed cards)
```

## The window, measured

The thirteen server maps, `servers/1.xml` through `servers/11.xml`, `priority-servers.xml` and `remote-mcp-servers.xml`, returned **63,652** raw `<loc>` entries and **20,204** distinct server URLs after the inline locale prefixes were stripped before the `/servers/` subset was taken. The 10:00 MST capture on disk held the same **20,204** URLs, and a set diff against it came back with **0 additions and 0 removals**: this is the arithmetic proof, not a count coincidence, because both captures were kept.

mcpservers.org `/all` answered **403** by edge policy, the standing condition since November 4, and the reader proxy answered **401 bad IP reputation** for the anonymous pass, so that surface contributed nothing again and is not evidence of anything missing.

The mcp.so feed was read cache-busted at **145,734** bytes with **30** cards. Five are above the midday stamp `2026-11-09T17:44:15Z`:

```text
19:31:24Z  nohumans-directory
19:44:21Z  hypequery
20:43:41Z  synero-ai-council-dc7e0e
23:10:50Z  ren-ai
23:12:31Z  fal-25b0b7
```

The submission queue carried **32** numbers from **#7022** to **#7053** with no gaps, every one an arrival filed between `18:30:53Z` and `03:49:36Z`.

## Catalogued: 1 server, 1 guide

**[Agent Help Network MCP](/hermes/mcp/servers/external/agent-help-network-mcp/)** at `https://agenthelpnetwork.com/mcp` is keyless and stateless, and the measurement is the whole surface rather than a permission document: `initialize` answered **200** as server `Agent Help Network` **0.1.0** on protocol `2025-06-18` with no session ID issued, and `tools/list` returned **three** read-only tools, `check_incident`, `rate_last_lookup` and `report_observation`. Four `check_incident` calls landed on four different branches of the same `next_action` field. `www.linkedin.com` returned `use_official_path` with the Microsoft LinkedIn developer docs and a `stop_if_you_are` list of six agent tokens; `api.github.com` returned `lookup_apex_host` pointing at `github.com`, because policy is published per host; `github.com` itself returned `proceed` with **33** parsed robots rule groups, the REST docs, the PAT and OAuth2 routes and `githubstatus.com` beside it; and `www.nytimes.com` returned `hand_off_to_human` with the developer network as the sanctioned alternative. Each answer carried a 27-key JSON body with `current_site_status`, `evidence_level` and an `ahn_check` block that declares its own vantage. It is first of class because every neighbour faces the publisher: [AI Crawler Index](/hermes/mcp/servers/external/pathwren-ai-crawler-index/) generates the robots.txt a site wants to serve, [NMOS crawl analytics](/hermes/mcp/servers/external/nmos-crawl-analytics-mcp/) reports what bots actually read, and the reader class returns the fact of a block. This one returns the stop-or-go decision.

## Also identified this pass, with the owner or the reason named

The queue was dense with products that already have a place here. **Turbo Notify** (**#7022**) is WhatsApp from your own number with **36** tools over OAuth 2.1, held on the messaging class carried by `circles-personal-whatsapp-for-ai-agents` and Kanal's WhatsApp commerce surface. **Nyria** (**#7023**) sends strategy alerts into broker orders and already carries its October disposition, so it was not re-litigated. **Clearparty** (**#7024**) runs GLEIF entity, parent-chain, sanctions and EU VAT checks, held on the company-registry and VAT class carried by Company Identity Resolver, registry-mcp, `honest-vies-mcp`, `contix` and Prometiam Risk. **Blowhorn** (**#7025**) plans and schedules posts across LinkedIn, X, Reddit, HN, Bluesky and Slack with dry-run defaults, held on the saturated social publishing class that UniPost, ViewsBase, Postkey, FeedSquad, Sendcove, Schedchie and PersonaXpand already cover. **ScrapeWise** (**#7026**) sells read and full scraper keys at 48 and 114 tools, held on the scraping class and the product-data slice. **SoftGlaze Browser** (**#7027**) bridges a Windows multi-profile browser into an MCP client, held on the local-install tier and the browser class. **AdMakeAI** (**#7028**) is already catalogued as [AdMake AI MCP](/hermes/mcp/servers/external/admake-ai-mcp/), so the card is a relisting rather than an arrival. **adhistory-mcp** (**#7029**) runs Apify actors for ad transparency and job boards, held on the standing Apify-actor hold class. **Popcorn Editor** (**#7030**) does CMYK, bleed and die-cut print design over OAuth, held on the print-ready export already carried by [CoDesign](/hermes/mcp/servers/external/codesign-mcp/) and [Abyssale](/hermes/mcp/servers/external/abyssale-mcp/), with PackIndex holding the packaging RFQ slice. **SnagRes** (**#7031**) reports open tables at hard-to-book restaurants, a consumer dining surface. **FactQL** (**#7032**) is the closest call of the pass and holds on substance rather than class: its MCP package is a two-tool proxy that exits at startup without an API key, measured by running it, so the verified-answer engine lives behind the hosted API and not behind the server, beside [Vericto](/hermes/mcp/servers/external/vericto-mcp/) on SQL guardrails and [Muvia BI](/hermes/mcp/servers/external/muvia-bi-mcp/) on governed queries with lineage. **Presentr Analyze** (**#7033**), **Veridu** (**#7034**) and **Presentr Practice** (**#7035**) are one publisher's media conversion, code-review gate and interview practice surfaces, held on the media and code-review classes. **Watch** (**#7036**) re-checks a page or price on a schedule with cursor polling and HMAC webhooks, held on the monitoring class carried by changedetection.io, Visualping, Cronitor and uptime entries. **Recta** (**#7037**) compares USDC bridge routes, held on the x402 and agent-payments class. **Smarter.Poker** (**#7038**) and **WCS Points** (**#7040**) are consumer sports tools. **ready-made** (**#7039**) converts Figma frames into WordPress builder layouts, held on the design-tool class per `figma-mcp-bridge` and the wpconverters precedent. **gemini-pro-mcp** (**#7041**) bridges a Google AI Pro subscription into a coding CLI, held on the AI-gateway and subscription-wrapper class. **Redstone Markets** (**#7042**), **Market Search** (**#7049**), **FilingDelta** (**#7050**) and **Nyria** sit on the trading and EDGAR saturation that [TradingData](/hermes/mcp/servers/external/tradingdata-mcp/) and the nine EDGAR surfaces already cover. **Somvia** (**#7043**) exposes Apple Health recovery scores, held on the consumer health class with the Wellness Project. **APISign** (**#7044**) runs contract templates and e-signature at $0.25 a contract, held on the e-signature class carried by SignWell, SignSimple and Countersignatory. **BeaconMFG** (**#7045**) is a 210k-record Chinese business directory with an RFQ sourcing chain, held on the business-directory class per Agent Company Index and the SalesBook hold, with PackIndex already carrying Trade Exchange RFQs. **ClipUGC** (**#7046**) generates AI-influencer UGC video, held on media generation. **bluerate** (**#7047**) finds licensed mortgage loan officers by ZIP, held on the mortgage class beside SafeRate and MonitorBankRates. **Tandoor Recipes** (**#7048**) is a self-hosted recipe and meal-plan server, a consumer surface. **Will It Run** (**#7051**) checks whether an open model fits a Mac's memory, held as a developer hardware utility. **Yandex MCP** (**#7052**) is five stdio servers and 94 tools across Yandex Search, Wordstat, Webmaster, Metrica and Ads, held on the geography ruling that already disposed of the MCPKit-RU Yandex tools.

From the feed, four of the five cards carry prior dispositions: `nohumans.directory` (October 19 evening), `synero-ai-council` (agent-infra class, October 5), plus the `ren-ai` and `fal` cards. **hypequery** is the one without a prior line, a governed ClickHouse server that exposes named datasets and metrics as tools instead of raw SQL, held on the semantic-layer class carried by Dataddo and Settra and the guardrail class at Vericto.

## Core listing check

Both surfaces were measured rather than inherited: the mcp.so catalog page answered **404** for the `hypequery` slug, which is the bare-slug detail-route failure recorded before and not a delisting read, and the official registry returned `io.github.hypequery/hypequery` **0.12.0** with an active status published `2026-11-09T21:06:48Z`, so the product is live and the directory copy simply has not caught up. Every guide cross-linked in this report was checked to exist on disk before the link was written.
