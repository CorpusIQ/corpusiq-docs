---
title: "Inside Ads MCP - CorpusIQ Docs - CorpusIQ Docs"
description: "Pre-campaign audience validation for new products: reach and CPC estimates against real ad inventory before you spend, via MCP"
category: Marketing
stars: n/a (new listing)
added: 2026-08-17
source: mcp.so GitHub issue #3618
relevance: ★★
tags: [advertising, audience-validation, cpc, media-planning, launch, remote-mcp, streamable-http]
---

# Inside Ads MCP

**Remote MCP server (Streamable HTTP) that estimates whether a real audience exists for a product before any budget is committed.** For a product you just shipped, Inside Ads estimates reach, click range, and cost per click against a given budget, and says so plainly when there is no matching inventory instead of recommending a campaign anyway. On your go-ahead it parses the landing page and generates the campaign.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (inside.ad account)
Endpoint: https://app.inside.ad/api/mcp
Registry: ad.inside/inside-ads
Pricing: Commercial (inside.ad)
Category: Advertising Pre-Flight
Built by: Inside Ads, repo github.com/inside-ad/claude-plugin
```

## Why This Matters for Operators

The most expensive ad mistake is the one launched at an audience that does not exist. Most ad platforms are structurally incentivized to say yes: there is always a keyword to bid on. Inside Ads inverts that incentive with a no-inventory verdict, which turns media planning into a go/no-go gate instead of an assumption.

For founders and growth teams shipping new products, the pre-flight estimate (reach, click range, CPC against budget) closes the loop between "we built it" and "people are searching for it" before the first dollar of spend. The landing-page parse then generates the campaign from the product's own page, so the copy is grounded in what the product actually says.

## Tools & Capabilities

| Capability | What it does |
|---|---|
| Audience estimate | Reach, click range, and CPC projections for a given product and budget |
| No-inventory verdict | Explicit negative signal when no matching ad inventory exists |
| Landing page parse | Extracts the product's positioning to seed campaign generation |
| Campaign generation | Builds the campaign structure after your go-ahead |

## Installation

```bash
claude mcp add --transport http inside-ads https://app.inside.ad/api/mcp
```

Sign in with your inside.ad account when the client opens the approval page.

## Configuration

```json
{
  "mcpServers": {
    "inside-ads": {
      "type": "http",
      "url": "https://app.inside.ad/api/mcp"
    }
  }
}
```

## Business Relevance

- **Founders** gate paid acquisition on a verified audience before spending
- **Growth marketers** get CPC and reach ranges in the planning conversation instead of after the test flight
- **Agencies** run the same pre-flight for every client launch as a standard step
- **Product marketers** keep campaign copy grounded in the landing page the product team actually shipped
- **Finance stakeholders** see the no-inventory verdict as the cheapest possible campaign: the one never launched

## Integration with CorpusIQ

Inside Ads validates the top of the funnel (does the audience exist and what will it cost) while CorpusIQ's Google Ads and Meta Ads connectors measure the actual spend, clicks, and conversions once campaigns run. The honest pairing: Inside Ads before launch, CorpusIQ during and after. Both surfaces are read-first, so planning and reporting stay separate from campaign mutation.

## Limitations

- Brand new listing (Aug 17, 2026), no track record yet
- Estimate quality depends on the ad networks it queries; treat projections as pre-flight ranges, not guarantees
- Commercial platform: no self-host option published
- Young repository (0 stars at discovery); treat as early-access tooling
- OAuth flow per client, so multiple agents mean multiple approvals

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
