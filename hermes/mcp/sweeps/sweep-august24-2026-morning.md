---
title: "MCP Discovery Sweep - August 24, 2026 (Morning)"
date: 2026-08-24
tags: [mcp-sweep, discovery, catalog]
description: "chatmcp/mcpso issues #3719-#3725 (Aug 24 07:39-09:41 UTC), mcp.so feed, mcpservers.org /all pages 1-3, mcp.so and mcpservers.org homepages; 8 catalogued with guides, 24 skipped"
last_updated: "2026-10-19"
---

# MCP Discovery Sweep - August 24, 2026 (Morning)

- **Cutoff:** night cron sweep evaluated chatmcp/mcpso issues through #3718 (Aug 24 02:00 UTC) and recorded /all pages 1-3 skips
- **Fresh window:** chatmcp/mcpso issues #3719-#3725 (Aug 24 07:39-09:41 UTC), mcp.so feed (30), mcpservers.org /all pages 1-3 (90 slugs), both homepages
- **Result:** 8 catalogued with guides, 24 skipped

## Catalogued (8 guides)

| Server | Stars | Category | Source |
|---|---|---|---|
| Acquisition.gov MCP (deterministic read-only FAR Overhaul model parts, agency-deviation index, deviation PDFs, RFO guidance; 5 verified tools with content hashes, canonical URLs and extraction warnings; stdio, uvx acquisition-gov-mcp==1.0.2, no credentials, MIT; registry com.1102tools/acquisition-gov-mcp; sibling to the 1102tools-dev 8-server federal data family) | 20 (family repo) | Compliance | chatmcp/mcpso issue #3720 + repo README |
| Universal Poison Armor (open-source prompt-injection and dataset-poisoning firewall: indirect injection, zero-width Unicode steganography, GCG suffixes, tracking pixels, Markdown XSS, semantic poisoning, Sybil/consensus attacks; sanitize_document + scan_dataset_for_anomalies on a local FastMCP server plus SKILL.md directives; MIT) | 0 | Security | mcpservers.org /all page 3 + GitHub README |
| SalesTouch (LinkedIn GTM prospecting platform: account, conversation, lookup, outreach, engagement, publishing, durable scheduling, queue, paginated extraction; OAuth browser flow at salestouch.io/api/mcp, v0.8.0, MIT; LinkedIn credentials never shared with the agent; mutations approval-gated) | 2 | Sales & Outreach | mcpservers.org /all page 1 + GitHub README |
| Agency AI MCP (hosted ad manager for Meta and Google accounts: 14 typed tools incl. create_ad, update_campaign, set_campaign_status, get_pacing, get_anomalies, get_performance_timeseries, get_recommendations; remote at s.agencyai.app/mcp; Apache-2.0; deepest automation on Shopify) | 1 | Marketing | mcpservers.org /all page 1 + GitHub README |
| Lavox Memory (local-first macOS meeting recorder: on-device Whisper, speaker ID, embeddings; two-layer bitemporal SQLite memory with typed decision index storing chosen option, rejected alternatives and reasoning anchored to verbatim quotes; local server 127.0.0.1:8040 + lavox-mcp.sh; MIT) | 1 | Productivity | chatmcp/mcpso issue #3724 + repo README |
| Electronics RFQ Agent (RFQ-to-quote automation: parses PDF/Excel/Word RFQs, prices line items against ERP catalogs, fill-rate audit; 9 tools incl. quote_rfq, audit_quote, check_inventory; connects SAP/Epicor/Oracle/Dynamics via their MCP servers; PyPI electronics-rfq-agent-cli; MIT) | 0 | ERP | mcpservers.org /all page 2 + GitHub README |
| Phonotheca MCP (read-only full-text search over interview transcript archives: speaker-labelled, timestamped passages with citation attached; Streamable HTTP at phonotheca.com/api/mcp, revocable bearer tokens, free account tier; license not declared) | 0 | Content & Research | mcpservers.org /all page 2 + GitHub README |
| Shotstack MCP (official hosted video editing API: render video and images, template rendering with merge values, template CRUD, render status, Studio editor links; endpoint mcp.shotstack.io confirmed live via 401 auth gate; API key auth) | n/a (hosted, no repo) | Content | mcp.so feed + mcp.so listing page |

## Skipped (24)

- **1102tools 8-server federal family (issue #3721)**: bls-oews, ecfr, federal-register, gsa-calc, gsa-perdiem, regulations-gov, sam-gov, usaspending-gov. Pre-existing April 2026 mcp.so listings surfaced by a publisher-migration update, not new submissions. Catch-up candidates for a future sweep.
- **AgentPub (#3719)**: agent-to-agent private messaging network. Agent community infra class, Fomite precedent.
- **Quantum Readiness Scan qrp-mcp (#3722)**: offline codebase crypto scanner. Dev tool.
- **Fleetpost (#3723)**: server-less agent mailbox coordination. Agent infra.
- **Daytime Agent Market (#3725)**: Base Sepolia testnet task marketplace. Agent infra, TaskMarket class.
- **MetricFire**: official infra-monitoring MCP; endpoint not verifiable from public pages (blog and /mcp 404). Thin docs.
- **BitBrowser MCP service**: antidetect browser automation, thin docs. Dev automation class.
- **Tseha**: design-system serving for coding agents. Dev tool.
- **NobGit**: git hosting platform MCP. Dev tool.
- **Swarme**: governed MCP tool-access marketplace. Thin docs.
- **Frantic**: agent bounty board paid in USDC on Base. Agent marketplace class.
- **Claude News**: Anthropic news feed. News category covered by Webz.io and NewsMind (CLSTR precedent).
- **Figs Relationship Expert**: consumer therapy persona.
- **Lucid Page**: Markdown to shareable page. Doc publishing utility, Booklet class.
- **Ssave**: TikTok/Instagram/YouTube downloader. Consumer media utility.
- **mcp.so homepage and feed repeats** already evaluated in Aug 23 sweeps: Mangii, Hypnothera, Agent Conductor, CodeSentinel, QR Planet, RADAAR (catalogued), Dados B3, Upfirst, Xverum, Simplepages, Signal Nodus, SavePropTax, Hermoso, AskRentAI, Truth Bear, TEOS WARN Act.
