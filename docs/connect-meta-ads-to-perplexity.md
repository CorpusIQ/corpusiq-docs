---
title: "Connect Meta Ads to Perplexity via MCP"
description: "Connect Facebook and Instagram Ads to Perplexity through CorpusIQ MCP. Ask which campaigns returned, what each lead cost and where frequency is climbing."
category: Perplexity Integrations
tags: ["connect Meta Ads to Perplexity", "Facebook Ads Perplexity integration", "Instagram Ads MCP connector", "Meta Ads data to AI", "ask Meta Ads in plain English", "CorpusIQ MCP"]
last_updated: "2026-11-15"
canonical: "https://www.corpusiq.io/docs/connect-meta-ads-to-perplexity"
robots: "index,follow"
---

# How to Connect Meta Ads to Perplexity with CorpusIQ MCP

Paid social reporting lives in four places at once: campaign level for budget, ad set level for audience, ad level for creative, and the lead form for what actually arrived.

Perplexity can tell you what cost per acquisition looks like in your category this quarter. It cannot tell you which of your campaigns is paying it.

Connecting Meta Ads through CorpusIQ MCP puts both halves in one thread. Perplexity answers from your own ad account, read-only, and names the campaign the figure came from.

### Why Connect Meta Ads to Perplexity?

- **Spend against benchmark.** "Our cost per lead rose this quarter. What is normal for this category, and which ad sets drove the rise?"
- **Placement comparison.** "Compare Facebook and Instagram placements by cost per result, then tell me where the audience overlap usually sits."
- **Waste.** "Which ad sets are spending but producing no conversions?"
- **Creative.** "Which ads have the best cost per result over 60 days, and what pattern do the winners share?"
- **Lead forms.** "How many leads came through our forms this quarter, and what did each cost against industry benchmarks?"
- **Read-only by annotation.** The retrieval tools documented on this page are read-only. There is no path from Perplexity into a budget or an audience.

### How It Works

1. **Connect Meta to CorpusIQ** through Meta's OAuth flow, approving `ads_read` on the accounts you select.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ reads** campaigns, ad sets, ads, audience insights and lead forms for the date range in your question.
4. **Perplexity answers** with the figure, the period it covers, and the outside context you asked for around it.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational logs keep query text, per-user tool-call metadata and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Open your dashboard and go to **Connectors**.
2. Select **Meta** and start the authorization. Meta is one connector covering Facebook, Instagram and Meta Ads, so you approve once.
3. Sign in with a Facebook user that is a person on the ad account in Business Manager. Page-level admin is not enough.
4. Choose which ad accounts CorpusIQ may read, and approve `ads_read` on Meta's consent screen.
5. Return to CorpusIQ. The connector turns green and the account is queryable.

**In Perplexity**

6. Open **Settings** and find the **MCP servers** section.
7. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

8. Connect and approve the CorpusIQ authorization page once.
9. Start a new thread with "which campaigns spent the most this month" to confirm the account is visible.

If the answer is "no ad accounts found", the Facebook user is not a person on the ad account in Business Manager. Add the person there and reconnect.

### Example Perplexity Questions

**Spend and return**

- "Which campaigns spent the most this month, and what did each return against category benchmarks?"
- "What is our cost per acquisition trend over six months, and how does it compare to paid search?"
- "Which ad sets are spending with no conversions in the last 30 days?"

**Placement and audience**

- "Compare Facebook and Instagram placements by cost per result."
- "Which audiences have the highest frequency, and where is fatigue showing?"
- "What is our reach against the size of the addressable audience for this category?"

**Creative and leads**

- "Which creatives have the best cost per result over 60 days?"
- "How many leads came through our lead forms this quarter, and what did each cost?"
- "Which ads produced leads that also appear as customers in our commerce platform?"

**Cross-source**

- "Compare Meta Ads cost per acquisition with Google Ads for the same period." (requires the Google Ads connector)
- "Do the purchases Meta reports match what our commerce platform booked?" (requires a commerce connector)
- "Is the email revenue from Klaviyo coming from customers we acquired through paid social?" (requires the Klaviyo connector)

### Security

- **Read-only retrieval tools.** The tools documented on this page are read-only. Spend, budgets, audiences and campaigns cannot be changed from Perplexity.
- **Meta permissions respected.** `ads_read` is a read permission, and the grant is limited to the ad accounts you selected during authorization.
- **No stored credentials on your side.** CorpusIQ holds the encrypted Meta token; you hold the grant and can revoke it in Business Manager at any time.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text, tool-call metadata and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Meta, CorpusIQ and Perplexity.

### Comparison: Ads Manager vs Meta Ads in Perplexity

| Aspect | Meta Ads Manager | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | Columns, breakdowns and filters you set up | A question in plain language |
| Levels | One level at a time | Campaign, ad set and ad in one answer |
| Outside context | Copy the figure into a search tab | Same thread, same answer |
| Cross-system | Export and join by hand | Asked across connectors |
| Attribution caveat | Visible in reporting settings | Stated alongside the figure |
| Write access | Yes, by your users | None through the retrieval tools |

Ads Manager reports what you configured it to report. A connected ad account answers the question that came up in the review.

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity pause an ad or change a budget?</strong></summary>

No. The retrieval tools documented on this page are read-only. Changes stay in Meta Ads Manager.
</details>

<details>
<summary><strong>Does this cover Instagram as well as Facebook?</strong></summary>

Yes. Meta is a single CorpusIQ connector covering Facebook, Instagram and Meta Ads, so placement-level comparison between the two is available in one question.
</details>

<details>
<summary><strong>Why do the numbers differ from Ads Manager?</strong></summary>

Meta revises attribution for up to seven days after a click, so figures inside that window can move. Ask for a date range that closed more than a week ago when a number has to match a report exactly.
</details>

<details>
<summary><strong>Can I see lead form performance?</strong></summary>

Yes. Lead form data is part of the Meta connector, so lead volume and cost per lead are queryable alongside campaign spend.
</details>

<details>
<summary><strong>Why does it say no ad accounts found?</strong></summary>

The authorizing Facebook user must be added as a person on the ad account in Business Manager. Being an admin of the Page does not grant ad account access. Fix the person assignment, then reconnect.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. Meta Ads is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

<details>
<summary><strong>Where is the ad data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Operational logs may persist for up to 30 days. See the [read-only and security documentation](/hermes/security/read-only-and-security).
</details>

---

**Next steps:** [Connect Meta Ads to Perplexity now](https://www.corpusiq.io/connectors/perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
