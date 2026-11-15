---
title: "Connect Slack to Perplexity via MCP"
description: "Connect Slack to Perplexity through CorpusIQ MCP. Ask what was decided, who owns the action and where a thread stalled, with cited answers from your workspace."
category: Perplexity Integrations
tags: ["connect Slack to Perplexity", "Slack Perplexity integration", "MCP Slack connector", "Slack data to AI", "ask Slack in plain English", "CorpusIQ MCP"]
last_updated: "2026-11-15"
canonical: "https://www.corpusiq.io/docs/connect-slack-to-perplexity"
robots: "index,follow"
---

# How to Connect Slack to Perplexity with CorpusIQ MCP

Perplexity answers the outside question well: what moved in your market, what a competitor shipped, what the benchmark for your segment looks like this quarter.

It cannot see the channel where the pricing change was argued out, the thread where the vendor decision was made, or the file someone dropped in a project channel three weeks ago. None of that is public.

Connecting Slack through CorpusIQ MCP puts both halves in one thread. Perplexity answers the internal question from your own workspace, read-only, and names the channel and date it read.

### Why Connect Slack to Perplexity?

- **Decisions with context.** "What did we decide about the pricing change, and how does that compare to what competitors announced this quarter?" Both halves in one answer.
- **Stalled threads.** "Which channels have gone quiet on the migration project this month?"
- **Ownership.** "Who committed to the vendor follow-up, in which channel, and when?"
- **Benchmarking.** "Our top ten channels by message volume this month. Is that pattern normal for a company our size?"
- **Meeting prep.** "Summarize everything discussed in the enterprise account channels in the last two weeks."
- **Read-only by scope.** The retrieval tools documented on this page are read-only. There is no path from Perplexity into a Slack message or setting.

### How It Works

1. **Connect Slack to CorpusIQ** through Slack OAuth 2.0, granting read-only access to the scopes you review on the consent screen.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ reads** the channels, messages, threads and files that answer the question, as the authorizing user.
4. **Perplexity answers** with the decision, the channel and the date, and the outside context you asked for around it.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational logs keep query text, per-user tool-call metadata and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Open your dashboard and go to **Connectors**.
2. Select **Slack** and click **Connect Slack**.
3. You land on the Slack OAuth screen. Review the requested scopes: `channels:read`, `channels:history`, `search:read` and `files:read`.
4. Approve the read-only grant and pick the workspace if you belong to more than one.
5. Return to CorpusIQ. The connector turns green and the workspace is queryable.

**In Perplexity**

6. Open **Settings** and find the **MCP servers** section.
7. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

8. Connect and approve the CorpusIQ authorization page once.
9. Start a new thread and ask a question about a channel.

A workspace owner may need to approve the app for the workspace before the grant completes. Slack's own permission model decides what an answer can contain: private channels and direct messages appear only where the authorizing user already has access.

### Example Perplexity Questions

**Decisions and context**

- "What did we decide about the Q4 pricing change, and what did competitors announce this quarter?"
- "Summarize the vendor selection discussion in the procurement channel, then tell me what public reviews say about that vendor."
- "Which objections came up in the enterprise channel, and how have other companies answered them?"

**Activity and coverage**

- "Which channels have had no messages in 30 days that used to be active?"
- "What are our ten busiest channels this month, and is that distribution healthy for a company of our size?"
- "Which project channels have open questions nobody answered this week?"

**Search and retrieval**

- "Find the last file shared in the marketing channel and tell me what changed in it."
- "Search Slack for everything said about the API deprecation, and when it was first raised."
- "Pull the full thread on the budget proposal and list the open items."

**Cross-source**

- "Which Slack decisions match the Jira tickets that are still blocked?" (requires the Jira connector)
- "Compare what the sales channel said about pipeline this month with the HubSpot figures." (requires the HubSpot connector)
- "Did the traffic spike GA4 recorded come up in Slack, and in which channel?" (requires the Google Analytics connector)

### Security

- **Read-only retrieval tools.** The tools documented on this page are read-only, and every Slack scope the connector requests is a read scope: `channels:read`, `channels:history`, `search:read` and `files:read`. There is no path from Perplexity into a Slack message, channel or setting.
- **Slack permissions respected.** Private channels and direct messages are reachable only where the authorizing user is already a member, so the connection never widens anyone's access.
- **No stored credentials on your side.** CorpusIQ holds the encrypted OAuth token; you hold the Slack grant and can revoke it at any time from the workspace's app settings.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text, tool-call metadata and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Slack, CorpusIQ and Perplexity.

### Comparison: Slack Search vs Slack in Perplexity

| Aspect | Slack search | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | A keyword or a person | A question in plain language |
| Scope | Messages that match the keyword | Answers synthesized across channels and threads |
| Outside context | Copy the thread into a search tab | Same thread, same answer |
| Cross-system | Read, then switch tools | Asked across connectors |
| Decisions | You read and infer | Extracted, with channel and date |
| Write access | Yes, by your users | None through the retrieval tools |

Slack search finds the message you already knew existed. A connected workspace answers the question that came up in the meeting.

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity post to Slack or change a channel?</strong></summary>

No. The retrieval tools documented on this page are read-only. Messages, channels and workspace settings are untouched.
</details>

<details>
<summary><strong>Can it read private channels and direct messages?</strong></summary>

Only where the authorizing user already has access. Slack's permission model is enforced on every call, so a private channel you are not in stays invisible.
</details>

<details>
<summary><strong>Does this cover Slack Connect channels?</strong></summary>

Yes, where the authorizing user has access. Messages from external organizations appear with the same attribution they carry in Slack.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. Each question reads the current state of the workspace, so a message posted a minute ago appears in the next answer. Verify time-sensitive points against the cited channel and date.
</details>

<details>
<summary><strong>Which scopes are requested?</strong></summary>

`channels:read`, `channels:history`, `search:read` and `files:read`. Every one is a read scope. No scope that can send a message or change a setting is requested.
</details>

<details>
<summary><strong>What about very large workspaces?</strong></summary>

Questions are answered against the channels and date ranges you name. "Search the sales channel for pricing discussions this month" narrows the read instead of scanning thousands of channels.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. Slack is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

<details>
<summary><strong>Where is the Slack data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Operational logs may persist for up to 30 days. See the [read-only and security documentation](/hermes/security/read-only-and-security).
</details>

---

**Next steps:** [Connect Slack to Perplexity now](https://www.corpusiq.io/connectors/perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
