---
title: "Why AI Should Never Write to Your Business Tools"
description: "Read-only OAuth lets AI read your business data without write risk. How per-source tokens and scopes keep QuickBooks, Shopify and Stripe safe."
last_updated: "2026-11-25"
canonical: "https://www.corpusiq.io/docs/hermes/architecture/read-only-oauth-ai-business-tools/"
robots: "index,follow"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Read-Only External-Source Retrieval: Why AI Should Never Write to Your Business Tools

Every business tool you use contains data that should never be modified by AI. Your QuickBooks general ledger. Your Shopify orders. Your Stripe transactions. Your HubSpot CRM records.

Connecting AI to these tools requires a hard boundary: read everything, write nothing.

## The Risk of AI Write Access

AI models are probabilistic. They are right most of the time but wrong some of the time. When an AI writes an email draft, a mistake means an awkward sentence. When an AI modifies your QuickBooks, a mistake means corrupted financials.

Write access risks include:

**Financial errors**: A miscategorized transaction. A payment applied to the wrong invoice. An expense recorded in the wrong period. Each error compounds through your books.

**Data corruption**: Overwriting valid records. Creating duplicate entries. Deleting historical data that seemed irrelevant to the AI but was needed for audit.

**Compliance violations**: Modifying records in ways that break audit trails. Changing transactions after close periods. Altering data subject to regulatory retention requirements.

**Security exposure**: Write access is a broader attack surface. If an AI with write access is compromised, every tool it can write to is compromised.

## How Read-Only External-Source Retrieval Works

Read-only external-source retrieval gives AI permission to query data but blocks all write operations. The authorization flow is:

1. You log into your tool (Shopify, QuickBooks, Stripe, etc.)
2. You grant access to the AI connector, at the narrowest scope the provider publishes
3. The connector receives a token bound to that one platform and that one account
4. Every retrieval call uses this token, and the connector issues only read calls against it

Where the provider publishes a read-only scope, that scope is the wall. Google's `*.readonly` scopes for Analytics, Gmail, Drive and Sheets, Shopify's `read_` scopes, and Microsoft's `Files.Read.All` and `Sites.Read.All` scopes cannot write, so a write attempt is rejected by the platform. Where the provider publishes no read-only scope - QuickBooks Online grants a single read-write accounting scope, and Mailchimp governs access by user role rather than by scope - the boundary is held by the connector, which only issues read calls against that token. Either way the boundary sits below the model, and it is inspectable: the granted scope is listed in the platform's own consent screen and app settings.

One distinction worth stating plainly: external retrieval is read-only, but some platforms also expose configuration or control-plane operations outside the retrieval path. Those operations change scoped platform state, so they are named and annotated separately instead of being folded into the read-only claim. Ask any provider to draw that line explicitly.

## Per-Source Authentication

Each tool gets its own read-only external-source retrieval token. Shopify has one token. QuickBooks has another. Stripe has a third. No shared credentials. No master key.

This means:
- Compromising one connector does not compromise others
- Revoking access to one tool does not affect others
- Each tool maintains its own audit log of AI queries
- You can see exactly what data each AI accessed and when

## What Read-Only Means in Practice

**Shopify**: Query orders, products, customers, and analytics. Cannot create orders, modify inventory, or process refunds.

**QuickBooks**: Query chart of accounts, transactions, reports, and vendor data. Cannot create invoices, modify journal entries, or reconcile accounts.

**Stripe**: Query payments, subscriptions, customers, and disputes. Cannot process charges, issue refunds, or modify subscriptions.

**HubSpot**: Query contacts, deals, companies, and tickets. Cannot create records, modify pipelines, or send emails.

**GA4**: Query traffic, conversions, and audience data. Cannot modify tracking settings or data streams.

## Why This Matters for AI Business Intelligence

The promise of AI business intelligence is that you can ask any question about your business and get a verified answer. That promise only works if the AI can access your data without putting it at risk.

Read-only access means:
- Verified answers from live data
- Retrieval operations do not modify their source records
- Complete audit trail of every query
- Per-source security boundaries

This is not a feature. It is the foundation of trust between AI and business data.

## What to Look For

When evaluating AI data access platforms, inspect provider scopes and tool-level safety metadata separately. Confirm that retrieval operations are marked read-only, identify any write-capable management or control-plane operations, ask what the platform retains, and check whether access is auditable.

If a platform cannot answer these questions clearly, it does not have the security boundary your business data requires.

The difference between read-only and read-write is the difference between safe intelligence and unnecessary risk.
