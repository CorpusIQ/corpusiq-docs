---
title: "MCP Server Discovery - November 12, 2026 (Midday Supplement)"
description: "One hour, one raw entry and thirteen stamp bumps that were not arrivals - and two OAuth products from the feed: an on-call calendar and a WhatsApp pipeline"
category: MCP Ecosystem
added: 2026-11-12
last_updated: 2026-11-12
source: "the mcpservers.org sitemap index re-read cache-busted at 2026-11-12T18:0xZ with the twelve server maps fetched individually, per-map counts compared to the 17:01Z capture and every lastmod at or after 17:05Z enumerated, the mcp.so feed read cache-busted at 144,264 bytes and parsed card by card from the M/D/YYYY stamp in the title attribute, the chatmcp/mcp-directory submission queue read through the GitHub API from #7193 to #7223, the official MCP registry queried for both catalogued products, and live keyless probes of both endpoints at 18:05Z with each protected-resource and authorization-server document fetched"
tags: ["mcp server", "model context protocol", "discovery", "sweep", "november 2026"]
---

# MCP Server Discovery - November 12, 2026 (Midday Supplement)

Fired on the **11:00 MST** tick, one hour after the midday pass shipped Kuotia. The canonical was flat to the key and not flat to the stamp, which is the distinction this page exists to record: **thirteen** listings on mcpservers.org were re-stamped inside the hour, and **not one of them is a new product**. Both entries that shipped came from the mcp.so feed, and both are OAuth services with an operator-facing control surface rather than another reporting dashboard.

```text
Surfaces:   /sitemap.xml 200, fifteen maps named, twelve carrying /servers/ URLs
            64,578 raw <loc> entries in those twelve, against 64,577 at 17:01Z
            per-map: priority 299 (held), 1 7,588 (held), 2 5,948 (held), 3 6,518 (held),
            4 6,744 (held), 5 6,952 (held), 6 6,756 (held), 7 9,351 (held), 8 6,589 (held),
            9 4,031 (held), 10 2,606 (held), 11 1,195 -> 1,196  (+1 raw)
            distinct locale-stripped keys 20,885 = 20,885, 0 additions / 0 removals
            lastmod at or after 17:05Z: 43 rows -> 13 distinct listings
Feed:       144,264 bytes, 34 card anchors, 30 stamped cards, 27 paired to a slug
            2 above the cut-off: hank 17:21Z, rushcrm 17:38Z
Queue:      #7193 - #7223 through the GitHub API, 4 arrivals after the midday read
Catalogued: 2 servers, 2 guides   Held: 12+ with the class owner named
Core check: mcpservers.org detail 403 by edge policy, mcp.so detail route 200 to HTML
```

## The window: one raw entry, no key, thirteen stamps

The sitemap index answered **200** and named **fifteen** maps, **twelve** of them carrying `/servers/` URLs. Those twelve returned **64,578** raw `<loc>` entries against **64,577** an hour earlier, and the entire movement is `servers/11` going from **1,195** to **1,196** while every other map held its count to the entry, `priority-servers.xml` included at **299**.

Normalising to the locale-stripped key set gave **20,885** keys on both captures: **0 additions**, **0 removals**. One raw entry, no product.

Then the stamps, which is where this hour differs from the night pass:

```text
lastmod >= 2026-11-12T17:05Z   43 raw rows
distinct listings after locale-stripping   13
new keys among them    0
```

Thirteen listings were re-indexed inside the hour - `n24q02m/better-notion-mcp` at 17:08Z, `eiry16/beacon-mfg` at 17:11Z, `daghis/teamcity-mcp` at 17:13Z, `tencentcloudbase/cloudbase-ai-toolkit` at 17:16Z, `jgravelle/jcodemunch-mcp` at 17:18Z, `mediar-ai/screenpipe` at 17:20Z, `1mcp-app/agent` at 17:25Z, `wlsdks/ontology-atlas` at 17:29Z, `lakshmanturlapati/fsb` at 17:29Z, `www-regdatalab-com-mcp` at 17:38Z, `enkiduhub/mentionforge` at 17:43Z, `mambalabsdev/mcp-reddit-search-thread-scraper` at 17:47Z and `heygen-com/hyperframes` at 17:52Z. Every one of them was already in the key set at 17:01Z, so a stamp is a re-index and not an arrival - and this is exactly the reading the November 11 night pass warned about, where a stamp cut-off overstates arrivals by an order of magnitude.

The one raw entry that did arrive is a re-served locale form of a page already counted, which is why the number that matters is **20,885 on both sides** and not the +1.

## The feed: two fresh cards in an hour

The mcp.so feed answered **200** at **144,264** bytes - **34** card anchors, **30** stamped cards in the `M/D/YYYY, HH:MM AM/PM` form, **27** of them pairing to a slug inside the card window. Two sit above the 17:05Z cut-off:

```text
hank      17:21Z   AI receptionist for restoration and home services   -> catalogued
rushcrm   17:38Z   Brazilian WhatsApp CRM with an OAuth MCP server     -> catalogued
```

The cards below them - `alba-design` 15:20Z, `courio` 15:14Z, `quo` 14:30Z, `ctlogs-dev` 13:11Z, `remote-nomad-jobs` 12:13Z, `deltabridge` 10:11Z, `billdog-io` 08:40Z - carry the midday pass's dispositions and are not re-litigated here.

## The queue: four arrivals, all held

The submission queue lives at `chatmcp/mcp-directory`, and the API redirects `repos/chatmcp/mcp-directory/issues` to repository id **899309258**, which is worth knowing because the redirect returns a JSON body rather than the list. From **#7193** to **#7223** in one call, four were created after the midday read:

```text
#7220  17:08Z  phonedriver      io.github.hridaya423/phonedriver
#7221  17:13Z  Magic Translate  io.magictranslate/mcp
#7222  17:39Z  Headshot Photo Check  de.profilfoto-ki/headshot-check
#7223  17:59Z  Louis Studios    com.lou15.studios/designer
```

All four are read and held: two are single-purpose utilities (a phone driver, a translation wrapper), one is an image compliance check for a photo product, and Louis Studios is a design asset surface. None of them answers a business-operations question this catalog does not already cover.

## Catalogued: Hank MCP

[Hank MCP](/hermes/mcp/servers/external/hank-mcp/) from feed card 17:21Z, remote Streamable HTTP at `https://app.dialhank.com/api/mcp`, registry `com.dialhank/hank` **1.0.0**. A keyless `initialize` answered **401** with `resource_metadata` and the protected-resource document named **two** scopes, `hank.settings.read` and `hank.settings.write`, with `header` as the bearer method; the RFC 8414 document published a **registration endpoint**, `code` as the only response type, `authorization_code` plus `refresh_token`, `none` as the only token auth method and **`S256`** only.

The product is an AI receptionist for restoration and home-service companies, and the interesting part is what the tools edit: the **on-call rotation**, the transfer routes and their calling orders, office hours, lunch and holiday closures, service-area ZIP codes and the lead policy - **40** tools in the vendor's reference, led by `explain_call_routing`, `plan_routing_change` and `apply_routing_change`. The plan primitive is worth the page: a plan **expires**, is bound to the user, app, organization, location and environment that created it, and `apply_routing_change` refuses expired, changed, differently scoped or unauthorized plans and returns the recorded result on a repeat. Underneath it the permissions page states the operator controls plainly - the assistant holds your role, office hours and lead policy are Admin and Owner only, removals preview first, changes that would leave a routing gap are refused, an audit log records every action **without the values**, and a read-only connection still reads transcripts and caller details through `search_calls`.

Two honest limits are recorded on the page: no Hank account exists here, so the 40 tools are the vendor's documentation rather than a measured `tools/list`, and the collection half was not driven.

## Catalogued: RushCRM MCP

[RushCRM MCP](/hermes/mcp/servers/external/rushcrm-mcp/) from feed card 17:38Z, remote Streamable HTTP at `https://rushcrm.com.br/api/v1/mcp/<account-slug>`, registry `br.com.rushcrm/crm` **1.0.0**. The keyless probe answered **401** with `resource_metadata` on the concrete org path the listing publishes, beside a **100 requests** rate-limit header and Cloudflare in front. The protected-resource document named **three** scopes in Portuguese - **`leitura`**, **`escrita`**, **`exclusao`** - and the authorization-server document published `/oauth/autorizar`, `/api/v1/oauth/token`, a registration endpoint, `/api/v1/oauth/revoke`, `code` only, `authorization_code` with `refresh_token`, `S256` only and `none` as the token auth method.

The product is a Brazilian WhatsApp CRM, and the vendor's README publishes **36** tools across contacts, deals and pipelines, activity, WhatsApp conversations, tags and forms, team targets and automations. Three details earn the guide: **`exclusao` is a separate scope from `escrita`**, so an assistant asked to keep the pipeline tidy never needs deletion rights; **the account administrator switches each tool on or off** in Settings → API → MCP Server, so the surface is per-connection rather than per-plan; and the automation group ships **`automacao_validar`** and **`automacao_simular`** beside create and update, which is the same plan-then-apply shape one layer up. Access tokens last **one hour**, the refresh token rotates on each use, and message sending passes the CRM's own pacing protections so the number is not put at risk.

Published pricing is in BRL and **API and MCP are a row in the plan comparison rather than an add-on**: 300 calls an hour on Starter at R$ 208 a month, 1,000 on Growth at R$ 348, 5,000 on Scale at R$ 698 and 5,000 on Enterprise from R$ 1,997. The page was in a launch campaign when it was read, so the promotional annual figures are marked as dated on the page.

## Held, with the owner named

**From the thirteen re-stamped listings.** `wlsdks/ontology-atlas` (**154** stars, a shared Markdown ontology of what a codebase builds and what a change could affect) is the strongest of them and is held on class: codebase comprehension is developer tooling, and the catalog keeps that slice behind the agent-skill entries. `heygen-com/hyperframes` (**83,326** stars, *write HTML, render video*) is the largest repository touched this hour and is **not an MCP server** - its README ships a CLI plus agent skills and names no MCP endpoint - so it belongs to the skills catalog, not this one, and it is recorded that way rather than stretched into the wrong page. `jgravelle/jcodemunch-mcp` (**2,843** stars, symbol-level code retrieval), `daghis/teamcity-mcp` (**32** stars, TeamCity builds and agents), `tencentcloudbase/cloudbase-ai-toolkit` (**1,165** stars, CloudBase backend for coding agents) and `1mcp-app/agent` (**530** stars, an MCP aggregator) are all developer infrastructure on classes this catalog covers elsewhere. `eiry16/beacon-mfg` (**2** stars, a bilingual directory of 210,000 Chinese businesses) is a company-data surface with a thin repository and no documentation trail yet. `lakshmanturlapati/fsb` (**204** stars, DOM-first browser automation; the repository now redirects to `fullselfbrowsing/FSB`) is on the browser-automation class already carried here. `www-regdatalab-com-mcp` has no resolvable repository under that name and is **recorded as unresolved rather than inferred**. `enkiduhub/mentionforge` (1 star, agent-native social listening priced at $0.02 USDC per call with ten free trials) is held on the social-listening class carried by `mentionbird` and the AI-visibility entries, and on its own evidence: a one-star repository is not a vendor yet. `mambalabsdev/mcp-reddit-search-thread-scraper` is the fifth wave of the one-tool-per-actor fleet now **44** across five waves, held under the standing Apify-actor ruling. `mediar-ai/screenpipe` and `n24q02m/notion` (**36** stars, markdown-first Notion for agents) both describe surfaces already catalogued here, and a re-stamp does not re-open a disposition.

**Carried forward.** Every hold from the midday pass stands: Nock, LaunchSpy, SealGuard, Aalto, Agent Demand Registry, Toolbox POD, FacturX, Deal.ai, OpenCheap, Switchyard, agents-room, Cred402, Scribase Mail, Sendblue, SovaTalk, the two What's On city servers, Neuro-CanvasLMS, Dagon Inference, fxapis MetaTrader 5, Safe Web Reader and volatiai. `alba-design`, `courio` and `quo` remain **unresolved** for the same measured reason as the midday pass: the mcp.so detail route answers "Only HTML requests are supported here" to a JSON-RPC probe and the reader proxy refused at **401** on bad IP reputation.

## Disposition of this pass

Two products, both OAuth tier, both measured to their gate and to the vendor's control surface, and neither driven with a live account - stated here and on both pages rather than implied. The value of the hour is the pair of mechanics: a **reviewable, expiring plan** in front of a settings write (Hank), and **deletion as a separate scope plus per-tool switches** (RushCRM). Both are shapes the rest of this catalog can be read against.
