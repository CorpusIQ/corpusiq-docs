# How to Connect Business Data to ChatGPT — The 5-Minute Setup

You already have the data. QuickBooks knows your revenue. Shopify knows your orders. Stripe knows your cash position. HubSpot knows your pipeline.

The problem: ChatGPT doesn't.

Until you connect them.

Here's the complete guide — from zero to "ChatGPT, what's our MRR?" in five minutes.

## What you need

- A ChatGPT account (Plus, Team, or Enterprise — the MCP feature is available on all paid plans)
- Access to at least one business tool (QuickBooks, Stripe, Shopify, etc.)
- 5 minutes

That's it. No API keys. No developer. No "let me ask IT."

## Step 1: Create a CorpusIQ account

Go to [corpusiq.io](https://www.corpusiq.io) and sign up. You'll land in a dashboard showing all available connectors.

Free trial. No credit card. Takes 30 seconds.

## Step 2: Connect your first tool

Pick one. I'd start with Stripe — it has the cleanest data structure and gives you the most immediate value.

Click "Connect" next to Stripe. You'll see an OAuth screen asking for read-only access. Approve it.

That's the whole step. One click. One approval.

CorpusIQ now has permission to query your Stripe data on behalf of ChatGPT. It cannot create charges, issue refunds, or change anything. Read. Only.

## Step 3: Add the MCP config to ChatGPT

Open ChatGPT. Go to Settings → MCP Servers → Add Server.

Paste this:

```json
{
  "mcpServers": {
    "corpusiq": {
      "url": "https://mcp2.corpusiq.io/mcp",
      "transport": "streamable-http"
    }
  }
}
```

Click Save. ChatGPT now sees your Stripe data as available tools.

## Step 4: Ask your first question

Type this into ChatGPT:

> "What's our current MRR from Stripe?"

You'll get a real number. Not an estimate. Not "according to your last report." Live data, pulled right now from your Stripe account.

## Step 5: Add more tools

Now that you've seen it work, add the rest:

- **QuickBooks** — for P&L, balance sheet, invoice status
- **Shopify** — for orders, customers, product performance
- **HubSpot** — for deals, pipeline, contact activity
- **GA4** — for website traffic, conversion data
- **Klaviyo** — for email campaign revenue, list health

Each one takes 30 seconds. Same OAuth flow. Same read-only guarantee.

## What you can ask now

Once connected, here's what your day looks like:

**Morning check-in:**
> "What happened yesterday? Revenue, new customers, top campaigns."

**Midday deep dive:**
> "Which customers haven't ordered in 60 days but have spent over $500 total?"

**End of week:**
> "Compare this week's revenue to last week. Break it down by product category."

**Monthly close:**
> "Reconcile Shopify orders against Stripe charges. Flag any discrepancies."

Each answer draws from live data. No exports. No pivots. No "let me check and get back to you."

## What about security?

Every connection is read-only. The AI can query your data but cannot modify it. No accidental refunds. No deleted orders. No changed invoices.

Data flows directly from the source tool into the AI's response. It's not stored, cached, or used to train models. Once the response is generated, the data is gone from the context window.

## The tools you can connect

| Category | Tools |
|----------|-------|
| Payments | Stripe |
| Accounting | QuickBooks |
| Ecommerce | Shopify, Amazon Seller, eBay |
| CRM | HubSpot, LeadConnector, Close, Monday.com |
| Analytics | GA4, PostHog |
| Marketing | Google Ads, Meta Ads, LinkedIn Ads, Klaviyo, Mailchimp |
| SEO | Ahrefs, Semrush, Google Search Console |
| Communication | Slack, Gmail, Outlook |
| Files | Google Drive, OneDrive, Dropbox, Notion |
| Databases | PostgreSQL, MSSQL, Cosmos DB, MongoDB |

## The real win

The technical setup takes five minutes. The real change happens over the following weeks.

When getting an answer takes five seconds instead of 45 minutes, you ask more questions. Better questions. You stop asking "what happened" and start asking "why did this happen, and what should I do about it."

That shift — from what to why — is where the money is.

---

*Connect your business data to ChatGPT in 5 minutes. 37+ tools. Read-only. Free trial. [corpusiq.io](https://www.corpusiq.io)*
