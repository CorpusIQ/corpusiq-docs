---
title: "MCP Discovery Sweep - August 21, 2026 (Morning)"
date: 2026-08-21
tags: [mcp-sweep, discovery, catalog]
description: "chatmcp/mcpso GitHub issues filed Aug 21 07:22-09:47 UTC plus both directory homepages; 3 catalogued with guides, 1 skipped"
---

# MCP Discovery Sweep - August 21, 2026 (Morning)

- **Cutoff:** prior sweep (overnight) evaluated through issue #3668 (Aug 21 00:48 UTC)
- **Fresh window:** issues #3669-#3672 (Aug 21 07:22-09:47 UTC), mcp.so + mcpservers.org homepages
- **Result:** 3 catalogued with guides, 1 skipped

## Catalogued (3 guides)

| Server | Stars | Category | Source |
|---|---|---|---|
| your-mail-mcp (self-hosted, read-only IMAP email: one-way mbsync mirror + notmuch index, 10 read-only tools: search, ids, files, count, show, thread, text, folders, refresh, attachment; OAuth 2.0 with DCR, Docker or static Go binaries, no write path to any account) | 0 | Communication & Email | GH issue #3669 |
| Newsmind MCP (hosted RSS for AI clients: 29 tools for read/brief, full-text + semantic search, story clustering, keyword watches with email digests, OPML import/export; OAuth 2.1 + Bearer PAT; 14-day trial then $24/year; endpoint live at newsmind.app/mcp) | n/a (submitted repo 404s) | Content & Research | GH issue #3670 |
| den MCP (Korean AEC standards: KDS/KCS/KS/building statutes with clause citations, abstention flags, scope labels, site_context, review_plan, as_of historical queries; Bearer token, free beta; endpoint live at mcp.den.archi/mcp) | 0 | Compliance | GH issue #3671 |

## Verification performed

- your-mail-mcp: repo wildsurfer/your-mail-mcp verified (created Aug 20 2026); README parsed for exact 10 tool names, mbsync pull-only config, deployment modes
- Newsmind: endpoint live-probed (HTTP 401, expected OAuth gate); official MCP registry confirms app.newsmind/mcp v0.13.0; submitted repo rdowty/newsmind 404s, so guide published with stars n/a and no repo line per doctrine
- den: endpoint live-probed (HTTP 401, expected Bearer gate); official MCP registry confirms archi.den/den_archi_mcp v1.1.0; server.json + README parsed for 10 exact tool names
- All candidates cross-referenced against catalog index.md: zero prior mentions
- Homepages: all 8 mcp.so recentServers and all 15 mcpservers.org homepage slugs are repeats already evaluated in the overnight report
- See Also slugs verified against real directories; em-dash scan clean; CI frontmatter gate (scripts/validate_frontmatter.py) green on all 3260 files

## Skipped (evaluated, consistent with prior decisions)

- #3672 Kura - local Ethereum wallet for AI agents (macOS app, x402 payments). Pure x402 payment plumbing, same class as Vibes-Coded and 402oracle: skipped.

## Catalog state

- Before: 295 servers, 181 guides
- After: 298 servers, 184 guides
- Next sweep cutoff: issue #3672
