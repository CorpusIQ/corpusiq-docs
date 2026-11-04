---
title: "Connect Google Drive to Perplexity via MCP"
description: "Connect Google Drive to Perplexity through CorpusIQ MCP. Ask what a contract says or which version is current and get answers tied to the live file."
category: Perplexity Integrations
tags: ["connect Google Drive to Perplexity", "Google Drive Perplexity integration", "MCP Drive connector", "search documents with Perplexity", "document Q&A", "CorpusIQ MCP"]
last_updated: "2026-11-04"
canonical: "https://www.corpusiq.io/docs/connect-google-drive-to-perplexity"
robots: "index,follow"
---

# How to Connect Google Drive to Perplexity with CorpusIQ MCP

Every business has a decision that is written down somewhere in Drive and cannot be found again. The contract, the pricing sheet, the policy, the proposal that was approved in March.

Drive search returns filenames. It does not return the clause.

Connecting Google Drive through CorpusIQ MCP makes the contents of those files answerable inside a Perplexity thread, read-only, with the answer tied to the file it came from.

### Why Connect Google Drive to Perplexity?

- **Clause lookup.** "What is the termination notice period in the Acme contract?"
- **Version truth.** "Which of these three proposals is the latest, and what changed between them?"
- **Policy checks.** "What does our refund policy say about partial-month cancellations?"
- **Research with your own documents.** Perplexity can weigh outside context against your actual paperwork in one answer.
- **Onboarding speed.** "Summarize what a new account manager needs to know from the client folder."
- **Read-only by scope.** The connector reads files. It cannot create, move, share, or delete anything.

### How It Works

1. **Connect Google Drive to CorpusIQ** through Google OAuth and approve the read scopes, Drive included.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ finds and reads** the documents that answer the question, within what the connected Google account can open.
4. **Perplexity answers** from that retrieved content and cites the file it used.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational query logs are retained for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connectors**.
2. Select **Google Drive** (or the Google Workspace connector, which covers Drive, Calendar, Sheets and Gmail in one authorization).
3. Sign in to Google and approve the read scopes.
4. Copy the MCP endpoint shown under **Settings, Integrations**.

**In Perplexity**

5. Open **Settings** and find the **MCP servers** section.
6. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

7. Connect and approve the CorpusIQ authorization page once.
8. Start a new thread and ask a question about a document.

The authorization persists after the first approval, so the setup is one time.

### Example Perplexity Questions

**Contracts and terms**

- "What is the renewal date and notice period in the vendor agreement?"
- "Which contracts expire in the next 90 days?"
- "Does the Master Services Agreement allow subcontracting?"

**Documents and versions**

- "Which version of the pricing sheet is the current one?"
- "What changed between the two approved proposals?"
- "Find the deck where we described the Q3 roadmap."

**Operations**

- "What does the onboarding checklist say happens on day one?"
- "Summarize the open items in the client folder for Acme."

**Cross-source**

- "Do the payment terms in the contract match what is in the billing system?" (requires the billing connector)

### Security

- **Read scope only.** The connection requests Google's read-only scopes. There is no write path from Perplexity into Drive.
- **Account-scoped reach.** The connector can reach what the connected Google account can open, and nothing else. Files never shared with that account stay out of scope.
- **Revocable at any time.** Google Account, Security, Third-party access. Revoking there ends the connection.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Google, CorpusIQ, and Perplexity.

### Comparison: Drive Search vs Drive in Perplexity

| Aspect | Drive search | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | Keywords you guess | A question about the content |
| Output | A list of files to open | An answer with the file cited |
| Reading | You open each result | Read on demand, per question |
| Version comparison | Manual, side by side | Asked as one question |
| Combining sources | Copy between documents | Asked across connectors |
| Write access | Yes, by you | None, read-only scope |

Search is the right tool when you remember the filename. A connected Drive is the right tool when you remember the question.

### FAQ: Common Questions

<details>
<summary><strong>Is this read-only?</strong></summary>

Yes. The connection is read-only at the scope level, not by policy promise. There is no tool that writes to Drive.
</details>

<details>
<summary><strong>Can it see files that were shared with me but that I do not own?</strong></summary>

Access follows the Google account you authorized. If that account can open the file, the connector can read it. A link-restricted share keeps its restriction.
</details>

<details>
<summary><strong>Can it read PDFs and Word files, or only Google Docs?</strong></summary>

Drive holds mixed content. Text-based documents come through as text. Scanned images without a text layer are the usual failure case, because there is nothing to read.
</details>

<details>
<summary><strong>Does it copy my files into an index?</strong></summary>

No. Raw customer files and full connector response payloads are not retained. Retrieval happens on demand per question, and what the operational logs keep is bounded to query text and outcome summaries with a 30-day window.
</details>

<details>
<summary><strong>Will it search the whole Drive on every question?</strong></summary>

It searches within the scope of the connected account and the question. Narrow questions get tighter answers: naming the folder or the counterparty is usually enough.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. The same subscription exposes Drive to ChatGPT, Claude, and Perplexity through the same endpoint. Use whichever client you are already in.
</details>

<details>
<summary><strong>Where is the retrieved content stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Operational logs may persist for up to 30 days. See the [security documentation](/hermes/security/read-only-and-security).
</details>

---

**Next steps:** [Connect Google Drive to Perplexity now](https://corpusiq.io/connect/google-drive-with-perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
