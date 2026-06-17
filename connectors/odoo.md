# Odoo

## What it unlocks
Pull your Odoo ERP into conversation — sales orders, invoices, CRM pipeline, inventory, projects, employees — without clicking through twenty Odoo screens. Ask questions that span modules in one shot.

## Before you connect
- An Odoo instance URL (Odoo Online, Odoo.sh, or self-hosted).
- A username and API key for an Odoo user with read access to the modules you want CorpusIQ to see.
- The database name.
- About 3 minutes.

## How to connect
1. Open your CorpusIQ dashboard and click Connections.
2. Find Odoo and click Connect.
<!-- screenshot: Odoo configuration form -->
3. Enter your Odoo URL (e.g., https://yourcompany.odoo.com), database name, login, and API key.
4. Save. CorpusIQ verifies the connection.

You'll see Odoo change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
- Partners (customers and vendors).
- Sale orders and quotations with line items.
- CRM leads and opportunities by stage.
- Customer and vendor invoices.
- Products and on-hand inventory.
- Stock transfers, journals, payments, taxes.
- Employees, projects, and project tasks.

Read-only. CorpusIQ never confirms orders, posts invoices, or moves stock.

## Questions you can ask
- "What's the value of open quotations in Odoo right now?"
- "How many opportunities are in the negotiation stage?"
- "Show me overdue customer invoices."
- "What's on-hand for SKU X across all warehouses?"
- "List active projects and their task counts."

## Troubleshooting
- "Authentication failed" — generate a fresh API key in Odoo (Preferences → Account Security) and retry.
- "Database not found" — check that the database name exactly matches what Odoo shows on the login screen.
- A module looks empty — confirm the connected user has access rights to that module's records.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
