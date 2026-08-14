---
title: "MCP Sweep — August 13, 2026 (Evening)"
description: "Evening sweep. 5 new servers catalogued, 4 guides. Platform MCPs expose read-only analytics warehouses with grant scoping (Alison Evo); data-minimization becomes a feature (easydocforms); verify-before-act rails keep thickening (AgenticRail, glc PromptGuard)"
date: 2026-08-13T18:30:00-07:00
sources: [mcpservers.org, mcp.so]
status: complete
finds: 5
guides: 4
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-august13-2026-evening/"
robots: "index,follow"
last_updated: "2026-08-13"
tags: ["mcp server", "model context protocol", "hermes mcp", "ad analytics", "healthcare", "agent governance", "prompt injection"]

---

# MCP Server Discovery Sweep — August 13, 2026 (Evening)

## Summary

- **5 new business-relevant servers** since the August 13 midday sweep
- **4 integration guides written** (Alison AI, easydocforms, AgenticRail Gate, glc PromptGuard)
- **Platform MCPs now ship read-only analytics warehouses** — Alison Evo's grant-scoped 14-tool surface is the same enforcement philosophy CorpusIQ ships
- **Data-minimization became a product feature** — easydocforms keeps PHI out of agent context entirely
- **Verify-before-act rails keep thickening** — AgenticRail receipt chains and glc PromptGuard join VerityLayer and FLINT
- **Catalog fix** — NERAI Risk Intelligence (guide + docs link since Aug 11) gained its missing body entry

## Sources Scanned

- mcpservers.org /all pages 1-3 (newest submissions)
- mcp.so Feed (30 newest submissions, from 2 hours to 6 days old)
- mcpservers.org + mcp.so server detail pages

## Catalogued (5)

### Alison AI MCP ★★★
Creative intelligence from your ad accounts inside any MCP client — spend and KPIs, creative tags, competitor intelligence (SensorTower/Pathmatics), and creative previews. 14 tools, all read-only; OAuth 2.1 PKCE + RFC 7591 dynamic client registration; the grant decides what the client can see. `evo.alison.ai/mcp`

### easydocforms MCP ★★
Healthcare intake forms over MCP with a PHI-minimization design — import a blank PDF, hand the patient a hosted fill link, retrieve the completed PDF; PHI never enters agent context. Docker-hosted (ghcr.io/easydocforms/easydocforms-mcp), API key auth, MIT. `github.com/easydocforms/easydocforms-mcp`

### AgenticRail Gate MCP ★★
Deterministic step-order enforcement for AI agents — evaluate_step returns ALLOW/DENY before a step runs and every ALLOW writes an Ed25519-signed, hash-chained receipt (R2-stored, tamper-evident); verify_receipt proves chain integrity. Public demo key, no auth required. `mcp.agenticrail.nz`

### glc PromptGuard ★★
Eight-layer source-aware prompt-injection gate — checks user prompts, RAG chunks, and tool outputs before they reach the model or tool loop. Intent × source × impact scoring, typed verdicts, agent self-registration tokens. `mcp.glc-rag.hu/mcp`

### Untangle Bio MCP ★ (catalog entry only)
Self-serve biotech process design — generate downstream purification routes, simulate separations, and run techno-economic analysis (CAPEX/OPEX/payback) from Claude via MCP or the web app. Vertical niche; notable as the TEA-over-MCP pattern. `untangle.bio`

## Also Identified (not catalogued)

- **Imag8 Studio** — style-locked AI image generation; listing is a one-liner with no MCP tool docs (thin-docs rule)
- **AppaTools MCP Studio** — no-code MCP server builder (dev tool)
- Repeats already skipped in prior sweeps: Syncro, LabTestSuperstore, SceneF, FLINT Network, Constants, Faxer, Departi, LocalCan, x402 tooling (Merchant Check, scvd.store, agent-economy), GetLulu micro-utilities, PyPI MCP, King Crimson MCP, swag2mcp, Sonaprompt, MoodleMCP, US Stocks (gino.im), ViewMade, TrueSend, Folklore Helena, AgentBrink, exposed-port junk slugs on /all pages 2-3

## Catalog Fixes

- **NERAI Risk Intelligence** — guide written and docs-linked in the Aug 11 afternoon sweep, but no catalog body entry was ever inserted. Added under Compliance & Regulatory.

## Key Observation

The five servers split into three patterns. (1) Platform MCPs now expose read-only analytics warehouses with server-side grant scoping — Alison Evo's "the grant decides, not the client" is the enforcement philosophy CorpusIQ ships natively. (2) Data-minimization is becoming a product feature — easydocforms' PHI-never-enters-context design extends the approval-gate pattern the Aug 12-13 sweeps tracked from actions to data itself. (3) The verify-before-act layer keeps thickening — AgenticRail's signed receipt chains and glc PromptGuard's source-aware injection gate join VerityLayer and FLINT as agent-governance rails, making this the fastest-growing new segment in the ecosystem.
