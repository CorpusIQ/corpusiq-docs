---
description: >-
  How to ask CorpusIQ good questions in Slack and Teams, what the answers look
  like, and a set of prompts worth trying across finance, ads, ecommerce, and
  more.
canonical: "https://www.corpusiq.io/docs/chat-apps/asking-questions/"
robots: "index,follow"
last_updated: "2026-10-07"
title: "Asking questions - CorpusIQ Docs"
tags: ["hermes agent", "ai agent", "documentation"]

---

# Asking questions

Once you're linked and your AI key is set, this is the whole job: ask, read,
ask again. This page is about asking well and knowing what you'll get back.

## How to ask

- **Direct message** the app for a private answer only you see.
- **In Slack channels**, @-mention the app (`@CorpusIQ ...`) when the answer
  belongs to the whole channel.
- **In Teams group chats and team channels**, mention the bot and send
  `corpusiq-share <question>` only when you intend to disclose the answer to
  everyone who can read that conversation. An ordinary question receives
  privacy guidance instead of business data. The request uses your own
  CorpusIQ identity and AI configuration, not a shared account. See
  [Teams setup](getting-started-teams.md) for private account linking.

Ask the way you'd ask a colleague who has all the numbers in front of them.
Use plain English for the question; in a shared Teams conversation, keep the
`corpusiq-share` prefix:

> How did revenue compare to last month?

You don't need to name the tool. CorpusIQ works out that "revenue" means your
accounting or payments data and goes there. If a question could mean two things,
it's fine to say which - "revenue from Stripe" or "orders in Shopify" - but you
rarely need to.

## Follow-ups work

Answers live in a thread, and you can keep going in it. Ask a broad question,
then narrow:

> How did sales do last week?

> Just the online store.

> Now break that down by product.

Where conversational context is available, each reply can build on the last.
Teams shared answers do not create persistent team-wide AI memory: include
enough context in each `corpusiq-share` request for it to stand on its own.

## What the answers look like

CorpusIQ replies with the numbers laid out, not buried in a paragraph. Key
figures come back as tiles in Slack and as cards in Teams - a revenue figure, a
change versus the prior period, a count of orders - so you can read the result
at a glance. Longer explanations come as short text above or beside the tiles.

When a question spans several tools, the answer pulls them together. When it
needs a tool you haven't connected, the reply says so and gives you a way to
connect it rather than guessing.

Two things CorpusIQ won't do: invent a number it can't source, or quietly leave
out a tool it couldn't reach. If data is missing, it tells you.

## Questions worth trying

A starter set across the common areas. Use the ones that match what you've
connected.

### Money and finance

> How much revenue did we bring in last month, and how does that compare to the
> month before?

> What are our biggest outstanding invoices right now?

> What did we spend with our top five vendors this quarter?

### Ads and marketing

> Which ad campaigns had the best return last week?

> Where are we spending the most and getting the least back?

> How did our email campaigns perform this month - opens, clicks, revenue?

### Store and orders

> How many orders are waiting to ship?

> What are my best-selling products in the last 30 days?

> Which products are running low on stock?

### Customers and pipeline

> Which deals are closing this month?

> Who are my highest-value customers this year?

> How many new leads did we get last week, and where did they come from?

### Web and search

> How much traffic did the site get last week, and where did it come from?

> Which pages get the most visits but the fewest sign-ups?

### Across everything

> Give me a quick read on how the business is doing this month.

> What changed the most week over week?

That last kind - the broad "how are we doing" question - is where the chat app
earns its place. An intentionally shared answer lets the conversation discuss
the same result, drawn live from your connected tools. In Teams, use
`corpusiq-share` and disclose only data you are authorized to share with those
participants.

## If an answer looks off

CorpusIQ shows where a number came from. If something looks wrong, the usual
cause is a tool that isn't connected or a question that could be read two ways.
Ask it to be specific - name the tool or the date range - and see
[troubleshooting.md](troubleshooting.md) if it persists.
