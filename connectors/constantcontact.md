# Constant Contact

## What it unlocks
If Constant Contact is where your email lives, this connector pulls campaign performance and contact lists into the same view as your Shopify revenue and GA4 sessions. That's what makes questions like "did last week's newsletter actually drive traffic?" answerable.

## Before you connect
- A Constant Contact account with admin access
- About 2 minutes

## How to connect
1. In CorpusIQ, open Settings → Connectors and find Constant Contact.
2. Click Connect.
3. Sign in to Constant Contact when the consent screen appears.
4. <!-- screenshot: Constant Contact OAuth consent screen -->
5. Approve read access and you'll be redirected back to CorpusIQ.

You'll see Constant Contact change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
Read-only access to:
- Email campaigns and their status (sent, scheduled, draft)
- Contacts, with search and filtering
- Contact lists

CorpusIQ never sends mail or edits contacts.

## Questions you can ask
- "Show me my last 10 Constant Contact campaigns."
- "How big is each of my email lists?"
- "Find contacts whose email contains 'gmail.com'."
- "What's scheduled to send this week?"
- "Compare my email send days to GA4 traffic spikes."

## Troubleshooting
- **"Token expired"** — Constant Contact tokens refresh automatically, but if you see this, disconnect and reconnect.
- **Empty contact list** — Make sure the account you authorized actually owns the lists you're expecting.
- **Campaign metrics look low** — The connector returns send-level data, not deep engagement metrics; for opens and clicks check the Constant Contact UI directly.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
