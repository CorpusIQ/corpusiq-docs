---
title: "MCP Cron Sweep — July 23, 2026"
description: "Automated cron sweep of mcp.so and mcpservers.org. 43 new servers identified, 1 business-operator guide created."
category: mcp-sweep
tags: [mcp-sweep, cron, discovery]
last_updated: 2026-07-23
---

# MCP Cron Sweep — July 23, 2026

**Sources:** mcp.so (22,680+), mcpservers.org (10,139+)
**Previous sweep:** [July 22, 2026 (evening)](/hermes/mcp/sweeps/sweep-july22-2026-evening/)
**Existing catalog:** 206 external server guides

## Methodology

1. **mcpservers.org/all** — extracted JSON-LD `itemListElement` with 30 newest servers
2. **mcp.so/feed** — extracted 30 h3 blocks with names and descriptions
3. **mcp.so server detail pages** — JSON-LD extraction for descriptions and categories
4. **Cross-reference** — deduped against 206 existing server slugs
5. **Business relevance filter** — only operator-relevant servers get full guides

## Headline Finds

| Server | Category | Why It Matters | Guide |
|--------|----------|----------------|-------|
| **Fullstory MCP Plugin** | Analytics / CX | Official MCP from Fullstory — behavioral analytics, session data, funnel metrics for AI agents. Beta program. Complements Subtext. | [Guide →](/hermes/mcp/servers/external/fullstory-mcp/) |

## Full Discovery List

### mcp.so/feed (30 servers)
discoverGPT, Lamina, DeepMark, Goalie Trademark Search MCP, Caulo, CryptoWhaleInsights, Tempreon, nuzur, twocents, Coinrule, iGaming Tools, patent-literature-search-mcp, Reelier, TaskerArmy Agent, Capital.com MCP, dokumendiregister, FT Optix MCP, Subtext, Libgen MCP, AgentCouch, InvestSights Indian Stock Research MCP, Moxie Docs, Fullstory, MailStream, ArtistAlly Conferences MCP, Support Inbox Agent, kiwoom-mcp-server, Vee3, Nippy

### mcpservers.org/newest (30 servers)
TaskerArmy Agent, Reelier, Taplio, iGaming Tools, Outside Agent, Fixou, Argus Testing, KoreanAds, BBW Belles Formalwear Evidence, Confluence to Markdown MCP Server, FeatureBoard, Routara LLM Gateway, AI Consensus, BountyVerdict Agent Decision Tools, KPI Depot, AIQUAA Playwright MCP Server, Retasc, Index One, BuiltWith, Actvt, Grok Chat MCP, 1ClickReport, Agent Browser MCP, Santiment, Snipara, Peil-mcp, Fable MCP, Claude Chat MCP, FreshBooks MCP, Google Image MCP

### Already in Catalog (deduped)
Capital.com MCP (capital-com-mcp), Goalie Trademark Search MCP, FreshBooks MCP, KPI Depot (kpidepot-mcp), FeatureBoard, Confluence to Markdown (confluence2md-mcp), 1ClickReport, BuiltWith, InvestSights, Agent Browser MCP (browser-mcp-agent360)

### Integration Guides Created

1. **Fullstory MCP Plugin** (`fullstory-mcp/index.md`) — 5,046 bytes. Official Fullstory behavioral analytics MCP. Covers session query, funnel analysis, CX insights, setup for Claude Code/Cursor, CorpusIQ integration strategy.

## Key Observations

- **Fullstory has two MCP products:** Subtext (agent-native session replay, already cataloged) and the main Fullstory MCP Plugin (behavioral analytics platform). Complementary but distinct.
- **GitHub API search broken:** Returned 0 results (spammy flag) — relied on mcp.so/feed and individual repo lookups instead.
- **Web search unavailable:** Firecrawl API key not configured on this host — all discovery via direct curl to MCP directories.
- **Taplio** identified as a potentially high-value LinkedIn MCP tool but no detail page found on mcp.so or mcpservers.org. Worth investigating in future sweeps.

## CorpusIQ Angle

Fullstory + CorpusIQ = revenue-to-behavior connection. Operators can cross-reference:
- **CorpusIQ:** Revenue data (Shopify, Stripe), ad spend (Google Ads, Meta), email performance (Klaviyo)
- **Fullstory MCP:** Session replays, rage clicks, funnel drop-offs, user journeys
- **Combined:** Identify which UX friction points directly impact revenue

## See Also

- [Previous sweep: July 22 evening](/hermes/mcp/sweeps/sweep-july22-2026-evening/)
- [Previous sweep: July 22](/hermes/mcp/sweeps/sweep-july22-2026/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
