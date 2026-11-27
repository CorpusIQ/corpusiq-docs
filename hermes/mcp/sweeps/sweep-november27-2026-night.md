---
title: "MCP Server Discovery - November 27, 2026 (Night)"
description: "A directory flat to the key, four feed cards and twelve filings, and three guides: a field-service CRM, a skill-audit store and a cited Wikipedia source."
category: "MCP Ecosystem"
last_updated: "2026-11-27"
---

# MCP Server Discovery - November 27, 2026 (Night)

Fired on the **03:00 MST** tick, **six hours** after the evening capture stored its baseline at 21:01 MST, into a window with no directory movement at all and a productive queue. The thirteen numbered server maps returned **38,251** raw `<loc>` entries against **38,251**, the same per-map counts, the same **24,494** distinct slugs and the same **24,528** keyed union, and the set difference against the stored baseline is **0 additions and 0 removals**. What moved was the feed, **four cards**, and the submission queue, **twelve filings** from **#8214** to **#8225**.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, 17 maps named, 13 numbered server maps
raw <loc>, maps 1..13         38,251   identical to the 21:01 MST evening read
  servers/1  ..... 4,134      servers/8  ..... 2,774
  servers/2  ..... 2,503      servers/9  ..... 2,604
  servers/3  ..... 2,952      servers/10 ..... 2,536
  servers/4  ..... 3,162      servers/11 ..... 2,515
  servers/5  ..... 3,332      servers/12 ..... 2,398
  servers/6  ..... 2,894      servers/13 .....   528
  servers/7  ..... 5,919      sum ............ 38,251 exact
distinct keys per map        1,987 / 1,990 / 1,994 / 1,999 / 1,996 / 2,000 x7 / 528
server-map distinct slugs    24,494   unchanged
priority-servers.xml         251 raw / 34 keys   (unchanged)
remote-mcp-servers.xml        15 raw /  1 key
union of keyed slugs         24,528   identical to the evening read
set diff vs 20261126_2101      0 additions, 0 removals
lastmod pairs, server maps   38,251
  at or after 23:02:40Z            1 row, and it is the boundary stamp itself
  newest anywhere            2026-11-26T23:02:40Z   (the evening read's own stamp)
```

**A quiet directory is a measurement, not an assumption.** The stored baseline `mcpservers_canonical_20261126_2101.txt` holds **24,528** keys and this capture holds **24,528**, with the per-map raw counts identical on all thirteen maps and the per-map distinct counts identical too. One `lastmod` row sits at or after the cutoff and it **is** the cutoff: the newest stamp anywhere in the capture is `2026-11-26T23:02:40Z`, the same value the evening pass printed, so there is no arrival, no removal and no restamp to report.

That is the fourth shape this surface has produced in five passes: a **re-shard** on November 25 night, a **736-key restamp wave** on November 25 evening, **309 arrivals** on November 26 midday, **101 duplicate raw entries with zero slugs** on November 26 evening, and now **byte-stability**. The measure that held across all five is the **per-map distinct count**, never the raw total, which moved 37,599 to 37,806 to 37,695 to 38,150 to 38,251 while the key set did the real work.

## The feed turned over four cards

`mcp.so/feed` answered **200** at **158,924** bytes with **36** anchors, **36** distinct slugs and **30** paired stamps. Four cards sit above the evening pass's newest card:

| Card | Stamp (UTC) | What it is | Disposition |
|---|---|---|---|
| `coral` | 09:51 AM | Execution rails for agents, permissions and custom tools over enterprise systems | Held, agent permissioning class |
| `lightsprint` | 09:10 AM | Multiplayer task board and agent sandboxes, a Linear and Jira alternative | Held, project management class |
| `silicon-caf-skill-store` | 08:42 AM | A skill store with pre-install audit tiers and recall notices | **Catalogued** |
| `pixel-art-generator-mcp-sprite-fusion` | 08:26 AM | Pixel art and sprite animation from a prompt | Held, creative media class |

Two reader notes belong in the log, because both have bitten this sweep before. The anchors are now the **plural** `/servers/<slug>` form, so a reader keyed on the old `/server/` prefix returns zero cards against a live document. And the bottom of the page carries **seven** anchors with no stamp at all, a popular block rather than a feed card, so pairing every anchor to the next stamp in document order leaves those seven honestly unstamped instead of silently mis-dated.

## The queue carried twelve filings

`chatmcp/mcpso` issues **#8214 to #8225**, the newest filed at **09:44:43Z**, read with bodies in one authenticated call. Twelve filings in five hours, and the distribution is the usual one: OAuth remote endpoints with a registry name, one publishing pair, and three local packages.

| Issue | Product | Disposition |
|---|---|---|
| #8214 | **NeurLead AI CRM** and Neuro Home | **Catalogued** (the CRM), Neuro Home documented inside it |
| #8215 | Flyn URL Shortener | Already catalogued (`flyn-mcp`, added 2026-08-27, refreshed 2026-11-19) |
| #8216 | Auto Poster AI | Held, social scheduling class |
| #8217 | The SEO Agent | Held, saturated SEO class |
| #8218 | postkeep | Held, email class |
| #8219 | PeptideCompare.co | Held, health vertical |
| #8220 | Starport Satellite and Launch Data | Held, consumer and space data |
| #8221 | wa2agent | Held, WhatsApp class |
| #8222 | Keepfold | Held, agent memory class |
| #8223 | Antigravity Action Launchpad | Held, local MCP App and agent tooling |
| #8224 | Glideworth | Held, personal finance class |
| #8225 | **WikiVectors** | **Catalogued** |

## Three guides

- [NeurLead CRM MCP - Field-Service Ops Behind an OAuth Grant](/hermes/mcp/servers/external/neurlead-crm-mcp/) - the **first field-service CRM in this catalog**, filed with a second server from the same publisher and documented at the OAuth tier rather than assumed. `initialize` answers **401** with `Bearer realm="NeurLead"` pointing at a protected-resource document that answered **200** and enumerated **32 scopes**, which read as a capability map: `leads:read`, `leads:create`, `leads:write`, `chats:read`, `chats:write`, `calls:read`, `calls:create`, `notes:write`, `catalog:read`, `prices:write`, `estimates:draft`, `estimates:send`, `invoices:draft`, `invoices:send`, `invoices:mark_paid`, `invoices:void`, `money:read`, `schedule:read`, `visits:write`, `tasks:write`, `campaigns:write`, `webhooks:manage`, `companies:read`, `companies:write`, `team:read`, `team:write`, `status:write`, `files:write`, `setup:write`, `reports:read`, `offline_access`. **The granularity is the product:** drafting an estimate, sending it, marking it paid and voiding an invoice are four separate grants, so a workspace can let an assistant draft while a person keeps the money. The plan document at `/connect/plans` answers keylessly as JSON built for a model to quote, **$99**, **$199** and **$399** a month, **14-day** trial with a card required, and it carries instructions addressed to the assistant (*"Show the user these plans and let them choose one"*), a commercial pattern this log records rather than endorses. **Neuro Home** from the same filing, `us.neurohome/neuro-home`, is the consumer booking side: about **100** home jobs in **10** groups across **eight** US metros, 401 with `invalid_token` at its own endpoint.
- [Silicon Café Skill Store MCP - Audit Before You Install](/hermes/mcp/servers/external/silicon-cafe-skill-store-mcp/) - **keyless, six tools, ten calls driven**, `1vr-skill-store` **1.0.0** on protocol **2025-06-18**, holding **43,000+** agent skills by the tool's own count against **30,000+** in its mcp.so filing, both recorded. The honest finding is what a static tier **means**: `get_skill` on id **42077** returns tier `notice` with `permissions: 0`, `network: 0`, `credentials: 0`, `dependencies: 1`, and a `meta` block reading `source_chars: 0` and `reason: source_unavailable`, so that tier means the store could not read the source rather than that anything was found. The status feed is the part worth subscribing to: four entries, including skill **1876** `e2etest` **recalled for a new high-risk signal** at `2026-11-27T07:40:24Z` with its tier label unchanged at `notice`, and three `source_changed_recheck` flips on November 25. `top_skills` ranks **nano-banana** first at **417** heat and tier **risk**, and every one of the twenty rows carries `install_hits: 0`, so "most looked up" on an anonymous connection is most audited. Three defects: an integer `skill_id` only, taglines truncated mid-word on an English-facing store, and Chinese category labels throughout.
- [WikiVectors MCP - Cited Wikipedia Paragraphs for Grounding](/hermes/mcp/servers/external/wikivectors-mcp/) - **keyless discovery, keyed calls**, `wikivectors` **1.0.0** on protocol **2025-06-18**. `initialize` and a **5-tool** `tools/list` answer with no credential and the server ships an `instructions` block that states the grounding contract outright: quote the text, cite its url, text is CC BY-SA 4.0. Every `tools/call` answered **401** with `code: missing_api_key` and a request id, so the entry is documented rather than driven, and the pricing came from the vendor's own docs: **1,000** searches a month free with no card, then **$2 per 1,000** prepaid, **$1 per 1,000** above a million, with an `answer_question` costing **5** units, a page lookup **1** per title and a **watch free**. **The field that earns the guide is `permalink`, which carries an `oldid`**: a paragraph cited with `https://en.wikipedia.org/w/index.php?oldid=1382287719` stays checkable after the page moves on. `watch_page` posts a signed JSON callback on every edit, move or delete, and `changes_since` returns the range with diff links.

## Also identified this pass (not catalogued)

Every one of these was probed to the tier, not assumed:

- **Glideworth** (#8224): a retirement and FIRE planner, AGPL-3.0, **72 tools** on its own count (53 read-only, 19 write), OAuth or a workspace key, and a **propose-then-apply** design where `propose_change_set` returns a diff and applies nothing. `initialize` answers **401** with `Bearer realm="glideworth"` and a complete `resource_metadata` pointer. Held on the **personal finance class**, which a personal finance server already carries with retirement planning and tax estimation among its tools.
- **PeptideCompare.co** (#8219): the filing says no authentication, and the first `initialize` this pass answered **429** with `{"error": {"code": "challenge", "message": "This request requires a challenge to be completed."}}` before a retry answered **200** as `co.peptidecompare/peptide-prices` **1.0.0**. So the surface is keyless and drivable and the dataset is well built (CC BY 4.0, cheapest per 30 days first, each price in the clinic's own words with the page and the date beside it, FDA status quoted). Held on the **health vertical**: it prices consumer clinic purchases rather than business systems.
- **Auto Poster AI** (#8216): `initialize` answers **200** with a session id and `tools/list` returns **16 tools** read keylessly, from `autoposter_draft_post` through `autoposter_get_analytics`. `tools/call` answers **200 with `isError: true`** and a `mcp/www_authenticate` meta naming `https://agent.autoposter.ai/.well-known/oauth-protected-resource`, and the filing states tools need a paid plan. Held on the **social scheduling class**.
- **Coral** (`github.com/withcoral/coral`, 09:51Z card): execution rails and per-agent permissions over enterprise systems. The mcp.so page carries no parseable MCP config block and points at the repository. Held on the **agent permissioning class**, which AgentKeyGate, AgentTrust and agenticrail-gate already carry.
- **Lightsprint** (`app.lightsprint.ai/mcp`, 09:10Z card): a task board with agent sandboxes and live previews. `initialize` answers **401** `-32001` with `resource_metadata` at its own protected-resource document. Held on **project management**.
- **Sprite Fusion** (`www.spritefusion.com/mcp`, 08:26Z card): pixel art and sprite animation, OAuth, `{"error": "unauthorized", "error_description": "Connect your Sprite Fusion account to use this server."}`. Held on **creative media**.
- **Starport Satellite and Launch Data** (#8220): `initialize` answers **401** with `Bearer realm="mcpize"` and scopes `mcp:tools mcp:resources mcp:prompts`, hosting at `mcpize.run`, **50** free calls a month then **$5 per 1,000**. Held on **consumer and space data**.
- **wa2agent** (#8221): read-only WhatsApp over two tools, `list_chats` and `get_messages`, by a publisher who discloses that he built and runs it. Held on the **WhatsApp class**, carried by WhatsApp Business Tools MCP.
- **Keepfold** (#8222), **Antigravity Action Launchpad** (#8223), **The SEO Agent** (#8217) and **postkeep** (#8218) held on the **agent memory**, **local MCP App**, **saturated SEO** and **email** classes respectively.
- **Flyn URL Shortener** (#8215) is **already catalogued** as `flyn-mcp`, added 2026-08-27 from the mcpservers.org page and refreshed 2026-11-19. A repeat filing is not a new product.

## Listings, re-measured

- **mcp.so**: `/servers/corpusiq-docs` answers **200** at **856,208** bytes with **175** case-insensitive `corpusiq` occurrences, against **857,624** bytes and the same **175** at the evening read.
- **mcpservers.org**: `/servers/corpusiq-io` and `/servers/corpusiq/corpusiq-docs` both answer **403** with the Cloudflare interstitial rather than a 404. Detail routes are edge-blocked by policy, not delisted, and our own mirror carries a fresh stamp in this capture.
- **Official registry**: `io.corpusiq/multi-source-mcp` holds **four** records from **1.0.0** to **1.0.3**, the latest published **2026-10-24T04:07:42Z** with a `streamable-http` remote at `https://mcp2.corpusiq.io/mcp`.

## What the pass says about the surface

Three nights in a row the same directory has told a different story and the same lesson has held. A rise in raw entries meant no new slugs, a flat key set meant no arrivals, and a byte-stable capture had to be proved by set identity rather than by a total that happened to look unchanged. **The arrival signal is per-map distinct movement and card rotation, never the raw `<loc>` count**, and the queue is the surface that actually carries new products when the directories are asleep.

### Why did a flat directory still produce three guides?

Because the two directories and the submission queue move on different clocks. `mcpservers.org` re-indexes in waves and can sit byte-stable for hours, and `mcp.so` rotates thirty cards a page, but the queue is where vendors file by hand, and twelve filings arrived in this five-hour window. Two of the three products in this pass came through the queue and the third arrived as a feed card stamped seventy-eight minutes before the run, so a pass that only diffs sitemaps would have reported nothing to see.
