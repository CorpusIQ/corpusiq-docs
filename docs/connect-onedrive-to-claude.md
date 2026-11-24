---
title: "Connect OneDrive to Claude via MCP - Read Any File"
description: "Connect OneDrive to Claude through CorpusIQ MCP. Ask what a contract says or what changed this quarter, read-only, with the file named in the answer."
category: Claude Integrations
tags: ["connect OneDrive to Claude", "OneDrive Claude integration", "MCP OneDrive connector", "OneDrive files to Claude", "file search in Claude", "CorpusIQ MCP"]
last_updated: "2026-11-24"
canonical: "https://www.corpusiq.io/docs/connect-onedrive-to-claude"
robots: "index,follow"
---

# How to Connect OneDrive to Claude with CorpusIQ MCP

Contracts, spreadsheets, board decks, the prior report you wrote three months ago. It is all in OneDrive, and OneDrive will find a file if you remember the name it was given.

The questions that matter are the other kind. What the renewal clause says. Which pricing sheet is current. What changed since the last review. Connecting OneDrive to Claude through CorpusIQ MCP makes those answerable in the conversation, read-only, with the file named in the answer.

### Why Connect OneDrive to Claude?

Document search answers a filename question. The work asks a content question, and the file is the place the answer happens to live.

- **Read the clause, not just find the file.** "Search OneDrive for any contract with Acme Corp and read the payment terms." Claude lists the file and reads the text inside it.
- **Current versus stale.** "What does the latest pricing spreadsheet say?" One answer instead of opening three versions and guessing which is live.
- **What changed.** "Which spreadsheets were edited since the first of the month?" and "show me files I opened recently" map the work that moved.
- **Account state.** "How much OneDrive storage am I using, and which files have been shared with me?" Useful before a cleanup, not after.
- **Cross-source context.** Put a contract in OneDrive beside the invoice in QuickBooks or the charge in Stripe, in the same conversation, so the document and the system agree.
- **Fewer hands on the keyboard.** The alternative is download, attach, and ask again in a fresh thread. This is the question asked where the answer is needed.

### How It Works

1. **Connect OneDrive to CorpusIQ.** Authorize read-only access with your Microsoft 365 work or personal account. If you already connected Outlook, OneDrive may already be authorized under the same Microsoft connection.
2. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your CorpusIQ account settings.
3. **CorpusIQ translates** your question into OneDrive file searches and reads, and retrieves the file listing or the file content you asked about.
4. **Claude answers** from that retrieved content, with the file it used named in the answer.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connectors**.
2. Select **OneDrive** (or the Microsoft 365 card, if your account groups them).
3. Sign in with your Microsoft account and accept the permissions shown on the consent screen.
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
        "https://mcp2.corpusiq.io/mcp"
      ]
    }
  }
}
```

7. Save the file and fully quit Claude Desktop. Not just the window: quit the application.
8. Reopen Claude, complete the device login when prompted, and the tools indicator appears next to the message box.

If the tools indicator does not appear, work through [Claude can't see CorpusIQ](troubleshooting/claude-cant-see-corpusiq.md) before changing anything else.

### Example Claude Questions

**Find and read**

- "Find my OneDrive file about the Q3 board meeting."
- "Search OneDrive for any contract with Acme Corp and read the payment terms."
- "What does the latest pricing spreadsheet say?"

**Change over time**

- "Show me files I opened recently."
- "Which spreadsheets were edited since the first of the month?"

**Account state**

- "How much OneDrive storage am I using?"
- "Which files have been shared with me?"

**Cross-source**

- "Compare the invoice totals in OneDrive against the bills in QuickBooks." (requires the QuickBooks connector)
- "Does the renewal date in the vendor contract match the next invoice date in Stripe?" (requires the Stripe connector)

### Security

- **Read-only by permission.** The connection requests read access to your file list, folder structure, and the contents of files you ask it to read. There is no path for Claude to edit, delete or share a file.
- **Enforced in two places.** The Microsoft consent scopes and the MCP tool set both refuse writes, so a write attempt fails rather than silently succeeding.
- **Revocable at any time.** Removing the CorpusIQ application in your Microsoft account, or disconnecting OneDrive in the CorpusIQ dashboard, ends the connection immediately.
- **Scoped direct-MCP retention.** Direct MCP retrieval is read-only. Raw customer files and full connector payloads are not retained. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **Tenant control.** If your Microsoft 365 admin restricts third-party applications, the connection stays blocked until the admin approves CorpusIQ for the tenant.
- **TLS in transit** between OneDrive, CorpusIQ, and Claude.

### Comparison: OneDrive Search vs OneDrive Through Claude

| Aspect | OneDrive search and preview | CorpusIQ MCP with Claude |
|---|---|---|
| Input | A filename or a keyword | A question about the content |
| Reading a document | Open, scroll, quote by hand | Claude reads it and answers |
| Several documents | One at a time | Compared in one answer |
| Mixing sources | Export and reconcile elsewhere | OneDrive plus QuickBooks, Stripe or email in one answer |
| Write access | Yes, by you | None, read-only |

OneDrive is the right tool when you know the file. Claude is the right tool when you know the question.

### FAQ: Common Questions

<details>
<summary><strong>Can Claude edit, delete or share OneDrive files?</strong></summary>

No. The connection carries read access and the connector exposes file listing and file read tools only. You read files inside Claude; anything that changes a file happens in OneDrive, by you.
</details>

<details>
<summary><strong>Which file types can it read?</strong></summary>

Word documents, Excel workbooks, PowerPoint decks, PDFs and plain text files. What gets read is the text embedded in the file.
</details>

<details>
<summary><strong>It cannot find a file that exists in OneDrive.</strong></summary>

Confirm the file lives in OneDrive rather than a SharePoint site or a Teams shared library. Those are different stores, and this connection reads the personal OneDrive store.
</details>

<details>
<summary><strong>It says consent is required.</strong></summary>

Your Microsoft 365 admin restricts third-party applications. Ask them to approve CorpusIQ for your tenant, then reconnect.
</details>

<details>
<summary><strong>Permission denied on one specific file.</strong></summary>

That file was shared with restricted access. Open it in OneDrive to confirm your own access, and the connector inherits the same boundary.
</details>

<details>
<summary><strong>What is retained after a query?</strong></summary>

Direct MCP retrieval does not retain raw customer files or full connector response payloads. Operational query logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
</details>

---

**Next steps:** [Connect OneDrive to Claude now](https://www.corpusiq.io/connectors)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
