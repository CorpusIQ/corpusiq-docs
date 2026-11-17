---
title: "Connect LinkedIn Ads to ChatGPT via MCP"
description: "Connect LinkedIn Ads to ChatGPT through CorpusIQ MCP. Ask about campaigns, spend and clicks in plain English, read-only, with the objects named."
category: ChatGPT Integrations
tags: ["connect LinkedIn Ads to ChatGPT", "LinkedIn Ads ChatGPT integration", "MCP linkedin-ads connector", "ask ChatGPT about business data", "CorpusIQ MCP"]
last_updated: "2026-11-17"
canonical: "https://www.corpusiq.io/docs/connect-linkedin-ads-to-chatgpt"
robots: "index,follow"
---

# How to Connect LinkedIn Ads to ChatGPT with CorpusIQ MCP

LinkedIn is the paid channel most B2B teams cannot attribute cleanly. Campaign Manager reports impressions, clicks and cost per campaign. It does not tell you which of those leads turned into pipeline, because that record lives in the CRM.

Connecting LinkedIn Ads through CorpusIQ MCP puts campaign performance next to the data that follows it. Ask which campaigns sourced deals that closed, and the answer reads your ad account and your CRM in one pass.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Why Connect LinkedIn Ads to ChatGPT?

- **Spend and pacing.** "How much did I spend on LinkedIn Ads last month?" answered from the ad account, not a screenshot.
- **Campaign comparison.** "Which LinkedIn campaigns are driving the most clicks?" read across campaign groups.
- **Creative performance.** "Which creatives are running in my remarketing campaign?" with statuses attached.
- **Daily trend.** Impressions, clicks, cost in local currency and conversions, day by day.
- **Cross-source attribution.** Campaign spend asked alongside CRM pipeline and closed revenue in the same question.

### How It Works

1. **Connect LinkedIn Ads to CorpusIQ.** Click Connect and approve read access for the account you sign in with, then pick the ad accounts.
2. **Connect CorpusIQ to ChatGPT** as an MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ translates** the question into read-only queries against your campaign and spend data and assembles the result.
4. **ChatGPT answers** from that result and names the objects each figure came from.

### Before you connect

- A LinkedIn account with access to the ad accounts you want read
- At least a Viewer role on each ad account - an admin can grant it in Campaign Manager under Account Settings, Manage Access
- About 2 minutes

### Setup Steps

**In CorpusIQ**

1. In CorpusIQ, open **Dashboard** then **Connectors** and find **LinkedIn Ads**.
2. Click Connect.
3. Sign in to LinkedIn when the consent screen appears.
4. Approve read access and select the ad accounts you want CorpusIQ to see.
5. You are returned to CorpusIQ, and the connector turns from gray to green.

**In ChatGPT**

6. Install **CorpusIQ** from the ChatGPT app store, or add the CorpusIQ MCP server under **Settings**, **Connectors**.
7. Approve the CorpusIQ authorization when prompted, once.
8. Start a new conversation and ask a question that needs your data.

If the connector does not appear, work through the [Quick Start guide](quick-start.md) before changing anything else.

### Example ChatGPT Questions

**Spend and pacing**

- "How much did I spend on LinkedIn Ads last month, by campaign?"
- "Which campaigns are pacing ahead of their budget?"
- "Show me daily spend for the last 30 days."

**Performance**

- "Which LinkedIn campaigns are driving the most clicks?"
- "Show me daily performance for my enterprise product campaign, including cost per conversion."
- "Which creatives are running in my remarketing campaign?"

**Accounts**

- "List all my LinkedIn ad accounts and their statuses."
- "Which ad accounts have no active campaigns right now?"

**Cross-source**

- "Which LinkedIn campaigns sourced deals that closed last quarter?" (requires the CRM connector)
- "Compare LinkedIn Ads spend against closed revenue by month." (requires the CRM or accounting connector)

### Security

- **Read-only ad account access.** The connector reads memberships, campaigns, creatives and daily analytics.
- **No campaign changes.** It never creates campaigns, changes budgets, or modifies ads.
- **Role-scoped.** What the connected LinkedIn user can see is what the connector can read. A Viewer role on two accounts means two accounts.
- **Revocable at any time.** Remove the CorpusIQ access in your LinkedIn account settings and the connection stops working.
- **Scoped direct-MCP retention.** CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

### Comparison: the native interface vs LinkedIn Ads through ChatGPT

| Question | The native interface | CorpusIQ MCP with ChatGPT |
|---|---|---|
| Input | Campaign Manager filters, one report at a time | A question across campaigns and dates |
| Output | Platform metrics | An answer joined to pipeline and revenue |
| Attribution | Manual export, then match in a spreadsheet | Asked directly, CRM read in the same pass |
| Reporting lag | You check each campaign | Said plainly: platform analytics lag 24 to 48 hours |

### FAQ: Common Questions

<details>
<summary><strong>What access level does my LinkedIn user need?</strong></summary>

Viewer on each ad account you want readable. An account admin can grant it in Campaign Manager under Account Settings, Manage Access.
</details>

<details>
<summary><strong>No ad accounts found. Why?</strong></summary>

The connected LinkedIn user holds no ad account membership. Being an admin of a LinkedIn Page is not the same as holding a role on an ad account.
</details>

<details>
<summary><strong>Insufficient permissions on a specific account.</strong></summary>

The role on that ad account is too restrictive for the read it needs. Viewer is the floor, and some accounts are shared with a role that does not cover campaign analytics.
</details>

<details>
<summary><strong>Campaign analytics return zero. Is the connector broken?</strong></summary>

Check the date range first. LinkedIn Ads reporting lags by 24 to 48 hours, so today's spend often reads as zero while yesterday's is present.
</details>

<details>
<summary><strong>Authentication fails after working for a while.</strong></summary>

Reset the LinkedIn Ads connector in your CorpusIQ dashboard and reconnect with the account that holds the ad account roles.
</details>

<details>
<summary><strong>Can the assistant change budgets or pause campaigns?</strong></summary>

No. The connection reads ad account data. Budgets, pauses and creative changes stay in Campaign Manager, where a person makes them.
</details>

---

**Next steps:** [Connect LinkedIn Ads to ChatGPT now](https://www.corpusiq.io/docs/connectors/linkedin-ads)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

## See also

- [Connect LinkedIn Ads to Claude](connectors/connect-linkedin-ads-to-claude.md) - campaign spend, creatives and clicks in one thread.
- [Connect LinkedIn Ads to Perplexity](connect-linkedin-ads-to-perplexity.md) - campaign spend, creatives and clicks in one thread.

- [LinkedIn Ads connector reference](connectors/linkedin-ads.md) - connection requirements, visible objects and troubleshooting.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
