---
title: "Personhood MCP - CorpusIQ Docs - CorpusIQ Docs"
description: Rewrite AI-generated text to read as human in a chosen voice for LinkedIn posts, cold emails, and DMs, delivered as a hosted MCP
category: Marketing
stars: n/a (new listing)
added: 2026-08-17
source: mcp.so GitHub issue #3611
relevance: ★★
tags: [content, ai-detection, de-ai, voice, copywriting, linkedin, cold-email, remote-mcp]
---

# Personhood MCP

**Hosted remote MCP server (Streamable HTTP) that rewrites AI-generated text so it reads as human, in a chosen persona's voice.** It removes common AI tells and rewrites text in preset or custom voices for LinkedIn posts, cold emails, DMs, and tweets. Free credits to start, billed per generation.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer API key (givepersonhood.com account)
Endpoint: https://api.givepersonhood.com/mcp
Registry: com.givepersonhood/personhood
Pricing: Free credits to start, then per-generation billing
Category: Content Operations
Built by: Personhood (givepersonhood.com)
```

## Why This Matters for Operators

Outbound content now competes in an inbox and a feed that have both learned to spot AI text. The operator's problem is not generation anymore, it is delivery: the message has to read like a person wrote it, or it never gets a reply. Personhood turns that into a transformation step the agent applies to its own drafts before anything ships.

The persona voices are the operational feature: a cold-email sequence, a founder's LinkedIn posts, and a support DM can each carry a distinct, consistent voice, defined once and applied by the agent at send time. For teams running multi-persona outbound programs, that consistency is normally a copy-editing tax; here it is one MCP call.

## Tools & Capabilities

| Capability | What it does |
|---|---|
| Humanizing rewrite | Removes AI tells and rewrites text to read naturally |
| Persona voices | Preset and custom voices applied consistently per use case |
| Channel formats | Tuned for LinkedIn posts, cold emails, DMs, and tweets |
| Billed by generation | Free credits to start, then pay per rewrite |

## Installation

```bash
claude mcp add --transport http personhood https://api.givepersonhood.com/mcp
```

Create an account at givepersonhood.com, copy the API key, and pass it as the Bearer token.

## Configuration

```json
{
  "mcpServers": {
    "personhood": {
      "type": "http",
      "url": "https://api.givepersonhood.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

## Business Relevance

- **Founders** keep their personal voice consistent across LinkedIn and outbound without drafting by hand
- **Sales teams** run multi-persona cold-email programs with per-persona voices
- **Marketing operators** apply the rewrite step before publishing anything agent-drafted
- **Support teams** soften AI-drafted replies into natural customer-facing language
- **Agencies** offer voice-consistent content across every client account from one surface

## Integration with CorpusIQ

Personhood is the last step before content ships; CorpusIQ is the measurement after it does. A draft flows through Personhood's rewrite inside the agent session, ships through the operator's normal channel, and the resulting engagement lands in CorpusIQ's GA4 and Meta Ads views for the next iteration. The loop closes: measure which personas perform, then tighten the voices that underperform.

## Limitations

- Brand new listing (Aug 17, 2026), no track record yet
- Hosted service: your drafts transit their API (review data handling before using on sensitive material)
- Rewrites are a style transformation, not a fact check: verify claims separately
- Per-generation pricing means cost scales with volume: watch it on high-frequency pipelines
- No self-host option published

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
