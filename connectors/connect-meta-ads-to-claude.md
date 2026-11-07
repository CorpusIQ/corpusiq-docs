---
title: "Connect Meta Ads to Claude via MCP - Paid Social"
description: "Connect Facebook and Instagram Ads to Claude through CorpusIQ MCP. Ask about campaigns, audiences, spend and lead forms in plain English, read-only."
last_updated: "2026-11-07"
---

# How to Connect Meta Ads to Claude with CorpusIQ MCP

Meta Ads is where Facebook and Instagram performance lives, and it is hard to interrogate because the reporting is split across campaigns, ad sets, audiences, and lead forms. Every answer arrives one level at a time.

Connecting Meta through CorpusIQ MCP puts ad account performance, campaigns, ad sets, individual ads, audience insights, and lead forms in the same conversation as the commerce platform and the other ad channels. You ask, Claude reads the account as it stands, and the answer names the placements and the window it used.

### Why Connect Meta Ads to Claude?

- **Spend questions.** "Which campaigns spent the most this month, and what did each return?"
- **Placement questions.** "Compare Facebook and Instagram placements by cost per result."
- **Waste questions.** "Which ad sets are spending but not producing conversions?"
- **Fatigue questions.** "Which audiences have the highest frequency, and where is fatigue showing?"
- **Lead questions.** "How many leads came through our lead forms this quarter, and what did each cost?"
- **Read-only by OAuth permission.** The connection reads. It cannot change a budget, pause an ad, or edit an audience.

### How It Works

1. **Connect Meta to CorpusIQ** through Meta's own OAuth flow, approving read access to the ad account.
2. **Meta is one connector** covering Facebook, Instagram, and Meta Ads, so you authorize once rather than per surface.
3. **Connect CorpusIQ to Claude** as an MCP server, using the config block from your account settings.
4. **CorpusIQ queries Meta**: ad account performance, campaigns, ad sets, individual ads, audience insights, and lead form results.
5. **Claude answers** from those results, naming the campaigns and the attribution window behind the figures.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Log in and open **Connections**.
2. Select **Meta** and start the authorization. Sign in with a Facebook user that is a person on the ad account in Business Manager, not merely an admin of the Page.
3. Approve the read permissions on Meta's consent screen, including `ads_read`.
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
        "https://mcp2.corpusiq.io/mcp"
      ]
    }
  }
}
```

7. Save the file and fully quit Claude Desktop. Not just the window: quit the application.
8. Reopen Claude, complete the device login when prompted, and the tools indicator appears next to the message box.
9. Verify with "which campaigns spent the most this month". If the campaign names are real, the account is connected.

If the tools indicator does not appear, work through [Claude can't see CorpusIQ](../troubleshooting/claude-cant-see-corpusiq.md) before changing anything else.

### Example Claude Questions

**Spend and return**

- "Which campaigns spent the most this month, and what did each return?"
- "What is our cost per acquisition trend over the last six months?"
- "Which ad sets are spending but not producing conversions?"

**Placement and creative**

- "Compare Facebook and Instagram placements by cost per result."
- "Which creatives have the best cost per result over the last 60 days?"
- "Where is the cost per result rising fastest?"

**Audience**

- "Which audiences have the highest frequency, and where is fatigue showing?"
- "Which interests produced the lowest cost per lead this quarter?"

**Lead forms**

- "How many leads came through our lead forms this quarter, and what did each cost?"
- "Which form produced the cheapest qualified lead?"

**Cross-source**

- "Compare Meta cost per acquisition with Google Ads for the same period." (requires the Google Ads connection)
- "Do the purchases Meta reports match what our commerce platform booked?" (requires the commerce connector)
- "Is our email revenue coming from customers acquired through paid social?" (requires the email connector)

### Security

- **Read-only connection.** The connector reads ad account performance, campaigns, ad sets, ads, audience insights, and lead forms. It cannot change budgets, pause ads, or edit audiences.
- **Scoped by Meta permissions.** What the authorizing user can see is what the connector can read, and the permissions are shown on Meta's own consent screen before you approve.
- **Revocable immediately.** Remove CorpusIQ in **Meta Business Settings, Integrations** and access ends at once.
- **One connector, three surfaces.** Facebook, Instagram, and Ads share one authorization, so there is one place to review and one place to revoke.
- **Scoped direct-MCP retention.** Direct MCP retrieval is read-only. Raw customer files and full connector payloads are not retained. Operational logs keep query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Meta, CorpusIQ, and Claude.

### Comparison: Meta Ads Manager vs Meta Ads Through Claude

| Aspect | Ads Manager | CorpusIQ MCP with Claude |
|---|---|---|
| Input | A column layout, a breakdown, a date range | A question, with the window stated |
| Output | Rows to scan across tabs | A number plus the campaigns counted |
| Facebook vs Instagram | A placement breakdown you configure | Asked directly |
| Across sources | Export, then reconcile | Asked across connectors |
| New question | Rebuild the view | Ask again |
| Write access | Yes, by you | None, read-only |

Ads Manager is the right place to change a budget. Claude is the right place for the question that compares what paid social reported against what the business booked.

### FAQ: Common Questions

<details>
<summary><strong>Is this read-only?</strong></summary>

Yes. The connector reads account performance, campaigns, ad sets, ads, audience insights, and lead forms. It cannot change budgets, pause ads, edit audiences, or create anything new.
</details>

<details>
<summary><strong>Does this cover Instagram as well as Facebook?</strong></summary>

Yes. Meta is a single connector covering Facebook, Instagram, and Meta Ads, so a placement-level comparison between the two is one question rather than two reports.
</details>

<details>
<summary><strong>How does the connection authenticate?</strong></summary>

Through Meta's OAuth flow, with the authorizing user approving read permissions on the ad account. Page admin alone is not enough: the Facebook user must be added as a person on the ad account in Business Manager.
</details>

<details>
<summary><strong>Can I see lead form performance?</strong></summary>

Yes. Lead forms are part of the Meta connector, so lead volume and cost per lead sit alongside campaign spend in the same answer.
</details>

<details>
<summary><strong>Why does spend differ from what I see in Ads Manager?</strong></summary>

Meta's attribution windows differ by surface, and some views show attributed numbers rather than raw spend. The connector pulls raw spend, which matches Billing and Payments. When a figure disagrees, check the window first.
</details>

<details>
<summary><strong>Is this worth it at a small budget?</strong></summary>

The cross-source question is worth asking at any spend level. "Do the purchases Meta reports match what we booked" changes a decision whether you spend hundreds or hundreds of thousands a month.
</details>

<details>
<summary><strong>Can Claude change a budget or pause an ad?</strong></summary>

No. There is no write path in the connection, so a session cannot spend money or stop a live campaign by accident. Those actions stay in Ads Manager.
</details>

---

**Next steps:** [Connect Meta Ads to Claude now](https://corpusiq.io/connect/meta-ads-with-claude)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
