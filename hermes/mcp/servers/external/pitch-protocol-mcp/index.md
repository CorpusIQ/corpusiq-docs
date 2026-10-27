---
title: "Pitch Protocol MCP - Agent-Native VC Applications"
description: "A founder-side server for agent-native venture capital: your agent packages and submits the pitch, and 15+ partner funds review it against their theses."
category: Finance / Fundraising
stars: n/a (new listing)
added: 2026-10-13
source: "mcp.so feed (October 13, 2026 evening sweep)"
relevance: ★★
tags: [venture-capital, fundraising, founders, pre-seed, seed, agent-native, keyless, remote-mcp]
last_updated: "2026-10-24"
---

# Pitch Protocol MCP

**Remote MCP server (Streamable HTTP, no account required)** - a founder-side application rail: your agent packages the company and submits the application to Pitch Protocol, where it is reviewed and matched against the theses of 15+ partner venture funds, and interested funds reach out directly.

```
Server type: Remote (Streamable HTTP), founder-side endpoint
Auth: None on the founder endpoint (no key)
Endpoint: https://api.pitchprotocol.vc/mcp/founder
Tools: 7 (schema, create, submit, update, verify, status)
Pricing: Free for founders
Built by: Pitch Protocol (pitchprotocol.vc)
Listing: mcp.so feed, October 13, 2026 evening sweep
```

## Why This Matters for Operators

Fundraising has an operations problem inside it: the application itself. Every fund wants the same facts in a different form, and most of the work is packaging what the founder already knows into a structure someone else can review. That is exactly the kind of work an agent with the company's context can do.

Pitch Protocol turns the first step into a tool call. The agent reads the application schema, fills it from what it knows about the company, submits, and the founder verifies by email. One submission is reviewed and matched against the theses of 15+ partner funds; funds that are interested contact the founder directly. About ten minutes, no web form, and the deck is optional.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| get_application_schema | The application structure the agent fills (fields, formats, expectations) |
| create_application | Start the application for a company |
| submit_answers | Submit the packaged answers |
| update_application | Revise an application after submission |
| verify_email | Verify the founder by email (the application counts once verified) |
| get_status | Read the application status |
| resend_verification | Resend the verification email |

## Installation

```
claude mcp add pitch-protocol --transport http https://api.pitchprotocol.vc/mcp/founder
```

Any MCP client that speaks Streamable HTTP can add the same URL. Pitch Protocol also publishes a skill file: point an agent at `https://api.pitchprotocol.vc/skill.md` and ask it to submit your company.

## Configuration

```json
{
  "mcpServers": {
    "pitch-protocol": {
      "type": "http",
      "url": "https://api.pitchprotocol.vc/mcp/founder"
    }
  }
}
```

## Business Relevance

- **Founders raising pre-seed or seed** submit through their own agent in about ten minutes, from any geography, without filling in a web form
- **Operators preparing a round** let the agent package the standardized parts (the company story, the numbers it already has) while they keep the judgment calls on how to pitch
- **Advisors and fractional teams** help several companies apply in the same structured way
- **Funds and scouts** get applications in a consistent, verified format instead of a per-fund form

## Integration with CorpusIQ

Pitch Protocol covers the application rail: schema, submission and status. CorpusIQ answers the surrounding business question from connected sources such as revenue data, spreadsheets, email and accounting, so the numbers that go into an application can be pulled together alongside the narrative.

Used together: ask CorpusIQ for the operating picture (revenue, customers, pipeline, runway) and submit through Pitch Protocol when it is time. Pitch Protocol stays the submission channel; CorpusIQ remains the place the company's operating answers live alongside.

## Limitations

- Brand new (v0.1.0 at listing time): the fund count, the theses and the review process are as the vendor states on their site
- A submission channel, not a guarantee: it routes your application to partner funds, and interest is theirs to give
- The founder endpoint is keyless; review the current terms and privacy page on pitchprotocol.vc before submitting
- Free for founders (pre-seed and seed, any geography)

## FAQ

### Is it really keyless?

Yes on the founder endpoint. A live probe returned 200 on initialize and `tools/list` with all 7 tools, no account or key.

### What actually happens after submission?

The application is reviewed and matched against the theses of 15+ partner venture funds; funds that are interested reach out to the founder directly. The `get_status` tool reads where the application stands.

### Who is it for?

Founders raising a pre-seed or seed round, anywhere in the world. The deck is optional and applying is free.

### How does it fit with other fundraising tools?

It is the application and submission side. The catalogued Fund Momentum entry covers the intelligence side (fund data, investor signals, matching), and Binderwork covers startup paperwork such as SAFEs and data rooms; Pitch Protocol completes the set with the actual application rail.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [Fund Momentum MCP - VC Intelligence for AI Assistants](/hermes/mcp/servers/external/fund-momentum-mcp/)
- [Binderwork MCP - Startup Paperwork and SAFE Rounds](/hermes/mcp/servers/external/binderwork-mcp/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
