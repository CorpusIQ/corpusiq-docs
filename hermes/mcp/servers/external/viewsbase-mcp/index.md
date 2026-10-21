---
title: "ViewsBase MCP - Creator Payouts for Clipping Campaigns"
description: "ViewsBase turns campaign view counts into what each creator is owed, flags who cannot be paid yet and records the payments that went out."
category: Marketing
stars: n/a (hosted, no public repo)
added: 2026-10-21
source: "chatmcp/mcpso submission issue #5881 (funCapital)"
relevance: ★★★
tags: [creator-marketing, ugc, clipping, payouts, cpm, campaign-ops, affiliate, remote-mcp]
---

# ViewsBase MCP

**A clipping or UGC campaign produces two numbers nobody joins up: how many views each post got, and how much each creator is owed against the deal they agreed. ViewsBase joins them, and the assistant can read the result.**

```
Server type: Remote (Streamable HTTP) at https://viewsbase.com/mcp
Auth: OAuth 2.1, workspace-scoped, read-only by default
Live check: POST initialize returned HTTP 401 Unauthorized without a session
Tools: 29, split read and write, money tools gated on payment rights
Requirements: AI and API access ship with the Growth plan and up
Vendor: ViewsBase (viewsbase.com), official registry io.github.funCapital/viewsbase
```

## Why This Matters for Operators

Paying creators for a campaign is a reconciliation problem, not a marketing problem. Views arrive in one place, the offer that was agreed lives in another, payout methods live in a third, and the period and caps that decide whether a post even qualifies are usually in a screenshot. Any brand running more than a handful of creators per month ends up with a spreadsheet that is always one week stale and a payments run that is always disputed.

The failure modes are structural. A creator has no payout method on file, so the amount is owed but cannot be sent. A post is still inside its counting window, so finalising it early locks in a number that will grow. A views spike puts a post in review, and paying it early pays for traffic that did not happen. Each is a rule, and rules are exactly what an assistant can check if the data is exposed.

## What It Actually Does

Read tools cover the campaign: `list_workspaces` shows what the connection can see with the caller's role per workspace, `list_campaigns` opens the campaigns, `list_posts`, `get_post` and `get_post_views` return posts and their counted views, `list_creators` and `get_creator` describe the people, `get_payouts_summary` splits money into owed and final, ready to pay, owed but blocked, payout details to check, held for a views spike, and counting, and `list_payment_requests`, `get_payment_request`, `list_payable_creators` and `list_payment_history` cover what is open, what can be paid now and what went out.

Operational read tools are the ones that make it a working surface rather than a dashboard mirror: `get_needs_you` returns the Overview list of what is waiting on the operator, `list_activity` returns the activity log as plain sentences filtered by campaign, type or creator, `list_applications` returns creator applications with file answers reported as attached rather than inlined, and `migration_checklist` reports what a workspace still has to fix.

Write tools change campaign terms: `set_post_cpm`, `finalize_post`, `refresh_post`, `add_creator`, `set_creator_offer`, `set_creator_link`, `pause_creator` and `resume_creator`. Finalising closes the view window, which is a money decision, so the vendor's guidance is explicit: read the exact record, show the proposed change and its payment effect, get approval, then read it back.

Scoping is the design worth reading. A connection picks one or more workspaces and an access level, read-only is the default, and the caller's current workspace, agency and campaign access applies to every tool call. The money tools require payment rights and never return payout details, emails or full account numbers.

## Installation

```bash
claude mcp add --transport http viewsbase https://viewsbase.com/mcp
```

Then run `/mcp` and sign in to ViewsBase. In ChatGPT the same URL is added as a custom MCP server with Authentication set to OAuth. Cursor and VS Code install from the AI connections page at viewsbase.com/mcp/connections. Connections are revoked from that page and each one lists the workspaces it holds.

## Limits Worth Knowing

Each connection allows 120 MCP requests and 30 write calls per minute, shared across server instances. If a used refresh token is sent twice the connection is revoked, and the client must send one refresh request at a time. A workspace on Starter cannot connect an app at all, so connections stop on the next call after a downgrade.

## FAQ

### Does the assistant move money?

No. It reads what is owed, who can be paid and what went out, and it can change offers, links and post status. Marking a payment paid stays in the dashboard, and the money tools only return amounts and status.

### What happens to a post that is still counting?

`get_payouts_summary` reports it under counting, and `finalize_post` closes the view window, which is why the vendor asks for a read, an approval and a read-back around that call.

### Can a viewer see the payout totals?

No. The money tools need campaign editor, campaign admin or workspace admin rights, and a viewer gets a 403.

## See Also

- [Marketing servers](/hermes/mcp/servers/external/) in this catalog
- [CorpusIQ connectors](/docs/hermes/mcp/servers/) for read-only business data in the same questions
