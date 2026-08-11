# The Source of Truth Problem — Why Every Business Dashboard Lies

Every business runs on numbers. Revenue. Margin. Churn. CAC. LTV. These numbers determine budgets, hiring, strategy, and survival.

Here is the problem: none of your tools agree on what these numbers mean.

## The Same Metric, Four Different Answers

Ask four different tools for your monthly revenue:

**Shopify** counts gross merchandise value. Every order at full price. Discounts applied later. Refunds processed separately. 

**Stripe** counts processed payments. Net of fees. Net of refunds. Different settlement timing than order date.

**QuickBooks** counts invoiced revenue. Based on accounting rules. Accrual or cash basis. Different recognition dates than transaction dates.

**GA4** counts attributed revenue. Only from tracked channels. Attribution windows vary. Cross-device de-duplication changes numbers.

Four tools. Four different definitions of revenue. All of them are correct. None of them agree.

## Why This Matters

When your team sits down on Monday morning to review the numbers, someone is always wrong. Not because they made a mistake. Because they pulled from a different source. 

The Shopify person says $142,000. The QuickBooks person says $138,000. The Stripe person says $135,000. The argument is not about accuracy. It is about definitions. And nobody wrote down what revenue actually means.

## The Fix: Declared Source of Truth

Before you can automate anything, you must define what you are measuring. Not in a dashboard tool. Not in a spreadsheet. In a declaration that every system references.

For revenue, the declaration might be: "Gross order value from Shopify at the time of order placement, excluding tax and shipping, for orders with status not equal to cancelled or fully refunded."

Every system can then be evaluated against this definition. The numbers still will not match perfectly. But now you know why they differ. And you know which number is the official one.

## Beyond Revenue

This problem affects every metric:

- **Customer count**: Shopify counts customers by email. Stripe by payment method. HubSpot by contact record. Three different counts of the same people.
- **Churn**: Subscription cancellation vs. payment failure vs. no-login-in-90-days. Three different definitions, three different churn rates.
- **Margin**: Revenue minus cost of goods. But which revenue definition? Which cost inclusion rules? Direct costs only or allocated overhead?

## What This Means for AI

When you connect AI to your business tools, the definition problem becomes critical. The AI will pull from multiple sources. If revenue is not defined, the AI will reconcile the numbers however it sees fit. You will get an answer. You will not know if it is right.

The solution is to define each metric once, store those definitions as canonical facts, and have every AI query reference them. The AI does not decide what revenue means. You do. The AI just does the math.

## The Bottom Line

Your dashboard is not lying to you. It is just answering a different question than you think you asked. Define the question first. Then build the dashboard. Or better yet, let AI answer questions against your definitions, not against the default ones each vendor ships.

Consistent answers require consistent definitions. Everything else is just four different numbers on one screen.
