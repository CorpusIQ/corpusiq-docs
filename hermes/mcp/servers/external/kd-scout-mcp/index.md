---
title: "KD Scout MCP: Keyword Research Arithmetic"
description: "Zero-dependency MCP server for keyword research arithmetic - difficulty estimation 0-100, blended opportunity scoring, and structured content briefs with H2 outline, word-count target and schema type. Deterministic mode needs no API keys."
category: SEO
stars: 0
added: 2026-08-23
source: "mcpservers.org /all + GitHub README"
relevance: ★★
tags: [keyword-research, seo, content-briefs, difficulty-scoring, content-planning, self-hosted]
last_updated: "2026-10-24"
---

# KD Scout MCP

**A zero-dependency MCP server for keyword research arithmetic - difficulty estimation, opportunity scoring, and structured content briefs - that runs anywhere Python 3.10+ runs with no packages and no API keys required for the deterministic mode.** The scoring model is derived from the editorial pipeline behind Groundwork's money and tools research, where it screens hundreds of candidate keywords weekly.

```
Server type: Local (stdio, pip package)
Auth: None (deterministic mode)
Package: pip install kd-scout
Tools: 3 (keyword_difficulty, opportunity_score, content_brief)
License: MIT
Category: SEO
Built by: moiosintel (GitHub)
```

## Why This Matters for Operators

Keyword research tools are either expensive subscriptions or free interfaces that bury the arithmetic in dashboards. KD Scout exposes the arithmetic directly to your agent: difficulty 0-100 per keyword, a blended opportunity score that weighs difficulty against monthly volume, and a content brief with H2 outline, word-count target, FAQs and schema type. Because it is deterministic and local, the same inputs always return the same scores - results you can diff, log and reason about instead of trusting a black box.

This is a screening instrument, not a full SEO suite: it answers "which of these 50 keywords should we actually write for" inside the agent that already has your content plan, at zero marginal cost, with no vendor lock-in.

## Tools & Capabilities

| Tool | Input | Output |
|---|---|---|
| `keyword_difficulty` | `keywords[]` | Per-keyword difficulty 0-100 |
| `opportunity_score` | `difficulty`, `monthly_volume` | Blended 0-100 opportunity score |
| `content_brief` | `topic` | H2 outline, word-count target, FAQs, schema type |

## Installation

```bash
pip install kd-scout
kd-scout            # stdio MCP server
```

Or point any MCP client at the module directly:

```json
{ "command": "kd-scout" }
```

## Configuration

```json
{
  "mcpServers": {
    "kd-scout": {
      "command": "kd-scout"
    }
  }
}
```

No keys, no signup, no network calls in deterministic mode. The production scoring model comes from Groundwork's editorial pipeline (gworky.com/money).

## Business Relevance

- **Content teams** screen hundreds of candidate keywords weekly and get a defensible shortlist with difficulty and opportunity scores.
- **SEO operators** get deterministic scoring they can log and compare across months, instead of a tool's changing proprietary metric.
- **Agencies** produce structured content briefs (outline, word count, FAQs, schema) straight from the agent that drafts the article.
- **Anyone allergic to subscriptions** gets keyword arithmetic for free, locally, with no vendor dependency.
