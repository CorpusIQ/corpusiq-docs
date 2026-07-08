---
title: "Connect Salesforce to Claude via MCP  --  Live Data, No Code | CorpusIQ"
description: "Connect your Salesforce account to Claude through CorpusIQ MCP. Ask natural language questions about your salesforce data and get real-time, source-cited answers  --  no exports, no coding required."
category: Claude Integrations
tags: ["connect Salesforce to Claude", "Salesforce Claude integration", "MCP Salesforce connector", "Salesforce data to Claude", "AI for Salesforce", "CorpusIQ MCP"]
last_updated: 2026-07-08
canonical: https://www.corpusiq.io/docs/connect-salesforce-to-claude
robots: index,follow
---

# How to Connect Salesforce to Claude with CorpusIQ MCP

Salesforce is the backbone of enterprise sales, service, and marketing operations  --  but extracting insights from it often requires dedicated Salesforce admins, complex reports, or expensive BI tools. Connecting Salesforce to Claude via CorpusIQ's MCP platform democratizes access to your CRM data. Any team member can ask Claude "What's our Q3 pipeline by region?", "Show me accounts at risk of churn", or "Which opportunities have been stuck for 60+ days?" and receive accurate, real-time answers.

The integration uses the Model Context Protocol (MCP) to give Claude secure, read-only access to your Salesforce org. Setup is OAuth-based and takes under five minutes. No Apex code. No API integration project. No consultant bill.

### Why Connect Salesforce to Claude?

Salesforce is powerful but complex. The average enterprise Salesforce org has hundreds of custom objects, fields, and workflows. Most employees interact with only a fraction of the data they need because building reports and dashboards requires specialized skills. Claude removes that barrier.

**Key benefits:**

- **Universal CRM access.** Marketing, finance, and operations teams can query Salesforce data without knowing how to build a report.
- **Instant pipeline visibility.** Executives can ask "What's our total pipeline?" and get an answer in seconds.
- **Cross-source enterprise intelligence.** Combine Salesforce pipeline with NetSuite financials, Stripe billing, or Snowflake analytics.
- **Meeting intelligence.** Before any customer call, ask Claude for the account's full history  --  opportunities, cases, recent activity.
- **Forecasting support.** Claude can analyze pipeline velocity, historical close rates, and current opportunities to support forecast discussions.
- **Read-only security.** OAuth 2.0 with read-only scope. Claude can never modify your Salesforce data.

### How It Works

1. **Connect Salesforce** via OAuth 2.0. CorpusIQ requests read-only access to your specified objects.
2. **Ask Claude** any question about your Salesforce data.
3. **CorpusIQ translates** your question into Salesforce REST API calls and executes them.
4. **Claude presents** the results with analysis, trends, and recommendations.

All queries are live. CorpusIQ never caches or stores your Salesforce data.

### Setup Steps

1. Navigate to **Connectors** in CorpusIQ.
2. Select **Salesforce** from the catalog.
3. Click **"Connect Salesforce"**  --  authorize via Salesforce OAuth.
4. Configure which objects Claude can access (Accounts, Opportunities, Contacts, Leads, Cases, etc.).
5. Start asking Claude CRM questions.

### Example Claude Queries

**Pipeline & Forecasting:**
- "What's our total pipeline by stage and by region?"
- "Which opportunities are expected to close this quarter, sorted by amount?"
- "What's our historical close rate for opportunities over $100K?"
- "Show me pipeline coverage ratio by rep."

**Account Management:**
- "Give me a complete profile of [Account Name]  --  contacts, open opportunities, recent cases."
- "Which accounts haven't had any activity in 90 days?"
- "Show me accounts by industry and annual revenue."

**Sales Operations:**
- "What's the average deal cycle time by opportunity type?"
- "Show me opportunities that have been in the same stage for more than 45 days."
- "Which lead sources have the highest conversion to closed-won?"

**Cross-Source:**
- "Compare Salesforce pipeline to QuickBooks actual revenue by quarter." (requires QuickBooks)
- "Match Salesforce accounts to Stripe customers for renewal analysis." (requires Stripe)

### Enterprise Security

- **Read-only OAuth 2.0.** Zero write capability.
- **SOC 2 compliant infrastructure.**
- **No data storage.** Live API calls only.
- **Field-level security respected.** Salesforce's native field permissions are honored.
- **Audit logging.** All queries logged for compliance.

### Comparison: MCP vs. Salesforce API Direct

| Aspect | CorpusIQ MCP | Salesforce API Direct |
|---|---|---|
| Setup | 5-minute OAuth | Weeks (integration project) |
| Technical skill | None | Salesforce developer required |
| Natural language | Yes | No  --  SOQL/REST API only |
| Cross-source | Built-in | Custom data warehouse |
| Cost | Included in CorpusIQ | Developer + maintenance |

### FAQ: Common Questions

<details>
<summary><strong>Does this work with custom Salesforce objects?</strong></summary>

CorpusIQ queries standard Salesforce REST API endpoints. Custom objects accessible via the REST API are queryable through Claude.
</details>

<details>
<summary><strong>Can Claude modify Salesforce records?</strong></summary>

No. The integration is strictly read-only.
</details>

<details>
<summary><strong>Does this respect Salesforce sharing rules?</strong></summary>

Yes. The OAuth token inherits the authenticated user's permissions. Users only see records their Salesforce profile allows.
</details>

<details>
<summary><strong>Can I connect multiple Salesforce orgs?</strong></summary>

Yes  --  sandbox and production orgs can be connected separately.
</details>

<details>
<summary><strong>Is this suitable for regulated industries (finance, healthcare)?</strong></summary>

CorpusIQ is SOC 2 compliant. The read-only architecture means no data can be modified. Evaluate within your specific regulatory framework.
</details>

---

**Next steps:** [Connect Salesforce to Claude now →](https://corpusiq.io/connect/salesforce)

*Connect Connect Salesforce to Claude via MCP  --  Live Data, No Code... with CorpusIQ → [corpusiq.io](https://www.corpusiq.io)*

*Connect Connect Salesforce to Claude via MCP  --  Live Data, No Code... with CorpusIQ → [corpusiq.io](https://www.corpusiq.io)*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
