---
title: "Connect Semrush to Claude via MCP - Keyword and Backlink Q&A"
description: "Connect Semrush to Claude through CorpusIQ MCP. Compare keyword footprints, backlink profiles and organic competitors inside one thread."
category: Claude Integrations
tags: ["connect Semrush to Claude", "Semrush Claude integration", "MCP Semrush connector", "Semrush data to Claude", "AI for competitor research", "CorpusIQ MCP"]
last_updated: "2026-11-16"
canonical: https://www.corpusiq.io/docs/connect-semrush-to-claude
robots: index,follow
---

# How to Connect Semrush to Claude with CorpusIQ MCP

Semrush answers a lot of questions well, one report at a time. The moment a question spans two domains, or two periods, or search data beside paid data, the work moves into a spreadsheet.

Connecting Semrush to Claude through CorpusIQ MCP keeps that work in the conversation. Ask where a competitor gained organic ground, and the answer names the keyword sets and referring domains that explain it.

### Why Connect Semrush to Claude?

- **Competitive keyword read.** Which terms competitors rank for, at which positions, with the volumes behind them.
- **Backlink profile comparison.** Referring domains and total backlinks for several domains in one answer.
- **Organic movement.** Where a domain is gaining or losing visibility, read as a list rather than a chart.
- **Demand sizing.** Search volume and CPC pulled into the same thread as the content or campaign decision.
- **Cross-source joins.** Search data beside revenue, pipeline or site analytics from other connectors.
- **Read path only.** CorpusIQ reads Semrush reports through the API and returns the rows to the conversation.

### How It Works

1. **Connect Semrush to CorpusIQ** using your Semrush API key.
2. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your CorpusIQ account settings.
3. **CorpusIQ translates** your question into the Semrush API reports that answer it, then assembles the returned rows.
4. **Claude answers** from that data, naming the domain, keyword and period each figure describes.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in to CorpusIQ and open **Connectors**.
2. Select **Semrush** and click Connect.
3. In Semrush, open **Settings, API** and copy your API key. The API requires the Business plan or higher, and each call spends API units.
4. Paste the key into the CorpusIQ form and save. Semrush turns from gray to green.
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

**Competitive questions**

- "Which keywords does competitor.com rank for that we do not?"
- "Compare keyword footprints for our domain and our two main competitors."
- "Who are our top organic competitors?"
- "Which competitor gained the most organic visibility this quarter?"

**Backlink questions**

- "How does my backlink profile compare to competitor.com?"
- "How many referring domains point at our site?"
- "Which referring domains link to two or more of our competitors?"
- "Has our referring domain count grown in the last 90 days?"

**Demand questions**

- "What is the search volume and CPC for enterprise CRM?"
- "Which of these ten keywords have the lowest difficulty above 1,000 volume?"
- "What does paid search demand look like for project management software?"
- "Which keywords do we rank for between positions 11 and 30?"

### Security

- **Key-scoped access.** The Semrush API key carries your plan entitlements and spends your API units. Issue a key you can rotate on its own.
- **Read reports only.** The connection issues read calls for analytics reports. Your Semrush projects, campaigns and position tracking are not modified.
- **Revocable at any time.** Regenerate the key in Semrush under Settings, API, and the connection stops working immediately.
- **Scoped direct-MCP retention.** CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Comparison: Semrush reports vs Semrush Through Claude

| Question | Semrush reports | CorpusIQ MCP with Claude |
|---|---|---|
| Input | A report and a domain field | A question in plain language |
| Output | Tables and charts | A direct answer with the metrics named |
| Multi-domain comparison | One domain at a time | Side by side in one answer |
| Keyword gap | Manual export and subtraction | Asked as a sentence |
| Unit spend | Per report, visible in the UI | Per question, as narrow as you make it |

Semrush gives you the reports. Claude turns them into answers, and only spends units on the reports a question needs.

### FAQ: Common Questions

<details>
<summary><strong>Which Semrush plan do I need?</strong></summary>

API access requires the Business plan or higher. On lower plans the key is rejected at the Semrush layer, not by CorpusIQ.
</details>

<details>
<summary><strong>Do questions consume API units?</strong></summary>

Yes. Every question issues the API calls needed to answer it, and Semrush bills those in units. Narrower questions spend less.
</details>

<details>
<summary><strong>Can Claude modify my Semrush projects?</strong></summary>

No. The connection reads report data only. Projects, campaigns and position tracking are untouched.
</details>

<details>
<summary><strong>Why does a domain show no data?</strong></summary>

Semrush data lags reality, so a very new domain can be missing until it is indexed. A domain with no data is reported as no data rather than zero.
</details>

<details>
<summary><strong>Can I compare several competitors in one question?</strong></summary>

Yes. Multi-domain comparisons are answered in a single response, which is where the export work usually disappears.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

CorpusIQ reads Semrush data as it stands when you ask. Database refresh timing is Semrush's own schedule, not a CorpusIQ cache.
</details>

---

**Next steps:** [Connect Semrush to Claude now](https://www.corpusiq.io/docs/connectors/semrush)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
## See also

- [Connect Semrush to Perplexity](connect-semrush-to-perplexity.md) - competitor keywords and backlinks inside a Perplexity thread.
- [Connect Semrush to ChatGPT](connect-semrush-to-chatgpt.md) - search demand and competitor research inside a ChatGPT thread.
- [Semrush connector reference](connectors/semrush.md) - connection requirements, visible data and troubleshooting.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
