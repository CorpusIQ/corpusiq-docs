---
title: Velarion MCP - Executive Compensation and Governance
description: "Hosted MCP server with 12 tools for executive compensation research and governance intelligence: CEO and NEO pay, Say-on-Pay risk prediction, disclosed peer benchmarking, pay-ratio and director-comp data, plus Governance Alpha Cards. Keyless catalog surface with free-plan tools confirmed by live probe, paid tools listed in a SKU catalog."
category: Finance
stars: n/a (no public repo)
added: 2026-09-04
source: mcp.so feed
relevance: ★★★
tags: [executive-compensation, governance, say-on-pay, proxy-research, investor-research, remote-mcp, keyless]
---

# Velarion MCP

**Remote MCP server (Streamable HTTP)** - executive compensation and governance intelligence from disclosed filings: CEO and NEO total pay, Say-on-Pay vote history and risk prediction, disclosed peer-group benchmarking, director compensation, and composite Governance Alpha Cards. 12 tools confirmed by live probe (serverInfo velarion-mcp v3.3.1) in this sweep.

```
Server type: Remote (Streamable HTTP)
Auth: None on the catalog surface; free-plan tools keyless, paid tools via plan
Endpoint: https://velarion-scraper-production.up.railway.app/mcp
Tools: 12 (6 free-plan, 6 paid/catalog)
```

## Why This Matters for Operators

Proxy season, board compensation decisions and M&A diligence all run on the same hard-to-assemble data: what do comparable companies actually pay their executives, how did shareholders vote on pay packages, and how does the target's pay-for-performance align. Velarion compiles disclosed compensation, performance and governance data into deterministic tools with cited sources. **An operator benchmarking a CEO hire against the disclosed peer group gets percentile data and TSR comparison in one call instead of a proxy-statement research project.**

The paid tools are packaged as a product catalog (`list_skus` returns every report with name, price, currency, delivery type and latency), so an agent can quote exactly what a deep-dive report costs before the operator commits.

## Tools & Capabilities

Free-plan tools (keyless, live-probed):

| Tool | Purpose |
|---|---|
| `get_company_compensation` | Summary Compensation Table components for named executives |
| `get_director_compensation` | Non-employee director compensation and board fee schedule |
| `get_disclosed_peer_group` | The company's own disclosed compensation peer group, latest fiscal year |
| `get_say_on_pay_history` | Say-on-Pay vote history with support percentages calculated from disclosed counts |
| `get_ceo_pay_ratio` | Most recent disclosed CEO pay ratio |
| `search_companies` | Search the covered universe by name or ticker (max 10 results) |

Paid/catalog tools:

| Tool | Purpose |
|---|---|
| `lookup_company_compensation` | CEO/NEO total compensation, pay mix breakdown and capping analysis |
| `predict_say_on_pay_risk` | Say-on-Pay risk prediction with trend phrase and peer-cohort distribution |
| `benchmark_executive_pay` | Pay percentile and TSR percentile versus disclosed peers |
| `compare_companies` | Ranked comparison on pay, performance and governance metrics |
| `generate_governance_alpha_card` | Composite card: pay alignment, modeled on the P4P approach |
| `list_skus` | Full product catalog with name, price, currency, delivery type, latency |

## Installation

```bash
claude mcp add --transport http velarion https://velarion-scraper-production.up.railway.app/mcp
```

No key on the catalog surface; initialize and tools/list answered anonymously in this sweep. Free-plan tools work immediately; paid tools follow the plan pricing in the SKU catalog.

## Configuration

```json
{
  "mcpServers": {
    "velarion": {
      "url": "https://velarion-scraper-production.up.railway.app/mcp"
    }
  }
}
```

The production URL carries a deployment name ("scraper-production" is the Railway deployment, not the product). Re-check the vendor's listing if the endpoint changes.

## Business Relevance

- **Boards and comp committees** benchmark executive pay against the company's own disclosed peers.
- **Investors and analysts** read Say-on-Pay history and risk trends before proxy votes.
- **M&A diligence** pulls CEO pay ratio and compensation structures of targets.
- **Compensation consultants** get percentile and TSR comparison data with citations.

## Integration with CorpusIQ

CorpusIQ connects financial statements and operational data; Velarion adds the governance layer those statements do not carry. A CorpusIQ agent researching a public company can pair the financial picture with Velarion's compensation and Say-on-Pay data for a complete investment or board-prep brief.

## Limitations

- No public repo found; coverage universe, methodology and citations are described in tool output, not audited externally.
- Free plan covers six tools; the deepest analytics (risk prediction, benchmarking, alpha cards) are paid per SKU.
- Listed on mcp.so since July 2026 but without directory detail pages elsewhere; treat as a niche research service.
- Railway-hosted endpoint could move; verify against the vendor listing.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [Factanker MCP - Evidence-Backed Company and Bank Facts](/hermes/mcp/servers/external/factanker-mcp)
- [SEC EDGAR MCP - Full-Text Filing Search for Agents](/hermes/mcp/servers/external/sec-edgar-mcp)
