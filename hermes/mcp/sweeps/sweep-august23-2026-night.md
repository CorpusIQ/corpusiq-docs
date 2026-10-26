---
title: "MCP Discovery Sweep - August 23, 2026 (Night)"
date: 2026-08-23
tags: [mcp-sweep, discovery, catalog]
description: "chatmcp/mcpso issues #3712-#3718 (Aug 23 16:42-02:00 UTC), mcp.so feed, mcpservers.org /all pages 1-3 (~90 slugs), Octura live endpoint probe; 11 catalogued with guides, ~40 skipped"
last_updated: "2026-10-19"
---

# MCP Discovery Sweep - August 23, 2026 (Night)

- **Cutoff:** evening cron sweep evaluated chatmcp/mcpso issues through #3711 (Aug 23 16:42 UTC)
- **Fresh window:** chatmcp/mcpso issues #3712-#3718 (Aug 23 16:42-02:00 UTC), mcp.so feed, mcpservers.org /all pages 1-3
- **Result:** 11 catalogued with guides, ~40 skipped

## Catalogued (11 guides)

| Server | Stars | Category | Source |
|---|---|---|---|
| TEOS WARN Act Layoff Intelligence MCP (hosted US WARN Act intelligence: 5,964 normalized layoff and plant-closing notices covering 545,647 workers across CA, TX, NY, IL, NC, refreshed every 12 hours from primary state sources with provenance; API key, Streamable HTTP at mcp.tppflow.com/mcp, REST mirror at api.tppflow.com with OpenAPI spec) | n/a (hosted, no repo) | Compliance | mcp.so feed (10 min before sweep) + tppflow.com/llms.txt |
| Walmart Marketplace MCP (spec-driven Walmart 3P-seller operations: 234 operations across 28 bundled OpenAPI specs, list_endpoints/describe_endpoint/call_endpoint + feed upload and report download, automatic OAuth2 with per-seller credential caching, PyPI mcp-walmart-marketplace, MIT; README candid about verified vs spec-wired operations) | 0 | Commerce & E-Commerce | mcpservers.org /all + GitHub README |
| Ozon Seller MCP (151 tools over Ozon Seller + Performance APIs: prices, promotions, ads, orders, returns, reviews, finance; multi-shop with encrypted local keys and per-call shop_id, stdio/SSE, MIT; sibling wb-mcp-server for Wildberries) | 2 | Commerce & E-Commerce | mcpservers.org /all + GitHub README |
| Epovest MCP (hosted GEO/AEO measurement: versioned brand Canon, tracker score series, raw engine response archives, surface checklists, source Atlas, corroborations; OAuth 2.1 PKCE or Bearer at mcp.epovest.com/mcp, official registry com.epovest/ai-visibility) | 0 | SEO | mcpservers.org /all + GitHub README |
| Octura Site Tools MCP (LIVE-PROBED: 30 deterministic ERP calculators - Odoo implementation/migration/upgrade/TCO/ROI/EDI/sh-pricing/stack-savings, US 50-state + nexus sales tax, Canadian GST/HST/PST/QST + payroll source deductions, EU VAT + VIES, inventory maths, ERP selection; keyless stateless at octurasolutions.com/mcp, server com.octurasolutions/site-tools v1.0.0) | 0 | ERP | mcpservers.org /all + GitHub README + live probe |
| KD Scout MCP (zero-dependency keyword research arithmetic: difficulty 0-100, blended opportunity score, structured content briefs; pip kd-scout, stdio, deterministic mode needs no keys; scoring from Groundwork's editorial pipeline) | 0 | SEO | mcpservers.org /all + GitHub README |
| Real Wave GHL MCP (native GoHighLevel workflow building - trigger, texts, waits, branches authored in the GHL builder, no public GHL API exists for this; agent build/test/launch by chat; OAuth sign-in at mcp.realwave.com/mcp, paid plan required, token option for Manus) | n/a (hosted, no repo) | Marketing | mcpservers.org /all detail page |
| OffenderSearch MCP (all 58 US sex-offender registries in one call: scored matches with matchConfidence/matchBasis, per-registry sourceStatus, warnings and citations with lastCheckedAt; batch_search up to 1,000; free 25 searches, $0.15/call metered; FCRA caveat documented) | 0 | Compliance | mcpservers.org /all + GitHub README + vendor page |
| GreenCalculus MCP (audit-traced carbon accounting: lookup/search/resolve/explain_absence factors + activity, electricity, embodied EN 15978, PCAF financed, freight, spend EEIO, business travel; every value carries source cell and pinned data version; Bearer key at mcp.greencalculus.com, registry com.greencalculus/api, npx/Docker bridge) | 0 | Compliance | mcpservers.org /all + GitHub README |
| Normi DVF MCP (17.4M+ geocoded French property transactions, DVF government data 2014-present: search, market stats, comparables, price trends, neighborhood comparison, activity, heatmaps, address history; 8 tools, credit pricing from free 100/mo, remote mcp.normi.fr/mcp or npx @normi/mcp-dvf) | 0 | Real Estate | mcpservers.org /all + GitHub README |
| PassportCraft MCP (EU Digital Product Passports (ESPR) drafting for textiles, batteries and general goods: catalogue reading, passport drafting, document attachment, gap analysis, manual publish gate; OAuth 2.0 at passportcraft.com/api/mcp, free plan included) | n/a (hosted, no repo) | Compliance | mcpservers.org /all + vendor connector page |

## Skipped (~40)

- **GH issues #3712-#3718:** motion-menu (597 motion/WebGL page patterns - dev/design tool), AURORA Agent (decision-context compiler with omission certificates - agent dev infra, same class as deja-vu skip), TRAECNclaw (TraeCN desktop automation, local stdio - dev tool), MCP Marketplace (880+ MCP server search utility - dev/directory tool), BuyWhere (repeat resubmission, already catalogued), Atlas Verified (duplicate of #3711, catalogued evening), TANCO SkillHub (skills catalog, not an MCP server).
- **mcp.so feed:** SecondSim (2-tool UK eSIM checkout funnel - consumer telecom utility, Roamzy class), plus repeats already evaluated (Mangii, Hypnothera, Truth Bear, Context.dev, Agent Conductor, CodeSentinel, Dados B3, HTML/CSS to Image, AskRentAI, One, Signal Nodus, lucid.page, AdminLanding, Hermoso, QR Planet, Upfirst, RADAAR, Riddle, Xverum, Parse, Simplepages, SavePropTax, CSOAI, DPF, UnificAlly, BCMS, Webz.io - all catalogued or previously skipped).
- **mcpservers.org /all pages 1-3:** NotFair Plugin (marketing SKILLS library, not an MCP server - listing overclaims 117 hosted tools), CLSTR (free keyless agent news feed - news covered by Webz.io/Newsmind), Botsify (white-label chatbot platform), ClipMyApp (app marketing video creation - no published tool list), Famulor (omnichannel contact-center management), Meistron (German crafts business software - geo-niche), Unplain (document-to-PDF - doc utility), Socializioz (social publishing - thin docs), FrankKi (printed-letter API), Magichour (AI media aggregator - UnificAlly class), WickedAPI (market data - thin docs), 9-bot (WhatsApp automation), Nautilinks (French backlink marketplace - geo-niche), Den (Korean construction standards - geo-niche), Neotic, Calaf, macadress, plus dev-tool slugs: dockndevai 8-server infra burst (Azure/ClickHouse/Kafka/Kubernetes etc - single-author dev-infra pack), framework-mcp, reqlan, cortex-connector, doco, commitlore, vinvai, ytdlp-transcript, m00nreport, diffcontext, plurality-memory, swarm-tips, hireme, betadrop, cli_revit, contextstream, geolens, canonic, payagents (x402 wallet plumbing), lvtd skills (x402 skill market).

## Notes

- Octura endpoint live-probed with the skill's mcp-tools-probe.py: initialize returned com.octurasolutions/site-tools v1.0.0 and tools/list returned 30 tools (README advertises 24) - probe is ground truth, guide reflects the live 30.
- PassportCraft recovered via the ApexVol upgrade path: the mcpservers.org page was thin ("No documentation available") but the vendor connector page (passportcraft.com/connector) documented the full OAuth connection flow, so the candidate was upgraded from thin-docs skip to guide.
- NotFair Plugin's directory description ("hosted Google Ads MCP with 117 tools") does not match its repo (a SKILL.md workflow library) - excluded under the skills-catalog class, never assert listing claims over repo truth.
- Mac Mini unreachable (SSH timeout, known partial-sleep pattern); entire sweep run from the Spark clone (fresher at 327 servers / +213 guides before this sweep).
- Walmart Marketplace MCP README carries explicit verification honesty (5 operation families verified against production, rest spec-wired); captured in the guide rather than hidden.
- Catalog index updated: 327 to 338 servers (+213 to +224 guides).
