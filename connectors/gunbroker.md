# GunBroker

## What it unlocks
GunBroker is the primary marketplace for firearms sellers, and its data — active listings, watchers, sold revenue, fraud claims — lives nowhere else. Connecting it lets CorpusIQ answer questions about inventory, sell-through, fees, and buyer disputes in plain English, alongside the rest of your business data.

## Before you connect
- A GunBroker seller account
- Your GunBroker username and password (used once to generate an API token on your behalf)
- About 2 minutes

## How to connect
1. In CorpusIQ, open Settings → Connectors and find GunBroker.
2. Click Connect.
3. <!-- screenshot: GunBroker credential setup form in CorpusIQ -->
4. Enter your GunBroker username and password in the secure form.
5. Click Save. CorpusIQ exchanges the credentials for an API token and discards the password.

You'll see GunBroker change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
Read-only access to:
- Your account summary, seller rating, and standing
- Active listings with bids, watchers, end dates, and title
- Sold items, unsold (expired) items, and scheduled launches
- Inventory summary with exact counts
- Watched items
- Orders with buyer info, item, amount, and fulfillment status
- Feedback you've received
- Open fraud or dispute claims
- Billing — listing fees, final value fees, account charges
- Marketplace search and category browsing
- FFL lookups by buyer ZIP code

CorpusIQ never lists items, edits prices, or contacts buyers.

## Questions you can ask
- "How many active GunBroker listings do I have right now?"
- "What did I sell on GunBroker in the last 30 days?"
- "Show me listings ending in the next 24 hours."
- "Are there any open fraud claims on my account?"
- "Find an FFL near ZIP 30303."

## Troubleshooting
- **"Invalid credentials"** — GunBroker is case-sensitive on username. Double-check capitalization and try again.
- **Two-factor blocking login** — Temporarily disable 2FA, connect, and re-enable. CorpusIQ keeps a long-lived API token after the first login.
- **Empty inventory summary** — If you have no active listings, the summary returns zeros. Check active listings directly to confirm.

<!-- DOC-GAP: No internal SETUP doc exists. Setup steps inferred from registry + vendor public docs. Verify before publish. -->
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
