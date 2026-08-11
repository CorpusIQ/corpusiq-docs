# Read-Only OAuth: Why AI Should Never Write to Your Business Tools

Every business tool you use contains data that should never be modified by AI. Your QuickBooks general ledger. Your Shopify orders. Your Stripe transactions. Your HubSpot CRM records.

Connecting AI to these tools requires a hard boundary: read everything, write nothing.

## The Risk of AI Write Access

AI models are probabilistic. They are right most of the time but wrong some of the time. When an AI writes an email draft, a mistake means an awkward sentence. When an AI modifies your QuickBooks, a mistake means corrupted financials.

Write access risks include:

**Financial errors**: A miscategorized transaction. A payment applied to the wrong invoice. An expense recorded in the wrong period. Each error compounds through your books.

**Data corruption**: Overwriting valid records. Creating duplicate entries. Deleting historical data that seemed irrelevant to the AI but was needed for audit.

**Compliance violations**: Modifying records in ways that break audit trails. Changing transactions after close periods. Altering data subject to regulatory retention requirements.

**Security exposure**: Write access is a broader attack surface. If an AI with write access is compromised, every tool it can write to is compromised.

## How Read-Only OAuth Works

Read-only OAuth gives AI permission to query data but blocks all write operations. The authorization flow is:

1. You log into your tool (Shopify, QuickBooks, Stripe, etc.)
2. You grant read-only access to the AI connector
3. The connector receives a token scoped to read-only operations
4. Every API call uses this token — the tool's own security rejects any write attempt

Even if the AI tries to modify data, the tool itself blocks the operation. The boundary is enforced at the API level, not the AI level.

## Per-Source Authentication

Each tool gets its own read-only OAuth token. Shopify has one token. QuickBooks has another. Stripe has a third. No shared credentials. No master key.

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
- Zero risk of data modification
- Complete audit trail of every query
- Per-source security boundaries

This is not a feature. It is the foundation of trust between AI and business data.

## What to Look For

When evaluating AI data access platforms, verify that every connector uses read-only OAuth. Ask whether the platform stores your data between queries. Check whether you can see audit logs of what was accessed.

If a platform cannot answer these questions clearly, it does not have the security boundary your business data requires.

The difference between read-only and read-write is the difference between safe intelligence and unnecessary risk.
