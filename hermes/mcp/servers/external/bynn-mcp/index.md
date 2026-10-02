---
title: Bynn MCP - KYC and Document Fraud Detection for Agents
description: Hosted MCP for identity verification, document fraud detection and content moderation. 143 tools over the Bynn API cover KYC session creation, forensic analysis of bank statements and invoices, age verification with liveness, face search against employee collections, AI-image detection and fraud reasoning agents. OAuth sign-in or bearer token.
category: Compliance
stars: n/a (new listing)
added: 2026-09-06
source: mcpservers.org
relevance: ★★★
tags: [kyc, fraud-detection, identity-verification, content-moderation, age-verification, compliance, autodoc, remote-mcp]
---

# Bynn MCP - KYC and Document Fraud Detection for Agents

**Remote MCP server (Streamable HTTP, OAuth or bearer token)** - a hosted compliance layer from Bynn (bynn.com) that puts identity verification, document fraud detection, age verification, content moderation, face search and account management in front of an AI agent: 143 tools over the Bynn API behind one connection. Fraud reports and AI-image checks render as interactive cards in Claude and ChatGPT, and the product ships as a native ChatGPT app.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth browser sign-in, or bearer token minted at dashboard.bynn.com/authenticate
Endpoint: https://mcp.bynn.com
Tools: 143 (KYC, document fraud, age verification, moderation, face search, AutoDoc workflows, account management)
Pricing: Usage-based billing visible in the Bynn dashboard (invoices and monthly usage exposed as tools)
Category: Compliance
Built by: Bynn (bynn.com)
```

## Why This Matters for Operators

Manual document review is where onboarding funnels stall and fraud slips through. A KYC analyst opens each bank statement or invoice in a viewer, checks watermarks and metadata by eye, and takes notes in a second system. Bynn lets the agent do the first pass natively: submit a document for fraud analysis and get back forensic findings, an AI-probability verdict on images with the likely generator, and a hosted KYC verification session link for the applicant in the same chat.

**The critical design point is that the agent never handles a raw key: hosted clients sign in with a Bynn account and the browser handles OAuth; API-style clients get a token from the Bynn dashboard that the operator can rotate with a grace period.** Everything else - KYC sessions, age verification with liveness, face search against your own employee collection, moderation model selection - runs through the same 143-tool surface, with interactive result cards instead of raw JSON dumps.

For operators, this means compliance checks stop being a queue of tickets and become a chat conversation the agent can run while the analyst reviews the verdicts.

## Tools & Capabilities

| Group | What the agent does |
|---|---|
| Document fraud | Submits bank statements and invoices for forensic analysis; answers whether a document is manipulated; runs passport-fraud orchestrators against analyzed documents |
| KYC verification | Creates KYC verification sessions and hands back hosted links; estimates age from photos with under-25 checks; creates age verification sessions with liveness |
| Moderation and media | Checks whether an image is AI-generated (verdict plus probability and likely generator); lists moderation models available for video; searches faces against an employee collection |
| AutoDoc workflows | Runs end-to-end document workflows beyond single checks |
| Account operations | Lists API keys with last-use timestamps; rotates live private keys while keeping a grace period; reads monthly usage and latest invoices |

## Installation

```bash
claude mcp add --transport http bynn https://mcp.bynn.com
```

The endpoint is the root path: do not append `/mcp`. Claude Desktop and claude.ai connect via Settings, Connectors, Add custom connector with the URL above; ChatGPT connects as an app; Cursor has a one-click install link; VS Code and Windsurf configs are published in the vendor docs (docs.bynn.com, with an llms.txt index for agents).

## Configuration

```json
{
  "mcpServers": {
    "bynn": {
      "type": "http",
      "url": "https://mcp.bynn.com"
    }
  }
}
```

On first use the browser opens for Bynn OAuth sign-in. API-style clients instead mint a token at dashboard.bynn.com/authenticate and send it as a bearer header on the connection.

## Business Relevance

- **Fintech and marketplace compliance teams** get KYC session creation and document fraud analysis without context-switching out of the chat that is triaging applicants.
- **Trust and safety teams** run AI-image detection, moderation model selection and face search against internal collections from one agent surface.
- **Finance and legal operators** keep a forensic trail: fraud findings summarized per document with the evidence the agent read.
- **Agencies running client onboarding** spin up hosted verification sessions on demand instead of licensing a separate KYC portal per client.

## Integration with CorpusIQ

Bynn reads documents and identities; CorpusIQ reads business systems. A composed compliance workflow: the agent pulls a transaction's counterparty and amounts from CorpusIQ's QuickBooks or Stripe connectors, then submits the associated bank statement to Bynn for fraud analysis in the same session - payment evidence and document forensics in one review thread. For onboarding, CorpusIQ's CRM connectors supply the applicant record while Bynn handles the KYC session and age or identity verification, with the verdict written back into the customer timeline. Both tools are read-first by design, which is what a compliance workflow needs: evidence assembled, human approves.

## Limitations

- Brand new to this catalog (mcpservers.org listing, no public repo or star history to assess).
- Commercial cloud service - no self-hosting; all documents flow through Bynn's platform.
- Usage-based pricing: cost depends on verification and analysis volume.
- Endpoint is the root path only; the common `/mcp` suffix returns nothing.
- Tool names are not published in full vendor docs; the live tool list is served from the endpoint after sign-in.

## See Also

- [Strac MCP DLP - Sensitive Data Redaction for AI Agents](/hermes/mcp/servers/external/strac-mcp-dlp)
- [Nizh MCP - Compliance Frameworks for AI Agents](/hermes/mcp/servers/external/nizh-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
