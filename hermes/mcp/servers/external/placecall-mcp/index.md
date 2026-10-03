---
title: "PlaceCall MCP - Agent Phone Calls to Real Businesses"
description: "Remote MCP and skill that lets an agent dial US businesses, navigate IVRs and hold, and return a verified outcome with transcript and recording."
category: "Automation"
stars: n/a (hosted platform, voygr.tech)
added: 2026-10-03
source: "mcpservers.org server page (voygr-tech/placecall)"
relevance: ★★★
tags: [automation, voice, phone, agents, bookings, quotes, remote-mcp, real-world]
---

# PlaceCall MCP

**Hosted MCP server** - PlaceCall gives an agent a phone. Hand it a US number or just describe the place, give it a task in plain English, and it dials, navigates IVRs and hold, talks to the business, and returns a verified outcome plus transcript and recording.

```
Server type: Hosted (streamable HTTP, remote) plus skill/plugin packages
Auth: OAuth sign-in or X-API-Key / Bearer header
Endpoint: https://api.voygr.tech/mcp
Registry: io.github.voygr-tech/placecall
Pricing: first 250 calls free
Category: Automation
Built by: Voygr (ex-Google Maps and Search team)
```

## Why This Matters for Operators

MCP extends agents to APIs. PlaceCall extends them to the physical world, where the interface is a phone number and an IVR tree. That covers the work API-only automation cannot reach: confirming a restaurant's kitchen hours, getting a quote from a supplier, checking stock, or booking and rescheduling appointments.

The return shape is deliberately verifiable. Every call ends in one of 17 defined outcomes with a full transcript and recording, including explicit failure reasons such as dropped calls, busy lines, voicemail and wrong numbers. An agent can report what actually happened rather than assuming success. Batches are supported, so a list of businesses can be contacted at once.

## What Agents Can Do

- Book, cancel or reschedule tables and appointments.
- Verify information, follow up on orders, check stock, get quotes.
- Contact many businesses in one run.
- Recommend a venue or vendor when you do not have a number, explaining why it picked them.
- Ask a question mid-call when the brief leaves room for it.

## Connect

- **claude.ai chat / ChatGPT:** add a custom connector or MCP app pointing at `https://api.voygr.tech/mcp`, then sign in with Google or email.
- **Any MCP client:**
```
claude mcp add --transport http --scope user placecall https://api.voygr.tech/mcp \
  --header "X-API-Key: <your key>"
```
- **Hermes:**
```
hermes mcp add placecall --url https://api.voygr.tech/mcp/ --auth header
```
Hermes stores the key in `~/.hermes/.env` and references it from config, so the value never lands in the config file. Note the trailing slash on the URL. Use the MCP route, not the skill route, on Hermes: a skill that sends an API key by curl to a non-loopback host trips Hermes's own scanner by design.

## Limitations

- US numbers only.
- Placing a call always confirms before dialing.
- The 250 free calls are per account; a key is required for real calls beyond that.

## FAQ

### Does PlaceCall confirm before calling?

Yes. Connecting through a connector or key always confirms before a call is placed, and calls bill to the key or account in use.

### What comes back from a call?

A verified outcome from a set of 17, plus the transcript and recording, with clear failure reasons for calls that do not complete.

### Can it call businesses outside the US?

No. PlaceCall handles US numbers only.

## Related

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - the curated catalog
- [MCP Ecosystem Sweeps](/hermes/mcp/sweeps/) - all sweep reports
