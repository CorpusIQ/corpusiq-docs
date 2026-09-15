---
title: "Klarix Intelligence Engine MCP - B2B Competitive Intelligence"
description: Live B2B competitive intelligence for agents - prospect matching over vector-embedded company profiles, 5-axis ICP fit scoring, competitor battlecards, tech stack teardowns and displacement playbooks built from cited public-web evidence
category: Sales & Outreach
stars: n/a (new listing)
added: 2026-09-03
source: "mcp.so feed"
relevance: ★★★
tags: [competitive-intelligence, sales-intelligence, icp-scoring, battlecards, prospect-research, remote-mcp, keyless]
---

# Klarix Intelligence Engine MCP

**Remote MCP server (Streamable HTTP, keyless) for B2B competitive and sales intelligence built from cited public-web evidence.** Fifteen tools, live-verified: semantic prospect matching over tens of thousands of pre-profiled companies, five-axis ICP fit scoring, live competitor battlecards, head-to-head comparisons, buying-committee mapping, account trigger detection, and institutional-grade tech-stack and product teardowns. Every answer is grounded in public web sources the agent can cite.

```
Server type: Remote (Streamable HTTP)
Auth: None required for reads (keyless)
Endpoint: https://mcp.klarix.ai/mcp
Tools: 15 (prospect matching, ICP scoring, battlecards, research, teardowns)
Pricing: Hosted; docs at klarix.ai/docs/api
Category: Sales & Competitive Intelligence
Built by: SpeaksenseAI (github.com/SpeaksenseAI/klarix)
```

## Why This Matters for Operators

The pre-call homework that separates a winning sales motion from a cold one - who the buying committee is, what changed at the account, where the incumbent is weak - usually lives in three tools and a consultant. Klarix compresses it into one endpoint the agent can call mid-conversation. The ICP scoring is the operator-friendly part: score a company against YOUR ideal customer profile on five weighted axes (Strategic Fit, Tech Alignment, Buyer Persona Readiness, Growth signals, and more) instead of renting a fit model. The battlecard and teardown tools run live research, so the SWOT and the displacement playbook carry current, citable evidence rather than last quarter's deck.

**Live-verified keyless.** The endpoint answered an anonymous MCP probe (server `klarix-intelligence v0.1.0`, protocol 2025-03-26) with all 15 tool names - no account needed to enumerate the surface.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `find_matched_prospects` | Semantic search over pre-profiled B2B companies (Voyage 4 embeddings, sub-100ms) |
| `score_prospect_fit` | Five-axis ICP fit scoring per account |
| `get_competitor_battlecard` | Live SWOT and positioning gap for a competitor domain |
| `analyze_head_to_head` | Your company vs a specific competitor, researched both sides |
| `get_company_intelligence` | Executive one-pager from live public sources |
| `generate_outreach_sequence` | Cold outreach that opens on a researched, dated insight |
| `get_market_landscape` | Tier-1 incumbents vs emerging challengers for a vertical |
| `get_buying_committee` | Economic Buyer, Champion, Technical Evaluator, Procurement mapping |
| `detect_account_triggers` | Leadership changes, funding, hiring surges, product updates |
| `teardown_tech_stack` | Technical stack deconstruction with displacement opportunities |
| `generate_displacement_playbook` | Switching-cost mitigations, POC blueprints, migration plans |
| `teardown_product_spec` | Hardware, battery, medical or API teardown to institutional grade |

Plus `generate_swot_analysis`, `get_deep_research` and `search_scientific_evidence` for citable literature.

## Installation

```bash
claude mcp add --transport http klarix https://mcp.klarix.ai/mcp
```

No key. The same endpoint works in Claude Desktop, Cursor, VS Code and any Streamable HTTP MCP client.

## Configuration

None required. For higher-rate or gated tool access, see the API docs at klarix.ai/docs/api.

## Business Relevance

Founders and revenue operators get a standing competitive-intelligence function inside their agent: score inbound leads against the ICP before the SDR touches them, generate battlecards on demand for pipeline reviews, and teardown a competitor's stack before a positioning conversation. The cited-evidence design means the outputs survive a skeptical review.

## Integration with CorpusIQ

CorpusIQ connects your own business systems (CRM, ads, commerce, finance) as read-only context. Klarix adds the external layer: prospect fit, competitor posture and market landscape. Together they give an agent both sides of a sales or expansion decision - internal performance from CorpusIQ, external evidence from Klarix - in one conversation.

## Limitations

- Pre-profiled company universe is tens of thousands, not the full B2B web; long-tail accounts may miss the vector index
- Early-stage (v0.1.0) - tool surface and pricing may shift
- Anonymous probe succeeded, but high-volume commercial use may require a key

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Xverum MCP - People Search Across 750M Professional Profiles](/docs/hermes/mcp/servers/external/xverum-mcp)
- [Apollo.io MCP - Lead Search and Contact Enrichment](/docs/hermes/mcp/servers/external/apollo-io-mcp)
- [Signal Nodus SEC Filings MCP - Primary-Source SEC Intelligence for AI Agents](/docs/hermes/mcp/servers/external/signal-nodus-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
