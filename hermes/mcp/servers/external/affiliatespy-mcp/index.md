---
title: "AffiliateSpy MCP - Competitor Creator Discovery for Agents"
description: "AffiliateSpy finds the TikTok, YouTube and Instagram creators and the blogs and roundups already promoting your competitors, with proof, then recruits them from your own inbox."
category: Marketing
stars: n/a (new listing)
added: 2026-09-28
source: "mcp.so server page (affiliatespy.io)"
relevance: ★★★
tags: [affiliate-marketing, influencer-marketing, competitor-research, creator-outreach, sales, remote-mcp]
---

# AffiliateSpy MCP

**Competitor creator and affiliate discovery with recruitment built in.** AffiliateSpy scans the creators and websites already selling your competitors, attaches the proof (post, discount code, affiliate link or disclosed partnership), grades each creator on fit and purchase intent, then reveals verified contacts and runs outreach from your own inbox.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 with dynamic client registration, or Bearer API key from Settings
Endpoint: https://www.affiliatespy.io/api/mcp
Tools: 32 named tools across account, creators, market intel, campaigns, inbox and Autopilot
Pricing: free quick scan and sandbox keys, vendor plans at affiliatespy.io
Category: Marketing / Affiliate and Creator Outreach
Built by: Savassi Limited (affiliatespy.io)
```

## Why This Matters for Operators

Affiliate and creator channels are the fastest way to borrow a competitor's distribution, but finding who actually sells them is manual detective work: watching tagged posts, reading review roundups, chasing contact emails. AffiliateSpy compresses that into a single agent workflow: paste a competitor's App Store, Google Play or website URL, and get every creator and website promoting it, each with the evidence and a fit grade.

The recruitment half runs from your own Gmail or Outlook, so outreach looks like it comes from you, not a platform, and replies land in a tracked pipeline. For operators, that turns a weeks-long prospecting slog into an overnight Autopilot draft queue.

## Tools & Capabilities

| Tool area | Tools | Purpose |
|---|---|---|
| Account and apps | get_account, list_apps, get_scan_status, start_quick_scan, get_quick_scan_preview, get_checkout_link | Connect the workspace, run the free quick scan, inspect results before paying |
| Creators | list_creators, get_creator, reveal_contact, save_creator, unsave_creator, set_creator_note, export_creators_csv | Browse graded creators, reveal verified contacts, manage shortlists |
| Market intel | list_websites, list_competitors, list_keywords | See which sites and competitors are being tracked and on what keywords |
| Campaigns and inbox | list_campaigns, get_campaign, create_campaign_draft, list_inbox_threads, get_thread, list_deals, move_deal_stage | Draft outreach, read replies, track recruitment as a pipeline |
| Autopilot | get_autopilot | Read Autopilot status and drafted actions |
| Guarded actions | launch_campaign, pause_campaign, resume_campaign, send_reply, start_scan, set_autopilot, approve_autopilot_action, reject_autopilot_action | Confirm-gated writes that return approval_required until the user says yes |

All 32 tool names come from the vendor's published tool list; each tool carries readOnlyHint and destructiveHint annotations. Sandbox API keys answer every tool from fixture data so an agent can be built and tested before paying.

## Installation

```bash
claude mcp add affiliatespy --transport http https://www.affiliatespy.io/api/mcp
```

OAuth 2.1 with dynamic client registration means just adding the URL in Claude, ChatGPT, Claude Code, Cursor or Codex is enough. A REST mirror is available at POST https://www.affiliatespy.io/api/v1/tools/{tool} with OpenAPI at affiliatespy.io/openapi.json.

## Configuration

```json
{
  "mcpServers": {
    "affiliatespy": {
      "type": "http",
      "url": "https://www.affiliatespy.io/api/mcp"
    }
  }
}
```

## Business Relevance

- **Growth operators** clone competitor distribution by recruiting the creators already promoting them
- **DTC and app teams** find the review sites and roundups that drive installs and purchases in their category
- **Affiliate managers** replace manual creator sourcing with a graded, evidence-backed shortlist
- **Founders** run outreach from their own inbox without hiring an agency

## Integration with CorpusIQ

AffiliateSpy pairs cleanly with CorpusIQ analytics connectors. Pull referrer and channel performance from GA4 or Shopify, identify which third-party sites and creators already send converting traffic, then feed those competitors and domains into AffiliateSpy to find the full roster promoting them. Recruit the winners, then close the loop by tracking recruited creators as a cohort in GA4 against the baseline the CorpusIQ connectors already report on.

For outreach volume, the reveal and draft cycle can feed a CorpusIQ lead pipeline: save graded creators, export the CSV, and hand the top tier to the lead-nurture sequences with the competitor context already attached.

## Limitations

- New listing with no track record yet
- Revealed contact data quality varies by niche and public footprint
- Guarded tools are confirm-gated, so fully hands-free runs stop at approval_required
- Outreach sends from your own Gmail or Outlook, so deliverability depends on your account health
- Vendor pricing details live on affiliatespy.io, not on the directory listing

## FAQ

### How is this different from an influencer marketplace?

Marketplaces list creators who opted in and charge platform margins. AffiliateSpy starts from a competitor and finds everyone already promoting them, with the post or affiliate link as proof, whether or not the creator is on any marketplace.

### What can agents do with it hands-free?

Scan competitors, grade creators, build shortlists, draft campaigns and summarize inbound replies. Anything that sends mail or launches a campaign is guarded and returns approval_required until you approve it.

### Does it replace my affiliate program?

No. It finds and recruits the partners; you still need program terms, tracking and payouts. Pair it with your existing program or treat it as the sourcing layer before you set one up.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
