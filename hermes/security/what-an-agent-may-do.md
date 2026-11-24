---
title: "What an Agent May Do at CorpusIQ"
description: "Every CorpusIQ MCP tool reviewed: 105 read business data, 16 change state, and all 16 change only your CorpusIQ workspace, never a connected business system."
canonical: "/hermes/security/what-an-agent-may-do/"
robots: "index, follow"
tags: [security, mcp, tools, read-only, permissions, governance, agent]
last_updated: "2026-11-24"
---

# What an Agent May Do at CorpusIQ

If you are reviewing CorpusIQ for a directory, a security questionnaire,
or your own procurement process, this page answers one question in full:
what can an AI client actually do once it holds a CorpusIQ connection?

The answer is bounded by the tool catalog itself. The server publishes
121 tools. 105 of them read business data. 16 of them change state. Every
one of the 16 changes state inside your CorpusIQ workspace only. None of
the 121 writes to a connected business system.

## The catalog at a glance

| Tool class | Count | What it touches |
|---|---|---|
| Read-only retrieval | 105 | Your connected business data, read only |
| Configuration | 16 | Your CorpusIQ workspace state |
| Writes to customer systems | 0 | Nothing |

The server declares this per tool, in the MCP tool annotations. The 105
retrieval tools carry `readOnlyHint: true`. The 16 configuration tools
carry `readOnlyHint: false`. A client that respects the specification can
inspect both values before it calls anything.

## The 105 read-only tools

These retrieve data from the systems you authorized: accounting,
commerce, payments, advertising, analytics, search performance, CRM,
email and messaging, files and documents, project tracking, databases,
and creator channels. Examples by family:

- Accounting and commerce: QuickBooks, Stripe, Shopify, Amazon Seller
- Advertising and analytics: Google Ads, Meta Ads, LinkedIn Ads, GA4
- Search performance: Google Search Console, Bing Webmaster Tools
- CRM and lifecycle: HubSpot, Salesforce, Klaviyo, Mailchimp, ActiveCampaign
- Files and documents: Google Drive, Sheets, Docs, Dropbox, Notion
- Databases and data platforms: PostgreSQL, MSSQL, Cosmos DB, PostHog
- Creator and developer: YouTube, GitHub, TikTok, Slack, Monday

A retrieval tool cannot create, update, delete, pause, or send anything.
It returns data to the AI client and stops there.

## The 16 configuration tools

These are the only tools in the catalog that change state, and their
reach ends at your CorpusIQ workspace.

**Workspace memory (8 tools).** Your declared facts, decisions, metric
definitions, and source-of-truth entries live in a tenant-scoped layer
inside CorpusIQ. `canonical_facts_set`, `canonical_decisions_add`,
`truth_sources_register`, `truth_sources_remove`, `metric_spec_set`,
and `metric_spec_remove` prepare such a change. `canonical_pending_commit`
applies it and `canonical_pending_cancel` discards it.

**Connector preferences and authentication (5 tools).**
`enable_connector` and `disable_connector` show or hide a connector's
tools for the current user. `reset_connector_token` clears stale
connector authorization so it can be re-established.
`disconnect_gunbroker_connection` removes stored GunBroker credentials.
`logout_all` deletes every stored OAuth token for the user and returns
re-authentication links.

**Creator channel registry (3 tools).** `add_my_youtube_brand_channel`,
`remove_my_youtube_brand_channel`, and `set_my_primary_youtube_channel`
maintain which Brand Account channels are registered to your CorpusIQ
user and which one is primary. Registration resolves a public channel
handle through the YouTube Data API and stores the result in your
CorpusIQ profile.

## Configuration changes are two-step by design

The workspace memory tools do not save on first call. Each one returns a
`pending_write_id` and waits. Nothing is written until the user confirms
in their own words and the client calls `canonical_pending_commit` with
that identifier. If the user declines, `canonical_pending_cancel`
discards the pending change. A client cannot append to your canonical
layer silently in one step.

## Access is decided per tenant and per user

Configuration tools act only on the caller's own scope. They take no
account identifier for a business system because they never touch one.

- Connector authorization is per user. Each person connects their own
  accounts through their own OAuth consent. One user's session cannot
  reach another user's connections.
- Connector visibility is per user. Disabling a connector hides its
  tools from that user's tool list and leaves everyone else untouched.
- Workspace memory is tenant-scoped. Facts, decisions, metric specs, and
  source-of-truth entries resolve against the calling tenant's namespace.
- Tokens are user-scoped. `logout_all` deletes the caller's stored OAuth
  tokens and no one else's.
- No one at CorpusIQ holds a tool that reads a customer's business
  system on the customer's behalf outside the authorized connection.

## What no tool in the catalog can do

- Create, edit, or delete a record in QuickBooks, Shopify, Stripe,
  HubSpot, Salesforce, or any other connected system
- Change an ad budget, bid, targeting setting, or campaign state in
  Google Ads, Meta, or LinkedIn
- Send an email, message, or post on your behalf
- Edit a document, sheet, or file in Drive, Dropbox, or Notion
- Execute arbitrary code, shell commands, or database statements
- Read another tenant's workspace memory or another user's connections

If you want an AI system that takes actions inside your business
systems, that is a different product with different permissions.
CorpusIQ is the governed read layer those agents can consume.

## Related

- [Security, Read-Only Access, and What CorpusIQ Never Does](/hermes/security/read-only-and-security)
- [MCP security best practices](/mcp-security-best-practices)
- [How the MCP architecture works](/how-it-works/mcp-architecture)
- [Connectors overview](/connectors)


