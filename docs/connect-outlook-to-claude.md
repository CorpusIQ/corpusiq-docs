---
title: "Connect Outlook to Claude via MCP - Search and Read Mail"
description: "Connect Outlook to Claude through CorpusIQ MCP. Search the mailbox, read threads and check the calendar in plain language, with read-only Microsoft Graph permissions."
category: Claude Integrations
tags: ["connect Outlook to Claude", "Outlook Claude integration", "MCP Outlook connector", "Microsoft Graph to Claude", "search Outlook mail in Claude", "CorpusIQ MCP"]
last_updated: "2026-10-30"
canonical: "https://www.corpusiq.io/docs/connect-outlook-to-claude"
robots: "index,follow"
---

# How to Connect Outlook to Claude with CorpusIQ MCP

Most of what a business agreed to is written down in email. The delivery date, the discount that was approved, the reason the last invoice was disputed. Finding it means opening Outlook, trying three spellings of a name, and reading a thread backwards.

Connecting Outlook through CorpusIQ MCP makes the mailbox askable. You describe what you are looking for, Claude searches the folders and reads the thread, and the answer comes back with the message it came from.

### Why Connect Outlook to Claude?

- **Thread recall.** "What did the client say about the delivery timeline?"
- **Search without spelling guesses.** "Find every email from the Microsoft account team this quarter."
- **Summaries.** "Summarize the unread mail from this morning, grouped by sender."
- **Action extraction.** "Pull the action items out of this week's project updates."
- **Relationship questions.** "When did I last email the vendor contact, and what did we agree?"
- **Calendar context.** "What is on my calendar this week that relates to the Acme renewal?"
- **Read-only by permission.** Microsoft Graph `Mail.Read` and `Calendars.Read`. Claude cannot send, delete, move, or create anything.

### How It Works

1. **Connect Outlook to CorpusIQ** through Microsoft's consent screen and accept the read-only permissions.
2. **CorpusIQ reads Microsoft Graph** on your behalf: folder structure, message content, attachments metadata, calendar events.
3. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your account settings.
4. **Claude searches and reads** the messages that answer the question, with Graph pagination and decoding handled behind the scenes.
5. **The answer cites the message** it came from, so the claim can be checked against the thread.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connections**.
2. Find **Outlook** (or **Microsoft 365**) and click **Connect**. If OneDrive is already connected under Microsoft 365, Outlook may already be authorized.
3. Sign in with your Microsoft account and review the requested permissions: `Mail.Read` and `Calendars.Read`. Click **Accept**.
4. You return to CorpusIQ and the Outlook card turns green.
5. Copy the MCP config block shown under **Settings, Integrations, Claude Desktop**.

**In Claude Desktop**

6. Open **Settings, Developer, Edit Config**. This opens `claude_desktop_config.json`.
7. Add the CorpusIQ entry:

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

8. Save the file and fully quit Claude Desktop. Not just the window: quit the application.
9. Reopen Claude, complete the device login when prompted, and the tools indicator appears next to the message box.
10. Verify with "show me my Outlook folders". If the folder names look right, mailbox access is working.

If the tools indicator does not appear, work through [Claude can't see CorpusIQ](troubleshooting/claude-cant-see-corpusiq.md) before changing anything else.

### Example Claude Questions

**Search**

- "Find all emails from the Microsoft account team this quarter."
- "Search my inbox for anything about the compliance audit."
- "Show me emails with attachments sent last week."
- "Which messages mention the contract negotiation?"

**Reading**

- "What did the client say about the delivery timeline?"
- "Summarize the thread about the budget approval and list what was agreed."
- "Pull the action items out of this week's project status emails."

**Folders and mailbox state**

- "How many unread emails do I have, by folder?"
- "Show me the messages in the Projects folder."
- "Which folders hold the most mail?"

**Relationships and calendar**

- "When did I last email the vendor contact?"
- "Show my email history with Acme over the last 12 months."
- "What is on my calendar this week?"

**Cross-source**

- "Which open deals in the CRM have no email in the last 30 days?" (requires the CRM connector)
- "Does the invoice amount in the email match what QuickBooks shows?" (requires the accounting connector)

### Security

- **Read permissions only.** `Mail.Read` and `Calendars.Read`. `Mail.Read` does not include any write capability, so there is no path from Claude into a message.
- **No sending.** The connection never sends mail, replies, deletes a message, moves a folder, or creates an event.
- **Tenant-controlled.** In a Microsoft 365 tenant, an administrator can require approval before any third-party application is granted access. The consent URL is in your dashboard.
- **Revocable two ways.** Click **Reconnect** to refresh a lapsed token, or revoke the application in Microsoft Entra to end access.
- **Scoped direct-MCP retention.** Direct MCP retrieval is read-only. Raw customer files and full connector payloads are not retained. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Microsoft Graph, CorpusIQ, and Claude.

### Comparison: Outlook Search vs Mail Through Claude

| Aspect | Outlook search | CorpusIQ MCP with Claude |
|---|---|---|
| Input | A keyword or a sender name | A question about what was said |
| Output | A list of messages | A summary with the message cited |
| Across folders | One folder at a time | Asked once, all folders |
| Thread reading | You read top to bottom | Asked directly, key points out |
| Attachments | Open each one | Filename, type, and size surfaced |
| Calendar plus mail | Two searches | One question, both sources |
| Write access | Yes, by you | None, read-only permission |

Search finds the message. Claude is what tells you what it means across forty of them.

### FAQ: Common Questions

<details>
<summary><strong>Is the connection read-only?</strong></summary>

Yes. CorpusIQ requests the `Mail.Read` and `Calendars.Read` delegated permissions from Microsoft Graph. Claude can search, list, and read mail across folders and read calendar events. It cannot send an email, delete a message, move one between folders, change categories, or create an event.
</details>

<details>
<summary><strong>What Outlook data can Claude access?</strong></summary>

Messages across the folders the signed-in account can open: Inbox, Sent Items, custom folders, and archive folders. Message properties include sender, recipients, subject, date, body, categories, flags, and importance. Folder structure with message and unread counts. Attachment metadata with filename, type, and size. Calendar events and their details.
</details>

<details>
<summary><strong>Can it search a specific folder?</strong></summary>

Yes. "Search the Client Projects folder for emails about the Q3 deliverables" works, and so does a search across all folders. Folder targeting adds precision in a large mailbox, which is usually the difference between a clean answer and a noisy one.
</details>

<details>
<summary><strong>My folder structure is nested and messy. Does that break it?</strong></summary>

No. Claude can discover the folder structure first, then search within the folder it found. You do not need to remember where something lives any more than you do in a chat with a colleague who knows your filing habits.
</details>

<details>
<summary><strong>Does it read attachments?</strong></summary>

It surfaces attachment metadata: filename, type, and size. The contents of a document attached to a message are a different read, and for Google or Microsoft documents the file tools are the right route.
</details>

<details>
<summary><strong>What if the mailbox is a shared or team mailbox?</strong></summary>

Access follows the account you authorize. A shared mailbox the account can open is reachable. One it cannot open stays out of reach. Folder targeting is the practical way to keep a shared mailbox answerable without mixing it into personal mail.
</details>

<details>
<summary><strong>My IT admin blocks connections. What happens?</strong></summary>

Microsoft Entra can require admin approval before any third-party application is granted permissions. If that happens, the connector reports "admin approval required" and your dashboard has the consent URL to send to the administrator. Nothing is half-connected in the meantime.
</details>

<details>
<summary><strong>Why Claude rather than Outlook's own search?</strong></summary>

Outlook search returns messages. Claude reads them, reconciles what three people said, and states what was actually agreed. For a thread of forty messages that is the difference between an afternoon and a question.
</details>

---

**Next steps:** [Connect Outlook to Claude now](https://corpusiq.io/connect/outlook-with-claude)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
