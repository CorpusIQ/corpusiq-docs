# 5. Fire your first prompt

You're connected. Now ask something useful.

## The starter prompt

Open Claude or ChatGPT (with CorpusIQ wired in) and paste:

> How healthy is my business right now?

That's it. No keywords, no syntax, no parameters. Plain English.

## What happens behind the scenes

1. Claude (or ChatGPT) receives the question and sees it has a CorpusIQ tool
   available.
2. CorpusIQ's **skills engine** matches the question to the
   `executive-snapshot` skill — a pre-built runbook for "give me a one-page
   business overview".
3. The runbook fires queries against your connected sources: pulling cash
   position from QuickBooks, revenue trend from Shopify, ad spend from Google
   Ads and Meta, pipeline from HubSpot, traffic from GA4 — whatever you have
   connected.
4. The assistant synthesizes the results into a readable summary.

You'll see a response shaped roughly like this:

> **Cash position:** [a number with a delta vs last month]
> **Revenue last 30 days:** [a number with WoW change]
> **Top wins:** [2-3 bullets, e.g. best-selling SKU, biggest deal closed]
> **Top risks:** [2-3 bullets, e.g. overdue invoices over $X, ROAS dropping
> on Channel Y, pipeline stalled at stage Z]
> **What I'd focus on this week:** [a short prioritized list]

The actual numbers come from your accounts. We don't fake or estimate.

## What if a section is blank?

If CorpusIQ says something like "no ad data — Meta Ads not connected", that's
just a missing connector. Connect it and re-run the prompt.

## Now explore

The [Prompts library](../prompts/) has 60+ curated prompts grouped by category.
A few to try next:

- **Money:** [What's blocking our cash flow?](../prompts/revenue-and-finance.md)
- **Marketing:** [What's my true CAC and ROAS by channel?](../prompts/marketing-roas.md)
- **Multi-source:** [Draft a board update for last quarter](../prompts/multi-source.md)

## Next step

Ready to unlock the real power of CorpusIQ? Move to
[6. Your first cross-source query](06-first-cross-source-query.md) — connect a second tool and ask questions that span both.
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
