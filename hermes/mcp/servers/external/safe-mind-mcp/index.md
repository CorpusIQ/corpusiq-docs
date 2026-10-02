---
title: Safe Mind MCP - Psychological Risk Assessment
description: "Official stdio MCP server for the Safe Mind platform that runs the legally required psychological risk assessment (GBU Psyche) for German companies: 12 tools to onboard an account, set up departments and locations, create survey drafts, and read anonymity-protected aggregated results with segmented analytics, published to npm as safe-mind-mcp."
category: Compliance
stars: n/a (new listing, github.com/lewo-media/safe-mind-tools)
added: 2026-08-28
source: "mcp.so GitHub issue #3806"
relevance: ★★
tags: [mcp-server, compliance, hr, germany, risk-assessment, stdio]
---

# Safe Mind MCP

**Official MCP server for Safe Mind, the platform for Germany's legally required psychological risk assessment (Gefährdungsbeurteilung psychischer Belastung, GBU Psyche).** German employers must periodically assess psychological strain factors in the workplace, and Safe Mind turns that obligation into a surveyed, documented workflow. The MCP server exposes 12 tools over the Safe Mind Public API: onboard an account, model departments and locations, draft surveys, and read the results.

```
Server type: Local stdio via npm (npx safe-mind-mcp)
Auth: API key (SAFE_MIND_API_KEY environment variable)
Install: npx -y safe-mind-mcp
Tools: 12 (account, departments, locations, survey drafts, aggregated results)
Pricing: Safe Mind platform subscription; API via safe-mind.de/developers
Category: Compliance / HR
Built by: lewo-media (safe-mind.de, GitHub lewo-media/safe-mind-tools, MIT)
```

## Why This Matters for Operators

GBU Psyche is a compliance obligation with real liability attached: German companies must document that they assessed psychological risks such as workload, autonomy, and social climate, and works councils can demand the documentation. Most companies run it in spreadsheets and portals that do not connect to the rest of their tooling.

Two properties make the MCP surface worth wiring up. First, the survey lifecycle is scriptable: an assistant can draft a survey per department, schedule it, and pull the results, so the annual obligation becomes a repeatable operation instead of a consultant engagement. Second, anonymity is enforced server-side: analytics endpoints return only aggregated results and filter groups below a minimum size, so an agent can read the data without ever being able to re-identify an employee.

**A legally required HR workflow becomes an automatable, documented operation.**

## Tools & Capabilities

Capability-level table from the submission and the developer documentation; the API requires an account and key.

| Area | Capability |
|---|---|
| Account | Onboard and authenticate against the Safe Mind account (login and API key handling) |
| Organization | Set up departments and locations for segmented assessment |
| Surveys | Create survey drafts with configurable start dates, durations, and employee counts |
| Results | Read anonymity-protected aggregated results with segmented analytics |

## Installation

```bash
npm install -g safe-mind-mcp
```

Or run it without installing:

```bash
npx -y safe-mind-mcp
```

An API key comes from the Safe Mind platform (safe-mind.de/developers).

## Configuration

```json
{
  "mcpServers": {
    "safe-mind": {
      "command": "npx",
      "args": ["-y", "safe-mind-mcp"],
      "env": {
        "SAFE_MIND_API_KEY": "sm_live_..."
      }
    }
  }
}
```

## Business Relevance

- **German HR teams** automate the GBU Psyche cycle: drafts, rollouts, and result pulls per department.
- **Compliance officers** get documented, repeatable risk assessments instead of one-off consultant runs.
- **Multi-site employers** model each location separately and read segmented aggregated results.
- **Works-council-facing managers** produce the documentation the obligation requires without manual reporting.

## Integration with CorpusIQ

Safe Mind produces compliance and workforce-risk data; CorpusIQ joins it to the business numbers. A composed workflow: the assistant pulls the latest aggregated GBU Psyche results per department, then reads headcount, payroll, and turnover context from CorpusIQ connectors to spot correlations between strain factors and attrition. Compliance data becomes a workforce-planning input.

## Limitations

- stdio only: no hosted remote endpoint, so server-side clients need a local runtime.
- Germany-specific: the workflow maps to German law and German-language surveys.
- Requires a Safe Mind account and API key; the developer tools are brand new (repo and npm package published Aug 28, 2026).
- Capability-level tool table: exact tool schemas need an authenticated session.
- Aggregated-only results are a feature and a limit: no individual-level reads by design.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [PassportCraft MCP - EU Digital Product Passports](/hermes/mcp/servers/external/passportcraft-mcp)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
