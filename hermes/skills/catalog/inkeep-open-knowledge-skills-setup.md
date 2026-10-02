---
title: Inkeep Open Knowledge Skills - Agent Knowledge Base
description: "inkeep/open-knowledge-skills - 33 skills, 17.1K combined installs. Inkeep's OpenKnowledge framework: a markdown-CRDT live multi-writer knowledge base plus agent skills for entity vaults, notes consolidation, specs, ADRs, postmortems, and personal CRM."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/inkeep-open-knowledge-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-31"
tags: ["hermes skill", "agent skill", "skill setup", "knowledge management"]
---

# Inkeep Open Knowledge Skills - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/inkeep/open-knowledge-skills) (17.1K combined installs)
**GitHub:** [inkeep/open-knowledge-skills](https://github.com/inkeep/open-knowledge-skills) (6⭐, MIT)
**Category:** Knowledge Management & Collaboration
**First Seen:** July 31, 2026 (skills.sh)
**Quality Tier:** 🟢 Production (Gen Agent Trust Hub Pass / Socket Pass / Snyk Pass)

OpenKnowledge (OK) is Inkeep's markdown-CRDT collaboration platform: it turns a directory of `.md`/`.mdx` files into a live, multi-writer knowledge base where agents and humans edit the same documents in real time, every change is attributed, and a browser preview renders edits as they land. The skill cluster covers discovery/install (`ok init`), the Open Knowledge Format (OKF) for entity vaults and knowledge bases, and a full software-lifecycle writing suite (specs, design reviews, decisions, postmortems) that ships as project-local skills.

---

## Installation

```bash
# Discovery skill - explains OK and installs the platform
npx skills add inkeep/open-knowledge-skills --skill open-knowledge-discovery

# Optional: run from any repository root to initialize the live knowledge base
ok init
```

The in-project read/write runtime contract (STOP rules for native file tools, grounding and linking rules, MCP routing) ships as a project-local skill installed by `ok init` - not via the skills.sh cluster.

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| open-knowledge-discovery | 6.3K | What OK is, install, and opening files (incl. standalone files) |
| open-knowledge-write-skill | 3.6K | Authoring content in OK format |
| open-knowledge | 2.6K | Core OK runtime contract |
| okf-knowledge-base | 2.5K | Open Knowledge Format knowledge-base structure |
| research-with-sources | 355 | Sourced research notes in OK format |
| knowledge-base / consolidate-notes | 351 | KB maintenance and note consolidation |
| codebase-wiki | 232 | Wiki-style codebase documentation |
| write-a-spec / review-a-design / record-a-decision / write-a-postmortem / frame-a-proposal | 81-82 | Software lifecycle documents as living KB entries |
| note-taking / personal-crm | 70 / 44 | Daily notes and contact tracking in OK format |
| writing-workflow / worldbuilding | 33 / 31 | Structured writing and fiction-world reference vaults |
| open-knowledge-pack-* (13 bundles) | 1-21 | Pre-packaged skill bundles per workflow |

## Prerequisites

- Node.js runtime for `ok init` and the OK client
- No credentials needed for local single-writer use; multi-writer sync uses the OK platform

## CorpusIQ Use Cases

- **Operator knowledge base** - the OKF entity-vault pattern (one file per entity, linked) is a clean reference for structuring CorpusIQ user-facing business knowledge
- **Live multi-agent documentation** - attributed, real-time co-editing of docs between agents and operators maps directly onto CorpusIQ's collaborative answer workflows
- **Lifecycle discipline** - the write-a-spec / record-a-decision / postmortem suite is a public counterpart to CorpusIQ's internal spec-and-decision governance patterns

## Limitations / Verification

- Low-star repo (6⭐) behind a well-known vendor (Inkeep) - skills.sh install counts (17.1K) are the adoption signal, not GitHub stars
- Multi-writer sync requires the OK platform; single-machine use works fully offline
- Verify install: `npx skills list | grep open-knowledge`

## Security

[Gen Agent Trust Hub: Pass](https://www.skills.sh/inkeep/open-knowledge-skills/open-knowledge-discovery/security/agent-trust-hub) · [Socket: Pass](https://www.skills.sh/inkeep/open-knowledge-skills/open-knowledge-discovery/security/socket) · [Snyk: Pass](https://www.skills.sh/inkeep/open-knowledge-skills/open-knowledge-discovery/security/snyk)

## Related

- [Basic Memory Skills - Agent Knowledge Graph Suite](/hermes/skills/catalog/basic-memory-skills-setup)
- [LJG Skills - Personal Knowledge Work Suite](/hermes/skills/catalog/ljg-skills-setup)
