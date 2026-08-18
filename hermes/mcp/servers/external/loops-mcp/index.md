---
title: "Loops MCP Server - CorpusIQ Docs"
description: Official Loops MCP for AI agents — manage contacts, mailing lists, campaigns, transactional email, and account data, paired with a CLI and agent skills.
category: Marketing
stars: n/a (new listing)
added: 2026-08-15
source: mcpservers.org
relevance: ★★★
tags: [email-marketing, transactional-email, contact-management, campaigns, deliverability, claude-skills, remote-mcp]
---

# Loops MCP Server

**MCP server (connection flow via Loops app, paired with CLI and agent skills)** — Loops, the email platform built for software companies, ships an official MCP server for managing contacts, mailing lists, campaigns, transactional email, and account data. It is part of a three-layer agent surface: the MCP server for Claude Code and Claude Desktop, a CLI, and installable agent skills that teach agents the Loops API, CLI, markup language (LMX), and email best practices.

```
Server type: MCP server via Loops app connection flow (Claude Code / Claude Desktop)
Auth: Loops account (app.loops.so)
Endpoint: Provisioned through the Loops app flow (vendor docs at loops.so/docs/mcp-server)
Tools: Contacts, mailing lists, campaigns, transactional email, account data (per vendor docs)
Pricing: Loops platform subscription
Category: Marketing / Email
Built by: Loops (loops.so)
```

## Why This Matters for Operators

Email is the highest-leverage owned channel for software businesses, and it is still run from a dashboard an agent cannot touch. Loops' MCP server closes that gap: the assistant that already knows the signup flow, the lifecycle logic, and the campaign calendar can now execute against the live platform — add a contact, fire a transactional email, check a list, read campaign state — instead of describing what a human should click next.

**The mechanism that matters is the skills layer around the server** — the vendor ships a CLI, API skills, an LMX email-markup skill, and a deliverability best-practices skill, so an agent gets both the tool surface and the operating knowledge in one install.

## Tools & Capabilities

The vendor describes the MCP surface as covering (per loops.so/docs/skills):

| Area | Purpose |
|---|---|
| Contacts | Create and manage contact records and properties |
| Mailing lists | Manage list membership and segments |
| Campaigns | Manage email campaigns |
| Transactional email | Send and manage transactional messages |
| Account data | Read account and deliverability state |

Parallel surfaces: REST API at `app.loops.so/api/v1` with a published OpenAPI spec (`app.loops.so/openapi.json`), plus the CLI and agent skills below.

## Installation

```bash
# One-shot installer — CLI plus every agent skill
curl -fsSL https://install.loops.so/wizard | sh
# Skills only
curl -fsSL https://install.loops.so/skills | sh
# Claude plugin marketplace (Claude Code)
claude plugin marketplace add loops-so/skills
claude plugin install loops@loops-plugins
```

The MCP server itself is added through the Loops connection flow documented at loops.so/docs/mcp-server for Claude Code and Claude Desktop (see also the skills repo at github.com/Loops-so/skills).

## Configuration

The vendor's agent guide points MCP users at the in-app "Add the Loops MCP server" flow rather than a copy-paste JSON block. For non-MCP automations, the REST API is the contract:

```bash
curl -X POST https://app.loops.so/api/v1/transactional \
  -H "Authorization: Bearer $LOOPS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"transactionalId": "YOUR_ID", "email": "user@example.com", "dataVariables": {"firstName": "Alex"}}'
```

Auth notes: Loops account credentials and API keys are managed in the Loops app (app.loops.so/settings).

## Business Relevance

- **Founders running software businesses** get lifecycle email operated from inside the agent that owns the product logic
- **Growth operators** get campaigns, lists, and transactional sends as tool calls instead of dashboard hops
- **Engineering teams** get the CLI and OpenAPI spec for app-side automation with an agent that already knows both
- **Deliverability-minded operators** get the email best-practices skill — consent, lifecycle coverage, and transactional-vs-marketing audits

## Integration with CorpusIQ

Loops composes with CorpusIQ's email and analytics connectors as an execution layer. A closed loop: GA4 connector reports signup conversion, the agent creates the contact and fires the welcome transactional email through Loops MCP, and the Klaviyo, Mailchimp, or ActiveCampaign connectors provide the cross-source reporting view of revenue attribution and engagement. Because CorpusIQ already normalizes email-platform metrics across Klaviyo, Mailchimp, Constant Contact, and ActiveCampaign, adding Loops MCP execution to that stack gives operators one agent that can both run the sends (Loops) and reconcile the results (CorpusIQ connectors).

## Limitations

- Brand new MCP listing — no long track record yet
- MCP connection flow is documented for Claude Code and Claude Desktop first; other clients go through the REST API or CLI
- The endpoint URL is provisioned through the vendor's in-app flow, not published as a copy-paste config
- Commercial SaaS — the MCP surface requires a Loops account and platform subscription
- Tool list is vendor-described, not independently enumerated; treat app.loops.so/openapi.json as the REST contract

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
