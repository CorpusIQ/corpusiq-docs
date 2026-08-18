---
title: "Prose Coach MCP - CorpusIQ Docs"
description: Deterministic AI-writing filter for MCP agents — flags 43 AI-writing patterns with quoted evidence and fixes before content ships
category: Content
stars: 0 (brand new)
added: 2026-08-12
source: mcp.so
relevance: ★★★
tags: [content, writing, editing, ai-writing, brand-voice, marketing, remote-mcp]
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/prose-coach-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"

---

# Prose Coach MCP

**Remote MCP server (Streamable HTTP, no auth) for Prose Coach.** A deterministic writing filter that marks 43 patterns that make text read as AI-generated — banned vocabulary and structural tells (triplets, negation formulas, summary closers, colon chains, flat rhythm) — with every finding quoting the line that triggered it and attaching the fix.

```
Server type: Remote (Streamable HTTP)
Auth: None
Endpoint: https://www.prose.coach/mcp
Pricing: Free tier (3 drafts/day, 12,000 chars per request); PRO $5/mo or $50/yr
Category: Content / Writing
```

## Why This Matters for Operators

Every AI assistant reaches for the same moves across every draft. Prose Coach is the first MCP purpose-built to de-AI drafts before they ship: a fixed rule set runs over your text, flags what's there, and density is scored against an accumulation threshold — one marker is noise, six is a habit. Because no language model reads your text, the same input always returns the same findings — unlike probabilistic "99% AI-written" detectors whose scores can't be checked against anything.

## Tools & Capabilities

| Tool | Tier | What it returns |
|---|---|---|
| `scan_draft` | Free | Every finding with the line quoted and the fix attached |
| `coach_draft` | PRO | Scan + the written rule behind each finding, scope map for content type, judgment layers |
| `verify_revision` | PRO | Before/after diff: patterns resolved, reduced, still present, or newly introduced |

Two prompts (`scan`, `polish`) ship alongside the tools. Re-scanning a draft after edits doesn't count against the free daily limit.

## Installation

```bash
claude mcp add prose-coach --transport http https://www.prose.coach/mcp
```

Per-client walkthroughs (Claude Code, Codex, Cursor, VS Code): [prose.coach/connect](https://www.prose.coach/connect)

## Configuration

```json
{
  "mcpServers": {
    "prose-coach": {
      "type": "http",
      "url": "https://www.prose.coach/mcp"
    }
  }
}
```

No API key. A browser scanner at [prose.coach](https://www.prose.coach/) runs the same engine if you want to try it before connecting anything.

## Business Relevance

- **Marketing teams** can run every email, ad, and social post through `scan_draft` before it ships — structural tells (triplets, summary closers) are exactly what makes mass-produced AI copy feel uncanny
- **Content operators** get a free tier covering 3 drafts/day — enough for daily posting cadences without a subscription
- **Founders and executives** get a deterministic filter instead of an opaque AI-probability score they can't verify
- **Agencies** can standardize voice at scale — PRO ($5/mo) gates `verify_revision`, which diffs the rewrite against the original

## Integration with CorpusIQ

Prose Coach pairs with CorpusIQ's business-data connectors on the content side of the stack: an agent pulls live numbers (Shopify orders, GA4 traffic, ad spend) through CorpusIQ, drafts customer-facing copy from that data, then runs the draft through Prose Coach before anything ships. CorpusIQ supplies the data; Prose Coach polishes the prose. The composition is natural for the same workflows covered by CorpusIQ's content-ops tooling: weekly performance recaps, customer win emails, and product update posts — all drafted by agents, all passed through a deterministic writing filter before they reach a human.

## Limitations

- Brand new — listed on mcp.so Aug 12, 2026, no ecosystem track record yet
- Free tier is a single tool (`scan_draft`); `coach_draft` and `verify_revision` require PRO
- The 43-pattern rule set targets English-language writing moves
- It flags patterns and attaches fixes — it does not rewrite; the revision happens in your client
- Hosted endpoint only (no self-hosted option); no auth means no account-scoped history

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
