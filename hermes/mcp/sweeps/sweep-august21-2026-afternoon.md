---
title: "MCP Discovery Sweep - August 21, 2026 (Afternoon)"
date: 2026-08-21
tags: [mcp-sweep, discovery, catalog]
description: "mcp.so Feed + mcpservers.org /all TanStack state + chatmcp/mcpso issues #3673-#3679 (Aug 21 11:08-17:36 UTC); 11 catalogued with guides, 7 skipped"
---

# MCP Discovery Sweep - August 21, 2026 (Afternoon)

- **Cutoff:** prior sweep (morning) evaluated through issue #3672 (Aug 21 09:47 UTC)
- **Fresh window:** mcp.so Feed newest 30, mcpservers.org /all TanStack state, issues #3673–#3679 (Aug 21 11:08–17:36 UTC)
- **Result:** 11 catalogued with guides, 7 skipped

## Catalogued (11 guides)

| Server | Stars | Category | Source |
|---|---|---|---|
| AskRentAI MCP (hosted read-only Rent Manager portfolio intelligence: NOI, rent roll, delinquency, vacancy, leases, work orders, vendor spend, financial reports; OAuth, $10/user/mo, 7-day trial; endpoint api.askrentai.com/mcp) | n/a (new listing) | Real Estate & Property Management | mcp.so Feed |
| Signal Nodus SEC Filings MCP (27 tools of primary-source SEC intelligence: YoY filing diffs, 8-K events, activist stakes, insider trades, 13F, IPO pipeline, EDGAR search since 2001, XBRL + claim verification; per-call x402 on Base or prepaid key; free lookup_company; mcp.signalnodus.ai) | n/a (new listing) | Finance | mcp.so Feed |
| One MCP (4-tool discovery+execute model over Gmail, Slack, Stripe, Shopify, HubSpot, Notion, Linear, Salesforce, QuickBooks; OAuth scoped grants; mcp.withone.ai/mcp) | n/a (new listing) | Integration & Automation | mcp.so Feed |
| Riddle Quiz Maker MCP (official Riddle.com: 62 tools for quizzes, polls, surveys, personality tests, forms, predictors, minigames, leaderboards; OAuth; riddle.com/creator/api/v3/mcp) | n/a (new listing) | Marketing | mcp.so Feed |
| Maeve Social MCP (social planning/scheduling/publishing with scope gates — read open, draft permissioned, publish needs by-name confirmation; api.maevesocial.com/mcp, verified HTTP 401 auth gate) | n/a (new listing) | Social Media Management | mcpservers.org /all |
| lucid.page MCP (7 tools: anonymous Markdown publish with claim-token flow, updates with revisions, bundles; lucid.page/mcp) | n/a (new listing) | Content & Publishing | mcp.so Feed |
| LinkedIn Ghostwriter MCP (ContentIn: write_post_in_my_voice from VoiceDNA, schedule/publish via official API, honest analytics; 8 tools; mcp.contentin.io/mcp-server) | n/a (new listing) | Content & Marketing | mcp.so Feed |
| ClaraConverts MCP (website conversion agent provisioning: 9 tools — pricing, trial tenant, embed, site-knowledge refresh, Cal.com, upgrades; claraconverts.com/mcp) | n/a (new listing) | Marketing & Conversion | GH issue #3675 |
| TomTicket MCP (helpdesk over stdio: tickets, operator replies with work time, statuses, customers, orgs, chats, KB; npx -y mcp-tomticket) | n/a (new listing) | Customer Support | GH issue #3679 |
| BestAppify MCP (Shopify App Store intelligence: 40 tools for keyword rankings, competitors, review intelligence, revenue/churn; bestappify.app/api/mcp, free 100 req/day) | n/a (new listing) | E-commerce | mcpservers.org /all |
| Mobbin MCP (official: natural-language search over 600K+ product screens, flows, sections with inline images + citation links; 3 tools; api.mobbin.com/mcp) | n/a (new listing) | Design & Product Research | mcp.so Feed |

## Verification performed

- All 11 cross-referenced against catalog index.md and the last three sweep reports: zero prior mentions
- Maeve Social endpoint live-probed: api.maevesocial.com/mcp returns HTTP 401 (expected auth gate); mcp.maevesocial.com 302s; well-known/mcp.json serves the SPA shell — guide documents the verified gate pattern
- One MCP tool list verified live from the mcp.so listing (4 exact tool names + scopes from tool descriptions)
- lucid.page tool list verified (7 exact tool names from listing)
- LinkedIn Ghostwriter verified (write_post_in_my_voice needs_input contract, analytics honesty note, X-MCP-Key header)
- Riddle: template-family tools verified from listing; 62-tool surface documented
- TomTicket: tool names from issue body; registry pending npm
- ClaraConverts: 9 exact tool names from issue body; registry com.claraconverts/clara
- Frontmatter gate (scripts/validate_frontmatter.py) green on all 3,286 files

## Skipped (evaluated, consistent with prior decisions)

- #3673 TaskMarket (x402 worker-market infrastructure — consistent with Vibes-Coded/402oracle skips)
- #3676 rasterly (Firecrawl alternative — saturated web-scraping category, consistent with cute-web-scraper skip)
- #3677 Magpie Capital (Solana lending — crypto, consistent with CoinLobster skip)
- Skycloak (128-tool Keycloak IAM management — dev/IT infra, not business-operator tooling)
- Parse.bot (browser-automation API builder — saturated category)
- AdminLanding (France/Switzerland rental-compliance — geo-niche, consistent with Saymon RU and eCourts India skips)
- Roboterradar RadarScore (humanoid-robot ratings dataset — research niche)
- mcpservers.org /all slugs reviewed and skipped: HostDeFi, ToolYour, DeepSearch, Melt, Registly, Signal Sprint, MaxCrawl (dev/niche tools)
- Feed repeats already catalogued or previously skipped: Hermoso, RADAAR, Upfirst, Webz.io, Simplepages, DPF, Xverum, SavePropTax, Waqi, Bitroad, QR Planet, 3gpp-mcp, CSOAI GSPC, FineData.ai, Sonar ASO, Raccha AI, My AskAI

## Catalog state

- Before: 298 servers, 184 guides
- After: 309 servers, 195 guides
- Next sweep cutoff: issue #3679
- Note: Mac Mini offline (SSH timeout) — sweep run entirely from the fresher local clone per fresher-clone doctrine
