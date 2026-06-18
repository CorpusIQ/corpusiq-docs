# Recipe: Shopify–QuickBooks Daily Reconciliation

**Connectors:** shopify, quickbooks
**Category:** reconciliation
**Complexity:** cross-domain

---

## Use Case

Finance teams need to confirm that every Shopify sale processed yesterday has
a corresponding invoice or payment entry in QuickBooks. Discrepancies —
orders that appear in Shopify but not QuickBooks, or QuickBooks entries with
no matching Shopify order — surface fulfillment issues, payment processing
failures, and accounting gaps before they compound. Run this daily, first
thing in the morning for the prior day.

---

## Prerequisites

- CorpusIQ connectors connected: shopify, quickbooks
- Required scopes:
  - Shopify: read_orders, read_transactions
  - QuickBooks: accounting (read)
- Frequency: daily (run for prior calendar day)

---

## Query

```
Reconcile yesterday's Shopify orders against QuickBooks.

From Shopify: pull all orders created yesterday with status = any (include
fulfilled, unfulfilled, cancelled). For each order give me: order_id,
order_number, created_at, financial_status, total_price, customer email.

From QuickBooks: pull all invoices and payments created or updated yesterday.
For each give me: doc_number, txn_date, total_amt, customer_name, status.

Match Shopify orders to QuickBooks records by order number (Shopify order_number
should appear in QuickBooks doc_number or memo field).

Show me three sections:
1. Matched — Shopify order + QuickBooks record, amounts agree
2. Matched with discrepancy — amounts differ by more than $0.01
3. Unmatched — present in one system but not the other (flag which system)
```

---

## Sample Output

```
Daily Reconciliation — May 25, 2025

MATCHED (47 orders — $12,840.15 total)
All amounts agree. No action required.

MATCHED WITH DISCREPANCY (2 orders)
Order #4821 — Shopify: $149.00 | QuickBooks: $139.00 — Delta: $10.00
Order #4835 — Shopify: $89.99  | QuickBooks: $89.90  — Delta: $0.09

UNMATCHED (3 records)
[Shopify only] Order #4802 — $210.00 — financial_status: paid — no QB record found
[Shopify only] Order #4844 — $55.00  — financial_status: refunded — no QB record found
[QuickBooks only] Invoice #INV-2891 — $320.00 — customer: Acme Corp — no Shopify match
```

---

## Notes

- Shopify order_number (e.g. #4821) must appear in QuickBooks doc_number or
  the transaction memo field for matching to work. This requires your QuickBooks
  integration (native or third-party) to populate that field consistently.
- Refunded orders in Shopify often have separate credit memo entries in QuickBooks.
  If your workflow creates credit memos rather than updated invoices, adjust the
  query to include QuickBooks credit_memo object type.
- Cancelled orders with no payment are expected to be Shopify-only. Filter them
  out by adding "exclude Shopify orders where financial_status = pending" if needed.
- Currency: if you operate in multiple currencies, add "group by currency" to
  avoid comparing USD and GBP amounts directly.

---

## Variations

- **Weekly rollup:** Change date range to last 7 days for end-of-week reconciliation
- **By sales channel:** Add "break down by Shopify sales channel" to separate
  online store, POS, and wholesale
- **High-value threshold:** Add "flag any unmatched order over $500" for priority alerting
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
