---
title: "HeyLead MCP - LinkedIn Outreach That Sends from Your Account"
description: "HeyLead is an AI agent for LinkedIn outreach: it finds the right people, writes in your voice, follows up and handles replies."
category: Marketing
stars: n/a (new listing)
added: 2026-09-29
source: "mcp.so server page (heylead.dev)"
relevance: ★★★
tags: [linkedin, outreach, lead-generation, sales, recruiting, oauth, remote-mcp]
---

# HeyLead MCP

**LinkedIn outreach that runs from your own account.** HeyLead is an AI agent for LinkedIn prospecting: it finds the right people, writes messages in the voice of your own LinkedIn posts, follows up on a schedule and handles replies, from Claude Code, Cursor, any MCP client or a web dashboard.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth browser sign-in, no API key
Endpoint: https://heylead.dev/mcp
Tools: persona building, lead search, campaign messages, follow-ups, inbox replies
Pricing: Free (1 seat, cloud sending) - Pro $29 per connected LinkedIn account per month
Category: Marketing
Built by: Denys Chumak (github.com/D4umak/linkedin-outreach-mcp, MIT client)
```

## Why This Matters for Operators

Outbound LinkedIn is where most B2B pipeline starts, and the failure point is almost never the list - it is the sustained follow-up. HeyLead runs the whole motion from one OAuth sign-in: it builds two to four buyer personas from a single sentence, previews the LinkedIn search before anything exists, then drafts a warm-up, invitation note, opening message, follow-ups and an InMail or email fallback for each specific person.

Every opening message and follow-up waits for approval until you switch a campaign to autopilot, so nothing goes out that you have not seen. Replies are read and answered from the campaign's facts, and anything ambiguous is held for you. Sends go out from your own LinkedIn account at a human pace - at most 20 invitations a day and 100 a week on a free account, Monday to Friday 08:00 to 22:00 in your time zone - which is exactly the cadence that keeps accounts healthy.

## Tools & Capabilities

| Capability | Purpose |
|---|---|
| Persona builder | Two to four buyer personas from one sentence, with the LinkedIn search previewed before anything is created |
| Campaign messages | Warm-up, invitation note, opening message, follow-ups, InMail and email fallback written per person |
| Approval gate | Opening messages and follow-ups wait for your approval until autopilot is switched on |
| Reply handling | Replies read and answered from campaign facts; ambiguous threads held for manual review |
| Campaign goals | Six modes: sell, find a job, hire, find partners or investors, find a vendor, research interviews |
| Sending controls | Human-pace limits from your own account, Monday to Friday in your local time zone |

Tool names are served from the endpoint; the vendor publishes a tool reference at heylead.dev/docs/tools.

## Installation

```bash
claude mcp add heylead --transport http https://heylead.dev/mcp
```

Connect through the OAuth browser sign-in - no API key. A setup guide for chat clients is published at heylead.dev/llms.txt.

## Configuration

```json
{
  "mcpServers": {
    "heylead": {
      "url": "https://heylead.dev/mcp"
    }
  }
}
```

## Business Relevance

- **Founders doing their own outbound** replace manual drip sequences with an assistant that writes and sends in their voice
- **SDRs and recruiters** run multiple campaigns with per-person messaging instead of templated blasts
- **Agencies** manage outreach across client accounts with approval gates on every send
- **Job seekers and fundraisers** use the hire, investor and partner campaign goals without learning a new tool

## Integration with CorpusIQ

HeyLead covers the outbound motion while CorpusIQ covers the business-data layer. An assistant can qualify a lead against live Stripe revenue, QuickBooks invoices or CRM deals through CorpusIQ connectors, then hand the approved shortlist to HeyLead for personalized outreach - and every send stays inside the human-pace limits that keep the account safe.

## Limitations

- Brand new listing, no track record yet
- Sends through Unipile's LinkedIn connection layer, which LinkedIn does not affiliate with
- Free tier is one seat; each additional connected LinkedIn account is a Pro seat
- No public tool catalog beyond the vendor's docs pages

## FAQ

### Does it send from my own LinkedIn account?

Yes. Campaigns send from your own connected LinkedIn account through Unipile, at human-pace limits (at most 20 invitations a day and 100 a week on a free account, Monday to Friday 08:00 to 22:00 local time).

### Can messages go out without my approval?

Opening messages and follow-ups wait for your approval until you explicitly switch a campaign to autopilot. Replies are answered from campaign facts, and ambiguous threads are held for you.

### What does it cost?

Free at $0 for one LinkedIn seat with cloud sending included. Pro is $29 per connected LinkedIn account per month.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
