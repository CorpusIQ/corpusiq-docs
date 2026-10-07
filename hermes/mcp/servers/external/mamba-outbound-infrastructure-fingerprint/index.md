---
title: "Mamba Outbound Infrastructure Fingerprint MCP"
description: "Check whether a company runs cold email outbound, on what sending stack and which lookalike domains, with quotable evidence per domain."
category: Sales & Outreach
stars: n/a (npm package, MIT)
added: 2026-10-07
source: "chatmcp/mcpso issue #4882 (Oct 7, 2026 morning sweep)"
relevance: ★★
tags: [outbound, cold-email, sales-intelligence, deliverability, dns, apify, local-mcp, npm]
---

# Mamba Outbound Infrastructure Fingerprint MCP

**Local MCP server (stdio, npm) - outbound program detection** for any company domain: whether that company runs cold email outbound, on what sending infrastructure, and the lookalike sending domains behind it, with quotable evidence.

```
Server type: Local (stdio), TypeScript, Node 18+
Auth: Your own Apify API token (APIFY_TOKEN)
Package: @mambalabsdev/mcp-outbound-infrastructure-fingerprint (npm, MIT, v1.2.1)
Tool: fingerprint_outbound_infrastructure (single tool, read-only)
Registry: com.mambabuilt/mcp-outbound-infrastructure-fingerprint
Pricing: Apify credits per domain analyzed (optional deliverability add-on billed separately)
Cache: 7-day result cache (skipCache to force a fresh run)
Built by: Mamba Labs (part of the Mamba Labs GTM Suite)
```

## Why This Matters for Operators

The detection logic is the interesting part: a real outbound program does not send from the domain the business runs on. It buys lookalike domains (`getcompany.com`, `company-mail.com`, `trycompany.co`), gives them their own mail tenant and redirects the web root at the real site. That redirect is the attribution handle, and following it is what this server does.

The read is useful three ways: sales tooling decisions (know which targets already live and breathe outbound), competitive intelligence (who runs outbound at scale in a market), and infrastructure context (the sending domains and mail providers behind a prospect). The vendor's own measurement on nine live domains: 6 of 6 detected on companies that demonstrably run outbound, 0 false positives on 3 controls.

## Tools & Capabilities

| Tool | What the agent can do |
|---|---|
| `fingerprint_outbound_infrastructure` | One flat row per domain: `runs_outbound` (program, light, none, unknown), confidence, sending domains, registration clusters, sending platforms, inbox provider, warmup detection, infrastructure vendors, SPF/DKIM/DMARC status and an evidence array of quotable strings |

Key inputs:
- `domain` or `domains` (batch takes precedence).
- `scan_sending_domains` (default true) - the strongest signal and the slowest step.
- `sending_domain_depth` (`deep` covers .com .co .io .net .org).
- `check_deliverability` (default false) - adds a separately billed blacklist check and health score.
- `max_sending_domain_probes`, `skipCache`, DNS and HTTP timeouts.

## Installation

```bash
npm i @mambalabsdev/mcp-outbound-infrastructure-fingerprint
```

Or run it without installing via `npx` using the configuration below.

## Configuration

```json
{
  "mcpServers": {
    "mamba-outbound-infrastructure-fingerprint": {
      "command": "npx",
      "args": ["-y", "@mambalabsdev/mcp-outbound-infrastructure-fingerprint"],
      "env": { "APIFY_TOKEN": "your-apify-token" }
    }
  }
}
```

Get a token at console.apify.com/account/integrations. The server lists its tools without a token; the token is needed to run a lookup, and each call runs the Mamba Labs actor under your own Apify account. The same tools also ship in the umbrella `@mambalabsdev/mcp-gtm-suite` package.

## Business Relevance

- **Sales tools and consultants:** qualify targets that already run outbound, and gauge the sophistication of their stack.
- **Competitive research:** map which companies in a market run outbound at scale.
- **Agencies:** benchmark prospect infrastructure before pitching sending or deliverability work.
- **Market analysis:** read the lookalike-domain footprint of an outbound-heavy cohort.

## Integration with CorpusIQ

CorpusIQ answers from the operator's own connected systems; the Fingerprint adds the outside view of a market's outbound activity. Reach for it while building a target list: shortlist the accounts, then read each one's sending infrastructure before the first touch.

## Limitations

- When the brand token is an ordinary English word (Gong, Clay, Ramp), lookalike patterns collide with unrelated businesses; the actor sets `brand_is_common_word` and caps confidence rather than reporting a confident "none".
- Sending-platform recall is partial by design: platforms that connect over OAuth to a customer's own mailbox (Instantly, Smartlead, Lemlist, Apollo, Salesloft) publish no SPF include host, so an empty `sending_platforms` tells you little while a populated one is solid.
- Static DNS and HTTP evidence only; programs hiding behind shared infrastructure can read `unknown`.
- Apify credits per domain; the optional deliverability add-on bills separately; 7-day cache.

## FAQ

### What do the runs_outbound values mean?

`program` for a full outbound operation, `light` for smaller or occasional sending, `none` when nothing fires and `unknown` when the read cannot conclude (for example a blocked or common-word brand).

### Why lookalike domains?

Because that is how real outbound infrastructure works: purchases of similar domains with their own mail tenants and a redirect at the web root. Finding them is the part a domain lookup alone misses.

### What is the deliverability add-on?

An optional, separately billed blacklist check and health score on the discovered sending domains, switched on with `check_deliverability`.

## See Also

- [Mamba Funding Investor Record MCP - SEC and UK Filings](/hermes/mcp/servers/external/mamba-funding-investor-record/)
- [Reach MCP - Operate a Real LinkedIn Account from Your Agent](/hermes/mcp/servers/external/reach-mcp/)
- [MisarReach MCP - Outbound Sales and Lead Pipeline for AI Agents](/hermes/mcp/servers/external/misarreach-mcp/)
- [Snov.io MCP - B2B Sales and Outreach for Agents](/hermes/mcp/servers/external/snovio-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
