---
title: codebase-design - Deep Module Design Vocabulary
description: "Install and use mattpocock/skills@codebase-design (584K+ installs) - shared vocabulary for designing deep modules: interfaces, seams, adapters, depth, leverage and locality for AI-navigable codebases."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/codebase-design-setup/"
robots: "index,follow"
last_updated: "2026-09-09"
tags: ["hermes skill", "agent skill", "skill setup", "codebase design", "architecture"]
---

# codebase-design - Setup Guide

**Source:** [mattpocock/skills](https://skills.sh/mattpocock/skills/codebase-design) (584,794 installs)
**Skill:** `mattpocock/skills@codebase-design`
**Installs:** 584,794
**Category:** Software Engineering / Architecture
**First Seen:** Sep 9, 2026

`codebase-design` is Matt Pocock's shared vocabulary for designing **deep modules** - a lot of behaviour behind a small interface, placed at a clean seam, testable through that interface. It is a language skill: it gives the agent precise, consistent terms (module, interface, seam, adapter, depth, leverage, locality) to use wherever code is designed or restructured. The point is consistent vocabulary across sessions, so design discussions between an agent and a codebase stay coherent instead of drifting between "component", "service", "API", and "boundary".

---

## Installation

```bash
npx skills add mattpocock/skills --skill codebase-design
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Any recent version with skill support |
| **Node.js 18+** | For the `npx skills` CLI |
| **A codebase to design in** | Works on any language; examples are TypeScript-flavoured |

---

## What It Provides

| Concept | Definition | Agent Trigger |
|---|---|---|
| **Deep module** | Small interface + lots of implementation; leverage for callers | "design/improve this module's interface" |
| **Shallow module** | Large interface + thin implementation; the anti-pattern | "find deepening opportunities" |
| **Seam** | Where behaviour can be altered without editing in that place (Feathers) | "decide where the seam goes" |
| **Adapter** | A concrete thing satisfying an interface at a seam; describes role, not substance | "make this testable / AI-navigable" |
| **Depth** | Leverage at the interface: behaviour exercised per unit of interface learned | "is this module deep enough?" |
| **Locality** | What maintainers get: change, bugs, knowledge, verification concentrate in one place | "should this live here?" |

## Key Principles

- **Depth is a property of the interface, not the implementation.** A deep module can be internally composed of small, mockable parts - they just aren't part of the interface.
- **The deletion test.** Imagine deleting the module. If complexity vanishes, it was a pass-through. If complexity reappears across N callers, it was earning its keep.
- **The interface is the test surface.** Callers and tests cross the same seam. If you want to test past the interface, the module is probably the wrong shape.
- **One adapter means a hypothetical seam. Two adapters means a real one.** Don't introduce a seam unless something actually varies across it.
- **Designing for testability:** accept dependencies, don't create them; return results, don't produce side effects; keep surface area small.
- **Rejected framings** (documented explicitly): depth as implementation-lines/interface-lines ratio; "interface" as the TypeScript keyword only; "boundary" (overloaded with DDD bounded context) - say seam or interface.

## Quick Start

1. Install the skill: `npx skills add mattpocock/skills --skill codebase-design`
2. Invoke it when designing a module interface, finding deepening opportunities, deciding where a seam goes, or making code testable / AI-navigable
3. The skill loads the full glossary plus two companion files: `DEEPENING.md` (dependency categories, seam discipline, replace-don't-layer testing) and `DESIGN-IT-TWICE.md` (design the interface several radically different ways via parallel sub-agents, then compare on depth, locality, seam placement)

## Limitations / Verification

```bash
# Verify skill installed
hermes skills list | grep codebase-design

# Functional test: ask the agent to apply the vocabulary
# "Using codebase-design: identify the seams in this repo and mark which are deep vs shallow"
```

- Vocabulary skill: no scripts or binaries; value is consistent design language across agent sessions
- Companion docs DEEPENING.md / DESIGN-IT-TWICE.md ship inside the skill directory

## Security

- [skills.sh listing](https://skills.sh/mattpocock/skills/codebase-design) - Pass
- [GitHub repo](https://github.com/mattpocock/skills) - Pass
- [Publisher](https://github.com/mattpocock) - Pass (146K+ stars, TypeScript educator)

## Related

- [Matt Pocock Agent Workflow Suite - 20-Skill Setup](/docs/hermes/skills/catalog/mattpocock-agent-workflow-suite-setup)
- [Resolving Merge Conflicts Setup](/docs/hermes/skills/catalog/resolving-merge-conflicts-setup)
- [Matt Pocock Engineering Skills Setup](/docs/hermes/skills/catalog/matt-pocock-engineering-setup)
- [Mattpocock Skills Setup](/docs/hermes/skills/catalog/mattpocock-skills-setup)
