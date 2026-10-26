---
title: "Binderwork MCP - Startup Paperwork and SAFE Rounds"
description: "Share a deck with per-investor tracked links, send NDAs and SAFEs for e-signature, and run a SAFE round with the cap table kept current."
category: Productivity
stars: n/a (new listing)
added: 2026-10-12
source: "chatmcp/mcpso issue #5210 (Oct 12, 2026 evening sweep)"
relevance: ★★
tags: [fundraising, safe, cap-table, e-signature, data-room, documents, startups, remote-mcp]
last_updated: "2026-10-19"
---

# Binderwork MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1)** - paperwork for startups from your chat. Share a deck with a tracked link per investor and see who read which pages and for how long; prepare an NDA, offer letter or SAFE for e-signature; run a SAFE round and keep the cap table. Binderwork never sends anything on its own: the assistant prepares, and everything that emails someone, signs or files waits for your tap or your approval.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 with dynamic client registration; free sign-up by email link, code or passkey
Endpoint: https://app.binderwork.com/mcp
Tools: 42 (deck links and activity, envelopes and e-signature, SAFE rounds, cap table, data rooms, hiring pipeline, approvals)
Pricing: free and open source; self-hostable; hosted service at binderwork.com
Category: Productivity / Fundraising
Built by: Binderwork (binderwork.com, hosted + self-hosted)
Website: binderwork.com/connect
Listing: chatmcp/mcpso issue #5210 (Oct 12, 2026 evening sweep)
```

## Why This Matters for Operators

Fundraising runs on documents and small, high-stakes errands: send the deck, send the SAFE, chase the signature, keep the cap table true. Each errand today means leaving the conversation for a different tool. Binderwork puts the errands behind MCP so the assistant can prepare them from where the work already happens, with an approval gate before anything leaves the building.

The deck side is the part investors notice: a tracked link per investor shows who opened the deck, which pages held attention, and how long - signal that normally arrives as vibes in an update, here it is a per-link activity feed the assistant can summarize. The round side keeps the paperwork disciplined: SAFE preparation, envelopes with reminders and voids, closing milestones, and a cap table the assistant reads and confirms.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| Deck links | link_create, link_update, link_revoke, link_activity: per-investor tracked links and read activity |
| E-signature | envelope_prepare, envelope_send, envelope_list, envelope_get, envelope_remind, envelope_void, document_add, document_list, document_read, document_upload_start: NDAs, offer letters and signature flows |
| Round and cap table | round_create, round_status, round_close, safe_prepare, safe_send, safe_register_confirm, captable_get, captable_prepare, captable_confirm, closing_consent_draft, closing_funding_mark, closing_filing_record: run the round and keep the table current |
| Data room and hiring | dataroom_create, dataroom_get, dataroom_item_add, opening_publish, opening_upsert, application_decide, application_move, candidate_email, offer_prepare, hiring_status, team_prepare |
| Approvals and activity | approval_get, activity_list, workspace_get, investor_upsert, sim_run: the approval queue and the audit trail |

## Installation

Connect from the client's connector flow or add the server directly:

```bash
claude mcp add --transport http binderwork https://app.binderwork.com/mcp
```

The setup guide is at binderwork.com/connect.

## Configuration

```json
{
  "mcpServers": {
    "binderwork": {
      "type": "http",
      "url": "https://app.binderwork.com/mcp"
    }
  }
}
```

## Business Relevance

- **Founders raising a round** can prepare and send SAFEs per investor and watch signing status without a tab-switching ritual.
- **Operators sharing materials** get per-link readership instead of a binary "sent the deck".
- **Small teams without an ops hire** get the paperwork trail - envelopes, approvals, closing milestones - organized by the tool rather than by memory.
- **Self-hosting shops** can run Binderwork themselves; it is free and open source under AGPL-3.0-or-later.

## Integration with CorpusIQ

CorpusIQ answers from the business systems; Binderwork carries the fundraising paperwork. Pair a Stripe or accounting source with it and ask where the round stands against the numbers: the assistant reads revenue and runway from the source of record, then checks the SAFE register and cap table in Binderwork for what has actually been signed. Everything in the write path waits for the operator's approval, so the assistant prepares and reports while the founder keeps the pen.

## Limitations

- New service: sign-up is free and the product is early, so treat critical documents with a review pass. The public repository opens with the first release.
- OAuth plan details evolve; confirm current terms on the vendor's site.
- 42 tools with approval semantics: reads and drafts are free to use, but sends and signatures are gated by design - plan the approval step into any workflow.

## FAQ

### Can the assistant send documents on its own?

No. Binderwork's model is prepare-then-approve: the assistant composes, and anything that emails someone, signs or files waits for your tap or your approval in Binderwork.

### What does deck tracking actually show?

Per-link activity: who opened the deck behind each investor's link, which pages they read and for how long. It is per-investor, so the assistant can summarize where interest is concentrating.

### Is Binderwork free?

Yes, free and open source, with a hosted service for teams that do not want to self-host. Self-hosting is supported under AGPL-3.0-or-later.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
