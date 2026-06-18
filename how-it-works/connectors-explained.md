# Connectors, explained

A **connector** is a one-way, read-only link between CorpusIQ and one of
your SaaS tools. Today there are 31 of them. The list grows every month.

## What a connector does

When you authenticate a connector — say, Shopify — three things happen:

1. You're sent to Shopify's login page (not CorpusIQ's). You sign in
   there, just like you would normally.
2. Shopify shows you a consent screen listing exactly what CorpusIQ is
   asking permission to read: orders, products, customers, etc. You
   approve.
3. Shopify hands CorpusIQ a token. CorpusIQ stores it encrypted, scoped
   to your account only. From then on, when you ask a question that
   involves Shopify, CorpusIQ uses that token to read your data.

That's it. CorpusIQ never sees your Shopify password. The token can be
revoked from Shopify's admin panel at any time, or by disconnecting the
connector from inside CorpusIQ.

## Why you have to authenticate

The alternative is screenshots. You log into Shopify, screenshot the
revenue chart, paste it into Claude, and ask Claude to interpret it. You
do that across ten tools and the founder's afternoon is gone.

OAuth eliminates the screenshot step. You authenticate once. After that,
CorpusIQ reads the live data automatically when a question needs it.

## What "OAuth" means

OAuth is a standard handshake — the same one behind every "Sign in with
Google" button — for letting one app read data from another **without**
ever sharing your password. You log in directly with the vendor (Google,
Shopify, QuickBooks), the vendor shows you what's being requested, and
you approve. The vendor stays in control. You can revoke access from
their side whenever you want.

If you've ever connected Zapier or Make to a tool, this is the same
flow.

## Read-only, every time

CorpusIQ asks for **read** scopes only. It can pull your sales data; it
cannot place an order. It can pull your QuickBooks P&L; it cannot create
an invoice. It can read Klaviyo lists; it cannot send a campaign.

This is a deliberate product decision. Writing to vendor accounts is the
single largest source of "agentic AI went wrong" stories. CorpusIQ
doesn't take that risk on your behalf.

## The 31 connectors today

Storefronts and finance: Shopify, QuickBooks, Amazon Seller, eBay,
GunBroker.

Ad platforms: Google Ads, Meta Ads (Facebook + Instagram), TikTok.

Analytics: GA4, Search Console, Semrush, YouTube.

Email and SMS marketing: Klaviyo, Mailchimp, ActiveCampaign, Constant
Contact, PostScript.

CRM and pipeline: HubSpot, LeadConnector (GoHighLevel), Calendly,
Monday, Airtable, Odoo.

Productivity: Google Workspace (Drive, Gmail, Sheets, Calendar),
Microsoft 365 (OneDrive, Outlook), Dropbox, Slack.

Databases: PostgreSQL, MSSQL, MongoDB, Cosmos DB.

The full per-connector setup guides are in
[../connectors/](../connectors/).

## When a connector isn't enough

Some questions need three or four connectors at once. "What's my real
CAC?" pulls from every ad platform, GA4, and Shopify or QuickBooks. You
don't have to know that — the skills engine handles it. See
[skills-explained.md](skills-explained.md).

## When you want it off

Disconnect any connector from the CorpusIQ status panel. The token is
deleted from CorpusIQ's storage. The vendor's side will also show the
app as removed once the token expires (most fire-and-forget tokens are
gone within an hour; refresh tokens are wiped immediately on
disconnect).

You can reconnect at any time. There is no penalty for switching off and
back on.
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
