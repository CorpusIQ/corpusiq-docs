---
title: "Connect HubSpot to Claude via MCP — AI-Powered CRM Intelligence"
meta_title: "Connect HubSpot to Claude | CorpusIQ MCP Integration for CRM"
meta_description: "Connect HubSpot to Claude using CorpusIQ's MCP platform. Query contacts, deals, companies, and pipeline metrics in natural language. Read-only OAuth, no-code, enterprise CRM in AI conversations."
url: "/docs/connect-hubspot-to-claude/"
h1: "Connect HubSpot to Claude: Your CRM in Natural Language"
category: "Claude Integrations"
last_updated: "2025-06-16"
author: "CorpusIQ"
canonical: "https://corpusiq.com/docs/connect-hubspot-to-claude/"
---

## Connect HubSpot to Claude: Your CRM in Natural Language

Sales teams spend more time updating and navigating HubSpot than they do selling. Connecting HubSpot to Claude via CorpusIQ's MCP platform flips that dynamic — Claude becomes a natural language interface to your entire CRM. Ask "What deals are closing this month?", "Show me contacts who haven't been contacted in 30 days", or "What's our pipeline by stage and rep?" and get instant, accurate answers drawn from your live HubSpot data.

The integration uses the Model Context Protocol (MCP), an open standard that CorpusIQ implements to connect Claude to business tools. Setup is point-and-click OAuth — no APIs to configure, no code to write, no developer required.

### Why Connect HubSpot to Claude?

HubSpot is the system of record for your customer relationships, sales pipeline, and marketing contacts. But extracting insights from HubSpot typically means building dashboards, running reports, or manually clicking through records. Claude eliminates that friction by letting anyone on your team ask natural language questions and receive instant answers from live CRM data.

**Key benefits of connecting HubSpot to Claude:**

- **Pipeline intelligence in seconds.** Ask "What's the total value of deals in the negotiation stage?" and get the answer without opening HubSpot.
- **Contact research at conversational speed.** "Tell me everything about [company]" returns contact, deal history, and recent activity in one response.
- **Sales coaching and accountability.** "Show me deals that haven't had activity in 14 days" helps managers identify stalled opportunities.
- **Cross-source revenue intelligence.** Combine HubSpot pipeline with QuickBooks actuals, Stripe payments, or Shopify orders for a complete revenue picture.
- **Meeting prep automation.** Before a call, ask Claude "Give me the full history for [contact/company]" for instant briefing.

### How the Integration Works

1. **Connect HubSpot** via OAuth. CorpusIQ requests read-only access to contacts, companies, deals, and associated records.
2. **Ask Claude** any question about your CRM data — pipeline, contacts, companies, deal status, activity history.
3. **CorpusIQ executes** the appropriate HubSpot API calls using your stored credentials.
4. **Claude presents** the answer in natural language, with context and actionable recommendations.

All communication is encrypted. CorpusIQ never stores your CRM data — every query is a live API call.

### Setup Steps

1. **Log into CorpusIQ** and go to Connectors.
2. **Select HubSpot** from the integration list.
3. **Click "Connect HubSpot"** — you'll be redirected to HubSpot's OAuth screen.
4. **Authorize read-only access** to contacts, companies, deals, and associated records.
5. **Return to CorpusIQ.** Start asking Claude CRM questions immediately.

### Example Claude Queries for HubSpot

**Pipeline Management:**
- "What's our total pipeline value, broken down by stage?"
- "Which deals are expected to close this month?"
- "Show me deals above $50,000 that are in the proposal stage."
- "What's our win rate by deal source?"
- "Which deals have been in the same stage for more than 30 days?"

**Contact & Company Intelligence:**
- "Tell me everything about [company name]."
- "Which contacts at [company] have we emailed in the last 90 days?"
- "Show me contacts who attended our last webinar but aren't in a deal."
- "What companies in our CRM are in the technology industry with 50+ employees?"

**Sales Management:**
- "Show me each rep's pipeline, closed-won, and closed-lost for this quarter."
- "Which reps have the highest deal velocity?"
- "Show me deals that haven't had any activity in the last 14 days."
- "What's the average deal size by rep?"

**Cross-Source Intelligence:**
- "Compare our HubSpot pipeline to actual revenue in QuickBooks by quarter." (requires QuickBooks)
- "Which HubSpot contacts have active Stripe subscriptions?" (requires Stripe)
- "Match HubSpot companies to Shopify customers — who buys through both channels?" (requires Shopify)

### Security

- **Read-only OAuth 2.0.** Claude can query contacts, companies, and deals but cannot create, update, or delete CRM records.
- **No data storage.** Your HubSpot data never lives on CorpusIQ servers.
- **Instant disconnect.** Revoke access from HubSpot or CorpusIQ at any time.

### Comparison: MCP vs. HubSpot API Direct

| Aspect | CorpusIQ MCP | HubSpot API Direct |
|---|---|---|
| Setup time | Under 5 minutes | Hours to days |
| Technical skill | None required | Developer required |
| Natural language | Yes — ask Claude directly | No |
| Cross-source | Built-in multi-tool correlation | Custom development |
| Cost | Included in CorpusIQ | Developer time + maintenance |

### FAQ

**Q: Can Claude create or update HubSpot records?**
A: No. The integration is read-only. Claude can analyze and report on CRM data but cannot modify it.

**Q: Which HubSpot hubs does this support?**
A: The integration supports contacts, companies, and deals across all HubSpot tiers. Marketing Hub and Service Hub objects may require additional scope configuration.

**Q: How many HubSpot accounts can I connect?**
A: You can connect multiple HubSpot accounts through CorpusIQ, each with independent permissions.

**Q: Is the data real-time?**
A: Yes. Every Claude query triggers a fresh API call to HubSpot.

**Q: Can I restrict which properties Claude can see?**
A: OAuth scopes control access at the object level. For property-level restrictions, use HubSpot's permission sets to limit what the OAuth app can access.

### Internal Links

- [Connect Salesforce to Claude](/docs/connect-salesforce-to-claude/) — Salesforce CRM in Claude.
- [Connect Slack to Claude](/docs/connect-slack-to-claude/) — Team communication data in Claude.
- [Connect Notion to Claude](/docs/connect-notion-to-claude/) — Knowledge management in Claude.
- [Connect QuickBooks to Claude](/docs/connect-quickbooks-to-claude/) — Financial data in Claude.
- [AI for Sales Reporting](/docs/ai-for-sales-reporting/) — AI-powered sales analytics.
- [AI for Revenue Operations](/docs/ai-for-revenue-operations/) — RevOps transformation.
- [AI for Customer Support](/docs/ai-for-customer-support/) — Support intelligence.
- [What is MCP?](/docs/what-is-mcp/) — Understanding the Model Context Protocol.

---

**Next steps:** [Connect HubSpot to Claude now →](https://app.corpusiq.com/connect/hubspot)
