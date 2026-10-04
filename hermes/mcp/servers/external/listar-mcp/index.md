---
title: Listar MCP - Verified B2B Contact Data
description: Remote MCP that finds a company's decision makers, verified work emails and phone numbers inside an assistant, with nothing billed when nothing is found.
category: Marketing
stars: n/a (new listing)
added: 2026-10-04
source: mcpservers.org
relevance: ★★★
tags: [marketing, sales, lead-generation, contact-data, enrichment, prospecting, remote-mcp, oauth]
---

# Listar MCP

**Remote MCP server (Streamable HTTP, account auth)** - Listar brings verified B2B contact data into an MCP client. Ask an assistant to find a company's manager, their email and their phone number, and Listar does the research so the assistant can put it to work in prospecting. The tools work in plain language, in a live chat as well as in a scheduled task that runs on its own.

```
Server type: Remote (Streamable HTTP)
Auth: Listar account (free credit on sign-up)
Endpoint: https://api.listar.fr/mcp
Tools: Find decision makers, enrich contacts, verify emails, flag phones, meet prep
Pricing: Free credit on sign-up; same prices as the Listar API
Category: Marketing
Built by: Listar
```

## Why This Matters for Operators

Prospecting stalls between "which company" and "who do I actually reach and how." Listar's mechanism is to **resolve the person and the verified contact details from the company**, pulling legal directors from the official register, surfacing the manager's phone and email, and flagging whether each phone is professional or personal. Nothing is billed when nothing is found, so failed lookups cost nothing.

For sales and GTM operators, that means a list of targets becomes a list of reachable people in one step, and enrichment can run as a nightly scheduled task that continuously adds decision makers. Data land cost is bounded by the find-only billing.

**The key advantage is company-to-verified-contact resolution with find-only billing, driven from a chat.**

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| Find decision makers | Surfaces the manager and legal representatives for a company |
| Enrich contacts | Adds verified work emails and phone numbers to a list one by one |
| Verify email | Confirms a work email address |
| Flag phone type | Marks a number as professional or personal |
| Meet prep | Reports who runs an account, who to contact and how to reach them |

Exports flow to CSV or Google Sheets through other connectors.

## Installation

```bash
claude mcp add --transport http listar https://api.listar.fr/mcp
```

Setup is a custom connector paste in Claude: Settings, Connectors, Add custom connector.

## Configuration

```json
{
  "mcpServers": {
    "listar": {
      "type": "http",
      "url": "https://api.listar.fr/mcp"
    }
  }
}
```

Sign in with a Listar account; a free credit is available on sign-up, and pricing matches the Listar API.

## Business Relevance

- **Sales teams** can turn a company list into reachable decision makers in one prompt.
- **SDRs and founders** can enrich a pasted list of contacts or companies with verified details.
- **Account managers** can prepare for a call by asking who runs the account and how to reach them.
- **RevOps** can schedule nightly prospecting that keeps the contact database current.
- **Agencies** can enrich client prospect lists with professional-vs-personal phone flags.

## Integration with CorpusIQ

Listar supplies the contact layer for CorpusIQ's pipeline. Where CorpusIQ's lead pipeline and analytics track who is in the funnel, Listar fills the missing person details, so an assistant can go from "these companies fit the ICP" to "here are the named decision makers and verified contacts."

A composed workflow: pull a target segment from CorpusIQ's lead pipeline, have Listar enrich it with decision makers and verified emails, then route the enriched list into an outreach server. CorpusIQ ranks the opportunity; Listar names the human behind it.

## Limitations

- Requires a Listar account; contact lookups consume credits.
- Data coverage is strongest for the regions Listar supports; verify before large campaigns.
- Hosted and proprietary; no self-hosting.
- Contact data should be used within applicable privacy and marketing law.
- Enrichment is look-up based, so it will not invent a contact that does not exist.

## FAQ

### Is anything billed when no contact is found?

No. Listar does not bill for lookups that return nothing.

### What can Listar find for a company?

Decision makers, verified work emails and phone numbers, with phones flagged professional or personal.

### Can Listar run on a schedule?

Yes. It works inside scheduled tasks, so it can add new decision makers daily.

### Does Listar export data?

Yes, via CSV or Google Sheets through your other connectors.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
