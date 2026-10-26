---
title: "MCP Server Discovery - September 7, 2026 (Night Sweep)"
description: "Night sweep over the mcp.so feed plus mcpservers.org /all page 1. One new business-relevant server catalogued with a guide (TrueClicks MCP), one skip (studiofromthesea)."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-10-19
---

# MCP Server Discovery - September 7, 2026 (Night Sweep)

**Source:** mcp.so feed (30 entries, newest-first), mcpservers.org /all page 1 (via r.jina.ai reader proxy after direct curl hit a Cloudflare challenge), GitHub API evening net (created:2026-09-07, pushed:2026-09-06)
**Method:** curl + feed $R-stream parsing, r.jina.ai proxy for mcpservers.org, unauthenticated GitHub search API
**Date:** September 7, 2026 ~02:00-02:30 UTC

## Summary

| Metric | Count |
|---|---|
| Feed entries examined | 30 |
| mcpservers.org page-1 slugs | 30 (unchanged since midday sweep) |
| GitHub created Sep 7 | 11 (none business-relevant) |
| New servers catalogued | 1 |
| Integration guides written | 1 |
| Skipped (not catalogued) | 1 |

## New Business-Relevant Servers

### TrueClicks MCP - PPC Audit Intelligence for Agents

- **Endpoint:** https://data.trueclicks.com/mcp (Streamable HTTP)
- **Auth:** OAuth - browser sign-in with the user's own TrueClicks login, per-user account scoping
- **Live verification:** unauthenticated initialize returned HTTP 401 with `www-authenticate: Bearer resource_metadata="https://data.trueclicks.com/.well-known/oauth-protected-resource/mcp"` - definitive OAuth-gated liveness signal
- **What it does:** read-only access to the TrueClicks PPC audit platform (Google, Microsoft, Meta Ads). Portfolio audit results ranked by wasted spend/severity, TrueClicks score forensics, triggered alerts with campaign-level numbers, budget pacing and efficiency-target flags, open-task triage, and campaign/keyword/search-term/asset performance queries
- **Category:** Marketing
- **Guide:** `/hermes/mcp/servers/external/trueclicks-mcp/`

## Skipped (Not Catalogued)

| Server | Reason |
|---|---|
| studiofromthesea (sfts-mcp-server) | French micro-agency listing exposing 2 static tools about its own pricing offers and coverage zones. 0-star repo created Sep 6. Self-promotional thin-listing class. |

## Notes

- mcpservers.org /all page 1: top five non-sponsor entries identical to the midday sweep (AdPlug, Encited, Bynn, Voibe, earn-*), so no new listings there. Direct curl still Cloudflare-challenged; r.jina.ai reader proxy worked (Published Time Sep 6 18:01 GMT).
- GitHub evening net: created:2026-09-07 returned 11 zero-star repos, none passing the business-operator filter (dev tools, consumer niches, hobby projects). pushed:2026-09-06 top-15 were already-known mega-repos.
- mcp.so feed clock skew: the two new blocks carry timestamps ahead of wall clock (05:46Z vs 02:15Z observed) - treated as newest-first ordering regardless.

## Actions Taken

- Guide written: `hermes/mcp/servers/external/trueclicks-mcp/index.md`
- Index updated: last-updated line (559 servers, +445 guides), top sweep section, tail block entry
- `.last-sweep` stamped
