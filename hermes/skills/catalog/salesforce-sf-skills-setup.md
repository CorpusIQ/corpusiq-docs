---
title: Salesforce Skills Library (sf-skills) - 330+ Agent Skills
description: "forcedotcom/sf-skills - Salesforce's official curated agent skills library: Apex, Flow, SOQL, LWC, Agentforce, Experience Cloud, Commerce B2B, Data360, Omnistudio, DX DevOps. 100+ skills indexed on skills.sh, ~500K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/salesforce-sf-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "agent skill", "skill setup", "salesforce", "crm", "apex", "agentforce", "lwc"]
---

# Salesforce Skills Library (sf-skills) - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/forcedotcom/sf-skills/platform-apex-generate) (100+ skills indexed, ~500K combined installs; top skill `platform-apex-generate` at 6,109)
**GitHub:** [forcedotcom/sf-skills](https://github.com/forcedotcom/sf-skills) (978⭐, 330 forks, Apache-2.0, pushed Sep 8, 2026)
**Category:** Development / CRM
**First Seen:** Sep 9, 2026 sweep (cluster surfaced via failed-query compensation; not previously evaluated)
**Quality Tier:** 🟡 Production, authority-justified (official Salesforce org; most skills Pass all audits - two flagged skills disclosed under Security)

Salesforce's official curated collection of agent skills for building on the Salesforce platform - 330+ skills covering Apex development, metadata and SOQL, Flow automation, Lightning Web Components, SLDS design systems, Agentforce, Experience Cloud, Commerce B2B, Data360, Omnistudio, and DX DevOps. Follows the open [Agent Skills specification](https://agentskills.io/) and is installable by any agent, including Hermes.

---

## Installation

```bash
npx skills add forcedotcom/sf-skills
```

For Hermes Agent, copy from a clone:

```bash
git clone --depth 1 https://github.com/forcedotcom/sf-skills.git
cp -r sf-skills/skills/* ~/.hermes/skills/
```

> ⚠️ **From the README:** "Expect frequent changes. The Salesforce skills library is evolving rapidly... Skills may be renamed, restructured, or removed between releases." Re-sync before long projects.

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Skills directory support (`~/.hermes/skills/`) |
| **Salesforce CLI (`sf`)** | `npm install -g @salesforce/cli` - required for org login, deploy, retrieve, test run |
| **Salesforce org credentials** | Dev org (free Developer Edition) or sandbox; `sf org login web` |
| **Node.js 18+** | For `npx skills` and the Salesforce CLI |

## Skill Roster (highlights of 100+ indexed)

| Domain | Representative skills |
|---|---|
| **Platform / Apex** | `platform-apex-generate` (6,109 - primary Apex authoring), `platform-apex-test-generate`, `platform-apex-logs-debug`, `platform-apex-test-run`, `platform-soql-query`, `platform-metadata-deploy/retrieve`, custom objects/fields/tabs/apps, permission sets, validation rules, sharing rules, flexipages, list views |
| **Agentforce** | `agentforce-generate`, `agentforce-architecture-analyze`, `agentforce-test`, `agentforce-observe`, `agentforce-d360-analyze` |
| **Design** | `design-systems-slds-validate`, `design-systems-slds-apply`, `design-systems-slds2-migrate` |
| **Experience Cloud** | `experience-lwc-generate`, `experience-ui-bundle-*` (9 skills), `experience-cms-*` (content generation) |
| **DX DevOps** | `dx-code-analyzer-run/configure`, `dx-org-manage/switch`, `dx-devops-test-*` |
| **Integration** | `integration-connectivity-connected-app-configure`, `integration-connectivity-generate`, eventing (CDC) subscriptions |
| **Commerce B2B / Data360 / Omnistudio / Mobile** | store creation, schema/code-extension generation, datamapper/omniscript/flexcard generation, mobile app creation |
| **Sep 29, 2026 sweep** | `platform-models-api-configure` (4,072), `developing-agentforce` (3,893), `service-helpagent-coordinate` (2,362) |

## Quick Start

1. Install skills + Salesforce CLI; `sf org login web` into a dev org
2. "Create a custom object for X" → `platform-custom-object-generate`
3. "Write an Apex batch job that Y" → `platform-apex-generate`
4. "Deploy this metadata" → `platform-metadata-deploy`

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **CRM integration roadmap** | CorpusIQ serves business operators who live in Salesforce - the agent gains working knowledge of the platform's extension points (Apex, Flow, LWC, Agentforce) for connector planning and operator Q&A |
| **Operator support** | Answer Salesforce automation questions (objects, fields, permission sets, flows) with spec-accurate generation instead of guesswork |
| **Prototyping integrations** | Scaffold Apex REST resources or connected apps to validate Salesforce integration ideas before engineering time |
| **Demo content** | Build working Salesforce app/flow demos for outreach to Salesforce-heavy ICP accounts |

## Limitations / Verification

- **Two flagged skills** (see Security) - install the rest freely
- **Repo churn:** skills may be renamed/removed between releases (README warning); pin a commit or re-sync deliberately
- **`minApiVersion: 66.0`** on platform skills - older orgs may need API version alignment

```bash
# Verify skill installed
ls ~/.hermes/skills/platform-apex-generate/SKILL.md
# Verify Salesforce CLI
sf version
```

## Security

Spot-checked Sep 9, 2026: `platform-apex-generate` Pass all three audits. Flagged skills:

| Skill | Trust Hub | Socket | Snyk | Note |
|---|---|---|---|---|
| `experience-content-media-search` | Pass | Pass | **Fail (HIGH W007)** | Insecure credential handling - instructs the agent to insert signed CMS/DAM URLs (including auth query params) verbatim into code. Signed URLs are the platform's auth mechanism, but avoid echoing them into logs/commits |
| `agentforce-generate` | Pass | **Warn** | Pass | Socket warning; review generated Agentforce configs before deploy |

The library is Apache-2.0, published by the official Salesforce org, and the vast majority of skills carry clean audits.

## Related

- [Microsoft Azure Skills - Setup Guide](/hermes/skills/catalog/microsoft-azure-skills-setup)
- [HubSpot Agent CLI Skills - Setup Guide](/hermes/skills/catalog/hubspot-agent-cli-skills-setup)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
