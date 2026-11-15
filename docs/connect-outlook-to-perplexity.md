---
title: "Connect Outlook to Perplexity via MCP"
description: "Connect Outlook to Perplexity via CorpusIQ MCP. Ask what a client agreed to and which threads went unanswered, with cited answers from your own mailbox."
category: Perplexity Integrations
tags: ["connect Outlook to Perplexity", "Outlook Perplexity integration", "MCP Outlook connector", "Microsoft 365 data to AI", "ask Outlook in plain English", "CorpusIQ MCP"]
last_updated: "2026-11-15"
canonical: "https://www.corpusiq.io/docs/connect-outlook-to-perplexity"
robots: "index,follow"
---

# How to Connect Outlook to Perplexity with CorpusIQ MCP

The commitment a client made is in an email. So is the delivery date somebody moved, the invoice dispute nobody closed, and the reason the renewal slipped.

Perplexity can research the company you are about to meet. It cannot read the thread where that company told you what it actually needs.

Connecting Outlook through CorpusIQ MCP puts the mailbox and the outside record in one thread. Perplexity answers from your own messages, read-only, and names the message and the date it read.

### Why Connect Outlook to Perplexity?

- **Account history.** "Summarize my email history with this account, then tell me what changed at that company publicly this quarter."
- **Unanswered threads.** "Which client threads have gone more than five days without a reply from us?"
- **Commitments.** "What delivery dates did we commit to in writing this month?"
- **Disputes.** "Find every message about the invoice dispute and list what was agreed and what is still open."
- **Vendor terms.** "What renewal terms did the vendor propose, and how do they compare to standard terms in their category?"
- **Read-only by permission.** The retrieval tools documented on this page are read-only, and `Mail.Read` carries no write capability.

### How It Works

1. **Connect Outlook to CorpusIQ** through Microsoft OAuth 2.0 with delegated read permissions on Microsoft Graph.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ reads** the messages, folders and conversation threads that answer the question, as the signed-in user.
4. **Perplexity answers** with what was said, when, by whom, and the outside context you asked for around it.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational logs keep query text, per-user tool-call metadata and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Open your dashboard and go to **Connectors**.
2. Select **Outlook**, or **Microsoft 365** if OneDrive is already connected, and click **Connect**.
3. Sign in with your Microsoft account and review the requested permissions: `Mail.Read` and `Calendars.Read`.
4. Click **Accept**. You return to CorpusIQ and the card turns green.
5. The mailbox is now queryable as the account you approved with.

**In Perplexity**

6. Open **Settings** and find the **MCP servers** section.
7. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

8. Connect and approve the CorpusIQ authorization page once.
9. Start a new thread with "show me my Outlook folders" to confirm the mailbox is visible.

A tenant administrator may need to consent before the grant completes, depending on the organization's app policy. Answers follow the mailbox of the account that authorized, so the connection never reaches a mailbox nobody approved.

### Example Perplexity Questions

**Account and relationship**

- "Summarize my correspondence with this account this year, then tell me what they announced publicly last quarter."
- "When did we last hear from the procurement contact, and what did they ask for?"
- "How many threads with this customer are still open?"

**Commitments and risk**

- "What delivery dates did we commit to in writing this month, and which are now at risk?"
- "Which client threads have had no reply from us in more than five days?"
- "Find every email that mentions a discount and list the terms offered."

**Operations**

- "What spreadsheets were shared with me last week, and by whom?"
- "List PDF attachments from the legal team in the last 30 days."
- "Which messages about the compliance audit are unanswered?"

**Cross-source**

- "Do the delivery dates in email match the milestones in the project tracker?" (requires a project connector)
- "Which accounts that emailed about renewal also have an open opportunity in the CRM?" (requires a CRM connector)
- "Compare what was agreed by email with the invoices issued this quarter." (requires a finance connector)

### Security

- **Read-only retrieval tools.** The tools documented on this page are read-only. `Mail.Read` on Microsoft Graph grants no ability to send, delete, move or modify a message.
- **Your mailbox, your permissions.** Answers follow the delegated permission of the account that authorized, and the tenant's own policies apply on top.
- **No stored credentials on your side.** CorpusIQ holds the encrypted OAuth token; you hold the Microsoft grant and can revoke it from your account at any time.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text, tool-call metadata and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Microsoft Graph, CorpusIQ and Perplexity.

### Comparison: Outlook Search vs Outlook in Perplexity

| Aspect | Outlook search | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | A keyword or a sender | A question in plain language |
| Result | A list of messages to open | An answer drawn from the message bodies |
| Threads | You read the whole chain | Summarized, with decisions and open items |
| Outside context | Copy the thread into a search tab | Same thread, same answer |
| Cross-system | Export and join by hand | Asked across connectors |
| Write access | Yes, by your users | None through the retrieval tools |

Search returns the message. A connected mailbox answers the question the message was about.

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity send, delete or move an email?</strong></summary>

No. The retrieval tools documented on this page are read-only, and `Mail.Read` carries no write capability on Microsoft Graph.
</details>

<details>
<summary><strong>Which mailbox does it read?</strong></summary>

The mailbox of the account that approved the grant. Shared mailboxes and other users' folders are not reachable through that consent.
</details>

<details>
<summary><strong>Can it search one folder at a time?</strong></summary>

Yes. "Show me my Outlook folders" lists the structure, then a question can target one folder or search across all of them.
</details>

<details>
<summary><strong>Does it read attachments?</strong></summary>

Attachment metadata such as filename, type and size is available. Attachment contents are not parsed into answers, so an attachment's body is out of scope.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. Each question reads the current state of the mailbox, so a message received a minute ago appears in the next answer. Verify anything time-sensitive against the cited message.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. Outlook is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

<details>
<summary><strong>Where is the email data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Operational logs may persist for up to 30 days. See the [read-only and security documentation](/hermes/security/read-only-and-security).
</details>

---

**Next steps:** [Connect Outlook to Perplexity now](https://www.corpusiq.io/connectors/perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
