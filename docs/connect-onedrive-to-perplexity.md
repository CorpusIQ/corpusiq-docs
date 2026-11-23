---
title: "Connect OneDrive to Perplexity via MCP"
description: "Connect OneDrive to Perplexity through CorpusIQ MCP. Ask what a contract says or which pricing sheet is current, with the file named in the answer."
category: Perplexity Integrations
tags: ["connect OneDrive to Perplexity", "OneDrive Perplexity integration", "MCP OneDrive connector", "search OneDrive files with AI", "ask about a document in plain English", "CorpusIQ MCP"]
last_updated: "2026-11-23"
canonical: "https://www.corpusiq.io/docs/connect-onedrive-to-perplexity"
robots: "index,follow"
---

# How to Connect OneDrive to Perplexity with CorpusIQ MCP

OneDrive holds the working documents of a business: contracts, pricing sheets, board decks, the report you wrote three months ago and cannot find by name now. OneDrive will locate a file if you remember what it was called and roughly where it went.

The questions that matter are the other kind. What the renewal clause says. Which pricing sheet is current. What changed between the two versions. Those need the file read, not just found.

Connecting OneDrive through CorpusIQ MCP makes the store answerable inside Perplexity, with the file named in the answer.

### Why Connect OneDrive to Perplexity?

- **Contract recall.** "Find the current MSA with Acme and list the payment terms and the renewal clause."
- **Version drift.** "Which pricing spreadsheet is the most recent, and what changed from the previous one?"
- **Deck and memo recall.** "Find the Q3 board deck and summarise the variance commentary."
- **Change over time.** "Which spreadsheets in OneDrive were edited since the first of the month?"
- **Account state.** "How much OneDrive storage am I using, and which files were shared with me?"
- **Read-only by capability.** The retrieval tools documented on this page list and read files. They do not edit, delete, move or share anything.

### How It Works

1. **Connect OneDrive to CorpusIQ.** Sign in with your Microsoft account and accept the permissions the consent screen shows.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ reads** the file list, the folder structure and the text inside the documents you ask about, in the OneDrive store that account can open.
4. **Perplexity answers** with the file named, so the claim can be checked against the document itself.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational logs keep query text, per-user tool-call metadata and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Sign up at [corpusiq.io](https://www.corpusiq.io). The 30-day trial needs no credit card.
2. Open **Dashboard**, then **Connectors**, and find **OneDrive** under the Microsoft 365 integrations.
3. Click **Connect**. If Outlook is already connected, check the connector list first: OneDrive is often already covered by that same Microsoft connection.
4. Sign in with your Microsoft account, review the permissions on the consent screen and click **Accept**.
5. The OneDrive card turns from gray to green.

**In Perplexity**

6. Open **Settings** and find the **MCP servers** section.
7. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

8. Connect and approve the CorpusIQ authorisation page once. Then start a new thread and name a document, a folder or a question the file answers.

Organisations that restrict third-party applications route this through a Microsoft Entra ID administrative approval, so the tenant's own policy decides what is authorised before any file is read.

### Example Perplexity Questions

**Find and read**

- "Find my OneDrive file about the Q3 board meeting."
- "Search OneDrive for any contract with Acme Corp and read the payment terms."
- "What does the latest pricing spreadsheet say?"

**Change over time**

- "Show me files I opened recently."
- "Which spreadsheets were edited since the first of the month?"
- "Compare this quarter's forecast workbook with the previous version and list the changed assumptions."

**Account state**

- "How much OneDrive storage am I using?"
- "Which files have been shared with me?"

**Cross-source**

- "Compare the invoice totals in OneDrive against the bills in QuickBooks." (requires the QuickBooks connector)
- "Does the renewal date in the vendor contract match the next invoice date in Stripe?" (requires the Stripe connector)
- "Do the figures in this board deck reconcile with the same period in the accounting system?" (requires an accounting connector)

### Security

- **Read-only retrieval tools.** The tools documented on this page list files, list folders and read file contents. Nothing is edited, deleted, moved or shared.
- **Your own permission set.** Access follows the Microsoft account you authorised: a file you cannot open yourself stays out of reach.
- **One personal store.** The connection reads the OneDrive store of that account, not a SharePoint site or a Teams library.
- **Revocable.** Disconnecting ends the connection, and Microsoft's own account permissions page lists the application too.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text, tool-call metadata and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Microsoft, CorpusIQ and Perplexity.

### Comparison: OneDrive search and Office

| Aspect | OneDrive search and Office | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | A file name, a folder path, a keyword | A question about what a document says |
| Match | Names and snippets | The passage that answers it |
| Scope | One store, one file at a time | The store, read against the question |
| Follow-ups | Open another file | Ask the next question in the same thread |
| Outside context | Open a second tab | Same thread, same answer |
| Write access | Yes, by you | None through the retrieval tools |

A search box finds documents. It does not read them for you.

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity edit, delete or share my files?</strong></summary>

No. The retrieval tools documented on this page list files and read their contents. Anything that changes a file happens in OneDrive, by you.
</details>

<details>
<summary><strong>Which file types can it read?</strong></summary>

Word documents, Excel workbooks, PowerPoint decks, PDFs and plain text files. What is read is the text inside the file.
</details>

<details>
<summary><strong>It cannot find a file that exists in OneDrive.</strong></summary>

Confirm the file lives in OneDrive rather than a SharePoint site or a Teams shared library. Those are different stores, and this connection reads the personal OneDrive store.
</details>

<details>
<summary><strong>Permission denied on one specific file.</strong></summary>

That file was shared with restricted access. Access follows the Microsoft account you authorised, so a file you cannot open yourself stays out of reach.
</details>

<details>
<summary><strong>The consent screen is blocked by my organisation.</strong></summary>

Your Microsoft 365 administrator restricts third-party applications. Ask them to approve CorpusIQ for the tenant, then reconnect.
</details>

<details>
<summary><strong>I already connected Outlook. Do I need to connect OneDrive separately?</strong></summary>

Often not. OneDrive can already be authorised under the same Microsoft connection, so check the connector list before running the consent flow again.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. OneDrive is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

### See Also

- [Connect OneDrive to ChatGPT](connect-onedrive-to-chatgpt.md) - the same document questions, asked from ChatGPT
- [OneDrive connector reference](connectors/onedrive.md) - what the connection can see and how the Microsoft consent flow works
- [Connect SharePoint to Perplexity](connect-sharepoint-to-perplexity.md) - the team libraries beside the personal store
- [Connect Google Drive to Perplexity](connect-google-drive-to-perplexity.md) - the other file store, the same questions

---

**Next steps:** [Add CorpusIQ to Perplexity now](https://www.corpusiq.io/connectors/perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
