---
title: "Sweep Report - September 3, 2026 - CorpusIQ Docs"
description: "Morning MCP catalog sweep: chatmcp/mcpso issues #3907-#3909 plus homepage feeds, cataloging 5 new servers with guides (Buska MCP, Asyntai, AnswerLoops, TaiLexi AI, Furrow Forms); catalog now 498 servers / 384 guides."
date: 2026-09-03T03:00:00-07:00
sources: [chatmcp/mcpso, mcp.so, mcpservers.org]
status: complete
last_updated: "2026-10-19"
---

# September 3, 2026 - Morning Cron Sweep

**Shift:** Morning (~03:00 MST, continuing after the Sep 2 night sweep)
**Prior cutoff:** chatmcp/mcpso issues #3892-#3906 (Sep 2 night sweep), catalog 493 servers / 379 guides
**Fresh window evaluated:** issues #3907-#3909
**Surfaces:** GitHub issues, mcp.so homepage recentServers, mcpservers.org homepage, mcpservers.org /all page 1
**Result:** 5 new servers catalogued (5 guides), catalog now 498 servers / 384 guides

## Catalogued (5)

| Server | Slug | Source | Verification |
|---|---|---|---|
| Buska MCP | buska-mcp | mcpservers.org /all (buska-io/buska-mcp) | Live 401 probe (Missing Bearer token), README tool docs (3 tools), MIT repo Buska-io/buska-mcp (0 stars, Sep 2), registry io.buska/buska |
| Asyntai | asyntai-mcp | GitHub issue #3907 | Live 401 probe (Missing bearer token), 40+ tool names recovered from vendor docs HTML, registry com.asyntai/support-agent, npm @asyntai/mcp, MIT |
| AnswerLoops | answerloops-mcp | mcpservers.org /all (answerloops/answerloops) | Hosted initialize 200 (tools/list empty anonymous), vendor MCP guide documents 5 tools, AGPL-3.0 repo (2 stars, Aug 19) |
| TaiLexi AI | tailexi-mcp | mcpservers.org /all (www-twlawbot-com-mcp) | Live 401 probe (invalid_token), vendor-published coverage (20M+ judgments, 1M+ indictments, 100K+ interpretations), endpoint mcp.twlawbot.com/mcp recovered from detail-page HTML |
| Furrow Forms | furrow-forms-mcp | mcp.so homepage New Arrivals (furrow-forms) | Endpoint api.furrowforms.com/mcp + 26 tool names from vendor docs, MIT repo useburrow/furrow-forms (1 star, Aug 26), registry com.furrowforms, npm @furrowforms/mcp |

## Not catalogued (skip prose)

- **Engram MCP (#3909) / Engram Alpha MCP (#3908):** agent memory infrastructure (ShadowGraph/AURORA class). Same vendor family as the previously noted "engram" index entry.
- **CapSolver (capsolver-ai/capsolver-mcp):** CAPTCHA-solving automation - fraud-adjacent automation plumbing.
- **Sniff (aboudjem/sniff):** QA bug-walker for web apps - dev utility.
- **MarsX (marsx-dev), Signadot (signadot/cli), MCPFinder (ux-xd/mcpfinder-mcp), LoopSkill (wisechef-ai/loopskill-api):** dev infrastructure and meta-directory utilities.
- **MagicMaster (magicmaster-pro-mcp):** audio mastering - creator utility.
- **KItinerary (mrwulf/kitinerary-mcp):** consumer travel extraction.
- **Rovyn (rovyn-app-docs):** podcast playlists - consumer media.
- **GospelChannel (gospelchannel-com), NC Wedding Guide (www-ncweddingguide-com):** consumer directories.
- **SEObot AI (seobotai-com):** thin docs - no MCP surface on the vendor site (integrations page and seo-ai-agent page carry zero MCP references, no endpoint found).
- **DevHunt (devhunt-org):** dev-tools launchpad, no endpoint or own repo on listing - thin docs.
- **ListingBott (listingbott-com):** directory submission service, no endpoint or own repo on listing - thin docs.
- **Flora (flora-mcp):** visual asset generation - creator utility.
- **Repeats already disposed by prior sweeps:** AON Agent Offer Network, Hostinger, Backblaze B2 (feed re-listings), QoreNext CRM and Trade Screening, PostMCP, OSIR Domain (catalogued), VenuNite, Sirro (mcpservers.org homepage).
- **mcpservers.org homepage:** all other slugs were famous-name re-indexes (atlassian, blender, calcom, chrome-devtools, context7, firecrawl, github, granola, minimax, playwright, proxyman, railway, supabase).

## Notes

- Issue window was thin (3 fresh issues); 2 of 5 catalogued servers came from /all catch-ups (Buska, AnswerLoops, TaiLexi) and 1 from the mcp.so homepage (Furrow Forms, a July-listing re-featured in New Arrivals - catch-up harvest per the age-rule-yields-to-business-data doctrine).
- TaiLexi endpoint recovery: the mcpservers.org detail page HTML carried https://mcp.twlawbot.com/mcp in its body; JSON-LD endpointUrl was empty.
- All 5 guides passed the bundled validate-guides.py and the repo frontmatter gate (3,824 files).
