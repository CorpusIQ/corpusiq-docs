---
title: "Connect Google Ads to Claude via MCP - Search Spend"
description: "Connect Google Ads to Claude through CorpusIQ MCP. Ask about campaigns, keywords, search terms and wasted spend in plain English, read-only."
last_updated: "2026-11-07"
---

# How to Connect Google Ads to Claude with CorpusIQ MCP

Google Ads holds the spend, the search terms, and the quality scores that set what everything costs next month. Reading it usually means one report, one date range, one campaign at a time, and the interesting question is almost always across two of those at once.

Connecting Google Ads through CorpusIQ MCP puts campaigns, ad groups, keywords, search terms, quality score components, and device and geographic breakdowns in the same conversation as analytics and the commerce platform. You ask, Claude reads the account as it stands, and the answer names the campaigns and the window it used.

### Why Connect Google Ads to Claude?

- **Spend questions.** "Which campaigns spent the most last month, and what did each return?"
- **Waste questions.** "Which search terms triggered ads but never converted, and how much did they cost?"
- **Quality score questions.** "Where is quality score lowest, and is it ad relevance or landing page experience?"
- **Comparison questions.** "How does mobile spend and conversion compare with desktop this quarter?"
- **Agency questions.** "Which client accounts had the biggest month-on-month rise in cost per conversion?"
- **Read-only connection.** The connection reads. It cannot change a bid, a budget, a campaign, or a creative.

### How It Works

1. **Connect Google Workspace to CorpusIQ** with the Google account that can see the Ads accounts. Google Ads comes through the same connection, not a separate one.
2. **If you use a manager account**, note the login customer ID so the linked client accounts can be reached.
3. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your account settings.
4. **CorpusIQ queries Google Ads**: campaign and ad group performance, keywords with quality scores and impression share, search terms, geographic and device breakdowns, and custom GAQL queries.
5. **Claude answers** from those results, naming the campaigns and the date window behind the figures.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connections**.
2. Select **Google Workspace** and sign in with the Google account that has access to the Ads account you want answerable.
3. Approve read access on Google's consent screen. Ads data arrives through the same connection.
4. If you manage accounts through an MCC, set the login customer ID so client accounts are reachable.
5. Copy the MCP config block shown under **Settings, Integrations, Claude Desktop**.

**In Claude Desktop**

6. Open **Settings, Developer, Edit Config**. This opens `claude_desktop_config.json`.
7. Add the CorpusIQ entry:

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

8. Save the file and fully quit Claude Desktop. Not just the window: quit the application.
9. Reopen Claude, complete the device login when prompted, and the tools indicator appears next to the message box.
10. Verify with "how much did I spend on Google Ads last month". If the figure matches the account, the connection is live.

If the tools indicator does not appear, work through [Claude can't see CorpusIQ](../troubleshooting/claude-cant-see-corpusiq.md) before changing anything else.

### Example Claude Questions

**Spend and return**

- "Which campaigns spent the most last month, and what did each return?"
- "What is our cost per conversion trend over the last six months?"
- "Which campaigns have spent with no conversions in the last 30 days?"

**Search terms and keywords**

- "Which search terms triggered ads but never converted, and how much did they cost?"
- "Which ad groups are bidding on terms we already rank organically for?"
- "Which keywords have the best conversion rate at the lowest cost per conversion?"

**Quality score**

- "Where is quality score lowest, and is it ad relevance or landing page experience?"
- "Which keywords lost impression share to budget this week?"

**Breakdowns and agencies**

- "How does mobile spend and conversion compare with desktop this quarter?"
- "Which countries produced the highest cost per conversion?"
- "Which of my client accounts had the biggest month-on-month increase in cost per conversion?"

**Cross-source**

- "Compare Google Ads cost per acquisition with Meta Ads for the same period." (requires the Meta connector)
- "Does the revenue Google Ads reports match what our commerce platform booked?" (requires the commerce connector)

### Security

- **Read-only connection.** The connector reads campaign, keyword, search term, and breakdown data. It cannot change bids, budgets, campaign settings, or creatives.
- **Scoped by Google account.** What the signed-in Google user can see is what the connector can read. Anyone without access to the Ads account cannot authorize it.
- **Revocable immediately.** Remove CorpusIQ's access in your Google account permissions and the connection ends at once.
- **Manager accounts are explicit.** Client accounts are reached only through the login customer ID you provide, not by discovery against every account you have ever touched.
- **Scoped direct-MCP retention.** Direct MCP retrieval is read-only. Raw customer files and full connector payloads are not retained. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Google, CorpusIQ, and Claude.

### Comparison: The Google Ads UI vs Google Ads Through Claude

| Aspect | Google Ads interface | CorpusIQ MCP with Claude |
|---|---|---|
| Input | A report, a segment, a date range | A question, with the window stated |
| Output | Tables to scan | A number plus the campaigns counted |
| Several accounts | Switch accounts, repeat the report | Asked across a manager account |
| Across sources | Export, then reconcile in a sheet | Asked across connectors |
| New question | Rebuild the report | Ask again |
| Write access | Yes, by you | None, read-only |

The Google Ads interface is the right place to change a bid. Claude is the right place for the question that compares what search returned against what the business actually booked.

### FAQ: Common Questions

<details>
<summary><strong>Is this read-only?</strong></summary>

Yes. The connector reads campaign, ad group, keyword, search term, quality score, and breakdown data. It cannot change bids, budgets, campaign settings, or creatives.
</details>

<details>
<summary><strong>How does the connection authenticate?</strong></summary>

Through Google OAuth on the Google Workspace connection. You sign in with the Google account that has access to the Ads account and approve read access on Google's consent screen. Ads is not a separate connector with its own credentials.
</details>

<details>
<summary><strong>Do you support manager accounts for agencies?</strong></summary>

Yes. Set the login customer ID for the manager account and the linked client accounts are reachable through the same connection, so a cross-client question is one question rather than one per account.
</details>

<details>
<summary><strong>Why does Google Ads reporting lag sometimes?</strong></summary>

Google Ads itself takes a few hours to settle recent spend and conversions, and conversion counts only include conversions configured in the Ads account. An imported GA4 conversion that stopped importing shows up here as a gap rather than a drop in performance.
</details>

<details>
<summary><strong>Can Claude change a bid or pause a campaign?</strong></summary>

No. The connection has no write path. Bids, budgets, and campaign state stay in Google Ads, which means an analysis session cannot spend money by accident.
</details>

<details>
<summary><strong>Can I ask custom queries?</strong></summary>

Yes. Beyond the standard retrieval tools, custom GAQL queries can be run, so a question shaped unlike any built-in report is still answerable.
</details>

<details>
<summary><strong>Why connect ad data to Claude at all?</strong></summary>

Because the platform's conversion count is not the business's revenue. The question worth asking crosses into analytics or commerce, and that join is where a single-platform report stops.
</details>

---

**Next steps:** [Connect Google Ads to Claude now](https://corpusiq.io/connect/google-ads-with-claude)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
