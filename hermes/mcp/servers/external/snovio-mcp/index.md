---
title: "Snov.io MCP - B2B Sales and Outreach for Agents"
description: "Find leads, verify emails, run email campaigns and answer replies in Unibox from one MCP connection to an existing Snov.io sales account."
category: Marketing & Sales
stars: n/a (new listing)
added: 2026-10-06
source: "mcpservers.org /all (Oct 6, 2026 midday sweep)"
relevance: ★★★
tags: [lead-generation, email-verification, cold-email, linkedin, unibox, crm, outreach]
---

# Snov.io MCP

**Remote MCP server (Streamable HTTP, account sign-in)** - Snov.io connects to Claude, ChatGPT or any MCP client and lets an operator run the whole outreach loop from prompts: find leads, verify email addresses, work with the CRM, run LinkedIn outreach, create and launch email campaigns, and reply to conversations in Unibox.

```
Server type: Remote (Streamable HTTP)
Auth: Snov.io account sign-in (OAuth) - requires an active Sales Suite or LinkedIn Automation plan
Endpoint: https://mcp.snov.io/mcp
Tools: Lead Finder, Email Verifier, Leads & Data, Campaigns, Unibox
Pricing: Included with an eligible Snov.io plan
Built by: Snov.io
Registry: via app.snov.io
```

## Why This Matters for Operators

Cold outreach tooling usually means dashboard work: search a database, export a CSV, verify a list somewhere else, upload it into a sequencer, then live in the inbox. Snov.io's MCP server puts the whole pipeline behind one conversation - and its two tool types keep the discipline honest. View-only tools look data up and change nothing; take-action tools create, send or update, and are designed to be confirmed before they run.

Because it works against an existing Snov.io account, everything here is first-party: your lists, your campaigns, your domain health, your Unibox. The agent reads and acts as you, inside the limits of your plan.

## Tools & Capabilities

| Area | What the agent can do |
|---|---|
| Lead Finder | Search prospects and companies, find emails by name and company, run LinkedIn searches by filters or saved search URL |
| Email Verifier | Verify one email or a whole batch, track bulk status, review results by status, save valid emails to a list |
| Leads and Data | Create lists and folders, add and update prospects and companies, segment, export when ready |
| Campaigns | Connect sender accounts, check domain health, build sequences, add content and recipients, pull stats and reports |
| Unibox | Read and reply to prospect conversations |

## Installation

```bash
claude mcp add --transport http snovio https://mcp.snov.io/mcp
```

Then sign in with your Snov.io account when prompted. The same URL works in ChatGPT and other MCP clients.

## Configuration

```json
{
  "mcpServers": {
    "snovio": {
      "url": "https://mcp.snov.io/mcp"
    }
  }
}
```

## Business Relevance

- **Founders doing their own outbound** run one loop - find, verify, load, launch, reply - without leaving the chat.
- **Sales teams** draft ICP searches and report campaign stats in the conversation they already use for planning.
- **Agencies** build client prospect lists with verification attached, then launch and monitor sequences.
- **Operators** keep sends confirm-gated: take-action tools can be reviewed before they touch a live campaign.

## Integration with CorpusIQ

CorpusIQ reads the operator's business data read-only - revenue, ads, analytics, support. Snov.io covers the outbound edge: who the business reaches, whether the emails land, and what the replies say. A pipeline question can now span both: what the funnel converted (CorpusIQ side) next to what the outreach sent and who replied (Snov.io side).

## Limitations

- Requires an active Snov.io account on a Sales Suite or LinkedIn Automation plan.
- The MCP server acts within your existing plan limits and credits - it does not add capacity.
- Sends are real: take-action tools should be confirmed before they run.
- New listing: no track record in this catalog yet.

## FAQ

### Which account do I need?

Any active Snov.io account on a Sales Suite or LinkedIn Automation plan. The MCP server URL is `https://mcp.snov.io/mcp`.

### Can the agent send emails on its own?

It can call send-type tools, but each tool is classified: view-only tools change nothing, and take-action tools - creates, sends, updates - are meant to be confirmed before they run.

### Does it work with my existing campaigns and lists?

Yes. It operates on your account, so lists, campaigns, senders and Unibox threads are the ones you already have.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Listar MCP - Verified B2B Contact Data](/hermes/mcp/servers/external/listar-mcp/)
- [PumpGTM MCP - AI SDR Outreach for Agents](/hermes/mcp/servers/external/pumpgtm-mcp/)
