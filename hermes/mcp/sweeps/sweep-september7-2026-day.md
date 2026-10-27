---
title: "MCP Server Discovery - September 7, 2026 (Day Sweep)"
description: "Day sweep over the mcp.so feed plus mcpservers.org /all page 1. Two new business-relevant servers catalogued with guides: PostNitro MCP (official carousel and social publishing connector, OAuth/API-key gated endpoint live-verified) and Yocoolab MCP (visual feedback to PR workflow, Apache 2.0 npm package)."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-10-24
---

# MCP Server Discovery - September 7, 2026 (Day Sweep)

**Source:** mcp.so feed (29 server blocks, TanStack $R refs), mcpservers.org /all page 1 (via r.jina.ai reader proxy), GitHub search API net (created after the night sweep cutoff)
**Method:** curl + feed $R-stream parsing, r.jina.ai proxy for mcpservers.org, unauthenticated GitHub search API, vendor doc + endpoint probing
**Date:** September 7, 2026 ~10:00-11:00 UTC

## Summary

| Metric | Count |
|---|---|
| Feed entries examined | 29 |
| mcpservers.org page-1 slugs | 15 (all previously disposed) |
| GitHub created since night cutoff | 455 total, 15 sampled (all zero-star spam) |
| New servers catalogued | 2 |
| Integration guides written | 2 |
| Skipped (not catalogued) | 0 |

## New Business-Relevant Servers

### PostNitro MCP - AI Carousels and Social Publishing for Agents

- **Endpoint:** https://mcp.postnitro.ai/mcp (Streamable HTTP)
- **Auth:** API key (starts with pn-, minted in dashboard profile > Embed); endpoint also advertises OAuth protected-resource metadata (scope postnitro, offline_access)
- **Live verification:** unauthenticated initialize returned HTTP 401 with `WWW-Authenticate: Bearer error="invalid_request", resource_metadata="https://mcp.postnitro.ai/.well-known/oauth-protected-resource"` - definitive auth-gated liveness signal
- **What it does:** 35 tools for carousel, single-image and short-video post creation across LinkedIn, Instagram, TikTok and Threads; AI image generation, template browsing, brand kit and social account management, and post scheduling, from inside any MCP client
- **Category:** Social Media Management
- **Guide:** `/hermes/mcp/servers/external/postnitro-mcp/`

### Yocoolab MCP - Visual Feedback to PR Workflow for Agents

- **Delivery:** local stdio via `npx -y @yocoolab/mcp-server@2 setup` (auto-configures Claude Code, Cursor, Cline, Roo Code, Windsurf); API base https://app.yocoolab.com
- **Auth:** JWT from the Yocoolab Chrome extension or app dashboard; GitHub PAT (or gh CLI auth) only for the PR tool
- **Repo:** github.com/Yocoolab/mcp-server - Apache 2.0, 1 star, created Apr 2026, pushed Sep 7, npm provenance + SBOMs + CI, 19 tools documented in the README
- **What it does:** 19 tools across threads (triage, context, replies, PR creation), selection/bridge (element context, page analysis), activity summaries, AI conversations, deployment previews and optional Pendo analytics
- **Category:** Productivity
- **Guide:** `/hermes/mcp/servers/external/yocoolab-mcp/`

## Notes

- mcpservers.org /all page 1: all 15 non-sponsor entries already evaluated in prior sweeps (top five were the Sep 6 midday candidates AdPlug/Encited/Bynn/Voibe/earn-*; WakeMark, ShopSynch, CareClinic, fetcher.sh family, Global Travel, UK Premises, Solana Snipe, AskPod all carry prior skip dispositions).
- GitHub net since the night sweep cutoff: 455 created, sampled top 15 - all zero-star hobby/spam repos (playwright clones, no-description MCP wrappers), none passing the business-operator filter.
- mcp.so feed carried exactly two blocks newer than the night sweep (PostNitro 16:29Z, Yocoolab 12:44Z); everything else was prior-sweep territory (TrueClicks and studiofromthesea were the night sweep's own dispositions).

## Actions Taken

- Guides written: `hermes/mcp/servers/external/postnitro-mcp/index.md`, `hermes/mcp/servers/external/yocoolab-mcp/index.md`
- Index updated: last-updated line (561 servers, +447 guides), top sweep section, tail block entry
- `.last-sweep` stamped
