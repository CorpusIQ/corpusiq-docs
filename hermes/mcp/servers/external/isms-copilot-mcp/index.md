---
title: "ISMS Copilot MCP - ISO 27001 and SOC 2 Compliance Work"
description: "Hands the compliance work to an agent: framework interpretation, policy drafting, control mapping, gap analysis and audit prep."
category: Compliance / GRC
stars: ★★ (OAuth workspace, multi framework)
added: 2026-10-28
source: "live probe of https://account.ismscopilot.com/v1/account/mcp returning HTTP 401 with the body UNAUTHORIZED Authentication failed, plus submission issue chatmcp/mcpso #6301, the vendor site ismscopilot.com/mcp and the registry entry io.github.tristanroth1/ismscopilot-account"
relevance: ★★★
tags: [compliance, iso-27001, soc-2, gdpr, nis-2, dora, gap-analysis, risk-register, audit, oauth]
last_updated: "2026-10-28"
---

# ISMS Copilot MCP

**Compliance work fails in the gap between the policy that was written and the control that was actually operated, and nobody notices until the auditor asks for the evidence.**

```
Server type: Remote (Streamable HTTP), OAuth workspace
Endpoint:    https://account.ismscopilot.com/v1/account/mcp
Registry:    io.github.tristanroth1/ismscopilot-account
Frameworks:  ISO 27001, SOC 2, GDPR, NIS 2, DORA and more
Docs:        docs.ismscopilot.com/docs/agents/connect-any-mcp-client
Repository:  github.com/better-isms/ismscopilot-plugin
```

## Why This Matters for Operators

An information security management system is a document set plus an operating rhythm, and both halves are usually someone's second job. The frameworks themselves are public. What is not public is the mapping between a control objective and the specific policy, risk entry and evidence that satisfies it in this company, at this size, with these systems.

This server takes the compliance half of the work and gives it to an agent working inside the customer's own ISMS Copilot workspaces. Framework interpretation, policy drafting, control mapping, gap analysis, risk registers and audit preparation all happen against the workspace documents rather than in a fresh chat that forgets the last one.

## What It Returns, Verified

The endpoint is live and gated: a bare `POST initialize` on `https://account.ismscopilot.com/v1/account/mcp` returned **HTTP 401** with the body `{"error":{"code":"UNAUTHORIZED","message":"Authentication failed. Please log in again."}}`, the correct shape for an account-scoped workspace.

The published surface, from the submission and vendor documentation:

- Interpret the frameworks, including ISO 27001, SOC 2, GDPR, NIS 2 and DORA
- Draft and revise policies against the company's own workspaces and documents
- Map controls between frameworks, so one control can satisfy several obligations
- Run gap analysis and keep a risk register current
- Prepare for an audit, working from the workspace rather than a blank prompt
- Connect from any MCP client using the documented agent connection guide

The registry entry is `io.github.tristanroth1/ismscopilot-account` and the published plugin repository is `github.com/better-isms/ismscopilot-plugin`.

## Limits Worth Recording

This is the framework and document layer, not the evidence collector. It drafts the policy and maps the control, but it does not read your cloud configuration to prove the control operated. Adjacent catalogued surfaces cover parts of that: **Nizh** serves compliance frameworks to agents with posture checks and hash-chained attestations, **Fallax** turns phishing simulation results into ISO 27001 A.6.3 audit evidence, and **Auditspark** covers audit workflow. The honest split is that an ISMS of record lives here and the technical evidence still comes from the systems themselves.

## FAQ

### Which frameworks does it cover?
ISO 27001, SOC 2, GDPR, NIS 2 and DORA are the named ones, and the framework layer is a general one rather than a single standard.

### Does it collect the audit evidence itself?
No. It interprets frameworks, drafts policy, maps controls, runs gap analysis and keeps the risk register. Evidence from your systems is a separate collection problem, partly served by Nizh and Fallax in this catalogue.

### Where does the content live?
In the customer's own ISMS Copilot workspaces and documents, which the agent works with through the account endpoint.

### Does it work from any MCP client?
Yes. The vendor publishes a connection guide for any MCP client at docs.ismscopilot.com, and the endpoint is a standard Streamable HTTP account route.
