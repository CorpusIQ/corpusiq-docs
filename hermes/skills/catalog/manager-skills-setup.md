---
title: "Manager Skills - Engineering Management Suite Setup"
description: "manager-dot-dev/manager-skills - 3.9K combined installs: skills for engineering managers covering 1:1s, feedback, hiring and planning."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/manager-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "engineering management", "leadership", "feedback"]
---

# Manager Skills - Engineering Management Suite Setup

**Source:** [manager-dot-dev/manager-skills](https://www.skills.sh/manager-dot-dev/manager-skills) via skills.sh - 3.9K combined installs across 27 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 morning sweep)
**GitHub:** [manager-dot-dev/manager-skills](https://github.com/manager-dot-dev/manager-skills) - 122 stars, MIT license, main branch, last pushed May 9, 2026; each skill lives in skills/<name>/SKILL.md with optional references/ support files.
**Category:** Engineering Management Skills
**Quality Tier:** 🟢 Green - all 15 sampled skills pass Gen Agent Trust Hub, Socket and Snyk.

manager-dot-dev is an opinionated library of Agent Skills for engineering managers, tech leads and directors, distilled from the author's newsletter, a decade of management reading, and his own experience. Each skill lives in skills/<name>/SKILL.md and triggers from realistic manager phrasing, asking only for the context that changes the advice and returning concise, manager-ready guidance instead of generic coaching.

The 27 indexed listings span the full management surface: 1:1s, feedback, hiring, performance reviews, delegation, roadmap planning, team health, stakeholder communication and personal effectiveness. The em-context foundation skill stores team and org context that the other skills read first, so repeated advice stays anchored to the manager's actual team. The repo last pushed May 9, 2026, roughly six months before this snapshot, and the install band is flat: every listing sits between 105 and 211 installs.

## Installation

Install with the Skills CLI in the project where you want the skills:

```bash
npx skills init
npx skills add manager-dot-dev/manager-skills
```

You can install a single skill instead:

```bash
npx skills add manager-dot-dev/manager-skills/skills/1on1s
```

Then create or update .agents/em-context.md with your team context so the other skills can tailor their advice.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| career-development | 211 | supporting career growth, promotion readiness and career conversations |
| delegation | 173 | moving managers out of the bottleneck role and building ownership |
| hiring | 170 | defining roles, structuring interviews, calibrating hiring and evaluating new hires |
| feedback | 167 | giving specific positive or corrective feedback and asking for feedback upward |
| roadmap-planning | 161 | planning roadmaps, prioritizing tech work and communicating tradeoffs |
| written-communication | 156 | drafting clear Slack messages, announcements and stakeholder updates |
| influence | 154 | persuading stakeholders and getting buy-in without direct authority |
| managing-up | 152 | building a reliable relationship with your manager and communicating upward |
| 1on1s | 152 | preparing, running, improving and following up on 1:1s |
| team-health | 149 | assessing and improving morale, trust, engagement and team culture |
| developer-productivity | 148 | measuring team productivity without harmful individual scoring |
| performance-reviews | 148 | diagnosing underperformance, writing reviews and deciding on PIPs or exits |
| meetings | 146 | deciding whether to meet, running better meetings and protecting focus time |
| knowledge-sharing | 140 | breaking knowledge silos and improving documentation and onboarding flow |
| managing-yourself | 139 | diagnosing personal EM traps, bad-day patterns and recurring tensions |
| shadow-work | 138 | identifying hidden capacity drains like support, glue work and shadow backlogs |
| managing-high-performers | 138 | managing top engineers, brilliant jerks, boredom, ambition and burnout risk |
| business-literacy | 137 | translating engineering work into business and finance language |
| difficult-situations | 135 | handling high-stakes management edge cases and sensitive situations |
| working-with-pm | 133 | building a stronger PM-EM partnership and improving product orientation |
| managing-urgency | 133 | handling deadlines, fake urgency, crisis pressure and tradeoff conversations |
| engineer-motivation | 133 | diagnosing what drives engineers and matching work to motivation |
| team-composition | 131 | diagnosing team capability gaps and hiring or assignment needs |
| management-transitions | 131 | navigating new-manager, inherited-team and acquisition transitions |
| retaining-developers | 128 | diagnosing attrition risk and preparing retention conversations |
| working-with-architects | 125 | working with architects, staff engineers and principal engineers |

The remaining 1 indexed listing is em-grid-scorer (105 installs), which scores an engineering manager's coverage across the 12 cells of the EM Grid from calendar and Slack data.

## Why This Matters for Hermes Agents

Engineering management is a domain where generic LLM advice is weak, and this library is explicitly built to be opinionated rather than safe. The skills trigger from realistic manager phrasing, not exact names, so a Hermes agent can step into a real 1:1 prep or a hard feedback conversation without a separate handoff. The em-context foundation skill acts as shared memory, so repeated advice stays anchored to the same team, people and org rather than starting over each session.

For an operator building management tooling, the library is a ready-made set of prompts and frameworks: SBI feedback statements, DORA and DevEx productivity models, Google's five team-health factors, and a database of 100 concrete team-improvement ideas. Each skill links to its source articles in references/sources.md, so every framework traces to the article or book that motivated it. The main caveat is the flat, modest install band and a six-month gap since the last push, which makes this a curated reading list distilled into skills more than a fast-moving project.

## Usage

| You say | What happens |
|---|---|
| Prepare for a 1:1 with a report | Uses 1on1s to build an agenda and diagnose a struggling relationship |
| Give hard feedback to a report | Uses feedback to script an SBI-framed conversation |
| Plan next quarter's roadmap | Uses roadmap-planning for prioritization and tradeoff framing |
| Figure out why the team feels burned out | Uses team-health for a factor-based diagnosis and activity ideas |
| Decide whether to promote internally or hire | Uses hiring for the promote-vs-hire call |
| Write an announcement for a reorg | Uses written-communication to draft the message |
| Show whether the team is getting faster | Uses developer-productivity for DORA and DevEx metrics |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/manager-dot-dev/manager-skills/main/README.md | head -40
```

Confirm the 1on1s skill body before installing:

```bash
curl -sL https://raw.githubusercontent.com/manager-dot-dev/manager-skills/main/skills/1on1s/SKILL.md | head -30
```

After install, confirm the skills landed under .agents/skills/, each directory holding a SKILL.md and optional references/.

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| career-development | Pass | Pass | Pass |
| delegation | Pass | Pass | Pass |
| hiring | Pass | Pass | Pass |
| feedback | Pass | Pass | Pass |
| roadmap-planning | Pass | Pass | Pass |
| written-communication | Pass | Pass | Pass |
| influence | Pass | Pass | Pass |
| managing-up | Pass | Pass | Pass |
| 1on1s | Pass | Pass | Pass |
| team-health | Pass | Pass | Pass |
| developer-productivity | Pass | Pass | Pass |
| performance-reviews | Pass | Pass | Pass |
| meetings | Pass | Pass | Pass |
| knowledge-sharing | Pass | Pass | Pass |
| managing-yourself | Pass | Pass | Pass |

All 15 sampled skills pass Gen Agent Trust Hub, Socket and Snyk.

## Limitations

- Snapshot data, verified Nov 24, 2026: 3,933 combined installs across 27 indexed listings; 122 GitHub stars; MIT license; last pushed May 9, 2026. Counts drift over time.
- The install band is flat: every listing sits between 105 and 211 installs, so no single skill is clearly dominant.
- The last push was May 9, 2026, roughly six months before this snapshot, so the library is in maintenance rather than active development.
- The tree ships 28 skill directories, but the em-context foundation skill carries no indexed install count, so only 27 listings appear in the index.
- skills.sh sampled 15 of the 27 listings; the other 12 carry no verdict in this snapshot.

## Related

- [GTM Agents - Go-to-Market & Sales Methodology](/hermes/skills/catalog/gtm-agents-setup)
- [writing-plans + subagent-driven-development Setup Guide](/hermes/skills/catalog/writing-plans-subagent-development-setup)
- [AgentMemory Setup - Persistent Memory for Hermes Agents](/hermes/skills/catalog/agentmemory-setup)
- [Review Loop Skill - Continuous Code Review Discipline](/hermes/skills/catalog/review-loop-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Set up .agents/em-context.md before first use so the skills tailor advice to your actual team instead of generic guidance.
- Stress the skills: ask for ideas, alternatives and pushback, since the author intends them as a thinking partner, not a how-to guide.
- Install individual skills (npx skills add manager-dot-dev/manager-skills/skills/1on1s) when you only need one management area.
- Treat the opinionated advice as a perspective to challenge, not universal truth, and follow your own judgement where you disagree.
- Follow the references/sources.md links when a framework needs its original article or book.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
