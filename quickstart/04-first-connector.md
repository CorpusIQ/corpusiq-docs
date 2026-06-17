# 4. Authenticate your first connector

Pick a connector that holds data you actually care about. For most founders,
that's **QuickBooks** (the money) or **Google Analytics 4** (the traffic). This
guide uses QuickBooks as the worked example — substitute your tool, the flow
is the same.

## What's about to happen

You'll click a "Connect" button in CorpusIQ. Your browser will jump to
QuickBooks (or whichever tool), QuickBooks will ask "Allow CorpusIQ to read
your data?", you'll click **Allow**, and you'll land back on the CorpusIQ
dashboard with QuickBooks now marked **Connected**.

CorpusIQ requests **read-only** scopes wherever the vendor offers them. We do
not post, edit, or delete anything in your accounts.

## Steps

1. In CorpusIQ, open the **Connectors** page.
2. Find **QuickBooks** in the list. Click **Connect**.
3. A new browser tab opens to Intuit's login. Sign in with the QuickBooks
   account that owns your books. If you have multiple companies, you'll pick
   the right one.
4. QuickBooks will show a permission screen describing what CorpusIQ wants
   access to. Click **Connect** / **Authorize**.
5. The tab closes (or returns to CorpusIQ). The QuickBooks row in your
   connector list now says **Connected** with a timestamp.

**Screenshot:** CorpusIQ Connectors page with QuickBooks card highlighted  
**Screenshot:** Intuit OAuth approval/consent screen  
**Screenshot:** Connector list showing QuickBooks with "Connected" status

## Confirm in Claude or ChatGPT

Open Claude or ChatGPT and ask:

> Show me my QuickBooks company info.

You should get back the company name, address, fiscal year, and industry —
read live from your QuickBooks. If you do, you're wired up.

## Connect a few more

You'll get the most value from CorpusIQ when at least 3–4 connectors are
authenticated. Recommended starter set by business type:

| Business type | Recommended starter connectors |
|---|---|
| Ecommerce | Shopify, Klaviyo, Google Ads, Meta Ads, GA4, QuickBooks |
| SaaS | QuickBooks, HubSpot, GA4, Google Workspace (Gmail + Drive), Stripe-in-QB |
| Agency | QuickBooks, HubSpot, Google Workspace, Slack, Monday |
| Marketplace seller | Shopify or eBay or Amazon Seller or GunBroker, QuickBooks, Google Workspace |

Each connector has its own page under [connectors/](../connectors/) with
specific click-paths.

## Next

[5. Fire your first high-impact prompt →](05-first-prompt.md)

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
