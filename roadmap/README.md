# Roadmap

What's live, what we're building, and what's on the list. This page is kept
current from the actual connector registry and the open work in our tracker —
it's not a wish list someone forgot to update.

Want something that isn't here? **[Open an Idea](https://github.com/CorpusIQ/corpusiq-docs/discussions/categories/ideas)**
in Discussions. Ideas have upvotes — the ones the community pushes to the top
are the ones we look at first.

One honest caveat: "Planned" means we intend to build it, not that there's a
ship date. Priorities move when customer pull moves them. If a date matters to
you, say so in the Idea thread and we'll tell you straight where it sits.

---

## ✅ Live now

37+ connectors are connected and answering questions in production today. The
full list with setup guides is in the [Connectors index](../connectors/). The
highlights:

- **Finance & ops** — QuickBooks, Stripe, Shopify, Amazon Seller, eBay, Odoo
- **Marketing & ads** — Google Ads, Meta Ads, LinkedIn Ads, Klaviyo, Mailchimp,
  ActiveCampaign, Constant Contact, PostScript SMS
- **Analytics & SEO** — Google Analytics 4, Search Console, PostHog, Semrush,
  Ahrefs
- **CRM & sales** — HubSpot, Close, GoHighLevel
- **Productivity & data** — Google Workspace, Microsoft 365 (Outlook, OneDrive),
  Dropbox, Slack, Notion, Airtable, Monday.com, Calendly, PostgreSQL, MS SQL,
  MongoDB, Cosmos DB
- **Content** — YouTube, TikTok
- **Cross-source** — ads + analytics correlation, email + multi-source
  attribution

Plus the **Canonical Layer** (your declared business facts) and **CorpusIQ
Usage** stats.

> A few recently-shipped connectors (Notion, Close, Stripe, Ahrefs, LinkedIn
> Ads) are live in production but their dedicated setup pages are still being
> written. They work today — the docs are catching up.

## 🔨 Building

Work that's actively in progress:

- **Reliability hardening** — cutting the long-tail latency on heavy tool calls
  so big result sets return fast and predictably ([#319](https://github.com/CorpusIQ/multi-source-mcp/issues/319)).
- **Stripe read-surface expansion** — deeper payment-intelligence coverage
  beyond the core reconciliation tools ([#247](https://github.com/CorpusIQ/multi-source-mcp/issues/247)).
- **Shopify embedded admin app** — install CorpusIQ directly from the Shopify
  admin, meeting App Store review requirements ([#226](https://github.com/CorpusIQ/multi-source-mcp/issues/226)).
- **MCP directory listings** — getting CorpusIQ into the Anthropic MCP directory
  and the official MCP ecosystem registry so it's discoverable ([#216](https://github.com/CorpusIQ/multi-source-mcp/issues/216)).

## 🗺️ Planned

On the list, not yet started. Upvote the matching Idea to move it up:

- **New connectors** — Zendesk (support ops, [#215](https://github.com/CorpusIQ/multi-source-mcp/issues/215)),
  Linear (issue tracking, [#214](https://github.com/CorpusIQ/multi-source-mcp/issues/214)).
- **HubSpot expansion** — go beyond CRM to deals, marketing, and email
  sequences ([#210](https://github.com/CorpusIQ/multi-source-mcp/issues/210)).
- **Self-hosted deployment** — a run-it-in-your-own-cloud option for
  privacy-critical customers ([#207](https://github.com/CorpusIQ/multi-source-mcp/issues/207)).
- **Workflow triggers** — connector-to-connector automation so one event can
  drive an action across sources ([#206](https://github.com/CorpusIQ/multi-source-mcp/issues/206)).

## 🧊 Parked

Real requests we've heard, deliberately deferred until enough customers ask:

- **Enterprise-tier connectors** — Salesforce, Workday, NetSuite, ServiceNow.
  Big builds; we'll start when there's clear pull ([#211](https://github.com/CorpusIQ/multi-source-mcp/issues/211)).

---

## How priorities get set

Three inputs, roughly in this order:

1. **Reliability and correctness** of what's already live. A connector that
   gives a wrong answer beats ten that don't exist yet — so bugs jump the queue.
2. **Customer pull** — upvoted Ideas, support requests, and direct asks from
   people actually using CorpusIQ.
3. **Strategic coverage** — filling obvious gaps in the categories above.

If you want to influence the order, the single most effective thing you can do
is open or upvote an [Idea](https://github.com/CorpusIQ/corpusiq-docs/discussions/categories/ideas)
and explain what you're trying to do with it. "I need X to answer Y about my
business" is worth more than a +1.

Powered by CorpusIQ.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
