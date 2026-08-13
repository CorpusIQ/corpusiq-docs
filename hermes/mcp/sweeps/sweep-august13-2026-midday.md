---
title: "MCP Sweep — August 13, 2026 (Midday)"
description: "Midday sweep. 8 new servers catalogued, 7 guides. Approval gates became the default architecture (BusyMail, Shipstar, OnePostly, DialNexa); voice AI gained a full-platform MCP (DialNexa); EU procurement surfaced (TED Tender Monitor)"
date: 2026-08-13T11:00:00-07:00
sources: [mcpservers.org, mcp.so, github.com]
status: complete
finds: 8
guides: 7
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-august13-2026-midday/"
robots: "index,follow"
last_updated: "2026-08-13"
tags: ["mcp server", "model context protocol", "hermes mcp", "social publishing", "voice ai", "procurement"]

---

# MCP Server Discovery Sweep — August 13, 2026 (Midday)

## Summary

- **8 new business-relevant servers** since the August 12 evening sweep
- **7 integration guides written** (OnePostly, Shipstar, DialNexa, Just Domain, Fakto.app wFirma, BusyMail, TED Tender Monitor)
- **Approval gates are now the default architecture** — BusyMail, Shipstar, OnePostly, and DialNexa all ship human-gate or permission-split designs
- **Voice AI gained its first full-platform MCP** — DialNexa with OAuth 2.1 PKCE and safety-level classification
- **EU public procurement surfaced as a vertical** — TED Tender Monitor, the first procurement entry in the catalog

## Sources Scanned

- mcpservers.org /all pages 1-3 (newest submissions)
- mcp.so Feed (33 newest submissions, from 2 minutes to 6 days old)
- mcp.so server detail pages, mcpservers.org detail pages, GitHub repo trees

## Catalogued (8)

### OnePostly MCP ★★★
Nine-platform social publishing over MCP — publish, schedule, and read normalized insights across X, Instagram, Facebook, Threads, LinkedIn, TikTok, YouTube, Pinterest, and Reddit. Bearer API keys with read_only variants; wallet-debited X pass-through billing; 9 tools with per-platform validation. `mcp.onepostly.com`

### Shipstar MCP ★★★
Product-marketing automation from commits — 21 tools generate changelogs, blog posts, feature pages, KB articles, release emails, X threads, and LinkedIn posts, then route every draft through review, approval, and publish. OAuth 2.1 with per-project scoping. `mcp.shipstar.ai/mcp`

### DialNexa MCP ★★★
Voice AI agent platform over MCP — create and manage voice agents, place confirmed outbound calls, run campaigns and batch calls, search and buy numbers, and read dashboard metrics. Every tool classified read-only/state-changing/destructive/billable with approval required before calls or spend. OAuth 2.1 PKCE, workspace-scoped consent. `api.dialnexa.com/v1/mcp`

### Just Domain MCP ★★
Domain availability and pricing checks for AI assistants — first-year AND renewal prices plus a checkout link for justdomain.ai. Read-only by design: no purchase in chat. No auth, Streamable HTTP. `mcp.justdomain.ai`

### Fakto.app wFirma MCP ★★
The only MCP for wFirma.pl (Polish accounting) — full read-write across ~45 tools: invoices, contractors, expenses, warehouse, KPiR and ZUS, cashflow forecasts, payment reminders. OAuth 2.0 (RFC 7591). Sister server for Fakturownia.pl. `fakto.app/wfirma/stream`

### BusyMail MCP ★★
IMAP email over MCP with the strongest approval gate observed: a token can never send — it queues, and approval happens while signed in, so the writer and approver can never be the same session. Scoped read/organize/send tokens. Invite-only. `busymail.app/mcp`

### TED Tender Monitor ★★
EU TED procurement monitoring via an Apify Actor — search notices by CPV, country, keyword, value, or type; persistent tasks deliver only new or changed tenders with dedup state. $0.005 per new tender. 13 example tasks + n8n and Make templates. `github.com/Telemark-Digital/apify-monitoring-workflows`

### KPainter MCP ★★ (catalog entry only)
Source-grounded videos, slides, and interactive knowledge content from your own materials. stdio MCP (`kp-mcp` CLI) with API key; `kp_*` tools with scene-level edits. `kpainter.ai`

## Also Identified (not catalogued)

- **ViewMade** — YouTube research/SEO/video production; listing page is only a support page, no MCP endpoint or tool docs
- **TrueSend** — email marketing ESP; listing page is homepage marketing copy, no MCP surface documented
- **Folklore Variant Evidence** (helena.bio) — genomics ACMG/AMP variant classification; healthcare niche
- **AgentBrink** — agent identity infra; already noted in the Aug 12 evening sweep
- Usual dev-tool/consumer entries (PyPI MCP, x402 tooling, GetLulu micro-utilities — previously noted)
- One junk slug on /all page 2 (exposed-port OpenClaw host dump) excluded

## Key Observations

1. **Approval gates went from pattern to default.** The Aug 12 sweeps flagged the human-gate pattern in content tools (Prose Coach, BanProof, Plainpaper). This sweep found the same architecture as the baseline across four unrelated domains: BusyMail (a token can never send email), Shipstar (approve_content before publish_content), OnePostly (read_only keys), and DialNexa (safety-level classification with mandatory confirmations before billable or destructive calls). Approval gates moved from content into email, marketing, social, and voice.

2. **Voice AI gained a full-platform MCP.** DialNexa is the first voice-agent platform observed with a production MCP surface covering the whole lifecycle — agents, calls, campaigns, workflows, numbers, billing, and metrics — behind OAuth 2.1 PKCE.

3. **EU public procurement surfaced.** TED Tender Monitor is the first procurement entry in the catalog. Its design (discovery vs persistent monitoring, dedup state, per-event pricing) is a template for how vertical lead-intelligence MCPs should be built.

4. **Regional accounting keeps deepening.** Fakto.app (wFirma.pl + Fakturownia.pl) follows the Polish Honest MCP suite — EU accounting MCPs are arriving one locale at a time, each with full write paths and local tax compliance.

## Catalog State

- Catalog: 174 servers (+68 guides), up from 166 (+61)
- Previous sweep: August 13 morning (10 finds, 0 guides, report only)
- Next sweep: evening or next cycle
