---
title: "MCP Server Discovery - November 12, 2026 (Midday)"
description: "A set-identical canonical and six fresh cards, and one entry that refuses a date it has not checked - Spanish autónomo tax, driven live"
category: MCP Ecosystem
added: 2026-11-12
last_updated: 2026-11-12
source: "the mcpservers.org sitemap index read at 2026-11-12T17:0xZ with the twelve server maps fetched and diffed against the 10:03Z capture kept on disk, the mcp.so feed read cache-busted at 143,765 bytes and parsed card by card from the M/D/YYYY stamp in the title attribute, the chatmcp submission queue read from #7193 to #7219 in one authenticated call, the official MCP registry queried by product name, and one live session on this host against https://kuotia.com/mcp: initialize, tools/list, eight tools/call requests, one in-band auth error inspected at its metadata, plus both the protected-resource and authorization-server documents fetched"
tags: ["mcp server", "model context protocol", "discovery", "sweep", "november 2026"]
---

# MCP Server Discovery - November 12, 2026 (Midday)

Fired on the **10:00 MST** tick, seven hours after the night pass shipped four. The canonical came back set identical to that pass's capture, so the window is the feed and the queue again, and the one entry that ships earned it on behaviour rather than on size: a tax server that refuses to state a date it has not checked.

```text
Surfaces:   /sitemap.xml 200, fifteen maps named, twelve carrying /servers/ URLs
            64,577 raw <loc> entries in those twelve, against 64,573 at 10:03Z
            per-map: priority 299 (held), 1 7,588 (held), 2 5,948 (held), 3 6,518 (held),
            4 6,744 (held), 5 6,952 (held), 6 6,756 (held), 7 9,351 (held), 8 6,589 (held),
            9 4,031 (held), 10 2,606 (held), 11 1,195  (+4 raw)
            distinct locale-stripped keys 20,885 = 20,885, 0 additions / 0 removals
Feed:       143,765 bytes, 34 anchors, 30 stamped cards, 6 above the 10:03Z cut-off
Queue:      #7193 - #7219 in one call, 27 arrivals with no gaps
Catalogued: 1 server, 1 guide   Held: 34 candidates with the class owner named
Core check: mcpservers.org 403 by edge policy, mcp.so 404 beside a 200 control, Glama 200
```

## The window: four entries more and no key more

The sitemap index at `/sitemap.xml` answered **200** and named **fifteen** maps, **twelve** of them carrying `/servers/` URLs (`priority-servers.xml` plus `servers/1` through `servers/11`), with `skills.xml`, `static.xml` and `remote-mcp-servers.xml` outside the server set. Those twelve returned **64,577** raw `<loc>` entries against **64,573** at the 10:03Z capture, and the whole of the movement is `servers/11` going from **1,191** to **1,195**: every other map held its count to the entry, and `priority-servers.xml` held at 299.

Four raw entries and no key more, which is the part that has to be measured rather than assumed. Normalising to the locale-stripped key set gave **20,885** keys on both captures, **0 additions** and **0 removals**. This pass did not stop at the raw delta and did not report it as arrivals: a raw entry can be the same product served under a second form, and on this surface that has been the explanation three passes running. The four extra entries are re-served forms, not four new products.

## The feed: six cards in seven hours

The mcp.so feed answered **200** at **143,765** bytes with **34** card anchors resolving to 30 stamped cards and 7 unstamped rails. Timestamps live in the `title` attribute in the `M/D/YYYY, HH:MM AM/PM` form and are **UTC**, so each was converted before the window comparison. Six cards sit at or above the 10:03Z cut-off:

```text
alba-design-1cb91b   15:20Z   design utility, no operator data surface
courio-f46da1        15:14Z   unresolved, detail route blocked (see below)
quo-878285           14:30Z   unresolved, detail route blocked (see below)
ctlogs-dev-…         13:11Z   certificate transparency, class owned by the catalogued CTlogs.io
remote-nomad-jobs    12:13Z   jobs class, carried by roTEAMnet and the hiring entries
deltabridge-…        10:11Z   threat intelligence, security class
```

The three unresolved tags are recorded as unresolved and not inferred from their slugs. `https://mcp.so/server/<slug>` answers "Only HTML requests are supported here" to a JSON-RPC probe, which is the route's own message and not a dead listing, and the reader proxy refused all five detail fetches with **401 bad IP reputation**, the standing condition since November 4.

## Catalogued: Kuotia MCP

[Kuotia MCP](/hermes/mcp/servers/external/kuotia-mcp/) from submission **#7219**, keyless at `https://kuotia.com/mcp`, registry `com.kuotia/kuotia` **1.0.1**. `initialize` returned **200** as `Kuotia` **1.0.1** on protocol `2025-06-18` with tools only, and `tools/list` returned **nine** tools: four public read-only (`kuotia_get_tax_calendar`, `kuotia_estimate_reta`, `kuotia_estimate_net_income`, `kuotia_get_autonomo_guide`), four reading a gestoría client's own record, and one write annotated `destructiveHint: true` that sends only text the client approved with an `idempotency_key`.

Eight calls were driven. **The finding is the refusal**: modelo 303 for `2026-T3` answered a verified `deadline: 2026-10-20` with its `direct_debit_cutoff` and an AEAT source, while the same modelo for `2026-T4` returned `isError: true`, code `not_verified`, the statutory window "del 1 al 30 de enero del año siguiente" and the IVA law as its source, rather than presenting the general rule as the checked date. The estimators were driven to a **reproduced control**: 30,000 income with 5,000 expenses in Madrid returned 4,570.56 in contributions, 2,775.29 in IRPF and 17,654.15 net, which are the vendor's own published figures for the same example to the cent, and the RETA call returned tramo **5** between 380.88 and 639.45 as the vendor's page states. Two argument-shape findings are recorded for whoever writes the prompt: `period` needs `2026-T3` (a plain "4T" fails the `^20\d\d(-T[1-4])?$` pattern) and `region` needs the lowercase key `madrid`, not "Madrid".

The connected half was measured to its gate and not driven, because no Kuotia account exists on this host. That gate is worth the paragraph: a connected tool called without a connection answers **HTTP 200** with `isError: true` and `_meta["mcp/www_authenticate"]` carrying `error="insufficient_scope"`, `scope="kuotia:gestoria:read"` and the protected-resource pointer, so a client reading only the status code would show the operator nothing. The protected-resource document names one authorization server and exactly two scopes, and the RFC 8414 document publishes `authorization_code` plus `refresh_token`, `none` as the only client auth method, S256 only, and client ID metadata documents supported.

## Held, with the owner named

**Sales and lead data.** **Nock** (`com.usenock/nock` 1.0.0, `https://api.usenock.com/mcp`) is the strongest candidate of the queue and is held on class: a keyless `initialize` answered **401** with `resource_metadata` and `scope="openid profile email"`, the protected-resource document names Clerk as the issuer, and the registry describes Brazilian B2B prospecting with buying signals, company and people search, enrichment and outreach. The lead-generation class already carries [Leadbay](/hermes/mcp/servers/external/leadbay-mcp/), [Vibe Prospecting](/hermes/mcp/servers/external/vibe-prospecting-mcp/), VOYGR and Layrcake, AskBond and Skael were held in the same slice, and Brazilian company data itself was held at **Fichário** on the regional CNPJ rule recorded against apipj, OpenBase, Corporary and Fuentio. Recorded as the closest call of the pass.

**Ads and creator intelligence.** **LaunchSpy** (`io.launchspy/launchspy` 1.2.0, published today at 14:02Z) answers **401** with `missing_api_key` off a protected-resource document carrying one scope, `mcp:read`, over a database of coaches and course creators with their Meta ads, hooks and funnels. Held on the ad-library class, which carries [Ad Library Intelligence](/hermes/mcp/servers/external/ad-library-intelligence-mcp/), [Adspy](/hermes/mcp/servers/external/adspy-mcp/), [SpyWinAds](/hermes/mcp/servers/external/spywinads-mcp/) and the openadlibrary hold.

**Class holds from the queue.** Statuz (social scheduling, the class carried by UniPost, Postkey and FeedSquad), Felku Connect (WhatsApp and Telegram, the messaging class), **HolicAudit** and **Cygnix SEO MCP** (SEO and AI-crawler visibility, the twenty-guide SEO class with Cygnix SEO already catalogued), **Dotmira** (30,000 web effects and UI components, design-asset class), **UTM Watch** (local macOS VM history, local-install tier), **VextCAD** (text-to-CAD, manufacturing and industrial class carried by MechanoFab), **YorkerAPI** (cricket data, consumer sports), **garmlink** (Garmin health data, consumer health), **HappyKeywords** (macOS-only ASO app server, local-install tier), **okdata** (Chinese and global social data, the saturated social-data class), **abap-config-mcp** (SAP developer tooling), **TruthTrail**, **Sniptide**, **Crossdrive**, **while.sh**, **Rush**, **StatsPAI**, **Soko-kun**, **Pleso Therapy**, **Vidmoat**, **Roilo**, **SightRadar**, **Loop Marketing** and **Dotmira**'s siblings by class, and **Kuotia**'s own gestoría sibling pages as one publisher. **SealGuard**, **Aalto**, **Agent Demand Registry**, **volatiai** and the **mambalabsdev** fleet carry their previous dispositions without re-litigation.

**Core listing check, measured rather than inherited.** `https://mcpservers.org/servers/corpusiq-io` answered **403** by edge policy, which is the standing condition and not a delisting. On mcp.so the four slugs answered **404** while the control `https://mcp.so/servers/anyreach`, lifted from the live feed minutes earlier, answered **200** in the same request batch, so the absence is a listing that is not there rather than a routing quirk. Glama answered **200** on the CorpusIQ record. The Smithery registry query returned an error envelope on this read and is recorded as a query-surface error, never as a delisting.

## Numbers for this pass

```text
Raw <loc> entries:            64,577  (64,573 at 10:03Z, +4 in servers/11)
Distinct locale-stripped keys: 20,885  (20,885 at 10:03Z, 0 additions / 0 removals)
mcp.so feed:                  143,765 bytes, 34 anchors, 30 stamps, 6 above cut-off
Submission queue:             27 arrivals, #7193 to #7219, no gaps
Servers catalogued:           1   Guides written: 1
Endpoints driven:             1   (eight tools/call requests, plus one auth-gated call inspected)
```
