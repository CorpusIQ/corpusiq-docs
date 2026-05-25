# The skills engine, explained

This is the part of CorpusIQ that makes the answers good.

## The naive way (which we don't do)

Imagine you ask Claude — without CorpusIQ — "how healthy is my
business?" It has 31 connectors available. What does it do?

It guesses. Maybe it asks Shopify for revenue. Maybe it forgets to ask
QuickBooks. Maybe it pulls GA4 sessions but skips the ad accounts. The
next time you ask the same question, it makes different guesses. The
answers don't match. You can't compare last month to this month because
the model didn't run the same play twice.

That's the failure mode of "agent + a pile of tools." Without structure,
you get a different shape of answer every time.

## What CorpusIQ does instead

When you ask a broad business question, CorpusIQ routes it to a
**skill** — an opinionated, multi-step procedure that knows exactly:

- Which connectors to hit (and in what order).
- What metrics to compute from the raw data.
- How to present the answer (sections, headings, what goes in the
  appendix).

Same question, same procedure, same answer shape. Every time. Month
over month, the numbers are comparable because they came from the same
play.

## A concrete example

You ask: *"What's my true CAC and ROAS by channel?"*

CorpusIQ routes this to the **ad-spend-truth-report** skill. The runbook
says:

1. Pull spend, clicks, and self-reported conversions from Google Ads.
2. Same for Meta Ads.
3. Same for TikTok.
4. Pull GA4 sessions and conversion events by source.
5. Pull actual revenue from Shopify (or QuickBooks if it's a non-store
   business).
6. Join ad spend → GA4 sessions → Shopify revenue at the channel level.
7. Compute CAC and ROAS per channel using **revenue from Shopify**, not
   the ad platforms' optimistic numbers.
8. Format as a per-channel matrix with a verdict.

That's 6 connectors and a specific order of operations. The skill knows
it. You don't have to.

## A few skills in the catalog

Every one of these is a real runbook with a specific output shape:

- **executive-snapshot** — "How healthy is my business?" Cash, revenue,
  wins, risks, focus list across QuickBooks, Shopify, HubSpot, ad
  accounts, GA4, email, calendar.
- **ad-spend-truth-report** — the CAC/ROAS reconciliation above.
- **board-update-drafter** — "Draft a board update for last quarter."
  Pulls financials, KPIs, prior updates from Drive for tone, writes the
  document.
- **financial-command-center** — full financial health check: cash,
  concentration risk, expense anomalies, late-payment patterns.
- **ecommerce-command-center** — full store review across Shopify, ads,
  GA4, and QuickBooks.
- **data-discrepancy-detector** — "Why don't my Shopify and QuickBooks
  numbers match?" Side-by-side with the gaps explained.
- **customer-health-scorecard** — every active account scored Healthy /
  At Risk / Critical, with the driving signal.

There are over a hundred more. You don't browse them. CorpusIQ picks the
right one based on your question.

## When there's no matching skill

If your question is narrow ("show me last week's Shopify orders"),
there's no skill to route to. CorpusIQ just queries the one connector
directly and gives you the data.

If your question is huge and ambiguous ("tell me everything"), CorpusIQ
will ask you to narrow it down or suggest a likely skill to run.

## Why this matters to you

Three things.

**Consistency.** Last month's executive snapshot and this month's were
produced by the same procedure. Variance is real change, not the
model's mood.

**Quality.** Each skill was designed by someone who knows what the
right answer looks like. You're not relying on the model to figure it
out from scratch.

**Speed.** You don't have to write a 400-word prompt every time. "Run
the executive snapshot" is enough.

## What's next

- [../prompts/](../prompts/) — the prompts that trigger these skills,
  organized by the question you're trying to answer.
- [privacy-and-security.md](privacy-and-security.md) — what happens to
  the data the skills pull.
