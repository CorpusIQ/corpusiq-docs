---
title: Peil MCP — Freelance Time Tracking & Invoicing
description: "Setup and usage guide for Peil MCP — Freelance Time Tracking & Invoicing. Part of the Hermes resource directory."
last_updated: 2026-08-12
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/peil-mcp/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# Peil MCP — Freelance Time Tracking & Invoicing

**Priority:** HIGH | **Category:** Finance / Freelance Operations  
**Transport:** TBD | **Auth:** TBD  
**Repository:** [Luminc/peil-mcp](https://github.com/Luminc/peil-mcp)  
**Discovered:** July 27, 2026 (mcpservers.org /all)

## What It Does for Operators

Connect Peil to any MCP client: log hours, draft invoices from unbilled hours, and get financial insights for your freelance practice — all in natural language. Peil bridges the gap between "I did the work" and "I got paid," which is the core operational loop for independent operators and small agencies.

## Installation

```bash
# Visit https://peil.app for setup instructions
# GitHub: https://github.com/Luminc/peil-mcp
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "peil": {
      "command": "npx",
      "args": ["-y", "peil-mcp"]
    }
  }
}
```

## Tools

Exact tool list TBD — based on description:
- Time entry logging (natural language: "Log 2.5 hours on client X project Y")
- Invoice drafting from unbilled hours
- Financial insights and practice health metrics
- Client/project organization

## Operator Use Cases

1. **Zero-friction time tracking:** "Hey agent, I just spent 3 hours on the Smith proposal — log it to Peil" — agent handles categorization, rate application, and invoice prep
2. **End-of-month batch invoicing:** Agent pulls all unbilled hours, drafts invoices per client, presents for review, sends with one approval
3. **Revenue forecasting:** Agent analyzes billable hours trend, projects monthly revenue, flags clients approaching retainer caps
4. **Client profitability analysis:** Agent correlates logged hours against client revenue to identify most/least profitable engagements
5. **Tax prep:** Agent exports categorized time data for Schedule C or T2125 filing

## CorpusIQ Angle

**Complementary — fills the solo-operator gap.** CorpusIQ handles business financials at the entity level (QuickBooks, Stripe). Peil handles the operator's personal practice layer — time → invoice → payment. Together they give a solo operator end-to-end financial visibility from time spent to cash collected.

## Limitations

- Limited public information — tools/auth/transport details TBD
- New product, may be early-stage
- Solo/freelance focus — may not scale to team time tracking
- GitHub repo (Luminc/peil-mcp) has minimal documentation
