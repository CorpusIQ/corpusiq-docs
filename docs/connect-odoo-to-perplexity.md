---
title: "Connect Odoo to Perplexity via MCP"
description: "Connect Odoo to Perplexity through CorpusIQ MCP. Ask about open quotations, overdue invoices, stock on hand and pipeline across ERP modules."
category: Perplexity Integrations
tags: ["connect Odoo to Perplexity", "Odoo Perplexity integration", "MCP Odoo connector", "ERP data to AI", "inventory and invoices", "CorpusIQ MCP"]
last_updated: "2026-11-05"
canonical: "https://www.corpusiq.io/docs/connect-odoo-to-perplexity"
robots: "index,follow"
---

# How to Connect Odoo to Perplexity with CorpusIQ MCP

Odoo holds the operating record of the business. Orders, quotations, invoices, inventory, projects, and the people doing the work.

It also holds them behind twenty screens arranged by module, which is why most Odoo questions get answered by an export.

Connecting Odoo through CorpusIQ MCP makes a question that spans modules answerable in one Perplexity thread, read-only.

### Why Connect Odoo to Perplexity?

- **Open quotations.** "What is the total value of quotations still awaiting a decision, by salesperson?"
- **Invoice exposure.** "Which customer invoices are overdue, and by how many days?"
- **Pipeline by stage.** "How many opportunities sit in negotiation, and what are they worth?"
- **Stock position.** "What is on hand for a SKU across every warehouse?"
- **Project load.** "List active projects with their open task counts."
- **Cross-source truth.** "Do the sales orders in Odoo match the revenue recorded in QuickBooks for last quarter?"
- **Read-only by scope.** The connection reads records. It cannot confirm an order, post an invoice, or move stock.

### How It Works

1. **Connect Odoo to CorpusIQ** with your instance URL, database name, login, and API key.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ queries** partners, sale orders, quotations, CRM leads, invoices, products, stock, journals, payments, taxes, employees, and projects as the question requires.
4. **Perplexity answers** from those records and names the period it measured.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational query logs are retained for up to 30 days.

### Setup Steps

**In Odoo**

1. Generate an API key for the user CorpusIQ will read as: **Preferences**, then **Account Security**, then new API key.
2. Confirm that user has read access to the modules you want queried.
3. Note your instance URL, in the form `https://yourcompany.odoo.com`, and the exact database name shown on the login screen.

**In CorpusIQ**

4. Open your dashboard, find **Odoo**, and click **Connect**.
5. Enter the URL, database name, login, and API key, then save. CorpusIQ verifies the connection.

**In Perplexity**

6. Open **Settings** and find the **MCP servers** section.
7. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

8. Connect and approve the CorpusIQ authorization page once.
9. Start a new thread and ask a question that crosses modules.

Two fields cause almost every failure. The database name must match what Odoo shows on the login screen exactly, and the API key must belong to a user who can already see the records you are asking about.

### Example Perplexity Questions

**Sales and quotations**

- "What is the value of open quotations right now?"
- "Which quotations have waited more than fourteen days for an answer?"
- "Compare this month's confirmed orders against the same month last year."

**Invoices and cash**

- "Show me overdue customer invoices with ageing."
- "What did we invoice in total last quarter, split by currency?"
- "Which vendor bills are due in the next two weeks?"

**Inventory and operations**

- "What is on hand for this SKU across all warehouses?"
- "Which products are below their reorder point?"
- "List this month's stock transfers by warehouse."

**Pipeline and projects**

- "How many opportunities are in the negotiation stage?"
- "List active projects and their task counts."
- "Which project has the most overdue tasks?"

**Cross-source**

- "Do the confirmed sales orders in Odoo match revenue in QuickBooks for last quarter?" (requires the QuickBooks connector)
- "Which Odoo customers have no record in the CRM?" (requires the CRM connector)

### Security

- **Read access only.** The API key reads records. There is no path from Perplexity that confirms an order, posts an invoice, moves stock, or edits a partner.
- **Revocable at any time.** Delete the key in Odoo and the connection ends immediately.
- **Permission-scoped.** Access is limited by the Odoo user's own rights. A module that user cannot open stays out of reach.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Odoo, CorpusIQ, and Perplexity.

### Comparison: Odoo Screens vs Odoo in Perplexity

| Aspect | Odoo interface | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | Navigate to the right module first | A question that spans modules |
| Output | A filtered list you read | An answer with the period named |
| Across modules | Open several screens | Asked in one question |
| Cross-source | Export to a spreadsheet | Asked across connectors |
| Ad-hoc questions | Build a filter or an export | Just ask |
| Write access | Full, by you | None, read only |

The screens are built for transactions. The connector is for the question that arrives between them.

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity confirm an order or post an invoice in Odoo?</strong></summary>

No. The connection carries read access and the connector has no write tool. Orders, invoices, stock, and partners are untouched.
</details>

<details>
<summary><strong>Why does authentication fail?</strong></summary>

Generate a fresh API key in Odoo under Preferences, Account Security, and reconnect. An expired or revoked key fails the same way a wrong one does.
</details>

<details>
<summary><strong>Why does it say the database was not found?</strong></summary>

The database name must match exactly what Odoo shows on the login screen, including any suffix. A near match is a different database.
</details>

<details>
<summary><strong>Why is a module empty in the answers?</strong></summary>

The connected Odoo user lacks access rights to that module's records. Grant read access to that user, or connect with a user who already has it.
</details>

<details>
<summary><strong>Does this work with a self-hosted Odoo?</strong></summary>

Yes. Odoo Online, Odoo.sh, and self-hosted instances all connect the same way, provided the instance is reachable over HTTPS from CorpusIQ.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. Odoo is exposed to ChatGPT, Claude, and Perplexity through the same endpoint on the same subscription.
</details>

<details>
<summary><strong>Where is the Odoo data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Operational logs may persist for up to 30 days. See the [security documentation](/hermes/security/read-only-and-security).
</details>

---

**Next steps:** [Connect Odoo to Perplexity now](https://corpusiq.io/connect/odoo-with-perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
