---
title: SoundGTM MCP - Partner Program Management for Agents
description: AI-native partner relationship management at partnertracker.soundgtm.com/api/mcp - 19 scoped tools for partner pipeline, deals, commissions and outreach with OAuth 2.1 or bearer key auth, free up to 10 partners.
category: Marketing
stars: n/a (new listing)
added: 2026-09-09
source: mcpservers.org
relevance: ★★
tags: [partners, partner-program, affiliate, commissions, prm, gtm, sales-operations, remote-mcp]
---

# SoundGTM MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1)** - partner program management as an MCP server: track partner pipeline, deals and commissions, and manage partner outreach. Ask your AI which partner deals are stalling, who to nudge, and what to pay. Registry name com.soundgtm/partner-tracker, free up to 10 partners.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (scopes read, read_write, openid, email) or bearer API key
Endpoint: https://partnertracker.soundgtm.com/api/mcp
Tools: 19 (pipeline, deals, partners, programs, commissions, outreach - read and read_write scoped)
Pricing: Free up to 10 partners
Category: Marketing
Built by: SoundGTM (soundgtm.com)
```

## Why This Matters for Operators

Partner programs leak revenue through neglect: deals stall, commissions pile up unpaid, and the partners who could move the needle never get the nudge. **SoundGTM MCP puts the partner ledger inside the agent's daily loop** - pipeline summaries, stalled-deal lists and a prioritized do-this-next queue come back in one read, so the agent tells you exactly who to nudge and what to pay before the quarter ends.

Safety is baked into the schema: reads are read-scoped, writes carry read_write scopes, and the money boundary is explicit - authorizing commissions never sends money, and marking a payment records bookkeeping only. Outreach tools draft partner emails as Gmail drafts that are never sent without a human pressing send.

## Tools & Capabilities

All 19 tool names below come from the vendor's published, unauthenticated server card (.well-known/mcp/server-card.json) - exact names with their scopes.

| Tool | Scope | Purpose |
|---|---|---|
| `pipeline_summary` | read | Deal counts by stage, at-risk count, pipeline value, pending commissions, partner health |
| `list_deals` | read | List deals with filters (stage, partner, risk, conversion status) - highest-risk first |
| `list_stalled_deals` | read | Deals with amber or red risk scores |
| `get_deal` | read | Full deal detail: members, recent events |
| `update_deal_stage` | read_write | Move a deal to a new stage |
| `convert_deal` | read_write | Mark converted - creates payout records and notifies the partner |
| `attach_deal_to_partner` | read_write | Attach an unattributed deal to an existing or new partner |
| `list_partners` | read | List partners with filters (status, tag, program, at-risk) |
| `get_partner_detail` | read | Partner's deals, commission terms, health score |
| `invite_partner` | read_write | Send a partner invite email |
| `list_programs` | read | Your partner programs and their settings |
| `get_action_queue` | read | Prioritized do-this-next queue |
| `get_ideal_partner_profile` | read | Your saved Ideal Partner Profile |
| `save_ideal_partner_profile` | read_write | Create or replace the Ideal Partner Profile |
| `list_pending_commissions` | read | All commissions awaiting payment |
| `authorize_commissions` | read_write | Bulk-approve for payment (does not send money) |
| `mark_commission_paid` | read_write | Record a payment made outside SoundGTM (bookkeeping only) |
| `send_announcement` | read_write | Announce to all or selected partners |
| `draft_partner_email` | read_write | Create a Gmail draft to a partner - never sends |

## Installation

```bash
claude mcp add soundgtm --transport http https://partnertracker.soundgtm.com/api/mcp
```

Claude Desktop can authenticate with an API key generated inside SoundGTM; other clients use the OAuth 2.1 flow. The vendor publishes setup walkthroughs at partnertracker.soundgtm.com/docs/mcp.

## Configuration

```json
{
  "mcpServers": {
    "soundgtm": {
      "type": "http",
      "url": "https://partnertracker.soundgtm.com/api/mcp"
    }
  }
}
```

Every connected assistant and API key can be disconnected instantly from inside SoundGTM without affecting the others.

## Business Relevance

- **Founders** see stalled partner deals and commission liabilities before month-end close
- **Partner managers** get a prioritized action queue instead of rebuilding it from a spreadsheet
- **GTM operators** track attribution and convert deals with audit-ready payout records
- **Agencies** run partner programs per client with scoped keys

## Integration with CorpusIQ

SoundGTM MCP pairs with CorpusIQ's revenue connectors as the partner layer: CorpusIQ reads MRR and churn from Stripe while SoundGTM tracks which partners sourced that revenue, so the agent can answer "which partners earned their commission this quarter" with numbers from both sides. It complements the catalogued Ambassly MCP (affiliate program administration) - Ambassly runs affiliate payouts, SoundGTM runs the partner-sourced pipeline in front of them.

## Limitations

- Free tier caps at 10 partners; pricing beyond is on soundgtm.com
- New listing - no independent track record yet
- Partner data lives on SoundGTM's cloud
- Email outreach is draft-only by design - nothing sends without a human
- No self-host option published

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
