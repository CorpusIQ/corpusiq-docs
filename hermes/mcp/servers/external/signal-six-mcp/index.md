---
title: Signal Six MCP - Cited Competitive Intelligence
description: "Competitor moves scored and cited with the page and date behind each one: signals, 90-day reports, a market map and your profile over remote MCP."
category: Competitive Intelligence
stars: n/a (new listing)
added: 2026-10-05
source: mcp.so feed (Oct 5, 2026 midday sweep)
relevance: ★★★
tags: [competitive-intelligence, competitor-tracking, market-monitoring, signals, reports, remote-mcp, oauth]
---

# Signal Six MCP

**Remote MCP server (Streamable HTTP, OAuth)** - the official server from Signal Six that puts competitive intelligence inside the assistant where the questions already happen. Ask what competitors shipped, repriced or changed, and every answer comes back with the page behind the move and the date Signal Six saw it.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth, one authorization scoped to your company
Endpoint: https://signalsix.ai/api/mcp
Surface: Signals, Reports, Market map, Profile
Docs: signalsix.ai/connect/claude
Availability: invitation-based onboarding (sign-ups closed while teams onboard)
```

## Why This Matters for Operators

Competitive research is the work that never gets scheduled. You know the questions matter - what did the competitor ship last quarter, how do they price the Pro plan, where do their capabilities edge out yours - but the answers live across dozens of pricing pages, changelogs and launches nobody has time to re-read. Signal Six has already done the reading: it scores every competitor move, keeps the page it happened on and the date it was observed, and writes 90-day reports against your company profile.

This server makes that intelligence queryable from the assistant you already work in. Instead of opening another dashboard, the operator asks "what moved this week?" in the same thread where the rest of the business gets discussed - and gets back scored moves, newest first, each with its source page and observation date that can be checked in one click.

## What the Agent Reads

| Surface | What it returns |
|---|---|
| Signals | Every competitor move scored for your company - search them, open one, or count them by competitor, category, importance or month |
| Reports | Your 90-day reports, listed and read back in full: the executive summary, the openings and risks, the deep dive on each competitor |
| Market map | The companies in your market, what each sells, what it costs, its capabilities, its customers, and what changed |
| Your profile | Your company and strategy - the lens every alert and report is written through; edits start as a preview, and saving is a separate step |
| Strategy refresh | A packaged skill reads the quarter's moves against the profile and proposes a rewrite; nothing is saved until you approve it |

## Installation

Add the server endpoint to any MCP client:

```bash
claude mcp add signal-six --transport http https://signalsix.ai/api/mcp
```

The first connection opens a browser sign-in and authorizes one company. Each person connects their own account, and the authorization is scoped to your company: it is revoked the moment you leave it.

## Business Relevance

- **Cited, every time**: every move the agent reads carries the page behind it and the date it was seen, so any claim can be checked in one click.
- **Quarterly rhythm**: 90-day reports turn scattered launches and price changes into a read on openings and risks.
- **Market map on demand**: pricing, capabilities and customers as each company publishes them, side by side with yours.
- **Review before saving**: the strategy refresh proposes changes and waits; nothing is written until a person approves.

## Integration with CorpusIQ

CorpusIQ reads the numbers inside the business - revenue, spend, traffic, pipeline - read-only and cited. Signal Six covers the mirror surface: the market outside it. An operator can ask about their own performance through CorpusIQ and about the competitive field through Signal Six in the same conversation, with both sides keeping source links on every claim.

## Limitations

- Access is currently invitation-based: sign-ups are closed while the vendor onboards a small group of teams, and setup starts with a conversation.
- Answers are scoped to what Signal Six has observed and scored for your company; it is a monitoring layer, not a live crawler the agent can point anywhere.
- One authorization per company; each person connects their own account.
- Hosted by Signal Six and governed by its terms; a live POST initialize returns 401 unauthenticated, confirming it is auth-gated.

## FAQ

### What is Signal Six?

A competitive intelligence service for teams: it scores competitor moves across the market (shipped, repriced, changed), keeps the source page and observation date on every move, and writes 90-day reports against your company profile.

### How does authentication work?

OAuth through the MCP client - the first connection opens a browser sign-in and approves one company. The authorization is scoped to that company and is revoked when you leave it.

### What does "cited" mean here?

Every competitor move carries the page behind it and the date Signal Six saw it, so the operator can check any claim at the source in one click.

### How do I get access?

Access starts with a conversation while the vendor onboards teams hands-on and connects the server live on the call; the connect page for Claude is at signalsix.ai/connect/claude.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
