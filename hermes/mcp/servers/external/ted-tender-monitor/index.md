---
title: TED Tender Monitor
description: EU TED procurement monitoring for AI agents — search and track tender notices by CPV code, country, keyword, value, and type via Apify
category: Sales
stars: n/a (new listing)
added: 2026-08-13
source: mcpservers.org
relevance: ★★
tags: [procurement, tenders, government-contracts, eu, apify, self-hosted]
---

# TED Tender Monitor

**MCP server over an Apify Actor (TED Tender Monitor — EU Procurement Alerts) from Telemark Digital.** Search official EU TED procurement notices by CPV code, country, keyword, value, or notice type, and run persistent scheduled monitoring that delivers only new or changed tenders. An unofficial community tool: it wraps the keyless TED Search API into structured JSON with deduplication state, and ships with n8n and Make workflows ready to import.

```
Server type: MCP server over Apify Actor (ted-tender-watch)
Auth: Apify account (the actor uses the keyless TED Search API underneath)
Repo: github.com/Telemark-Digital/apify-monitoring-workflows (ted-tender-monitor/)
Tools: TED notice search (CPV, country, keyword, value, type), change-notice tracking, JSON notice output
Pricing: $0.005 per newly delivered or changed tender; Apify platform usage applies
Category: Procurement / Sales
Built by: Telemark Digital (unofficial, not affiliated with TED or the EU)
```

## Why This Matters for Operators

Public-sector revenue is the largest customer acquisition channel most operators never work: EU TED publishes the entire public procurement market above the thresholds, and every notice is a qualified, budgeted buyer. The problem has always been signal triage — thousands of notices, keyword noise, and duplicate reads.

**Discovery and monitoring are different, and this tool is built for the difference.** Sample-mode tasks return up to ten recent matching notices immediately for exploration; persistent tasks prime state once and thereafter return only new or changed notices plus one summary record. That deduplication is what makes a weekly tender review practical instead of a second job.

## Tools & Capabilities

| Use case | Ready-made example task |
|---|---|
| AI procurement | monitor-eu-ai-procurement-notices |
| Cybersecurity tenders | track-eu-cybersecurity-tenders |
| Healthcare tenders | find-eu-healthcare-tenders |
| Public-sector SaaS | monitor-public-sector-saas-tenders |
| Software (CPV 72) | watch-cpv-72-software-tenders |
| Construction | track-eu-construction-procurement |
| Renewable energy | monitor-eu-renewable-energy-procurement |
| Change notices | track-ted-change-notices-and-corrigenda |

Thirteen bounded example tasks ship in the repo, plus an importable n8n workflow (n8n.io/workflows/18030) and a Make scenario specification.

## Installation

```bash
# 1. Try a public example task in sample mode (no charge)
# 2. Copy it to a persistent Task in your Apify account
# 3. Set sampleMode=false and run once to prime state
# 4. Keep maxNewPerRun <= 999 for the included workflows
# 5. Attach an Apify schedule or wire to n8n / Make
```

The repo's README and thirteen example tasks define the monitoring surface; the mcpservers.org listing carries the server metadata. Workflows intentionally retrieve one non-paginated page with limit 1000.

## Configuration

Connect the repo's `server.json` through your MCP client once the Apify token is available, or import the credential-free n8n workflow (`n8n.io/workflows/18030-monitor-eu-ted-tenders-with-apify-and-store-notices-in-n8n-data-tables/`). Webhook destinations and signing secrets are deliberately absent from public examples — configure them only in your private Task input for direct push delivery.

## Business Relevance

- **B2B operators entering the EU market** get a standing view of public buyers actively procuring in their category.
- **Agencies and consultancies** run CPV-72 software tenders as a lead channel with a human review step.
- **Founders in AI, security, and healthtech** track the exact procurement categories their product fits.
- **Compliance-driven vendors** watch change notices and corrigenda without re-reading full notice feeds.

## Integration with CorpusIQ

Tender monitoring produces leads; CorpusIQ converts them into pipeline. The composition: TED Tender Monitor surfaces new notices as structured JSON, the assistant qualifies them against the operator's fit, and CorpusIQ connectors take over — the prospect lands in HubSpot or Close as a lead, quotes and invoicing run through QuickBooks or Axonaut (for French entities, the natural EU pairing), and campaign ROI closes the loop in Stripe and GA4. For public-sector work in the EU, this is the first end-to-end chain from notice to invoice observed in the catalog.

## Limitations

- Unofficial community tool — not affiliated with TED or the EU Publications Office
- Apify account required; per-tender event charges on top of platform usage
- Notice content depends on TED's own API availability
- Brand new listing — no track record yet; the repo's VALIDATION.md notes account-gated checks still in progress

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
