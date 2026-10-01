---
title: "Common Paper Contracts MCP - Agreement Workflow for Agents"
description: "Find, draft, send, negotiate and void NDAs, DPAs and service agreements from standard templates, with read tools free-running and every send gated on approval."
category: Legal & Contracts
stars: n/a (hosted platform, commonpaper.com)
added: 2026-09-30
source: "mcp.so server page (common-paper-contracts)"
relevance: ★★★
tags: [contracts, legal, agreements, e-signature, nda, dpa, document-automation, oauth, remote-mcp]
---

# Common Paper Contracts MCP

**Agreement workflow for revenue and legal teams, driven from the conversation.** Common Paper is a contract platform for startups and growing businesses: create agreements from standard templates, send them for e-signature, negotiate changes with recipients and track everything in one place. The MCP server lets an assistant ask what is waiting for signature, look up a counterparty's terms, compare payment schedules across active contracts, or draft and send a new NDA from a standard template without leaving the chat.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (no API key needed)
Endpoint: https://api.commonpaper.com/mcp
Tools: read tools (find, status, history, download) plus gated create/send/void actions and template management
Pricing: requires a Common Paper account
Category: Legal & Contracts
Built by: commonpaper.com
```

## Why This Matters for Operators

Contract admin is a stop-and-search workflow: a deal stalls, someone asks for the DPA, and the person with the account has to stop what they are doing, find the template, fill the cover page and send it. Common Paper's MCP server moves the lookup and the drafting into the agent session, so "send Acme our standard mutual NDA" or "is the Acme MSA signed yet" is answered from live contract state rather than a folder of PDFs.

The safety split is the part worth noting: read tools run without interrupting the conversation, while anything that creates, sends or voids an agreement always asks the operator first. That is the right default for a surface that produces legally binding documents.

## Tools & Capabilities

| Area | What it does |
|---|---|
| Find agreements | Look up agreements by type, status, created date or recipient |
| Check status | Whether an agreement has been viewed or signed, plus its full history |
| Create and send | NDAs, Cloud Service Agreements, DPAs, BAAs, Professional Services Agreements and more from standard or custom templates |
| Edit drafts | Change the recipient, message, CC users or Cover Page terms before sending |
| Manage sent | Resend, reassign or void an agreement, or generate a shareable signing link |
| Download | Pull a copy of any agreement |
| Templates | Create, list and update templates, custom templates and custom terms |

Supported agreement types include NDAs, Cloud Service Agreements, DPAs, BAAs, Professional Services Agreements, Letters of Intent, Pilot Agreements, Software Licenses and Design Partner Agreements.

## Installation

```bash
claude mcp add common-paper-contracts --transport http https://api.commonpaper.com/mcp
```

Authentication is handled through OAuth against your Common Paper account, so no API key is issued or stored.

## Configuration

```json
{
  "mcpServers": {
    "common-paper-contracts": {
      "type": "http",
      "url": "https://api.commonpaper.com/mcp"
    }
  }
}
```

## Business Relevance

- **Revenue teams** check signature status and counterparty terms mid-deal without leaving the CRM conversation
- **Legal and ops** send standard NDAs and DPAs from a template rather than retyping them
- **Finance** compares payment schedules across active contracts for a cash-flow view
- **Founders** turn a stalled contract step into a two-line instruction to the agent

## Integration with CorpusIQ

Contract state sits next to the money. A composed workflow: Common Paper answers whether the Acme MSA is signed, and CorpusIQ supplies the Stripe revenue, HubSpot deal stage or GA4 traffic numbers that surround it, so the same session can reconcile signed contracts against booked revenue. For operators running both, the signed-agreement question and the revenue question no longer need two tools and two logins.

## Limitations

- Requires a Common Paper account; the server is not usable anonymously
- The directory listing showed no fetchable tool list at catalog time, so action names are described by capability rather than exact tool identifiers
- Write actions are gated on approval by design, which adds a confirmation step for bulk sends
- OAuth means the server grants access to the whole account scope the connection was approved for

## FAQ

### Does the server ever send an agreement without asking?

No. Read tools run silently, but anything that creates, sends or voids an agreement asks for confirmation first.

### Do I need an API key?

No. Authentication is OAuth-based against your Common Paper account.

### Which agreement types are supported?

Any standard Common Paper template, including NDAs, CSAs, DPAs, BAAs, PSAs, LOIs, Pilot Agreements, Software Licenses and Design Partner Agreements.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [SignSimple MCP - E-Signature Workflow over MCP](/hermes/mcp/servers/external/signsimple-mcp/)
- [Legalize MCP - Legal Document Intelligence for Agents](/hermes/mcp/servers/external/legalize-mcp/)
- [DocuSign alternatives in the external catalog](/hermes/mcp/servers/external/)
