---
title: Connect Odoo to ChatGPT via MCP
description: "Connect Odoo to ChatGPT through CorpusIQ MCP. Ask about open quotations, overdue invoices, stock on hand and pipeline across modules."
category: ChatGPT Integrations
tags: ["connect Odoo to ChatGPT", "Odoo MCP", "Odoo ChatGPT integration", "ask ChatGPT about ERP data", "Odoo inventory in ChatGPT", "CorpusIQ MCP"]
last_updated: "2026-11-08"
canonical: "https://www.corpusiq.io/docs/connect-odoo-to-chatgpt"
robots: "index,follow"
---

# How to Connect Odoo to ChatGPT with CorpusIQ MCP

Odoo is many applications sharing one database. The value is in the joins: a quotation that became an invoice, an invoice against a delivery, a delivery against stock on hand. The interface makes you open four screens and join them yourself.

Connecting Odoo through CorpusIQ MCP makes those cross-module questions answerable inside ChatGPT, read-only, with the module and record named in the answer.

## What Questions Can You Ask?

**Sales and pipeline**

- "What is the value of open quotations in Odoo right now?"
- "How many opportunities are in the negotiation stage?"
- "Which sales orders are confirmed but not yet delivered?"

**Money owed**

- "Show me overdue customer invoices."
- "What is the total of vendor bills due in the next 14 days?"
- "Which customers have both an overdue invoice and an open quotation?"

**Inventory**

- "What is on hand for SKU X across all warehouses?"
- "Which products are below their reorder point?"

**Operations**

- "List active projects and their task counts."
- "Which project tasks are past their deadline?"

**Cross-source**

- "Compare Odoo invoiced revenue against Stripe payouts this month." (requires the Stripe connector)
- "Which Odoo customers also have open deals in HubSpot?" (requires the HubSpot connector)

## FAQ: Common Questions

<details>
<summary><strong>Can ChatGPT confirm orders, post invoices or move stock?</strong></summary>

No. Every exposed tool is a read: partners, sale orders and quotations with line items, CRM leads and opportunities, customer and vendor invoices, products and on-hand inventory, stock transfers, journals, payments, taxes, employees, projects and tasks.
</details>

<details>
<summary><strong>What do I need to connect Odoo?</strong></summary>

Your Odoo instance URL, the database name, a login, and an API key for a user with read access to the modules you want visible. Setup takes about three minutes.
</details>

<details>
<summary><strong>Does this work with Odoo Online, Odoo.sh and self-hosted?</strong></summary>

Yes. Any instance that answers over HTTPS with a reachable database name works, including Odoo Online, Odoo.sh and a self-hosted deployment.
</details>

<details>
<summary><strong>Authentication failed. What should I check?</strong></summary>

Generate a fresh API key in Odoo under Preferences, then Account Security, and reconnect. A key created for a different user will also fail if that user lacks module access.
</details>

<details>
<summary><strong>One module comes back empty.</strong></summary>

The connected user probably has no access rights to that module's records. Odoo enforces its own permissions, so the connection can only read what the user can open in the interface.
</details>

<details>
<summary><strong>What is retained after a query?</strong></summary>

Direct MCP retrieval is read-only. Raw customer files and full connector response payloads are not retained; operational query logs keep query text and bounded outcome summaries for up to 30 days.
</details>

## How It Works

1. You enter your instance URL, database name, login and API key in the CorpusIQ connector form and save.
2. CorpusIQ verifies the credentials against the instance and exposes the readable modules as read-only MCP tools.
3. You add the CorpusIQ MCP server to ChatGPT. See the [Quick Start guide](quick-start.md).
4. ChatGPT calls the module the question needs and joins the records it returns.
5. The answer names the module and the period, so the figure can be reconciled in Odoo.

## Setup Guide

1. **Sign up** at [corpusiq.io](https://www.corpusiq.io). The 30-day trial needs no credit card.
2. **Connect Odoo.** Open Dashboard, then Connections, find Odoo, then enter your instance URL, the database name, a login and an API key with read access.
3. **Connect ChatGPT.** Add the CorpusIQ MCP server per the [Quick Start guide](quick-start.md).
4. **Verify.** Ask "how many opportunities are in each stage". Real stage names mean the connection is live.
5. **Explore.** Then ask the cross-module question that has meant four screens and a manual join.

## Related Pages

- [Odoo connector reference](connectors/odoo.md) - what the connection can see and the credential setup
- [Connect Odoo to Perplexity](connect-odoo-to-perplexity.md) - the same modules inside a Perplexity thread
- [Connect QuickBooks to ChatGPT](connect-quickbooks-to-chatgpt.md) - the accounting side of the same question
- [Connect NetSuite to ChatGPT](connect-netsuite-to-chatgpt.md) - the other ERP, same shape
- [Connect Salesforce to ChatGPT](connect-salesforce-to-chatgpt.md) - the CRM record beside the ERP record
- [Browse all CorpusIQ connectors](connectors.md) - the full list
- [How to Connect Business Data to ChatGPT](how-to-connect-business-data-to-chatgpt.md) - the general setup

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
