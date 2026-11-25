---
title: "Pipa Skills - Service Business Operations Setup"
description: "lunchpaillola/pipa-skills - 8.8K combined installs: operational skills that put service-business workflows into the agents you already use."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pipa-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "operations", "project management", "service business"]
---

# Pipa Skills - Setup Guide

**Source:** [lunchpaillola/pipa-skills](https://www.skills.sh/lunchpaillola/pipa-skills) via skills.sh - 8.8K combined installs across 67 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 evening sweep)
**GitHub:** [lunchpaillola/pipa-skills](https://github.com/lunchpaillola/pipa-skills) - 3 stars, MIT license, main branch, last pushed Oct 25, 2026; skills live under skills/<name>/SKILL.md with a pipa root router, six business-lane skills and a set of lane-owned operation skills.
**Category:** Service Business Operations (Agent Skills)
**Quality Tier:** 🟠 Orange - pipa-audio-brief fails Gen Agent Trust Hub and Snyk, pipa-huddle-beta and pipa-time-tracking fail Snyk, and most other sampled skills carry Warn cells.

lunchpaillola/pipa-skills publishes Pipa, a suite of operational skills that layer service-business workflows - getting opportunities, defining scope, coordinating delivery, collecting money, keeping clients and improving operations - on top of the agent a user already runs. Built by Lola at Lunch Pail Labs, it is organized as a pipa root router that routes business work into six lanes and two meta surfaces (Manage Pipa and Pipa Tools), with narrow operation skills beneath each lane.

The README documents 67 indexed listings at 8.8K combined installs, but the current tree carries 39 skill directories. The 26 pm-* listings and generate-synthetic-data (all at 1-2 installs) have no matching directory, and composio-mcp is listed under a name that differs from its skills/composio/ directory. The pipa-* skills are the live set.

## Installation

Install the full skill pack:

```bash
npx skills add lunchpaillola/pipa-skills
```

Install one self-contained capability, or list every available skill:

```bash
npx skills add lunchpaillola/pipa-skills --skill pipa-audio-brief
npx skills add lunchpaillola/pipa-skills --list
```

Update later:

```bash
npx skills update lunchpaillola/pipa-skills
```

The pipa root router and business lane skills require the full pack because they delegate to operation skills; do not install pipa or a lane by itself. Single-skill install is only for a self-contained operation such as pipa-audio-brief. To clone instead:

```bash
git clone https://github.com/lunchpaillola/pipa-skills.git
cp -r pipa-skills/skills/* .agents/skills/
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| pipa-huddle-beta | 317 | start a live voice huddle to talk through work with Pipa or the active agent |
| pipa-follow-up-reminders | 237 | create and cancel one-shot email follow-up reminders through Pipa |
| pipa-improve-operations | 234 | run shutdown, acceptance, handover, retrospective or closeout to improve operations |
| pipa-audio-brief | 234 | turn sessions, PRs, plans, docs and links into a listenable audio brief |
| pipa-time-tracking | 233 | start, stop, switch, backfill and summarize work time entries |
| pipa-keep-clients | 233 | maintain client trust through follow-ups, check-ins and relationship care |
| pipa-tools | 232 | route standalone Pipa utilities such as audio briefs, huddles and reminders |
| pipa-manage | 232 | manage Pipa configuration, connectors, memory, permissions and automations |
| pipa-get-paid | 232 | track invoices, payments, billable time, budgets, margin and payment follow-through |
| pipa-deliver-work | 232 | coordinate active delivery: status, blockers, risks, handoffs and next actions |
| pipa-define-work | 232 | turn fuzzy demand into defined work via one focused operation |
| composio-mcp | 232 | route external app work through the Composio MCP |

The remaining 55 indexed listings range from 1 to 231 installs.

Index-vs-tree drift: composio-mcp (232) lives in the skills/composio/ directory (the README maps the composio-mcp name to that path), and a separate composio listing (2 installs) points at the same directory. The 26 pm-* listings and generate-synthetic-data have no matching directory in the current tree.

## Why This Matters for Hermes Agents

Pipa is a worked example of intent routing: a single pipa entry skill classifies the user's ask into one of six business lanes and delegates to a narrow operation skill, so generic language reaches specialized workflows without the user memorizing skill names. The lane-plus-operation split (six lanes, two meta surfaces, many narrow operations) is a layout worth copying for any Hermes agent that serves a multi-step domain. Each skill ships evals.json plus trigger-eval sets, and the repository validates skill architecture and frontmatter in CI, which is the kind of coverage a serious skills catalog should have. The Composio-backed connector path shows how to give an agent external app access with tool discovery and authorization links. The router and lanes are a pack, not individual skills, which forces the installer to reason about dependencies up front.

## Usage

| You say | What happens |
|---|---|
| Plan my workday | Routes through pipa into a lane and a daily plan operation |
| Remind me tomorrow at 9 to follow up | Uses pipa-follow-up-reminders to schedule a one-shot email reminder |
| Give me an audio brief of this PR | Uses pipa-audio-brief to turn the PR into a listenable brief |
| Start tracking my time | Uses pipa-time-tracking to start a work time entry |
| Talk this through by voice | Uses pipa-huddle-beta to start a live voice huddle |
| What should we charge for this change? | Uses pipa-change-control to work out the money impact |
| Shut down work for the day | Uses pipa-improve-operations to run the daily shutdown |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/lunchpaillola/pipa-skills/main/README.md | head -40
```

Review the root router skill before installing:

```bash
curl -sL https://raw.githubusercontent.com/lunchpaillola/pipa-skills/main/skills/pipa/SKILL.md | head -30
```

After installing, `npx skills add lunchpaillola/pipa-skills --list` prints every available skill.

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| pipa-huddle-beta | Pass | Warn | Fail |
| pipa-follow-up-reminders | Pass | Warn | Warn |
| pipa-improve-operations | Pass | Pass | Warn |
| pipa-audio-brief | Fail | Warn | Fail |
| pipa-time-tracking | Pass | Warn | Fail |
| pipa-keep-clients | Pass | Pass | Warn |
| pipa-tools | Pass | Pass | Pass |
| pipa-manage | Pass | Pass | Warn |
| pipa-get-paid | Pass | Pass | Warn |
| pipa-deliver-work | Pass | Pass | Warn |
| pipa-define-work | Pass | Pass | Warn |
| composio-mcp | Pass | Pass | Pass |
| pipa | Pass | Pass | Pass |
| pipa-triggers | Pass | Warn | Pass |
| pipa-get-work | Pass | Pass | Warn |

Only 15 of the 67 listings were sampled. pipa-audio-brief fails both Gen Agent Trust Hub and Snyk, and pipa-huddle-beta plus pipa-time-tracking fail Snyk.

## Limitations

- Snapshot data, verified Nov 24, 2026: 8,787 combined installs across 67 indexed listings; 3 GitHub stars; MIT license; last pushed Oct 25, 2026. Counts drift over time.
- Index-vs-tree drift: the index lists 67 listings but the current tree carries 39 skill directories; 26 pm-* listings and generate-synthetic-data have no directory, and composio-mcp is listed under a name that differs from its skills/composio/ directory.
- The pipa root router and lane skills must be installed as the full pack; single-skill install is only valid for self-contained operations such as pipa-audio-brief.
- Three sampled skills carry Fail cells (pipa-audio-brief, pipa-huddle-beta, pipa-time-tracking) and most others carry Warn cells; re-check before production use.
- Some workflows depend on connected services (Composio, email reminders, voice relays), so the skill alone is not enough without the account setup.

## Related

- [manager-dot-dev - Engineering Management Skills Setup](/hermes/skills/catalog/manager-skills-setup)
- [FuDesign2008 Open Skills - Jira, Git and Workflow Setup](/hermes/skills/catalog/fudesign-open-skills-setup)
- [Darkmatter Skills - Team Skill Catalog Setup](/hermes/skills/catalog/darkmatter-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the full pack first; the pipa router and lanes delegate to operation skills and break if installed alone.
- Use --list before installing to see the exact skill names, since the index carries listings the tree no longer has.
- Connect your account and Composio before relying on audio briefs, reminders or voice huddles; several workflows need external services.
- Treat the six-lane router as the reference pattern if you are building your own intent-routing entry skill.
- Read the pipa skill's references/help-menu.md to see how the root router presents its help surface.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
