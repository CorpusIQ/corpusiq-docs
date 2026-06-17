# Recipes

Recipes are reusable query patterns for CorpusIQ connectors.

Each recipe captures a specific analytical workflow: which connectors it uses,
what the query looks like, and what output to expect. Recipes are designed to
be copied, adapted, and run directly against your CorpusIQ MCP instance.

## What makes a good recipe

- Solves a real operational problem
- Uses actual CorpusIQ connector field names
- Includes a concrete example of the expected output
- Is specific enough to run, not so specific it only works for one team

## Available Recipes

| Recipe | Connectors | Use Case |
|--------|-----------|----------|
| [Weekly Ad ROI Report](weekly-ad-roi-report.md) | Google Ads, Meta Ads, GA4 | Cross-source weekly advertising ROI |
| [Shopify-QuickBooks Reconciliation](shopify-quickbooks-reconciliation.md) | Shopify, QuickBooks | Daily sales vs invoice reconciliation |
| [HubSpot-Klaviyo Pipeline](hubspot-klaviyo-pipeline.md) | HubSpot, Klaviyo | Deal pipeline correlated with email engagement |

## Submitting a Recipe

See [CONTRIBUTING.md](../CONTRIBUTING.md) for submission instructions.
Use [TEMPLATE.md](TEMPLATE.md) as your starting point.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
