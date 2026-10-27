---
title: "Sweep Report - September 4, 2026 - CorpusIQ Docs"
description: "Night MCP catalog sweep: mcp.so feed plus mcpservers.org /all pages 1-3, cataloging 8 new servers with guides (Ryze Google Ads, BoldDesk, Viral Manager, Accordio, Watchgoose, Drag, Modem, OpenShorts); catalog now 522 servers / 408 guides."
date: 2026-09-04T03:14:00-07:00
sources: [mcp.so, mcpservers.org]
status: complete
last_updated: "2026-10-24"
---

# September 4, 2026 - Night Cron Sweep

**Shift:** Night (~03:00 MST)
**Prior cutoff:** Sep 3 evening sweep (mcp.so feed 29 slugs + mcpservers.org /all page 1), catalog 514 servers / 400 guides
**Fresh window evaluated:** mcp.so feed (31 submissions newest-first), mcpservers.org /all pages 1-3 (51 slugs batch-classified)
**Surfaces:** mcp.so feed via web_extract, mcpservers.org /all pages 1-3 via curl + slug extraction, individual detail pages via web_extract
**Result:** 8 new servers catalogued (8 guides), catalog now 522 servers / 408 guides

## Catalogued (8)

| Server | Slug | Source | Verification |
|---|---|---|---|
| Ryze Google Ads | ryze-google-ads-mcp | mcpservers.org /all | Vendor docs fully mapped: endpoint connector.get-ryze.ai/mcp, OAuth 2.0, 14 tools enumerated with schemas (8 read, 6 write approval-gated), free to connect, Ads Autopilot $89/mo optional; 2,000+ clients |
| BoldDesk | bolddesk-mcp | mcpservers.org /all | Syncfusion vendor docs (developer.bolddesk.com/mcp-server): hosted per-account endpoint your-subdomain.bolddesk.com/mcp, OAuth 2.0 or x-api-key; capabilities documented (tickets, replies, search, approvals), no numbered tool list published |
| Viral Manager | viral-manager-mcp | mcpservers.org /all | Vendor page documents 50 read/write tools with named examples (list_viral_posts, get_post_analysis, create_assignment, get_trending_sounds, summarize_my_accounts); published in official MCP registry as com.viral-managers/viral-manager; endpoint provisioned per workspace, not a static URL |
| Accordio | accordio-mcp | mcpservers.org /all | Vendor docs fully mapped: endpoint mcp.accordio.ai/mcp, scoped OAuth, 28 tools with names (26 free, 2 Legend), free tracking tier, Legend $39/mo; no send/sign/delete/payment verbs by design; Mac tracker open source |
| Watchgoose | watchgoose-mcp | mcpservers.org /all | Vendor docs fully mapped: endpoint mcp.watchgoose.com/mcp, OAuth 2.1 PKCE + DCR, 10 tools enumerated with scopes (read-only default, mcp:write for writes), project-scoped consent, 90-day audit retention |
| Drag | dragapp-mcp | mcpservers.org /all | Vendor docs fully mapped: hosted endpoint app.dragapp.com/mcp or npx @dragapp/mcp-server (MIT), 47 tools across 12 categories fully enumerated, OAuth 2.1 PKCE + DCR, DragApp API key entered once on connect page |
| Modem | modem-mcp | mcpservers.org /all | Vendor docs fully mapped: endpoint mcp.modem.dev/mcp, OAuth with data:read and agent:invoke scopes, 14 tools enumerated with input schemas, 20 calls/min/org/tool rate limit, write tools act as signed-in user |
| OpenShorts | openshorts-mcp | mcpservers.org /all | Vendor docs fully mapped: endpoint mcp.openshorts.app/mcp, OAuth 2.1 or osk_ API key, 8 tools enumerated (process_video, create_upload, get_job_status, list_clips, get_quota, add_subtitles, recut_clip, publish_clip), MIT self-hosted edition, free 20 min/mo cloud |

## Not catalogued (skip prose)

- **Memwyre (/all):** persistent agent-memory layer, 12 tools, remote endpoint server.memwyre.tech/mcp - agent memory infra class (Engram Sep 3 morning, Sirro precedent).
- **Cracked (/all):** pay-per-call aggregator of 63k+ tools, 164 capability surfaces at cracked.ai/mcp - x402 infra class (NanoTools, x402 List precedent).
- **Imaginode (/all):** AI image and video generation, 48 models, 4 tools, API key - media generation class (Deep Art, FLORA precedent).
- **Snipmat (/all):** single-purpose background-removal utility, 5 tools, OAuth, 50 free credits/mo - image utility class (Screenies precedent).
- **HelpMyAgent (/all):** French company and procurement data APIs, $0.002-0.02 per call x402 - regional x402 data catalog class.
- **Naibul (/all):** agent-only board game hall, 11 games, Ed25519 keys - consumer gaming class.
- **Makinai (/all):** consultancy marketing shell with a chatbot, no tool list or endpoint - thin docs class.
- **The 402 Wall 404humans (/all):** agent-only x402 pixel billboard on Base - novelty art class.
- **MyFlohmarkt (/all):** German flea market events search, 3 read-only tools - consumer regional niche class.
- **Feed and /all repeats:** Lawstronaut (resubmission of the July 15 catalogued entry), Klarix and Strac DLP (Sep 3 evening catalogued), Tracetify, Extend, iubenda, Sorank, HiBot (Sep 3 midday catalogued), Furrow Forms, Asyntai, TaiLexi/twlawbot (Sep 3 morning catalogued), AuType, ToBid, Lifesight, NeuralVerge, Farmwalk, Fallax, TheLuckyStrike (Sep 2-3 catalogued). Prior dispositions: pdfAssistant, FLORA, RAVN, Neither, QuantumProxies, Voibe, dot.tools, MarketCode, PostMCP, OSIR Domain, Trendos, Koongo, AON, Hostinger, QoreNext CRM and Trade Screening, send-email, Backblaze B2, Layers, Mantis, ZenSched, Wagglet, Digital Darts, ListingBott, SEObot AI, DevHunt, Rovyn, MarsX, GospelChannel, MagicMaster, NC Wedding Guide, x402 List, Sirro, VenuNite, Slop.
