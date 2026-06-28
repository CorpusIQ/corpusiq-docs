---
title: Opencloudcosts MCP Server Integration Guide
description: Multi-cloud pricing for AI agents — AWS, GCP, Azure real-time pricing without credentials. Anchor AI FinOps to live cloud costs with Opencloudcosts MCP
category: mcp
tags: [mcp, opencloudcosts, finops, cloud, aws, gcp, azure, pricing, cost-optimization, hermes-agent]
last_updated: 2026-06-28
---

# Opencloudcosts MCP — Credentialless Cloud Pricing for Hermes Agent

Anchor AI FinOps to real, live cloud pricing. Multi-cloud MCP server for AWS, GCP, and Azure — covering both public list prices AND enterprise negotiated rates (Reserved Instances, Savings Plans, CUDs, EDPs). No cloud provider credentials needed.

## What It Does

Opencloudcosts gives AI agents access to current cloud pricing data without requiring access to your cloud accounts:

- **AWS pricing** — EC2, RDS, Lambda, S3, EKS, and 200+ services with list + enterprise rates
- **GCP pricing** — Compute Engine, Cloud SQL, Cloud Run, GKE, BigQuery with CUDs
- **Azure pricing** — VMs, SQL Database, Functions, AKS with Enterprise Agreement rates
- **Commitment analysis** — Reserved Instances, Savings Plans, Committed Use Discounts pricing
- **Cross-cloud comparison** — Compare equivalent services across providers at real pricing

## Quick Setup

### Prerequisites
- **No cloud credentials needed** — Public pricing data, no provider access required
- **No API key required** — Open access

### Add to Hermes Agent

```bash
hermes mcp add opencloudcosts -- url https://opencloudcosts.com/mcp
```

Or manual config:

```json
{
  "mcpServers": {
    "opencloudcosts": {
      "url": "https://opencloudcosts.com/mcp",
      "transport": "streamable-http"
    }
  }
}
```

## Key Capabilities

| Tool | Description |
|------|-------------|
| `get_service_pricing` | Get current list price for any cloud service by region |
| `get_enterprise_rate` | Query enterprise negotiated rates (RIs, Savings Plans, CUDs, EDPs) |
| `compare_services` | Cross-cloud comparison — e.g., "EC2 vs Compute Engine vs Azure VM" |
| `estimate_monthly` | Estimate monthly cost for a given configuration across providers |
| `list_commitment_options` | List available Reserved Instance, Savings Plan, and CUD options for a service |

## Use Cases for Business Operators

### 1. Architecture Cost Estimation
Before deploying a new service, have your AI agent estimate costs across clouds:

```
Agent prompt: "We need to run PostgreSQL with 16GB RAM, 4 vCPUs, 
500GB storage in us-east-1. What's the monthly cost on AWS RDS 
vs GCP Cloud SQL vs Azure Database? Include enterprise rates 
(we have an AWS EDP and GCP CUDs)."
```

### 2. Commitment Purchase Decisions
When your finance team asks about RI/Savings Plan purchases:

```
Agent prompt: "We run 50 m6i.xlarge instances in us-east-1 24/7. 
Compare 1-year all-upfront vs 3-year partial-upfront Reserved 
Instance costs. Factor in our 12% EDP discount."
```

### 3. Cloud Migration Cost Analysis
When evaluating a cloud migration:

```
Agent prompt: "We're moving a 200-instance workload from AWS to GCP. 
Estimate the equivalent GCP Compute Engine costs for our instance 
fleet and compare with our current AWS spend including our 
Savings Plan commitments."
```

### 4. Budget Planning
During quarterly budget planning:

```
Agent prompt: "Our engineering team wants to add 20% more capacity 
next quarter. Based on our current blend of on-demand, RI, and 
Savings Plan purchasing, estimate the incremental monthly cost 
for 20 m7i.xlarge instances in us-west-2."
```

## Integration with CorpusIQ

Opencloudcosts + CorpusIQ = complete cloud financial operations:

1. **CorpusIQ QuickBooks connector** → pull actual cloud spend from accounting
2. **CorpusIQ database connector** → query resource utilization data
3. **AI agent** → correlate actual spend with real-time pricing
4. **Opencloudcosts** → validate invoices, forecast costs, optimize commitments

This gives FinOps operators an end-to-end cloud cost intelligence pipeline.

## Why Credentialless Matters

- **Security:** No cloud provider credentials — pricing data is public
- **Speed:** No IAM setup, no cross-account roles — start querying immediately
- **Audit-safe:** Pricing queries don't appear in CloudTrail/audit logs
- **Multi-cloud:** One interface for AWS, GCP, and Azure — no per-provider setup

## Pricing

Free public access. Visit [opencloudcosts.com](https://opencloudcosts.com) for current status.

---

*← [External MCP Catalog](/hermes/mcp/servers/external/) | [MCP Overview](/hermes/mcp/)*

*↑ [MCP Documentation](/hermes/mcp/)*
