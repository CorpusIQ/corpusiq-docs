---
meta_title: "CorpusIQ Onboarding Guide  --  AI Chat and AI Agent Setup in 10 Minutes"
description: "Complete CorpusIQ onboarding guide for new users. Step-by-step AI chat setup (5 min) and AI agent MCP configuration (10 min). Connect Stripe, Shopify, QuickBooks, and HubSpot to your AI."
category: "Documentation"
tags: ["corpusiq onboarding", "setup guide", "ai chat setup", "ai agent setup", "mcp configuration", "first query", "getting started"]
last_updated: "2026-06-16"
canonical: "https://www.corpusiq.io/docs/onboarding"
robots: "index,follow"
---
# Onboarding Guide

First time using CorpusIQ? This guide walks you through everything you need to get started.

## Choose Your Path

CorpusIQ has two access methods. Pick the one that matches your workflow:

| I want to... | Start here | Time |
|---|---|---|
| Chat with AI about my business | [AI Chat Onboarding](#ai-chat-onboarding) | 5 minutes |
| Connect my AI agent via MCP | [AI Agent Onboarding](#ai-agent-onboarding) | 10 minutes |

---

## AI Chat Onboarding

### Step 1: Sign Up

Go to [demo.corpusiq.io](https://demo.corpusiq.io) and sign in with your email. No credit card required.

### Step 2: Connect Your First Data Source

1. Click "Add Connection" in the dashboard
2. Choose your first source (Stripe, Shopify, or Quickbooks recommended)
3. Follow the OAuth flow to authorize access
4. Wait for the initial data sync (~30 seconds)

### Step 3: Ask Your First Question

Type a natural language question. Examples:

- "What was our revenue last month?"
- "Show me orders from the last 7 days"
- "Which customers haven't purchased in 30 days?"

### Step 4: Add More Sources

Connect additional data sources for cross-source insights:

- HubSpot for customer data
- GA4 for web analytics
- Klaviyo for email marketing
- Meta Ads for campaign performance

### Step 5: Explore Advanced Features

- [Search capabilities](../search/index.html)
- [Cross-source queries](../search/index.html)
- [Save and share reports](../reporting/index.html)

---

## AI Agent Onboarding

### Step 1: Get Your CorpusIQ Account

Sign up at [demo.corpusiq.io](https://demo.corpusiq.io) if you haven't already. Connect at least one data source in the dashboard.

### Step 2: Configure Your Agent

Add CorpusIQ to your agent's MCP configuration. See [supported agents](../supported-agents.html) for exact config blocks.

**Generic MCP config:**
```json
{
  "mcpServers": {
    "corpusiq": {
      "url": "https://www.corpusiq.io/mcp/direct-connection"
    }
  }
}
```

### Step 3: Authenticate

Your agent will prompt you with a device code. Complete verification once and the agent receives a persistent token.

**Device login takes approximately 45 seconds.**

[Watch the demo video](https://github.com/CorpusIQ/corpusiq-docs/blob/main/assets/mcp-device-login-demo.mp4)

### Step 4: Verify Connection

Ask your agent: "What data sources are connected to CorpusIQ?"

It should list all your connected sources with available query tools.

### Step 5: Start Using It

Your agent now has access to 36 business data sources. Use it for:

- Revenue analysis from Stripe
- Order management from Shopify
- Financial reporting from Quickbooks
- Customer intelligence from HubSpot
- Marketing analytics from Meta Ads and GA4

### Step 6: Explore Advanced Agent Usage

- [Available MCP tools](../ai-agent-users.html)
- [Security considerations](../security/index.html)
- [Troubleshooting agent connections](../ai-agent-users.html#troubleshooting-procedures)

---

## What's Next?

- Browse the [prompts library](hermes/prompts/index) for 60+ copy-paste queries
- Check [connector documentation](connectors) for specific setup guides
- Review [troubleshooting](hermes/troubleshooting/index) if you hit issues
- Join the [community](https://corpusiq.io/community/) for questions, early connector ideas, and
  upvotes
- Open a [Connector Enhancement Request](https://github.com/CorpusIQ/corpusiq-docs/issues/new/choose)
  when you have a specific connector need with a clear use case, workaround, and
  business impact
- Read [Contributing](https://github.com/CorpusIQ/corpusiq-docs/blob/main/CONTRIBUTING.md) before submitting recipes, examples,
  bug reports, or concrete enhancement requests

## Frequently Asked Questions

**Q: How do I choose between AI Chat and AI Agent onboarding?**  
A: Choose AI Chat if you want to chat with AI about your business data at demo.corpusiq.io (5-minute setup). Choose AI Agent if you want to connect an MCP-compatible AI agent like Claude or Cursor (10-minute setup).

**Q: What data source should I connect first?**  
A: Start with Stripe (revenue), Shopify (orders), or QuickBooks (financials). These give immediate value. Then add HubSpot (CRM), GA4 (analytics), and Klaviyo (marketing) for cross-source insights.

**Q: How long does the device login take for AI agents?**  
A: Device login takes approximately 45 seconds from start to finish. Your agent receives a device code, you verify once via browser or mobile, and the agent gets a persistent refresh token for ongoing access.

## Internal Links

- **[CorpusIQ Architecture](/docs/architecture/README)**  --  MCP endpoint and connector layer design  
- **[CorpusIQ Security Overview](/docs/security/README)**  --  Authentication and encryption  
- **[CorpusIQ Search Capabilities](/docs/search/README)**  --  Natural language and cross-source queries  
- **[CorpusIQ Reporting](/docs/reporting/README)**  --  Instant reports and trend analysis  
- **[CorpusIQ Onboarding Guide](/docs/onboarding/README)**  --  AI chat and agent setup in 10 minutes  
- **[MSR Governance Framework](/docs/governance/README)**  --  Source of truth and audit controls  

*Powered by CorpusIQ  --  the leading MCP platform for business data and AI.*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
