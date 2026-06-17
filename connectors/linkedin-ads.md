# LinkedIn Ads

## What it unlocks
LinkedIn Ads is the primary paid-acquisition channel for B2B. Connecting it lets CorpusIQ pull campaign performance, creative analytics, and account-level spend — then line them up next to your CRM pipeline and revenue to see which LinkedIn campaigns actually closed deals.

## Before you connect
- A LinkedIn account with access to the ad accounts you want to read
- Your LinkedIn user must have at least a "Viewer" role on each ad account
- About 2 minutes

## How to connect
1. In CorpusIQ, open Settings → Connectors and find LinkedIn Ads.
2. Click Connect.
3. Sign in to LinkedIn when the consent screen appears.
4. <!-- screenshot: LinkedIn Ads OAuth consent screen -->
5. Approve read access and select the ad accounts you want CorpusIQ to see.
6. You'll be returned to CorpusIQ.

You'll see LinkedIn Ads change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
Read-only access to:
- Your ad account memberships and roles
- Sponsored ad accounts with names, currencies, and statuses
- Campaigns with objectives, budgets, statuses, and campaign groups
- Ad creatives with statuses and content references
- Daily campaign analytics: impressions, clicks, cost in local currency, and conversions
- Account-level lifetime analytics

CorpusIQ never creates campaigns, changes budgets, or modifies ads.

## Questions you can ask
- "How much did I spend on LinkedIn Ads last month?"
- "Which LinkedIn campaigns are driving the most clicks?"
- "Show me daily performance for my enterprise product campaign."
- "List all my LinkedIn ad accounts and their statuses."
- "Which creatives are running in my remarketing campaign?"

## Troubleshooting
- **"No ad accounts found"** — Your LinkedIn user doesn't have Viewer access to any ad account. Ask an account admin to add you in Campaign Manager → Account Settings → Manage Access.
- **"Insufficient permissions"** — Your role on the ad account may be too restrictive. You need at least Viewer access.
- **Campaign analytics return zero** — Check the date range. LinkedIn Ads reporting may lag by 24–48 hours.
- **Auth fails** — Reset the LinkedIn Ads connector in your dashboard and reconnect with the correct LinkedIn account.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
