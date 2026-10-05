---
title: Instant Expert MCP - Paid Expert Calls for Agents
description: Remote MCP that finds executives, operators and domain experts, sends paid invitations and charges only when they book the call or answer.
category: Business Operations
stars: n/a (new listing)
added: 2026-10-04
source: mcp.so feed
relevance: ★★★
tags: [business-operations, expert-network, research, customer-discovery, sales, outreach, remote-mcp, oauth]
---

# Instant Expert MCP

**Remote MCP server (Streamable HTTP, OAuth)** - the official server from Instant Expert that gets a short call or a written answer from a specific professional. The agent finds the person (by description, or starting from a name and company, LinkedIn URL or email), checks the work email, and prepares a paid invitation with your message, request type and per-person offer. Nothing is sent or charged until you approve, you pay only if the person books or answers, and unanswered requests expire after 7 days at zero cost.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth
Endpoint: https://instant.expert/mcp
Tools: People search, lists, paid request drafts, request tracking, replies
Pricing: Pay per booked call or written answer; minimum $5 per person, 20% fee included
Category: Business Operations
Built by: Instant Expert
```

## Why This Matters for Operators

Expert networks used to be an enterprise line item with a screening call before you could even search. Instant Expert flips that into a self-serve flow an assistant can drive: describe who you need to talk to (for example, "procurement directors at US hospitals"), and the server finds the person and their work email, then sends a paid invitation with your offer attached. The commercial model is outcome-based: you are charged only when the person books or answers, and requests expire after 7 days with nothing charged.

For founders and operators this is customer discovery, sales research and due diligence in one surface. Instead of guessing what a buyer segment cares about, an operator buys a handful of calls and has the assistant turn the transcripts and written answers into a decision memo.

**The key advantage is expert access priced per outcome and gated by explicit approval.**

## Tools & Capabilities

| Capability | What it does |
|---|---|
| Find people | Search by description, or start from a name and company, LinkedIn URL or email |
| Lists | Save and inspect people lists across requests |
| Paid request drafts | Compose the message, choose a call or written answer, set a per-person offer (minimum $5) and a total spending cap |
| Approval gate | Nothing is sent or charged without the buyer's explicit approval |
| Track and read | Follow request states and read replies as they come in |

You set the offer per person and Instant Expert's 20% fee is included. A request that expires after 7 days is never charged. The endpoint requires OAuth sign-in on first connect.

## Installation

```bash
claude mcp add instant-expert --transport http https://instant.expert/mcp
```

Sign in with OAuth when prompted. The same endpoint works in Claude, ChatGPT, Cursor, Codex and any client that supports remote MCP servers. Docs: instant.expert/docs/mcp.

## Business Relevance

- **Customer discovery** - talk to the exact buyers a product targets before committing to a roadmap.
- **Sales research** - have a short paid call with a prospect's peer to learn how their buying process actually runs.
- **Due diligence** - reach operators who have worked with a company, market or vendor you are evaluating.
- **Product validation** - turn "would someone pay for this?" into a small set of paid conversations with a decision attached.
- **Recruiting research** - map a function by speaking with practitioners in it before writing the role.

## Integration with CorpusIQ

CorpusIQ reads the business; Instant Expert reaches the people around it. An operator can pull revenue trajectory from CorpusIQ's Stripe connector, see which segments moved in GA4, and then buy two or three expert calls to pressure-test why - an assistant drafts the invitation with the numbers attached and later folds the answers back into the memo.

A composed workflow: measure with CorpusIQ's read-only connectors, validate with Instant Expert calls, and let the same assistant keep the evidence in one thread. Neither system writes to the other; each answers a question the other cannot.

## Limitations

- Paid per booked call or written answer; minimum $5 per person, with the 20% platform fee included in your offer.
- Availability depends on the person; requests that go unanswered expire after 7 days and are never charged.
- Built for reaching specific people, not for volume cold outreach.
- OAuth sign-in is required; there is no static-key path documented.
- The service is hosted by Instant Expert and governed by its terms.

## FAQ

### What is Instant Expert?

A service that books paid short calls or written answers from specific executives, operators and domain experts, exposed here as a remote MCP server.

### When am I charged?

Only when the person books the call or sends the written answer. Requests expire after 7 days with nothing charged.

### Can the agent send requests on its own?

No. Drafts are prepared for you and nothing is sent or charged without your explicit approval.

### What does a request include?

Your message, the request type (call or written answer), a per-person offer of at least $5, and a total spending cap across everyone in the list.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [PumpGTM MCP - AI SDR Outreach for Agents](/hermes/mcp/servers/external/pumpgtm-mcp/)
- [Listar MCP - Verified B2B Contact Data](/hermes/mcp/servers/external/listar-mcp/)
