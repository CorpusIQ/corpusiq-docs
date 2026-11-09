---
title: "Security and Read-Only Access"
description: "CorpusIQ security model: read-only OAuth access on every connector, no retention of raw files, and the guarantee that CorpusIQ never acts inside your systems."
canonical: "/hermes/security/"
robots: "index, follow"
tags: [security, read-only, privacy, no-storage, oauth, governance]
last_updated: "2026-11-09"
---

# Security and Read-Only Access

CorpusIQ is built on one rule: it reads, and it never acts.

Every connector uses read-only OAuth. CorpusIQ can retrieve data from
your connected business tools, but it cannot write to them, modify them,
or execute anything inside them.

One boundary worth stating precisely: external retrieval is read-only,
and configuration controls can write scoped platform state. Enabling or
disabling a connector, or re-authorizing one, changes a setting inside
your CorpusIQ account. It never changes a record in Shopify, Stripe,
QuickBooks, or any other connected system.

## Pages

- [Security, Read-Only Access, and What CorpusIQ Never Does](read-only-and-security) - the
  complete answer to the questions customers ask most: can CorpusIQ
  change anything in my systems? Does it retain my data? Can it act
  like an AI agent? The answer to all three is no.

## Related

- [Security Best Practices for Hermes Agent](../best-practices/security) - token and credential management, least-privilege access, and audit logging
- [Integrations](../integrations/index.md) - platform integrations and read-only connector patterns
- [Privacy and Security](https://www.corpusiq.io/docs/how-it-works/privacy-and-security/) - architecture, compliance, and data handling
