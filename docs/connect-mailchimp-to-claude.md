---
title: "Connect Mailchimp to Claude via MCP - Campaign Answers"
description: "Connect Mailchimp to Claude through CorpusIQ MCP. Ask whether the newsletter moved revenue, not just opens, read-only from your live campaign data."
category: Claude Integrations
tags: ["connect Mailchimp to Claude", "Mailchimp Claude integration", "MCP Mailchimp connector", "campaign performance in Claude", "email marketing analytics", "CorpusIQ MCP"]
last_updated: "2026-10-29"
canonical: "https://www.corpusiq.io/docs/connect-mailchimp-to-claude"
robots: "index,follow"
---

# How to Connect Mailchimp to Claude with CorpusIQ MCP

Email marketing reports answer the easy question. Open rate, click rate, unsubscribes. They do not answer the one the business actually has: did this campaign make money?

That answer lives across Mailchimp and whatever holds the orders. Connecting Mailchimp through CorpusIQ MCP puts the campaign record in the same conversation as the revenue record, so the question can be asked once.

### Why Connect Mailchimp to Claude?

- **Campaign to revenue.** "Which campaign drove the most orders in the last quarter?" (with the commerce connector)
- **Audience movement.** "How did the list grow last month, and which signup source contributed most?"
- **Segment performance.** "Which segment has the highest click rate across the last ten campaigns?"
- **Content learning.** "What subject lines performed best, and what do the winners have in common?"
- **Churn signals.** "Which subscribers stopped opening in the last 60 days?"
- **Read-only by scope.** The connection reads campaigns, audiences, and reports. It cannot send, edit, or change a list.

### How It Works

1. **Connect Mailchimp to CorpusIQ** with a read-only API key or OAuth, whichever your account supports.
2. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your CorpusIQ account settings.
3. **CorpusIQ queries** campaigns, reports, audiences, and segments as the question requires.
4. **Claude answers** from that retrieved content, with the campaigns it used.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connectors**.
2. Select **Mailchimp**.
3. Authorize the connection with a read-only key, or through OAuth if your Mailchimp plan supports it.
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

**Campaign performance**

- "Compare the last five campaigns on click rate and revenue per recipient."
- "Which campaign had the highest unsubscribe rate, and what was different about it?"
- "How did the last send perform against the previous one?"

**Audience and growth**

- "How did the audience grow last month, by source?"
- "Which segment has the highest engagement over the last ten sends?"
- "Which subscribers have not opened anything in 60 days?"

**Content learning**

- "What subject lines got the best open rate this quarter?"
- "Which send day performs better, Tuesday or Thursday?"
- "List the campaigns that mentioned a discount and compare their click rates."

**Cross-source**

- "Which campaign drove the most orders in the last quarter?" (requires the commerce connector)
- "Did the audience that clicked the launch email convert into paying customers?" (requires billing or CRM)

### Security

- **Read scope only.** The connection reads campaigns and reports. Claude cannot send a campaign, edit a list, or change automation.
- **Revocable at any time.** Mailchimp, Account, Extras, API keys. Revoking the key ends the connection.
- **Scoped to the authorized account.** Access follows the Mailchimp account or key you approve, and nothing outside it is reachable.
- **Scoped direct-MCP retention.** Direct MCP retrieval is read-only. Raw customer files and full connector payloads are not retained. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Mailchimp, CorpusIQ, and Claude.

### Comparison: Mailchimp Reports vs Mailchimp Through Claude

| Aspect | The Mailchimp report | CorpusIQ MCP with Claude |
|---|---|---|
| Input | Pick a campaign and a date range | A question across campaigns |
| Output | Charts and tables | An answer with the campaigns named |
| Revenue | A separate system | Asked beside order data |
| Trend work | Export and build a sheet | Asked across a quarter |
| Comparison | One campaign at a time | Ranked across many |
| Write access | Yes, by you | None, read-only |

The Mailchimp report is the right tool when you want this campaign's numbers. Claude is the right tool when you want to know which campaigns actually worked.

### FAQ: Common Questions

<details>
<summary><strong>Can Claude send a campaign through this connection?</strong></summary>

No. The connection is read-only. Claude reads campaigns, audiences, segments, and reports. Sending, editing, and automation changes are not available.
</details>

<details>
<summary><strong>Which Mailchimp plans does this work with?</strong></summary>

The connector uses Mailchimp's API, which is available across their paid plans. Some reporting detail depends on what your plan exposes, so the answer is limited to the data your account can already show you in the Mailchimp interface.
</details>

<details>
<summary><strong>Does it read subscribers, including personal data?</strong></summary>

It can read audience and segment data, which includes subscriber records. That is why the scope is read-only and revocable, and why the connector should be authorized on an account whose data you are allowed to query. Retrieval is on demand, with no warehouse of subscriber records behind it.
</details>

<details>
<summary><strong>Can it compare campaigns with revenue?</strong></summary>

Yes, once a commerce or billing connector is also connected. "Which campaign drove the most orders last quarter" is one question across Mailchimp and the order system, instead of an export and a manual match.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. Campaign reports are read at the moment you ask. A send from this morning is visible to the next question, though some Mailchimp metrics settle over the first day.
</details>

<details>
<summary><strong>Does it cover automations and journeys?</strong></summary>

Campaign and audience reporting is the core of this connector. Ask a question that names an automation or a journey and see whether the returned answer is scoped to it. If it is not, the answer will say what it did read rather than guessing.
</details>

<details>
<summary><strong>Where is my marketing data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Retrieval happens on demand. Operational logs may persist for up to 30 days. See the [security documentation](../security/) for detail.
</details>

---

**Next steps:** [Connect Mailchimp to Claude now](https://corpusiq.io/connect/mailchimp-with-claude)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
