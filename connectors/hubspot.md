# HubSpot

## What it unlocks
HubSpot is where your sales pipeline, customer relationships, and deal history live. Connecting it lets CorpusIQ answer "how is my pipeline doing?" and pull a full account 360 for any customer — relationship history, deal state, open items — by combining HubSpot with email, calendar, and billing data from your other connectors.

## Before you connect
- A HubSpot account with admin access
- About 2 minutes

## How to connect
1. In CorpusIQ, open Settings → Connectors and find HubSpot.
2. Click Connect.
3. Sign in to HubSpot when the consent screen appears.
4. <!-- screenshot: HubSpot OAuth scope approval screen -->
5. Choose the HubSpot account (portal) you want to authorize and approve read access.
6. You'll be returned to CorpusIQ.

You'll see HubSpot change from gray to green in your CorpusIQ dashboard.

## What CorpusIQ can see
Read-only access to:
- Account and portal metadata
- Contacts, with full details and keyword search
- Companies, with full details
- Deals, with full details

CorpusIQ never creates contacts, moves deals, or sends sequences.

## Questions you can ask
- "Pull together everything I need to know about Acme Corp."
- "How many deals are in the negotiation stage?"
- "Search HubSpot for contacts at 'Stripe'."
- "Show me my top 10 deals by amount."
- "Score my customer portfolio by health."

## Troubleshooting
- **"Wrong portal"** — HubSpot prompts you to pick a portal during OAuth. If you authorized the wrong one, disconnect and reconnect.
- **"Insufficient scopes"** — Reconnect and make sure all requested scopes are checked. Free HubSpot accounts may not grant some object scopes.
- **Search returns nothing** — HubSpot search indexes a subset of fields. Try the full name or email instead of a partial match.
