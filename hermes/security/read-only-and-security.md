---
title: "Security, Read-Only Access, and What CorpusIQ Never Does"
description: "CorpusIQ connectors do not retain raw customer files or full connector response payloads. CorpusIQ is not an AI agent: it reads authorized business data and returns it to your AI client on demand."
canonical: "/hermes/security/read-only-and-security/"
robots: "index, follow"
tags: [security, read-only, privacy, no-storage, oauth, governance, ai-agent]
last_updated: "2026-08-22"
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
