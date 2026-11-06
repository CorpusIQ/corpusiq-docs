---
title: "Connect Gmail to Perplexity via MCP"
description: "Connect Gmail to Perplexity through CorpusIQ MCP. Ask which threads carry a commitment, what a vendor actually agreed and what is still unanswered."
category: Perplexity Integrations
tags: ["connect Gmail to Perplexity", "Gmail Perplexity integration", "MCP Gmail connector", "search Gmail in Perplexity", "CorpusIQ MCP"]
last_updated: "2026-11-06"
canonical: "https://www.corpusiq.io/docs/connect-gmail-to-perplexity"
robots: "index,follow"
---

# How to Connect Gmail to Perplexity with CorpusIQ MCP

A Perplexity thread is good at the public record. It is blind to the part of the record that arrived by email: the price change a supplier mentioned on a Tuesday, the delivery date a customer agreed to, the clause nobody put in the contract.

Connecting Gmail through CorpusIQ MCP puts your own correspondence inside the same thread, read-only. You ask a question, Perplexity reads the messages that answer it, and the answer names the threads it used.

### Why Connect Gmail to Perplexity?

- **The internal half of a research question.** "What did this supplier tell us about lead times before the shortage was public?" needs your mailbox and the web in one answer.
- **Commitments, not keywords.** Gmail search returns messages that match words. It will not tell you which promise is still open.
- **Across threads.** A single deal usually spans four conversations with three domains. The question is about the deal, not about one thread.
- **Numbers buried in prose.** Amounts, dates and quantities sit inside sentences. Asked properly, they come back as a list.
- **Read-only by scope.** The connector holds `gmail.readonly`. There is no send, delete or relabel path from either assistant.
- **Silence is an answer.** "Which customers have not replied since the quote?" is a question about what is missing, and it is answerable here.

### How It Works

1. **Connect Gmail to CorpusIQ** with Google OAuth, approving the read-only Gmail scope. The same connection can cover Google Calendar, Drive and Sheets if you want them in the same thread.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ turns the question into Gmail searches**, pulls the matching messages and threads, and decodes the bodies.
4. **Perplexity answers** from what came back, and names the period and the threads it measured.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational query logs are kept for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Sign in and open **Connectors**.
2. Select **Gmail**, or **Google Workspace** if you want Calendar, Drive and Sheets alongside it.
3. Sign in to Google with the account that holds the mailbox, and approve read access.

**In Perplexity**

4. Open **Settings** and find the **MCP servers** section.
5. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

6. Connect, then approve the CorpusIQ authorization page once.
7. Open a new thread and ask an inbox question.

Two things decide whether the first question works. The Google account you signed in with must be the one that owns the messages, and the thread has to be new: Perplexity resolves the server's tools when a thread starts, so a thread already open keeps the tools it had.

### Example Perplexity Questions

**Commitments**

- "What delivery dates did we promise customers this quarter, and which have passed?"
- "Find the last thing we told this supplier about volumes."
- "Which threads mention a refund and what did we agree to?"

**Money**

- "List every invoice amount mentioned in email this month, with the sender."
- "Which customer asked for a discount and did we agree?"
- "Compare the price in this supplier's latest email against what we paid last quarter."

**Silence**

- "Which quotes are still unanswered after fourteen days?"
- "Who have we emailed three times without an answer?"
- "Which customers have gone quiet since the price change?"

**Research paired with the web**

- "What did this vendor tell us privately, and what have they said publicly since?" (Perplexity searches the web in the same thread)
- "Summarise our email history with this domain, then check whether the company was acquired."

**Cross-source**

- "Which companies in these threads are also open deals in our CRM?" (requires the HubSpot connector)
- "Which senders are also customers in Stripe?" (requires the Stripe connector)

### Security

- **Read scope only.** The connection carries `gmail.readonly`. No tool in this connector sends, deletes, archives or relabels a message.
- **Revocable from Google.** Removing CorpusIQ's access in your Google account ends the connection immediately, and reconnecting needs a fresh approval.
- **Account-scoped.** Access follows the Google account you approved. A mailbox you have not connected is not reachable.
- **Scoped retention.** Raw customer files and full connector response payloads are not retained. Operational logs keep query text, per-user tool-call metadata and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Google, CorpusIQ and Perplexity.

### Comparison: Gmail Search vs Gmail Inside a Perplexity Thread

| Aspect | Gmail search | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | Keywords and operators | A question, in plain words |
| Output | A list of messages to open | An answer that names the threads |
| Across threads | One search at a time | One question across many |
| Cross-source | Export and reconcile by hand | Asked alongside other connectors |
| Missing information | Not searchable | Askable, e.g. who has not replied |
| Write access | Full, by you | None, read scope only |

Search is built for finding a message you already know exists. This is built for the question you cannot phrase as a search.

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity send an email on my behalf?</strong></summary>

No. The connection is read-only, and no tool in the Gmail connector can send, delete or change a label.
</details>

<details>
<summary><strong>Does this read my whole mailbox?</strong></summary>

It can read anything the approved Google account can read, because that is what the scope means. It reads only what a question requires. Raw customer files and full connector response payloads are not retained; operational logs are kept for up to 30 days.
</details>

<details>
<summary><strong>Why does it find nothing when Gmail search does?</strong></summary>

Two usual causes. The question was phrased as a search instead of a question, or the Search Console style operators people type into Gmail do not translate. Ask for the thing you want to know, not the words you would type.
</details>

<details>
<summary><strong>Can it read attachments?</strong></summary>

It reads attachment metadata and the text of common document and spreadsheet formats. A scanned PDF with no text layer comes back as a file reference, not as content.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. Gmail is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

<details>
<summary><strong>Where is the email data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Operational logs may persist for up to 30 days. See the [security documentation](/hermes/security/read-only-and-security).
</details>

---

**Next steps:** [See the connectors CorpusIQ supports](https://www.corpusiq.io/connectors)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
