---
title: "MCP Discovery Sweep - August 30, 2026 (Midday)"
description: "MCP ecosystem discovery sweep report: newly catalogued servers, evaluation notes, and skip classifications. Part of the Hermes resource directory."
last_updated: 2026-09-17
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-august30-2026-midday/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp", "ecosystem sweep"]
---

# MCP Discovery Sweep - August 30, 2026 (Midday)

- **Run:** Aug 30, 2026 ~18:00 UTC (11:00 MST), Spark (fresher clone; Mac Mini up but stale at Aug 29 night)
- **Shift label:** Midday (morning sweep of the same day already committed Relm + Sequel)
- **Issue window:** chatmcp/mcpso #3835-#3839 (cutoff: morning sweep high-water mark #3834)
- **Sources:** chatmcp/mcpso issues, mcp.so homepage (recentServers), mcpservers.org /all pages 1-3, mcpservers.org homepage
- **Catalogued:** 1 new server + guide -> **Laver MCP** (437 servers, +323 guides)
- **Commit:** pushed to main from Spark

## Catalogued

- **Laver MCP** (issue #3835) - official MCP server from laver.app, a kanban/sprints/team-wiki project management tool for small teams. 59 tools over boards, tickets, comments, subtasks, labels, custom fields, attachments, wiki pages, automations and published links. stdio via `npx -y @laver/mcp`, workspace-scoped API key (acts as the person who created it), versioned writes with 409 re-read-and-retry. MIT, npm @laver/mcp v0.5.0, official registry io.github.Developyn/laver-mcp. Free plan (3 billable people), Pro GBP 2.99/person/month. Repo 0 stars, created Aug 13, 2026. Guide at `hermes/mcp/servers/external/laver-mcp/`, relevance ★★.

## Also identified (not catalogued)

- Faxer #3836 - resubmission of the fax-ops utility already skip-classed in four prior sweeps (Aug 12-15 index prose) - utility class, no material change.
- 402Signal #3837 - fail-closed x402 endpoint router - x402 infrastructure class, 402oracle precedent.
- mcpx #3838 - MCP client (Unix CLI), not a server.
- kwnva.design portfolio #3839 - personal studio portfolio catalog - portfolio class.
- file2markdown (mcp.so homepage Aug 30) - document/web-page to Markdown conversion - dev utility class, BiGapi/Booklet precedent.
- mcpservers.org /all thin-docs slugs (no listing page, generic directory title): pfsense-mcp-server, etch-mcp, mdedit-agent-plugin, kitchensink4word, mcp-light-memory, wuwei-mcp, deskmcp, rhizome-mcp, nanoparse-mcp, enviadores-mcp, phi-guard-mcp, memesh-llm-memory, ghiblimcp.
- All other /all and homepage slugs were morning-sweep or prior-sweep dispositions (Genviral, Spike, Appbot, TuFirma, DrillerDB, Ransack, Forency, MagicPixel.art, etc.).

## Mechanics

- Cross-reference: single case-insensitive alternation grep over index.md plus guide-dir checks; confirmed Faxer and AgentCouch prior dispositions from index skip prose before declaring candidates new.
- Detail fetch: fetch-mcpservers-details.py returned generic titles for all 13 never-seen /all slugs (no listing pages) - thin-docs skip class per Aug 29 midday doctrine.
- Laver verification chain: npm v0.5.0 published + official registry listing + GitHub repo (MIT) + 45KB README enumerating all 59 tools with error semantics.
- Index patched with one atomic Python patcher (assert-before-write); guide validated with bundled validate-guides.py.
