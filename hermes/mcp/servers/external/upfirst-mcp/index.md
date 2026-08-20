---
title: "Upfirst MCP - AI Phone Receptionist for Small Businesses"
description: "First-party MCP server for Upfirst, the AI answering service: configure greetings, knowledge, skills, transfer rules and schedules, and audit call transcripts and missed-call outcomes from any MCP client"
category: Communication
stars: n/a (new listing)
added: 2026-08-20
source: mcpservers.org
relevance: ★★★
tags: [ai-receptionist, phone-answering, small-business, call-transcripts, appointment-booking, customer-service, front-office, remote-mcp]
---

# Upfirst MCP

**Remote MCP server (Streamable HTTP, OAuth connect flow) — the official Upfirst integration for configuring and auditing your AI phone receptionist from any MCP client.** Upfirst answers a business's calls, takes messages, books appointments and answers questions about the business. The MCP server exposes the receptionist's settings and call history as agent tools, so an AI assistant can review recent calls, fill knowledge gaps, and edit greetings, transfer rules and schedules in place — the phone line becomes a system an operator tunes from chat instead of a settings dashboard.

```
Server type: Hosted remote (Streamable HTTP)
Auth: OAuth-style connect flow (endpoint URL provisioned in-app)
Endpoint: provisioned in the Upfirst app (Add connector flow)
Tools: 9 (calls, transcripts, knowledge, skills, agent settings)
Pricing: free tier available (no credit card to try)
Category: Communication / Front Office
Built by: Upfirst (upfirst.ai)
```

## Why This Matters for Operators

A missed call is a missed lead, and the classic failure mode of AI receptionists is silence: the receptionist picks up, botches a question, and nobody in the business ever finds out. Upfirst MCP closes that loop. The agent can pull `list_calls`, open `get_call_details` and `get_call_transcript`, and read `get_agent_knowledge` to see exactly what the receptionist actually said — then push a fix with `update_agent_knowledge` so the same failure never repeats. The audit-to-fix cycle that used to require listening to recordings and navigating a dashboard now runs entirely inside an agent session.

The second win is configuration from a description. `create_agent_skill` and `create_agent_knowledge` let an agent build a complete receptionist setup — greeting, knowledge base, transfer rules, weekly schedules, SMS follow-up skills — from a plain paragraph about the business. That collapses a multi-hour setup into one prompt, which matters most for operators running several locations or brands, where each line needs its own greeting, hours and transfer map.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `list_calls` | Filter and search past calls by status, tags, or date range |
| `get_call_details` | Full detail for a single call |
| `get_call_transcript` | Transcript of a specific call for outcome analysis |
| `get_agent_knowledge` | Read the receptionist's current knowledge entries |
| `create_agent_knowledge` | Add knowledge entries (from a business description or gap audit) |
| `update_agent_knowledge` | Edit knowledge entries to fix mis-handled calls |
| `create_agent_skill` | Add SMS, scheduling, or call-transfer skills incl. weekly schedules and transfer destinations |
| `update_agent_skill` | Adjust existing skills in place |
| `update_agent_by_id` | Change conversational parameters: greeting, voice tone, hold music (partial updates supported) |

## Installation

The connection is created from the Upfirst app, not from a config file you assemble yourself: Upfirst provisions the MCP endpoint URL in-app, then you add it as a connector in Claude, ChatGPT, Gemini, or any MCP client and approve with your existing Upfirst login.

```bash
# Once the URL is provisioned in-app:
claude mcp add upfirst --transport http <provisioned-endpoint-url>
```

No local install and no API key to store in your client config — approval happens through the Upfirst account.

## Configuration

```json
{
  "mcpServers": {
    "upfirst": {
      "type": "http",
      "url": "<endpoint-url-from-upfirst-app>"
    }
  }
}
```

Auth note: the vendor does not publish a public endpoint string; the URL is issued per account from the app (Settings). Treat the directory-listed tool surface above as verified from the official listing, and the live tool list as served from your provisioned endpoint.

## Business Relevance

- **Local services operators** (clinics, salons, trades, agencies) get a phone line that answers 24/7 and a chat surface to review every missed call and fix the receptionist the same day
- **Multi-location owners** can stand up per-location greetings, hours, and transfer rules from one agent session instead of clicking through per-branch settings
- **Front-office managers** get call-transcript search to audit how the receptionist answers pricing, hours, and booking questions
- **Marketing leads** see the appointment-booking outcome per call, so ad-driven call volume can be tied to actual booked revenue

## Integration with CorpusIQ

Upfirst MCP pairs naturally with the CorpusIQ CRM connectors: after a call lands a booking, the operator reads the outcome through the CorpusIQ HubSpot or Close connector and logs the lead with the call transcript as context, so pipeline attribution runs from ad click to answered call. For businesses that run Calendly on the front end, the CorpusIQ Calendly connector shows the appointments the receptionist actually generated, closing the loop between phone coverage and booked pipeline. The direction of flow: Upfirst MCP handles the phone conversation; CorpusIQ reads the downstream business systems the conversation feeds.

## Limitations

- Brand new listing — no community track record yet
- Endpoint URL is provisioned per account in-app, not published; setup requires an Upfirst account
- The receptionist quality itself depends on Upfirst's voice stack; the MCP layer tunes it but cannot replace it
- Phone-centric value — businesses without meaningful call volume will see less payoff
- Live tool list served from the provisioned endpoint; tool names above come from the official directory listing

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
