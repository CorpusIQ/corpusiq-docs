---
title: "Connect Odoo to Claude via MCP - ERP Answers in One Question"
description: "Connect Odoo to Claude through CorpusIQ MCP. Ask across sales orders, invoices, stock and projects in one question instead of twenty screens."
category: Claude Integrations
tags: ["connect Odoo to Claude", "Odoo Claude integration", "MCP Odoo connector", "Odoo data to Claude", "AI for ERP", "CorpusIQ MCP"]
last_updated: "2026-11-16"
canonical: https://www.corpusiq.io/docs/connect-odoo-to-claude
robots: index,follow
---

# How to Connect Odoo to Claude with CorpusIQ MCP

Odoo holds the operating record: quotations, invoices, inventory, projects, employees. It also spreads that record across modules, so a question that crosses modules becomes a tour of the menu.

Connecting Odoo to Claude through CorpusIQ MCP collapses that tour. Ask what open quotations are worth and which customers owe you money, and both answers arrive with the records behind them.

### Why Connect Odoo to Claude?

- **Cross-module questions.** Sales, invoicing, inventory and projects answered in one response instead of four screens.
- **Quotation and order visibility.** Open quotations, their line items and their total value, without building a filter.
- **Receivables.** Overdue customer invoices and vendor bills read as a list.
- **Stock position.** On-hand quantities per product and location, asked as a sentence.
- **Project and people context.** Active projects, task counts and employee records read alongside the commercial data.
- **No write path.** The connection reads records. It never confirms orders, posts invoices or moves stock.

### How It Works

1. **Connect Odoo to CorpusIQ** with your instance URL, database name, login and API key.
2. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your CorpusIQ account settings.
3. **CorpusIQ translates** your question into Odoo record reads across the modules involved, then assembles the results.
4. **Claude answers** from those records and names the module and record type each figure comes from.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in to CorpusIQ and open **Connectors**.
2. Select **Odoo** and click Connect.
3. Enter your Odoo URL, for example https://yourcompany.odoo.com, the database name shown on the Odoo login screen, your login and an API key.
4. Save. CorpusIQ verifies the connection and Odoo turns from gray to green.
5. Copy the MCP config block under **Settings, Integrations, Claude Desktop**.

**In Claude Desktop**

7. Open **Settings, Developer, Edit Config**. This opens `claude_desktop_config.json`.
8. Add the CorpusIQ entry:

```json
{
  "mcpServers": {
    "corpusiq": {
      "command": "npx",
      "args": [
        "-y", "mcp-remote",
        "https://mcp2.corpusiq.io/mcp"
      ]
    }
  }
}
```

9. Save the file and fully quit Claude Desktop. Not just the window: quit the application.
10. Reopen Claude, complete the device login when prompted, and the tools indicator appears next to the message box.

If the tools indicator does not appear, work through [Claude can't see CorpusIQ](troubleshooting/claude-cant-see-corpusiq.md) before changing anything else.

### Example Claude Questions

**Sales and pipeline questions**

- "What is the value of open quotations in Odoo right now?"
- "How many opportunities are in the negotiation stage?"
- "Which quotations expire this month?"
- "Show me sale orders confirmed this week with their totals."

**Finance questions**

- "Show me overdue customer invoices."
- "Which vendor bills are unpaid?"
- "What did we invoice last month, by customer?"
- "How much tax did we collect last quarter?"

**Inventory and project questions**

- "What is on hand for SKU X across all warehouses?"
- "Which products are below their reorder point?"
- "List active projects and their task counts."
- "Show me stock transfers scheduled this week."

### Security

- **Record-level access.** Odoo enforces the connected user's access rights, so Claude sees the modules and records that user can already open. Connect a read-scoped user if you want the boundary explicit.
- **No write path.** CorpusIQ reads records. There is no confirm, post, validate or stock-move path exposed to the assistant.
- **Revocable at any time.** Revoke the API key in Odoo under Preferences, Account Security, and the connection stops working.
- **Scoped direct-MCP retention.** CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Comparison: Odoo screens vs Odoo Through Claude

| Question | Odoo UI | CorpusIQ MCP with Claude |
|---|---|---|
| Input | Module, menu, filters | A question in plain language |
| Output | Record lists you read | A synthesized answer with records named |
| Cross-module | One module at a time | Sales, finance and stock in one answer |
| Exports | Manual list export | Structured text on request |
| Write access | Full record access in the UI | None exposed to the assistant |

Odoo records the business. Claude answers questions about it without making anyone learn the menu structure.

### FAQ: Common Questions

<details>
<summary><strong>Does this work with Odoo Online, Odoo.sh and self-hosted instances?</strong></summary>

Yes. The connection takes your instance URL, database name, login and API key, which covers Odoo Online, Odoo.sh and self-hosted deployments.
</details>

<details>
<summary><strong>Can Claude confirm orders or post invoices?</strong></summary>

No. The connection reads records only. Order confirmation, invoice posting and stock moves stay in Odoo, performed by your team.
</details>

<details>
<summary><strong>What happens if a module looks empty?</strong></summary>

Access follows the connected user's rights. If a module returns nothing, the user is probably missing that module's access rights in Odoo.
</details>

<details>
<summary><strong>How do I connect a specific Odoo user?</strong></summary>

Generate the API key from that user's Preferences, Account Security page. The key inherits that user's access rights.
</details>

<details>
<summary><strong>Authentication failed. What should I check?</strong></summary>

Generate a fresh API key in Odoo and confirm the database name matches exactly what the Odoo login screen shows.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Each question runs against your Odoo instance when you ask, so records created this morning are included.
</details>

---

**Next steps:** [Connect Odoo to Claude now](https://www.corpusiq.io/docs/connectors/odoo)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
## See also

- [Connect Odoo to Perplexity](connect-odoo-to-perplexity.md) - quotations, invoices and stock across ERP modules inside a Perplexity thread.
- [Connect Odoo to ChatGPT](connect-odoo-to-chatgpt.md) - ERP questions answered inside a ChatGPT thread.
- [Odoo connector reference](connectors/odoo.md) - connection requirements, visible objects and troubleshooting.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
