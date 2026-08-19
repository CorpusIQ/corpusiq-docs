---
title: "PCL Domain Expert Skills — 104 Persona Skill Pack Setup"
description: "personamanagmentlayer/pcl — 104 skills, 36.2K installs: a persona-management-layer pack of domain-expert skills covering finance, telecom, trading, banking, and 100 more specialist personas for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pcl-domain-expert-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-18"
tags: ["hermes skill", "agent skill", "skill setup", "domain experts", "persona", "finance", "expert systems"]
---

# PCL Domain Expert Skills — Setup Guide

**Source:** [personamanagmentlayer/pcl](https://skills.sh/personamanagmentlayer/pcl)
**GitHub:** [personamanagmentlayer/pcl](https://github.com/personamanagmentlayer/pcl)
**Skills:** 104 skills · 36.2K total installs
**Category:** Domain Expertise
**First Seen:** January 23, 2026 (catalogued August 18, 2026 sweep)
**Quality Tier:** 🟡 Trusted — Snyk Warn on the finance-expert flagship (named); Gen Agent Trust Hub Pass and Socket Pass; 41 GitHub stars

The Persona Management Layer (PCL) ships 104 domain-expert skills, each one a specialist persona an agent can load for a vertical: finance, telecommunications, trading, real estate, banking, insurance, construction, logistics, healthcare, aerospace, maritime, and farming on the business side; GCP, PostgreSQL, Kafka, Kubernetes, Terraform, Snowflake, and Rust on the technical side. The flagship finance-expert covers financial systems, FinTech, banking platforms, payment processing, risk management, and regulatory compliance (PCI-DSS, SOX, Basel III). Each skill is a compact knowledge persona rather than an API connector — useful for domain framing, terminology, and compliance context, not for live data access.

---

## Installation

```bash
npx skills add personamanagmentlayer/pcl
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/personamanagmentlayer/pcl --skill finance-expert
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Domain data** | The personas provide expertise, not connectors — pair with the operator's own data sources for live work |

## What It Provides

| Skill | Installs | Domain |
|---|---|---|
| finance-expert | 6.2K | Financial systems, FinTech, banking, payments, PCI-DSS/SOX/Basel III |
| telecommunications-expert | 1.8K | Telecom networks and operations |
| trading-expert | 944 | Trading platforms and market operations |
| real-estate-expert | 775 | Property transactions and markets |
| banking-expert | 773 | Core banking platforms |
| insurance-expert | 676 | Insurance products and workflows |
| construction-expert | 632 | Construction project operations |
| accountant-expert | 595 | Accounting practice guidance |
| manufacturing-expert | 565 | Manufacturing systems |
| logistics-expert | 529 | Supply chain and logistics |

The remaining 94 personas span cloud platforms (gcp-expert, azure-expert, aws-expert), data (snowflake-expert, databricks-expert, dbt-expert), languages (python-expert, java-expert, go-expert, rust-expert), and infrastructure (kubernetes-expert, terraform-expert, istio-expert, linkerd-expert).

## Quick Start

1. Install: `npx skills add personamanagmentlayer/pcl`
2. Load the matching persona before vertical work: `--skill finance-expert` for a FinTech question
3. Use the persona for domain framing and compliance context; pull live numbers from your own connectors

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Vertical context for operator questions** | A persona like finance-expert sharpens financial-domain answers before any connector is called |
| **Compliance-aware agent framing** | Banking and insurance personas carry regulatory context (PCI-DSS, SOX, Basel III) useful for enterprise builds |
| **Rapid domain ramp** | 104 personas let agents switch vertical context without retraining or prompt engineering per domain |
| **Pairing with CorpusIQ connectors** | Persona knowledge plus live connector data gives domain-shaped answers |

## Limitations / Verification

- Security audits on the finance-expert flagship: Gen Agent Trust Hub Pass, Socket Pass, Snyk Warn (named in the tier)
- Publisher-page total verified (36.2K across 104 skills); 41 GitHub stars as of the sweep
- Personas are knowledge packs, not APIs — no live data access and no authentication handling
- The publisher name is spelled "personamanagmentlayer" (sic) in both the skills.sh listing and the GitHub org

```bash
npx skills add personamanagmentlayer/pcl   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
