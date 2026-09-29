---
title: "Markifact Meta Ads MCP - Approval-Gated Meta Ads"
description: "Markifact connects Facebook and Instagram ads to any AI agent with approval-gated campaign and creative management."
category: Advertising & Marketing
stars: n/a (new listing)
added: 2026-09-29
source: "mcpservers.org listing + markifact.com/meta-ads-mcp"
relevance: ★★★
tags: [meta-ads, facebook-ads, instagram-ads, marketing, campaign-management, creative, approval-gated, remote-mcp]
---

# Markifact Meta Ads MCP

**Facebook and Instagram ads with approval before anything ships.** Markifact connects Meta Ads to Claude, ChatGPT or any AI agent to analyze performance, create campaigns and creatives, manage ad sets, and approve every change before it touches a live account.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth sign-in (also installable from the Claude directory at claude.ai/directory/markifact)
Endpoint: https://api.markifact.com/mcp/meta-ads
Tools: reporting, Pixel and CAPI inspection, campaign and ad set creation, creative building
Pricing: vendor pricing (markifact.com)
Category: Advertising & Marketing
Built by: Markifact (markifact.com, github.com/markifact/meta-ads-mcp)
```

## Why This Matters for Operators

Meta's campaign hierarchy is the most punishing surface in paid media: campaigns, ad sets, ads, creatives, placements and attribution all interact, and one misconfigured ad set can burn budget for a week. Markifact's Meta Ads server lets an agent draft across that whole hierarchy while every change still waits for operator approval.

For operators running both paid channels, this is the sibling to the Markifact Google Ads MCP, which means one vendor, one login and the same approval discipline across Google and Meta.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Cross-account reporting | Campaign, ad set, ad and creative performance with placement, device, age and gender breakdowns |
| Pixel and CAPI checks | Meta Pixel and Conversions API setup, event coverage, match quality, attribution issues |
| Campaign and ad set creation | Build campaigns and ad sets the operator approves before launch |
| Creative building | Image, video, carousel and catalog ads connected to campaigns in one workflow |

The GitHub repository lists the full Meta Ads operation set; every write operation is approval-gated.

## Installation

```bash
claude mcp add markifact-meta-ads --transport http https://api.markifact.com/mcp/meta-ads
```

Install Markifact from the Claude directory or ChatGPT marketplace and sign in, or use the hosted endpoint above with the same login.

## Configuration

```json
{
  "mcpServers": {
    "markifact-meta-ads": {
      "type": "http",
      "url": "https://api.markifact.com/mcp/meta-ads"
    }
  }
}
```

## Business Relevance

- **Performance marketers** get placement and demographic breakdowns without manual pivot tables
- **Creative teams** hand carousel and catalog ad assembly to an agent and review before launch
- **Agencies** audit Pixel and CAPI health across client accounts
- **Growth operators** manage Google and Meta from one vendor's approval-gated surface

## Integration with CorpusIQ

Markifact covers Meta; CorpusIQ connectors close the attribution loop. Combine Markifact Meta reporting with CorpusIQ GA4, Stripe and Shopify data to see which Meta campaigns drive revenue, not just clicks, and let the agent propose budget shifts backed by both sides of the funnel.

Pair with the Markifact Google Ads MCP and CorpusIQ cross-source connectors so one assistant session compares Google versus Meta efficiency against actual web and revenue data.

## Limitations

- Writes are approval-gated, which is a feature and also a throughput limit
- Meta only; Google and other channels are separate Markifact servers
- Organic Facebook and Instagram performance analysis is a separate question from paid ads
- Pricing is not disclosed on the directory listing

## FAQ

### Can the agent create ads without me?

It can draft campaigns, ad sets and creatives, but every change waits for your approval before it goes live.

### Does it check tracking setup?

Yes. It inspects Meta Pixel and Conversions API setup, event coverage and match quality, and flags issues that hurt attribution.

### Does it replace a media buyer?

No. It removes the manual reporting and drafting work, but the operator keeps judgment on budgets, offers and creative direction.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
