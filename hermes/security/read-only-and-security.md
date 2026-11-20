---
title: "Security, Read-Only Access, and What CorpusIQ Never Does"
description: "CorpusIQ connectors do not retain raw customer files or full connector response payloads. CorpusIQ is not an AI agent: it reads authorized business data."

canonical: "/hermes/security/read-only-and-security/"
robots: "index, follow"
tags: [security, read-only, privacy, no-storage, oauth, governance, ai-agent]
last_updated: "2026-11-20"
---

# Security, Read-Only Access, and What CorpusIQ Never Does

CorpusIQ is built on one rule: it reads, and it never acts.

This page is the complete answer to the questions customers ask most:
can CorpusIQ change anything in my systems? Does it retain my data?
Can it act like an AI agent? The answer to all three is no.

## CorpusIQ uses read-only access on every connection

Every connector uses read-only OAuth. CorpusIQ can retrieve data from
your connected business tools. It cannot write to them, modify them, or
execute anything inside them.

- No campaign changes. CorpusIQ cannot create, edit, or pause ads in
  Google Ads, Meta, or any advertising platform.
- No budget changes. Bidding, budgets, and targeting are never touched.
- No data writes. CorpusIQ never creates records, updates fields, or
  deletes anything in QuickBooks, Shopify, Stripe, or any other system.
- No file edits. Documents, sheets, and emails are read only.

## CorpusIQ is not an AI agent

An AI agent takes actions on your behalf. CorpusIQ does not.

CorpusIQ only allows ChatGPT, Claude, Perplexity, or another AI client
to securely read the business data you authorized. The AI client is the
conversation layer. CorpusIQ is the governed intelligence layer that
decides which systems get checked, validates the data, and returns a
verified answer. There is no execution capability inside CorpusIQ.

If you ever want an AI system to take actions, write data, or execute
workflows, you would use a separate external AI agent. That agent could
use CorpusIQ through a direct MCP connection to securely read the
business data it needs, and then act through its own integrations.

## Retention: raw data is not retained

Data passes through CorpusIQ on demand.

When you ask a question, the authorized data is retrieved from your
systems, processed for the answer, and returned to your AI client as
read-only information. CorpusIQ uses read-only access for direct MCP
live retrieval. It does not retain raw customer files or full connector
response payloads; operational logs retain query text, per-user
tool-call metadata, and bounded outcome summaries for up to 30 days.
There is no warehouse, no data lake, and no retention of your business
records beyond those scoped operational logs.

## No one at CorpusIQ can access your accounts

Your connections are yours. The OAuth authorization you approve is
scoped to your account, and no CorpusIQ staff member can access or read
your connected systems. The data flows from your systems to your AI
client through CorpusIQ, on demand, without human access.

## Why this is intentional

CorpusIQ's business model is designed to avoid the security and
liability risks of allowing AI to write to or execute actions inside
customer systems. Read-only access means:

- No risk of accidental writes or destructive actions
- No data retention liability
- No privilege escalation surface
- Answers you can trust, because the data was never modified

## How the read-only guarantee is enforced

1. Read-only OAuth scopes on every connector. CorpusIQ requests only
   the permissions needed to read data, never to modify it.
2. No mutation endpoints. The CorpusIQ server exposes no path that can
   write to a connected system.
3. On-demand passthrough. Data is fetched per question and returned,
   not collected or stored.
4. Independent authentication. Each connector authenticates separately
   under your account, with no shared credentials.

One boundary worth stating precisely: external retrieval is read-only,
and configuration controls can write scoped platform state. Enabling or
disabling a connector, or re-authorizing one, changes a setting inside
your CorpusIQ account. It never changes a record in Shopify, Stripe,
QuickBooks, or any other connected system.

## What an agent may do: the machine-readable answer

A security reviewer or an agent platform asks a narrower question than policy
prose can answer: at the tool level, what may this connection do? CorpusIQ
answers that per tool, in the standard MCP way, inside the tool listing itself.

Measured on 2026-11-20 against the live server (`tools/list` on
`https://mcp2.corpusiq.io/mcp`):

| Measure | Count |
|---|---|
| Tools exposed | 526 |
| `readOnlyHint: true` | 504 |
| Not read-only | 22 |
| Tools without annotations | 0 |

The 22 tools that are not read-only are all configuration controls inside your
CorpusIQ account. None of them writes to a connected business system. They are:

- Answer governance: `canonical_facts_set`, `canonical_decisions_add`,
  `canonical_pending_commit`, `canonical_pending_cancel`,
  `truth_sources_register`, `truth_sources_remove`
- Metric definitions: `metric_spec_set`, `metric_spec_remove`
- Connector lifecycle: `enable_connector`, `disable_connector`,
  `reset_connector_token`
- Direct database connection setup: `configure_cosmos_connection`,
  `configure_imap_connection`, `configure_mssql_connection`,
  `disconnect_cosmos_connection`, `disconnect_imap_connection`,
  `disconnect_mssql_connection`, `disconnect_gunbroker_connection`
- Channel settings: `add_my_youtube_brand_channel`,
  `remove_my_youtube_brand_channel`, `set_my_primary_youtube_channel`
- Session: `logout_all`

## Where authority is enforced

The OAuth metadata advertises identity scopes only (`openid`, `email`,
`profile`) and three grant types: `authorization_code`, `refresh_token` and
`urn:ietf:params:oauth:grant-type:device_code`. Resource authority is not
expressed as OAuth scopes, because access is not decided at scope granularity.
It is decided server side for each principal and each tenant, and each access
token carries the principal, tenant, actor type and policy version it was
issued under.

That is the honest description: the read and write split is machine-readable at
the tool level, and the per-user decision is enforced on the server rather than
by a scope string. A platform that asks users to approve what an agent may do
can read the split from the tool listing and does not need a separate document.

## Questions you can ask

- "Can CorpusIQ change my ad campaigns?"
- "Does CorpusIQ store my business data?"
- "Can CorpusIQ write to QuickBooks or Shopify?"
- "Is CorpusIQ an AI agent that takes actions?"
- "Who at CorpusIQ can access my connected accounts?"

## Related pages

- [Connectors overview](/connectors)
- [Google Workspace connector](/connectors)
- [Meta connector](/connect/meta-ads-with-chatgpt)
- [MCP Apps: Interactive UIs](/hermes/mcp/mcp-apps-interactive-ui)
