---
title: Expired Domains MCP - Karma.Domains Domain Intelligence for Agents
description: Screen expired, auction, backorder and buy-now domains in plain language through one hosted MCP endpoint. KarmaScore and Karma Metric rankings, SEO enrich with Ahrefs, Moz and SimilarWeb data, saved filters, guest share links and 13 live domain checkers for SEO operators, domain investors and agencies.
category: SEO
stars: n/a (new listing)
added: 2026-09-08
source: mcp.so
relevance: ★★★
tags: [domains, expired-domains, domain-investing, seo, backlinks, whois, remote-mcp]
---

# Expired Domains MCP

**Remote MCP server (Streamable HTTP, OAuth or Pro API key)** - Karma.Domains gives an agent the same auctions, expired, backorder and buy-now inventory as its website, driven from chat. One hosted endpoint exposes 31 tools over four groups: structured domain searches with the full 90-plus filter catalog, account favorites, report workflow tools (saved filters, annotations, guest share links, SEO enrich jobs), and 13 live checkers for expiry, WHOIS, DNS, backlinks and traffic.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser sign-in on karma.domains) or Pro API key (Bearer header)
Endpoint: https://mcp.karma.domains/mcp
Tools: 31 (reports, account, workflow, live checks)
Pricing: Pro plan required; live checks 1 credit each; x402 USDC credit packs for agent access
Category: SEO
Built by: Karma.Domains (karma-domains/expired-domains-mcp on GitHub)
```

## Why This Matters for Operators

Buying expired domains is a manual research grind: open a marketplace, stack filters, eyeball Wayback history, check DA and spam scores, repeat for every auction. **Karma.Domains MCP collapses that loop into one chat query**: the agent returns a shortlist of up to ten candidates per source with a match count and links to full reports, so the operator only spends time on finalists.

The platform covers 400k-plus new domains daily from 40-plus data sources with 90-plus search filters, and its scoring layers (KarmaScore for listings, Karma Metric for Wayback and backlink profile comparison) mean an agent can pre-screen for authority instead of dumping raw lists. Live checkers cost 1 credit per domain, so due diligence stays cheap and cache hits are free.

## Tools & Capabilities

| Area | Tools | Purpose |
|---|---|---|
| Reports | `search_reports`, `get_domain`, `instructions` | Primary structured query with the app's full filter set; full report for an exact domain; field glossary and filter catalogs |
| Account | `get_user_profile`, `list_favorites`, `add_favorite`, `remove_favorite` | Balance and plan status; pinned domains across all databases |
| Workflow | `list_saved_filters`, `save_saved_filter`, `delete_saved_filter` | Reuse named searches for morning sweeps or client niches |
| Annotations | `list_annotation_tags`, `get_report_annotation`, `set_report_annotation`, `delete_report_annotation` | Team notes and tags on reports; Pro-gated writes |
| Sharing | `create_share_link` | Guest share URL for clients without an account |
| SEO enrich | `enrich_report_seo`, `get_enrich_report_seo_job` | Paid enrich jobs with fresh Ahrefs, Moz and SimilarWeb metrics |
| Live checks | `check_domain_expiry`, `check_expired_report`, `get_domain_karma_metric`, `domain_authority_checker`, `domain_age_checker`, `domain_expiry_checker`, `backlink_checker`, `anchor_text_checker`, `website_page_counter`, `website_traffic_checker`, `dns_lookup`, `whois_lookup`, `spam_score_checker` | Registration availability, expired-report re-checks (free), Wayback Karma Metric, DA/DR/AS, archive age, expiry dates, Moz backlinks and anchors, sitemap page count, SimilarWeb/Semrush traffic, DNS records, structured WHOIS, Moz Spam Score |

Live checkers cost 1 credit per domain unless noted; cache hits are free and expired-report re-checks are free once every three hours.

## Installation

```bash
claude mcp add karma-domains --transport http https://mcp.karma.domains/mcp
```

Claude.ai and ChatGPT connect with OAuth (browser sign-in). Cursor and other IDE clients attach the Pro API key from Profile -> Settings in the Authorization header (Bearer scheme). A Pro plan is required before the key is issued.

## Configuration

```json
{
  "mcpServers": {
    "karma-domains": {
      "type": "http",
      "url": "https://mcp.karma.domains/mcp"
    }
  }
}
```

OAuth clients complete a browser sign-in on karma.domains on first connect. The same Pro key drives both the MCP server and the Public API, with a shared 60 requests per minute rate limit, a 50,000 rows per day list quota, and 200 non-cache live calls per day. Agent accounts can skip the browser entirely with x402 payments: USDC credit packs on Base or Solana at $1.50 for 100 credits, $6.00 for 500, and $20.00 for 2,000, with the discovery manifest at karma.domains/.well-known/x402.

## Business Relevance

- **SEO operators** get an authority pre-screen before buying expired domains: KarmaScore, DA, Wayback history and spam risk in one shortlist instead of a dozen browser tabs.
- **Domain investors** run auction sweeps in chat - filter lots by platform, end date, price cap and link metrics, then open reports only for names worth bidding on.
- **Agencies** keep client pipelines tidy with saved filters, tags, notes and guest share links, so a domain report goes to the client without handing out the account.
- **Brand protection teams** check registration availability and monitor drops around brand-adjacent names with the live checkers.

## Integration with CorpusIQ

CorpusIQ connects the business data (GA4, Shopify, Stripe and 40-plus other systems) that tells an operator which niches actually make money. Karma.Domains MCP supplies the domain-acquisition layer CorpusIQ does not cover: the operator identifies a niche that performs well in CorpusIQ dashboards, then asks the agent for expired domains matching that niche with an authority floor, and validates the shortlist with live backlink and traffic checks before bidding.

The composed loop is simple: GA4 traffic and Shopify revenue in CorpusIQ pick the niche, Karma's domain intelligence picks the asset, and after acquisition CorpusIQ keeps measuring the business the new property brings in. The x402 credit packs also make the server budget-friendly for autonomous agents that only need occasional domain lookups.

## Limitations

- Brand new - listed on mcp.so September 8, 2026 with a 0-star GitHub repo; no track record yet.
- Pro plan required - the MCP key is not issued on free tiers, and live checks consume credits.
- Hosted only - no self-host option; the endpoint is Karma.Domains infrastructure.
- Shared rate limit of 60 requests per minute with the Public API, and 200 non-cache live calls per day.
- SEO enrich jobs cost 3 credits on Pro and 22 on Unlimited.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [KD Scout MCP - Keyword Research Arithmetic](/docs/hermes/mcp/servers/external/kd-scout-mcp)
- [CiteRank MCP - AI Search Visibility Audits](/docs/hermes/mcp/servers/external/citerank-mcp)
- [SEOmatic MCP - Real Search Console Data with Approval-Gated Fixes](/docs/hermes/mcp/servers/external/seomatic-mcp)
