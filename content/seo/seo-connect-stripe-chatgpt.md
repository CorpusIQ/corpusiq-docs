# Connect Stripe to ChatGPT — See Your Revenue in Plain English

You process payments through Stripe. Every morning you check the dashboard: MRR, recent charges, churn. You know the numbers.

What if you could just ask?

> "What's our MRR today? Compare it to last month and last year."

> "Which customers churned this month? What was their lifetime value?"

> "Show me revenue by plan. Which plans are growing fastest?"

Here's how to connect Stripe to ChatGPT in 2 minutes.

## Step 1: Sign up

Go to corpusiq.io. Create an account. No credit card.

## Step 2: Connect Stripe

Click "Connect" next to Stripe. Approve the OAuth screen. Read-only access only.

## Step 3: Add to ChatGPT

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

## Step 4: Ask

"What's our MRR?"

Done. Live Stripe data in ChatGPT.

---

*CorpusIQ: Connect Stripe to ChatGPT in 2 minutes. Read-only. Free trial. [corpusiq.io](https://www.corpusiq.io)*
