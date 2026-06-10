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

- [Search capabilities](docs/search/README.md)
- [Cross-source queries](docs/search/cross-source.md)
- [Save and share reports](docs/reporting/README.md)

---

## AI Agent Onboarding

### Step 1: Get Your CorpusIQ Account

Sign up at [demo.corpusiq.io](https://demo.corpusiq.io) if you haven't already. Connect at least one data source in the dashboard.

### Step 2: Configure Your Agent

Add CorpusIQ to your agent's MCP configuration. See [supported agents](supported-agents.md) for exact config blocks.

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

- [Available MCP tools](ai-agent-users.md)
- [Security considerations](docs/security/README.md)
- [Troubleshooting agent connections](ai-agent-users.md#troubleshooting-procedures)

---

## What's Next?

- Browse the [prompts library](/prompts/) for 60+ copy-paste queries
- Check [connector documentation](/connectors/) for specific setup guides
- Review [troubleshooting](/troubleshooting/) if you hit issues
- Join the [community](/community/) for questions, early connector ideas, and
  upvotes
- Open a [Connector Enhancement Request](https://github.com/CorpusIQ/corpusiq-docs/issues/new/choose)
  when you have a specific connector need with a clear use case, workaround, and
  business impact
- Read [Contributing](/CONTRIBUTING.md) before submitting recipes, examples,
  bug reports, or concrete enhancement requests
