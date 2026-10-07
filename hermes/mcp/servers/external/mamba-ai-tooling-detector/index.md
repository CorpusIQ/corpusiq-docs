---
title: "Mamba AI Tooling Detector MCP - AI Adoption Signals"
description: "Evidence-backed AI adoption tiers for any company domain: commercialized, deployed, declared or none, with the signals behind every call."
category: Competitive Intelligence
stars: n/a (npm package, MIT)
added: 2026-10-07
source: "chatmcp/mcpso issue #4855 (Oct 7, 2026 morning sweep)"
relevance: ★★
tags: [ai-adoption, competitive-intelligence, gtm, sales-signals, clay, apify, local-mcp, npm]
---

# Mamba AI Tooling Detector MCP

**Local MCP server (stdio, npm) - evidence-backed AI adoption reads** for any company domain: whether a company only talks about AI, actually runs AI tooling on its site, or charges money for AI, with the proof behind the tier.

```
Server type: Local (stdio), TypeScript, Node 18+
Auth: Your own Apify API token (APIFY_TOKEN)
Package: @mambalabsdev/mcp-ai-tooling-detector (npm, MIT, v1.3.1)
Tool: detect_ai_tooling (single tool, read-only, idempotent)
Registry: com.mambabuilt/mcp-ai-tooling-detector
Pricing: Apify credits per domain analyzed (free Apify plans get 15 results/month)
Cache: 7-day result cache (skipCache to force a fresh run)
Built by: Mamba Labs (part of the Mamba Labs GTM Suite)
```

## Why This Matters for Operators

AI claims are cheap and everywhere. The useful question is whether a company deploys AI, sells AI, or only name-drops it - and that question has observable evidence: pricing pages, inference endpoints, vendor fingerprints, llms.txt files and crawler rules. This server turns that evidence into a four-level maturity tier so competitive and market research stops at the claim and starts at the proof.

The tier model is the product: `commercialized` means the company charges for AI (credits, token allowances, AI-named plans or per-outcome pricing on the pricing page); `deployed` means AI tooling is running on the site; `declared` means they say AI with nothing observable beyond copy and crawl rules; `none` means nothing fired. A domain behind a bot challenge comes back flagged as blocked at low confidence instead of a confident "no".

## Tools & Capabilities

| Tool | What the agent can do |
|---|---|
| `detect_ai_tooling` | Read a domain's AI maturity tier with the evidence behind it; single or batch mode; optionally narrowed to chosen vendors |

Key inputs:
- `domain` or `domains` (batch mode takes precedence).
- `vendors` - report only specific tools among the 52 fingerprinted vendors (for example Sierra, Decagon, Intercom Fin, OpenAI API, Anthropic API, Pinecone, LangChain). Omitting it reports everything.
- `check_pricing` - default true; required to prove the `commercialized` tier.
- `skipCache`, `batchSize` and a request timeout for larger runs.

## Installation

```bash
npm i @mambalabsdev/mcp-ai-tooling-detector
```

Or run it without installing via `npx` using the configuration below.

## Configuration

```json
{
  "mcpServers": {
    "mamba-ai-tooling-detector": {
      "command": "npx",
      "args": ["-y", "@mambalabsdev/mcp-ai-tooling-detector"],
      "env": { "APIFY_TOKEN": "your-apify-token" }
    }
  }
}
```

Get a token at console.apify.com/account/integrations. The server lists its tools without a token; the token is needed to run a lookup, and each call runs the Mamba Labs actor under your own Apify account. The same tools also ship in the umbrella `@mambalabsdev/mcp-gtm-suite` package if you would rather run one server than many.

## Business Relevance

- **Competitive research:** read whether a competitor's AI story matches deployed tooling or stays on marketing copy.
- **Sales targeting:** find companies whose AI spending is real before pitching into them.
- **Market mapping:** batch-check a cohort and rank it by AI maturity evidence.
- **Due diligence light:** a fast outside-in read on what a company runs before a call.

## Integration with CorpusIQ

CorpusIQ connects the operator's own systems - CRM, ads, store, accounting - for consistent answers from their own data. The AI Tooling Detector adds the outside-in read: what a target, competitor or partner actually runs. Pair a pipeline in CorpusIQ with an AI maturity check on every account in it.

## Limitations

- Tiers are static-signal reads; a site that reveals AI only after JavaScript runs can be undercounted.
- Batch runs consume Apify credits per domain; check the actor page for costs before large batches.
- Vendor detection covers the 52 fingerprinted tools; niche or in-house systems may not be attributed.
- Results are cached for 7 days; force a fresh run when recency matters.

## FAQ

### What counts as commercialized?

Charging for AI: AI credits, token allowances, AI-named plans or per-outcome AI pricing on the pricing page.

### Does it work on sites that block crawlers?

Yes, with honesty: a blocked domain returns `blocked: true` at low confidence instead of a false "none".

### Do I need an Apify account?

Yes. The server is a thin client for the Mamba Labs actor; calls run on Apify under your own account and token.

## See Also

- [Mamba Ecommerce Platform Profiler MCP - Stack Detection](/hermes/mcp/servers/external/mamba-ecommerce-platform-profiler/)
- [Mamba Outbound Infrastructure Fingerprint MCP](/hermes/mcp/servers/external/mamba-outbound-infrastructure-fingerprint/)
- [Signal Six MCP - Cited Competitive Intelligence](/hermes/mcp/servers/external/signal-six-mcp/)
- [Debriefing MCP - Competitor Moves with Evidence](/hermes/mcp/servers/external/debriefing-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
