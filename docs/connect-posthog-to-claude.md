---
title: "Connect PostHog to Claude via MCP - Ask Product Analytics"
description: "Connect PostHog to Claude through CorpusIQ MCP. Ask about events, funnels, person records and HogQL, then join product usage to revenue and the CRM."
category: Claude Integrations
tags: ["connect PostHog to Claude", "PostHog Claude integration", "MCP product analytics connector", "product analytics in Claude", "HogQL questions", "CorpusIQ MCP"]
last_updated: "2026-10-30"
canonical: "https://www.corpusiq.io/docs/connect-posthog-to-claude"
robots: "index,follow"
---

# How to Connect PostHog to Claude with CorpusIQ MCP

PostHog answers the product question. The revenue question needs the same facts next to the CRM, the billing system, and the support desk, and that is where the answer usually stops.

Connecting PostHog through CorpusIQ MCP puts events, funnels, person records, and HogQL in the same conversation as everything else you run the business on. You ask, Claude reads the project as it stands, and the answer names the events it counted.

### Why Connect PostHog to Claude?

- **Funnel questions.** "How many users completed onboarding this week, and where do the rest stop?"
- **Activation questions.** "What is the conversion rate from signup to first data source connected?"
- **Live behaviour.** "Which events fired most in the last 24 hours?"
- **Segment questions.** "Which accounts from last month's cohort are still active today?"
- **HogQL when the question needs it.** "Run a HogQL query that groups weekly active accounts by plan."
- **Read-only by key.** The personal API key reads. It cannot capture an event, change a person record, alter a feature flag, or touch session recordings.

### How It Works

1. **Create a personal API key in PostHog** and note the project ID you want visible.
2. **Connect PostHog to CorpusIQ** with that key and project ID. Anything the key cannot reach is invisible to the connector.
3. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your account settings.
4. **CorpusIQ queries the project**: events, event definitions, person records, funnel results, and HogQL results.
5. **Claude answers** from those results, naming the events and the window it used.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In PostHog**

1. Open **Settings**, then **Personal API keys**, and create a key for this purpose. Do not reuse a key that is already embedded in your application.
2. Note the **project ID** for the project you want answerable.
3. If the key has scopes, grant read access to the project resources you need and nothing else.

**In CorpusIQ**

4. Log in and open **Connections**.
5. Select **PostHog** and paste the personal API key with the project ID.
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
        "https://www.corpusiq.io/mcp/direct-connection"
      ]
    }
  }
}
```

9. Save the file and fully quit Claude Desktop. Not just the window: quit the application.
10. Reopen Claude, complete the device login when prompted, and the tools indicator appears next to the message box.
11. Verify with "which events fired most in the last 24 hours". If the event names are real, the key is working.

If the tools indicator does not appear, work through [Claude can't see CorpusIQ](troubleshooting/claude-cant-see-corpusiq.md) before changing anything else.

### Example Claude Questions

**Funnels and activation**

- "How many users completed the onboarding funnel this week?"
- "What is the conversion rate from signup to first data source connected?"
- "Where in the funnel do most users stop, and what event precedes the drop?"

**Events and definitions**

- "Which events fired most in the last 24 hours?"
- "Which events are defined but have not fired in 30 days?"
- "Show the properties we send with the signup event."

**People and cohorts**

- "Which accounts signed up last month and are still active today?"
- "How many distinct accounts hit the report event last week?"
- "Which plan is the most active cohort right now?"

**HogQL**

- "Run a HogQL query that groups weekly active accounts by plan."
- "Write a HogQL query for activation rate by signup week, then run it."

**Cross-source**

- "Which accounts are heavy product users in PostHog but on the lowest plan in Stripe?" (requires the billing connector)
- "Do accounts that churned in the CRM show a usage drop two weeks earlier?" (requires the CRM connector)

### Security

- **Read-only key.** The connector reads events, event definitions, person records, funnel data, and HogQL results. It cannot capture an event, edit a person record, change a feature flag, or read session recordings through this path.
- **Scoped by key.** What the personal API key cannot reach, the connector cannot answer from. Create a key for this purpose rather than reusing an application key.
- **Revocable immediately.** Delete the key in PostHog under **Settings, Personal API keys** and access ends at once.
- **Project-scoped.** The project ID bounds what is visible. A second project needs its own connection.
- **Scoped direct-MCP retention.** Direct MCP retrieval is read-only. Raw customer files and full connector payloads are not retained. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **TLS in transit** between PostHog, CorpusIQ, and Claude.

### Comparison: The PostHog UI vs PostHog Through Claude

| Aspect | PostHog interface | CorpusIQ MCP with Claude |
|---|---|---|
| Input | A chart or an insight you configure | A question, with the window stated |
| Output | A graph to interpret | A number plus the events counted |
| HogQL | You write it | Written and run for you |
| Across sources | Export, then reconcile | Asked across connectors |
| New question | Build another insight | Ask again |
| Write access | Yes, by you | None, read-only key |

The PostHog interface is the right place for the dashboard you open every morning. Claude is the right place for the question that arrives once and needs an answer today.

### FAQ: Common Questions

<details>
<summary><strong>Is this read-only?</strong></summary>

Yes. The connector reads events and event definitions, person records, funnel conversion data, and HogQL query results. It cannot capture an event, change a person record, alter a feature flag, or touch session recordings.
</details>

<details>
<summary><strong>How does the connection authenticate?</strong></summary>

With a PostHog personal API key plus the project ID you want visible. Both are created in PostHog under **Settings**, then **Personal API keys**. Anything the key cannot reach is invisible to the connector, and revoking the key in PostHog ends access immediately.
</details>

<details>
<summary><strong>Do I need to know HogQL?</strong></summary>

No. Most questions are answered from events, funnels, and person records without any query language. When a question needs HogQL, Claude writes it and runs it, so you can read the query it produced and check the logic rather than authoring it yourself.
</details>

<details>
<summary><strong>Does it see session recordings or replays?</strong></summary>

No. Session recordings are outside this connection. The path reads events, persons, funnels, and query results, not screen recordings.
</details>

<details>
<summary><strong>Can Claude change a feature flag?</strong></summary>

No. Feature flags are outside this connection entirely, so Claude can neither read flag state nor change it. Rolling out a flag is a deliberate human action in PostHog.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live against the project when you ask. PostHog itself has ingestion lag on very recent events, so a question about the last five minutes can read lower than reality. Ask over a completed day or week when the number matters.
</details>

<details>
<summary><strong>Which project does it read?</strong></summary>

The project ID you entered. If you run separate projects for production and staging, connect production and keep staging out of range entirely.
</details>

<details>
<summary><strong>Why connect product analytics to Claude at all?</strong></summary>

Because the useful questions are rarely about product data alone. "Which heavy users are on the lowest plan" spans PostHog and billing. "Did usage drop before churn" spans PostHog and the CRM. A product analytics tool answers the first half of those questions well.
</details>

---

**Next steps:** [Connect PostHog to Claude now](https://corpusiq.io/connect/posthog-with-claude)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
