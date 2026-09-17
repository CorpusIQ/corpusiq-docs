---
title: "MCP Discovery Sweep - August 31, 2026 (Morning)"
description: "MCP ecosystem discovery sweep report: newly catalogued servers, evaluation notes, and skip classifications. Part of the Hermes resource directory."
last_updated: 2026-09-17
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-august31-2026-morning/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp", "ecosystem sweep"]
---

# MCP Discovery Sweep - August 31, 2026 (Morning)

- **Run:** Aug 31, 2026 ~10:00 UTC (~03:00 MST), Spark (fresher clone)
- **Shift label:** Morning (~03:00 MST wall-clock convention; first Aug 31 section, no collision)
- **Issue window:** chatmcp/mcpso #3845-#3847 (cutoff: night sweep high-water mark #3844)
- **Sources:** chatmcp/mcpso issues, mcp.so homepage (recentServers), mcp.so feed, mcpservers.org homepage
- **Catalogued:** 1 new server + guide (444 servers, +330 guides)
- **Commit:** pushed to main from Spark

## Catalogued

- **OpenHire MCP** (issue #3845) - agent-native job protocol over ~120 employers' first-party ATS APIs (Greenhouse, Lever, Ashby, Beisen): 16,000+ live AI/infra, autonomous-driving and embodied-AI postings across the US, Europe and China (incl. 11 CN robotics employers: Unitree, UBTECH, Galaxea, Dobot, Mech-Mind, Pudu, SIASUN). 5 tools (search_jobs, watch_intent, check_watches, get_company_info, authorize_application); every listing is schema.org/JobPosting plus verified_at, source, ghost_score, response_sla_days and apply_channel. Local-first privacy: matching runs client-side, résumés structurally cannot transit the server (authorize_application has no file parameter), ranking is a locked f(match_quality, freshness) function enforced by CI. stdio via uvx openhire or pipx install openhire (PyPI v0.2.0), MIT, registry io.github.gzchenhao/openhire v0.2.0. Repo 2 stars, created Jul 14, 2026. Guide at `hermes/mcp/servers/external/openhire-mcp/`, relevance ★★ (Worklittle/Vocaneo jobs-data precedent; category Business Operations).

## Also identified (not catalogued)

- ShadowGraph #3846 - local-first decision memory for AI agents (27 tools full, 12 compact; preserves decisions, rejected alternatives, evidence, outcomes, reconsideration conditions) - agent dev infrastructure class, AURORA decision-context precedent.
- local-gpu-imagegen #3847 - connect agents to local ComfyUI/WebUI/Diffusers GPU stacks (17 tools, stdio) - creator utility class, klo-mcp precedent.
- treg.to - pay-per-call gateway to 3,028 third-party APIs across 82 platforms, one token - API-gateway infrastructure class (moves money and routes calls; carries no first-party business data).
- Gamedai NFL MCP (omniviewai/gamedai-nfl-mcp) - read-only NFL scores, wire news, scout grades and fantasy start/sit calls - consumer sports class.
- FlashDesk MCP (flashdesk/flashdesk-mcp) - remote desktop control from Claude Code (screenshot, mouse, keyboard, SSH, file transfer) - dev automation class.
- Hispanic Legacy MCP (citarium/hispanic-legacy-mcp) - Spanish contributions to science, exploration and culture - niche educational class, Noodle precedent.
- Soulfield Lens MCP (mrhpython/lens-mcp) - independent ten-check review layer for AI-generated text - QA utility class.

mcp.so homepage recentServers and feed repeats were prior-sweep dispositions (File2Markdown, BiGapi, DrillerDB, MagicPixel, CrawlForge, Ransack, Genviral, AgendaForge, BidSkim, OmniSocials, SocialRobot, Hologrow, Forency, Tactiq, Gemina, Contextflo); the remaining mcpservers.org homepage slugs were famous-name re-indexes (atlassian, blender, browserbase, calcom, chrome-devtools, cloudflare, context7, deepwiki, exa, firecrawl, github, google/mcp, granola, minimax, next-devtools, notebooklm, playwright, proxyman, railway, supabase, xcodebuildmcp).

## Mechanics

- Cross-reference: bare-brand grep over index.md with variant generation plus full-line context reads to distinguish catalogued vs skip-prose vs false-positive hits; 30 candidates checked.
- Verification: GitHub API (repo stars/license/creation), PyPI JSON (version), raw README fetch (tool names, install and config shapes, privacy model).
- Validation: per-guide asserts (YAML frontmatter, title 30-70, description >= 100, em-dash scan, credential-redaction scan, See Also dir existence) plus the repo CI gate `scripts/validate_frontmatter.py` (3652 files, all valid).
- Index patched with one atomic Python patcher (assert-before-write: last-updated line, top sweep section, docs-links tail block).
- Shift label collision check: grep for "August 31" - none existed.
