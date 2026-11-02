---
title: "MCP Server Discovery - November 2, 2026 (Midday Supplement)"
description: "Supplement to the midday pass: one new server catalogued, three new submissions and five directory cards re-probed with measurements."
last_updated: 2026-11-02
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november2-2026-midday-supplement"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 2, 2026 (Midday Supplement)

## Summary

One hour after the midday pass, fired on the 11:00 MST tick, so this is a supplement rather than a second read of the same surfaces. The midday pass had already shipped [Versum MCP](/hermes/mcp/servers/external/versum-mcp/) from the submission window and dispositioned the mcp.so cards and the mcpservers.org page, and none of that is re-argued here. What this pass adds is one guide, three submissions that landed after the earlier read, a correction to an existing guide, and measurements where the earlier pass had grouped names without probing them.

One arrival earned a guide. **AttriKit MCP** is the first entry in this catalogue that closes the loop from ad spend to app install to subscription revenue to a budget decision, and the decision is computed by the attribution engine rather than by the model: `get_campaign_decision` returns the engine's call verbatim and `record_campaign_decision` stores it with the inputs that produced it.

The correction is worth more than most new entries. The catalogued Builders in Fintech server now returns **23** tools from a live `tools/list` where the guide recorded **19**, and the guide is fixed in the same commit rather than left to drift.

## Sources Swept

| Source | Read | Result |
| --- | --- | --- |
| chatmcp/mcpso issue window | one authenticated call, bodies included | **#6585** to **#6623** read in full; the three at the top, `Publish MCP` **#6621**, `norc` **#6622** and `Lingard Vocab` **#6623**, landed after the midday read |
| mcp.so homepage `recentServers` | direct, `--compressed`, TanStack block | the same five cards above the night stamp of `2026-11-02T09:04:11Z`, from `paperjoy-01f7bf` at `14:39:24Z` down to `eddyter-ai-rich-text-editor-mcp` at `11:13:20Z` |
| mcpservers.org `/all` | r.jina.ai, read twice | **18,887** live on both reads, the counter the midday pass had already reached; `hologramxyz/avastudio-mcp` and `perisclaw-mcp` at the top |
| Endpoint probes | keyless JSON-RPC | **200** on `442ball` (**12** tools) and `builders-in-fintech` (**23** tools); **401** on avastudio, paperjoy, forge-by-ui8 and perisclaw |
| Listing surfaces | direct and reader proxy | four mcp.so slugs **404**; mcpservers.org live through the proxy; Glama live in the connectors index; official registry active; Smithery API erroring |

## New Servers Catalogued

### AttriKit MCP - App Attribution That Returns a Decision

Relevance: HIGH. **Package verified, tools documented** (`@attrkit/mcp` **2.0.1** on npm with bin `attrkit-mcp` and a repository field, the MIT repository `KamyarTaher/attrikit-mcp` whose README carries the full **39**-tool table, the MCP setup page publishing the same inventory and the same count, and the pricing page publishing the free allowance in its headline). There is no hosted endpoint and the package is stdio only, so no tool was called; the guide states that tier rather than implying a driven session.

The product is web-to-app attribution for iOS and Android apps that buy ads, and the MCP server is a thin client over the vendor's Management API with the tenant scope resolved from the management key, which can be workspace or app scoped and read only or read write.

The decision is the part that distinguishes it here. `get_campaign_decision` returns the attribution engine's call verbatim with the evidence behind it, `record_campaign_decision` writes the operator's scale, cut or hold confirmation back with the inputs used so it can be graded later, and the vendor states both that the model reports the call rather than recomputing it and that a suggestion is not a profit guarantee. Around that, `import_spend`, `pull_network_spend`, `set_cost_model` and `get_spend` make ad spend an input the agent can read, and RevenueCat joins purchases, renewals and refunds to installs.

It earns a guide because nothing in **1,085** guides answers the budget question. [Mobzio MCP](/hermes/mcp/servers/external/mobzio-mcp/) is link level marketplace attribution for one regional seller set and stops at the order; the ad surfaces stop at the creative, with Abyssale generating, AdTest scoring before spend, Ad Library Intelligence and Adspy reading competitors and AdMake joining research to generation and publishing.

Guide: [AttriKit MCP](/hermes/mcp/servers/external/attrkit-mcp/)

## Also Identified (Not Catalogued)

The five mcp.so cards above the night stamp were grouped by the midday pass without measurements. They were probed here and stand as measured holds. `442ball` answered a keyless `initialize` **200** as `442ball` **0.1.0** with **12** tools over one publication's club Power Ratings (`resolve`, `club_rating`, `compare_clubs`, `league_strength`, `rankings`, `rating_history`, `method`, `club_runs`, `league_runs`, `movers`, `league_index`, `greatest_sides`), held as consumer sports data. `forge-by-ui8` answered **401** with OAuth protected-resource metadata and `fragments:read` and `fragments:write` scopes, a design-asset retrieval surface held on the design asset class. `paperjoy-01f7bf` answered **401** `Unauthenticated.` on `https://paperjoy.co/mcp` behind **9** listed tools, Poland-only handwritten postcards held on the print-and-post class carried by MailStream. `eddyter-ai-rich-text-editor-mcp` is a local `npx` server that stages a React rich text editor into a codebase, held as developer library integration. `builders-in-fintech` is a relist of the catalogued entry, and its live `tools/list` returns **23** tools in **21,348** bytes where the guide recorded **19**, so the guide count, its FAQ and its last updated date are corrected in this commit.

On `/all`, `hologramxyz/avastudio-mcp` answered **401** requiring an `x-api-key` or a bearer token with protected-resource metadata, a growth surface over TikTok breakout detection, the account's own best ads, briefs carrying the source videos, video-model prompting and a monthly credit budget set at consent, with **76** tool annotations in its listing snapshot, held on the ad creative class because [AdMake AI MCP](/hermes/mcp/servers/external/admake-ai-mcp/) already joins research to generation and publishing and [Adspy MCP](/hermes/mcp/servers/external/adspy-mcp/) already covers organic posts later run as ads. `perisclaw-mcp` answered **401** `Missing Authorization header` on `https://api.perisclaw.com/mcp/plugin`, personal WhatsApp catch-up, search and reply behind read-only or read-write consent, held on the read-only messaging archive slice carried by Kaption WhatsApp and the WhatsApp Business class carried by `whatsapp-business-tools-mcp`.

The three submissions that landed after the midday read are held on the same classes as their neighbours. `Publish MCP` (`#6621`) publishes to the operator's own social accounts with a preview before every post behind OAuth 2.1, held against the six catalogued schedulers. `norc` (`#6622`) manages cron jobs, machines and run history behind a bearer key at `https://mcp.norc.app/mcp`, held on the cron and uptime class carried by [WatchCron MCP](/hermes/mcp/servers/external/watchcron-mcp/), `healthchecks-mcp`, `realuptime-mcp` and `hosttracker-mcp`, which monitor jobs rather than edit them, so the pair is worth a second look if an operator ever needs to change a schedule from chat. `Lingard Vocab` (`#6623`) is a language-learning app with anonymous discovery and OAuth 2.1 for tool calls, held beside the `Japanese Skills` precedent.

## Core Listing Verification

| Surface | Result |
| --- | --- |
| mcp.so four direct slugs | **404** on `/server/corpusiq`, `/server/corpusiq-io`, `/server/corpusiq-mcp` and `/server/io.corpusiq`, unchanged |
| mcpservers.org `/servers/corpusiq-io` | live, read through the r.jina.ai proxy; a direct fetch answers **403** to a plain client, which is the Cloudflare wall rather than a delisting |
| Glama | live in the connectors index at `/mcp/connectors/io.corpusiq/multi-source-mcp` |
| Official MCP registry | `io.corpusiq/multi-source-mcp` active, published **2026-05-25** |
| Smithery | the registry API answered an error this run, recorded as not readable rather than not listed |

## Verification

- AttriKit is documented from its own package, repository and pricing page, and the guide names what was not measured: the decision payload, the confidence field, the evidence labels and real spend import latency. No tool was called and the entry says so.
- The Builders in Fintech count is corrected from a live `initialize` and `tools/list` (**23** tools against **19** in the guide), with the FAQ and the last updated date changed in the same commit.
- The five directory cards and the two `/all` arrivals carry probe results rather than grouped assertions, and the four gated endpoints are recorded as **401** rather than as absent surfaces.
- Guide tree counted from disk: **1,085** server directories before this supplement, **1,086** after it.

## Sources

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [AttriKit MCP](/hermes/mcp/servers/external/attrkit-mcp/)
- [Builders in Fintech MCP](/hermes/mcp/servers/external/builders-in-fintech-mcp/)
- [Versum MCP - the midday pass that preceded this one](/hermes/mcp/servers/external/versum-mcp/)
