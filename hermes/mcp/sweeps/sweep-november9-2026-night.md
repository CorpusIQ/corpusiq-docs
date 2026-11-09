---
title: "MCP Server Discovery - November 9, 2026 (Night)"
description: "Night sweep at a six-hour gap: both directory surfaces flat, sixteen queue arrivals, and two public-record lead connectors catalogued."
category: MCP Ecosystem
added: 2026-11-09
last_updated: 2026-11-09
source: "the mcpservers.org thirteen-sitemap canonical, the mcp.so feed read twice (plain and cache-busted), and the chatmcp/mcpso submission window #6970 to #6985"
tags: ["mcp server", "model context protocol", "discovery", "sweep", "november 2026"]
---

# MCP Server Discovery - November 9, 2026 (Night)

Fired on the **03:00 MST** tick, six hours after the evening sweep. Both directory surfaces came back flat and the whole window is sixteen submissions, of which two are catalogued. Both of those are the same pattern from the same publisher: one public government file, reshaped into a ranked list for one trade.

```text
Canonical:   20,204 distinct server URLs from 63,644 raw <loc> entries across 13 maps
             (0 additions, 0 removals against the 05:06Z evening capture)
Feed:        145,250 bytes plain, 145,283 cache-busted, same newest card
Queue:       #6970 to #6985, 16 issues, no gaps, all arrivals
Catalogued:  2 servers, 2 guides
Evaluated:   16 queue arrivals plus 1 fresh feed card
```

## The window, measured

The thirteen server maps, `servers/1.xml` through `servers/11.xml`, `priority-servers.xml` and `remote-mcp-servers.xml`, returned **63,644** raw `<loc>` entries and **20,204** distinct server URLs after the inline locale prefixes were stripped before the `/servers/` subset was taken. That is the same raw count and the same distinct count as the evening capture, and the set difference is **0 additions and 0 removals**. The flat result is credible here because both numbers reconcile rather than one being held constant by hand.

The mcp.so feed was read twice. The plain read returned **145,250** bytes and the cache-busted read **145,283**, with the same newest card, `platemark` at `2026-11-09T06:14:44Z`. Below it sits `dsers-official-mcp-server` at `2026-11-09T03:21:17Z`, which the evening sweep already catalogued, and then the November 8 cohort that pass dispositioned. The eighteen-card bulk publish the evening sweep saw stamped `2026-11-09T08:00:01Z` to `08:00:18Z` was not on this read at all, which fits the scheduled-publish pattern recorded on November 7 rather than a set of listings that came and went.

The queue carried **#6970** to **#6985**, sixteen numbers with no gaps, every one an arrival and none a listing update.

## Catalogued: the public-record lead pattern, twice

Both finds come from the queue and both are read-only connectors that take one published government file and rank it around a ZIP, for one trade with a purchase behind it.

- [newlyraised MCP - SEC Form D and SBA Raise Leads](/hermes/mcp/servers/external/newlyraised-mcp/) - remote Streamable HTTP at `https://app.newlyraised.com/mcp`, OAuth 2.1 with PKCE, DCR and Client ID Metadata Documents, registry `com.newlyraised/newlyraised` **1.0.0**, submission `#6975`, **5** read-only tools over six US metros. A keyless `initialize` answers **401** with a protected-resource document naming scope `newlyraised` and a full authorization-server document, so the tier is documented and gated rather than driven. It joins SEC Form D filings to SBA 7(a) and 504 approvals of a million dollars or more, with the vendor stating its own freshness: a Form D daily index covering November 2 to 6, fetched the morning of November 7, and an SBA file dated October 30 carrying approvals through September 30, republished quarterly. The class neighbours are all adjacent and none overlaps: [Mamba Funding Investor Record](/hermes/mcp/servers/external/mamba-funding-investor-record/) is a record lookup for one named company, [AllClear Lending](/hermes/mcp/servers/external/allclear-lending-mcp/) works the borrower's side of commercial credit, and [SpendQuery](/hermes/mcp/servers/external/spendquery-mcp/) covers federal awards. This is the acquisition side read as a market.
- [StandbyBrief MCP - CMS Citation Leads for Contractors](/hermes/mcp/servers/external/standbybrief-mcp/) - remote Streamable HTTP, registry `com.standbybrief/standbybrief` **1.0.0**, submission `#6972`, **6** tools over CMS's nursing-home fire-safety inspection file. A keyless `initialize` on the app host answers **401** with a protected-resource pointer and the scope `standbybrief`. The product joins three citation tags to three trades: K918 for emergency power, which is the generator dealer, and K353 plus K345 for sprinklers and fire alarms, which are the two contractors. What makes it a sales instrument rather than a report is the correction date on the row, because a facility under a correction deadline is a facility that has to spend money. The published apex route carried the parent company's website rather than an MCP handshake at the time of this pass, so the guide documents the app host that answers and states the routing gap as measured.

## Held, with the reason each one was held

**erateradar, the third sibling, is held on a measurement rather than a judgement.** Submission `#6971` publishes `https://erateradar.com/mcp`, registry `com.erateradar/erateradar` **1.0.0** agrees, and the app host answers the handshake with a **403** whose JSON-RPC message is `Use https://erateradar.com/mcp`, while that apex route returns the parent company's website instead of an MCP response. The backend is live and its own OAuth documents are published, but no client can connect through either route today, so the entry waits for one route to answer. The class it would enter is empty here: zero E-rate coverage in the catalogue, and the vertical is school and library network bids for IT and cabling providers.

The rest of the window, dispositioned once:

- **mambalabsdev fleet, #6980 to #6985** (Zillow listing details, US import records buyer finder, site crawler links and tables, MCP server change and health monitor, Amazon price and stock tracker, Google Trends scraper): six npm packages wrapping Apify actors, each one tool, registry under `com.mambabuilt`. Held on the standing Apify-actor hold class and the October 7 Mamba Labs fleet ruling, both of which this catalogue already carries with the five GTM standouts catalogued and the remainder held.
- **Plainmail** (`dev.plainmail/mail`, #6970): agent mailboxes on the user's own domains with MX, SPF, DKIM and DMARC written through the DNS host. Held on the saturated agent-email class carried by Mektup, Loops, Lumail, assistantmail, Voidmail and GhostPaw, notwithstanding that DNS provisioning is the one part of that loop the others do not do.
- **CyberRedd** (`com.cyberredd/cyberredd`, #6974): Reddit community, post, brand-mention and share-of-voice search behind OAuth. Held on the social-data class per ScrapeAtlas and the social-listening class per Octolens.
- **QIE Wallet** (`digital.qie/wallet`, #6977): six keyless read-only tools over QIE chain balances, transaction status, tokens and name resolution. Held on the crypto-rail class carried by Base Payment Assurance, Brasil Data and AICryptoVault.
- **FAI Legal Research** (`site.failegal/fai-legal`, #6978): 19,771 statute sections and 188,602 reported Pakistani judgments behind a personal token link. Held on the regional legal class at saturation, with TaiLexi the owner and the LEGAION, aka-recht and Specter Cite trio the precedent.
- **Assura** (`io.github.assura-lang/assura`, #6973): six stdio tools that check Assura contracts with Z3 and CVC5. Held on the developer-utility class; nothing here is a business data surface.
- **Selan MCP Extension** (#6976): a Chrome extension that lets a client use the person's own signed-in tabs, scoped to a tab group and an allowlist that starts empty. Held on the browser-automation class carried by Cotlet, Veilus and Full Self Browsing.
- **JiZhiMCP** (`io.github.alanwang100/jizhineng-mcp`, #6979): 21 gateway tools plus a hash-chained cross-agent settlement ledger. Held on geography and on the agent-payments class.
- **platemark**, the only fresh feed card: template slots rendered into finished images. Held on the media-generation class carried by Evergen, SpicyAPI, Tanvo and North Noir.

## Core listing check, measured

The fresh canonical carries `/servers/corpusiq-io` and `/servers/corpusiq/corpusiq-docs`. mcpservers.org `/all` answered **403** by edge policy, the standing condition since November 4 rather than a delisting. All four direct mcp.so slugs answered **404** (`corpusiq`, `corpusiq-io`, `corpusiq-mcp`, `io.corpusiq`), so that listing remains absent. Both Glama routes answered **301** to their query pages, the routing change recorded on November 8 and carried forward as a redirect rather than read as a removal.

## Frequently asked questions

### Why does a flat window still produce a sweep report?

Because the two catalogued servers arrived on a surface that no sitemap carries. mcpservers.org indexes a different population from mcp.so, so a submission filed on mcp.so can be a genuinely new listing while both canonical captures are set-identical. The report records the flat measurement so the next pass knows the wave was zero rather than unmeasured.

### What does "documented and gated rather than driven" mean here?

Both new entries answer a keyless handshake with an OAuth challenge and publish their metadata documents, which proves the endpoint is live and describes the scopes. Neither has a keyless tool list, so every tool name in the guides comes from the vendor's own documentation and the submission body. Where that is the source, the guides say so rather than implying a live call.

### Why hold a connector whose only problem is a wrong URL?

Because a catalogue entry that a reader cannot connect is worse than no entry. The app host answers today, so the guide ships with the measuring note attached and the vendor's routing corrected in public. The sibling whose backend refuses callers in favour of a route that does not answer waits for a later pass.
