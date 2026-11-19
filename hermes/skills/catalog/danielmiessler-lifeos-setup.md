---
title: "Daniel Miessler LifeOS - Life Operating System Setup"
description: "danielmiessler/lifeos: 8.1K combined installs across 90 listings; a personal AI operating system of research, security and creative skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/danielmiessler-lifeos-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "ai harness", "research", "security"]
---

# Daniel Miessler LifeOS - Setup Guide

**Source:** [danielmiessler/lifeos](https://www.skills.sh/danielmiessler/lifeos) via skills.sh - 8.1K combined installs across 90 indexed listings; first seen Nov 18, 2026 (Nov 18, 2026 evening sweep)
**GitHub:** 19,939 stars, MIT licence, `main` branch, last pushed 2026-11-18. Skills live as `LifeOS/install/skills/<Name>/SKILL.md`, one directory per skill; several indexed names have no matching directory in the current tree.
**Category:** Personal AI operating system (harness)
**Quality Tier:** 🟠 Orange - 4 Fail cells among the 12 sampled skills (PrivateInvestigator, Council, Recon, WebAssessment); MIT licence.

LifeOS is Daniel Miessler's general-purpose AI harness, a personal AI operating system built around one idea: moving from your Current State to your Ideal State. It captures who you are, what you care about, and where you are going, then layers memory, skills, routing and self-improvement on top of any capable agent harness (Claude Code, Cursor, Codex, Hermes). The README counts 97 public skills spanning research, security, writing, art, video, publishing and home.

On skills.sh the suite indexes as 90 listings, with a research and security core at the top of the install list. Several of those top listings (OSINT, Recon, WebAssessment, PromptInjection) are offensive-security and OSINT research playbooks, and the repo is in constant flux: it was pushed on the snapshot day, and a number of indexed names have no matching skill directory in the current tree.

## Installation

LifeOS is installed by an AI, so the install is a prompt. Paste this into Claude Code, Cursor, Codex, Hermes, or any capable agent:

```
Read https://ourlifeos.ai/install and install LifeOS for me.
```

There is also a one-line terminal shortcut for Claude Code on macOS or Linux:

```bash
curl -fsSL https://ourlifeos.ai/install.sh | bash
```

Either path needs a capable AI coding harness and bun. The installer asks for confirmation before touching anything and asks you to acknowledge that you are responsible for your own system's security.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| OSINT | 426 | Open-source intelligence gathering playbook; the current tree carries no OSINT skill directory, so its workflow is not described in the fetched repo. |
| Documents | 283 | Document handling; the current tree has Docx, Pdf and HTML skills but no Documents directory. |
| FirstPrinciples | 213 | Physics-based reasoning that deconstructs a problem to fundamentals, classifies constraints, and rebuilds the solution. |
| PrivateInvestigator | 171 | Ethical people-finding and identity verification via parallel research agents, with confidence-scored results (removed from the current tree). |
| RedTeam | 157 | Adversarial analysis deploying parallel expert agents to stress-test ideas, plus 11 world models over 6 months to 50 years. |
| Council | 150 | Multi-agent collaborative debate producing round-by-round transcripts with real intellectual friction. |
| Recon | 142 | Reconnaissance playbook; no matching skill directory in the current tree. |
| Art | 138 | Static visual content in 20+ formats (diagrams, infographics, comics, icons, wallpaper) via Nano Banana and Flux. |
| Prompting | 135 | Meta-prompting library for generating, optimizing and composing prompts via Standards, Handlebars templates and tools. |
| Browser | 135 | Browser automation; no Browser skill directory in the current tree (a ComputerUse skill exists separately). |
| agents | 134 | Agent definitions; the current tree keeps these as LifeOS/install/agents/*.md rather than a single skill. |
| WebAssessment | 127 | Web assessment playbook; no matching skill directory in the current tree. |
| PromptInjection | 126 | Prompt injection testing playbook; no matching skill directory in the current tree. |
| Research | 125 | Multi-agent web research with verified URLs and confidence-tagged output at four depths. |
| Apify | 124 | Scrape social platforms and business data via Apify actors (Instagram, LinkedIn, TikTok, YouTube, Amazon), filtering in code (removed from the current tree). |
| Fabric | 123 | Ideal-state ports of the most-used Fabric patterns, each with its own eval suite. |
| BeCreative | 123 | Single-pass divergent ideation via verbalized sampling that surfaces the strongest of several candidates. |
| THEALGORITHM | 122 | The LifeOS hill-climbing algorithm; no THEALGORITHM directory (the algorithm content lives under LifeOS/install/LIFEOS/ALGORITHM/). |
| CreateSkill | 120 | Mandatory orchestrator for scaffolding, editing, validating and testing any LifeOS skill. |

The remaining 71 indexed listings range from 9 to 118 installs.

## Why This Matters for Hermes Agents

LifeOS is a reference implementation of a harness layer rather than a bag of one-off prompts. Every skill is a self-contained `SKILL.md` with a clear USE WHEN / NOT FOR contract, so an agent can route a request to the right workflow instead of guessing. The research cluster is the strongest part: multi-agent web research with verified URLs, adversarial red-teaming, and multi-perspective debate are patterns a builder can lift into their own agent setup.

Several top listings are offensive-security and OSINT research playbooks (OSINT, Recon, WebAssessment, PromptInjection, RedTeam, PrivateInvestigator). They are documented research and testing workflows, but the repo is explicit that security is the operator's responsibility, and these skills should only run against systems you own or are authorized to test.

The repo changes quickly and some indexed listings have drifted out of the current tree, so pin a commit or treat installs as a snapshot. The Security section below carries the sampled verdicts; the README's own warning is worth reading before production use.

## Usage

| You say | What happens |
|---|---|
| "Do some research on X" | Research runs multi-agent web research and returns verified URLs with confidence tags. |
| "Stress-test this plan" | RedTeam deploys parallel expert agents to attack claims and returns severity-ranked findings. |
| "Weigh these options" | Council runs a multi-agent debate and returns a round-by-round transcript. |
| "Get me to the fundamentals of this problem" | FirstPrinciples deconstructs the problem and rebuilds it from fundamentals alone. |
| "Illustrate this idea" | Art generates diagrams, infographics, comics or wallpaper images. |
| "Write a better prompt for this task" | Prompting composes and optimizes a prompt via Standards and Handlebars templates. |
| "Find this person" | PrivateInvestigator runs parallel people-search agents (a skill removed from the current tree, so confirm it is present first). |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/danielmiessler/LifeOS/main/LifeOS/install/skills/FirstPrinciples/SKILL.md
```

The top listing by installs, OSINT, has no matching directory in the current tree, so probe a skill that actually exists in the repo before relying on it. Then install via the prompt or the curl shortcut above and confirm the harness walks the setup.

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| OSINT | Warn | Warn | Warn |
| Documents | Pass | Warn | Pass |
| FirstPrinciples | Pass | Pass | Pass |
| PrivateInvestigator | Pass | Warn | Fail |
| RedTeam | Pass | Pass | Warn |
| Council | Pass | Pass | Fail |
| Recon | Warn | Warn | Fail |
| Art | Pass | Warn | Pass |
| Prompting | Pass | Pass | Pass |
| Browser | Warn | Pass | Pass |
| agents | Pass | Pass | Pass |
| WebAssessment | Pass | Fail | Pass |

The sample covers 12 of the 90 indexed listings. Several of the offensive-security and OSINT listings carry Warn or Fail cells, and the README's own security section states plainly that responsibility for the security of your system is yours, not the authors'. The installer asks you to acknowledge that before it proceeds.

## Limitations

- Snapshot data, verified Nov 18, 2026: 8,127 combined installs across 90 indexed listings; 19,939 GitHub stars; MIT licence; last pushed 2026-11-18. Counts drift over time.
- The install index outruns the tree: OSINT, Documents, Recon, Browser, agents, WebAssessment, PromptInjection and THEALGORITHM carry install counts but have no matching skill directory in the current tree, and PrivateInvestigator and Apify were removed after being indexed.
- Several skills are offensive-security and OSINT research playbooks; only run them against systems you own or are authorized to test, and re-read the repo's "Your Security Is Your Responsibility" warning.
- LifeOS is one person's personal harness published as-is and constantly changing, so individual skills can be added, renamed or removed between releases.
- The whole system is a harness install, not a single skill drop-in, and needs bun plus a capable agent to set up.

## Related

- [OSINT Skills - Open-Source Intelligence Suite Setup](/hermes/skills/catalog/osint-skills-setup)
- [Security Hardening - AI Agent Security Setup](/hermes/skills/catalog/security-and-hardening-setup)
- [Deep Research Skill - Citation-Tracked Research Setup](/hermes/skills/catalog/claude-deep-research-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Pin a commit or read a skill's SKILL.md directly from raw.githubusercontent before relying on it, because the tree changes fast.
- Start with the research cluster (Research, FirstPrinciples, RedTeam, Council) before touching the offensive-security playbooks.
- Use Fabric to pull the Fabric patterns you already know into the LifeOS eval model.
- Treat the install as a whole-harness setup, not a skill-by-skill drop-in; the prompt installs the full system.
- Re-check the security pages on skills.sh before any production use of the Warn or Fail skills.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
