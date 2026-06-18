# Meta Ads (Facebook & Instagram)

## What it unlocks
Meta Ads is usually one of the largest line items in a SaaS or ecommerce budget, and Meta's own ROAS numbers are notoriously optimistic. Connecting Meta Ads lets CorpusIQ pull spend, impressions, clicks, and platform-reported conversions, then compare them honestly to GA4 sessions and Shopify revenue — so you can see what Meta actually drove, not what Meta claims it drove.

## Before you connect
- A Meta Business account with access to the ad account(s) you want to read
- Admin or analyst role on those ad accounts
- About 2 minutes

## How to connect
1. In CorpusIQ, open Settings → Connectors and find Meta Ads.
2. Click Connect.
3. Sign in to Facebook when the consent screen appears.
4. <!-- screenshot: Meta Ads OAuth consent — ad account selector -->
5. Choose which ad accounts CorpusIQ may read and approve `ads_read` access.
6. You'll be returned to CorpusIQ.

You'll see Meta Ads change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
Read-only access to:
- Ad accounts and their currency, status, and balance
- Campaigns, ad sets, and individual ads with creative details
- Account-level insights — impressions, clicks, spend, reach, frequency, CPM, CPC, CTR
- Campaign-level daily performance
- Breakdowns by age, gender, geography, device, platform, and placement

CorpusIQ never creates ads, edits budgets, or pauses campaigns.

## Questions you can ask
- "How much did I spend on Meta Ads last week?"
- "Which Facebook campaigns have the best CTR?"
- "Compare my Meta-reported conversions to GA4 conversions."
- "Show me daily spend on the spring sale campaign."
- "What's my true ROAS on Meta after attribution through GA4 and Shopify?"

## Troubleshooting
- **"No ad accounts found"** — Your Facebook user must be added as a person on the ad account in Business Manager. Page-level admin isn't enough.
- **"Permissions error on insights"** — Reconnect and make sure you approved the `ads_read` permission during OAuth.
- **Spend looks different than Meta UI** — Meta defaults to a 7-day click attribution window in some places and 1-day in others. CorpusIQ pulls raw spend, which always matches Billing & Payments, not the campaign UI's attributed numbers.
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
