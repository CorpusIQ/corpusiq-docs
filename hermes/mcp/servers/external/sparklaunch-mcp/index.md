---
title: SparkLaunch MCP - Founder Validation and Company Formation
description: "Official hosted MCP from SparkLaunch for founder operations: project creation with auto-queued idea validation research, brand palette and logo generation, campaign, QR and landing-page creation with signal review, private CRM context, and entitlement-gated incorporation cases. OAuth-gated endpoint, official MCP Registry listed."
category: Productivity
stars: "1 (new listing, SparkLaunch-Dev/SparkLaunch-Skills)"
added: 2026-09-02
source: "mcpservers.org /all JSON-LD (Sep 2, 2026 morning sweep)"
relevance: ★★
tags: [mcp-server, founders, startups, incorporation, idea-validation, branding, campaigns]
---

# SparkLaunch MCP

**Founder operations as agent workflows, from idea to incorporation.** SparkLaunch walks early-stage founders through selecting or creating a business project, validating the idea, generating brand assets, publishing measurable launch surfaces, reviewing campaign and landing-page signals, operating private CRM workflows, and preparing entitlement-gated incorporation cases with person-specific Action Center tasks. The hosted MCP endpoint sits alongside a public skills repository and a ChatGPT connector; writes that touch public or destructive state return a confirmation preview that a human must approve before the call is resubmitted with its confirmation token.

```
Server type: Hosted (sparklaun.ch/api/mcp/) with skills repo and plugin package
Endpoint: https://sparklaun.ch/api/mcp/ (Streamable HTTP, OAuth)
Registry: io.github.SparkLaunch-Dev/sparklaunch (official MCP Registry)
Repo: github.com/SparkLaunch-Dev/SparkLaunch-Skills (created Feb 2026, proprietary license notice)
Website: sparklaun.ch
Tools: capability-level (OAuth-gated; anonymous probe returns 401 invalid_token with login_url)
```

## Why This Matters for Operators

Founders are operators at their most exposed - every workflow (validation, incorporation, campaigns) is a first-time workflow. SparkLaunch is built so the agent carries the process and the human holds the approvals.

First, **validation is queued, not vibed.** When a project is created with a complete business description, Idea Validation research is automatically queued and completes in 10-15 minutes - the founder gets research-backed validation instead of an assistant's opinion.

Second, **the launch surface is measurable.** Campaigns, QR files and landing pages are created as publishable artifacts, then observed signals are reviewed - the loop between publishing and measuring is part of the workflow, not a separate tool.

Third, **writes are confirmation-gated.** Destructive or public-state tools return a one-time confirmation preview only after a server-side authorization preflight succeeds; the user explicitly approves before the exact call is resubmitted with its confirmation token. Autonomous execution is the default architecture for the safe half.

## Tools and Capabilities

Capability-level table from the README and skills repository; the OAuth-gated endpoint refuses anonymous enumeration (401 invalid_token with a login URL - which confirms liveness). Exact tool contracts are published to the official MCP Registry and generated from the backend source.

| Area | Capabilities |
|------|--------------|
| Projects | Select an accessible project or create one with a complete business description; auto-queued Idea Validation research |
| Brand | Generate palette and logo options |
| Launch surfaces | Create a campaign, QR file and landing page; review observed campaign and landing-page signals |
| CRM | Operate private CRM workflows with grounded context |
| Incorporation | Prepare entitlement-gated incorporation cases with person-specific Action Center tasks |

The connected ChatGPT experience exposes the same surface through skills; the skills never request credentials, OAuth codes or transport headers - authentication is managed by the host and starts on the first protected action.

## Installation

Other MCP clients discover `io.github.SparkLaunch-Dev/sparklaunch` through the official MCP Registry, or configure the Streamable HTTP endpoint directly:

```
https://sparklaun.ch/api/mcp/
```

The client must support the server's OAuth flow; tokens are never pasted into prompts or shared configuration. Codex users install the `sparklaunch` plugin from the Git plugin marketplace (github.com/SparkLaunch-Dev/SparkLaunch-Skills); ChatGPT availability is separate from the public repository and the Registry listing.

## Configuration

Authentication is OAuth-connected and managed by the host. A legacy user-scoped MCP API key path exists for existing developer clients. If a loaded connection is expired or revoked, the surface stops before writes and asks the user to reconnect, then retries only after reconnection succeeds.

## Business Relevance

- **Founders** get idea validation, brand assets, launch surfaces and incorporation cases as one connected workflow.
- **Operators running multiple ventures** get a CRM workflow and campaign signal review per project.
- **Teams** get person-specific Action Center tasks inside incorporation preparation.

## Integration with CorpusIQ

SparkLaunch composes with CorpusIQ as the operations layer for the newly incorporated company. SparkLaunch carries the founder through validation, launch and incorporation; CorpusIQ then answers from the live business data (Stripe, QuickBooks, Shopify, HubSpot) once the company is running. An operator can ask "what did our launch campaign signals show, and what did the revenue look like behind them" - SparkLaunch reads the campaign side, CorpusIQ reads the money side. Pairs with FoundRole for the hiring workflow that follows incorporation.

## Limitations

- OAuth-gated endpoint: anonymous enumeration is refused, so the tool table above is capability-level from the skills repository.
- One-star repo with a proprietary license notice; the MCP server source itself is closed.
- Skills-first surface: the richest experience is the connected ChatGPT connector; other clients get the raw endpoint.
- Registry publications are immutable and version-locked, so capability changes land on a publication cadence.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [FoundRole MCP - Fact-Checked AI Job Search and Application Tracking](/hermes/mcp/servers/external/foundrole-mcp)
