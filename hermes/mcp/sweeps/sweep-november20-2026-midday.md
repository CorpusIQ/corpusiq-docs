---
title: "MCP Server Discovery - November 20, 2026 (Midday)"
description: "A flat seven-hour window with one raw entry of churn, twenty-seven queue arrivals, and two servers that read dates and prices nobody publishes."
category: "MCP Ecosystem"
last_updated: "2026-11-20"
---

# MCP Server Discovery - November 20, 2026 (Midday)

Fired on the **10:00 MST** tick, seven hours after the night sweep closed at **10:00Z**. The canonical moved by one raw entry that added no key, so the window's material came from the submission queue and the feed: **27** arrivals and **8** cards, of which two earned a guide - the first calendar-data surface in this catalog and the first price surface that returns a verdict with a date on it.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          66,963   against 66,962 at the 10:00Z night capture  (+1)
  servers/1  ..... 7,588     servers/7  ..... 9,351     sums to 66,963 exactly
  servers/2  ..... 5,949     servers/8  ..... 6,590
  servers/3  ..... 6,518     servers/9  ..... 4,022
  servers/4  ..... 6,746     servers/10 ..... 2,608
  servers/5  ..... 6,954     servers/11 ..... 2,638   <- the whole rise, 2,637 to 2,638
  servers/6  ..... 6,756     servers/12 ..... 1,243
priority-servers.xml          299 raw,  34 distinct keys
remote-mcp-servers.xml         15 raw,   1 distinct key
distinct keys, twelve maps    22,958   IDENTICAL to the night capture
distinct keys, union basis    22,993   IDENTICAL to the night capture
lastmod rows at or after the cutoff   563, collapsing to 139 distinct keys
mcp.so /feed                  200, 158,757 bytes, 37 anchors, 30 stamps
                              EIGHT cards above the cutoff, 0 shipped
submission queue              #7697 to #7723, twenty-seven arrivals, bodies in one call
```

Three readings agree that no product arrived on this surface: the raw count rose by **one**, the distinct key set is **unchanged on both bases**, and the **563** `lastmod` rows at or after the cutoff collapse to **139** keys of which eight carry the same URL **fifteen times each inside one second** - the re-shard signature this surface has shown all week. The one raw entry is a locale form, not an arrival. `/all` was not re-read: **403** by edge policy, the standing condition since 4 November.

**The one key that did move is a map form, not a product.** The twelve-map key set is set-identical, and the single addition on the union basis is `https://mcpservers.org/remote-mcp-servers/clockwise` - the remote map's own form of a slug the evening pass had already read and dispositioned as a prior route. It is recorded here as a form change rather than counted as a discovered server.

## The feed, and the queue

The mcp.so feed answered **200** at **158,757** bytes with **37** anchors, **30** stamps and **eight** cards above the **10:00Z** cutoff:

```text
eventtia                         servers  16:43Z
quso-ai                          servers  16:09Z
mycorr                           agents   16:01Z
kirat-multi-model-ai-council     agents   13:32Z
vciso-fractional-ciso-services   servers  13:30Z
upinvoice                        servers  12:33Z
invoicexml-16ea0c                servers  10:47Z
apimodels                        servers  10:37Z
```

Detail routes on the feed cards were not readable this pass: `r.jina.ai` answered **401 bad IP reputation** on every page, and a direct request is blocked by the same edge policy that closes `/all`. The cards carry a name and a stamp but no description in the feed HTML, so these eight are recorded as **unresolved** rather than guessed at - a slug is not a product brief, and two of them (`eventtia`, `upinvoice`) name classes this catalog already owns through invoicing and event surfaces.

The submission queue carried **#7697** to **#7723**, **27** arrivals with no gaps, read with bodies in one authenticated call. It was the richest queue of the day and most of it was fleets: **five** `mambalabsdev` packages (**#7709** to **#7713**) on the standing Apify ruling, **five** `henrycrawl` Apify integrations (**#7718** to **#7722**), and **three** more Apify actors (**#7715** to **#7717**) covering Lazada, Google Flights and a KAYAK comparison.

## Shipped, with guides

### SchedJoules - the first calendar-data entry in this catalog

`https://www.schedjoules.com/mcp`, *schedjoules* **1.0.0** on **2025-06-18**, **three** keyless tools, no session id issued. Queue entry **#7708**.

Ten `tools/call` requests across five calendars. The Netherlands public-holiday calendar (**50077**) returns *Christmas Day 2026-12-25*, *Second Christmas Day 2026-12-26* and *New Year's Day 2027-01-01*; the southern school calendar (**50080**) returns *Kerstvakantie 2026-12-19* - six days before the public holiday, which is the rota answer; the Ajax calendar (**29128866**) returns five fixtures with UTC kick-offs from **2026-11-22 13:30** to **2026-12-06 13:30**; and the financial calendars - a category this catalog had no owner for - return Prudential Financial's dividend sequence (*projected ex-dividend 2026-11-24*, *projected record 2026-11-24*, *payment 2026-12-10*, *projected payment 2026-12-17*), with the word *Projected* carried in the event title itself.

**Limits recorded rather than smoothed:** the preview is capped at **five events inside sixty days**, so a full-year question cannot be answered; the subscribe link is an app deep link (App Store **853708554**, Play `com.schedjoules.sync`) rather than an ICS URL; search is keyword matching that returns FC Basel for *financial events* and ten TV shows for *weather*; and the country word does not scope the results, so *netherlands holidays* returns German, French, Belgian and Australian calendars inside the same twenty. Refusals are precise on all three paths.

### Fordeal - the first price surface that returns a verdict with a date

`https://fordeal.ai/mcp`, *fordeal* **0.1.0** on **2025-06-18**, **two** action-switched tools, keyless, SSE responses. Queue entry **#7697**.

Eight calls. An *iPhone 16* in **CZ** returns verdict **wait** at **CZK 19,990** from Mobil Pohotovost (2,882 ratings, 0.82, `price_status: verified`, captured **2026-11-20T10:54:58Z**) because the 90-day low is **18,015.06** on **2026-11-08** - and the `history` action returns exactly the series that number comes from: **21** points over a **365**-day window, first **2026-10-01** at **21,260.09**, max **22,990** on **2026-10-03**. The trending board for CZ separates goods from shipping the way the instructions promise (**3,190 + 69 = 3,259** for AirPods 4 across **4** shops), and every search response carries an affiliate disclosure in the tool output itself.

**Defects recorded:** the card says two countries while the refusal path prints six (`CZ, SK, PL, DE, AT, HU`); text search rewrote *robot vacuum* to include *irobot* and returned a mop pad at **388 CZK** and a replacement brush at **308 CZK** as partial matches; `history` rejects `query` and demands a slug, naming an internal `price_history` action the schema does not list; `most_searched` for SK returns an empty ranking whose `next_actions` calls a tool (`search_products`) and a parameter (`deliver_to_country`) that do not exist; `abroad` returns an empty list with no reason; and one product's `offers` array mixes **1,029 EUR** into a CZK response without conversion.

## Held, with the gate or class named

- **Imperio Utilities** (**#7702**) - Italian tax tools, keyless, and the first name that looked like a ship. It is already catalogued: [Imperio MCP](/hermes/mcp/servers/external/imperio-mcp/) has held the Italian tax slot since **2026-08-17** with the same codice fiscale, F24 and FatturaPA surface. A duplicate of our own entry is the cheapest mistake to make in this job and the crossref caught it.
- **Eurodatum** (**#7699**) - Europe's AI-infrastructure and grid-power data. The endpoint is not there: `https://eurodatum.com/mcp` answers **405** to a JSON-RPC POST and **404** to a GET, `/agents/` and `/llms.txt` both **404**, and the apex serves a page reading *"This site is offline."* A dead host, recorded rather than inferred.
- **GuestDrop** (**#7707**) - OAuth 2.1 with dynamic registration, `401` with a complete `WWW-Authenticate` naming `/.well-known/oauth-protected-resource/api/mcp`, PRM **200** with scopes `events:read` and `events:write`. Certified as a handshake, held on substance: guest photo collection for private events, consumer-shaped and with no readable tool list.
- **epistemic-guard** (**#7714**) and **aiZee** (**#7698**) - agent receipt verification and a governance kernel. Both sit on a class this catalog already owns: the Ed25519-signed hash-chained receipt entry and the `ledger_append` / `ledger_verify` audit entry are the owners, and a third and fourth entry would repeat them.
- **SchedJoules' neighbours in the queue**: **NotePorter** (**#7723**) is a macOS-only app with a built-in stdio server, nothing drivable from a Linux host and a **$15** one-time price; **HostSherlock** (**#7703**) is DMARC/SPF/DKIM deliverability on the email-auth class an existing owner already carries; **PipeForge** (**#7705**) and the **HenryCrawl** five (**#7718** to **#7722**) are Apify transport; **Kuickr** (**#7704**) and **Druks** (**#7700**) are OAuth and bearer-token gateways with no readable surface; **GuaraPay** (**#7706**) issues virtual cards to agents and is held on the payments class with nothing read; **Christian Pure** (**#7701**) is devotional content; **Fordeal's neighbour** **SchedJoules** aside, **Eurodatum** is the only energy candidate and it is offline.

Twenty candidates were resolved through the official MCP registry or by name against the catalog index, and one of them - Imperio - was a prior entry. The rest are recorded in the catalog's hold register rather than dropped.

## Listings, re-measured

The cron's stated target is the CorpusIQ listing, so all five surfaces were checked rather than inherited:

```text
mcpservers.org  LISTED    https://mcpservers.org/servers/corpusiq-io in servers/5,
                          six rows in the union naming corpusiq across three locale
                          forms for two keys; the docs mirror also sits at
                          /servers/corpusiq/corpusiq-docs, re-stamped 11:37:54Z today
mcp.so          LISTED    /servers/corpusiq-docs 200 at 858,407 bytes, title
                          "Corpusiq Docs MCP Server: Tools, Setup & Config",
                          175 corpusiq mentions on the page; the four guessed
                          product slugs (corpusiq, corpusiq-io, corpusiq-mcp,
                          io.corpusiq) all 404 and are not a listing verdict
glama.ai        LISTED    /mcp/connectors/io.corpusiq/multi-source-mcp 200
smithery.ai     LISTED    registry.smithery.ai/servers/@benoit-p/Cprusiq 200,
                          qualifiedName benoit-p/Cprusiq, displayName CorpusIQ
Anthropic       NOT LISTED  scripts/anthropic_directory_watch.py: 1,198 pages
                            across 3, listed=False, exit 0 - unchanged
```

**Correction made inside this pass.** The first reading here recorded mcp.so as NOT LISTED on the strength of four 404s against guessed product slugs. That is the wrong test: mcp.so carries this product as a repo-derived page at `/servers/corpusiq-docs`, which answers **200** at **858,407** bytes with the title *Corpusiq Docs MCP Server: Tools, Setup & Config* and **175** corpusiq mentions, and its description is the **docs repository's** blurb (*"Hermes Agent Production Knowledge Repository - 406+ repos, AI Agent Marketplace..."*) rather than the product line. The state is LISTED with an accuracy debt on the platform's copy, which is a different problem from absence and one this catalog cannot fix from here. A guessed slug is never evidence against a confirmed listing; the page is.

The mcpservers.org detail page still answers **403** by edge policy, so the sitemap is the evidence for that listing, as it has been since November 4. The Anthropic review status lives only in the portal at `claude.ai/directory/manage`; the feed check is the only public reading available.

## What the window says

Two things worth carrying forward. First, a flat canonical is a precondition and not a verdict: this pass's whole material came from the queue, and the queue was the richest of the day with **27** arrivals. Second, the two ships both earned their slot on the same test - they answer a question with a date and a number that nobody publishes in one place: when the school break actually starts, and whether today's price is above the fifty-one-day low. Neither is a scraper; both refuse out-of-scope requests with a named fix.
