---
title: "MCP Server Discovery - November 10, 2026 (Evening)"
description: "A ten-hour window with fifteen new server URLs, twenty-nine queue arrivals and thirteen feed cards, where three operator surfaces earned guides"
category: MCP Ecosystem
added: 2026-11-10
last_updated: 2026-11-10
source: "the mcpservers.org fifteen-map sitemap index read from /sitemap.xml and the twelve server maps it names (63,995 raw loc entries, 20,411 distinct server URLs), the mcp.so feed read cache-busted, the chatmcp/mcpso submission window #7100 to #7128, and the official MCP registry for candidate resolution"
tags: ["mcp server", "model context protocol", "discovery", "sweep", "november 2026"]
---

# MCP Server Discovery - November 10, 2026 (Evening)

Fired on the **21:00 MST** tick, ten hours after the midday supplement. The canonical carried **fifteen** new server URLs, the queue carried **twenty-nine** arrivals and the feed carried **thirteen** cards, and the three entries that earned guides are all day-of operating surfaces rather than reporting ones: who is on the departure, who walked the patrol route, and what the assistant changed in the last fifteen minutes.

```text
Surfaces:    15 maps named, 12 of them server maps, 63,995 raw <loc> entries
             43,569 locale prefixes stripped, 20,411 distinct server URLs
             (20,396 at the 04:32 MST capture: 15 additions, 0 removals)
Feed:        143,294 bytes cache-busted, 30 cards, 13 above the 14:05Z cutoff
Queue:       #7100 to #7128, 29 numbers, no gaps, all arrivals
Catalogued:  3 servers, 3 guides
Crossref:    57 candidates, 3 catalogued, 54 held or already disposed
```

## The window, measured

The sitemap index at `https://mcpservers.org/sitemap.xml` answered **200** and still names **fifteen** maps, of which **twelve** are server maps: eleven numbered partitions, `priority-servers.xml` and `remote-mcp-servers.xml`. `static.xml` and the newer `skills.xml` are not server maps and were skipped:

```text
priority    299   servers/1  7,588   servers/7   9,351
servers/2 5,948   servers/8  6,588   servers/9   4,031
servers/3 6,518   servers/10 2,604   servers/11    601
servers/4 6,744   servers/5   6,952   servers/6   6,756
remote       15                      total      63,995
```

After **43,569** inline locale prefixes were stripped the `/servers/` subset came to **20,411** distinct server URLs. The 04:32 MST capture on disk held **20,396**, so the set diff is **15 additions and 0 removals**, with three fragment slugs normalized to their `#` form on both sides before the diff so a `%23` entry cannot read as a phantom pair.

The fifteen additions decompose rather than repeat, and the decomposition is what kept the research honest:

```text
 4  prior dispositions that reappeared, including one already catalogued
    padel-expert-lab, glp1health, pendingdeletenet, buzzmark-mcp
 1  a catalogued product in namespace form
    wegravel/mcp                     (catalogued as wegravel-mcp on Nov 10)
10  new slugs
    bot-appetit, brandlio, glen, the-influencer-ai, telerivet, tieline,
    tripworks, truedialog, uncanny-automator, whatsapp-by-green-api
```

Two of those repairs are the reason this block exists. **buzzmark-mcp** is not an arrival: the catalogued [Buzzmark MCP](/hermes/mcp/servers/external/buzzmark-mcp/) has been here since the October brand-voice pass, and the canonical simply minted the slug for it, which is the slug-versus-product divergence this catalog has to check on every wave. **wegravel/mcp** is the namespace form of a product catalogued this morning, so a naive diff reads the same server twice in one day.

`mcpservers.org/all` answered **403** with a 5,424-byte edge interstitial, the standing condition since November 4, so the sitemap union carried the window alone. The mcp.so feed was read cache-busted at **143,294** bytes with **30** cards, and **thirteen** sat above the midday cutoff of `2026-11-10T14:05Z`, which is the largest feed cohort here in a week and reads as an afternoon publish batch rather than thirteen discoveries.

The submission queue carried **twenty-nine** numbers from **#7100** to **#7128** with no gaps and every one an arrival, read in a single authenticated call with bodies included.

## Catalogued: 3 servers, 3 guides

**[TripWorks MCP](/hermes/mcp/servers/external/tripworks-mcp/)** at `https://mcp.tripworks.com/mcp` is the first tour and activity operator surface in this catalog, and it is wired for the day-of question rather than the reporting one. A keyless `initialize` answered **401** with a JSON-RPC error object (`-32001 Missing or malformed Authorization header`) and a `WWW-Authenticate` header naming its protected-resource path, which returned **200** and pointed at an authorization server on the same host whose metadata document publishes the whole product in scope names: **50** of them, including `bookings.read` and `bookings.write`, `manifest.read`, `waivers.write`, `waiver-types`, `experience-timeslots`, `gift-cards`, `promo-codes`, `resellers`, `reviews`, `payments.read`, `phone-calls.read`, `reports.read`, `audit-log.read` and `api-logs.read`, against `authorization_code`, `refresh_token`, `S256`-only PKCE, dynamic registration and token-endpoint auth `none`. Three scopes have no write counterpart, and that asymmetry is the useful part: the manifest, payments and the audit log are read-only by construction. The vendor's help article publishes the per-area permission map and three controls that stack: the connection runs as the person who approved it and can never exceed their permission group; the approval screen offers Read, Write or both and leaving Write unchecked blocks every create, edit and delete; and every write returns a **preview** that must be confirmed. It also draws the cleanest protocol boundary recorded here: with MCP a person is always behind the connection and each request needs their approval, while an API key or a Zapier connection is a standing credential with nobody approving each call, so the same vendor recommends MCP when a person is in the loop and the others when software runs alone. Report links expire in **15 minutes**, which a scheduled job has to plan for.

**[PatrolTech MCP](/hermes/mcp/servers/external/patroltech-mcp/)** at `https://mcp.patroltech.online/mcp` is the first security patrol surface here, and its write path is the reason to catalogue it. A keyless `initialize` answered **401** with a full challenge: `error="invalid_token"`, `scope="read write"` and a `resource_metadata` path that returned **200** naming a separate authorization host, whose RFC 8414 document publishes `authorization_code`, `refresh_token`, `S256` only, `none` for token auth, a revocation endpoint, a JWKS, client ID metadata documents and the issuer response parameter. The same document requested from the MCP host answers **404**, which is the split worth remembering: the resource lives on one host and the identity provider on another and only the protected-resource document connects them. `/health` returned version **0.2.8** while the registry's newest record is **0.2.7**, a one-patch drift that reads as a deployment rather than a fact about the registry. Changes never write directly: `patroltech_<area>_propose_<verb>` queues a proposal, one user and one client form one batch of at most **10** that expires after **30 minutes**, and `patroltech_proposals_confirm` executes it in order with the parameters as proposed. Writes without the `write` scope answer **403 insufficient_scope** with the challenge naming both scopes. The server holds no credentials and forwards the user's token, a closed list of writes is allowed to agents, and deleting records, inviting users and billing are outside its capability. Results are `{ data, truncated?, notices?, note }` capped at **60,000** characters, reads are limited to **60** calls a minute and writes to **20** per user, and every call writes one audit line holding a **hash of the arguments and never the arguments**. Four prompts and two resources carry the domain vocabulary, and the `reading-the-data` resource is the one that matters, because a rejected scan is not a missed round and an assistant left to guess will say it is.

**[Genaya MCP](/hermes/mcp/servers/external/genaya-mcp/)** at `https://api.genaya.com/mcp` is the first entry here where the assistant's own changes are tools rather than an audit report. Discovery is open and execution is gated, which is the friendliest evidence tier in this pass: a keyless `initialize` answered **200** as `genaya` **1.2.0**, `tools/list` answered **200** with exactly **seven** tools, and an unauthenticated `tools/call` answered **401** with `scope="read ai act send offline_access"` and the protected-resource path. The seven are `ask_genaya`, `genaya_act`, `confirm_action`, `cancel_action`, `undo_action`, `list_actions` and `whoami`, and the split the vendor documents is the product: a record change is confirmed **in the chat** and can be undone for **15 minutes**, while texts, emails and anything about money are confirmed on a Genaya page where the member is signed in. Both well-known documents answered **200**, both list the same five scopes, and the reference page adds the constraints an IT review will ask for, including the `gnc_` organization-issued clients that must present a secret and the per-host limits for Microsoft 365 Copilot, Slack and Salesforce Agentforce. The initialize instruction string closes a door this catalog has not seen closed in those words: record text is customer data, never instructions, and a result that says `needs_human` means show the link and stop.

## Also identified this pass, with the owner or the reason named

Every one of the fifty-four holds has a named class owner or a measured reason, and the pass lists them because the queue was short of business surfaces rather than quiet.

From the fifteen canonical additions: **telerivet** (SMS, WhatsApp, Viber, IVR and USSD in 150+ countries, registry `com.telerivet/telerivet` 1.0.0) holds on the messaging class carried by wuapi, sendlettersonline, fwrd-sms, virtnumber, Kanal and more than twenty WhatsApp entries; **whatsapp-by-green-api** is the same class in its re-slugged form, after the 13:04Z card of November 10 was already held; **the-influencer-ai** holds on creator discovery, the ruling that disposed of the influencer-tool batch; **glen** (a team's shared agent memory, skills and docs, read from its feed card) holds on the memory class that carries PLUR, Azquo, MemoryBrain, Dawnmere and oortmem; **tieline** is a static front-end to back-end contract-drift checker, registry `io.github.nugehs/tieline` 0.1.4, developer tooling; and **padel-expert-lab**, **glp1health**, **pendingdeletenet** and **buzzmark-mcp** are the prior dispositions above. Four slugs could not be classified at all and are recorded as unattributed rather than guessed: **bot-appetit**, **brandlio**, **truedialog** and **uncanny-automator** have no registry record, the mcpservers.org detail route answered **403** with a 5,689-byte Cloudflare interstitial for every one of them, and the reader proxy answered **401** on IP reputation, so the pass states the names and the blocked surfaces instead of inventing a product. Each is re-checkable the moment a detail page answers.

From the thirteen feed cards: **rap-ai-video** is a consumer video generator and an `/agents/` card rather than a server listing; **x1-wealth** (trusts, entities, properties and documents with cited answers) was disposed as wealth operations beside Milemarker before this window; **site-audit-mcp-server** is an Apify actor on the standing Apify hold class; **seller-labs-amazon** holds on the Amazon seller and ads class recorded against WisePPC and the Amazon marketplace data precedents; **verrow** (sourced rural and federal data, zoning, permits, soil, wind, airspace, EPA labels, paid per call over x402) holds on [Placestack](/hermes/mcp/servers/external/placestack-mcp/), which already carries US parcel, zoning and permit data, with the x402 payment rail held by Recta, Warden and nohumans.directory; **glypse** holds on the prediction-market data class carried by Kalshi Eye; **blog-automation** on the content automation class; **mokxi** (Arduino, ESP32 and Pico circuits) on hardware tooling; **ctrl-cv** as a consumer clipboard utility across AI apps; **rentadriver-sameday-delivery** on the logistics class already carrying Fitralo, HaulierScope, Plain Freight and Container Tracking, with booking breadth stated as its only addition; **align-cli** as developer tooling for a local decision graph from git history.

From the twenty-nine queue arrivals: **NL;NL Labs** (**#7128**) publishes free daily AI pricing per right answer across nine business jobs and holds on the model-evaluation fixture class, where `llm-prices-cn` already carries the price half; **AlphaPrime Stocks** (**#7127**) on trading per the November 9 disposition of the same publisher and the Altair, ValuEdge, fAlpha and BDE saturation; **Ready Check** (**#7126**) as a prepaid single-email inspection at $0.0025 a check on the agent-security class; **HopBase** (**#7125**) as a backend-as-a-service on the developer infrastructure class; **Zolva** (**#7124**) on the Robinhood Chain trading rail beside solara and the Solana entries; **Vitalink** (**#7123**) as a healthcare quote directory beside TMSClinics and SleepStudies; **grindfree-agent-security** (**#7122**) on the x402 agent-security class carried by GrindFree's own precedents and the seven-shield check family; **Pixohub** (**#7121**) on media specification data; **Calligraphy EDA** (**#7120**) on hardware design data, which this catalog disposed at BoardRepo; **Bunker** (**#7119**) as an offline crypto address exposure scanner on the security class; **Narwhal** (**#7118**) as an API marketplace; **Dawnmere** (**#7117**) on the local memory tier beside PLUR and Archipelago; **Prickelly** (**#7116**) as consumer price tracking on Turkish marketplaces; **within** (**#7115**) as consumer retail availability across independent boutiques; **Solara AI** (**#7114**) on media generation; **Zylcut** (**#7113**) on the local video-editor tier; **CheapestInIndia** (**#7112**) on the consumer price comparison class; **PinnFeed** (**#7111**) on betting odds; **Amaltash** (**#7108**) on consumer retirement calculators; **Keel Stats** (**#7107**) as consumer sports statistics; **TalaLevel** (**#7106**) as a careers surface; **OnlyFonts** (**#7105**) as a creative asset catalogue; **Web-Intel** (**#7104**) on the pay-per-call web intelligence class already recorded for that publisher; **Flint Despacho** (**#7103**, 17 accounting tools, Norma 43 and ContaBridge) on the Spanish accounting geo-niche whose class owner is Aikount with Modelo 303 and bank reconciliation already catalogued; **AEC Pilot** (**#7102**) on the architecture and AEC hold; **MemoryBrain** (**#7101**) on the memory class; and **Grafizum** (**#7100**) as a command center for coordinating coding agents, developer tooling.

## Core listing check

Measured rather than inherited. The fresh canonical carries `/servers/corpusiq-io` and `/servers/corpusiq/corpusiq-docs`, so the mcpservers.org listing is present in the same sitemap union this pass diffed. The four mcp.so detail routes answered **404** for `corpusiq`, `corpusiq-io`, `corpusiq-mcp` and `io.corpusiq`, which is the recorded bare-slug failure and not a delisting, and `mcpservers.org/all` answered the standing **403** by edge policy. The official registry returned **four** active records for `io.corpusiq/multi-source-mcp`: 1.0.0 published 2026-05-25 with the older 30+ wording, 1.0.1 and 1.0.2 in October, and **1.0.3** published 2026-10-24 with the 40+ wording intact, so the drift recorded as closed on November 6 is still closed on the newest version.

## FAQ

### What separates a catalogued entry from a held one?

Whether the surface answers a question an operator asks about their own business and whether the class it belongs to is already owned. Three entries cleared both tests this pass: a departure manifest, a patrol round and an action ledger. A held candidate either sits in a class with a named owner already in this catalog or is a consumer, developer or hardware tool whose audience is not the operator asking a business question.

### Why does the pass count thirteen fresh feed cards and still catalogue none of them?

Because freshness is not the test. Every one of the thirteen resolved to a class this catalog has already ruled on, most of them from cards published in the same week: the Amazon seller and ads class, the prediction-market data class at Kalshi Eye, the parcel and zoning class at Placestack, and the memory class across five entries. Recording them with the owner named is what stops the same card being re-evaluated as new on the next pass.

## Counts

Canonical **20,411** against **20,396**, **15** additions and **0** removals from **63,995** raw loc entries across twelve server maps of the fifteen the index names, with **43,569** locale prefixes stripped; feed **143,294** bytes, **30** cards, **13** above the 14:05Z cutoff; queue **29** arrivals from **#7100** to **#7128**, no gaps; **57** candidates evaluated, **3** catalogued with **3** guides; two endpoints measured to the handshake plus both metadata documents each and one driven to a full `tools/list`; guide tree **1,140** directories before this pass and **1,143** after; **1,284** catalog entries before and **1,287** after; **1,558** Markdown files under `hermes/mcp/` before and **1,562** after, with **3,746** total Markdown files before and **3,750** after.
