---
title: "Marketing Mindset - B2B Marketing OS for AI Agents Setup"
description: "axelfreeman/marketing-mindset - marketing-mindset skill, 28.8K installs, 52 GitHub stars. A 15-year B2B marketer's operating framework for agents: six decision principles, three-month horizons, and client-stage playbooks that turn 'should I do X to get Y' questions into testable marketing actions. Hermes explicitly listed in the adapter table."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/marketing-mindset-setup/"
robots: "index,follow"
last_updated: "2026-09-07"
tags: ["hermes skill", "agent skill", "skill setup", "marketing", "growth", "b2b", "positioning"]
---

# Marketing Mindset - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/axelfreeman/marketing-mindset) (28.8K installs)
**GitHub:** [axelfreeman/marketing-mindset](https://github.com/axelfreeman/marketing-mindset) (52⭐, MIT)
**Category:** Marketing / Growth Strategy
**First Seen:** Sep 2026 (repo created Sep 1, 2026)
**Quality Tier:** 🟢 Production (Gen Agent Trust Hub Pass / Socket Pass / Snyk Pass)

Marketing Mindset is "the marketing OS for AI agents" by Axel Freeman - a 15-year hands-on B2B internet marketer. It is deliberately not another bag of CRO/SEO/copywriting tactics; it encodes how a working marketer decides, so an agent gives a real opinion instead of a template. Six principles (no stale sources, three-month horizons, user's right to make the first move, fast-testable hypotheses, marketing runs ahead of the product, marketing never works for free) plus client-stage playbooks, competitor-as-source-of-truth rules, and memorable heuristics. The README's adapter table lists Hermes (Nous) as a tested platform using SKILL.md, alongside Claude Code, Codex, Cursor, ChatGPT, Grok, and others.

---

## Installation

```bash
npx skills add axelfreeman/marketing-mindset
```

For weaker or low-context models the publisher ships a compressed variant (`SKILL.lite.md`) with the same mindset condensed to essentials. A first-client gate script (`scripts/first-client-gate.py`) is included for evaluation.

## Prerequisites

| Requirement | Details |
|---|---|
| **No API keys** | Fully self-contained skill - SKILL.md, principles, and playbooks |
| **Hermes Agent** | Reads SKILL.md natively; listed in the publisher's tested-models table |
| **Optional: examples** | `examples/demo-transcript.md` shows a worked example (SaaS for finance, 0 customers → sharp 3-month plan) |

## What It Provides

| Capability | How It Works |
|---|---|
| **Decision framework** | Evaluates "should I do X to get Y" requests against the six principles instead of dumping tactics |
| **Three-month horizon** | Kills 2-year marketing cycles; every idea evaluated on a 90-day usefulness window |
| **Client-stage playbook** | First client by hand and free → 2-10 by copying competitors → scale |
| **Competitor source of truth** | Positioning and angles reverse-engineered from what competitors actually do |
| **First-move doctrine** | The user has the right to make the first move - bold or hacky first steps are not blocked |
| **Exchange accounting** | Every marketing action must trade for something; zero-exchange work is refused with the math spelled out |
| **Heuristics** | The McDonald's Burger (photograph the product better than it is), think like a cancer cell, the stop-list, the Despair Dividend |

## Quick Start

1. Install the skill (above)
2. Trigger it with a decision question: "should we do X to get Y", "where do we get first customers", or "evaluate this positioning"
3. The skill answers as a director-level marketer - honest feedback, three-month framing, concrete deliverables (competitor analysis, three outbound angles, sharper positioning)
4. For a worked example, read `examples/demo-transcript.md`
5. Pair with execution skills (cold-email, content-strategy) once the direction is decided

## CorpusIQ Use Cases

- **Positioning and launch work** - sharpen CorpusIQ messaging, launch plans, and competitive angles with an operator's framework rather than generic LLM doctrine
- **Outreach decision support** - judge cold-outreach campaigns and affiliate programs against the exchange principle before burning sends
- **Content angle selection** - belief-bridge and help-first content angles stress-tested against the three-month usefulness window
- **Growth experiment design** - every hypothesis must be fast-testable by any teammate; the skill enforces the test design discipline
- **Investor and partner decks** - marketing claims and go-to-market narratives get the same honest due-diligence read the skill gives founders

## Limitations / Verification

- **Opinionated framework** - the skill is one marketer's method, not a strategy library; it deliberately ships judgment, not templates
- **Freshness dependency** - principle 1 forbids learning from stale sources; the skill expects recent data to work from, which agents must fetch themselves
- **B2B bias** - strongest for services and B2B SaaS; consumer and marketplace dynamics get partial coverage

## Security

All three skills.sh security audits pass (verified Sep 7, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Pass |
| Socket | Pass |
| Snyk | Pass |

## Related

- [Content Strategy - Full Planning Framework Setup](/hermes/skills/catalog/content-strategy-setup/)
- [Revenue-Centric Design Skill - SaaS Conversion Playbook Setup](/hermes/skills/catalog/revenue-centric-design-setup/)

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Discovery Page](/hermes/skills/marketplace/new-sep7-2026/) →*
*Powered by CorpusIQ*
