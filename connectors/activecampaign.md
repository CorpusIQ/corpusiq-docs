# ActiveCampaign

## What it unlocks
ActiveCampaign holds your email contacts, automations, and pipeline deals — the moment-by-moment record of how prospects move from a first open to a closed sale. Connecting it lets CorpusIQ answer questions about list health, campaign performance, and which automations are actually pulling weight, alongside revenue data from Shopify, QuickBooks, and GA4.

## Before you connect
- An ActiveCampaign account with admin access
- Your ActiveCampaign API URL and API key (Settings → Developer)
- About 2 minutes

## How to connect
1. In CorpusIQ, open Settings → Connectors and find ActiveCampaign.
2. Click Connect.
3. <!-- screenshot: ActiveCampaign credential form in CorpusIQ -->
4. In a second tab, sign in to ActiveCampaign and go to Settings → Developer.
5. Copy your API URL and API key.
6. Paste both into the CorpusIQ form and click Save.

You'll see ActiveCampaign change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
Read-only access to:
- Contacts and contact details, with search
- Lists and tags
- Email campaigns and per-campaign performance
- Automations
- Deals in your pipeline
- Account info

CorpusIQ never sends mail, edits contacts, or changes automations.

## Questions you can ask
- "How did my last ActiveCampaign campaign perform?"
- "Which automations have the most active contacts?"
- "Show me deals that have been open longer than 30 days."
- "How big is each of my lists?"
- "Find every contact tagged 'webinar-april'."

## Troubleshooting
- **"Invalid API key"** — Regenerate the key in ActiveCampaign (Settings → Developer) and paste the new value.
- **API URL wrong** — It must be your full account URL like `https://youraccount.api-us1.com`, not the dashboard URL.
- **Empty campaign list** — Your API user may not have permission for the campaign view; switch to an admin-level key.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
