---
title: "Connect Gmail to Claude via MCP -- Live Inbox Data, No Code"
description: "Connect Gmail to Claude through CorpusIQ MCP. Ask about inbox threads, attachments, and commitments and get source-cited answers from live email."
category: Claude Integrations
tags: ["connect Gmail to Claude", "Gmail Claude integration", "MCP Gmail connector", "Gmail data to Claude", "AI for Gmail", "CorpusIQ MCP"]
last_updated: "2026-10-26"
canonical: https://www.corpusiq.io/docs/connect-gmail-to-claude
robots: index,follow
---

# How to Connect Gmail to Claude with CorpusIQ MCP

Your inbox is where decisions, commitments, and vendor terms actually live. The problem is that Gmail is a search box, not an analyst. It finds messages. It does not read forty replies and tell you what was agreed.

Connecting Gmail to Claude through CorpusIQ MCP closes that gap. You ask a question in plain language, Claude reads the messages that answer it, and the answer comes back with the source threads named. No exports. No CSV. No scrolling.

### Why Connect Gmail to Claude?

Email is the least structured system most businesses run on, and the hardest to query across. Claude gives you a natural language layer over it.

- **Thread summarization.** "Summarize the thread about the renewal terms." Claude reads every message in the thread, not just the top result.
- **Commitment tracking.** "What did we promise Acme about the delivery date?" The answer is in an email from six weeks ago. Claude finds it.
- **Structured extraction.** "List every invoice amount mentioned in emails this month." Unstructured email text becomes a table.
- **Relationship history.** "When did we last hear from this vendor?" One question instead of fifteen searches.
- **Cross-source context.** Pair email with CRM, billing, or order data in the same conversation, so correspondence and records get checked against each other.
- **Read-only by scope.** Gmail access is `gmail.readonly`. Claude can search and read. It cannot send, delete, or relabel anything.

### How It Works

1. **Connect Gmail to CorpusIQ** through Google OAuth, authorizing the read-only Gmail scope.
2. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your CorpusIQ account settings.
3. **CorpusIQ translates** your question into Gmail searches, retrieves the matching messages and threads, and decodes the bodies.
4. **Claude answers** from that retrieved content, with the messages it used.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connectors**.
2. Select **Gmail** (or the Google Workspace connector if you want Calendar, Drive, and Sheets alongside it).
3. Sign in to Google and approve the read-only Gmail scope.
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

**Inbox triage**

- "Summarize my unread email from this week in five bullets."
- "Which messages from today need a reply from me?"
- "What did I receive from Acme Corp in the last 30 days?"

**Decisions and commitments**

- "What did we agree with the customer about the delivery date?"
- "Find the last pricing we quoted and tell me which version is newest."
- "What did the vendor say changed in the contract?"

**Thread work**

- "Summarize the 40-message thread about the migration decision, with action items."
- "Who has not replied in the renewal thread?"
- "List the open questions in that thread and who owns each one."

**Extraction**

- "Pull every invoice amount mentioned in emails this month into a table."
- "List all the meeting times proposed in the last week of messages."
- "Extract every shipping address from order confirmations this quarter."

**Cross-source**

- "Show me email threads with customers who have open deals in the CRM." (requires the CRM connector)
- "Which vendor invoices mentioned by email match unpaid bills in accounting?" (requires the accounting connector)
- "Find feedback emails from customers who ordered recently." (requires the commerce connector)

### Security

- **Google-enforced read scope.** The connection requests `gmail.readonly`, a scope Google itself defines as read-only. There is no send, delete, or modify path.
- **Revocable at any time.** Google Account, Security, Third-party access. Revoking there ends the connection.
- **Consent screen transparency.** Google shows exactly what is granted, and it is one read scope, not a bundle of write scopes.
- **Scoped direct-MCP retention.** Direct MCP retrieval is read-only. Raw customer files and full connector payloads are not retained. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Gmail, CorpusIQ, and Claude.

### Comparison: Gmail Search vs Gmail Through Claude

| Aspect | Gmail search | CorpusIQ MCP with Claude |
|---|---|---|
| Input | Keywords and operators | A question in plain language |
| Output | A list of matching messages | A synthesized answer with the sources named |
| Reading | You open each message | Claude reads the bodies and threads |
| Long threads | Manual scrolling | Summarized with owners and open items |
| Extraction | Copy and paste into a spreadsheet | Returned as structured text |
| Cross-source | Gmail only | Email plus CRM, billing, orders |
| Write access | Yes, by you | None, read-only scope |

Gmail search is the right tool when you know which message you want. Claude is the right tool when you know which question you have.

### FAQ: Common Questions

<details>
<summary><strong>Can Claude send or delete email through this connection?</strong></summary>

No. The connection uses Google's read-only Gmail scope. Claude searches, lists, and reads messages. It cannot send, delete, archive, relabel, or change settings. Any write-capable tool, where one exists, is named separately and annotated.
</details>

<details>
<summary><strong>Which Gmail accounts can I connect?</strong></summary>

Each account is authorized independently, so a work account and a personal account can both be connected without sharing a login. Access follows the Google account you approve on the consent screen.
</details>

<details>
<summary><strong>Do I need to learn Gmail search operators?</strong></summary>

No. Ask in plain language and Claude builds the underlying query. If you already know operators such as `from:`, `has:attachment`, or `newer_than:`, you can put them in your question and they are used directly.
</details>

<details>
<summary><strong>Can Claude read attachments?</strong></summary>

Attachment metadata is available, and text-based attachments in supported formats can be read. Binary formats are referenced rather than parsed.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Every question is answered against the mailbox at the moment you ask. There is no nightly copy of your inbox behind the answers.
</details>

<details>
<summary><strong>Does this work with Google Workspace accounts?</strong></summary>

Yes, where the Workspace administrator permits third-party OAuth apps. If the admin has restricted app access, the consent screen is blocked at the Google layer and the fix is on the Workspace side, not in Claude.
</details>

---

**Next steps:** [Connect Gmail to Claude now](https://corpusiq.io/connectors/gmail)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
