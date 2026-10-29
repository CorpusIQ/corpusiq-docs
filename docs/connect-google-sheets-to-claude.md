---
title: "Connect Google Sheets to Claude via MCP - Live Sheet Answers"
description: "Connect Google Sheets to Claude through CorpusIQ MCP. Ask about budgets, trackers and pipelines in plain language and get answers tied to the sheet and tab used."
category: Claude Integrations
tags: ["connect Google Sheets to Claude", "Google Sheets Claude integration", "MCP Sheets connector", "spreadsheet data to Claude", "ask questions about a spreadsheet", "CorpusIQ MCP"]
last_updated: "2026-10-29"
canonical: "https://www.corpusiq.io/docs/connect-google-sheets-to-claude"
robots: "index,follow"
---

# How to Connect Google Sheets to Claude with CorpusIQ MCP

Half of a business lives in spreadsheets nobody designed as a database. The budget, the hiring plan, the pipeline tracker, the inventory count somebody updates on Fridays.

Claude can read that data and answer questions about it, but only if the data reaches Claude. Copying a tab into a chat works once and is stale by the next question.

Connecting Google Sheets through CorpusIQ MCP closes that gap. You ask a question, Claude reads the sheet as it stands, and the answer names the spreadsheet and the tab it came from.

### Why Connect Google Sheets to Claude?

- **Questions over formulas.** "Which cost centres are over budget this quarter?" instead of building another pivot.
- **Tracker reads.** "Which deals in the pipeline tracker have not moved in 30 days?"
- **Reconciliation.** "Compare the budget sheet to actuals in the accounting system, by category." Two sources, one question.
- **Change detection.** "What changed in the hiring plan since the last version?"
- **Threshold checks.** "Which SKUs in the inventory count are below the reorder point?"
- **Read-only by scope.** The connection reads spreadsheets. It cannot edit a cell, add a row, or change sharing.

### How It Works

1. **Connect Google Sheets to CorpusIQ** through Google OAuth and approve the read-only scopes on Google's consent screen.
2. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your CorpusIQ account settings.
3. **CorpusIQ translates** your question into spreadsheet reads, opens the tabs and ranges that answer it, and returns the values.
4. **Claude answers** from that retrieved content, naming the sheet and tab used.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connectors**.
2. Select **Google Sheets** (or the Google Workspace connector if you want Drive, Calendar, and Gmail alongside it).
3. Sign in to Google and approve the read-only scopes.
4. Copy the MCP config block shown under **Settings, Integrations, Claude Desktop**.

**In Claude Desktop**

5. Open **Settings, Developer, Edit Config**. This opens `claude_desktop_config.json`.
6. Add the CorpusIQ entry:

```json
{
  "mcpServers": {
    "corpusiq": {
      "command": "npx",
      "args": [
        "-y", "mcp-remote",
        "https://www.corpusiq.io/mcp/direct-connection"
      ]
    }
  }
}
```

7. Save the file and fully quit Claude Desktop. Not just the window: quit the application.
8. Reopen Claude, complete the device login when prompted, and the tools indicator appears next to the message box.

If the tools indicator does not appear, work through [Claude can't see CorpusIQ](troubleshooting/claude-cant-see-corpusiq.md) before changing anything else.

### Example Claude Questions

**Budget and spend**

- "What is total spend in the Q4 budget tab, by category?"
- "Which departments are more than 10 percent over plan?"
- "Show the three largest line items and who owns each one."

**Pipeline and operations**

- "Which deals in the pipeline tracker have not moved in 30 days?"
- "Sum open pipeline by stage and compare it with last month."
- "Which rows in the inventory count are below the reorder threshold?"

**People and planning**

- "Sum the headcount plan by department and compare it to actual headcount."
- "Which roles are approved but not yet opened?"

**Cross-source**

- "Compare the budget tab to actuals in QuickBooks for last quarter." (requires the accounting connector)
- "Which customers in the tracker have open invoices in billing?" (requires the billing connector)

### Security

- **Read scope only.** The connection requests Google's read-only spreadsheet scopes. There is no write path from Claude into a sheet.
- **Revocable at any time.** Google Account, Security, Third-party access. Revoking there ends the connection.
- **Account-scoped.** Access follows the Google account you approve. A sheet that account cannot open stays out of reach.
- **Scoped direct-MCP retention.** Direct MCP retrieval is read-only. Raw customer files and full connector payloads are not retained. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Google, CorpusIQ, and Claude.

### Comparison: Spreadsheet Search vs Sheets Through Claude

| Aspect | Searching a sheet | CorpusIQ MCP with Claude |
|---|---|---|
| Input | Ctrl+F, or a filter you rebuild | A question in plain language |
| Output | Rows you then read | A summarized answer with the tab named |
| Cross-tab | Manual, one tab at a time | Asked once across tabs |
| Formulas | You read the cell | Read as computed values |
| Combining sources | Export and merge | Asked across connectors |
| Write access | Yes, by you | None, read-only scope |

Spreadsheet search is the right tool when you know the row. Claude is the right tool when you know the question.

### FAQ: Common Questions

<details>
<summary><strong>Can Claude edit my spreadsheet through this connection?</strong></summary>

No. The connection reads spreadsheet data. Cells, rows, and sharing settings are untouched. Any write-capable path would be a separate decision with a separate credential, and it is not part of this connector.
</details>

<details>
<summary><strong>Does the whole file come through, or one tab?</strong></summary>

The connector can read a spreadsheet's tabs and ranges. For a large workbook, naming the tab in the question gives the tightest answer: "the FY26 budget tab" rather than "the budget file".
</details>

<details>
<summary><strong>Do merged cells and formulas break the answers?</strong></summary>

Formulas come through as their computed values, which is what you want. Merged cells and multi-row headers are the usual cause of a wrong answer, because the header no longer labels the right column. A clean tab with a single header row fixes it in a minute.
</details>

<details>
<summary><strong>Can it combine a sheet with QuickBooks or Stripe?</strong></summary>

Yes, and this is the strongest use of a Sheets connector. The plan lives in a sheet and the actuals live in accounting. "Compare budget to actual by category for last quarter" becomes one question instead of a manual reconciliation.
</details>

<details>
<summary><strong>Does connecting Sheets expose my whole Drive?</strong></summary>

No. Sheets is its own connector. Google's consent screen lists the read-only permissions being requested, and you approve them in one place. Revoke any of them later from your Google Account security settings. Connect only what a question would actually use.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. When you ask, the connector reads the sheet as it stands. A number typed a minute ago is visible to the next question. There is no nightly copy behind the answers.
</details>

<details>
<summary><strong>What about sheets owned by somebody else?</strong></summary>

Access follows the Google account you authorized. If that account can open the sheet, the connector can read it. A link-restricted share keeps its restriction.
</details>

<details>
<summary><strong>Where is my spreadsheet data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Retrieval happens on demand. Operational logs may persist for up to 30 days. See the [security documentation](../security/) for detail.
</details>

---

**Next steps:** [Connect Google Sheets to Claude now](https://corpusiq.io/connect/google-sheets-with-claude)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
