---
title: "MCP Server Discovery - September 11, 2026 (Midday Sweep)"
description: "Midday sweep over the mcp.so feed, mcpservers.org /all pages 1-2 via the r.jina.ai reader proxy and chatmcp/mcpso issues #4067-#4070. 3 new business-relevant servers catalogued with guides, all 3 endpoints live-verified over JSON-RPC."
category: mcp
tags: [mcp-servers, daily-scan, september-2026]
last_updated: 2026-09-11
---

# MCP Server Discovery - September 11, 2026 (Midday Sweep)

**Source:** mcp.so feed (30 server blocks, curl + regex), mcpservers.org /all pages 1-2 (r.jina.ai reader proxy, 60 slugs batch-classified), chatmcp/mcpso issues #4067-#4070 (the fresh window past the night sweep's cutoff at #4064)
**Method:** GitHub issues API, /all slug extraction via reader proxy, JSON-RPC initialize probes
**Date:** September 11, 2026 ~10:05 MST (17:05 UTC)

## Summary

| Metric | Count |
|---|---|
| New GitHub issues evaluated | 4 (#4067-#4070) |
| mcpservers.org /all slugs batch-classified | 60 (pages 1-2) |
| New servers catalogued | 3 |
| Integration guides written | 3 |
| Skipped (not catalogued) | 10 new names + shell class + all prior-sweep dispositions |

## New Business-Relevant Servers (3 guides)

| Server | Slug | Class | Verification |
|---|---|---|---|
| RedReplier MCP | redreplier-mcp | Social lead monitoring - 5-network mention watching with 0-100 lead scoring, per-mention reasoning and drafted replies | Live-verified: HTTP 401 "Authentication required" on anonymous initialize (OAuth or API key); vendor tool reference lists 6 tools |
| Draxlr MCP | draxlr-mcp | SQL BI for agents - schema inspection, read-only SQL, saved queries, dashboards, exports, row-level security | Live-verified: HTTP 401, JSON-RPC -32001 "Authentication required" on anonymous initialize; vendor MCP page documents 14 database engines |
| Coderbuds MCP | coderbuds-mcp | Engineering delivery intelligence - 22 tools over shipping standards, org map, review turnaround, deploy lag | Live-verified: HTTP 401 with browser-auth remediation message from the server; registry namespace com.coderbuds/insights |

## Findings

- **RedReplier MCP**: hosted at mcp.redreplier.com/mcp (Streamable HTTP). Tool reference from the vendor docs: list_keywords, add_keyword, search_threads, get_thread, get_relevance_score, list_subreddits. Mentions from Reddit, Facebook, Hacker News, X and Bluesky in one list, filterable by website, source, status and score; each mention carries score reasoning and a saved drafted reply; website and keyword management with cost previews; email alert digests. API tokens start with the redreplier_ prefix. Packaged Agent Skill published at github.com/redreplier/agent.
- **Draxlr MCP**: hosted at api.draxlr.com/mcp over OAuth. The assistant reads schema, writes SQL, runs it read-only (write statements refused); saved queries, dashboards and widget management, CSV and Excel exports. Row-level security runs every request with the signed-in member's exact access - two members can run the same query and get different rows. 14 engines: PostgreSQL, MySQL, MariaDB, PlanetScale, CockroachDB, YugabyteDB, SQL Server, Redshift, BigQuery, Supabase, ClickHouse, Databricks, Snowflake, Neon.
- **Coderbuds MCP**: hosted at coderbuds.com/mcp/insights, OAuth 2.1 with browser authorization (bearer fallback for headless). Named tools from the docs: assess-change-fit, get-team-context, record-change-fit-decision, report-ai-usage; 22 tools total grouped by delivery-loop stage; the "Work Our Way" prompt primes a session. Source code is never sent to Coderbuds; acting tools are narrow (deploy hooks only, admin-only posture, review requests to the team's Slack).

## Directory Status (core maintenance)

- **mcpservers.org:** LISTED - r.jina.ai proxy 200, "CorpusIQ MCP Server | Awesome MCP Servers"; direct curl 403 CF wall unchanged.
- **glama.ai:** LISTED - 200, "corpusiq by CorpusIQ | Glama" on the canonical /mcp/servers/@corpusiq/corpusiq-docs slug.
- **smithery.ai:** LISTED - registry ?q=corpusiq returns benoit-p/Cprusiq, displayName CorpusIQ, unlisted=false; no flap.
- **mcp.so:** NOT LISTED - SSR "No servers match" plus empty-state; quarantine holds, no resubmit.
- **PulseMCP:** LISTED - r.jina.ai proxy 200, "Official CorpusIQ MCP Server | PulseMCP".

## New Directory Discovery

Pass-1 15-query GitHub search (123 directory-style candidates screened): one NEW vetted candidate for the next-cycle pool - **toolprint/awesome-mcp-personas** (39★, persona-based MCP toolkits, third-party "Add MCP Server" issue flow alive at #14 and #12, corpusiq-issues=0). Rejects screened: sickn33/agentic-awesome-skills (skills-only entry format), travisvn/awesome-claude-skills (skills-only), agentic-community/mcp-gateway-registry (self-hosted gateway software, no submission surface), github/awesome-copilot (configs, not an MCP server directory), anthropics/claude-plugins-official (official, gated). No submissions fired this cycle - three submissions were already fired today by the morning submission cycle (account moderation queue day 30 persists).

## Skipped (also identified, not catalogued)

- **UmmahAPI** - Quran, hadith, tafsir and prayer data with citations; reference niche.
- **Midpoint Card Prices** - trading-card market prices and grading ROI; consumer collectibles class.
- **Tribeunal** - human and AI jury verdicts with 39 tools, signed webhooks and arbitration mode; decision novelty class.
- **Switchboard** - agent call network from Anywhere Intelligence; agent infrastructure, sign-in walled.
- **AANet** - private metered agent coordination service; agent infrastructure class.
- **MiniMax H3 Max** - AI video generator; media generation class (Imaginode/Deep Art precedent).
- **Course Profiler** - trail-running and ultramarathon analysis; sports niche.
- **kolourr, offensive360** - /all 404 shells; **sikcapri, aceatdev, sadri-dridi** and the numbered author slugs - nav-only shells.
- **Resell Pro #4068** - Vinted resale market analytics; HOLD (the vendor's own docs state the MCP publication documents are drafts and not ready for directory submission; re-check next cycle).
- **TERM #4069** - signed agent community and coordination platform; agent coordination class.
- **DeliverKit #4070** - packaging and signing knowledge for agents; dev utility class.
- **Prior-sweep dispositions respected** - Theyond, TruVerifAI, OpenZiti LLM-Gateway, OpenZiti MCP Gateway, Reach, Airside Labs, Nova Data Analytics, Canarics, Orthogonal, VenuNite, toll402, Loadster, priostack, pulse-verity, Prove AI, Ultimate Web Scraper, Artlist, Fluenta, VarynForge, Expired Domains, HasData family.

## Catalog State

- Catalog: 634 → 637 servers; 520 → 523 guides.
- 3 endpoints live-probed over JSON-RPC (all 401 auth-gated exactly as documented; no keyless tools/list captures this cycle).
