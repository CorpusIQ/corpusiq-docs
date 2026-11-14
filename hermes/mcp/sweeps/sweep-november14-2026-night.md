---
title: "MCP Server Discovery - November 14, 2026 (Night)"
description: "An ingestion wave of 225 new keys that is not 225 products, two feed cards, nine queue arrivals, and two servers shipped on what they can actually do."
category: "MCP Ecosystem"
last_updated: "2026-11-14"
---

# MCP Server Discovery - November 14, 2026 (Night)

Fired on the **03:00 MST** tick, six hours after the midday-supplement capture at 04:01Z. The directory moved by **225 new keys** and nearly all of them are pages being ingested rather than products arriving; the feed carried **two** cards and the queue **nine** submissions. Two servers ship, and both of them are the first of their kind here: a European print-and-mail service that prices a letter before you write it, and a Sharia compliance screen that publishes every verdict change with its date.

## The window, measured

```text
mcpservers.org /sitemap.xml      200, fifteen maps named, twelve of them server maps
raw <loc> entries, maps 1-11     65,013   against 64,760 on the Nov 13 21:03 capture (+253)
per-map counts                   7,588 / 5,948 / 6,518 / 6,744 / 6,952 / 6,756 /
                                 9,351 / 6,589 / 4,030 / 2,607 / 1,930
per-map movement                 servers/11 1,677 to 1,930 (+253), ten maps held exactly
distinct keys, locale-stripped   21,322   against 21,131 (+191)
set diff                         225 added, 34 absent = a re-shard inside an ingestion wave
URLs per surviving key           3.05     against 3.08 on the prior capture
newest lastmod                   2026-11-14T08:28:00Z (forgemeshlabs/utility-grid-mcp)
lastmod at or after 04:01Z       298 rows, 95 distinct listings, 90 of them already listed
mcp.so /feed                     200 at 155,460 bytes, 37 anchors, 30 stamped cards
                                 2 above the cutoff: mojobase 07:28Z, vantage 05:36Z
submission queue #7319 to #7327  9 arrivals, no gaps, read with bodies
```

## 225 new keys, and almost none of them are products

The twelve-map total stated at the 21:03 capture was **65,059**. This capture read the eleven numbered maps only and returned **65,013**, which is **+253** against the **64,760** those same eleven carried on the prior capture; the 299 entries that make up the difference are the `priority-servers` map, which lives at `/sitemaps/priority-servers.xml` rather than `/sitemaps/servers/N.xml` and was not re-read here. The eleven counts sum to **65,013** exactly, so nothing is double-counted inside the capture, and the whole of that +253 sits in `servers/11` (1,677 to 1,930). The other ten maps are identical to the Nov 13 evening capture to the entry - the correction that pass made to `servers/9` (4,031 to 4,030) holds here, so nothing else moved. The distinct key set rose by **191**, from 21,131 to 21,322.

The set diff gives **225** keys not present on the 21:03 capture. That number is a wave, not 225 discoveries, and the decomposition is mostly mechanical:

- **Apify actor slugs.** Twenty-one `apify-com-*` entries, including a seven-item `dheerajitbhu` set and a four-item `plainrecordlabs` set. Standing Apify-actor ruling: these are distribution of someone else's scraper, not a data product.
- **One publisher fleet.** Eleven `cotlet-dev-integrations-*` entries (Dubsado, ERPNext, Fatture in Cloud, Inoreader, Invoice Simple, Lexware Office, MYOB, Shiftbase, Squire, Taxdome, Zotero) - resolved once, held as a commercial integration marketplace.
- **A second and third fleet.** Three `renzojohnson-com-contributions-*` slugs (GA4, Google Ads, Google Workspace) and three `urbanmorph/*` slugs (geodata, mugilu, overlooked), plus two `nodemaven` (residential proxies), two `mypinpal` beyond the pair already known, two `www-mcpstamp-com-*` and three `www-brainiac-software-api-*`.
- **Documentation mirrors and marketing pages indexed as servers.** `docs-*`, `*-docs-*`, `*-llms-txt`, `*-connect`, `*-developers`, `*-ai-assistants`, `github-com-*` and `blog` slugs form the largest single class in the wave - pages that describe a server rather than serve one.
- **Prior dispositions arriving as new canonical slugs.** `ikoi-ai`, `turlockmike/habits-guard-mcp`, `itmarkerz/calcbloc-mcp`, `docquery-io`, `koda-ai-studio/agent-bom`, `verand-ai-mcp`, `jobiba-com-developers`, `martinschenk/palimpalem-mcp`, `platform-sonilo-com-mcp`, `radar-offseq-com-api-docs`, `pangolin-spg/pangolinfo-review-mining-mcp`, `www-key-rank-com-docs-mcp`, `useagentdrive-com` and `splera-ai-mcp` are all products this catalog has already read and ruled on, re-entering under a domain slug. A canonical slug for a catalogued product is a slug acquisition, not an arrival.

What remains after that decomposition is a long tail of one- and two-slug SaaS connectors - `showmrr-com`, `taxinger-com-agents`, `sviy-ai`, `servana-ai-for-agents`, `setupbay-com`, `printandmailcompany-com-en-ai-assistants` (the one that shipped), `linkpreflight`, `datafast-app`, `webinarstack-co`, `hostedmcp-org` and about seventy others - of which one carried a driveable endpoint worth a guide.

**The 95 lastmod stamps are the arrival signal, and 90 of them are re-index, not arrival.** Ninety of the ninety-five distinct listings stamped at or after 04:01Z were already in the Nov 13 key set: Skyvern, IBM's context forge, ClickHouse Loom, Couchbase, Builder.io, Notte, Unity MCP, voice-mcp, Umami, MCPJam's inspector, Agent BOM, Zambo, Ghostlight. A stamped page is a page re-read, and reading the stamp as a discovery is how a wave becomes a false claim. Only **five** were genuinely new:

| Slug | First stamp | Disposition |
|---|---|---|
| `omd-123/browser-verified-skill` | 04:52Z | unattributed - no registry record, no resolveable product page |
| `twelveswaras/twelveswaras` | 06:24Z | thin - a personal listing with no product statement |
| `lanbass869-cell/canari` | 06:28Z | unattributed |
| `github-com-agenttools-cloud-...-agent-tools-mcp` | 06:28Z | documentation mirror of a collection page |
| `julian-dev28/pathiel` | 06:34Z | unattributed |

Three unattributed slugs are recorded as unidentified rather than inferred. A slug is not a product.

## The feed, two cards

Read at **155,460** bytes with **37** card anchors and **30** stamps in the `M/D/YYYY, HH:MM AM/PM` UTC form. Two sat above the 04:01Z cutoff.

**Mojobase** (`mojobase`, `https://app.mojobase.ai/mcp`) - *one MCP server for your whole business: email, chat, calendar, tasks, files, customers and numbers*. Registry published **2026-11-14T06:17Z**, an hour before the card was stamped, with two remotes: a per-company URL (`/mcp/{company}`, the id from Settings, sign-in on connect) and a base URL requiring `Authorization: Bearer {key}`. `initialize` returned **401** with error code **-32001** and the body *needs a key: Settings - Connect an agent*, `WWW-Authenticate: Bearer realm="Mojobase"`, and **404** on both `/.well-known/oauth-protected-resource` and `/.well-known/oauth-authorization-server`. That is the static-token tier with no discovery document: the handshake is measured, the tool surface is not, and a guide would be a description of a marketing page. **Held pending a keyed session** - it is a unified business console, which is close enough to this catalog's own territory that it deserves a driven read rather than a listing.

**Vantage** (`vantage-977587`, `https://vantagemcp.dev/mcp`) - checks whether ChatGPT, Gemini and Perplexity cite your site, and who they cite instead, with **11** tools and a public GitHub repository. **Held on the visibility class**, owned here by geolint, LogNorm and the saturated rank-tracking surfaces, with Verand held on the same ground two days ago. Its own registry record runs to 1.10.0 with a free tier, so it is a serious product landing in a class that already has four owners.

## The queue, nine arrivals

Read from **#7319** to **#7327** in one authenticated call, with bodies.

**Shipped - Print and Mail Company.** Not from the queue: the wave carried `printandmailcompany-com-en-ai-assistants` and the registry resolved it to `com.printandmailcompany/printandmailcompany` at `https://printandmailcompany.com/mcp`. Fourteen tools, three of them keyless; a **236-country** destination list in five zones; quoted **€4.20** for two pages to France and **€23.95** registered, a flat **€19.75** registered surcharge proven on two different zones; and `send_letter` gated behind `confirm` plus `user_accepted_terms` against a specific draft. The European counterpart to MailStream and PostAgent.

**Shipped - Barakah Halal Stock Screen** (`com.barakahprofits.app/halal-screen`, #7320). Keyless, two tools, ten calls driven. Apple and Microsoft land **DOUBTFUL** on a revenue-mix review while passing both ratio tests at 1.6%/1.2% and 1.5%/2.0%; JPMorgan fails three checks at once (57.9% debt, 90.6% cash); Exxon sits **NEEDS REVIEW** because interest income cannot be read. The ledger returned 25 dated events back to 19 October, including Occidental and Nebius each breaking and clearing inside 48 hours - the market-cap denominator doing what the vendor says it does.

**Held, with the owner named.**

**ShowMRR** (`com.showmrr/showmrr` 1.0.1, `https://showmrr.com/api/mcp`, keyless, six tools driven) holds on the **revenue-data class** owned by MobileMRR (provider-verified marketplace revenue, five tools) and MRR Ledger (sourced leaderboards, keyless, CC BY data). Its differentiator would be the provenance taxonomy, and it is honest - but the vendor's own methodology page, read today, reports **56,750 public listings, 0 verified from a connected provider, 3 self-reported from a public page, 3 typed in, and 56,744 with no revenue figure at all**. The screen's own `verified_only` leaderboard returned *No startups found*, and `list_categories` reports **0 verified in all nineteen categories**. A provenance label that is empty everywhere is a plan, not a data product, and it cannot displace MobileMRR.

**Paygent** (`ai.paygenthq/paygent`, #7323) holds on the **agent payments class** carried by Agent402, Agent Payment Node, Veyra and Privi: OAuth with a PIN approval per payment is the right shape, and bank transfers in Nigeria, Kenya and South Africa plus mobile money in Ghana, Kenya and Tanzania is a genuinely new regional slice - but every owner in that class is a hold and this pass adds no driven evidence.

**Oracle by SaltCrate** (`com.saltcrate/oracle`, #7322) holds on the **x402 pay-per-call utility class** - fetch, extract, search, link check, change watch and CVE scanning at a cent a call with 200 free hourly calls, which is the SiteCheck and AuraNet shape with better packaging rather than a new capability.

**GoMarble MCP** (`ai.gomarble/mcp-api`, #7326) and its open-source **GA4 MCP** (#7327) hold on **ad-operations density** - 400+ tools across Meta, Google, TikTok, LinkedIn, Microsoft Ads, GA4, Search Console, Shopify and Klaviyo is the Adrails, Markifact and Blend class, and the 400-tool figure is the vendor's.

**Bitquery** (`io.bitquery/mcp`, #7321) holds on the **crypto and on-chain data class**; **Agent Nexus** (#7319, a discovery registry with signed health receipts) on agent infrastructure beside Peerlace and MCPALL; **iotaudit** (#7324, local IoT network audit, MIT) as a home-network utility rather than operator tooling; **VedicDost** (#7325) as a consumer astrology vertical; and **Barakah** shipped rather than held because a compliance screen is a different capability from a price feed, which is the class that was actually saturated.

## What the window says

The directory contributed **zero new products** for the third pass running, and this time it did it while adding **225 keys** - a reminder that the key count is a description of the index, never of the market. Ninety of ninety-five fresh stamps were re-reads of listings already held.

Both ships came from surfaces the index does not own: one from a marketing page the wave dragged in that happened to be a real keyless endpoint, one from the submission queue. And both earned their guides on the same ground as the last two passes - not on a feature list but on what the tool does when it is asked: a price that reconciles to the cent with a flat registered surcharge, and a compliance verdict that refuses to read a line it cannot see.

## 🆕 November 14, 2026 - Night (2 New, 2 Guides)

A six-hour window where the canonical added 225 keys and no products, the feed carried two cards, and the queue carried nine - with the two ships decided by arithmetic rather than by claims.
