---
title: "MCP Server Discovery - November 21, 2026 (Midday)"
description: "A flat directory window where both push surfaces carried four new products: a sovereignty directory, a gig calendar, a geoscience surface and a press desk."
category: "MCP Ecosystem"
last_updated: "2026-11-21"
---

# MCP Server Discovery - November 21, 2026 (Midday)

Fired on the **10:00 MST** tick, seven hours after the night pass closed on the capture it stamped **10:00Z**. The directory came back identical on every reading, so the whole window came from the two push surfaces - and they produced four products, each first of its class or a distinct slice of one.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          36,971   IDENTICAL map for map to the night capture
  servers/1  ..... 4,153     servers/7  ..... 5,878     sums to 36,971 exactly
  servers/2  ..... 2,526     servers/8  ..... 2,716
  servers/3  ..... 2,995     servers/9  ..... 2,609
  servers/4  ..... 3,172     servers/10 ..... 2,592
  servers/5  ..... 3,367     servers/11 ..... 2,539
  servers/6  ..... 2,879     servers/12 ..... 1,545
distinct keys, maps 1-12      23,220   against 23,220         (0 / 0)
URLs per key                   1.59   against 1.59
priority-servers.xml            262 raw,  34 distinct keys
remote-mcp-servers.xml           15 raw
lastmod, server maps          33,411 stamped pairs; ZERO rows at or after 10:00Z
mcp.so /feed                  200, 157,379 bytes, 35 anchors, 30 stamps
                              TWO cards above the cutoff
submission queue              #7758 to #7773, sixteen arrivals
```

## A flat window, proved three ways

The raw count, the per-map block and the distinct key set all agree, and the `lastmod` scan agrees with them:

1. **36,971** raw `<loc>` entries, mapped one for one against the night capture's numbers, summing exactly to the stated total.
2. **23,220** distinct locale-stripped keys on both sides, at the same **1.59** URLs per key - so nothing was added, removed or re-sharded.
3. **Zero** `lastmod` rows at or after the 10:00Z cutoff across **33,411** stamped pairs in the twelve server maps.

Two notes on the arithmetic, because both have produced phantom findings on this surface before. The night page printed **23,219** twelve-map keys where this pass computes **23,220** on both its own capture and the derived baseline; the one-key difference is a normalisation edge on a `%23` fragment and the like-for-like set diff is what settles it - **0 additions, 0 removals** on the twelve map plus priority basis. And the remote map serves its slugs under `remote-mcp-servers/<slug>` with locale prefixes, so a naive union against a twelve-plus-priority baseline reports fifteen "additions" that are fifteen URL forms of one slug (`clockwise`). Neither is an arrival.

The `/all` pages were not re-read: the surface has answered 403 by edge policy since 4 November.

## Where the material came from

**Feed.** 200 at **157,379** bytes, 35 server anchors, 30 stamps, two cards above the cutoff: `outstand-so` at **15:30Z** and `askhooman` at **13:30Z**. The three earlier cards on the page (`cortex66` and `ai-checker-humanizer-b54a66` at 07:58Z, `pitbi` at 07:12Z) belong to the night pass and are not counted here.

**Queue.** `chatmcp/mcpso` carried **#7758** to **#7773**, sixteen arrivals with bodies read in one authenticated call. That is the whole delta of a seven-hour window, and four of the sixteen earned guides.

## Shipped: four, all keyless or measured to the gate

### Europe Instead - the first vendor-sovereignty entry

Submission **#7765**, `https://europeinstead.com/mcp`, registry `com.europeinstead/europe-instead` **1.0.0**, five tools, no auth. Every tool carries two independent answers built from sourced facts: an **origin score 0-100** (legal entity 30, ownership 30, operations 15, data residency 15, openness 10) and an **exposure level 1-5**. Eleven `tools/call` requests were driven keyless.

The measurement that justifies the guide: **Wire scores 100 / 100** with each part verified and the imprint quoted - and still reads exposure **level 3**, *"Account or support data leaves Europe"*, `disclosed: false`. Brevo scores **93**, loses seven points on `openness`, reads exposure **level 4** with `disclosed: true`, and its residency note names the arrangement - *"OVH in France and Google Cloud in Belgium"*. A perfect origin score is not a promise about data, and this server is the clearest place in the catalogue to see why. `Slack` returns **20** alternatives, `crm` returns **27** tools, and the network-level facts carry `source_url`, a quoted passage and a `checked_at` date each.

### djbnb - the first event-calendar entry

Submission **#7771**, `https://djbnb.com/mcp`, registry `com.djbnb/djbnb` **1.0.0**, two tools and one MCP Apps resource, no auth. `list_cities` returns **17** US cities; `whos_playing` returned **11** nights in Detroit and **40** in New York for the same weekend question - a ratio a model would not guess. Door prices appear when the venue published one (`$20 cover`, `Free`), and each night links its own event page. The unknown-city refusal names all seventeen covered cities, and the one enum argument refuses `weekend` while accepting `this_weekend`. `resources/read` on `ui://djbnb/night-card-v1.html` returns **10,456** bytes of `text/html;profile=mcp-app`, so the card is a real client-rendered view rather than a second API.

### AgenticGeoMate - first of class, at the documented tier

Submission **#7758**, `https://geomate.nlp-tlp.org/mcp`, registry `io.github.PascalSun/agenticgeomate` **1.1.0** published **2026-11-21T10:51:01Z**. Geoscience had no owner anywhere in this catalogue - the string appeared in no guide, no section and no row. **92 tools** were listed keyless: tenure, drillholes and intercepts, geochemistry, a WA prospectivity model over eight metals, exploration-report corpora, a data library and a read-only SQL surface. Six `tools/call` requests across six tool families all returned **401**, with a complete `WWW-Authenticate` naming `resource_metadata`, a protected-resource document that answers **200** on both the bare and `/mcp` routes and names one authorization server, and nothing on the parent host.

That makes it the **discovery-open, execution-gated** tier in its purest form: the whole surface is readable before the sign-in, and not one answer is. The guide records the tool surface and the gate, and states explicitly that no tool response was read on this pass.

### Startups Españolas press desk - the receiving half of press

Submission **#7768**, `https://app.startups-espanolas.es/mcp`, registry `es.startups-espanolas/notas-de-prensa` with domain ownership verified by DNS TXT, four tools. Three were driven keyless: `ver_medios` returns the three publications of the network with their topics and criteria pages, `ver_condiciones` returns the whole contract - **5 free notes per sender**, then **19 EUR** for ten, **69** for fifty, **99** for a hundred, **199** for two hundred and fifty - with paid notes labelled *contenido patrocinado* and `rel=sponsored`, free notes `rel=nofollow`, publication an editorial decision, and the closing sentence *"Esta herramienta nunca mueve dinero"*. `estado_nota` on an unknown ticket returns `estado: unknown` rather than an error. `enviar_nota` was left undriven because it emails a confirmation to a real sender and opens a human editorial queue.

[Comunicate MCP](/hermes/mcp/servers/external/comunicate-mcp) already owns paid placement distribution here; this is the editorial intake of one network, which is the other half of the job, and the guide states the distinction rather than claiming novelty on the category. One measured nuance is recorded too: `language: "en"` translates the topics and the acceptance prose but left the `accepts` body in Spanish, so it is a partial translation and not a switch.

## Held, with the gate or the class named

Eleven, from the other twelve queue arrivals and the two feed cards:

```text
#7773 Beamfar website monitoring   OAuth 401 (no keyless read) plus the monitoring rows
#7772 Vexo Analytics               OAuth 2.1 plus the product-analytics and session-replay rows
#7770 whittle-mcp                  local CLI filter, developer tooling not business data
#7769 Clipbeat                     media generation (music video) plus a bearer key; class saturated
#7767 RecPix                       local macOS app, requires the app installed to answer anything
#7766 GotEmail                     inbox access on a Mac; email and inbox class saturated
#7764 polarka-agent                agent wallet on the x402 class (SaltCrate Oracle, Reciprocal Ruler)
#7763 rcs-ads-mcp                  } one vendor fleet of four: Yandex Direct, VK Ads,
#7762 RCS Cloud Connector          } Bitrix24 and 1C Enterprise - advertising and ERP
#7761 bitrix24-mcp                 } classes already carried, and one author submitting four
#7760 mcp-1c                       } items in sixty seconds
#7759 Nubbo                        OAuth 2.1 plus the S3 object-storage row already catalogued
feed outstand-so                   social publishing and scheduling, a saturated class
feed askhooman                     needs a phone-app account; agent-to-human approval class
```

## Listings, re-measured

The five surfaces the cron exists for were each measured rather than inherited:

| Surface | Reading |
|---|---|
| mcpservers.org | **LIVE** - `https://mcpservers.org/servers/corpusiq-io` present in `servers/5.xml` of the fresh capture, beside the docs mirror at `servers/corpusiq/corpusiq-docs` |
| mcp.so | **NOT LISTED**, unchanged - `/server/corpusiq`, `/server/corpusiq-io`, `/server/corpusiq-mcp`, `/server/io.corpusiq` all 404 |
| glama.ai | **LISTED** - `/mcp/connectors/io.corpusiq/multi-source-mcp` answers 200, title *CorpusIQ - MCP Connector* |
| smithery.ai | **LISTED** - the registry record for the CorpusIQ server answers 200 under the `Cprusiq` qualified name, display name CorpusIQ |
| Anthropic Connectors Directory | unchanged by the watch script; review status lives only in the portal |

## What the window taught

- **A flat canonical is a precondition, not a verdict.** Three independent readings agreed that nothing arrived, and the pass still shipped four guides, because the arrivals moved on the feed and the queue while the sitemaps stood still.
- **The first-of-class finds are in the queue, not the crawl.** Geoscience, event calendars and vendor sovereignty all arrived as submissions before they arrived as slugs.
- **A big tool surface is a brief, not a result.** Ninety-two tools were readable without a token and not one was callable; the guide ships the surface and says plainly that it measured the gate and stopped.
- **Two scores beat one.** Europe Instead separates "how European" from "who can reach the data", and the two disagree on the same product - which is the whole argument for asking both questions.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [Europe Instead MCP](/hermes/mcp/servers/external/europe-instead-mcp)
- [djbnb MCP](/hermes/mcp/servers/external/djbnb-mcp)
- [AgenticGeoMate MCP](/hermes/mcp/servers/external/agenticgeomate-mcp)
- [Startups Españolas Press Desk MCP](/hermes/mcp/servers/external/startups-espanolas-press-desk-mcp)
