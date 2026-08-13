---
title: "MCP Sweep — August 12, 2026 (Evening)"
description: "Follow-up to the Aug 12 afternoon sweep (~3 hours later). 4 new business-relevant MCP servers catalogued, 3 integration guides written — consulting-grade deliverable generation, field-service ERP with write-capable MCP, AI-search-visibility tooling, and self-hosted task management."
date: 2026-08-12
sources: [mcpservers.org, mcp.so]
status: complete
finds: 4
guides: 3
---

# MCP Server Discovery Sweep — August 12, 2026 (Evening)

**Timestamp:** 2026-08-12 (evening, UTC)  
**Sources scanned:** mcpservers.org /all page 1 (30 newest, curl + regex slug extraction), mcp.so Feed (33 newest submissions, web_extract), 9 server detail pages fetched (mcp.so + mcpservers.org) for endpoint/auth/tool verification  
**New servers found:** 4 business-relevant (3 guides written, 1 catalog entry)

---

## Summary

| Server | Relevance | Category | Guide |
|---|---|---|---|
| EM+x | ★★★ | Productivity / Consulting deliverables | ✅ |
| ATLASS OS | ★★★ | ERP / Field service | ✅ |
| CiteRank | ★★★ | SEO / GEO / AI visibility | ✅ |
| QTask | ★★ | Task management (self-hosted) | catalog entry |

## Finds

### EM+x — board-ready deliverables from chat
Remote Streamable HTTP server (33 tools, OAuth) that turns conversation into steerco readouts, executive briefs, market scans, and QBR decks — brief files itself from chat, storyline approved before drafting, deterministic quality gates + adversarial partner review, native .pptx/.docx on the user's own templates. Free: 1 project + 5 revisions/mo; paid from $8/mo. `emplusx.com/api/mcp`, by Cubed Studios. Submitted to mcp.so ~8h before this sweep — genuinely new since the afternoon sweep.

### ATLASS OS — field-service ERP with a native MCP surface
Business platform for construction trades (CRM, scheduling, jobs, double-entry books, GST, payroll, payables, inventory) with 58 MCP tools (35 write-capable, 32 permission scopes), machine-censused Aug 10, 2026. Tokens minted in-app; per-call permission checks; every financial write posts balanced double-entry to an append-only audit log; no payment rail by design. Founding-stage rollout in Alberta. `app.atlass-os.com/mcp`. First field-service platform with a working write-capable MCP surface.

### CiteRank — AI search visibility as agent tools
Five MCP tools over an AI-visibility audit suite: URL audits (schema, E-E-A-T, agentic readiness, AI citation score), brand citation checks in Google AI Overviews/Gemini (citation rate, share of voice, competitor analysis), JSON-LD schema generation, agentic-readiness tests (llms.txt, WebMCP, A2A, potentialAction), and agent-journey simulation (book/quote/contact/buy/subscribe). `citerankscore.com/api/mcp-server`. Purpose-built for GEO/AEO programs.

### QTask — self-hosted task management MCP (catalog entry)
Open-source task/project management with built-in MCP server: list/create/update tasks and projects, staged write approval (AI proposes, human approves), semantic search. Self-hosted via Docker + Ollama; hosted qtask.dev available. `github.com/dbeasty/qtask`.

## Cross-reference notes

- **Excluded — catalog-spam burst:** the ~30-entry single-author rudrendupaul burst on mcpservers.org /all page 1 was excluded per the Aug 12 spam-burst doctrine; not cherry-picked.
- **Already covered by prior sweeps:** Clipkit (Aug 12 morning sweep guide exists at `/hermes/mcp/servers/external/clipkit-mcp/`), Prose Coach/ROIC.ai/cloro/Stratyfix/FlowyTeam/QuestDB (afternoon sweep), Syncro/Bastion/wecallio/Klarefi (Aug 11 midday skip list), SonaPrompt/sshmng/ohm/mercury-cortex (afternoon sweep skip list), Sightseer/scvd.store/directree/crosscode-cli (Aug 11 evening skip list).
- **Skipped this sweep:** SceneF (consumer), LabTestSuperstore (lab supplies, re-noted), AgentBrink (agent identity infra), swag2mcp (OpenAPI→MCP dev bridge), US Stocks & Market Data gino.im (overlaps catalogued ROIC.ai), PyPI MCP + ~10 dev/utility entries.
- **Pattern:** the afternoon sweep's "human-gate" observation extends — EM+x (approve-before-draft) and ATLASS OS (scoped, audited writes) both make the human approval boundary the product, one for output, one for money.
