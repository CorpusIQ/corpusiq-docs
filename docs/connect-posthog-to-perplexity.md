---
title: "Connect PostHog to Perplexity via MCP"
description: "Connect PostHog to Perplexity through CorpusIQ MCP. Ask funnel, retention and event questions in plain English, with cited answers from your project."
category: Perplexity Integrations
tags: ["connect PostHog to Perplexity", "PostHog Perplexity integration", "MCP PostHog connector", "PostHog analytics to AI", "ask funnels in plain English", "CorpusIQ MCP"]
last_updated: "2026-11-18"
canonical: "https://www.corpusiq.io/docs/connect-posthog-to-perplexity"
robots: "index,follow"
---

# How to Connect PostHog to Perplexity with CorpusIQ MCP

Product analytics answers a question you already know how to ask inside the tool. The question you actually have is messier: why did signup conversion drop after the release, which step loses the most people, and is that the same step that lost them last month.

Getting there means building an insight, choosing a breakdown, and remembering which event name the team settled on.

Connecting PostHog through CorpusIQ MCP puts the project behind a question. Perplexity reads live events, funnels and person records, read-only, and names what it used.

### Why Connect PostHog to Perplexity?

- **Funnel performance.** "How many users completed the onboarding funnel this week, and which step lost the most?"
- **Retention.** "What percentage of users who signed up last week are still active today?"
- **Event health.** "Which events are firing most frequently in the last 24 hours?"
- **Segments.** "Show the top ten users by event count this month."
- **Custom analysis.** Run a SQL-style HogQL query when a question needs one.
- **Read-only by capability.** The retrieval tools documented on this page are read-only, and the credential is a personal API key you scope and can revoke.

### How It Works

1. **Connect PostHog to CorpusIQ** with a personal API key and the project ID it should read.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ queries** events, event definitions, person records and funnel data for that project.
4. **Perplexity answers** from the returned rows, with the project and the events named.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational logs keep query text, per-user tool-call metadata and bounded outcome summaries for up to 30 days.

### Setup Steps

**In PostHog**

1. Open **Settings**, then **Personal API Keys**, and create a key for CorpusIQ.
2. Copy the key and note the **Project ID** of the project you want read.

**In CorpusIQ**

3. Open your dashboard and go to **Connectors**.
4. Select **PostHog**, paste the personal API key and the project ID.
5. The connector turns green and the analytics tools become available.

**In Perplexity**

6. Open **Settings** and find the **MCP servers** section.
7. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

8. Connect and approve the CorpusIQ authorization page once. Then start a new thread and ask about a funnel, an event or a cohort.

The key decides the reach. A personal API key carries the scopes it was issued with, and the project ID decides which project's data is read.

### Example Perplexity Questions

**Funnels and conversion**

- "How many users completed the onboarding funnel this week, and which step lost the most?"
- "What is the conversion rate from signup to first data connector connected?"
- "Which funnel step has the widest drop for mobile users?"

**Retention and cohorts**

- "What percentage of users who signed up last week are still active today?"
- "Compare week four retention for the last two monthly cohorts."
- "Which acquisition source retains best after 30 days?"

**Events and adoption**

- "Which events are firing most frequently in the last 24 hours?"
- "Which features are used by fewer than five percent of active users?"
- "Show the top ten users by event count this month."

**Cross-source**

- "Do the paying accounts in PostHog match the active subscriptions in Stripe?" (requires the Stripe connector)
- "Which customers raised a support thread and then stopped using the product?" (requires a support or mailbox connector)
- "Compare trial signups in PostHog with the sessions reported in Analytics." (requires the Google Analytics connector)

### Security

- **Read-only retrieval tools.** The tools documented on this page read events, person records, funnel data and run HogQL queries. They do not capture events, edit definitions or change project settings.
- **Your own key, your own scope.** The personal API key is issued in PostHog, carries the scopes you grant it, and can be revoked there at any time.
- **Project-scoped.** A connection reads the single project whose ID you supply.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text, tool-call metadata and bounded outcome summaries for up to 30 days.
- **TLS in transit** between PostHog, CorpusIQ and Perplexity.

### Comparison: PostHog insights and dashboards

| Aspect | PostHog insights and dashboards | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | An insight builder and a chosen breakdown | A question, with the breakdown implied |
| Scope | The events and properties you pick | The events, people and funnels that fit |
| Follow-ups | Rebuild the insight | Ask the next question in the same thread |
| Outside context | Open a second tab | Same thread, same answer |
| Cross-system | Export to a sheet | Asked across connectors |
| Write access | Yes, by your users | None through the retrieval tools |

A dashboard shows what you thought to chart. The question is the one you did not.

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity change anything in PostHog?</strong></summary>

No. The retrieval tools documented on this page read events, person records and funnels. Nothing is captured, edited or deleted.
</details>

<details>
<summary><strong>Which credential does it need?</strong></summary>

A PostHog personal API key plus the project ID. The key is created under Settings, then Personal API Keys.
</details>

<details>
<summary><strong>Does it see session recordings or feature flags?</strong></summary>

No. The connector covers events and event definitions, person records, funnel conversion data and custom HogQL queries. Session recordings and feature flags are outside it.
</details>

<details>
<summary><strong>Can it run a HogQL query?</strong></summary>

Yes, when a question needs one. Simple questions are answered without you writing any query.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. Each question reads the project as it stands, subject to PostHog's own ingestion delay for very recent events.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. PostHog is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

### See Also

- [Connect PostHog to ChatGPT](connect-posthog-to-chatgpt.md) - the same funnel and event questions, asked from ChatGPT
- [Connect PostHog to Claude](connect-posthog-to-claude.md) - the same questions with the Claude Desktop config block
- [PostHog connector](connectors/posthog.md) - everything the connection can see, and what it cannot

---

**Next steps:** [Add CorpusIQ to Perplexity now](https://www.corpusiq.io/connectors/perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
