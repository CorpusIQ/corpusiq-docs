---
title: "ClosedLoop AI MCP - Customer Evidence, Ranked"
description: "Product insights built from sales calls, support tickets, surveys and Slack."
category: Data & Analytics
stars: n/a (vendor-hosted; mcp.so card verified and featured)
added: 2026-10-23
source: "mcp.so /feed page 1 card (posted 2026-10-23T13:23:40Z, submitted by Jiri Kobelka, verified and featured) plus the vendor MCP documentation"
relevance: ★★★
tags: [customer-feedback, product-intelligence, voice-of-customer, revenue-at-risk, churn, roadmap, sales-calls, support-tickets, remote-mcp, oauth]
last_updated: "2026-10-24"
---

# ClosedLoop AI MCP

**Every company already owns the answer to what to build next. It is scattered across call recordings, support threads and surveys, and nobody has time to read it before the roadmap meeting. This puts that evidence behind a question an assistant can ask.**

```
Server type: Remote (Streamable HTTP), US at https://mcp.closedloop.sh, EU at https://eu.mcp.closedloop.sh
Auth: OAuth 2.1 with dynamic client registration, PKCE S256, private_key_jwt supported (RS256 and ES256) for machine clients; scopes mcp:tools and mcp:read
Live check: POST initialize without a token returned HTTP 401 {"jsonrpc":"2.0","error":{"code":-32000,"message":"Authorization required"}} with www-authenticate naming resource_metadata="https://mcp.closedloop.sh/.well-known/oauth-protected-resource"
Discovery: that path returns 200 with resource https://mcp.closedloop.sh and authorization server https://mcp.closedloop.sh; /.well-known/oauth-authorization-server returns authorize, token and register endpoints, code, refresh and client_credentials grants
Tools: 14 documented read tools plus 4 write tools, in the vendor reference
Pricing: volume-based on customer feedback volume, quoted on contact; unlimited team members and MCP access included
Vendor: ClosedLoop AI (closedloop.sh)
```

## Why This Matters for Operators

The gap between what customers say and what the roadmap does is not a listening problem. Companies listen constantly. Calls are recorded, tickets are logged, surveys are collected, and the reason none of it changes a decision is that the evidence arrives as thousands of separate events with no shared language and no revenue attached. Someone has to read it, group it, and then defend the grouping.

Product analytics tools answer what users did. This answers what they said, and the difference matters most for the questions analytics cannot see: which missing feature is costing a renewal, which competitor is being named in churn conversations, and which complaint appears in twelve accounts that together pay six figures.

The distinction worth naming for this catalog: Feedier covers surveys and NPS, ParrotNotes and Granola cover meeting transcripts, and the Customer Intelligence and Segmentation entry covers customer tiering. None of them synthesizes across calls, tickets, surveys and CRM notes into ranked product themes with the original quote attached. That synthesis is the entry.

## What It Actually Does

The vendor publishes a full tool reference, and the shape is unusual for this catalog: almost everything reads.

Overview and discovery: `get_overview` returns total insights, deal blockers, churn risks and top categories for a window of 7, 30 or 90 days or all time, and is documented as the starting point. `get_facets` returns aggregated counts by dimension, and `get_trends` returns the time series.

Customer intelligence: `search_customers` and `get_customer`, where a customer profile carries the deals and revenue context behind the account.

Product intelligence: `search_insights` searches insights by keyword or meaning, and `get_insight` returns one insight with its evidence.

Conversation evidence: `list_conversations` and `get_conversation`, which is the path back to what was actually said.

Sales intelligence: `search_signals`, `get_signal`, `get_competitors`, `search_opportunities` and `get_opportunity` for satisfaction, churn risk, competitor mentions and buying behavior.

The four write tools are deliberately small: `send_closedloop_feedback`, `create_watch` (a watch that notifies Slack, Teams, email or a webhook when it fires), and two tools that log and update a test permission request without ever emailing a customer. There is no tool that changes a customer record or sends anything to a customer.

One structural detail deserves attention: the vendor's own example of the pipeline starts with three different customers saying the same thing in three different channels and ends with one product insight, a source quote for each, and a roadmap candidate a person decides on. The tool does the grouping, the person keeps the decision.

## Installation

```bash
claude mcp add --transport http closedloop --url https://mcp.closedloop.sh
```

For Hermes:

```bash
hermes mcp add closedloop --url https://mcp.closedloop.sh
hermes mcp auth closedloop
```

The vendor's own path for chat clients is a custom connector: name it, paste the regional URL, and leave the advanced client settings empty because the server registers the client itself.

## Configuration

```json
{
  "mcpServers": {
    "closedloop": {
      "type": "http",
      "url": "https://mcp.closedloop.sh"
    }
  }
}
```

EU workspaces use `https://eu.mcp.closedloop.sh`. Headless clients that cannot do an interactive browser sign-in have two documented options: a registered RSA or P-256 public key for `private_key_jwt`, or an OAuth client ID and shared secret, which the vendor names for LiteLLM specifically.

## What It Costs

Pricing scales with how much customer feedback the workspace processes, and higher volumes qualify for lower rates. Team members are unlimited, and MCP access is included rather than sold as a tier. There is no public price list: the vendor routes pricing to a contact form, and the plans named in the setup documentation (Free, Pro, Max, Team, Enterprise) are the Claude plans that can host a custom connector, not ClosedLoop's own tiers.

For an operator that means the cost question is answerable only against a real feedback volume, and it should be asked before a rollout rather than after.

## Integration with CorpusIQ

The natural pairing is evidence against results. CorpusIQ already answers what the business recorded: revenue from the accounting connector, support volume from the helpdesk, pipeline from the CRM, usage from the product analytics connector. This adds what customers said about it, with the account and the revenue attached, which is the missing half of any churn question.

A sequence that fits: pull the accounts with revenue at risk from this server, then ask CorpusIQ's own connectors what those accounts actually did last quarter, and compare the two. The disagreement between what a customer said and what the account did is the decision.

The read-only default is also a governance fit for the product's thesis. An evidence layer an assistant can read and cite, with every write gated behind a person, is the shape CorpusIQ argues for generally.

## Limitations

- **No tool call was made in this entry.** Every tool needs an OAuth connection to a ClosedLoop workspace with connected sources, and this sweep does not create accounts. Liveness rests on the live 401, the protected-resource document, the authorization-server metadata and the vendor tool reference.
- **It only knows what you connect.** The evidence comes from Gong-style call recordings, Zendesk and Intercom tickets, Slack threads, CRM notes and surveys. A source that is not integrated is invisible, and a company whose customer truth lives in email only gets a partial picture.
- **Pricing is not public and is volume-based.** No plan, price or credit model is published, so cost cannot be evaluated without a sales conversation.
- **It groups, it does not decide.** The vendor is explicit that the roadmap call stays with the team. The output is ranked evidence, not a plan.
- **The protected-resource document is advertised on the MCP host while the product site serves a 404 on its bare well-known path.** The correct document is `https://mcp.closedloop.sh/.well-known/oauth-protected-resource`, the one the 401 header names; discovery clients that guess the apex domain will get an HTML 404 page instead of JSON.

## FAQ

### Do I need an account to read anything?

Yes. There is no anonymous tool: an unauthenticated initialize returns 401, and the profile, insight and conversation tools all return workspace data. The vendor's free tier makes the account free, not keyless.

### How is this different from the customer feedback entries already here?

Feedier covers surveys, NPS and sentiment classification. The Customer Intelligence and Segmentation entry tiers customers by value. Meeting-note servers search transcripts. This one joins all of those sources into one ranked set of product themes, keeping the original quote and the revenue of the customers who raised it, which is the evidence a roadmap argument actually needs.

### Can an assistant change anything?

Four tools write, and three of them are operational: a feedback note to the vendor, a watch that fires on a condition, and two calls that log a test permission request without messaging a customer. No tool edits customer records or contacts customers.

### Does it work for a European workspace?

Yes, with a separate host: `https://eu.mcp.closedloop.sh` for the EU region and `https://mcp.closedloop.sh` for the US, chosen when the connector is added.

## See Also

- [Feedier MCP](/hermes/mcp/servers/external/feedier-mcp)
- [ParrotNotes MCP](/hermes/mcp/servers/external/parrotnotes-mcp)
- [Granola MCP](/hermes/mcp/servers/external/granola-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
