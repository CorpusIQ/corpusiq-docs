# What is CorpusIQ?

Every business runs on twelve to twenty SaaS tools. Shopify for the store.
QuickBooks for the books. Google Ads and Meta Ads for the spend. HubSpot
for the pipeline. Klaviyo for email. GA4 for traffic. Slack for everything
else.

None of them talk to each other.

So when you ask the simple question — "how is my business doing?" — there's
no single place to look. You log into Shopify. Then QuickBooks. Then the
ad accounts. Then HubSpot. You screenshot a chart from each, paste them
into a doc, and try to draw a conclusion. It takes hours. You do it once
a quarter. The rest of the time you're flying on instinct.

CorpusIQ fixes that.

## What it is

CorpusIQ connects to all your business tools (31 connectors today, more
every month) and puts an AI agent on top of them. You ask the agent a
question in plain English, in Claude or ChatGPT, and it figures out which
systems to query, runs the queries, and gives you the answer.

You don't pick the connectors. You don't write the queries. You don't
stitch anything together. You ask. It answers.

## The three pieces

**Connectors.** One-way, read-only links to your SaaS tools. You
authenticate each one once via OAuth (the same flow you've used a hundred
times — "Sign in with Google" and the like). CorpusIQ then reads your
data when you ask a question. It never writes back to your tools.

**Skills engine.** When you ask a complex question, CorpusIQ doesn't
blindly query everything. It routes your question to a *skill* — an
opinionated procedure that knows which connectors to hit, in what order,
and how to present the answer. The same question always runs the same
play. Results are predictable.

**The AI agent.** You talk to CorpusIQ through Claude Desktop or ChatGPT
(custom GPT). The agent uses CorpusIQ's tools to fetch data, runs the
skills, and writes the answer in your chat. You can ask follow-ups.

## What it's not

It's not a dashboard. There's no UI to click around in. You ask
questions; you get answers.

It's not a data warehouse. CorpusIQ doesn't copy your data into a giant
database. It queries your tools live when you ask.

It's not a replacement for your SaaS tools. Shopify is still the source
of truth for orders. QuickBooks is still the source of truth for books.
CorpusIQ just reads them.

## Who it's for

Founders, operators, and finance leads who already use ten or more SaaS
tools and are tired of the screenshot routine. If your business runs on
five spreadsheets and one tool, you don't need CorpusIQ yet.

## What's next

- [connectors-explained.md](connectors-explained.md) — what a connector
  actually is.
- [skills-explained.md](skills-explained.md) — why the answers are
  consistent.
- [privacy-and-security.md](privacy-and-security.md) — what CorpusIQ
  does and doesn't do with your data.
- [../quickstart/](../quickstart/) — get connected in 10 minutes.
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
