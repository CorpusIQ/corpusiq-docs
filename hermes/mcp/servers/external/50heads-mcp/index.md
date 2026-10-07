---
title: "50heads MCP - Ask 50 Verified People from Your Agent"
description: "Ask a short question to 50 phone-verified people and get the split, margin and confidence, from any MCP client with a daily spend cap."
category: Research
stars: n/a (hosted + npm, MIT)
added: 2026-10-07
source: "chatmcp/mcpso issue #4892 (Oct 7, 2026 morning sweep)"
relevance: ★★
tags: [market-research, surveys, human-data, product-testing, oauth, remote-mcp, npm]
---

# 50heads MCP

**Hosted MCP server (Streamable HTTP, OAuth 2.1) plus a local npx bridge - ask real people** one short question from your agent and get how they split: the winner, the margin and how confident you can be. About ten minutes for 50 answers, from 20p an answer.

```
Server type: Hosted (stateless Streamable HTTP) + local stdio bridge
Auth: OAuth 2.1 (PKCE S256, dynamic client registration) or an fh_live_ API key
Endpoint: https://mcp.50heads.com/mcp
Tools: 18 across ask, results, targeting, exports and account reads
Pricing: Per answer from GBP 0.20; daily spend cap per connection set at consent (5,000 credits default)
Registry: com.50heads/mcp (official MCP registry)
Built by: 50heads
```

## Why This Matters for Operators

Testing a name, an image or a line used to mean either guessing or commissioning a study. This is the middle path an agent can drive end to end: choose a question type (single choice, A/B image, pairwise, scale, ranking, yes-no or free text), pick the audience (countries, languages, pool bands, interest audiences, tiers), estimate the price and time first (`estimate` never spends), then ask and read the result as winner, margin and confidence - exportable as CSV, a PDF report or a PNG card.

The trust mechanics are the point: phone-verified heads, tier-2 ID checks, per-answer attestation references that can be flagged for review with upheld flags refunded, and a daily spend cap per connection that is set at consent and can be revoked in a second.

## Tools & Capabilities

| Tool | What the agent can do |
|---|---|
| `estimate` | Price, time and validation for a question; never spends, call it first |
| `ask` | Post a question (returns a task; needs an idempotency key) |
| `get_results` / `wait_for_results` | Read the results object, partial while live; wait up to 600 seconds with a minimum answer count |
| `list_questions` / `cancel` / `add_heads` | Reuse recent questions, stop a live one (with refunds), top up a question with more heads |
| `get_answers` / `export` / `flag_answer` | Individual answers a page at a time (filtered by option, tier, country, age band or keyword), file exports, and per-answer flags |
| `templates` / `list_targeting` / `list_audiences` | Fixed-price templates, targetable countries and bands, and interest audiences with prices by grade |
| `balance` / `upload_image` / `build_ask_link` | Credits and cap remaining, image upload for a question, and portal links for a human to confirm |

Pre-filled ask links (`https://50heads.com/app/ask?...`) open the composer for a person to check the price and press Ask; `build_ask_link` writes them.

## Installation

Claude (claude.ai and Desktop): add a custom connector at `https://mcp.50heads.com/mcp` and sign in with OAuth.

```bash
claude mcp add --transport http 50heads https://mcp.50heads.com/mcp
```

Local bridge (Node 20+): `npx -y @50heads/mcp` with an `FIFTYHEADS_API_KEY`, or a one-time `npx -y @50heads/mcp login`.

## Configuration

```json
{
  "mcpServers": {
    "50heads": {
      "url": "https://mcp.50heads.com/mcp"
    }
  }
}
```

Local alternative with an API key:

```json
{
  "mcpServers": {
    "50heads": {
      "command": "npx",
      "args": ["-y", "@50heads/mcp"],
      "env": { "FIFTYHEADS_API_KEY": "fh_live_..." }
    }
  }
}
```

## Business Relevance

- **Founders:** A/B two names, two hero images or two lines with real people before committing.
- **Marketers:** quick message and creative tests with margins and confidence that can go straight into a deck.
- **Product teams:** put a question to an audience mid-sprint and read the split the same session.
- **Anyone spending on ads or packaging:** a small, bounded test beats an expensive guess.

## Integration with CorpusIQ

CorpusIQ answers "what is happening in the business" from the operator's own connected systems. 50heads answers "what would people choose" from a verified panel. Ask the question, then measure the outcome against your own numbers.

## Limitations

- Paid per answer; run `estimate` first (it is free) and set the daily spend cap before a team uses it.
- Answers are the opinions of a verified panel, not a census; read the margin and confidence with the split.
- Rate limits: 60 requests a minute and 10 asks a minute per connection; 1 MB request bodies.
- If a question is refused or invalid, the call errors with a one-sentence reason a model can act on.

## FAQ

### How fast are answers?

About ten minutes for 50 answers is typical; rush mode aims for under an hour, and `wait_for_results` can park for up to 600 seconds.

### What does it cost?

From GBP 0.20 per answer depending on audience and tier; `estimate` returns price and time and never spends.

### Can I control the spend?

Yes. A daily spend cap is set per connection at consent (5,000 credits by default), changeable or revocable in the portal; a revoked connection stops within a second.

### Who are the heads?

Phone-verified people, with tier-2 ID checks; answers carry attestation references and upheld flags are refunded.

## See Also

- [Revup MCP - Promotions, Forms and Giveaways](/hermes/mcp/servers/external/revup-mcp/)
- [AskOne MCP - Live Q&A and Polls for Events](/hermes/mcp/servers/external/askone-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
