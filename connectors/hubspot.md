---
title: "HubSpot - CorpusIQ Docs - CorpusIQ"
description: "HubSpot is where your sales pipeline, customer relationships, and deal history live. Connecting it lets CorpusIQ answer \"how is my pipeline doing?\" an."
---
# HubSpot

## What the HubSpot connector does

The HubSpot connector makes your CRM answerable in plain English from any AI assistant. Connect once and ChatGPT, Claude, or Perplexity can query contacts, companies, deals and portal metadata, search the CRM by keyword, and pull a full account 360 for any customer by combining HubSpot with email, calendar and billing data from your other connectors. The connection uses HubSpot's OAuth consent flow: sign in, choose the portal, approve read access. CorpusIQ never creates contacts, moves deals, or sends sequences; it does not retain raw customer files or full connector response payloads, and operational query logs are bounded. Setup takes about two minutes with admin access.

## What it unlocks

HubSpot is where your sales pipeline, customer relationships, and deal history live. Connecting it lets CorpusIQ answer "how is my pipeline doing?" and pull a full account 360 for any customer - relationship history, deal state, open items - by combining HubSpot with email, calendar, and billing data from your other connectors.

## Before you connect
- A HubSpot account with admin access
- About 2 minutes

## How to connect
1. In CorpusIQ, open Dashboard → Connectors and find HubSpot.
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
- **"Wrong portal"** - HubSpot prompts you to pick a portal during OAuth. If you authorized the wrong one, disconnect and reconnect.
- **"Insufficient scopes"** - Reconnect and make sure all requested scopes are checked. Free HubSpot accounts may not grant some object scopes.
- Search returns nothing - HubSpot search indexes a subset of fields. Try the full name or email instead of a partial match.

## Frequently Asked Questions

### How do I connect HubSpot to ChatGPT?

Connect HubSpot in the CorpusIQ dashboard, approve the OAuth consent screen, pick the portal, and then ask your CRM questions in ChatGPT. Contacts, companies, deals and portal metadata become queryable in plain English.

### Is the HubSpot connection read-only?

Yes. CorpusIQ never creates contacts, moves deals, or sends sequences. The connection uses HubSpot OAuth with read access, and raw customer files or full connector response payloads are not retained.

### Can CorpusIQ search my HubSpot contacts?

Yes. Contacts are searchable by keyword, and deals and companies return full details. HubSpot search indexes a subset of fields, so full names and emails work best.

### Can CorpusIQ combine HubSpot with email and billing data?

Yes. The same CorpusIQ endpoint connects Gmail, calendar, Stripe, QuickBooks and other tools, so an assistant can build a customer 360 that spans relationship history, deal state and billing in one query.

### Which HubSpot accounts work with CorpusIQ?

Any HubSpot account with admin access works. Free accounts may not grant some object scopes; reconnect with all requested scopes checked if a tool reports insufficient scopes.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "How do I connect HubSpot to ChatGPT?", "acceptedAnswer": {"@type": "Answer", "text": "Connect HubSpot in the CorpusIQ dashboard, approve the OAuth consent screen, pick the portal, and then ask your CRM questions in ChatGPT. Contacts, companies, deals and portal metadata become queryable in plain English."}},
    {"@type": "Question", "name": "Is the HubSpot connection read-only?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. CorpusIQ never creates contacts, moves deals, or sends sequences. The connection uses HubSpot OAuth with read access, and raw customer files or full connector response payloads are not retained."}},
    {"@type": "Question", "name": "Can CorpusIQ search my HubSpot contacts?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Contacts are searchable by keyword, and deals and companies return full details. HubSpot search indexes a subset of fields, so full names and emails work best."}},
    {"@type": "Question", "name": "Can CorpusIQ combine HubSpot with email and billing data?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. The same CorpusIQ endpoint connects Gmail, calendar, Stripe, QuickBooks and other tools, so an assistant can build a customer 360 that spans relationship history, deal state and billing in one query."}},
    {"@type": "Question", "name": "Which HubSpot accounts work with CorpusIQ?", "acceptedAnswer": {"@type": "Answer", "text": "Any HubSpot account with admin access works. Free accounts may not grant some object scopes; reconnect with all requested scopes checked if a tool reports insufficient scopes."}}
  ]
}
</script>

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
