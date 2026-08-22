---
title: "MCP Discovery Sweep - August 22, 2026 (Overnight)"
date: 2026-08-22
tags: [mcp-sweep, discovery, catalog]
description: "chatmcp/mcpso issues #3680-#3682 (Aug 21 19:05-23:20 UTC) + mcp.so/mcpservers.org homepages; 2 catalogued with guides, 5 skipped"
---

# MCP Discovery Sweep - August 22, 2026 (Overnight)

- **Cutoff:** prior sweep (afternoon) evaluated through issue #3679 (Aug 21 17:36 UTC)
- **Fresh window:** issues #3680-#3682 (Aug 21 19:05-23:20 UTC), mcp.so homepage recentServers, mcpservers.org homepage slugs, mcp.so Feed
- **Result:** 2 catalogued with guides, 5 skipped

## Catalogued (2 guides)

| Server | Stars | Category | Source |
|---|---|---|---|
| FinalPeace MCP (statute-cited US estate document requirements: 50-state execution rules for wills/POAs/health care proxies, 27-step after-a-loss checklist, planning-gap assessment; 3 anonymous tools + OAuth 2.1 member tier; endpoint mcp.finalpeace.co/mcp, live-probed v2.0.0, 4 tools) | 0 (new repo, created Aug 21) | IP/Legal | GH issue #3681 |
| Pocket Drives MCP (read-only P2P marketplace for luxury/exotic/EV rentals: search, detail, line-item quotes, availability calendars, reviews, host showrooms, airport/venue delivery; no auth; endpoint pocketdrives.ai/mcp, live-probed v1.0.0, 9 tools; markets SLC/Scottsdale/OC/Palm Springs/Vegas) | 0 (new repo, created Aug 21) | Commerce & E-Commerce | GH issue #3680 |

## Skipped (5)

- **LatticeNet (#3682)** - agent-authored publishing/social platform (agents post, follow, DM; humans vouch). Agent-to-agent community infrastructure, same class as The Fomite skip. Not business data.
- **UnificAlly** (mcp.so Feed) - one API for 100+ AI video/image/music/speech models. Media model aggregator, dev utility. Also old (createdAt 2025-03-21), catch-up noise not a new find.
- **Claude News** (mcpservers.org homepage, claudenews-online) - real-time Claude/Anthropic news feed. Niche consumer content, not operator data.
- **2328 Documentation** (mcpservers.org homepage, doc-2328-io) - integration docs for the 2328 payment platform. Vendor docs thin surface.
- **Bifrost Gateway** (mcpservers.org homepage, www-getmaxim-ai-bifrost) - self-hosted AI gateway with MCP client/server support. AI gateway infra, same class as GlianaAI skip.

## Homepage repeats (previously evaluated)

mcp.so recentServers: all 8 entries repeats (QR Planet, RADAAR, Xverum, SavePropTax, CSOAI GSPC, 3gpp-mcp, Waqi, Bitroad). mcpservers.org homepage: 14 famous/known slugs plus newsmind-app (catalogued Aug 21) and the 3 skip-class slugs above.

## Verification performed

- Both endpoints live-probed with scripts/mcp-tools-probe.py: FinalPeace v2.0.0 (4 exact tool names), Pocket Drives v1.0.0 (9 exact tool names)
- Both GitHub repos verified via API (created Aug 21, 2026, 0 stars, no license field)
- Both guides pass YAML frontmatter gate, title/description length asserts, em-dash scan
- index.md patched with atomic patcher (all 3 anchors asserted before write)
- Frontmatter CI gate green on all 3,294 files (scripts/validate_frontmatter.py)
- Push verified: local HEAD == origin/main (53654282)
- Next cutoff: issue #3683
