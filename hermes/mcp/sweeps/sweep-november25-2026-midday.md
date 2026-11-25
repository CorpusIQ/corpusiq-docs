---
title: "MCP Server Discovery - November 25, 2026 (Midday)"
description: "A flat directory proven three ways, with three keyless ships from the queue: name checks, font licences, and car repair costs."
category: "MCP Ecosystem"
last_updated: "2026-11-25"
---

# MCP Server Discovery - November 25, 2026 (Midday)

Fired on the **10:00 MST** tick, about **6.5 hours** after the night capture stored its baseline at **10:20Z**. The directory did not move, and this pass can prove that three ways rather than assert it: every per-map raw count identical, every per-map distinct key count identical, and **not one** `lastmod` stamp inside the window. All three ships came from the submission queue, all three are keyless, and all three were driven end to end before a word was written.

## The window, measured

```text
mcpservers.org /sitemap.xml   SEVENTEEN maps named, unchanged
  static.xml, priority-servers.xml, servers/1..13.xml, skills.xml, remote-mcp-servers.xml
raw <loc>, numbered server maps 1-13   37,806   identical to the night capture
  servers/1  ..... 4,129     servers/8  ..... 2,754
  servers/2  ..... 2,513     servers/9  ..... 2,594
  servers/3  ..... 2,953     servers/10 ..... 2,554
  servers/4  ..... 3,195     servers/11 ..... 2,447
  servers/5  ..... 3,270     servers/12 ..... 2,431
  servers/6  ..... 2,876     servers/13 .....   220
  servers/7  ..... 5,870     sum 37,806 exact
distinct keys per map                    1,987 / 1,990 / 1,994 / 1,999 / 1,996 / 2,000 x7 / 220
  identical on all thirteen               the shard ceiling holds at 2,000
priority-servers.xml                     232 raw / 34 keys     (unchanged)
remote-mcp-servers.xml                    15 raw / 15 keys     (unchanged)
union, raw                               38,053                identical to the night capture
union, distinct keys                     24,235                against 24,221 stored overnight
lastmod pairs, server maps only          34,376
  rows at or after 10:30Z                     0
  newest stamp anywhere              2026-11-25T09:06:09Z
```

**Why the fourteen-key gap is not fourteen arrivals.** The stored night figure is 24,221 and this capture reads 24,235, but a genuine arrival has to show up somewhere in the window: it moves a per-map raw count, a per-map key count, or a `lastmod` stamp. Not one of the thirteen maps moved on either count, and the `lastmod` scan is empty at or after the cutoff. The gap is the same locale-prefix normalizer difference this catalog recorded on November 24 evening, when a stored 23,906 read as 23,892 under the current extractor. The `lastmod` scan is restricted to the thirteen server maps on purpose: `skills.xml` alone carries **13,124** skill slugs and floods any scan that includes it.

`/all` was not re-read. It has answered **403** by edge policy since 4 November.

## The feed, and the queue that carried everything

The feed answered **200** at **160,721** bytes with **36** anchors and **30** stamps. Three cards sit above the night read: **urml** at 11:00Z, **instapods** at 10:39Z and **the-glitch** at 10:27Z. None was reached, so none is catalogued, and all three are recorded below as seen rather than judged.

The queue carried **#8055** to **#8086**, **32** filings, with bodies read in one authenticated call. Two of the thirty-two are one product filed twice: `#8080` and `#8078` are the same KI-Agenten-Test submission with the same endpoint.

## The three ships

- [tld.expert MCP - Domain and Name Checks With Sources](/hermes/mcp/servers/external/tld-expert-mcp/) - **six keyless tools, driven**. Availability comes from RDAP with the registry named: `corpusiq.io` taken through a privacy service, registrar **Name.com, Inc.**, registered **16 October 2025**, expiring **16 October 2027** from `rdap.identitydigital.services`; `acme.com` taken with **eNom, LLC**, registered **17 April 1991** from `rdap.verisign.com`. Prices are dated per row: `.com` **$11.62** first year and renewal at Dynadot with a Cloudflare renewal that **moved from $10.46 to $11.17 on 2026-11-24**, `.io` **$20.91** first year against **$51.80** renewal at Porkbun, a trap the tool names as **2.5x**, `.ai` **$82.70** on a **two-year minimum** so **$165.40** at checkout. Every five-year figure reproduces by hand (`20.91 + 4 x 51.80 = 228.11`; `82.70 x 5 = 413.50`; `11.62 x 5 = 58.10`). The distinct job is `check_brand_name`: GitHub taken by an organization, npm with no such package and no live US trademark, each timestamped, with the server saying in the answer that *"none means the source has no record, not that the name is free to use."* Domain availability alone is already covered here by Just Domain MCP; the brand cross-check is not covered by anything.
- [Fontier MCP - Font Licences Answered With the Quote](/hermes/mcp/servers/external/fontier-mcp/) - **five keyless tools over 2,168 open-licence families, driven**. Every verdict carries a verbatim quote, the source URL, the licence id and a SHA-256 of the text read. Inter for commercial use is **yes** under **OFL 1.1** with the sentence that decides it, and **5,344 of the top 100,000 sites** (Tranco `JZW4Y`) load it while the phone downloads **23,664** bytes for Regular and **48,432** for Regular plus Bold. Satoshi for a logo is the answer worth the guide: its licence says a wordmark **may be registered as a trademark** and, three lines later, that the font files **may not be provided to external designers, agencies, contractors or printers**, so an outside agency has to license its own copy. Pairings come with the arithmetic to implement them: Fragment Mono at **104%** of Inter's size makes the lowercase align. One measured caveat: `sort: "size"` orders on the **Bold** WOFF2 size, so the Regular column is not monotone (Cuprum's 9,284 precedes Khand's 7,664).
- [Oil & Miles MCP - Repair Costs Before the Quote Lands](/hermes/mcp/servers/external/oil-and-miles-mcp/) - **six keyless tools, CC BY 4.0, driven**. P0420 returns the meaning, what the computer saw, what gets checked and what the code **does not prove**: *"It doesn't prove the converter is bad. An exhaust leak or the engine's software can set the code with nothing wrong inside it."* **21** codes and **6** repair jobs are listed, brake pad and rotor returns two cars rather than a blended range (**2025 Subaru Crosstrek**: $391 to $488 independent against $530 to $565 dealer; **2021 Silverado 2500HD**: $415 to $690 against $768 to $844, so the dealer floor sits $78 above the independent ceiling), and the markup reproduces by hand at **35.5%** and **85.1%**. Two defects recorded: the `headline` range of $391 to $565 describes only the first car while a second car in the same response reaches $844, contradicting the tool's own note that each car has its own range; and coolant coverage is three Honda cars with an honest `isError` for a 2019 Toyota Camry.

## Also identified this pass (not catalogued)

Held on a named class or gate, each from the filing's own description unless stated:

- **Aura MCP** (#8086) and **Elementor MCP** (#8085), one vendor's WordPress pair, both install-gated: Aura requires an account, Elementor is a WordPress plugin. Held on the local-install tier.
- The aviation trio **EU261** (#8084), **FAA Part 117** (#8083) and **EASA FTL** (#8082) from one author, all three Apify actor endpoints behind a Bearer Apify token with per-event pricing. Held on the Apify-actor distribution class recorded on 7 October with Metqo. The EU261 calculator's 9,000-airport great-circle distance band is the one worth a probe if the class ever opens.
- **KI-Anzeigen-Planer** (#8081), **KI-Agenten-Test** (#8080 and its duplicate #8078) and **KI-Sichtbarkeits-Test** (#8079) from ki-suchergebnis.de, four filings for three products, all keyless and German-language. Held on the AI-visibility class already carried here by geolint, LogNorm, Agitech Site Check and 1Alexander.
- **DBA Brain** (#8077) with graded OK/WARNING/CRITICAL health checks across SQL Server, Oracle, PostgreSQL and MySQL, and read-only SQL that is always rolled back. Both doors are gated, a pip stdio install and an OAuth remote, so it is queued for a local drive rather than catalogued from a description.
- **n8n Preflight** (#8076), static checks on exported n8n workflow JSON for missing Respond to Webhook nodes, HTTP calls without retry and literal API keys in the file. stdio, no network calls, MIT. Queued for a local drive; the secret-scanning angle is the part no existing entry covers.
- **Mindmetrics** (#8074) unifying marketing data from more than 30 platforms behind OAuth 2.1 with dynamic registration and PKCE S256. Held pending a real grant, and noted as the closest product in this ecosystem to our own connector set.
- **Cybership** (#8058), warehouse management for 3PLs behind OAuth. The strongest business fit among the holds and the one to queue for a grant.
- **Pivlu App Database** (#8059), App Store chart snapshots in 150 countries with revenue estimates from chart rank, behind OAuth 2.1.
- The **yojowa quartet**: **WithBy** (#8068), **StockMap** (#8067), **Talkhao** (#8066) and **FamilyLore** (#8065), four products on one shared authorization host `auth.yojowa.com`, each keyless for between two and nine of its tools. Held as one publisher fleet, with StockMap also landing on the saturated stock-research class.
- **GateCore AI** (#8071), a governed marketplace for agents: discovery keyless, procurement behind a `gcmk_` key. **Clustr** (#8073) is keyless but asks for name, company and work email, held as a lead-capture gate. **LMH Agent Data Tools** (#8072) is an eleven-actor Apify bundle behind a Bearer token.
- **Logic Pro MCP** (#8070) is a stdio install driving Logic Pro on macOS, held on the media class. **SpeedPainter** (#8075) is whiteboard video generation behind Google OAuth, same class. **Oryn** (#8057) builds browser games behind OAuth.
- **Formify** (#8064) lands on the e-signature class already seeded. **Bookare** (#8060) is booking software with per-venue OAuth. **Pandex** (#8062) serves legislation and court decisions at 50 anonymous calls a day, on the regional legal class carried by LEGAION, aka-recht and Specter Cite. **Perklo** (#8061) returns 27 keyless UK deal and voucher tools, held as the deals commodity class.
- From the feed, recorded as seen and not reached: **urml** (11:00Z), **instapods** (10:39Z), **the-glitch** (10:27Z).

## Listings, re-measured

- **mcpservers.org**: detail routes answer **403** to curl by edge policy, so presence cannot be read from a status code. Our own mirror `/servers/corpusiq/corpusiq-docs` carries a fresh `lastmod` stamp in the canonical capture, and the prior passes recorded the listing as live.
- **mcp.so**: **LISTED** at the repo-derived slug `/servers/corpusiq-docs`, which answers **200** at **857,549** bytes with the title *Corpusiq Docs MCP Server: Tools, Setup and Config* and **175** occurrences of the name in the served payload. The four guessed singular slugs (`corpusiq`, `corpusiq-io`, `corpusiq-mcp`, `io.corpusiq`) still answer **404**, which is the recorded shape of this listing and not a delisting: a guessed URL never counts as evidence against a confirmed listing. The row describes the docs repository rather than the 40+ connector server, and the accuracy debt on that copy is recorded in the entity checklist.
- **Smithery**: the registry API answered **500** on two attempts, so this pass cannot re-read the API status. The listing was live in the API on November 23 with the public page 404 a namespaced-route condition; no delisting inferred from a server-side 500.
- **Glama**: the API now requires a key (**401**, with a licensing notice naming attribution requirements) and the connectors route answers **404** unauthenticated. The listing was recorded live on November 23; a 404 on a guessed URL is not a delisting, so the prior status stands.
- **Anthropic connector directory**: the watcher ran over **1,223** pages and returned **exit 0**, unchanged. CorpusIQ is not in the feed. The submission filed on 16 November is still under review in the portal, and review status lives only at `claude.ai/directory/manage`.

## Held for the next pass

**Cybership** for a real OAuth grant, **DBA Brain** and **n8n Preflight** for a local stdio drive, **Mindmetrics** on a grant, and the three unreached feed cards. The fourteen `lastmod`-window free passes in a row say the directory is not where the material is arriving; the queue is.
