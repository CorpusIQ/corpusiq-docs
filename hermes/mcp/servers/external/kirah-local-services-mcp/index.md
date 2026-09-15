---
title: "Kirah Local Services MCP: Local Business Discovery"
description: "Keyless MCP gateway to the Kirah local services marketplace: search businesses, list services with pricing, duration and intake fields, check real-time availability, and create, reschedule or cancel bookings. 10 tools live-probed on kirah-agent-gateway v2.16, read-only discovery with guest-checkout booking."
category: Business Operations
stars: n/a (new listing)
added: 2026-08-23
source: "mcpservers.org homepage + live endpoint probe"
relevance: ★★★
tags: [local-services, booking, marketplace, availability, smb, remote-mcp, keyless]
---

# Kirah Local Services MCP

**One keyless endpoint opens a real local services marketplace to agents: search businesses, read their published service catalogs (price, duration, deposit, intake fields), check live availability, and book appointments - with guest checkout that needs only a name and email.** Kirah runs a gateway (`kirah-agent-gateway`, live-probed at v2.16, protocol 2025-03-26) at `https://kirah.ai/api/mcp` that serves both global discovery (find any AI-discoverable business) and tenant-scoped booking operations for a named business.

```
Server type: Remote (Streamable HTTP, hosted)
Auth: None (keyless discovery; guest checkout for bookings)
Endpoint: https://kirah.ai/api/mcp
Tools: 10 (live-probed; server v2.16, protocol 2025-03-26)
OpenAPI: https://kirah.ai/.well-known/kirah-gateway.openapi.json
Built by: Kirah (kirah.ai)
```

## Why This Matters for Operators

Local services are the long tail of business operations: finding an available plumber, booking a cleaning, rescheduling an inspection - these are phone-call workflows that agents historically could not touch. **Kirah exposes the marketplace itself as tool calls: `search_businesses` discovers active providers globally, `list_services` reads a provider's authoritative catalog with pricing and intake requirements, and `get_availability` returns real open slots for an exact date range.** The booking lifecycle (create, status, reschedule, cancel) is tool-native, which means an operator's agent can book real appointments end to end, including the reschedule dance that eats human hours.

## Tools & Capabilities

10 tools confirmed by live probe:

| Tool | Purpose |
|---|---|
| search_businesses | Global cross-tenant discovery: find active, AI-discoverable Kirah businesses when the user has not named one |
| list_services | A tenant's authoritative catalog: services with price, duration, deposit and intake fields, providers, timezone |
| search_services | Lexical helper: rank up to 5 catalog services against a short free-text query |
| get_availability | Open slots for a service across an exact YYYY-MM-DD date range (max 31 days, max 20 slots) |
| find_available_services | Global bounded earliest-availability search across businesses when the user wants the soonest opening |
| create_booking | Book an exact ISO-8601 instant for a client (guest checkout: name + email, phone optional) |
| get_booking_status | Current state of a booking by tenant and booking reference |
| get_reschedule_options | Read-only: valid move windows for a booking (requires the booking's grant) |
| reschedule_booking | Move an existing appointment to a new time |
| cancel_booking | Cancel an appointment the agent booked |

The gateway is read-only for discovery and writes only through the booking tools, with grant tokens scoping reschedule and cancel to the booking that created them.

## Installation

```json
{
  "mcpServers": {
    "kirah": {
      "type": "http",
      "url": "https://kirah.ai/api/mcp"
    }
  }
}
```

For the Claude Code CLI: `claude mcp add --transport http kirah https://kirah.ai/api/mcp`

## Configuration

No API key for discovery. Bookings use guest checkout (name + email, phone optional); deposit-required tenants surface the deposit in the service catalog so the agent can inform the client before committing. The full API surface, including the mcp-directory and mcp-info endpoints, is documented in the published OpenAPI spec at `https://kirah.ai/.well-known/kirah-gateway.openapi.json`.

## Example Prompts

- "Find a house cleaner available in my area next week with reviews, and list their prices."
- "Book the earliest appointment with a licensed electrician for Thursday."
- "Reschedule my booking to Friday morning if there is an open slot."
- "What deposit does this business require before booking?"

## Business Relevance

Local service discovery and booking are high-friction workflows for operators in field services, property management and consumer ops: comparing providers, checking availability and managing reschedules across phone and email. Kirah MCP moves that into the agent loop, so an operations assistant can propose a real bookable slot instead of a search-result list. The global discovery tools also make it a live directory of local SMBs - useful for market research on service density and pricing.

## Integration with CorpusIQ

CorpusIQ is the read-side authority for a business's own systems (CRM, calendar, billing). Kirah MCP adds the external local-services layer: an agent can find and book a provider (Kirah), then log the booking and reconcile the spend in CorpusIQ. Bookings made through Kirah become structured, auditable events rather than off-the-books phone calls.

## Limitations

- Marketplace coverage is Kirah's business network only; no data for businesses not on the platform.
- Discovery is free-form text search over catalogs; there are no reviews or ratings tools in the exposed surface.
- Booking writes are guest-level: name, email, optional phone - the agent must relay deposit terms and confirmations to the client.
- Reschedule and cancel require the grant token from the original booking, so those operations must stay in the same session or store the grant.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external) - curated third-party MCP servers for operators
- [Austin MLS MCP](/docs/hermes/mcp/servers/external/austin-mls-mcp) - regional real estate listings with photos and detail pages
- [MCP Integration Guide](/docs/hermes/mcp) - connecting MCP servers to Hermes Agent
