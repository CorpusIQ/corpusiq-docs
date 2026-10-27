---
title: "Sweep Report - September 3, 2026 - CorpusIQ Docs"
description: "Evening MCP catalog sweep: chatmcp/mcpso issues #3910-#3917, mcp.so feed, and mcpservers.org /all, cataloging 7 new servers with guides (SellerMate, Neonjelly, Klarix Intelligence Engine, Raposa Aval, Strac DLP, ToBid and more); catalog now 514 servers / 400 guides."
date: 2026-09-03T19:00:00-07:00
sources: [chatmcp/mcpso, mcp.so, mcpservers.org]
status: complete
last_updated: "2026-10-24"
---

# September 3, 2026 - Evening Cron Sweep

**Shift:** Evening (~19:00 MST)
**Prior cutoff:** midday sweep (mcp.so feed 30 + mcpservers.org /all pages 1-3), catalog 507 servers / 393 guides
**Fresh window evaluated:** chatmcp/mcpso issues #3910-#3917, mcp.so feed (29 slugs), mcpservers.org /all page 1 (16 slugs)
**Surfaces:** GitHub issues, mcp.so feed, mcpservers.org /all page 1
**Result:** 7 new servers catalogued (7 guides), catalog now 514 servers / 400 guides

## Catalogued (7)

| Server | Slug | Source | Verification |
|---|---|---|---|
| SellerMate | sellermate-mcp | GitHub issue #3913 | Live 401 probe (Authorization token required) proves endpoint live; vendor README documents 50+ tools, OAuth 2.1 PKCE, policy guardrails + admin approvals + audit trail; 2,000+ brands, Amazon Ads Partner Awards finalist |
| Neonjelly | neonjelly-mcp | GitHub issue #3917 | Live keyless probe: server neonjelly v1.0.0, 59 tools enumerated (resolve_store, diligence_pack, compare_stacks, niche_research, trending_product_ideas, ...); 1.37M-store catalog; registry io.neonjelly/mcp |
| Klarix Intelligence Engine | klarix-intelligence-engine-mcp | mcp.so feed | Live keyless probe: server klarix-intelligence v0.1.0, all 15 tool names captured (find_matched_prospects, score_prospect_fit, get_competitor_battlecard, teardown_tech_stack, ...); repo SpeaksenseAI/klarix |
| Raposa Aval | raposa-aval-mcp | GitHub issue #3914 | README documents 3 tools + SHA-256 hash-chained audit log; stdio via uvx raposa-mcp; free sandbox 100 approvals/month; EU-hosted, DPA; MIT, registry group.raposa/raposa-mcp |
| Strac DLP | strac-mcp-dlp | mcp.so feed | README documents 5 tools (redact_text, detect_sensitive_data, detect_file, redact_file, detokenize); thin client over Strac DLP API; stdio + streamable-http; key from strac.io/mcp-integrations |
| ToBid | tobid-mcp | mcpservers.org /all | Live keyless probe: server tobid v1.29.1, all 8 tools enumerated (search_tenders, price_analysis, vendor_report, unit_report, hot_opportunities, ...); free no registration; published Sep 3, 2026 |
| AuType | autype-mcp | mcpservers.org /all | Mintlify docs mapped via llms.txt; overview documents endpoint mcp.autype.com/mcp, OAuth 2.1 PKCE + DCR, per-tool scopes, 40+ tools across documents/render/styles/blocks/records/files |

## Not catalogued (skip prose)

- **ReadyAgents (#3916):** local YAML/JSON agent workflow CLI + stdio MCP - dev utility class.
- **PromptBranch (#3915):** local-first prompt version control - dev utility.
- **recipebooq (#3912):** iOS 26 Liquid Glass React Native components - dev utility.
- **Scholium Live Needle (#3911):** URL string-probe tool (fetch a URL, check for an exact string) - dev utility.
- **RAVN (feed):** cross-chain crypto swap execution, 12 venues - consumer investing class.
- **pdfAssistant MCP Server (feed):** 40+ PDF operations incl. OCR/redaction/encryption - document class saturated this week (Extend midday, PDFGate, iFillPDF).
- **Digital Darts Shopify SEO (mcpservers.org /all):** thin MCP docs - vendor site carries Chrome extension pages only, no MCP endpoint published; SEO class saturated (Tracetify, Sorank, HiBot this week).
- **NanoTools (mcpservers.org /all):** 44 paid x402 pay-per-call tools - x402 infra class.
- **ComputeSage StackBench (#3910):** prior disposition (midday skip).
- **Feed repeats already disposed by prior sweeps:** AON, Hostinger, Backblaze B2, QoreNext x2, PostMCP, OSIR Domain, Trendos, send-email, flora, QuantumProxies, Voibe, dot.tools, Neither, Sirro, VenuNite, MarsX, ListingBott, SEObot AI, DevHunt, GospelChannel, Rovyn, MagicMaster, NC Wedding Guide, KItinerary, CapSolver, Sniff, MCPFinder, LoopSkill, Signadot. **Feed repeats already catalogued:** MarketCode, Koongo, ZenSched, Layers, Mantis.
- **mcpservers.org /all page 1:** remaining slugs were prior-disposed (sirro, venuNite, NC Wedding Guide, SEObot, Rovyn, MarsX, GospelChannel, DevHunt, MagicMaster, ListingBott, flora) or already catalogued (TaiLexi/twlawbot).

## Notes

- First evening sweep to run three live keyless probes in one shift (Neonjelly 59 tools, Klarix 15 tools, ToBid 8 tools) - all three endpoints answered anonymous initialize + tools/list, giving guides exact tool names instead of directory descriptions.
- ToBid's tools/list required the MCP-Session-Id header returned by initialize; the bare probe script failed on the second POST, a session-id-aware probe succeeded.
- AuType: Mintlify llms.txt one-GET doc-tree map worked as designed (per the Sep 2 night-sweep addendum) - the MCP overview page under /automation/integrations/mcp/ was found through it.
- All 7 guides passed the bundled validate-guides.py and the repo frontmatter gate.
