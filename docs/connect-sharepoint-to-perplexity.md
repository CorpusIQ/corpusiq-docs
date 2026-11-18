---
title: "Connect SharePoint to Perplexity via MCP"
description: "Connect SharePoint to Perplexity through CorpusIQ MCP. Ask what a policy or a board deck says across your site libraries, read-only and cited."
category: Perplexity Integrations
tags: ["connect SharePoint to Perplexity", "SharePoint Perplexity integration", "MCP SharePoint connector", "SharePoint documents to AI", "ask SharePoint in plain English", "CorpusIQ MCP"]
last_updated: "2026-11-18"
canonical: "https://www.corpusiq.io/docs/connect-sharepoint-to-perplexity"
robots: "index,follow"
---

# How to Connect SharePoint to Perplexity with CorpusIQ MCP

SharePoint holds the documents a company runs on: policies, board decks, statements of work, close packs, security questionnaires. Finding one is a folder drill or a search box that matches file names and snippets, not meaning.

The harder question is never where the file is. It is what the file says, and whether it still agrees with the one written six months later.

Connecting SharePoint through CorpusIQ MCP puts the library behind a question. Perplexity reads the documents the connection can open, read-only, and names what it read.

### Why Connect SharePoint to Perplexity?

- **Policy questions.** "What does our data retention policy say about customer PII, and which clause covers deletion on request?"
- **Deck and memo recall.** "Find the Q3 close presentation and summarise the variance commentary."
- **Version drift.** "Which security questionnaire answers no longer match the current policy?"
- **Coverage checks.** "Which sites have an incident response plan, and which do not?"
- **Cross-system context.** "Do the figures in this close pack reconcile with the same period in the accounting system?"
- **Read-only by capability.** The retrieval tools documented on this page are read-only, and the Microsoft grant carries `Sites.Read.All` and `Files.Read.All`.

### How It Works

1. **Connect SharePoint to CorpusIQ** with a Microsoft OAuth grant for your tenant. The consent screen names the two permissions it requests, `Sites.Read.All` and `Files.Read.All`, before you approve anything.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ reads** the sites and documents the grant reaches, and returns the passages that answer the question.
4. **Perplexity answers** with the document named, next to the outside context it already provides.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational logs keep query text, per-user tool-call metadata and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Navigate to **Connectors**.
2. Select **SharePoint**, under the Microsoft 365 integrations.
3. Click **Connect SharePoint** and authorise through Microsoft OAuth.
4. Review the permissions it requests: `Sites.Read.All` and `Files.Read.All`, both read-only, covering SharePoint sites and files.

**In Perplexity**

5. Open **Settings** and find the **MCP servers** section.
6. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

7. Connect and approve the CorpusIQ authorization page once. Then start a new thread and name a site, a document or a policy.

Organisations running Conditional Access policies can route the grant through a Microsoft Entra ID administrative consent workflow, so the tenant's own policy decides what is approved before anything is read.

### Example Perplexity Questions

**Policies and compliance**

- "What does our data retention policy say about customer PII?"
- "Which policy documents were not reviewed in the last twelve months?"
- "Summarise the incident response plan and list the steps with named owners."

**Finance and board material**

- "Find the Q3 close presentation and summarise the variance commentary."
- "Which board pack figures differ from the previous quarter, and by how much?"
- "List the documents in the finance site updated since the last close."

**Sales and legal**

- "Find the current MSA template and list the clauses a customer most often redlines."
- "Which statements of work expire this quarter?"
- "What does the security questionnaire say about subprocessors?"

**Cross-source**

- "Do the figures in this close pack reconcile with the same period in QuickBooks?" (requires a finance connector)
- "Which contracts in the CRM have a matching document in SharePoint?" (requires a CRM connector)
- "Compare the headcount plan document with the people data in the sheet." (requires Google Sheets)

### Security

- **Read-only permissions.** The connection requests `Sites.Read.All` and `Files.Read.All`, both read-only, and the retrieval tools documented on this page only read.
- **Tenant consent.** Conditional Access organisations can require Microsoft Entra ID administrative consent before the grant becomes active.
- **No stored credentials on your side.** CorpusIQ holds the encrypted Microsoft grant; a tenant administrator can revoke it in Entra ID, and revocation takes effect on the next call.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text, tool-call metadata and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Microsoft 365, CorpusIQ and Perplexity.

### Comparison: SharePoint search and folder navigation

| Aspect | SharePoint search and folder navigation | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | A file name, a phrase, or a folder path | A question about the content |
| Scope | One site or library at a time | Every site the grant reaches |
| Reading | Open each document yourself | Passages returned across documents |
| Outside context | Open a second tab | Same thread, same answer |
| Cross-system | Copy content out by hand | Asked across connectors |
| Write access | Yes, by your users | None through the retrieval tools |

Search returns files. The answer needs the parts of them that matter.

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity edit or upload a SharePoint document?</strong></summary>

No. The grant carries `Sites.Read.All` and `Files.Read.All`, and the retrieval tools documented on this page only read. Libraries, permissions and versions are untouched.
</details>

<details>
<summary><strong>Which sites can it reach?</strong></summary>

The ones the Microsoft grant covers. A tenant administrator approves or restricts that scope, and Conditional Access organisations can require explicit admin consent first.
</details>

<details>
<summary><strong>Does it read inside PDFs and Office files?</strong></summary>

Yes. Document content is read, not just file names and metadata.
</details>

<details>
<summary><strong>Does it respect SharePoint permissions per user?</strong></summary>

The connection reads with the grant it was given, which is a tenant or account-level authorisation. Review the permissions on the consent screen before approving.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. Each question reads the current version of the document, so an edit made a minute ago appears in the next answer.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. SharePoint is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

### See Also

- [Connect SharePoint to ChatGPT](connect-sharepoint-to-chatgpt.md) - the same document questions, asked from ChatGPT
- [Connect SharePoint to Claude](connect-sharepoint-to-claude.md) - the same questions with the Claude Desktop config block
- [Connect Google Drive to Perplexity](connect-google-drive-to-perplexity.md) - the same reading pattern on a drive-based library

---

**Next steps:** [Add CorpusIQ to Perplexity now](https://www.corpusiq.io/connectors/perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
