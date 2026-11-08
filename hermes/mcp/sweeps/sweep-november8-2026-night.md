---
title: "MCP Server Discovery - November 8, 2026 (Night)"
description: "A canonical that came back set-identical to 20,000 server URLs, one new mcp.so card, twelve queue arrivals, and one server catalogued because it is a check rather than a lookup."
last_updated: 2026-11-08
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november8-2026-night"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 8, 2026 (Night)

## Summary

This pass fired on the **03:00 MST** tick, six hours after the evening sweep that had catalogued four servers. Both named surfaces were quiet in the measurable sense: the mcpservers.org twelve-sitemap canonical returned **20,000** distinct server URLs, the same number as the 21:00 capture, and the diff is **zero additions and zero removals**; the mcp.so homepage carried **one** card above the evening stamp. The submission queue carried **twelve** arrivals between the evening window and this one.

**One server was catalogued**: [DutyKit MCP](/hermes/mcp/servers/external/dutykit-mcp/). It is the only arrival in twelve whose job is not already done by an entry in this catalog, and what makes it different is its shape rather than its data. The other eleven are all in classes already carried, and each is named below with the entry that owns the class.

The pass also produced a piece of arithmetic worth keeping: the canonical has now returned the same 20,000 URLs on two consecutive reads ten and six hours apart, from the same 63,359 raw `<loc>` entries across the same twelve server maps, with the locale prefixes stripped before the comparison. A flat day on this surface is now a measured statement rather than an impression.

## Sources Swept

| Surface | Read | Result |
| --- | --- | --- |
| mcpservers.org twelve-sitemap canonical | 12 server maps (`servers/1` to `servers/10`, `priority-servers`, `remote-mcp-servers`) fetched fresh with plain urllib and a browser user agent; **63,359** raw `<loc>` entries, inline locale prefixes stripped (`/pt-BR/`, `/zh-CN/` and the rest, case-insensitive), `/servers/` subset taken as the universe | **20,000** distinct server URLs against **20,000** at 21:00, **0 additions and 0 removals** |
| mcpservers.org `/all` and detail pages | direct fetch with a browser user agent | **403**, the standing condition since November 4, so no detail page and no `/all` listing was readable this pass either |
| mcp.so homepage | two direct reads with a browser user agent, gzip decoded, plain then cache-busted, the TanStack `recentServers` staging payload parsed on `slug`, `name` and `createdAt` | both reads identical: **172** `createdAt` stamps, **159** distinct, newest `2026-11-08T08:56:02.072Z`; **1** card strictly above the 21:00 stamp of `2026-11-08T06:00:20.000Z` |
| chatmcp/mcpso submission queue | authenticated `gh api`, titles and bodies | **12** arrivals, `#6923` to `#6935` with `#6932` absent, none a listing update |
| official MCP registry | `registry.modelcontextprotocol.io/v0/servers?search=` per candidate | two active records for **DutyKit** (`io.github.r08150816s-star/dutykit` **0.1.0** published `2026-11-07T16:05:01Z`, `io.github.renschrder-stack/dutykit` **0.1.1**), one repository each |
| candidate endpoints | keyless `initialize` then `tools/list`, and a `tools/call` where the catalog is open | **seven** endpoints probed: **four** keyless **200** with tool lists (`dutykit` 5, `offermagnet` 5, `quasslabs-api` 32, `powerplayers-public-read` 10), **three** answered **401** (`localprospects`, `1clickwebsite`, `agentxhq`) |

Two counting notes on the canonical. The sitemap index now carries `skills.xml` beside `static.xml` and the twelve server maps, so a raw union over every document in the index would over-report by the whole skills and marketing surface; only the twelve server maps were read, which is the same method as the previous passes, and the figure is directly comparable to them. And the locale strip has to be case-insensitive: an earlier attempt this pass used `[a-z]{2}` and read 37,483 URLs, because `/pt-BR/` and `/zh-CN/` survived the strip and tripled the count.

## Catalogued

- [DutyKit MCP - The Compliance Gate Before an Agent Acts](/hermes/mcp/servers/external/dutykit-mcp/) - keyless `initialize` **200** on `https://dutykit.dev/mcp` as `dutykit` **0.1.0** on protocol `2025-06-18`, no account and no key, with **five** tools listed and all five called live. Three are pre-checks on an action rather than lookups: `werbung_vorpruefen` (may this email or call go out, § 7 UWG), `rechnung_vorpruefen` (§ 14 Abs. 4 UStG mandatory fields), `vat_pruefen` (a live VIES check). The remaining two are `pflichten`, the obligation catalogue for Germany, Luxembourg and EU-wide duties with legal basis, source URL, check date and verification status on every line, and `ki_hinweis`, the AI Act Art. 50 Abs. 1 disclosure wording in de, fr, en and lb. The verdict is **three-valued**: `erlaubt: false` for a consumer email with no documented consent under § 7 Abs. 2 UWG, and `erlaubt: null` with "human approval required" for the business-customer exception under § 7 Abs. 3 UWG, so the ambiguous case is handed to a person instead of collapsing into a pass. Every answer carries a `nachweis` with a timestamp, the tool, a `verantwortlich` field and a **SHA-256** of the result, which is what makes a check re-verifiable later. Driven live in this pass: `vat_pruefen` on `LU26375245` returned `gueltig: true` with **AMAZON EUROPE CORE S.A R.L.** and its Luxembourg address as VIES holds them; `pflichten` for `DE` + `online_handel` returned the EU provider-information duty (Directive 2000/31/EC Art. 5), the German Impressum (§ 5 DDG) and the small-business rule with its **EUR 25,000** / **EUR 100,000** thresholds (§ 19 UStG, § 34a UStDV), each marked `pruefstand: belegt` and `geprueft: 2026-11-07`; `rechnung_vorpruefen` on a thin invoice returned `bestanden: false` with eight named missing fields and its own boundary stated, that the EN 16931 format check is not done here. Free public beta at **200** tool calls a day per IP, no account, and the vendor states the free tier stores no inputs and no results; MIT code and a CC BY 4.0 obligation catalogue; repository **0** stars, created `2026-11-08T09:23:40Z`, pushed `09:24:36Z`, size **0 KB**, recorded as a limit rather than smoothed over. Output is German apart from `ki_hinweis`. Not a duplicate of [EU VAT VIES](/hermes/mcp/servers/external/honest-vies-mcp/), [Rechnungslotse](/hermes/mcp/servers/external/rechnungslotse-mcp/) or [EU AI Act Explorer](/hermes/mcp/servers/external/eu-ai-act-explorer-mcp/): those are references the agent may consult, this one is called instead of acting and returns a verdict with a hash.

## Held, with the class owner named

**From the twelve queue arrivals.**

- **OfferMagnet Jobs** (`io.offermagnet/jobs`, #6930) on the jobs class owned by [FoundRole](/hermes/mcp/servers/external/foundrole-mcp/), which already runs live career-page openings with ghost-posting, real-pay and **visa-sponsorship** fact-checks on every posting. Driven keyless to **200** as `offermagnet` **1.0.0** with five tools (`search_jobs`, `get_job`, `check_visa_sponsorship`, `job_market_stats`, `apply_with_offermagnet`); the visa reading is the strongest leg and it is already carried, so the entry holds on the class rather than on quality.
- **LocalProspects** (`ai.localprospects/mcp`, #6924) on the local-business lead class carried by [Google Maps Scraper](/hermes/mcp/servers/external/google-maps-scraper-mcp/) and the lead-gen shelf (Leadgen, Goodleads, Heylead, Cold Leads, DeepLead). Owner names, business emails and phone-carrier enrichment over live Maps data. `initialize` answered **401**, so this tier would have been documentation only.
- **1ClickWebsite** (`ai.1clickwebsite/mcp`, #6923) on the WordPress and site-builder class carried by [WordPress.com](/hermes/mcp/servers/external/wordpress-com-mcp/) and Elementor. **401** on a keyless `initialize`; the agency lead-gen demo batches are a workflow on a covered surface.
- **QuassLabs API** (#6927) as agent and delivery tooling: **32** deterministic scorers, linters and calculators (ticket and PR linting, sprint health, SaaS metrics, model and cost advice, MCP tool-definition linting, OpenAPI diff, BLM land lookup, Mermaid QA). Keyless `initialize` **200** as `quasslabs-api` **0.3.0** with the full catalogue listed, and `tools/call` refused with "Missing API key", so the tier is a catalogue read. A utility bag rather than a business data surface.
- **Power Players** (`io.github.Playpowerpolitics/powerplayers`, #6928) as a civic vertical: keyless **200** as `powerplayers-public-read` **1.0.0** with **ten** tools over US federal and state officials, crowdsourced citizen ratings with sample counts and dates, voter-registration hand-offs, embeds and press kits. Well built and outside the operator surface this catalog tracks.
- **Billigast** (`io.github.idoo/billigast-mcp`, #6929) on the regional consumer class already set by the same author's Blocket MCP, held in the evening pass: a read-only Swedish price comparison across Prisjakt and PriceRunner merged per product, no key, in three distributions.
- **EasyTranscriber** (#6934) on the transcript class carried by [Patchwell](/hermes/mcp/servers/external/patchwell-mcp/) and the YouTube reading entries.
- **Vectorial Data Terminal** (`com.vectorialdata/terminal`, #6926) on the saturated trading class: Hyperliquid, Polymarket and yield data behind OAuth 2.1 with dynamic client registration or a `vd_agt_` agent key.
- **AgentX** (`com.agentxhq/agentx`, #6925) as coding-agent fleet infrastructure: a console over Claude Code, Codex CLI and Grok CLI running on the operator's own machines. `initialize` answered **401** with an empty body after advertising OAuth discovery.
- **MCP Security Scanner** (#6931) as agent infrastructure: an open-source scanner for MCP servers with a badge API and a leaderboard over an audit of 42,163 servers.
- **whoelse** (#6933) as research and developer tooling: GitHub prior-art clustering with a merge plan and collaborator discovery across OpenAlex, arXiv and Hugging Face. Keyless and stdio, no business data behind it.

**From the mcp.so card.**

- **PendingDelete.net** (`pendingdelete-net-pending-delete-free-mcp-server`, published `2026-11-08T08:56:02.072Z`) on the domain class carried by [Expired Domains](/hermes/mcp/servers/external/expired-domains-mcp/): pending-delete and dropped-domain search with drop times and linking-domain filters. The only card above the evening stamp, and it is a good product in a class this catalog already carries.

## Core listing check, measured

The fresh canonical still carries `/servers/corpusiq-io` and `/servers/corpusiq/corpusiq-docs`. The mcpservers.org `/all` surface answers **403**, the standing edge policy rather than a delisting. On mcp.so the namespaced slug `/servers/corpusiq/multi-source-mcp` now answers **307** to `https://mcp.so/server/multi-source-mcp/corpusiq`, which answers **404**, and the four direct slugs (`corpusiq-io`, `corpusiq`, `multi-source-mcp`, `corpusiq-multi-source-mcp`) all answer **404**, so that listing remains absent and the redirect is a routing change rather than a change of state. Glama answers **200** on `/mcp/connectors/io.corpusiq/multi-source-mcp`.

## Counts

The guide tree held **1,119** directories before this pass and holds **1,120** after it, **1,262** entries counting single-file guides before and **1,263** after, and **1,527** Markdown files under `hermes/mcp/` before against **1,529** after (the guide and this page). One server catalogued, one guide written, no resubmissions and no corrections to prior entries. Seven endpoints probed: four keyless 200 with tool lists, three bare 401 refusals.
