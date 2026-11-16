---
title: "Connect Dropbox to Claude via MCP - Files and Contracts"
description: "Connect Dropbox to Claude through CorpusIQ MCP. Search contracts, decks and invoices in plain language and get answers with the files named."
category: Claude Integrations
tags: ["connect Dropbox to Claude", "Dropbox Claude integration", "MCP Dropbox connector", "Dropbox data to Claude", "AI for document search", "CorpusIQ MCP"]
last_updated: "2026-11-16"
canonical: https://www.corpusiq.io/docs/connect-dropbox-to-claude
robots: index,follow
---

# How to Connect Dropbox to Claude with CorpusIQ MCP

A lot of operating context lives in Dropbox. Signed contracts, past board updates, vendor invoices, design files, the deck someone rebuilt three times. Finding the right document is usually a memory test, and reading it is a second one.

Connecting Dropbox to Claude through CorpusIQ MCP turns that folder tree into something you can question. Ask what the latest agency contract says, and the answer comes back with the file it came from.

### Why Connect Dropbox to Claude?

- **Search by meaning, not filename.** "The invoice from the logistics vendor in March" does not need the file to be called that.
- **Read inside documents.** Word, Excel, PowerPoint, PDF and text contents are read, not just listed.
- **Cross-source context.** Contract terms sit in the same conversation as revenue, customer records or project data from other connectors.
- **Folder inventory.** What is in a folder, what changed this week, what nobody has touched since last year.
- **Quota and account checks.** Storage usage and account details without opening the Dropbox admin page.
- **No write path.** The connection reads files. It never uploads, edits, moves or deletes them.

### How It Works

1. **Connect Dropbox to CorpusIQ** through the Dropbox consent screen, approving read access.
2. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your CorpusIQ account settings.
3. **CorpusIQ translates** your question into Dropbox search and file reads, then extracts the text from the matching documents.
4. **Claude answers** from that content and names the file each detail came from.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in to CorpusIQ and open **Connectors**.
2. Select **Dropbox** and click Connect.
3. Sign in to Dropbox when the consent screen appears.
4. Approve read access. You are returned to CorpusIQ and Dropbox turns from gray to green.
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

**Finding documents**

- "Find my Dropbox file mentioning the Q3 board deck."
- "Which contracts in Dropbox were signed this year?"
- "Show me files added to the Shared folder in the last two weeks."
- "Find the most recent invoice from our logistics vendor."

**Reading documents**

- "What does the latest agency contract say about termination notice?"
- "Summarize the terms in our current office lease."
- "Compare the payment terms in these two vendor agreements."
- "What did the last board update say about hiring?"

**Account and housekeeping questions**

- "How much Dropbox storage am I using?"
- "Which files in the Contracts folder have not been modified in a year?"
- "What is in my Dropbox Contracts folder?"
- "List the five largest documents in this folder."

### Security

- **OAuth consent, read scope.** Access is granted through Dropbox OAuth and limited to reading account information and file contents.
- **No write tools.** CorpusIQ never uploads, edits, deletes or moves files, and does not expose share-link creation to the assistant.
- **Revocable at any time.** Dropbox, Settings, Connected apps. Removing CorpusIQ there ends the connection.
- **Scoped direct-MCP retention.** CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Comparison: Dropbox search vs Dropbox Through Claude

| Question | Dropbox search | CorpusIQ MCP with Claude |
|---|---|---|
| Input | Filename keywords and filters | A question in plain language |
| Output | A list of files | An answer with the file named as the source |
| Reading | You open each document | Claude reads the contents and synthesizes |
| Comparison | Manual across files | Difference between two documents in one answer |
| Cross-source | Dropbox only | Documents plus records from other connectors |
| Write access | Yes, by you | None exposed to the assistant |

Dropbox search is the right tool when you know the filename. Claude is the right tool when you know the question.

### FAQ: Common Questions

<details>
<summary><strong>Can Claude see every file in my Dropbox?</strong></summary>

It can search what the authorizing account can access. Files shared with you and Team folders follow your existing Dropbox permissions, so the connection never sees more than you do.
</details>

<details>
<summary><strong>Can Claude change or delete files?</strong></summary>

No. The connection is read-only. Nothing is uploaded, edited, moved or deleted.
</details>

<details>
<summary><strong>Which file types can be read?</strong></summary>

Word documents, Excel workbooks, PowerPoint decks, PDFs and plain text are read. Images and other binary formats are referenced by name and metadata rather than parsed.
</details>

<details>
<summary><strong>Does this work with Dropbox Business?</strong></summary>

Yes. It connects to personal and Business accounts. Team folders appear according to the permissions of the account that authorized the connection.
</details>

<details>
<summary><strong>How current is the file list?</strong></summary>

Each question runs against Dropbox at the moment you ask, so files added minutes ago are visible.
</details>

<details>
<summary><strong>Do I need to move files into a special folder?</strong></summary>

No. Nothing needs reorganizing and no files are copied. The connection searches your existing folder structure.
</details>

---

**Next steps:** [Connect Dropbox to Claude now](https://www.corpusiq.io/docs/connectors/dropbox)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
## See also

- [Connect Dropbox to Perplexity](connect-dropbox-to-perplexity.md) - contracts and decks read from your own folders inside a Perplexity thread.
- [Connect Dropbox to ChatGPT](connect-dropbox-to-chatgpt.md) - document search and comparison inside a ChatGPT thread.
- [Dropbox connector reference](connectors/dropbox.md) - connection requirements, visible objects and troubleshooting.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
