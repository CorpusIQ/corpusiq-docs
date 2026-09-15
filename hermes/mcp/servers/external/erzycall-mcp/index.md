---
title: "ErzyCall MCP - Real Phone Calls and WhatsApp for Agents"
description: "Hosted MCP that gives agents and apps real phone calling: place and receive calls with confirmation-before-dial, manage contacts, cases and assistants, send WhatsApp messages, and report on usage over OAuth 2.1. No API key needed."
category: Communication & Email
stars: "n/a (hosted service)"
added: 2026-09-01
source: "chatmcp/mcpso issue #3876 (Sep 1, 2026 midday sweep)"
relevance: ★★
tags: [mcp-server, phone-calls, voice, whatsapp, contact-management, telephony, oauth, remote-mcp]
---

# ErzyCall MCP

**Hosted phone-calling MCP for agents and apps.** ErzyCall lets an agent or application place and receive real phone calls and WhatsApp messages through MCP without assembling a telephony stack. OAuth 2.1 sign-in scopes the connection to one organization, calls require explicit confirmation before dialing, and everything lands in the ErzyCall account's call log with usage reporting. Fresh submission; endpoint live and OAuth-gated.

```
Server type: Hosted, remote (Streamable HTTP)
Endpoint: https://app.erzycall.com/api/mcp
Auth: OAuth 2.1 PKCE + Dynamic Client Registration; no API key needed for MCP
Tools: capability-level across calls, contacts, cases, assistants, phone numbers, WhatsApp and usage (served after sign-in)
Pricing: account-based; API keys exist only for the REST API
Category: Communication & Email
Built by: ErzyCall (erzycall.com)
```

## Why This Matters for Operators

Voice remains the highest-touch channel for appointments, confirmations and escalations, and it is the channel most AI agents cannot touch. ErzyCall removes that wall by giving the agent real calling capability without assembling SIP trunks, phone numbers and call scripts.

First, **confirmation-gated dialing.** The assistant asks for confirmation before it places a real call or sends a WhatsApp message, so autonomous workflows stay inside the operator's control.

Second, **call context lives where the work lives.** Contacts, cases, assistants and call scripts are ErzyCall resources the agent reads and updates, so a call is prepared and logged from the same context as the follow-up email or CRM note.

Third, **usage visibility.** The usage scope and webhooks expose call activity and events, so operators can measure what the agent actually did on the phone instead of trusting a summary.

## Tools and Capabilities

Capability-level table sourced from the vendor's MCP docs and OAuth scopes; the live tool list is served from the endpoint after OAuth sign-in (anonymous enumeration is refused with 401).

| Surface | What it covers |
|---------|----------------|
| Calls | Place outbound calls with scripts, take inbound calls, read call logs and outcomes (calls:read, calls:write) |
| Contacts & Contact Groups | Read and manage the people the agent can reach (contacts:read, contacts:write, contact_groups:read) |
| Cases | Track call-related cases and follow-ups (cases:read, cases:write) |
| Assistants | The calling personas and scripts the agent uses (assistants:read, assistants:write) |
| Phone Numbers | Read the organization's numbers available to dial from (phone_numbers:read) |
| WhatsApp | Send and read WhatsApp messages (whatsapp:read, whatsapp:write) |
| Usage & Webhooks | Usage reporting plus real-time event webhooks (usage:read) |

## Installation

```bash
claude mcp add --transport http erzycall https://app.erzycall.com/api/mcp
```

Paste the endpoint into any MCP client and sign in. Leave the client ID and secret blank - the server registers your tool automatically via Dynamic Client Registration. No API key is needed for MCP; keys exist only for the REST API.

## Configuration

```json
{
  "mcpServers": {
    "erzycall": {
      "type": "http",
      "url": "https://app.erzycall.com/api/mcp"
    }
  }
}
```

First connection opens a browser sign-in where you pick which ErzyCall organization to connect; only that organization's data is reachable. Grants are revocable any time from the AI tool's connector list, and tokens expire on their own. The endpoint is POST-only Streamable HTTP (GET returns 405); SSE is not supported.

## Business Relevance

- **Field-service and appointment-based operators** let the agent call customers to confirm tomorrow's appointments using the operator's own scripts.
- **Sales and follow-up teams** have the agent place follow-up calls and log outcomes, with WhatsApp as the text fallback.
- **Support operations** route inbound calls and cases with the same context the agent already has from the CRM.
- **Agencies and multi-client setups** connect one ErzyCall per client organization and revoke cleanly per engagement.

## Integration with CorpusIQ

ErzyCall composes with CorpusIQ as the action layer on top of the business data CorpusIQ already reads. A CorpusIQ agent can watch Stripe payment failures or HubSpot deal stages, then trigger an ErzyCall confirmation or follow-up call with the context assembled from those connectors, and write the call outcome back into HubSpot or a Gmail thread as the closing note. The operator keeps one governance point: ErzyCall's confirmation gate means the agent proposes the call and the human approves the dial, while CorpusIQ supplies the account context that makes the call worth making. Webhooks close the loop, feeding call events back into the operator's dashboards alongside the other business signals.

## Limitations

- Brand new listing - no track record or public adoption data yet.
- OAuth sign-in required per organization; no anonymous or API-key-only MCP mode.
- Voice compliance is the operator's responsibility - the vendor's docs state that calling capability is not permission to contact people; consent and jurisdiction rules apply.
- Capability-level tool table above; exact tool names appear after sign-in.
- Hosted service only - no self-host option documented.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [imap-mcp - Read-Only IMAP Mailbox Operations for Agents](/docs/hermes/mcp/servers/external/imap-mcp)
- [Atomic Mail MCP - Programmable Inbox for AI Agents](/docs/hermes/mcp/servers/external/atomic-mail-agentic)
