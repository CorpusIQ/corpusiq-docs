---
title: "MCP Discovery Sweep - August 23, 2026 (Overnight)"
date: 2026-08-23
tags: [mcp-sweep, discovery, catalog]
description: "chatmcp/mcpso issues #3699-#3700 (Aug 22 19:56-22:34 UTC), mcpservers.org homepage slugs, mcp.so homepage recentServers; 1 catalogued with guide (BulkTranscripts), 6 skipped"
last_updated: "2026-10-19"
---

# MCP Discovery Sweep - August 23, 2026 (Overnight)

- **Cutoff:** docs maintenance sweep evaluated chatmcp/mcpso issues through #3698 (Aug 22 18:02 UTC)
- **Fresh window:** chatmcp/mcpso issues #3699-#3700 (Aug 22 19:56-22:34 UTC), mcpservers.org homepage slugs, mcp.so homepage recentServers
- **Result:** 1 catalogued with guide, 6 skipped

## Catalogued (1 guide)

| Server | Stars | Category | Source |
|---|---|---|---|
| BulkTranscripts MCP (hosted remote YouTube research: get_transcript, get_transcripts batch of 20, search_youtube, search_channel, get_channel_videos, get_playlist_videos, get_latest_videos; keyless start with 50 free transcript extractions per IP, one-time credit packs, cached transcripts free; endpoint bulktranscripts.co/mcp, live-probed v1.0.0, 7 tools) | n/a (new listing) | Content & Research | mcpservers.org homepage |

## Skipped (6)

- **Markovo (#3699)** - customer-side file and public-URL to Markdown converter (stdio CLI). Dev utility class, same as Booklet.
- **deja-vu (#3700)** - local BM25 memory over the session histories of 20 coding agents. Agent dev infra.
- **Agents Get Paid Kit** - x402 MCP path so agents help humans clear USDC, with spend caps and AUP. Payment plumbing, same class as 402oracle.
- **Public Signal Data** - Polymarket odds, whale trades and Workday ATS jobs behind mcp.apify.com actors with the user's own Apify token. Thin vendor surface, no first-party endpoint.
- **Appraisily** - appraisal prep, sample reports, a start link, and up to six past auction results per search. Lead-gen funnel with a thin data teaser.
- **Fresh Jots** - notebook for scripts and agents with webhooks and dead-man alerts. Agent infra class, same as prior notebook/logging skips.

## Notes

- BulkTranscripts endpoint probed live: initialize returned serverInfo bulktranscripts v1.0.0, protocol 2025-03-26, and anonymous tools/list returned all 7 tools. The marketing page lists six tools; the probe is the ground truth (search_channel is the seventh).
- get_transcript covers YouTube and TikTok; archive and search tools are YouTube-only.
- mcp.so homepage recentServers carried 8 entries, all previously evaluated (Agent Conductor and CodeSentinel were skip-recorded in the Aug 21 afternoon skip prose).
- Catalog index updated: 320 to 321 servers (+206 to +207 guides).
