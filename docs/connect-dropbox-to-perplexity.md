---
title: "Connect Dropbox to Perplexity via MCP"
description: "Connect Dropbox to Perplexity through CorpusIQ MCP. Ask about contracts, board decks and invoices held in your folders, answered from the actual files."
category: Perplexity Integrations
tags: ["connect Dropbox to Perplexity", "Dropbox Perplexity integration", "MCP Dropbox connector", "document search", "contract lookup", "CorpusIQ MCP"]
last_updated: "2026-11-08"
canonical: "https://www.corpusiq.io/docs/connect-dropbox-to-perplexity"
robots: "index,follow"
---

# How to Connect Dropbox to Perplexity with CorpusIQ MCP

A lot of operating context never reaches a database. Contracts, past board updates, vendor invoices, design files, the renewal letter a supplier sent in March.

It lives in Dropbox folders, in files with names only the person who saved them understands.

Connecting Dropbox through CorpusIQ MCP lets a Perplexity thread search and read those files, read-only, beside the live numbers from your other connectors.

### Why Connect Dropbox to Perplexity?

- **Document lookup.** "Find the file in Dropbox that mentions the Q3 board deck."
- **Clause reading.** "Read the latest agency contract and tell me the termination notice period."
- **Folder inventory.** "What is in the Contracts folder, newest first?"
- **Recency.** "Which Dropbox files did we touch in the last week?"
- **Storage.** "How much Dropbox storage are we using, and what is the quota?"
- **Cross-source truth.** "Does the renewal date in the vendor contract match the next invoice date in QuickBooks?"
- **Read-only by scope.** The connection can search and read. It cannot upload, edit, move, or delete a file.

### How It Works

1. **Connect Dropbox to CorpusIQ** through the Dropbox consent screen.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ searches and reads** folders, file listings, recently modified files, and the text inside Word, Excel, PowerPoint, PDF, and plain text files as the question requires.
4. **Perplexity answers** from those files and names what it read.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational query logs are retained for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Open your dashboard, find **Dropbox**, and click **Connect**.
2. Sign in to Dropbox when the consent screen appears and approve read access. You are returned to CorpusIQ with the connector green.

**In Perplexity**

3. Open **Settings** and find the **MCP servers** section.
4. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

5. Connect and approve the CorpusIQ authorization page once.
6. Start a new thread and ask a document question.

Dropbox search runs against Dropbox's own index, which can lag for very recent uploads. Name the folder when you know it, because a folder question returns faster and more completely than a whole-account search.

### Example Perplexity Questions

**Finding a document**

- "Find my Dropbox file mentioning 'Q3 board deck'."
- "What is in the Contracts folder, newest first?"
- "Show me Dropbox files I have touched in the last week."

**Reading a document**

- "Read the latest agency contract from Dropbox and summarise the payment terms."
- "Which of our vendor agreements auto-renew this quarter?"
- "Pull the invoice totals out of the PDFs in the Invoices folder."

**Folder and account state**

- "How much Dropbox storage am I using?"
- "Which folders hold the most files?"
- "List the shared folders and who they are shared with."

**Cross-source**

- "Does the renewal date in the vendor contract match the next invoice date in QuickBooks?" (requires the QuickBooks connector)
- "Which Dropbox contracts have no matching deal in the CRM?" (requires the CRM connector)

### Security

- **Search and read only.** The connection reads listings and file contents. There is no path from Perplexity that uploads, edits, moves, or deletes a file.
- **Revocable at any time.** Disconnect in CorpusIQ or revoke the app in Dropbox and the connection ends immediately.
- **Account-scoped.** Access follows the Dropbox account you authorised. A folder you cannot open yourself stays out of reach.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Dropbox, CorpusIQ, and Perplexity.

### Comparison: Dropbox Search vs Dropbox in Perplexity

| Aspect | Dropbox search | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | A filename or a keyword | A question about the content |
| Output | A list of files to open | An answer quoting what the files say |
| Across folders | One search at a time | Asked as one question |
| Cross-source | Copy the figure by hand | Asked across connectors |
| Summarising | Read each file yourself | Asked directly |
| Write access | Full, by you | None, read only |

Search tells you where a file is. The connector tells you what it says and how it compares to the numbers elsewhere.

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity upload or delete a Dropbox file?</strong></summary>

No. The connection carries read access and the connector has no write tool. Files, folders, and sharing settings are untouched.
</details>

<details>
<summary><strong>Why can I not find a file I just uploaded?</strong></summary>

Dropbox search uses Dropbox's index, which can lag for very recent uploads. Wait a few minutes, or ask for the folder listing instead of a content search.
</details>

<details>
<summary><strong>A PDF reads blank. Why?</strong></summary>

Image-only PDFs need OCR to yield text, and this connection reads embedded text. Ask for a text-based export or paste the clause you need.
</details>

<details>
<summary><strong>Can it read Excel files and not just documents?</strong></summary>

Yes. Word, Excel, PowerPoint, PDF, and plain text files all yield their text.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. Dropbox is exposed to ChatGPT, Claude, and Perplexity through the same endpoint on the same subscription.
</details>

<details>
<summary><strong>Where is the Dropbox data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Operational logs may persist for up to 30 days. See the [security documentation](/hermes/security/read-only-and-security).
</details>

---

**Next steps:** [Connect Dropbox to Perplexity now](https://corpusiq.io/connect/dropbox-with-perplexity)

**Also in ChatGPT:** [Connect Dropbox to ChatGPT](connect-dropbox-to-chatgpt.md) - contracts, decks and invoices read from your folders inside a ChatGPT thread.

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
