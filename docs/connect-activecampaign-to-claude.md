---
title: "Connect ActiveCampaign to Claude via MCP - Lists and Deals"
description: "Connect ActiveCampaign to Claude through CorpusIQ MCP. Ask about list health, campaign performance and pipeline deals in plain language."
category: Claude Integrations
tags: ["connect ActiveCampaign to Claude", "ActiveCampaign Claude integration", "MCP ActiveCampaign connector", "ActiveCampaign data to Claude", "AI for email marketing", "CorpusIQ MCP"]
last_updated: "2026-11-16"
canonical: https://www.corpusiq.io/docs/connect-activecampaign-to-claude
robots: index,follow
---

# How to Connect ActiveCampaign to Claude with CorpusIQ MCP

ActiveCampaign knows which contacts open, which automations fire, and which deals are sitting still. What it does not do is answer a question that spans all three. Reporting lives behind a builder, and the answer you usually want needs a contact list joined to campaign performance joined to pipeline stage.

Connecting ActiveCampaign to Claude through CorpusIQ MCP puts that join in a sentence. You ask, Claude reads the records that answer it, and the reply names the campaigns, lists and deals behind the number.

### Why Connect ActiveCampaign to Claude?

- **List health in one question.** Contact counts, engagement and which tags are actually in use, without building a segment first.
- **Campaign performance read across sends.** "How did the last three newsletters compare" returns a comparison, not three screenshots.
- **Automation load.** See which automations carry the most active contacts, and which ones have quietly stopped mattering.
- **Pipeline context beside email history.** Deals sit in the same connector as the sequences that produced them, so a stalled deal can be traced to the last automation a contact finished.
- **Cross-source joins.** Pair contact and campaign data with orders, revenue or site analytics in the same conversation.
- **Read path only.** The connection uses an API key with read permissions. Claude searches and reads. It does not send mail.

### How It Works

1. **Connect ActiveCampaign to CorpusIQ** using your API URL and API key from Settings, Developer.
2. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your CorpusIQ account settings.
3. **CorpusIQ translates** your question into ActiveCampaign API calls, retrieves the matching contacts, campaigns, automations and deals, and assembles the records.
4. **Claude answers** from that retrieved content, naming the campaigns and lists behind each figure.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in to CorpusIQ and open **Connectors**.
2. Select **ActiveCampaign** and click Connect.
3. In a second tab, sign in to ActiveCampaign and open **Settings, Developer**.
4. Copy your **API URL** and **API key**.
5. Paste both into the CorpusIQ form and save. ActiveCampaign turns from gray to green.
6. Copy the MCP config block under **Settings, Integrations, Claude Desktop**.

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

**List and contact questions**

- "How many contacts are on each of my ActiveCampaign lists?"
- "Which tags have more than 500 contacts on them?"
- "Show me contacts added in the last 30 days and which list each one landed on."
- "Which contacts have not opened anything in 90 days?"

**Campaign questions**

- "How did my last campaign perform?"
- "Compare open and click rates across my last four newsletters."
- "Which campaign drove the most clicks per recipient?"
- "List campaigns sent this quarter with subject lines and send dates."

**Automation and pipeline questions**

- "Which automations have the most active contacts?"
- "Which automation has the lowest completion rate?"
- "Show me deals that have been open longer than 30 days."
- "What is the total value of deals in each pipeline stage?"

### Security

- **Key-scoped access.** ActiveCampaign issues the API key, and the permissions attached to that key bound what Claude can read. Issue a dedicated key if you want this connection isolated from your other integrations.
- **Read path only.** CorpusIQ reads contacts, lists, campaigns, automations and deals. No send, edit or automation-toggle path is exposed to the assistant.
- **Revocable at any time.** Rotate or delete the key in ActiveCampaign under Settings, Developer, and the connection stops working immediately.
- **Scoped direct-MCP retention.** CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Comparison: ActiveCampaign reporting vs ActiveCampaign Through Claude

| Question | ActiveCampaign reports | CorpusIQ MCP with Claude |
|---|---|---|
| Input | A report builder and segment filters | A question in plain language |
| Contacts plus campaign | Two exports and a spreadsheet join | One answer |
| Automation comparison | One automation at a time | A ranked list across automations |
| Deals in email context | A separate pipeline view | Same conversation as the email history |
| Write access | Full account access in the UI | None exposed to the assistant |

ActiveCampaign reporting tells you what happened in one corner of the account. Claude answers questions that cross corners.

### FAQ: Common Questions

<details>
<summary><strong>Can Claude send or schedule email through this connection?</strong></summary>

No. The API key is used for read calls only. Campaigns are read as records, and there is no send, schedule or draft path reachable from the assistant.
</details>

<details>
<summary><strong>Can Claude edit contacts, tags or automations?</strong></summary>

No. CorpusIQ exposes no write tools for ActiveCampaign. Contact edits, tag changes and automation changes stay in ActiveCampaign.
</details>

<details>
<summary><strong>Does this include deal and pipeline data?</strong></summary>

Yes. Deals, their values, stages and open dates are available alongside contacts and campaigns, so email activity and pipeline movement can be read together.
</details>

<details>
<summary><strong>Which API key should I use for this?</strong></summary>

A key you can rotate without breaking other integrations. ActiveCampaign lets you issue keys under Settings, Developer, so a dedicated key keeps this connection isolated.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Every question is answered against the account at the moment you ask. There is no nightly copy of contacts or campaigns behind the answers.
</details>

<details>
<summary><strong>Can I restrict what the connection sees?</strong></summary>

The key inherits the permissions of the user who created it. Scope it by issuing the key from an account limited to the lists and pipelines you want visible.
</details>

---

**Next steps:** [Connect ActiveCampaign to Claude now](https://www.corpusiq.io/docs/connectors/activecampaign)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
## See also

- [Connect ActiveCampaign to Perplexity](connect-activecampaign-to-perplexity.md) - contacts, campaigns and pipeline read from the same account inside a Perplexity thread.
- [Connect ActiveCampaign to ChatGPT](connect-activecampaign-to-chatgpt.md) - list health and automation questions answered inside a ChatGPT thread.
- [ActiveCampaign connector reference](connectors/activecampaign.md) - connection requirements, visible objects and troubleshooting.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
