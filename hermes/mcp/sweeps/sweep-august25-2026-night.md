---
title: "MCP Discovery Sweep - August 25, 2026 (Night)"
date: 2026-08-25
tags: [mcp-sweep, discovery, catalog]
description: "chatmcp/mcpso issues #3750-#3757 (Aug 25 18:03 - Aug 26 01:34 UTC), mcp.so homepage + feed, mcpservers.org /all pages 1-3 + homepage; 3 catalogued with guides (Transcodely, Rapidly, PopOff Data), 4 issue skips, 6 slug dispositions"
last_updated: "2026-10-24"
---

# MCP Discovery Sweep - August 25, 2026 (Night)

Run at ~02:00 UTC August 26 (19:00 MST August 25), following the August 25 evening sweep (cutoff: issue #3749, stamped 18:13 UTC).

## Sources scanned

- chatmcp/mcpso GitHub issues, open, 30 newest: #3727-#3757; fresh window #3750-#3757 (8 issues, all evaluated)
- mcp.so homepage `recentServers` (8 entries, 2026-08-23 through 2026-08-26)
- mcp.so /feed (30 slugs)
- mcpservers.org homepage (18 slugs) and /all pages 1-3 (90 slugs, broad href pattern)
- Cross-referenced 92 candidates against the catalog index (354 dirs, 825 names) and index skip prose

## Catalogued (3 guides)

1. **Transcodely MCP** (`transcodely-mcp/`) - issue #3753. Hosted agent-native video infrastructure: transcode gs://, s3://, https:// sources, adaptive-ladder hosting with CDN player link, AI WebVTT captions, EUR usage reads. 7 tools confirmed from vendor docs (create_video_from_url, create_job, generate_captions, get_video, get_job_status, list_jobs, get_usage). OAuth 2.1 PKCE or app-scoped key. Endpoint https://mcp.transcodely.com/mcp probed: 401 unauthenticated (liveness verified). Repo transcodely/mcp, MIT, 0 stars (created Aug 25). No delete/cancel/update tools.
2. **Rapidly MCP** (`rapidly-mcp/`) - issue #3756. Idea validation: Lean Canvas, riskiest-assumption hypothesis with researched pass mark, Pretotyping experiment design with build prompts. 21 tools confirmed from repo docs/tools.md. Bearer token (RAPIDLY_MCP_TOKEN, shown once) or OAuth for existing teams. Registry co.rapidly/rapidly. Endpoint https://www.rapidly.co/mcp probed: 401 bearer-required (liveness verified). Repo Exponentially-Platform/Rapidly-MCP, MIT, 1 star. Free trial: 5 ideas.
3. **PopOff Data MCP** (`popoff-data/`) - issue #3754. Reality-TV social analytics: Instagram/TikTok follower time series at ~30-minute resolution, follow/unfollow graphs, engagement, trend events, citation-ready season CSVs. 12 tools named in the submission (list_shows, get_show, list_episodes, get_cast, get_contestant, get_follower_history, get_follow_graph, get_follow_events, get_trend_events, get_engagement, export_season_csv, get_usage). API key (popoff_sk_) or OAuth; $79/mo flat with 5,000 calls, then $0.02/call; REST and MCP share one meter. Registry tv.popoff/data. Endpoint https://popoff.tv/mcp probed: 401 key-required (liveness verified). Hosted, no repo.

## Skipped (issue window)

- AgentSeed #3750 - AST-level code verification and anti-hallucination guardrails for coding agents - dev tool class
- Spoolis #3752 - outcome verification for result-shaped agent purchases - commerce infra, no business data carried
- SSSNACK #3755 - agent self-registration design network - agent community infra class
- 1Claw #3757 - HSM-backed agent secrets vault and signing - agent security infra class

## Slug dispositions (homepage and /all)

- BoardRepo (boardrepo-com-connect) - KiCad/Altium PCB search - niche hardware dev data
- PZERO (docs-pzero-studio-agents-mcp) - AI model marketplace aggregator - UnificAlly class
- Walletwatch (loki-freedomlab-space-mcp-docs) - Solana wallet lookup - crypto consumer class
- AstroFabric (www-astrofabric-ai-docs) - agentic OS for deploying growth/revenue agents - agent orchestration infra, ADA Turbo class
- WaveMaster (wavemaster-ai/mcp-server) - surf forecasting - niche consumer data
- Hird (no-materials/hird) - Hird language compiler introspection - dev tool class
- myrocket slug = xRocket Exchange MCP - already catalogued (Aug 25 morning sweep)

## Already evaluated in prior sweeps (no action)

CorpusLaw, Real Wave GHL, BulkTranscripts, Normi DVF (catalogued); Appraisily (skip). Famous-name mcpservers.org homepage slugs (atlassian, blender, calcom, chrome-devtools, firecrawl, github, playwright, supabase, railway, minimax, granola, proxyman) are re-indexes. All remaining feed and /all slugs resolved to prior-sweep skip prose (QuanticData, AgentRisk M2M, Batru, Hypnothera, Windframe, OAIA Arena, Context.dev, Routebase, SecondSim, Magichour, CLSTR, Agent Conductor, dockndevai family, and others).

## Verification

- 3/3 guide frontmatter valid (YAML, title 30-70, description >= 100, no em dashes, See Also dirs resolve)
- repo `scripts/validate_frontmatter.py` green (3,462 files scanned)
- 3/3 endpoints live-probed (401 auth responses prove liveness)
- git push verified: local HEAD == origin/main full hash
