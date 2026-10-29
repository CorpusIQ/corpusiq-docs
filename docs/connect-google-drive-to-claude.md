---
title: "Connect Google Drive to Claude via MCP - Ask Your Documents"
description: "Connect Google Drive to Claude through CorpusIQ MCP. Ask what a contract says, find the current version of a document, and get answers tied to the file used."
category: Claude Integrations
tags: ["connect Google Drive to Claude", "Google Drive Claude integration", "MCP Drive connector", "search documents with Claude", "document Q&A", "CorpusIQ MCP"]
last_updated: "2026-10-29"
canonical: "https://www.corpusiq.io/docs/connect-google-drive-to-claude"
robots: "index,follow"
---

# How to Connect Google Drive to Claude with CorpusIQ MCP

Every company has a decision written down somewhere in Drive that nobody can find again. The contract, the pricing sheet, the policy, the proposal that was approved in March.

Drive search returns filenames. It does not return the clause. That gap is where people give up and ask whoever was there at the time.

Connecting Google Drive through CorpusIQ MCP makes the contents of those files answerable. You ask what the document says, and Claude answers with the file it read.

### Why Connect Google Drive to Claude?

- **Contract questions.** "What is the termination notice period in the Acme agreement?"
- **Version confusion.** "Which pricing sheet is the current one, and what changed?"
- **Policy lookup.** "What does our refund policy say about opened items?"
- **Deal rooms.** "Summarize the proposal folder for this account, with open questions."
- **Cross-source checks.** "Does the signed contract match the terms in the CRM record?"
- **Read-only by scope.** The connection reads files the connected account can open. It cannot edit, move, or delete anything.

### How It Works

1. **Connect Google Drive to CorpusIQ** through Google OAuth and approve the read-only Drive scopes.
2. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your CorpusIQ account settings.
3. **CorpusIQ searches** the files that answer the question, reads the relevant documents, and returns the passages.
4. **Claude answers** from that retrieved content, naming the file it used.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connectors**.
2. Select **Google Drive** (or the Google Workspace connector to add Calendar, Sheets, and Gmail to the same connection).
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

**Contracts and terms**

- "What is the renewal date and notice period in the Acme agreement?"
- "Which of these two contract versions has the better payment terms for us?"
- "List every obligation that falls on us in this MSA."

**Pricing and proposals**

- "Which pricing sheet is the most recent, and what changed in it?"
- "Summarize the proposal we sent this account, with the assumptions it relies on."
- "Find the discount policy and tell me whether this deal needs an exception."

**Operations**

- "What does the onboarding checklist require before a customer goes live?"
- "Find the current brand guidelines and list the approved colours."
- "Which document defines the escalation path for support incidents?"

**Cross-source**

- "Compare the signed contract terms with the deal record in the CRM." (requires the CRM connector)
- "Which invoices in billing have no matching purchase order file in Drive?" (requires the billing connector)

### Security

- **Read scope only.** The connection requests Google's read-only Drive scopes. Claude can open and read. It cannot edit, move, share, or delete.
- **Account-scoped access.** Only files the connected Google account can already open are reachable. Files never shared with that account stay out of scope.
- **Revocable at any time.** Google Account, Security, Third-party access. Revoking there ends the connection.
- **Scoped direct-MCP retention.** Direct MCP retrieval is read-only. Raw customer files and full connector payloads are not retained. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Google, CorpusIQ, and Claude.

### Comparison: Drive Search vs Drive Through Claude

| Aspect | Drive search | CorpusIQ MCP with Claude |
|---|---|---|
| Input | A filename, a guess at the words | A question about the content |
| Output | A list of files | A synthesized answer with the file named |
| Reading | You open each file | Claude reads the passages that answer it |
| Versions | You compare by date | It reports which file it read |
| Contracts | Manual clause hunting | The clause, quoted, with its source |
| Combining sources | Export and paste | Asked across connectors |
| Write access | Yes, by you | None, read-only scope |

Drive search is the right tool when you remember the file. Claude is the right tool when you remember the question.

### FAQ: Common Questions

<details>
<summary><strong>Can Claude edit or move files in my Drive?</strong></summary>

No. The connection is read-only. Claude can search and read files the connected account can open. It cannot create, edit, move, share, or delete anything in Drive.
</details>

<details>
<summary><strong>Does it read PDFs and Word documents?</strong></summary>

Text-based formats are read, which covers the common business set: Docs, PDFs with a text layer, Word files, plain text, and spreadsheets. Scanned images without a text layer are referenced rather than parsed, because there is no text to read.
</details>

<details>
<summary><strong>How does it handle multiple versions of the same document?</strong></summary>

Ask for the current one explicitly: "the latest signed version of the Acme agreement". The connector reads files as they stand, so a document edited this morning is what the next answer sees. When two files could match, the answer names the file it used so you can check it.
</details>

<details>
<summary><strong>Can it read files in shared drives?</strong></summary>

Yes, where the connected account has access to that shared drive. Access follows the Google account you approved, and the shared drive's own restrictions still apply.
</details>

<details>
<summary><strong>Can it combine Drive with my CRM or accounting?</strong></summary>

Yes. This is where document search stops being a search box. "Does the contract match what the CRM says about this account?" is one question across both sources instead of two manual checks.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. Files are read at the moment you ask. Raw customer files are not retained, and scoped operational logs may persist for up to 30 days.
</details>

<details>
<summary><strong>Where is my document data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Retrieval happens on demand. Operational logs may persist for up to 30 days. See the [security documentation](../security/) for detail.
</details>

---

**Next steps:** [Connect Google Drive to Claude now](https://corpusiq.io/connect/google-drive-with-claude)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
