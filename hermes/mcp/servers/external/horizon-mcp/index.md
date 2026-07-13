---
title: "Horizon AI Intelligence MCP — Integration Guide"
description: "Free AI-industry intelligence for agents — briefings, regulation tracker, and regional lenses."
category: mcp
tags: [mcp-server, ai-intelligence, regulation, briefings, policy]
last_updated: 2026-07-13
---

# Horizon AI Intelligence MCP — Integration Guide

**Provider:** system-alchemist
**GitHub:** system-alchemist
**Category:** AI & Agents — Industry Intelligence
**Listing:** mcp.so (July 13, 2026)

## Overview

Horizon AI Intelligence is a free MCP server providing AI-industry intelligence directly to AI agents. It delivers briefings, tracks AI regulation changes, and offers regional lenses for understanding the AI landscape across different jurisdictions.

## Why This Matters for Operators

- **Regulation tracking:** AI regulation is evolving rapidly (EU AI Act, US executive orders, China AI laws). Horizon tracks changes so operators don't have to.
- **Competitive intelligence:** Briefings on AI industry movements help operators understand where the market is heading.
- **Regional lenses:** Different rules apply in different regions — Horizon provides jurisdiction-specific context.
- **Free:** No API key or payment required — lowers the barrier to AI industry awareness.

## Installation

```json
{
  "mcpServers": {
    "horizon": {
      "command": "npx",
      "args": ["-y", "@system-alchemist/horizon-mcp"]
    }
  }
}
```

## Available Tools

*To be confirmed from the provider documentation:*
- AI industry briefing retrieval
- Regulation change tracking
- Regional compliance lens queries
- Policy update notifications

## Use Cases

1. **Compliance Planning:** AI agents monitor regulation changes and flag impacts on your product or operations
2. **Market Research:** Pull AI industry briefings to inform product strategy and competitive positioning
3. **Regional Expansion:** Use regional lenses to understand AI compliance requirements before entering new markets
4. **Investor Updates:** Generate AI industry context for board decks and investor communications

## Complementary to CorpusIQ

CorpusIQ provides operational business data. Horizon provides the AI industry context around that data — operators can combine market intelligence with their own metrics for strategic decision-making.

## Status

⚠️ **New listing (July 13, 2026)** — early-stage, independent developer. Value proposition is strong (free, regulation-focused) but monitor for maintenance cadence before relying on it for compliance-critical workflows.
