# Google Ads

## What it unlocks
Google Ads is often the single largest acquisition channel, and the platform's reported conversions rarely match what GA4 or your CRM actually see. Connecting Google Ads lets CorpusIQ pull spend, clicks, impressions, and conversions at the campaign, ad group, keyword, and search-term level — then line them up next to GA4 sessions and revenue so you can see your real CAC.

## Before you connect
- A Google account with access to the Google Ads customer ID you want to read
- If you use a manager account (MCC), know which login customer ID to use
- About 2 minutes

## How to connect
1. In CorpusIQ, open Settings → Connectors and find Google Ads.
2. Click Connect.
3. Sign in with the Google account that has access to your Ads account.
4. <!-- screenshot: Google Ads OAuth consent screen -->
5. Approve read access and you'll be returned to CorpusIQ.

You'll see Google Ads change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
Read-only access to:
- All Google Ads accounts your Google user can see
- Account-level performance summaries
- Campaigns with impressions, clicks, cost, conversions, CTR, and CPC
- Ad groups and individual ads
- Keyword performance with quality scores and impression share
- Search terms — the actual queries that triggered your ads
- Breakdowns by geography, device, age, and gender
- Custom GAQL queries for anything else

CorpusIQ never creates campaigns, changes bids, or pauses ads.

## Questions you can ask
- "How much did I spend on Google Ads last month?"
- "Which keywords have the best conversion rate?"
- "Show me search terms that are wasting budget on brand keywords."
- "Compare my Google Ads conversions to GA4 conversions by day."
- "What's my true CAC and ROAS by channel?"

## Troubleshooting
- **"No accounts found"** — The Google user you signed in with doesn't have access to any Ads account. Add yourself in Google Ads → Tools → Access and Security.
- **MCC errors** — If you manage accounts through an MCC, you'll need to pass the manager customer ID as `login_customer_id` when querying client accounts.
- **Conversion counts seem low** — Google Ads only counts conversions configured in the Ads conversion settings. If you rely on GA4 imported conversions, check that the import is active.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
