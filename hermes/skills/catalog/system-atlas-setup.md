---
title: System Atlas - Explorable Architecture Map
description: "inkboard/system-atlas - 1 skill, 94 installs, 164 GitHub stars: build an explorable, progressively-disclosed isometric atlas of a system's architecture from one data file, with an interactive page and generated SYSTEM.md."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/system-atlas-setup/"
robots: "index,follow"
last_updated: "2026-08-24"
tags: ["hermes skill", "agent skill", "skill setup", "architecture documentation", "system documentation", "system map"]
---

# System Atlas - Setup Guide

**Source:** [inkboard/system-atlas](https://skills.sh/inkboard/system-atlas)
**GitHub:** [inkboard/system-atlas](https://github.com/inkboard/system-atlas) (164⭐, MIT, active through Aug 24, 2026)
**Skills:** 1 skill (system-atlas), 94 installs
**Category:** Developer Tools / System Documentation
**First Seen:** August 24, 2026 sweep (skills.sh first-listed ~Aug 21, 2026 - 3 days old at sweep time)
**Quality Tier:** 🔵 Community - brand-new skill on the hot board with a clean audit record (Gen Agent Trust Hub Pass, Socket Pass, Snyk Pass) but under the 100-install bar

System Atlas turns an architecture discussion into an explorable isometric "atlas" of the system: one data file drives an interactive page (hover to read, click to pin) plus a generated SYSTEM.md, with progressive disclosure so a viewer can zoom from the whole system down to one component. For a multi-service operation like CorpusIQ (Spark worker, docs pipeline, MCP server, gateway fleet, cron mesh), this is a lightweight way to keep a browsable architecture map current without maintaining a diagram tool.

---

## Installation

The maintained-checkout pattern (recommended - keeps the skill updateable with `git pull`):

```bash
git clone https://github.com/inkboard/system-atlas.git
```

```yaml
# ~/.hermes/config.yaml
skills:
  external_dirs:
    - /absolute/path/to/system-atlas
```

Or via the skills.sh marketplace:

```bash
npx skills add inkboard/system-atlas
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Architecture context** | The skill is driven by an architecture discussion or existing docs - it maps what you describe into the atlas data file |
| **Static hosting (optional)** | The interactive page is a static artifact; host it anywhere (docs site, internal page) for the hover/pin experience |

## Core Skill

| Skill | Installs | Use For |
|---|---|---|
| system-atlas | 94 | Build and maintain an explorable, progressively-disclosed isometric atlas of a system's architecture - an interactive page (hover to read, click to pin), one data file, and a generated SYSTEM.md |

## Security Audit Status (skills.sh, verified Aug 24, 2026)

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| system-atlas | Pass | Pass | Pass |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Architecture documentation** | One atlas data file + generated SYSTEM.md replaces hand-maintained diagram boards for the CorpusIQ system map (workers, deploys, crons, gateways) |
| **Onboarding artifact** | Progressive disclosure (whole-system zoom to single component) is the right shape for onboarding new collaborators onto CorpusIQ infrastructure |
| **Docs-site embed** | The static interactive page can be published under the hermes docs tree as a living architecture page |

## Limitations / Verification

- 94 installs and first-seen ~Aug 21, 2026 - early-stage skill; verify output quality on your own architecture before adopting as the canonical map.
- Single-skill pack; the value is the atlas format and interaction pattern, not a large toolkit.
- No long-run marketplace history yet - re-check the skills.sh security audits on later sweeps.

## Related

- [Skills Marketplace](/hermes/skills/marketplace) - more discovery batches
- [Hermes Field Kit Setup](/hermes/skills/catalog/hermes-field-kit-setup) - system inspect/diagnose/recover skills that pair with an atlas map
