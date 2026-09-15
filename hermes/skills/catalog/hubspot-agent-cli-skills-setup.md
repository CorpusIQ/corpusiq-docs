---
title: "HubSpot Agent CLI Skills Setup Guide for Hermes Agents"
description: "hubspot/agent-cli-skills - 17.8K installs across 15 skills, official HubSpot org: CRM operations, ticket resolution, deal management, sales reporting, and data quality skills that drive the hubspot CLI."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hubspot-agent-cli-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-31"
tags: ["hermes skill", "agent skill", "skill setup", "hubspot", "crm", "sales ops", "ticketing"]
---

# HubSpot Agent CLI Skills - Setup Guide

**Source:** [hubspot/agent-cli-skills](https://skills.sh/hubspot/agent-cli-skills) (17.8K installs across 15 skills)
**GitHub:** [hubspot/agent-cli-skills](https://github.com/hubspot/agent-cli-skills) (21 stars)
**Skills:** 15 skills; top skills: `ticket-resolution` (1.5K), `crm-lookup` (1.3K), `bulk-operations` (1.2K)
**Category:** Business / CRM & Sales Operations
**First Seen:** skills.sh May 26, 2026; catalogued in the Aug 31, 2026 sweep
**Quality Tier:** 🟡 Trusted - first-party publisher (official `hubspot` org) but Socket and Snyk audits carry warnings on the top skill (see Security Audit Status)

HubSpot's official agent skill suite turns the `hubspot` CLI into a guided CRM operations layer for AI agents. Fifteen skills cover the revenue-operations lifecycle: ticket resolution, CRM record lookup, bulk operations, data quality, workflow automation, deal management, sales reporting, data enrichment, communication history, custom objects, sales execution, team ownership, customer retention, audience targeting, and quote-to-cash.

The skills are procedural and portal-aware. They explicitly refuse hard-coded assumptions: pipeline stage IDs differ in every HubSpot portal and must be discovered per session, and enumeration property values (`hs_ticket_priority`, `hs_ticket_category`, `hs_resolution`) are portal-configurable and must be probed from live records rather than assumed. `bulk-operations/SKILL.md` is the required first read - JSONL piping, batch reads, pagination, and the dry-run / digest / confirm pattern live there, and `hubspot <command> --help` is authoritative.

---

## Installation

```bash
npx skills add hubspot/agent-cli-skills
```

Or per-skill:

```bash
npx skills add https://github.com/hubspot/agent-cli-skills --skill ticket-resolution
```

## Prerequisites

| Requirement | Details |
|---|---|
| **HubSpot CLI** | `hubspot` CLI installed and authenticated against the target portal (the skills drive this binary) |
| **Portal access** | API access to the HubSpot portal the agent will operate on |
| **Node.js** | Recent LTS for the `npx skills` installer |

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| ticket-resolution | 1.5K | Support ticket triage and resolution: pipeline discovery, enum verification, stage transitions |
| crm-lookup | 1.3K | Finding CRM records (contacts, companies, deals) by property and association |
| bulk-operations | 1.2K | JSONL piping, batch reads, pagination, dry-run / digest / confirm (read FIRST) |
| crm-data-quality | 1.2K | Deduplication and property hygiene across CRM records |
| workflow-automation | 1.2K | Building and inspecting HubSpot workflows from the CLI |
| deal-management | 1.2K | Deal pipeline operations and stage movement |
| sales-reporting | 1.2K | Pipeline and revenue reporting from CRM data |
| data-enrichment | 1.2K | Enriching records with external or derived data |
| communication-history | 1.2K | Reading and summarizing engagement timelines |
| custom-object-management | 1.2K | Working with custom object schemas and records |

Plus `sales-execution`, `team-ownership`, `customer-retention`, `audience-targeting`, and `quote-to-cash`.

## Security Audit Status (skills.sh, verified Aug 31, 2026)

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ticket-resolution | Pass | Warn | Warn |

Gen Agent Trust Hub Pass, but Socket and Snyk both carry warnings on the top skill - the reason this suite ships 🟡 Trusted rather than 🟢 Production.

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **CRM connector work** | CorpusIQ connects HubSpot as a first-class data source; these skills are the vendor's own playbook for navigating portals, pipelines, and enum properties correctly |
| **Ticket and deal analysis** | Agents that pull HubSpot data for business intelligence reports use `crm-lookup` and `ticket-resolution` to fetch the right records instead of guessing API paths |
| **Data quality operations** | `crm-data-quality` and `data-enrichment` map directly to CorpusIQ's operator-facing data-hygiene use cases |
| **Portal-aware automation** | The per-session pipeline and enum discovery pattern is a reusable discipline for any agent working against tenant-configurable SaaS |

## Limitations / Verification

- Below the 20K-install drafting bar; drafted on **publisher authority**: first-party `hubspot` org, direct CRM domain relevance to CorpusIQ operations, and a clean Gen Agent Trust Hub audit - the same brand-authority precedent as the github/gh-stack cluster.
- The skills assume a working, authenticated `hubspot` CLI; they do not include CLI installation or OAuth setup steps.
- Socket and Snyk warnings are named in the tier above; treat write-heavy operations (bulk updates, stage transitions) with the dry-run pattern from `bulk-operations` before confirming.

Verification after install:

```bash
hubspot --version 2>/dev/null || echo "hubspot CLI not installed"
npx skills add hubspot/agent-cli-skills --list    # 15 skills discovered
```

## Related

- [Skills Catalog](/docs/hermes/skills/catalog) - full quality-tiered directory
- [Skills Marketplace](/docs/hermes/skills/marketplace) - more discovery batches

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Skills Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
