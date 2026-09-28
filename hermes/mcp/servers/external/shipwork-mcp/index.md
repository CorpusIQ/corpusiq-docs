---
title: Shipwork MCP - Keyless Technical SEO Audits
description: "Shipwork's free keyless JSON API for technical SEO: site audits, 0-100 scores, bulk status checks, sitemap generation and 24 named checks."
category: SEO
stars: n/a (new listing)
added: 2026-09-27
source: "mcpservers.org + shipwork.io/api-docs"
relevance: ★★★
tags: [seo, technical-seo, site-audit, sitemap, canonical, structured-data, keyless, remote-mcp]
---

# Shipwork SEO Checks

**A keyless audit surface where every check returns the page, the finding and the fix.** Shipwork is a free technical SEO checker exposed as JSON endpoints at shipwork.io. Agents, scripts and dashboards send a site and get findings grouped by check, each with the offending page and the fix. Anonymous requests work with no key and no signup, on the same free allowance as the website, and the API ships an OpenAPI 3.1 spec, an API catalog and an agent skill manifest for agent-native use.

```
Server type: Remote (JSON API with agent skill and API catalog)
Auth: none for the free allowance (optional sign-in raises the limit)
Endpoint: https://shipwork.io (POST /api/audit, /api/score, /api/bulk-status, /api/sitemap-generator, GET /api/check/{name})
Tools: 4 endpoints plus 24 named checks
Pricing: free allowance; over-limit responses return HTTP 429 with free_limit
Category: SEO
Built by: Shipwork (shipwork.io)
```

## Why This Matters for Operators

Technical SEO failures are usually silent: a noindex crept in, a canonical broke, structured data stopped validating. The cheapest moment to catch them is before a launch or right after a change, but most audit tools gate that behind accounts and credits. Shipwork's anonymous endpoints mean an agent can run a full audit, a 0-100 score or a single named check on demand, and the response names the page and the fix rather than dumping raw crawler output.

The named-check list is the power move for operators: agent-readiness, backlinks, certificate, DNS, email-auth, headers, headings, hreflang, indexnow, lighthouse, markup, meta, mixed-content, rich-results, serp-features, site-crawl and more, each callable individually with its raw data included.

## Tools & Capabilities

| Endpoint | Purpose |
|---|---|
| POST /api/audit | Crawl a set of pages and run every applicable check with per-finding fixes |
| POST /api/score | Return a 0-100 health score, letter grade and top fixes |
| POST /api/bulk-status | Status codes plus redirect hops and noindex/canonical flags for up to 25 URLs |
| POST /api/sitemap-generator | Generate sitemap.xml with every excluded page and the reason |
| GET /api/check/{name} | Run one of 24 named checks on one address with raw data |

## Installation

```bash
curl -X POST https://shipwork.io/api/score -H "content-type: application/json" -d '{"url":"example.com"}'
```

For agent clients, load the agent skill from the Shipwork well-known manifest so the assistant knows the endpoints and how to call them. No key and no signup for the free allowance.

## Configuration

```json
{
  "mcpServers": {
    "shipwork": {
      "type": "http",
      "url": "https://shipwork.io/api/audit"
    }
  }
}
```

Requests are anonymous JSON POSTs; over the free limit the API returns HTTP 429 with a `free_limit` flag, and signing in raises the allowance.

## Business Relevance

- **Founders without an SEO hire** get launch-day checks with zero setup
- **Agencies** can automate pre-launch and post-change audits per client
- **Operators** get a shareable score snapshot for stakeholder reports
- **Dev teams** can wire audits into CI without managing another API key

## Integration with CorpusIQ

Shipwork pairs with CorpusIQ's seo-crawl-audit workflow: CorpusIQ surfaces indexing and coverage signals from Search Console, and Shipwork runs the outside-in audit that explains them with page-level fixes. Sitemap generation and canonical checks feed directly into the CorpusIQ docs SEO passes before pages ship.

## Limitations

- Free tier is a preview allowance per visitor; heavy use needs sign-in or limits
- Audits run from outside the network, so intranet-only pages stay uncovered
- New listing; single-purpose SEO surface rather than a full rank tracker
- No key means no per-account history of past audits

## FAQ

### Do I need an API key for Shipwork?

No. Anonymous requests work on the free allowance; signing in raises the limit. Over-limit calls return HTTP 429 with a free_limit flag.

### What checks can the agent run?

24 named checks plus a full audit, a 0-100 score, bulk status codes and sitemap generation.

### Is there an agent-facing interface?

Yes. The site publishes an OpenAPI 3.1 spec, an API catalog and an agent skill manifest.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
