---
title: "Connect Salesforce to Perplexity via MCP"
description: "Connect Salesforce to Perplexity through CorpusIQ MCP. Ask about pipeline by region, accounts at risk and stalled deals, with cited answers from your own CRM"
category: Perplexity Integrations
tags: ["connect Salesforce to Perplexity", "Salesforce Perplexity integration", "MCP Salesforce connector", "Salesforce data to AI", "ask Salesforce in plain English", "CorpusIQ MCP"]
last_updated: "2026-11-14"
canonical: "https://www.corpusiq.io/docs/connect-salesforce-to-perplexity"
robots: "index,follow"
---

# How to Connect Salesforce to Perplexity with CorpusIQ MCP

Perplexity is built for the outside view: market movement, competitor announcements, what analysts say about your sector this quarter.

It cannot see your pipeline, your account history, or the deal that has sat in the same stage since July, because none of that is public.

Connecting Salesforce through CorpusIQ MCP puts both halves in one thread. Perplexity answers the CRM question from your own org, read-only, and names the objects it read.

### Why Connect Salesforce to Perplexity?

- **Pipeline with market context.** "Our win rate on deals over 100,000 is 34 percent. How does that compare to enterprise SaaS benchmarks?" Both halves answered in one thread.
- **Accounts at risk.** "Which accounts have had no activity in 90 days and still carry an open opportunity?"
- **Stalled deals.** "Show me opportunities that have not moved stage in 45 days, by owner."
- **Forecast support.** Pipeline by stage, by region, by rep, before the forecast call rather than during it.
- **Account prep.** One question returns contacts, open opportunities and recent cases for the account you are about to call.
- **Read-only by scope.** The retrieval tools documented on this page are read-only. There is no path from Perplexity into a Salesforce record.

### How It Works

1. **Connect Salesforce to CorpusIQ** through Salesforce OAuth 2.0, granting read-only access to the objects you select.
2. **Add CorpusIQ to Perplexity** as a custom remote MCP server, using the endpoint from your CorpusIQ account settings.
3. **CorpusIQ reads** the accounts, opportunities, contacts and cases that answer the question.
4. **Perplexity answers** with the figure, the period it covers, and the outside context you asked for around it.

Direct MCP retrieval is read-only. It does not retain raw customer files or full connector response payloads; operational logs keep query text, per-user tool-call metadata and bounded outcome summaries for up to 30 days.

### Setup Steps

**In CorpusIQ**

1. Open your dashboard and go to **Connectors**.
2. Select **Salesforce** and click **Connect Salesforce**.
3. You land on the Salesforce OAuth screen. Approve the read-only grant.
4. Choose which objects are reachable: Accounts, Opportunities, Contacts, Leads, Cases, and any custom object the REST API exposes.
5. Return to CorpusIQ. The connector turns green and your org is queryable.

**In Perplexity**

6. Open **Settings** and find the **MCP servers** section.
7. Add a custom MCP server and paste the endpoint:

```
https://mcp2.corpusiq.io/mcp
```

8. Connect and approve the CorpusIQ authorization page once.
9. Start a new thread and ask a question about your pipeline.

Requires a Salesforce admin for the initial grant. Field-level security is honored, so a user who cannot see a field in Salesforce will not see it in an answer.

### Example Perplexity Questions

**Pipeline and forecast**

- "What is our total pipeline by stage and region this quarter?"
- "Which opportunities over 100,000 are expected to close before the end of the quarter?"
- "What is our historical close rate for opportunities above 100,000, and how does that compare to the sector?"
- "Show pipeline coverage ratio by rep."

**Account health**

- "Which accounts have had no activity in 90 days and still have an open opportunity?"
- "Give me a profile of the account we meet on Thursday: contacts, open deals, recent cases."
- "Which accounts renewed last year have no renewal opportunity in the current quarter?"

**Sales operations**

- "What is the average deal cycle by opportunity type?"
- "Which lead sources convert to closed won most often?"
- "Show me every opportunity that has been in the same stage for more than 45 days."

**Cross-source**

- "Compare Salesforce pipeline by quarter to QuickBooks booked revenue." (requires the QuickBooks connector)
- "Which Salesforce accounts also appear in Stripe with a lapsed subscription?" (requires the Stripe connector)

### Security

- **Read-only retrieval tools.** The tools documented on this page are marked read-only, and the OAuth grant covers read access to the objects you selected. There is no write path from Perplexity into a Salesforce record.
- **Field-level security respected.** Salesforce's own permissions decide what an answer can contain.
- **No stored credentials on your side.** CorpusIQ holds the encrypted OAuth token; you hold the Salesforce grant and can revoke it at any time.
- **Scoped direct-MCP retention.** Raw customer files and full connector payloads are not retained. Operational logs keep query text, tool-call metadata and bounded outcome summaries for up to 30 days.
- **TLS in transit** between Salesforce, CorpusIQ and Perplexity.

### Comparison: Salesforce Reports vs Salesforce in Perplexity

| Aspect | Salesforce reports and dashboards | CorpusIQ MCP with Perplexity |
|---|---|---|
| Input | A report someone configured | A question in plain language |
| Owner | Admin or analyst | Anyone with the connector |
| Outside context | Copy the number into a search tab | Same thread, same answer |
| Cross-system | Export and join by hand | Asked across connectors |
| Follow-up | Rebuild the report | Ask the next question |
| Write access | Yes, by your users | None through the retrieval tools |

A dashboard answers the question your team knew to ask last quarter. A connected org answers the one that came up in the meeting.

### FAQ: Common Questions

<details>
<summary><strong>Can Perplexity change anything in Salesforce?</strong></summary>

No. The retrieval tools documented on this page are read-only. Opportunities, accounts and cases are untouched.
</details>

<details>
<summary><strong>Does this work with custom objects?</strong></summary>

Yes, when the object is reachable through the Salesforce REST API and your grant covers it. Objects outside the grant stay invisible.
</details>

<details>
<summary><strong>Which Salesforce editions are covered?</strong></summary>

Any edition where an admin can approve an OAuth connected app with API access. Sandbox and production orgs carry separate grants, so choose which one you connect.
</details>

<details>
<summary><strong>How current is the data?</strong></summary>

Live. Each question reads the current state of the org, so a stage change made a minute ago shows up in the next answer. Verify time-sensitive figures against the cited record.
</details>

<details>
<summary><strong>Does this work only in Perplexity?</strong></summary>

No. Salesforce is exposed to ChatGPT, Claude and Perplexity through the same endpoint on the same subscription.
</details>

<details>
<summary><strong>Can I limit an answer to one business unit?</strong></summary>

The grant is per org, and answers follow the field and object permissions of the connecting role. If you need unit-level separation, connect the org role that matches the boundary you want.
</details>

<details>
<summary><strong>Where is the Salesforce data stored?</strong></summary>

CorpusIQ does not retain raw customer files or full connector response payloads. Operational logs may persist for up to 30 days. See the [read-only and security documentation](/hermes/security/read-only-and-security).
</details>

---

**Next steps:** [Connect Salesforce to Perplexity now](https://www.corpusiq.io/connectors/perplexity)

*Part of the MCP knowledge base at [corpusiq.io](https://www.corpusiq.io) - connect 40+ business tools to AI.*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.CorpusIQ.io).*
