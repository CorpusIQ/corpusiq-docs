---
title: "Connect Klaviyo to Claude via MCP - Email Revenue"
description: "Connect Klaviyo to Claude through CorpusIQ MCP. Ask about flows, campaigns, abandoned carts and list growth in plain English, read-only."
last_updated: "2026-11-07"
---

# How to Connect Klaviyo to Claude with CorpusIQ MCP

Klaviyo holds the email and SMS revenue for the store, plus the flows, campaigns, and segments that produced it. Reading it usually means opening one report at a time and holding the numbers in your head until the next report loads.

Connecting Klaviyo through CorpusIQ MCP puts campaigns, flows, abandoned cart recovery, list growth, and subscriber health in the same conversation as the commerce platform and the ad accounts. You ask, Claude reads the account as it stands, and the answer names the report it used.

### Why Connect Klaviyo to Claude?

- **Flow questions.** "Which flows generated the most revenue in the last 30 days, and what is each one's revenue per recipient?"
- **Campaign questions.** "How did this month's campaigns compare with the same month last year?"
- **Recovery questions.** "What is our abandoned cart recovery rate, and how has it moved this quarter?"
- **List questions.** "How fast is the list growing, and what share of new subscribers came from popups versus checkout?"
- **Deliverability questions.** "Which segments carry the highest unsubscribe rate right now?"
- **Read-only by key.** The private API key reads. It cannot send a campaign, edit a flow, or modify a profile.

### How It Works

1. **Create a Klaviyo private API key** with read scopes on the objects you want visible.
2. **Connect Klaviyo to CorpusIQ** with that key. Anything the key cannot reach is invisible to the connector.
3. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your account settings.
4. **CorpusIQ queries Klaviyo**: campaigns and their metrics, flows and flow performance, abandoned cart data, lists and segments, subscription health, forms, and predictive analytics.
5. **Claude answers** from those results, naming the window and the metric it used.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In Klaviyo**

1. Open **Account**, then **Settings**, then **API keys**, and create a private API key for this purpose. Do not reuse the key your storefront integration already uses.
2. Tick read scopes on Campaigns, Flows, Lists, Segments, Profiles, Metrics, Forms, and Events. Anything left unticked is unreachable.
3. Copy the key.

**In CorpusIQ**

4. Log in and open **Connections**.
5. Select **Klaviyo** and paste the private API key.
6. Copy the MCP config block shown under **Settings, Integrations, Claude Desktop**.

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
11. Verify with "how much revenue did my flows generate last month". If the figure matches the Klaviyo dashboard, the key is working.

If the tools indicator does not appear, work through [Claude can't see CorpusIQ](../troubleshooting/claude-cant-see-corpusiq.md) before changing anything else.

### Example Claude Questions

**Flows and automation**

- "Which flows generated the most revenue in the last 30 days, and what is each one's revenue per recipient?"
- "How is the abandoned cart flow performing this quarter against last quarter?"
- "Which flows have not sent to anyone in 60 days?"

**Campaigns**

- "How did this month's campaigns compare with the same month last year?"
- "Which campaign subject lines performed best by open rate?"
- "Show revenue attributed to email versus SMS this month."

**List and health**

- "How fast is the list growing, and what share of new subscribers came from popups versus checkout?"
- "Which segments carry the highest unsubscribe rate?"
- "How many profiles are suppressed or bounced right now?"

**Cross-source**

- "Does Shopify revenue match what Klaviyo attributes to email for the same period?" (requires the Shopify connector)
- "Is our Meta spend producing subscribers who later buy, or just subscribers?" (requires the Meta connector)
- "How does email revenue compare with paid channel revenue over the last 90 days?" (requires the ads connectors)

### Security

- **Read-only key.** The connector reads campaigns, flows, lists, segments, profiles, metrics, forms, and events. It cannot send a campaign, edit a flow, or modify a profile.
- **Scoped by key.** What the private API key cannot reach, the connector cannot answer from. Create a key for this purpose rather than reusing the storefront key.
- **Revocable immediately.** Delete the key in Klaviyo under **Account, Settings, API keys** and access ends at once.
- **Scoped direct-MCP retention.** Direct MCP retrieval is read-only. Raw customer files and full connector payloads are not retained. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Klaviyo, CorpusIQ, and Claude.

### Comparison: The Klaviyo UI vs Klaviyo Through Claude

| Aspect | Klaviyo interface | CorpusIQ MCP with Claude |
|---|---|---|
| Input | A report you pick from a menu | A question, with the window stated |
| Output | A chart to read | A number plus the metric behind it |
| Flows vs campaigns | Two separate reports | One question across both |
| Across sources | Export, then reconcile | Asked across connectors |
| New question | Build another report | Ask again |
| Write access | Yes, by you | None, read-only key |

Klaviyo is the right place to build and send. Claude is the right place for the question that compares email revenue against the orders that actually booked.

### FAQ: Common Questions

<details>
<summary><strong>Is this read-only?</strong></summary>

Yes. The connector reads campaigns, flows, abandoned cart data, lists, segments, profiles, metrics, forms, and events. It cannot send a campaign, edit a flow, or modify a subscriber profile.
</details>

<details>
<summary><strong>How does the connection authenticate?</strong></summary>

With a Klaviyo private API key you create, carrying read scopes on the objects you want answerable. Anything the key cannot reach is invisible, and deleting the key in Klaviyo ends access immediately.
</details>

<details>
<summary><strong>Does it cover SMS as well as email?</strong></summary>

Yes. Campaign and flow performance covers both channels, so revenue attributed to email and to SMS can be compared in a single answer.
</details>

<details>
<summary><strong>Do I need a particular Klaviyo plan?</strong></summary>

You need an account with API access and the permission level required to create a private key with read scopes. Predictive analytics such as CLV and churn risk need enough order history, so a new account may show them empty for weeks.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. The connector queries Klaviyo when you ask, so a campaign that finished an hour ago is reflected in the next question. There is no overnight refresh in between.
</details>

<details>
<summary><strong>Can Claude change a flow or pause a campaign?</strong></summary>

No. Sending, editing, and pausing all stay in Klaviyo. The connection is a read path, so the worst case is a wrong answer rather than a wrong send.
</details>

<details>
<summary><strong>Why connect email data to Claude at all?</strong></summary>

Because the question that matters is rarely about email alone. "Does Klaviyo revenue match what Shopify booked" and "do email subscribers buy again" both need a second system in the same answer.
</details>

---

**Next steps:** [Connect Klaviyo to Claude now](https://corpusiq.io/connect/klaviyo-with-claude)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
