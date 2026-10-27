---
title: "Sweep Report - August 31, 2026 - CorpusIQ Docs"
description: "Afternoon MCP catalog sweep: chatmcp/mcpso issues #3848-#3857, cataloging new servers into the CorpusIQ MCP ecosystem directory."
date: 2026-08-31T11:00:00-07:00
sources: [chatmcp/mcpso, mcp.so]
status: complete
last_updated: "2026-10-24"
---

# Sweep Report - August 31, 2026 (Afternoon Cron Sweep)

- **Shift:** Afternoon (run ~11:00 MST, ~18:00 UTC)
- **Fresh window:** chatmcp/mcpso issues #3848-#3857 (all filed after the midday sweep stamp of 10:08 UTC)
- **Secondary surface:** mcpservers.org /all page 1 (30 slugs, broad-pattern cross-ref)
- **Prior sweep cutoff:** issues through #3847 (morning sweep), midday sweep dispositions respected
- **Outcome:** 4 new servers catalogued with guides; 2 live-verified over JSON-RPC

## Catalogued (4)

| Server | Source | Verification chain |
|--------|--------|--------------------|
| Edgrapi MCP | issue #3848 | Live probe api.edgrapi.com/mcp: initialize 200, all 9 tools captured. Repo paperandbeyond23-gif/edgrapi-mcp (MIT, 0 stars, created Aug 24). Server card at .well-known/mcp/server-card.json. Catalog surface open anonymously; data calls use the free key. |
| Small Business Intelligence by Brick & Mortar | issue #3856 | Live probe brickandmortar.dev/mcp: serverInfo small-business-intelligence v0.1.0, all 11 tools captured. Repo 2016judea/small-business-intelligence-mcp (MIT, 0 stars, created Aug 8). Keyless. Registry io.github.2016judea/small-business-intelligence. CC BY 4.0 datasets. |
| DocMake MCP | issue #3849 | stdio - no endpoint. npm @docmake/mcp v0.1.1 (published, created Aug 9). Repo docmake-io/mcp (MIT, 0 stars, created Aug 31). README tools table: 6 tools + resources + generate-document prompt. Registry io.docmake/mcp. |
| Atomic Mail MCP | /all page 1 catch-up | stdio - no endpoint. npm @atomicmail/mcp-github v0.3.26 (created Jun 10). Repo Atomic-Mail/atomic-mail-agentic (MIT, 255 stars, created May 7). Registry search: 21 version entries, v0.3.14 latest. Catch-up catalogue on the BusyMail/imap-mcp email-ops precedent. |

## Skipped (issues)

- **#3850 Truth Bear (GAUGE)** - resubmission of the already-catalogued truth-bear-gauge entry (guide dir exists since Aug 23). BuyWhere precedent.
- **#3851 JSONGuy** - JSON formatter/validator/repair. Dev utility class.
- **#3854 EditItAll MCP** - local-first in-browser editors (PDF/sheet/photo/vector/Word/slides) via headless Chrome. Creator/desktop utility class (klo-mcp precedent).
- **#3855 NEX Agent Co.** - A2A-speaking agent on Base with x402, Cloudflare-tunnel endpoint. Agent infra + x402 payment plumbing class.
- **#3857 Neuronto ARD Index** - agentic resource discovery index. Agent infra class.

## Skipped (/all page, never-seen slugs)

- **automatedvideoapp-com** - narrated/captioned video generation. Creator utility class.
- **campingroute-app-mcp** - 20,000 European campsites, hiking trails, wine festivals. Consumer travel class (FlightQueue precedent).
- **citarium/agentreliability-mcp** - agent testing/benchmarking harnesses. Dev infra class.
- **dockndevai/mcp-percona-pg** - Percona PostgreSQL + PgBouncer on Kubernetes. Dev infra class (vendor family: mcp-kafka).
- **elleryfamilia/terminal-mcp** - shared live terminal session view. Dev automation class.
- **getbirthchart-com** - birth charts and synastry. Consumer class.
- **lovable-dev-products-clever-stream-engine** - Fanus AI music maker. Consumer/creator class.
- **mrhpython/lens-mcp** - Soulfield Lens. Already disposed morning sweep (QA utility class).
- **rendermcp-com-llms-txt** - data/HTML to PNG/SVG images. Creator utility class.
- **rumors-app** - multilingual pick-up line corpus. Consumer entertainment class.
- **worakorn-prince/th-memory-mcp** - local SQLite agent memory. Agent infra class.
- **www-trvrse-com-docs-agents** - generative media studio (image/video/voiceover). Creator utility class.

## Notable dispositions

- **Atomic Mail catch-up precedent applied:** a never-seen /all listing from May 2026 (255 stars) cleared the business-data test on the email-ops precedent (BusyMail catalogued Aug 13, imap-mcp Aug 30 night). The age rule yields to the business-data test.
- **Same-day third sweep re-confirms the issues-first doctrine:** the entire 4-guide yield came from the issues window #3848-#3857 plus one /all catch-up; the /all page otherwise carried only prior-sweep dispositions and class-skips.

## Commit

- Guides: edgrapi-mcp, small-business-intelligence-mcp, docmake-mcp, atomic-mail-agentic
- Index: top section + tail block + last-updated line (451 servers, +337 guides)
- Validation: 4/4 guides clean (YAML, lengths, em-dash, credential-guard, See Also dirs + labels); repo validate_frontmatter.py gate green
