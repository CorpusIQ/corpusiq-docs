# 6. Your first multi-connector query

You've authenticated one connector (QuickBooks, Shopify, GA4, etc.). Now you'll connect a second one and ask a question that needs both.

This walk-through uses **GA4 + Shopify**, but the pattern is the same for any pair.

## What you'll do

1. Authenticate GA4 (if you use Shopify)
2. Ask a question that CorpusIQ answers by reading both connectors
3. Debug if the answer is empty or wrong

This takes ~5 minutes if both connectors are already live, or 10 if you need to set up the second one.

## Prerequisites

- [Step 4](04-first-connector.md) is done (one connector authenticated)
- For this example: Shopify **and** GA4 accounts
- (If you don't have both, substitute your second tool; the pattern is identical)

## Part 1: Authenticate the second connector

Pick a connector that pairs well with your first.

### Common pairings

| First connector | Good second connector | What you can ask |
|-----------------|----------------------|------------------|
| Shopify | GA4 | "Which traffic source drives the most orders?" |
| Google Ads | Shopify or GA4 | "What's my real CAC by campaign?" |
| QuickBooks | Shopify | "Are my Shopify orders matching my invoice revenue?" |
| Klaviyo | Shopify | "Which email campaigns drove the most revenue?" |
| HubSpot | GA4 | "How many MQLs became customers?" |

### Steps to connect the second

1. In CorpusIQ, open **Connectors**.
2. Find your second tool (e.g., **GA4**). Click **Connect**.
3. Follow the OAuth flow (same as Step 4):
   - Sign in with the right account
   - Approve all permissions
   - Return to CorpusIQ
4. Confirm it shows **Connected** with a timestamp.

You now have two connectors authenticated.

## Part 2: Ask your first cross-source question

Open Claude or ChatGPT and ask a question that needs both connectors.

### Example: GA4 + Shopify

> Show me orders from the last 7 days, grouped by traffic source. For each
> source, tell me: traffic sessions, orders, revenue, and average order value.

**What CorpusIQ does behind the scenes:**

- Queries GA4 for traffic by source (sessions, users)
- Queries Shopify for orders by timestamp
- Matches orders to sessions by date and IP/user ID (where possible)
- Presents results side by side

**Expected output shape:**

```
Traffic Source | Sessions | Orders | Order Value | AOV
Direct         | 450      | 45     | $4,500      | $100
Organic Search | 320      | 32     | $3,200      | $100
Google Ads     | 210      | 35     | $5,250      | $150
...
```

(Numbers are examples; yours will be real from your data.)

### Example: Google Ads + Shopify

> Last month, break down my Google Ads spend by campaign and show me actual
> orders placed, revenue, and ROAS.

**Expected output:**

```
Campaign       | Spend  | Orders | Revenue | ROAS
Brand Keywords | $3,000 | 75     | $9,000  | 3.0
Product Promo  | $2,500 | 45     | $5,400  | 2.16
Competitor     | $1,500 | 12     | $1,800  | 1.2
...
```

### Example: Klaviyo + Shopify

> Which email campaigns drove the most revenue in Q2? Show me: sends,
> open rate, click rate, attributed orders, and attributed revenue.

**Expected output:**

```
Campaign Name       | Sends | Open Rate | Click Rate | Orders | Revenue
Summer Sale Flash   | 45k   | 28%       | 3.2%       | 180    | $18,000
New Product Launch  | 32k   | 22%       | 2.1%       | 95     | $9,500
...
```

## Part 3: Debug if something goes wrong

### Scenario: Empty results

You asked the question but got back something like:

> "I couldn't find any matching data."

**Troubleshooting:**

1. **Check both connectors are connected** — Go to CorpusIQ Connectors. Both should show **Connected** in green.

2. **Ask a simpler question per connector** — Try:
   - "Show me my GA4 account name" (tests GA4)
   - "Show me my Shopify company info" (tests Shopify)
   
   If one of these returns data, that connector works. If both fail, see [../troubleshooting/connector-shows-no-data.md](../troubleshooting/connector-shows-no-data.md).

3. **Check date range** — "Show me orders from the last 7 days" works. "Show me orders from 2025" won't (it's May 2026 in this example). Adjust to a date range where you know data exists.

4. **Ask CorpusIQ to show its work** — Follow up with:
   > "Show me the raw numbers. Which source did you use? GA4, Shopify, or both?"
   
   CorpusIQ will explain which connectors it queried and what it got back.

### Scenario: Numbers seem wrong

You got results but they don't match what you see in Shopify or GA4.

**Common causes:**

1. **Time zone mismatch** — GA4 and Shopify may use different timezones. Ask: "Show me the results in [your timezone] (EST / PST / UTC)."

2. **Different date ranges** — You looked at last quarter in Shopify but CorpusIQ queried a different date. Verify the dates in the answer match your question.

3. **Filtering differences** — You filtered by "Paid orders only" in Shopify, but CorpusIQ included all orders. Specify the filter in your question.

4. **Pending/draft orders** — Some tools show pending orders; others only final orders. Ask CorpusIQ: "Show me only completed/shipped orders."

5. **Different attribution** — Shopify tracks orders by order date; GA4 tracks sessions by session date. An order placed on Day 2 came from a session on Day 1. Results may differ by a day. This is normal.

**How to verify:**

Open Shopify and GA4 in parallel tabs. Pick a single metric (e.g., "orders placed on May 20") and verify both tools show the same number. If they don't, you've found the source of the discrepancy.

## Part 4: Tips for great cross-source questions

1. **Be specific about what you want** — "Show me revenue by source" is vague. "Show me revenue from Google Ads campaigns in May" is clear.

2. **Name the sources if multiple** — "Compare Shopify orders to Klaviyo-attributed revenue" tells CorpusIQ which connectors to pull from.

3. **Specify date ranges** — "Last 30 days" is safer than "this quarter" (time zones matter).

4. **Ask for breakdowns** — "Show me ... by [dimension]" is faster than "Show me each one."

5. **Request raw data if the answer seems off** — "Show me the raw numbers and which sources you used" forces CorpusIQ to explain itself.

## What to try next

Now that you have 2+ connectors:

- **[Browse the prompts library](../prompts/)** — See 60+ copy-paste questions organized by business impact. Many use 2–3 connectors.
- **[Read about skills](../how-it-works/skills-explained.md)** — Learn why complex questions work reliably.
- **[Check rate limits](../how-it-works/rate-limits-and-quotas.md)** — If you're running production queries, know the bounds.
- **[Explore advanced usage](#)** (coming soon) — Custom questions, canonical facts, skill invocation.

## Common questions

**Q: If I don't have both connectors, can I still use CorpusIQ?**  
A: Yes. Every question only uses the connectors you have. If you have only GA4, CorpusIQ can only answer traffic questions. Add more connectors to unlock more questions.

**Q: How long does a cross-source query take?**  
A: Usually 2–5 seconds for both APIs to respond. If either vendor is slow, it may take up to 30 seconds. Very rarely, 60 seconds.

**Q: Can I ask about more than 2 connectors at once?**  
A: Yes. Some of the best questions involve 4+ sources (e.g., "What's my real CAC?" = Google Ads + GA4 + Shopify + QuickBooks).

**Q: What if the connectors don't have overlapping data?**  
A: CorpusIQ will do its best to match them (by date, by customer ID, etc.). Some data won't match. It will tell you.

---

## Next

You've finished the quickstart. From here:

- **Run one of the [prompts](../prompts/)** that matches your business type.
- **Read [how it works](../how-it-works/)** to understand the substrate.
- **Troubleshoot** with [troubleshooting guide](../troubleshooting/).

---

**Powered by CorpusIQ**
