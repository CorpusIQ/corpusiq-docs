---
title: "Google Workspace - Gmail, Calendar, Drive, GA4, Ads"
description: "One Google connection for everything: Gmail, Calendar, Drive, GA4, Google Ads, and Search Console. Ask questions across all of it with cited answers."
---
# Google Workspace - Gmail, Calendar, Drive, GA4, Ads

## What it unlocks
Google Workspace is where most founders actually run their day - email, meetings, contracts, KPIs in a spreadsheet. It is also the single Google connection for everything Google: Analytics (GA4), Google Ads, and Search Console are all read through this one connector. Connecting it gives CorpusIQ read access to all of it in one go, so questions like "what did the agency promise me last month?", "what is my Google Ads spend?", or "what is on my calendar before the board meeting?" can pull straight from the original source.

## Before you connect
- A Google account (Workspace or personal Gmail both work)
- About 1 minute

## How to connect
1. In CorpusIQ, open Dashboard → Connectors and find Google Workspace.
2. Click Connect.
3. Sign in with the Google account you use for work.
4. <!-- screenshot: Google Workspace OAuth consent screen - scope list -->
5. Approve read access for Gmail, Calendar, and Drive when prompted.
6. You'll be redirected back to CorpusIQ.

You'll see Google Workspace change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
Read-only access to:
- **Gmail** - list and search messages, read individual messages
- **Calendar** - list your calendars, list upcoming events, get a specific event, search events by text
- **Drive** - list and search files, read file contents (Docs, PDFs, text), get Drive storage stats
- **Sheets** - read ranges from any spreadsheet you have access to
- **Google Analytics (GA4)** - traffic, sessions, users, conversions, acquisition
- **Google Ads** - campaigns, ad groups, keywords, spend, clicks, conversions, search terms
- **Search Console** - organic clicks, impressions, queries, pages, CTR

All of these come through the one Google Workspace connection. You do not connect GA4, Google Ads, or Search Console separately - they are included in this connector. The Google account you sign in with must have access to each Google product you want to read (for Ads, the account must be a user on the Ads customer ID).

## Google Ads permissions (exact scope)

The Google Ads API publishes one permission scope: `https://www.googleapis.com/auth/adwords`. Google offers no read-only variant of this scope, so the consent screen asks for it as-is. The CorpusIQ Google Ads tools are retrieval tools only: they run reporting queries and have no code path that writes, edits, or executes anything in your Ads account. The other Google permissions requested alongside it (Gmail, Drive, Sheets, GA4, Search Console) are Google's explicit `.readonly` scopes.

**Read-only guarantee:** CorpusIQ cannot change campaigns, budgets, bidding, targeting, or keywords. It only reads. It is not an AI agent and does not retain raw customer files or full connector response payloads; no one at CorpusIQ can access your account. Full details: [Security and Read-Only Access](/docs/hermes/security/read-only-and-security)

CorpusIQ never sends mail, creates events, edits files, or shares anything.

## Questions you can ask
- "Find the email thread from the agency about September spend."
- "What's on my calendar for next Tuesday?"
- "Pull the KPI numbers from cell B2:B12 of my Q3 metrics sheet."
- "How much did I spend on Google Ads last month?"
- "What were my organic clicks from Search Console last week?"
- "How many users did my site get this month in GA4?"
- "Find the latest contract draft in my Drive."
- "Summarize today's meetings."

## Troubleshooting
- **"Insufficient permissions"** - Google asks you to approve each scope on a separate checkbox. Reconnect and make sure you tick all of them.
- **Workspace admin blocks the app** - Some Workspace admins restrict third-party apps. Ask your admin to allow CorpusIQ, or sign in with a personal Google account.
- **Sheet read returns empty** - Confirm the spreadsheet ID and the range string (e.g. `Sheet1!A1:C10`). The ID is the long token in the sheet URL.

<!-- DOC-GAP: No internal SETUP doc exists. Setup steps inferred from registry + vendor public docs. Verify before publish. -->
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
