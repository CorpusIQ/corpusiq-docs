---
title: StartupPerks MCP - Startup Credits and Perks Database
description: "StartupPerks finds the startup credits, perks and deals a company qualifies for across 1,000+ source-cited programs."
category: Finance
stars: n/a (new listing)
added: 2026-09-27
source: "mcpservers.org + startupperks.co/mcp-server"
relevance: ★★★
tags: [startup-credits, perks, aws-activate, startup-programs, cost-savings, free-tier, keyless, remote-mcp]
---

# StartupPerks MCP

**A keyless lookup over every startup credit a company qualifies for.** StartupPerks exposes a hosted MCP server at `https://startupperks.co/mcp` that finds the startup credits, perks and deals a company qualifies for across 1,000-plus source-cited programs, including AWS Activate, Google for Startups and NVIDIA Inception. It is free, read-only and needs no API key or sign-up.

```
Server type: Remote (Hosted)
Auth: none (keyless, no sign-up)
Endpoint: https://startupperks.co/mcp
Tools: program search and eligibility lookup
Pricing: free
Category: Finance / Startup Programs
Built by: StartupPerks (startupperks.co)
```

## Why This Matters for Operators

Startup credits are the closest thing to free money an early business gets, and most companies leave a meaningful fraction unclaimed because nobody has time to crawl a thousand program pages. StartupPerks makes the lookup a conversation: the agent matches the company against the program catalog, with source citations behind each eligibility claim.

The keyless design matters for adoption: there is no account to create, no key to rotate and no spend to manage, so an operator can ask on day one.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Program search | Find credits and perks across 1,000+ source-cited programs |
| Eligibility | Check what a company qualifies for by stage and profile |
| Sources | Every program entry carries source citations |

## Installation

```bash
npx add-mcp 'https://startupperks.co/mcp'
```

Claude desktop and claude.ai users add the URL under Settings > Connectors > Add custom connector; no sign-up is required.

## Configuration

```json
{
  "mcpServers": {
    "startupperks": {
      "type": "http",
      "url": "https://startupperks.co/mcp"
    }
  }
}
```

## Business Relevance

- **Founders** claim credits they qualify for before they expire
- **Finance operators** reduce early infra and SaaS spend materially
- **Accelerators** point portfolio companies at qualified programs
- **CFOs** track what is claimed versus what is available

## Integration with CorpusIQ

StartupPerks complements CorpusIQ's Stripe and QuickBooks connectors by attacking the cost side: CorpusIQ shows current spend through Stripe balance transactions, and StartupPerks shows the credits that could offset parts of it. CorpusIQ business recaps can pair claimed perks with actual spend to show realized savings.

## Limitations

- Read-only database; programs must still be applied to through vendors
- Eligibility signals are source-cited but should be re-verified at the program page
- Coverage is startup-program oriented, not general cost reduction
- New listing; catalog completeness depends on the vendor's crawl

## FAQ

### Is there a sign-up or API key?

No. The server is free, read-only and keyless at startupperks.co/mcp.

### How many programs does it cover?

More than one thousand source-cited programs, including AWS Activate, Google for Startups and NVIDIA Inception.

### Does it apply to programs for me?

No. It finds what a company qualifies for; applications still go through each vendor.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
