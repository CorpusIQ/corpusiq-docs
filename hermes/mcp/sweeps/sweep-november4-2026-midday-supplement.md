---
title: "MCP Server Discovery - November 4, 2026 (Midday Supplement)"
description: "Supplement pass: six endpoint probes on the morning window, one crawl-log entry catalogued with a stated reversal, and the class correction that followed."
last_updated: 2026-11-04
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november4-2026-midday-supplement"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 4, 2026 (Midday Supplement)

## Summary

This pass fired on the **11:00 MST** tick, one hour after the **10:00 MST midday pass**, so it is recorded as a supplement rather than a second reading of the same surfaces. The midday pass had already refreshed the twelve-sitemap canonical, read mcpservers.org `/all` pages one to five, read the submission window through **#6743** and dispositioned all five fresh listings. Nothing here re-triages that work.

What the supplement added is evidence the midday pass did not have: **six live endpoint probes** on the morning's candidates, and one catalogue entry. It also records a correction, and the correction is the part worth reading.

**The reversal, with reasons.** The midday pass held **NMOS.NET Crawl Analytics** on the crawl-visibility class, citing SEOcrawl AI, the AI Crawler Index and IndexLinks' crawl receipts. This pass reverses that hold on the *surface*, not on the vendor, and the distinction it rests on is narrow: [IndexLinks](/hermes/mcp/servers/external/indexlinks-mcp/) proves a crawl for pages sent to its own submission network, one page at a time, on a plan priced by submitted pages from **$49** a month. NMOS.NET installs a beacon once and logs every crawler that reaches any page of a site, including pages nobody submitted, with sitemap gaps, robots conflicts, reverse-DNS authenticity and SSL health beside it, and a free tier that makes the claim testable in an afternoon. Passive site-wide logging and active per-page submission receipts are different instruments, so both belong in the catalogue.

**The correction.** The first merged version of that guide claimed this catalogue held the answer side of AI visibility and "the input side none". That claim was wrong: IndexLinks, added October 6, reads verified crawler visits with timestamps, and the AI Crawler Index verifies crawler IPs against operator-published ranges. The guide now names both entries, states what each does, and explains what NMOS.NET adds instead of asserting it was absent. The lesson is the ordinary one: a class claim is a grep, not an impression, and it has to be run against every neighbour the prior pass named before it goes into a page.

## Sources Swept

| Source | Read | Result |
| --- | --- | --- |
| chatmcp/mcpso submission window | authenticated `gh api`, bodies included, one call | **27** items **#6719** to **#6745**; **25** were dispositioned by the 10:00 pass, **2** are new here (`#6744 Tabula`, `#6745` a listing-removal request) |
| mcpservers.org twelve-sitemap canonical | reused the 10:15 capture as the baseline, no fresh refresh | the **5** additions it recorded (astraeye-labs, exclusive-digits, lingviko, orinyx, snapwidget) were all dispositioned at 10:00, and nothing new has entered the sitemaps since |
| mcpservers.org `/all` | second read of the newest page through the reader proxy | **19,344** against **19,342** on the first read, a two-slot rotation (`eas` and `reciba` out, `lingviko` and `snapwidget` in) |
| mcp.so `/feed` | direct fetch with a browser UA, `createdAt` parsed | **124** objects, newest `2026-11-04T14:37:59Z` (Gamebeast), **one** card above the 10:00 stamp |
| Endpoint probes | keyless `initialize`, six endpoints | **2** answering **200** (`workload-zero` **2.1.0** with **149** tools, `gameshipkit` **1.0.0**) and **4** answering **401** |

## New Servers Catalogued

### NMOS.NET Crawl Analytics MCP - Observed AI Bot Visits

Relevance: HIGH. **Tier 3, measured 401**: a keyless `initialize` to `https://nmos.net/mcp` returned `HTTP 401` with JSON-RPC `-32001 Unauthorized. Connect via OAuth or send Authorization: Bearer ***`. No tool was called.

Six read-only tools (`list_sites`, `list_bot_visits`, `get_crawl_stats`, `get_traffic_overview`, `get_robots_status`, `get_site_health`) behind OAuth 2.0 with PKCE, dynamic client registration and a client ID metadata document. The data arrives by beacon rather than by API: a meta tag plus `tracking.js`, a no-JS CSS beacon, or a Cloudflare Worker at the edge, with WordPress and GTM on Pro+, and the vendor states plainly that a meta tag alone identifies the site and records no visits.

What it answers: whether Googlebot reached the important pages, with visits, journeys and sitemap gaps; what AI bots are reading, as visit trails plus `llms.txt` coverage match or miss; and which bots hit HTTP errors, robots conflicts or a forged user agent, the last checked by reverse DNS on Pro and above. The vendor's limit is quoted in the guide rather than smoothed: visit records and policy signals, not search rankings or model-training proof. Pricing: free for **1** site and **100** crawl visits a month with crawl analysis only, and `llms.txt` coverage, sitemap coverage, bot authenticity and the crawl-like-a-bot simulation all start at **Pro, $20** a month, with the integrations panel at **Pro+, $40** and yearly billing at ten times monthly.

## Read and Held, With the Measurement Behind Each Ruling

The two arrivals this pass added to the window: `#6744 Tabula` is credit for agents that pay x402 sellers and roll the charges into one loan repaid with a signature, held on the agent-payments class carried by [FiatDock](/hermes/mcp/servers/external/fiatdock-mcp/), CoinVello and SnapEX Pay; `#6745` asks mcp.so to retire an unmaintained community prototype in favour of the maintained FinancialFilings server, housekeeping rather than an arrival.

The morning's holds stand and were not re-opened: astraeye-labs on the public-market research class, exclusive-digits as number inventory, orinyx as a healthcare vertical, lingviko outside scope, snapwidget as a website embed rather than a data surface, and `Gamebeast` as a single-vendor game-LiveOps analytics connector with a promotion test recorded.

Two keyless **200** probes sharpen holds the midday pass could only group. `workload.zero` answered as `workload-zero` **2.1.0** with **149** tools across profile and colleagues, projects and budgets, clients, tasks, timers, goals, deals, quotes, quote-to-invoice and revenue, the widest surface seen in a week, and it is held because every slice of that suite is carried already, CRM and revenue by Deskhand, NOVA for Kommo, Finwise, Reciba and Volanea, and the task and project slice by the project-management entries. `GameshipKit` answered as `gameshipkit` **1.0.0** with five tools over 69 browser tools for pixel art, VFX and store assets, outside operator scope. Three **401** probes attached a tier to holds that would otherwise be assertions: `Links as a Service` returned `invalid_token` on a Danish link marketplace with 150k publisher domains at publisher cost plus a 20 percent margin, held because the link-building slice is carried by [RankControl](/hermes/mcp/servers/external/rankcontrol-mcp/) and [MentionAgent](/hermes/mcp/servers/external/mentionagent-mcp/) and what remains is a checkout over bought inventory; `UX Pilot` returned `-32001 API key is required` and drives UI design on its own canvas; `EZ@Work` returned an empty-bodied **401** and is the freelancer version of the invoicing and time slice. `Smitline` was held without a probe because its two halves are both carried, voice by PlaceCall and meeting notes by [Granola](/hermes/mcp/servers/external/granola-mcp), ParrotNotes, Tactiq and Lavox.

## Count

The guide tree held **1,098** directories before this supplement and holds **1,099** after it, **1,242** entries counting single-file guides before and **1,243** after. Sources: the chatmcp/mcpso submission window **#6719** to **#6745** with **2** items new to this pass; a reused twelve-sitemap baseline at **19,344** with no fresh refresh because the 10:15 capture already dated the window; mcpservers.org `/all` read at **19,342** then **19,344**; the mcp.so `/feed` at **124** objects with the newest at `2026-11-04T14:37:59Z`; and **6** endpoint probes, **2** answering **200** and **4** answering **401**.
