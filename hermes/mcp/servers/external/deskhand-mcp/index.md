---
title: "DeskHand MCP - The CRM an Agent Can Be Trusted to Run"
description: "Thirty tools for contacts, deals, drafts and campaigns, behind per-agent keys, an audit log, run-level undo and a dry run."
category: Sales & Outreach
stars: n/a (vendor-hosted; no public repository)
added: 2026-11-07
source: "The mcpservers.org twelve-sitemap addition `sobelendimm-deskhand` in the November 7 evening window; the official MCP registry record `com.grain64.deskhand/deskhand` at 1.2.1 with the remote `https://deskhand.grain64.com/api/mcp`; the vendor site, pricing page and console descriptions at deskhand.grain64.com; and a keyless initialize on the endpoint that answered 200 as deskhand 1.0.0 with 30 tools listed and a policy preamble the server writes for the agent itself"
relevance: ★★★★
tags: [crm, outbound, email-drafts, campaigns, audit-log, undo, per-agent-keys, scopes, approvals, dry-run, remote-mcp]
last_updated: "2026-11-07"
---

# DeskHand MCP

**The usual objection to letting an agent touch a CRM is not that it will write the wrong note. It is that nobody will be able to say afterwards what it did, and nobody will be able to take it back.** DeskHand is built around that objection: the agent works the desk directly, and every write is recorded with a before and an after, grouped into the run that produced it, and reversible one action or one run at a time.

```
Server type: Remote (Streamable HTTP, also a plain HTTP API)
Endpoint:    https://deskhand.grain64.com/api/mcp
Auth:        per-agent bearer key, scopes, paused or revoked individually
Tools:       30
Price:       free during early access, Pro EUR 19 a month
Import:      HubSpot or Attio export, previewed, undoable in one click
```

## What the endpoint says about itself

A keyless `initialize` on `https://deskhand.grain64.com/api/mcp` answers **200** as **deskhand 1.0.0** on protocol `2025-06-18`, and the server writes its own instructions to the model, which are worth quoting because they are the product's governance model in the server's words:

> Deskhand is the system of record for this operator's prospects, with every action audited and undoable. Upsert contacts before you draft to them. Drafts are auto-approved unless the operator turned approval on; read `get_policy` for what applies to you. If `draft_email` returns `contact_suppressed`, stop.

`tools/list` returns **30** tools, all callable without a credential at the list stage, grouped by what they touch:

- **Contacts.** `search_contacts` (by text, status, source, company or custom field), `upsert_contact` (creates, or updates the contact that already holds that email, matched case-insensitively), `update_contact`.
- **Pipeline.** `create_deal`, `move_deal` across `lead`, `contacted`, `qualified`, `proposal`, `won`, `lost`, `add_note`.
- **Tasks.** `create_task` with a due date, `list_due_tasks` returning overdue and due-today first, then the next seven days, with tasks on contacts who replied or unsubscribed suppressed.
- **Email.** `draft_email`, `list_email_status`, `list_replies`, `get_thread`, `mark_replied` (which cancels that contact's pending drafts and follow-ups).
- **Policy.** `get_policy`, the tool the server tells the agent to read first.
- **Campaigns.** `create_campaign`, `update_campaign`, `get_campaign`, `list_campaigns`, `enroll_contacts`, `simulate_campaign`, `launch_campaign`, `pause_campaign`, `resume_campaign`, `stop_enrollment`, `campaign_report`.
- **Sending.** `get_outbox`, `report_send`, `list_sending_identities`.
- **Suppression.** `add_suppression`, `list_suppressions`, applied across every campaign.

## The four controls that make it usable

**A key per agent.** Each agent gets its own key, shown once and stored hashed, with its own scopes (`read_crm`, `write_crm`, `manage_tasks`, `manage_campaigns`) and its own rate limit and daily send cap. One agent can be paused, rotated or revoked without touching the others, and a paused agent's next call is refused with the reason.

**Undo at the run level.** The console groups every call into the run that produced it, with what it created and changed, and offers "Revert this run". A single change can be reverted on its own. That is the difference between an agent that is allowed to work and an agent that is supervised after the fact.

**Approval as a switch, not a rewrite.** Approval can be turned on for email drafts or for every write, for the whole workspace or for a single agent. Drafts then wait in one inbox grouped by run, with inline edit, and a rejection carries a reason the agent can read back.

**A dry-run identity.** `simulate_campaign` returns what would go out over the next N days, per contact and per step: the send time in UTC and local, the fully rendered content, and the counters. `launch_campaign` refuses with `launch_blockers` named (postal address, sender name, an email step, enrolled contacts), and campaigns run under a built-in `dry_run` sending identity until the operator connects their own.

## The workflow the tools encode

The order is enforced by the instruction rather than left to the model: upsert the contact, then read the policy, then draft. Replies stop the chase (`mark_replied` cancels pending drafts and follow-up tasks and refuses new drafts). Suppression is server-side and absolute: replied, unsubscribed and bounced contacts are refused, and a block list stops drafts to domains the operator names. `report_send` records what actually left, and reporting the same message twice is safe, which is the kind of idempotency an agent loop needs.

## Pricing, read off the pricing page

**Free during early access.** Three agents, **1,000** records, **100** agent-written emails a month, **2** campaigns and **250** campaign contacts, with the full set of controls included: one key per agent, undo per action or per run, complete audit log.

**Pro at EUR 19 a month.** Five agents, **10,000** records, **1,000** agent-written emails a month, **10** campaigns and **5,000** campaign contacts, longer audit history, and an email digest. A workspace and a key can be created with one click and no sign-up, then claimed with an email.

## Limits worth writing down

- **Sending runs through identities the operator connects.** The built-in identity is a dry run, so a campaign does not reach a real inbox until the operator adds their own sender. That is a safety property and also a setup step people will miss.
- **Early access pricing is a promise, not a contract.** Free today with published limits, so treat the Pro list as the likely shape rather than a settled one.
- **The email side is a drafting and approval desk, not a full sequencer.** It is closer to a CRM with an outbound gate than to a cold-email platform with deliverability tooling; the catalog's [Warmerly entry](/hermes/mcp/servers/external/warmerly-mcp) covers mailbox health and DNS, and this one does not.
- **No public repository**, so the audit guarantees are a vendor claim read from the console's description rather than something that can be checked in code.
- **The keyless read is limited to `initialize` and `tools/list`.** Nothing was written during this pass: no workspace was created and no contact was inserted, because creating records against a live vendor workspace is not a read.

## Where it sits beside the CRM entries

The catalog carries CRM connectors (HubSpot, Attio, Pipedrive and the agency-side desks) and it carries outbound platforms. The gap this fills is the one that matters when an agent, not a person, is the operator: per-agent identity, an append-only log, run-level reversal, and a policy tool the model is told to read before it writes. An operator who would not hand a shared CRM key to a script can hand a scoped key to an agent here and still see, per run, what it did.

## Frequently asked questions

### What does DeskHand MCP cost?

**Free during early access**: three agents, 1,000 records, 100 agent-written emails a month, two campaigns and 250 campaign contacts. **Pro is EUR 19** a month for five agents, 10,000 records, 1,000 emails a month, ten campaigns and 5,000 campaign contacts.

### Can an agent send email on its own?

It can draft. Sending runs through a sending identity the operator connects, and until then campaigns use the built-in `dry_run` identity, so `simulate_campaign` shows what would go out while nothing reaches a real inbox.

### How do you undo what an agent did?

Every call is grouped into the run that produced it, and the console offers "Revert this run" as well as reverting a single change, with an append-only audit log recording who changed what, on which record, before and after.

### Does one agent share a key with the others?

No. Each agent gets its own key, shown once and stored hashed, with its own scopes, rate limit and daily send cap, and can be paused, rotated or revoked without touching another agent.
