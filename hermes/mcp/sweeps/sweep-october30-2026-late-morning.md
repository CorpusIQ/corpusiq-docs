---
title: "MCP Server Discovery - October 30, 2026 (Late Morning)"
description: "An hour after the midday pass: three entries from the newest pages, two candidates already catalogued, and one jurisdiction the catalogue lacked."
last_updated: 2026-10-30
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october30-2026-late-morning/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 30, 2026 (Late Morning Sweep)

This pass fired at `11:00 MST`, fifty-five minutes after the midday read. A short window is useful for a different reason than a long one: almost nothing has changed, so whatever did change moved onto the newest page in front of you rather than being buried in a long tail. The read covered the mcpservers.org `/all` page with the TanStack state decoded from the gzip body, the mcp.so `/servers` index and the homepage `recentServers` block, then cross-referenced every slug against all 1,446 files in the guide tree, the sweep reports and the previous ledger.

Three entries were catalogued. Two of the raw candidates turned out to be duplicates of guides shipped days ago, which is the useful finding of a short-gap pass.

## What Was Catalogued

[Tuqui MCP](/hermes/mcp/servers/external/tuqui-odoo-mcp/) sits at `https://tuqui.com/mcp` and answered a keyless `tools/list` with **HTTP 401** `{"error":"unauthorized"}`, the expected state for an OAuth connector bound to a vendor account. The card was filed on mcp.so on `2026-10-21`, carries repository `github.com/Tuqui-AI/tuqui-mcp` (**HTTP 200**) and docs at `docs.tuqui.com` (**HTTP 200**), licence LGPL-3.0. The claim is the absence of a build: nothing installed in Odoo, no module deployed, one URL added to the assistant. Two sentences do the security work, **read-only by default** and **only what your Odoo user can see**, and the second reuses Odoo's own record rules rather than inventing a parallel permission model. Versions 16 through 20 across Community, Enterprise, Odoo Online, Odoo.sh and self-hosted. The honest comparison is against the Odoo server already catalogued, and it is not setup-versus-no-setup because both claim little Odoo-side configuration; the split is that the local server takes `ODOO_DB` and `ODOO_PASSWORD` into your own config, while this one holds the session vendor-side behind a consent screen. **Gap recorded:** `tools/list` needs a token, so the tool names are the vendor's publication and not a list this pass drove.

[MarketPrint MCP](/hermes/mcp/servers/external/marketprint-print-on-demand/) sits at `https://mcp.marketprint.de/mcp` and answered **HTTP 401** with `Missing bearer token. Connect via OAuth, or use a static mcpacct_ token from your account settings.` That refusal is better than most: it names both credential paths, so an agent reading it knows what to try instead of reporting a bare failure. The card was filed `2026-10-14`, vendor MarketConsultive GmbH, `authType` oauth, no repository because the service is closed. Production is split by destination, **Germany for Europe and Houston, Texas for the USA**, which for print-on-demand is not a footnote but the difference between a shipping estimate that survives a customs form and one that does not. Four channels: Shopify, Etsy, WooCommerce and TikTok Shop. This is the catalogue's first print-on-demand entry and its first look at the supply side, where a physical object begins to exist rather than a fifth opinion on storefront health. **Gap recorded:** the publish path is capable but unverified, and a trial should settle draft-versus-live publishing, per-channel pricing and whether listings can be read back for reconciliation.

[Casus MCP](/hermes/mcp/servers/external/casus-mcp/) sits at `https://mcp.wearecasus.com/mcp`, answering **HTTP 401** to a keyless `tools/list` and **HTTP 405** to a bare `GET`, the normal pair for an OAuth-gated Streamable HTTP endpoint that speaks only POST. Flagged official on mcpservers.org and at position 2 of the newest page. The corpus is deliberately national rather than broad: **230,419 articles of 77 codes** from Légifrance with successive versions, BOFiP administrative doctrine, **more than 3.4 million court decisions** searchable by number or ECLI, tax treaties and EU law, as of 18 October 2026. The reason to care is the date axis. `get_code_article` reads an article in the version applicable to a **given date**, and `resolve_references` grades a citation as found, found with a difference, ambiguous, not found, not applicable at the date, or outside the corpus. Those statuses are not a boolean, and an agent that collapses them into "not found" throws away the signal a reviewer needs. Two self-descriptions earn the entry: a text **absent from the corpus is not a text that does not exist**, and the version history is **partial, reaching back mostly to 2025**, so earlier dates can return "undetermined at the date" rather than a guess. Scope is `legal:read`. **Gap recorded:** the tool names come from vendor documentation, not from a driven list.

## Two Duplicates That Looked New

The most useful result of a fifty-five minute window is catching what a longer sweep might have written twice.

`free-seo-audit-for-claude` on the mcp.so `/servers` index reads as an unregistered slug, and it is not. Its `repoUrl` resolves to `github.com/houtini-ai/seo-audit` and its package to `@houtini/seo-audit-console` on npm at **0.17.0**, which is the server the catalogue already carries as [SEO Audit Console MCP](/hermes/mcp/servers/external/seo-audit-console-mcp/), added `2026-10-28`. The local `known()` cross-reference missed it because the directory slug and the guide directory do not share a full normalised form; the repository and npm record are what settled it.

`best-ai-search-agency-aeo-report` resolves to a public remote endpoint at `https://aeoengine.ai/mcp`, which a keyless probe drove to **2 tools**, `run_aeo_report` and `get_aeo_report_status`, matching the surface already catalogued as [AEO Engine MCP](/hermes/mcp/servers/external/aeo-engine-mcp/) on the same day. Same endpoint, same two tools, different listing.

## What Was Read and Held

Two paid sponsorship cards arrived on the `/all` newest page carrying `utm_medium=paid_sponsorship` in their own links, which is worth recording because a sponsorship is not an arrival. `Fulcra Dynamics` (agent-to-agent shared context, memory) and `Springbrand.ai` (10,000+ tools to search, post and sell) both return **404** on their detail pages, so neither has a drivable surface and neither is claimed. `StockCake MCP` is the third sponsored card, free AI-generated images, held on the design and media generation class this catalogue carries heavily.

`GPT Image Hub` is image generation, the same class. `FFxF` was named and held in the midday pass an hour earlier and is unchanged. `FSB` (`full-self-browsinhg`, a typo in the published slug) is DOM-first browser automation, MIT, repository `github.com/fullselfbrowsing/FSB` (**HTTP 200**), but its card carries `createdAt` of `2025-02-23`, so it is a year-old project newly indexed rather than a new arrival, and it is held on the browser automation class. `Poker Bots All Stars` is live Texas Hold'em played by agents at a 3D table, consumer entertainment rather than an operator surface. `kin` and `cli-a2b26f` are generic slugs with no card content to evaluate and nothing is claimed about them.

Two more were already dispositioned and are recorded so the next pass cannot read them as fresh: `Anry` was named in the 28 October morning pass and `m1k3` in the 18 October night pass.

## Count

The mcpservers.org counter reads **18,402** with **27** unique entries recovered from the newest page, 5 of them carrying vendor descriptions through the TanStack state and 22 through the JSON-LD breadcrumb list. The JSON-LD block is a reliable fallback but it returned no names on this read while the TanStack block returned only 5 description-bearing blocks, so both extractions were needed and neither alone would have produced the list. The guide tree held **1,062** server entries before this pass and holds **1,065** after it, with 1,182 guide files in total when the legacy flat pages are counted beside the directories.
