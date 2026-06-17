---
title: "Connect HubSpot to ChatGPT via MCP — Live Data, No Code | CorpusIQ"
description: "Connect your HubSpot account to ChatGPT through CorpusIQ MCP. Ask natural language questions about your hubspot data and get real-time, source-cited answers — no exports, no coding required."
category: ChatGPT Integrations
tags: ["connect HubSpot to ChatGPT", "HubSpot ChatGPT integration", "MCP HubSpot connector", "HubSpot data to ChatGPT", "AI for HubSpot", "CorpusIQ MCP"]
last_updated: 2026-06-16
canonical: https://www.corpusiq.io/docs/connect-hubspot-to-chatgpt
robots: index,follow
---

# How to Connect HubSpot to ChatGPT with CorpusIQ MCP

Your **HubSpot** account holds critical business data — but accessing insights usually means logging in, navigating dashboards, and running manual reports. **Connecting HubSpot to ChatGPT through CorpusIQ MCP** eliminates all that friction. Once connected via a secure OAuth flow, ChatGPT can query your live HubSpot data directly — you ask questions in plain English, and get cited answers drawn from your actual account, not outdated exports or screenshots.

Once connected, ChatGPT can search your contacts, list deals by stage, pull full company profiles, and answer questions that span contacts, deals, and companies — all in plain English, all from live HubSpot data.

This page covers the connection architecture, what you can ask, security, setup, and how MCP compares to direct HubSpot API integration.

## FAQ: Common Questions

<details>
<summary><strong>What CRM questions can I ask ChatGPT about HubSpot?</strong></summary>

Questions about contacts, deals, companies, and your pipeline. Examples: "Pull together everything I need to know about Acme Corp", "How many deals are in the negotiation stage?", "Search HubSpot for contacts at Stripe", "Show me my top 10 deals by amount", "Which deals are closing this month?", "What's my pipeline value by stage?", "Show me all contacts created in the last 30 days", "Which deals have been stuck in the same stage for over 2 weeks?", "Give me a summary of all activity with Company X."
</details>

<details>
<summary><strong>How does CorpusIQ connect HubSpot to ChatGPT?</strong></summary>

CorpusIQ connects to HubSpot via OAuth 2.0 and exposes HubSpot's CRM objects as MCP tools. You authorize read-only access once (selecting which HubSpot portal to connect), then add the CorpusIQ MCP server to ChatGPT. When you ask a CRM question, ChatGPT calls the appropriate tool — contact search, deal listing, company retrieval — and returns a cited answer from your live HubSpot data.
</details>

<details>
<summary><strong>Is the connection read-only?</strong></summary>

Yes. CorpusIQ requests read-only scopes from HubSpot. ChatGPT can see contacts, deals, and companies. It cannot create contacts, move deals between stages, modify company properties, or change anything in your CRM. The read-only guarantee is enforced at both the OAuth scope level and the MCP tool level.
</details>

<details>
<summary><strong>What HubSpot objects can ChatGPT access?</strong></summary>

Contacts with full property details and keyword search. Companies with full details. Deals with status, stage, amount, and close date. HubSpot account and portal metadata. All accessed through read-only operations — ChatGPT reads your CRM data, it never writes to it.
</details>

<details>
<summary><strong>Can ChatGPT combine HubSpot data with data from other tools?</strong></summary>

Yes. This is where MCP creates value that no single-platform dashboard can match. "Show me all deals closing this month and cross-reference with email activity from Gmail" combines HubSpot deal data with Gmail communication history. "Which customers have open deals and overdue invoices?" spans HubSpot and QuickBooks. The cross-source capability is the differentiator — see our [Benefits of MCP for Business](../docs/benefits-of-mcp-for-business.md).
</details>

<details>
<summary><strong>How is this different from HubSpot's built-in AI features?</strong></summary>

HubSpot's AI features (like Breeze AI) are designed for specific HubSpot-native workflows — content generation, forecasting, email composition. They work within HubSpot's interface and primarily on HubSpot data alone. Connecting HubSpot to ChatGPT via MCP enables ad-hoc natural language queries across your CRM data and any other connected data source. The interface is ChatGPT (where many teams already spend time), and the scope is your entire data stack, not just HubSpot.
</details>

<details>
<summary><strong>What permissions do I need in HubSpot?</strong></summary>

You need a HubSpot account with admin access to authorize the OAuth connection. Once authorized, any CorpusIQ user with access to that authorization can query the connected portal through ChatGPT. Free HubSpot accounts may have limited object scopes — some properties may not be accessible.
</details>

<details>
<summary><strong>Can I search across all CRM objects at once?</strong></summary>

You can ask questions that span contacts, deals, and companies. "Find every interaction with Company X — contacts, open deals, recent activity." ChatGPT will make multiple MCP tool calls as needed and synthesize the results. This multi-object query capability is built into the MCP architecture.
</details>

<details>
<summary><strong>How does this handle custom properties?</strong></summary>

Custom HubSpot properties are included in contact, deal, and company objects. If you've created custom fields in HubSpot, ChatGPT can query and reference them. Just ask: "Show me all deals where the custom field 'Implementation Tier' is 'Enterprise'."
</details>

<details>
<summary><strong>Does this work with multiple HubSpot portals?</strong></summary>

Yes. You can connect multiple HubSpot portals to CorpusIQ. Each portal's data is isolated, and you can specify which portal to query — or ask ChatGPT to pull data across portals for multi-brand or multi-region sales analysis.
</details>


## How It Works

1. **Connect HubSpot to CorpusIQ.** In your CorpusIQ dashboard, click Connections → HubSpot → sign into HubSpot → select your portal → approve read-only access. Takes 2 minutes.

2. **Connect CorpusIQ to ChatGPT.** Add the CorpusIQ MCP server as a connected app in ChatGPT. ChatGPT automatically discovers your available CRM tools.

3. **Ask CRM questions.** ChatGPT receives your question, identifies the HubSpot tools it needs, calls them, and returns a cited response from live data.

4. **Iterate conversationally.** "Now show me the contacts at those companies" or "Which of those deals are most at risk?" — follow-up questions maintain context.

No ETL pipeline. No data warehouse. No scheduled syncs. Your CRM data is queried live, every time.

## Benefits

**Sales pipeline visibility without CRM navigation.** Your CEO, finance lead, or board members can ask about pipeline health without logging into HubSpot. "What's our pipeline value by stage?" is a ChatGPT question, not a CRM login session.

**Account 360 in one question.** Preparing for a customer call? Ask ChatGPT: "Give me everything on Acme Corp — contacts, open deals, deal values, last activity dates." One question replaces clicking through multiple HubSpot screens.

**Pipeline management at scale.** "Which deals are stalled?" "Show me deals with no activity in 14 days." "Which reps have the most deals in the proposal stage?" Pipeline hygiene questions that would require custom reports in HubSpot become instant queries.

**Cross-source relationship intelligence.** The real power comes from connecting HubSpot with your other tools. "Show me open deals for customers with overdue invoices" combines HubSpot and QuickBooks. "Which customers with open deals haven't opened our last email campaign?" combines HubSpot and Klaviyo. This cross-source context is unique to [MCP platforms like CorpusIQ](../docs/benefits-of-mcp-for-business.md).

**Source-cited answers you can verify.** Every response includes provenance — which HubSpot object was queried, when, and what was returned. If a deal amount looks wrong, you can trace it back to the source record.

## Use Cases

### Pre-Call Briefing

Before a sales call: "Give me a full brief on Company X — all contacts, open deals, deal amounts, last activity, and any recent email threads." One question, one answer, no tab-switching.

### Weekly Pipeline Review

Instead of building a pipeline report in HubSpot: "Show me all deals by stage with amounts, close dates, and owner. Flag any that are past their expected close date." Your weekly review becomes a conversation.

### Territory and Rep Performance

"How many deals did each rep close this quarter?" "What's the average deal size by rep?" "Which territories have the healthiest pipeline?" Sales leadership gets answers without building reports.

### Customer Health Scoring

"Score my top 20 customers by deal recency, deal size, and email engagement." ChatGPT can retrieve HubSpot deal data, cross-reference with email activity, and calculate a composite health score — all from one prompt.

### Cross-Source Attribution

"Which marketing campaigns generated the most HubSpot deals this quarter?" queries HubSpot for closed deals in the period, then cross-references with Google Ads and Meta Ads for campaign attribution. See our [MCP for Marketing guide](../docs/mcp-for-marketing.md) for more attribution use cases.

## Security: Read-Only by Design

The HubSpot integration is read-only at every layer:

- **OAuth Scopes:** Read-only access to contacts, companies, deals, and account metadata. No write, create, update, or delete permissions.
- **MCP Tools:** Only query tools are exposed — contact search, deal listing, company retrieval. No tools exist to create, modify, or delete HubSpot records.
- **No Data Persistence:** CorpusIQ does not store your CRM data. Queries execute, responses are delivered, data is discarded.
- **Encryption:** All data in transit is encrypted via TLS 1.3 between HubSpot, CorpusIQ, and ChatGPT.

For sales organizations with strict data governance requirements, this architecture means your CRM data stays in HubSpot. The MCP layer provides governed, auditable access without data duplication.

## Comparison: MCP vs. Direct HubSpot API Integration

| Aspect | Direct API Integration | CorpusIQ MCP |
|--------|----------------------|--------------|
| **Setup** | Days of development — HubSpot API client, OAuth, pagination, rate limiting | 2 minutes — OAuth authorization |
| **Query interface** | REST endpoints, JSON parsing, custom code for each query type | Natural language — ask any CRM question |
| **Multi-object queries** | Must code joins across contacts, deals, companies manually | Automatic — ChatGPT orchestrates tool calls |
| **Cross-source** | Separate integrations for every tool, custom orchestration layer | One question across all connected tools |
| **Search** | HubSpot search syntax, property-specific filters | Natural language search with automatic property mapping |
| **Maintenance** | API version updates, property schema changes, token rotation | CorpusIQ handles all maintenance |

The direct API approach is right when you need write operations — creating contacts programmatically, updating deal stages via workflow, or building custom HubSpot integrations. For CRM data access, Q&A, and reporting, MCP is faster to deploy, safer by default, and instantly cross-source capable.

## Setup Guide

1. **Sign up** at [corpusiq.io](https://www.corpusiq.io) — free 30-day trial.
2. **Connect HubSpot.** Dashboard → Connections → HubSpot → sign into HubSpot → select portal → authorize read-only access.
3. **Connect ChatGPT.** Add the CorpusIQ MCP server to ChatGPT. See our [Quick Start guide](../docs/quick-start.md) for instructions.
4. **Verify.** Ask "How many contacts are in my HubSpot account?" to confirm the connection.
5. **Explore.** Try "Show me my open deals sorted by amount" or "Search for contacts at example.com."

Under 5 minutes from signup to your first CRM query in ChatGPT.

## Related Pages

- [Connect Salesforce to ChatGPT](../docs/connect-salesforce-to-chatgpt.md) — enterprise CRM data in ChatGPT
- [Connect Shopify to ChatGPT](../docs/connect-shopify-to-chatgpt.md) — ecommerce data in ChatGPT
- [Connect QuickBooks to ChatGPT](../docs/connect-quickbooks-to-chatgpt.md) — financial data in ChatGPT
- [Connect Gmail to ChatGPT](../docs/connect-gmail-to-chatgpt.md) — email data in ChatGPT
- [Connect Slack to ChatGPT](../docs/connect-slack-to-chatgpt.md) — team communication in ChatGPT
- [ChatGPT Integration Overview](../docs/chatgpt-integration.md) — how the connection works
- [Benefits of MCP for Business](../docs/benefits-of-mcp-for-business.md) — why MCP architecture matters
- [MCP for Sales](../docs/mcp-for-sales.md) — MCP for sales teams
- [HubSpot Connector Reference](../connectors/hubspot.md) — technical details
- [MCP vs. API Integrations](../docs/mcp-vs-api-integrations.md) — detailed comparison

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "headline": "How to Connect HubSpot to ChatGPT with CorpusIQ MCP",
  "author": {
    "@type": "Organization",
    "name": "CorpusIQ",
    "url": "https://www.corpusiq.io"
  },
  "publisher": {
    "@type": "Organization",
    "name": "CorpusIQ",
    "url": "https://www.corpusiq.io"
  },
  "datePublished": "2026-06-16",
  "dateModified": "2026-06-16",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What CRM questions can I ask ChatGPT about HubSpot?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Questions about contacts, deals, companies, and your pipeline. Examples: \"Pull together everything I need to know about Acme Corp\", \"How many deals are in the negotiation stage?\", \"Search HubSpot for contacts at Stripe\", \"Show me my top 10 deals by amount\", \"Which deals are closing this month?\", \"Wh"
      }
    },
    {
      "@type": "Question",
      "name": "How does CorpusIQ connect HubSpot to ChatGPT?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "CorpusIQ connects to HubSpot via OAuth 2.0 and exposes HubSpot's CRM objects as MCP tools. You authorize read-only access once (selecting which HubSpot portal to connect), then add the CorpusIQ MCP server to ChatGPT. When you ask a CRM question, ChatGPT calls the appropriate tool \u2014 contact search, d"
      }
    },
    {
      "@type": "Question",
      "name": "Is the connection read-only?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. CorpusIQ requests read-only scopes from HubSpot. ChatGPT can see contacts, deals, and companies. It cannot create contacts, move deals between stages, modify company properties, or change anything in your CRM. The read-only guarantee is enforced at both the OAuth scope level and the MCP tool le"
      }
    },
    {
      "@type": "Question",
      "name": "What HubSpot objects can ChatGPT access?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Contacts with full property details and keyword search. Companies with full details. Deals with status, stage, amount, and close date. HubSpot account and portal metadata. All accessed through read-only operations \u2014 ChatGPT reads your CRM data, it never writes to it."
      }
    },
    {
      "@type": "Question",
      "name": "Can ChatGPT combine HubSpot data with data from other tools?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. This is where MCP creates value that no single-platform dashboard can match. \"Show me all deals closing this month and cross-reference with email activity from Gmail\" combines HubSpot deal data with Gmail communication history. \"Which customers have open deals and overdue invoices?\" spans HubSp"
      }
    },
    {
      "@type": "Question",
      "name": "How is this different from HubSpot's built-in AI features?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "HubSpot's AI features (like Breeze AI) are designed for specific HubSpot-native workflows \u2014 content generation, forecasting, email composition. They work within HubSpot's interface and primarily on HubSpot data alone. Connecting HubSpot to ChatGPT via MCP enables ad-hoc natural language queries acro"
      }
    },
    {
      "@type": "Question",
      "name": "What permissions do I need in HubSpot?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You need a HubSpot account with admin access to authorize the OAuth connection. Once authorized, any CorpusIQ user with access to that authorization can query the connected portal through ChatGPT. Free HubSpot accounts may have limited object scopes \u2014 some properties may not be accessible."
      }
    },
    {
      "@type": "Question",
      "name": "Can I search across all CRM objects at once?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You can ask questions that span contacts, deals, and companies. \"Find every interaction with Company X \u2014 contacts, open deals, recent activity.\" ChatGPT will make multiple MCP tool calls as needed and synthesize the results. This multi-object query capability is built into the MCP architecture."
      }
    }
  ]
}
</script>
