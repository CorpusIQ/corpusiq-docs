---
title: "Sweep Report - September 1, 2026 - CorpusIQ Docs"
description: "Morning MCP catalog sweep: chatmcp/mcpso issues #3864-#3872, cataloging new servers into the CorpusIQ MCP ecosystem directory."
date: 2026-09-01T03:00:00-07:00
sources: [chatmcp/mcpso, mcp.so]
status: complete
last_updated: "2026-10-19"
---

# Sweep Report - September 1, 2026 (Morning Cron Sweep)

- **Shift:** Morning (run ~03:00 MST, ~10:00 UTC)
- **Fresh window:** chatmcp/mcpso issues #3864-#3872 (all filed after the Aug 31 late-day sweep cutoff of #3863)
- **Secondary surface:** mcpservers.org /all page 1 (30 broad slugs, cross-ref) + mcp.so homepage recentServers + mcpservers.org homepage
- **Prior sweep cutoff:** issues through #3863 (late-day sweep commit 69603f9b6, catalogued Gemalli, DFX Real Estate, VulX Watch)
- **Outcome:** 4 new servers catalogued with guides; 1 live-verified with full tool capture

## Catalogued (4)

| Server | Source | Verification chain |
|--------|--------|--------------------|
| Gridar MCP | issue #3868 | Endpoint mcp.gridar.app/mcp initialize 401-verified live (JSON-RPC Unauthorized, OAuth flow URL in error body - liveness signal per the Jitsu class). Registry app.gridar/gridar v0.7.0 confirms repo TokDar2410621/blog-dashboard subfolder mcp-server (public, 0 stars, no license declared, created Feb 2026, pushed Sep 1 2026). 69 tools capability-level from the submission; anonymous enumeration refused by the OAuth 2.1 gate. |
| Hive Intelligence MCP | issue #3869 | Live probe mcp.hiveintelligence.xyz/mcp: initialize 200, all 8 root tools captured with descriptions (get_token_price, check_token_safety, get_wallet_portfolio, search_tools, get_api_endpoint_schema, invoke_api_endpoint, invoke_stateful_endpoint, validate_task_result). 607-tool catalog behind the search-then-invoke dispatcher. Registry xyz.hiveintelligence/mcp v1.1.4. Repo hive-intel/hive-sdk (MIT, 18 stars, created Aug 2025). Keyless 25 calls/IP/day. |
| Ranki MCP | /all page 1 (rankdelta-ai listing) | README from repo 1fancy/seo-aeo-audit-mcp-ranki (MIT, 0 stars, created Jun 2026) enumerates all 22 tools with schemas. npm @ranki.io/seo-aeo-mcp v0.1.0 and @ranki.io/mcp v0.1.0 both published (registry verified). Hosted endpoint mcp.ranki.io per README config; anonymous probe inconclusive (405 at root, 404 at /mcp route - the npm stdio packages are the verified consumable path, noted in the guide). |
| StackScope MCP | /all page 1 (stackscope-dev-docs-mcp listing) | Vendor /docs/mcp page documents endpoint mcp.stackscope.dev, OAuth sign-in flow, all 10 tools, credit pricing model and the operator (DATAFREAK LTD, UK company no. 17328826). Domain is Cloudflare-protected (browser UA passes). No public repo - stars n/a (hosted service). |

## Skipped (issues)

- **#3864 MCPg** - resubmission of the Aug 19 prose-catalogued PostgreSQL entry (index line "MCPg -- Production PostgreSQL MCP ★ New", repo devopam/MCPg). BuyWhere precedent.
- **#3865 Fastcrawl** - Firecrawl alternative cloud scraping API. Saturated web-scraping class per the rasterly precedent (#3676).
- **#3866 agent-identity-mcp** - throwaway email plus UK phone identity for agents. Identity/OTP plumbing class.
- **#3867 sms-florin-mcp** - rent a real UK number for SMS/OTP receipt. Same plumbing class, gray-area.
- **#3870 personal-understanding** - evidence-chain personal memory. ShadowGraph agent-memory class.
- **#3871 Deskwright** - computer use on GNOME/Wayland. FlashDesk desktop-automation class.
- **#3872 Atmita** - message your personal AI agent. AgentPub agent-to-agent messaging class.

## Skipped (/all page 1, never-seen slugs)

- **3d-agent-com** - Blender 3D modeling plugin. Creator utility class.
- **symvanta-com** - codebase call graph for coding agents. Dev tool class.
- **wan30ai-com** - video generator. Creator utility class.
- **mathismeadows/roamer-mcp-plugin** - spec-first dev workflow. Dev tool class.
- **imstocker/ims-creators** - game design collaboration. Niche creative class.
- **hanzou1234/ai** - Agent Economy Engine marketplace. Agent infra class.
- **dast-133-cn-mcpassets-agent-md** - Chinese airline flight data (dynamics, delay prediction, weather). Consumer travel class (FlightQueue precedent).
- **munhq/chat-recall** - cross-client session memory. Agent memory infra class.
- **sauna-guide** + **seedance x2** - consumer sauna quotes and video generation. Consumer/creator classes.
- **gridcarbon, theonchaindiary, cordfind, vaanzari, firefly-iii, getsigvest, consentstack, local-gpu-imagegen, docmake** - prior-sweep dispositions (evening/late-day reports).

## Catch-up candidates (recorded for future sweeps)

- **LinkUpAPI** (docs-linkupapi-com-api-reference-mcp-setup) - LinkedIn outreach actions: search people and companies, engagement intent signals, invitations and messages. Sales & Outreach class candidate.
- **GridNews** (gridnews/mcp) - market news, press releases and ticker sentiment. Financial news data candidate.
- **Perception** (perception-to-integrations-mcp) - real-time digital asset narrative intelligence, 31 tools. Paid analytics data candidate.
- **mlab.sh** (doc-mlab-sh-...) - threat intel: IOC enrichment, CVE and actor search, SBOM scanning. Security data candidate.
- **urdigitalau mcp-integrations family** (4 packages: Bing Webmaster Tools 12 tools, MS Clarity, Cloudflare, WordPress 46 tools; WordPress package homepage-listed as fresh) - personal integration collection; Bing Webmaster Tools is the SEO-data catch-up candidate.

## Notable dispositions

- **Sibling-race resolved by rebase, not conflict:** a late-day sweep (commit 69603f9b6) landed between my initial fetch and rebase, cataloguing the issues window #3858-#3863. The fresh-window cutover was derived from that commit's index section, so no duplicate guides were written.
- **mcpservers.org homepage hydration changed again:** the numeric latest-ids array (evening sweep found ids 12458-12464) is absent from this morning's shell; 18 homepage slugs were mostly famous-name re-indexes plus one fresh urdigitalau-wordpress slug.
- **mcp.so homepage was 100% prior-sweep dispositions** (Atomic Mail re-listing with future-dated createdAt artifact, CarChat, file2markdown, BiGapi, DrillerDB, MagicPixel.art, Forency, TikTok Transcript) - confirms the same-day doctrine that issues plus /all carry the yield.
- **MCPg resubmission check:** the #3864 issue resubmits the Aug 19 prose-catalogued entry (index line 2831, repo devopam/MCPg) which has no guide dir - BuyWhere precedent applied.
- **Fastcrawl vs rasterly precedent:** both are Firecrawl-alternative scraping APIs; rasterly (#3676) was skipped as saturated web-scraping category, Fastcrawl follows.
- **Gridar OAuth 401 mined for the flow URL:** the 401 error body carried the OAuth flow URL, consistent with the Forency 401-body-mining recipe.
- **Ranki probe inconclusive but consumable verified:** hosted endpoint route negotiation returned 405/404 on anonymous probes; the two published npm packages (server + hosted shim) are the verified consumable path, README config is the source of record.

## Commit

- Guides: gridar-mcp, hive-intelligence-mcp, ranki-mcp, stackscope-mcp
- Index: top section + tail block + last-updated line (460 servers, +346 guides)
- Validation: 4/4 guides clean (YAML, lengths, em-dash, credential-guard, See Also dirs + labels via index-label fallback for the corrupt-title targets); repo validate_frontmatter.py gate green
