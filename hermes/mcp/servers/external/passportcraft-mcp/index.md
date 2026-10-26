---
title: "PassportCraft MCP: EU Digital Product Passports"
description: "Hosted MCP connector for drafting EU Digital Product Passports (ESPR) - reads your catalogue, drafts passports for textiles, batteries and general goods, attaches documents and flags missing data. OAuth 2.0 sign-in, no API key, works on every plan including the free one."
category: Compliance
stars: n/a (hosted, no public repo)
added: 2026-08-23
source: "mcpservers.org /all + vendor connector page"
relevance: ★★★
tags: [digital-product-passport, eu-compliance, espr, textiles, batteries, sustainability, remote-mcp]
last_updated: "2026-10-19"
---

# PassportCraft MCP

**Draft EU Digital Product Passports with the AI assistant you already use - the PassportCraft connector reads your catalogue, drafts passports, attaches your documents and tells you what is still missing, with publishing staying your click.** The EU's ESPR regulation is phasing in mandatory Digital Product Passports for textiles, batteries and general goods, and PassportCraft turns the compliance paperwork into an agent-native workflow.

```
Server type: Remote (Streamable HTTP, hosted)
Auth: OAuth 2.0 sign-in (no API key to paste)
Endpoint: https://passportcraft.com/api/mcp
Workspace: one workspace per connection, revocable anytime
Plans: every plan, the free one included
Category: Compliance / EU regulatory
Built by: PassportCraft (passportcraft.com)
```

## Why This Matters for Operators

Digital Product Passports are not a tech-nice-to-have; they are the regulatory paperwork that decides whether a product can be sold in the EU once the ESPR rollout reaches its category. The passport captures material composition, sustainability data, repair and recycling information - and the data has to be accurate and traceable, which is where manual drafting breaks down. PassportCraft's connector keeps the human in the loop at the right point: the agent drafts and assembles, the operator publishes.

The workflow is deliberately scoped for auditability: the connector reads your catalogue, drafts the passport, attaches supporting documents and identifies gaps - it does not publish on its own. That division (AI drafts, human clicks publish) matches how compliance teams actually want to work when the document carries legal weight.

## Tools & Capabilities

PassportCraft does not publish a static tool list; capabilities below come from the vendor's connector documentation (the connector page notes that once connected, asking the assistant "What can I do with PassportCraft?" describes the full live surface):

| Capability | What it does |
|---|---|
| Catalogue reading | Reads your product catalogue as the source of truth |
| Passport drafting | Drafts DPPs for textiles, batteries and general goods |
| Document attachment | Attaches supporting documents to the passport |
| Gap analysis | Tells you what data is still missing before publishing |
| Publishing handoff | Publishing stays a manual click in the workspace |

## Installation

Add a custom connector in Claude (Settings > Connectors > Add custom connector), name it PassportCraft, and paste the URL. Sign in when prompted, choose your workspace, done. The same URL works with ChatGPT, Cursor, Windsurf, GitHub Copilot and any MCP client over HTTP.

```bash
claude mcp add --transport http passportcraft https://passportcraft.com/api/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "passportcraft": {
      "type": "http",
      "url": "https://passportcraft.com/api/mcp"
    }
  }
}
```

OAuth 2.0 sign-in on first connect; no API key to paste. One workspace per connection, revocable anytime from Settings. No account yet? Start free - the connector works on every plan, the free one included.

## Business Relevance

- **EU exporters in textiles, batteries and general goods** get ahead of the ESPR phase-in instead of scrambling at the deadline.
- **Compliance teams** keep a human publish gate while the agent handles drafting, attachment and gap analysis.
- **Product operations** run DPP drafts straight from catalogue data, eliminating re-keying into compliance software.
- **Agencies advising consumer brands** offer passport readiness as a service through the tools their clients already use.
