---
title: "CorpusIQ in the ChatGPT App Store"
description: "CorpusIQ is an official public app in the ChatGPT app store."
last_updated: "2026-10-26"
---

# CorpusIQ in the ChatGPT App Store

**Status:** LIVE, verified Aug 16 2026; new version approved Sep 30 2026
**Direct link:** https://chatgpt.com/plugins/plugin_asdk_app_6a9f5d19efbc8191b9d5a5fd4be12426 (browse: chatgpt.com/plugins?q=corpusiq)
**Listing:** "CorpusIQ - Ask questions across files"

CorpusIQ is an official public app in the ChatGPT app store (the surface that replaced the Plugins store). This is the third distribution surface for the product, alongside MCP access inside Claude (you add the CorpusIQ connector yourself, there is no directory listing) and the web app at corpusiq.io.

## What the listing gives users

- One-click install inside ChatGPT
- Ask questions in plain English, get source-cited answers from connected business tools
- Read-only access to Shopify, QuickBooks, Stripe, GA4, Google Ads, HubSpot and 40+ more
- Zero data stored, validated answers with citations

## Why it matters

The same product is now reachable in the three places business users actually look:

1. ChatGPT app store (search "corpusiq")
2. Claude, by adding the CorpusIQ MCP connector in Claude's connector settings
3. corpusiq.io web app

The consistent-answer promise is the point: the same number in ChatGPT, Claude, and Perplexity. Every time. The store listing makes that promise literal.

## Usage in promotion

- Mention the ChatGPT store listing in social content (listing documented at corpusiq.io/llms.txt; re-checked Oct 26, 2026)
- Affiliate and outreach emails can say "available in the ChatGPT app store, and inside Claude through our MCP connector". Never claim a Claude directory listing or a one-click Claude install  --  Anthropic's public directory API returns no CorpusIQ entry.
- Docs links should use the direct plugin link above

## Verification method

curl the llms.txt at corpusiq.io (it documents the listing), then confirm via browser search at chatgpt.com/plugins?q=corpusiq. The listing card reads "CorpusIQ - Ask questions across files" and is public. A plain curl of the direct plugin URL returns 403 for non-browser clients, which is bot filtering, not a missing listing  --  check it in a browser.

For the Claude side, curl https://api.anthropic.com/api/directory/servers and search for "corpusiq". As of Oct 26, 2026 the response contains no CorpusIQ entry, so Claude access is described as a custom MCP connector, never as a directory listing.
