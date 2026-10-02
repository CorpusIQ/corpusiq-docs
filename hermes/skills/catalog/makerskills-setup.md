---
title: "Makerskills - Personal Operator Agent Suite Setup"
description: "coreyhaines31/makerskills - 23-skill suite for the personal operator's craft (4.7K installs, 681 stars): second-brain and company-brain knowledge vaults, deep-research, decide, business-brainstorm, CFO skills, content and PM workflows, plus meta-skills for authoring your own. Platform-agnostic SKILL.md playbooks load natively in Hermes Agent."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/makerskills-setup/"
robots: "index,follow"
last_updated: "2026-08-24"
tags: ["hermes skill", "agent skill", "skill setup", "second brain", "knowledge management", "business operations"]
---

# Makerskills - Setup Guide

**Source:** [coreyhaines31/makerskills](https://skills.sh/coreyhaines31/makerskills)
**GitHub:** [coreyhaines31/makerskills](https://github.com/coreyhaines31/makerskills) (681⭐, created June 3, 2026, actively maintained)
**Catalog size:** 23 skills, 4.7K total installs (publisher page, authoritative count)
**Category:** Business Operations & Knowledge Management
**First Seen:** July 2, 2026 on skills.sh
**Quality Tier:** 🟡 Trusted (Gen Agent Trust Hub: Pass, Socket: Pass, Snyk: Warn)

Makerskills is a cohesive suite of agent skills for the personal operator's craft: decisions, research, knowledge vaults, content rotation, scenario modeling, and finance. Each skill is a standalone SKILL.md playbook with standard frontmatter (name, description, metadata) and no platform binding, so they load natively in Hermes Agent like any other skill.

**Compatibility note:** the repo README targets Claude Code, Codex, and Cursor, and the playbook prose is Claude-flavored ("so Claude can answer questions"). The mechanics are agent-agnostic procedural workflows (vaults, modes, triggers) with no Claude-specific tool requirements; Hermes users install through the skills.sh CLI or by copying individual SKILL.md files.

---

## Overview

| Skill | Installs | Domain |
|---|---|---|
| `watch-video` | 339 | Content intake |
| `decide` | 303 | Decision workflow |
| `social-fetch` | 268 | Social content intake |
| `read-book` | 265 | Reading workflow |
| `business-brainstorm` | 242 | Strategy |
| `second-brain` | 241 | Personal knowledge vault |
| `jab-hook` | 239 | Content rotation |
| `company-brain` | 238 | Team knowledge vault |
| `slide-deck` | 238 | Presentation generation |
| `loopify` | 231 | Workflow automation |
| `toolify` | 231 | Tool authoring |
| `pm` | 231 | Product management |
| `paste` | 228 | Clipboard sharing |
| `skillify` | 227 | Skill authoring |
| `deep-research` | 223 | Multi-source research |
| `company-cfo` | 221 | Business finance |
| `domain` | 216 | Domain research |
| `personal-cfo` | 216 | Personal finance |
| `unstuck` | 167 | Creative unblocking |
| `maker-council` | 96 | Scenario modeling |
| `adapt-skill` | 1 | Meta: adapt skills |
| `update-skill` | 1 | Meta: update skills |
| `create-skill` | 1 | Meta: author skills |

**Not included:** none excluded; the three 1-install meta-skills (`adapt-skill`, `update-skill`, `create-skill`) are authoring utilities documented in the roster above rather than given separate guides.

---

## Installation

Install the full suite via the skills.sh CLI:

```bash
npx skills add coreyhaines31/makerskills
```

Install individual skills by name:

```bash
npx skills add https://github.com/coreyhaines31/makerskills --skill company-brain
```

Or copy a playbook directly into your Hermes skills directory (the repo stores 20 SKILL.md files under `skills/`):

```bash
mkdir -p ~/.hermes/skills/makerskills
curl -sL https://raw.githubusercontent.com/coreyhaines31/makerskills/main/skills/company-brain/SKILL.md \
  -o ~/.hermes/skills/makerskills/company-brain/SKILL.md
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Any version with skills directory support (`~/.hermes/skills/`) |
| **Node.js 18+** | Only for the `npx skills` CLI path |
| **No API keys** | The playbooks are knowledge and decision guides; they use tools you already have configured |
| **Network (optional)** | Only needed for `npx skills` fetch or raw.githubusercontent.com downloads |

## What It Provides

### Knowledge vaults

`second-brain` wraps the Karpathy LLM Wiki schema over any Obsidian or markdown vault with a raw → wiki → outputs pipeline (capture, compile, query, lint, connect, search modes; defaults to `${SECOND_BRAIN_VAULT:-$HOME/Documents/SecondBrain}`). `company-brain` is the team-scope sibling with structured category dirs (people, companies, meetings, SOPs, decisions, sales-objections) plus capture, compile, query, review, lint, connect, and search modes, with author and timestamp stamping on every capture.

### Research and decisions

`deep-research` runs multi-pass research with source planning, verification, citations, contradictions, and gap analysis, archiving every run to `~/.config/makerskills/deep-research/archive/` so the corpus compounds. `decide` walks the 37signals Guide to Making Decisions question set (plus an opportunity-cost question), triages to the 6-8 load-bearing questions, and archives every call with a revisit date.

### Business operations

`company-cfo` and `personal-cfo` bring finance discipline to business and personal money questions. `business-brainstorm` and `maker-council` cover strategy generation and scenario modeling. `pm` applies product-management discipline to spec work. `domain` researches a business domain before diving in.

### Content and workflow

`watch-video`, `read-book`, and `social-fetch` turn content into vault captures. `jab-hook` manages content rotation, `slide-deck` generates presentations from vault material, `paste` shares clipboard state, `unstuck` breaks creative blocks, and `loopify` chains skills into repeatable workflows. `skillify`, `toolify`, and the three meta-skills close the loop by authoring new skills from your own patterns.

## Quick Start

```bash
# Install the full suite
npx skills add coreyhaines31/makerskills

# Start a personal knowledge vault
# Trigger: "/second-brain" or "capture this"

# Start a team knowledge vault
# Trigger: "/company-brain" or "log this meeting"

# Run a research pass
# Trigger: "/deep-research" or "do a deep dive on X"
```

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Memory architecture** | Use `second-brain` and `company-brain` patterns as reference designs alongside GBrain and Honcho when discussing agent memory layers |
| **Lead research** | Use `deep-research` for pre-call prospect research and due diligence |
| **Deal decisions** | Use `decide` to log go/no-go calls with revisit dates on partnerships and placements |
| **Finance checks** | Use `company-cfo` as a review lens for budget and spend questions |
| **Content ops** | Use `jab-hook` and `watch-video` patterns for content rotation across CorpusIQ social surfaces |
| **Skill authoring** | Use `skillify` and the meta-skills when converting recurring agent workflows into skills |

## Limitations / Verification

- Below the usual 20K publisher bar; drafted on suite-scale precedent (23 cohesive skills, 4.7K publisher-page installs, 681⭐, active development the day of the sweep) and direct relevance to business-operator agents
- The repo README and playbook prose target Claude Code, Codex, and Cursor; Hermes installs via the paths above, and tool references (e.g. `deep-research` naming WebSearch, WebFetch, Notion) map onto equivalent Hermes tools
- Snyk flags a Warn on the security audit (Gen Agent Trust Hub and Socket pass) - review SKILL.md files before activation
- Install counts are from skills.sh publisher pages as of the August 24, 2026 sweep; API search undercounts this cluster ~10x

```bash
# Verify skills installed
ls ~/.hermes/skills/makerskills/

# Verify the skills.sh listing
npx skills find "company-brain" --json 2>&1 | grep skills.sh
```

## Security

- [coreyhaines31/makerskills repo](https://github.com/coreyhaines31/makerskills) - review SKILL.md files before install (standard practice)
- [Hermes skills security](/hermes/best-practices/security) - skill trust guidance
- skills.sh security audits: Gen Agent Trust Hub Pass, Socket Pass, Snyk Warn

## Related

- [GBrain Agent Operations Setup](/hermes/skills/catalog/gbrain-agent-operations-setup) - vector memory layer for Hermes agents
- [Honcho Integration Setup](/hermes/skills/catalog/honcho-integration-setup) - conversational memory infrastructure
- [Agentic Awesome Skills (AAS) Setup](/hermes/skills/catalog/agentic-awesome-skills-setup) - 2,000+ skill catalog with memory-systems playbooks
- [Skills Catalog](/hermes/skills/catalog) - full catalog index

*← [Skills Catalog](/hermes/skills/catalog) | [Marketplace](/hermes/skills/marketplace) →*

*Powered by CorpusIQ*
