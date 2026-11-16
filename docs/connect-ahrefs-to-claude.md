---
title: "Connect Ahrefs to Claude via MCP - SEO Data in Conversation"
description: "Connect Ahrefs to Claude through CorpusIQ MCP. Ask for domain ratings, ranking keywords and referring domains without opening the dashboard."
category: Claude Integrations
tags: ["connect Ahrefs to Claude", "Ahrefs Claude integration", "MCP Ahrefs connector", "Ahrefs data to Claude", "AI for SEO research", "CorpusIQ MCP"]
last_updated: "2026-11-16"
canonical: https://www.corpusiq.io/docs/connect-ahrefs-to-claude
robots: index,follow
---

# How to Connect Ahrefs to Claude with CorpusIQ MCP

Ahrefs holds the clearest view of who ranks for what, but the work of reading it is manual. A competitive question turns into five tabs, three exports and a spreadsheet that is out of date by the time anyone opens it.

Connecting Ahrefs to Claude through CorpusIQ MCP makes the research conversational. Ask how two domains compare, and the answer names the referring domains and keywords behind the comparison.

### Why Connect Ahrefs to Claude?

- **Domain comparison in one answer.** Domain Rating, referring domains and organic traffic for several domains side by side.
- **Keyword footprint questions.** Which terms a domain ranks for in the top ten, with positions and volumes.
- **Backlink reading.** Live backlinks, referring domains and historical totals without the backlink explorer.
- **Competitor sizing.** Organic competitors and the pages earning their traffic, so content gaps are visible rather than inferred.
- **Demand checks.** Search volume, difficulty and CPC before a keyword decision, in the same thread as the content plan.
- **Read path only.** CorpusIQ reads Ahrefs data through its API and returns it to the conversation.

### How It Works

1. **Connect Ahrefs to CorpusIQ** using an API token from your Ahrefs account.
2. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your CorpusIQ account settings.
3. **CorpusIQ translates** your question into the Ahrefs API calls that answer it: domain overview, organic keywords, backlinks, referring domains or keyword research.
4. **Claude answers** from the returned data, naming the domain and metric each figure describes.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in to CorpusIQ and open **Connectors**.
2. Select **Ahrefs** and click Connect.
3. In a second tab, open Ahrefs **Settings, API** and copy your API token. API access requires an Advanced plan or higher.
4. Paste the token into the CorpusIQ form and save. Ahrefs turns from gray to green.
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

**Domain questions**

- "What is the Domain Rating for competitor.com?"
- "Compare Domain Rating and referring domains for our domain against our three closest competitors."
- "How much organic traffic does example.com get per month?"
- "Which of these four domains has the strongest backlink profile?"

**Keyword questions**

- "Which keywords does my domain rank for in the top 10?"
- "What is the search volume and CPC for enterprise CRM?"
- "Which high volume keywords do competitors rank for that we do not?"
- "List our quick win keywords: positions 11 to 20 with volume above 500."

**Backlink and content questions**

- "Show me the top referring domains linking to my site."
- "Which competitor pages earn the most organic traffic?"
- "Who are my top organic competitors?"
- "Has our referring domain count grown this quarter?"

### Security

- **Token-scoped access.** The API token carries the permissions of your Ahrefs account and the limits of your plan. Issue a token you can rotate on its own.
- **Read calls only.** The connection issues read calls for domain, keyword and backlink data. Your Ahrefs projects, alerts and saved reports are not modified.
- **Revocable at any time.** Delete the token in Ahrefs under Settings, API, and the connection stops working immediately.
- **Scoped direct-MCP retention.** CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Comparison: Ahrefs dashboards vs Ahrefs Through Claude

| Question | Ahrefs dashboard | CorpusIQ MCP with Claude |
|---|---|---|
| Input | A report and a domain picker | A question in plain language |
| Output | Tables and charts to read | A direct answer with the metrics behind it |
| Multi-domain comparison | Export and line up by hand | One comparison answer |
| Keyword gap analysis | Manual set arithmetic | Asked as a sentence |
| Write access | Project and report edits | None exposed to the assistant |

Ahrefs is where the data lives. Claude is where the question gets answered.

### FAQ: Common Questions

<details>
<summary><strong>Do I need a specific Ahrefs plan?</strong></summary>

API access requires an Advanced plan or higher. Without it the token is refused by Ahrefs and the connector cannot read data.
</details>

<details>
<summary><strong>Does every question spend API rows?</strong></summary>

Yes. Each question issues the API calls needed to answer it, so narrower questions cost less. CorpusIQ reads only what the question requires.
</details>

<details>
<summary><strong>Can Claude see keyword and backlink data for any domain?</strong></summary>

It can read whatever your Ahrefs plan entitles the token to read, including domains outside your own account, subject to your plan limits.
</details>

<details>
<summary><strong>Can Claude change my Ahrefs projects?</strong></summary>

No. The connection is read-only for the documented reports. Projects, alerts and saved reports stay untouched.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Ahrefs refreshes on its own crawl schedule, and CorpusIQ reads the data available when you ask. Very new domains can lag until Ahrefs indexes them.
</details>

<details>
<summary><strong>Can I use this for client reporting?</strong></summary>

Yes. The answers are drawn from the same account data you would export, with the domain and metric named so the source is checkable.
</details>

---

**Next steps:** [Connect Ahrefs to Claude now](https://www.corpusiq.io/docs/connectors/ahrefs)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
## See also

- [Connect Ahrefs to Perplexity](connect-ahrefs-to-perplexity.md) - domain ratings and keyword footprints inside a Perplexity thread.
- [Connect Ahrefs to ChatGPT](connect-ahrefs-to-chatgpt.md) - backlink and keyword research inside a ChatGPT thread.
- [Ahrefs connector reference](connectors/ahrefs.md) - connection requirements, visible data and troubleshooting.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
