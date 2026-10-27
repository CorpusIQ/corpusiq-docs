---
title: "MCP Server Discovery - September 2, 2026 (Morning Sweep)"
description: "Morning cron sweep over chatmcp/mcpso issues #3886-#3891 plus mcpservers.org /all JSON-LD and mcp.so homepage recentServers - 5 new business-relevant MCP servers catalogued with guides, 3 endpoints verified live."
category: mcp
tags: [mcp-servers, daily-scan, morning-sweep, september-2026]
last_updated: 2026-10-24
---

# MCP Server Discovery - September 2, 2026 (Morning Sweep)

**Source:** chatmcp/mcpso GitHub issues #3886-#3891, mcpservers.org /all JSON-LD newest-30, mcp.so homepage recentServers, mcpservers.org homepage slugs
**Method:** GitHub issues API + parse-homepages.py + extract-mcpservers-jsonld.py + live JSON-RPC probes (batch-probe.py, mcp-tools-probe.py) + npm/registry/repo checks
**Cutoff:** issues past #3885 (Sep 1 night sweep cutoff); run at 03:00 MST Sep 2 / 10:00 UTC Sep 2

## Summary

- Fresh issues evaluated: 3 (#3886, #3888, #3891)
- /all JSON-LD newest-30 cross-referenced: 18 slugs, 10 never-seen
- mcp.so recentServers: 8 entries, 3 never-seen
- Catalogued with guides: 5
- Skipped: 11 fresh plus all prior-sweep dispositions

## New Business-Relevant Servers Catalogued (5 guides)

| Server | Source | Verification | Category |
|--------|--------|--------------|----------|
| FoundRole | issue #3891 | endpoint www.foundrole.com/mcp 401-verified live (OAuth); npm @foundrole/ai-job-search-mcp v1.1.11 published; repo foundrole/jobs-mcp-proxy MIT | Business Operations |
| SEOmatic | mcpservers.org /all | endpoint app.seomatic.ai/api/mcp 401 INVALID_API_KEY live; repo Minh42/seomatic-mcp MIT created Sep 1 2026; 13 tools from README | SEO |
| Ashton & Forge Agency Directory | mcpservers.org /all | 3 tools live-probed keyless at ashtonforge.com/mcp/directory (server v1.0.0) | Business Operations |
| Mysocial | mcpservers.org /all | endpoints app.mysocial.io/mcp and /mcp/universe both 401-verified live; 50+ tool roster from vendor connector docs | Social Media Management |
| SparkLaunch | mcpservers.org /all | endpoint sparklaun.ch/api/mcp/ 401 invalid_token with login_url (OAuth); registry io.github.SparkLaunch-Dev/sparklaunch; repo SparkLaunch-Dev/SparkLaunch-Skills | Productivity |

## Verification Notes

- FoundRole: OAuth 2.1 PKCE, no API key, free account. Capabilities: live openings from company career pages (hourly refresh, 40+ industries), ghost-posting/pay/visa fact-checks, match scoring, deterministic ATS resume parser, Kanban tracker, reminders with calendar invites, H1B certified-wage data. Capability-level tool table (anonymous enumeration refused).
- SEOmatic: 13 consolidated tools named in README (gsc_performance, gsc_indexing, keyword_research, keyword_clusters, backlink_profile, serp_competitors, traffic_analytics, local_presence, site_pages, dataset_library, strategy_insights, task_manage, campaign_manage). Free tier = insight tools with monthly quota; acting tools paid + human-approval gate. OAuth 2.1 or API key (smk_live_...).
- Ashton & Forge: keyless, read-only, no account. directory_summary / search_agencies / get_matched all live-probed. Root /mcp path serves the marketing page (405 on POST); /mcp/directory is the endpoint. Anonymized listings by design.
- Mysocial: OAuth 2.1 PKCE + DCR. Full tool roster from the listing's connector docs: own-archive reads (search_posts, find_similar_posts, get_hit_dna, get_post_psychology, compare_post_candidates), Creator Universe research (search_universe, explore_topic), people/brands (search_brands, search_linkedin_people, find_contacts), lead pipeline, Brand Studio, additive writes with revision history. No tool deletes anything.
- SparkLaunch: OAuth-gated; confirmation-token write flow (destructive/public-state tools return a one-time confirmation preview after authorization preflight). Skills repo is the public interface; MCP server source is closed; proprietary license notice. Capability-level table.

## Skipped (not catalogued)

- Slidingbox Hydrate/Dehydrate (#3886) - one-shot encrypted secret handoff between agents, $0.02 per read over x402: agent secret plumbing class.
- Munnin (#3888) - agent identity and memory server (awaken/create_agent/19 tools): agent infra class (ShadowGraph/AURORA precedent).
- AON Agent Offer Network (mcp.so recentServers) - buyable offer links for MCP agents: agent commerce infra class (AmanChain precedent).
- Hostinger (mcp.so recentServers) - official hosting API MCP: cloud infra class (Backblaze B2 precedent).
- Memnest (/all) - local-first memory for coding agents: dev infra class.
- IMBA Wallet (/all) - agentic wallet with cards/eSIM for agent payments: x402 wallet class (Kura precedent).
- FactMem (/all) - local SQLite memory engine: agent memory class.
- Melaya (/all) - 6k-tool agent orchestration with Android control: dev infra class.
- Code Relay (/all) - branch-scoped runbooks and verification receipts for coding agents: dev tool class.
- QoreNext CRM and QoreNext Trade Screening (mcp.so recentServers) - already catalogued (qorenext-crm-mcp, qorenext-tradescreening-mcp).
- mcpservers.org homepage slugs and remaining /all entries: prior-sweep dispositions (Layers, Mantis, Novu, Backblaze B2, AmanChain, ComputeSage, FlightPowers, DFX, Pangolinfo, Katto, famous-name re-indexes).

## Trends

- Job-market and social-analytics surfaces both arrived this sweep (FoundRole, Mysocial), extending the Worklittle and Social Glass precedents with fact-checked posting data and own-archive social memory.
- The verification-first submission pattern continues (FoundRole shipped npm + registry + OAuth with filed-wage data); the confirmation-gated write architecture (SparkLaunch confirmation tokens, SEOmatic approval gates, Mysocial additive writes) is now the default across commercial agent servers.
- mcpservers.org /all JSON-LD remains a productive catch-up surface when cross-referenced against skip prose, not just dirs - 5 of 18 slugs were fresh dispositions this sweep.

## Actions Taken

- 5 integration guides written to hermes/mcp/servers/external/<slug>/index.md
- index.md updated: top sweep section, last-updated line, docs-links tail block (474 servers, +360 guides)
- validate-guides.py: 5/5 PASS; See Also dir + label checks run; scripts/validate_frontmatter.py green (3772 files)
- Committed and pushed to main with full-hash verification
