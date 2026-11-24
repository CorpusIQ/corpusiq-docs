---
title: "AWS Well-Architected Skills - Review and Steering Setup"
description: "aws-samples/sample-well-architected-skills-and-steering - 3.9K combined installs: AWS Well-Architected review skills and steering for coding agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/aws-well-architected-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "aws", "well-architected", "architecture"]
---

# AWS Well-Architected Skills - Setup Guide

**Source:** [aws-samples/sample-well-architected-skills-and-steering](https://www.skills.sh/aws-samples/sample-well-architected-skills-and-steering) via skills.sh - 3.9K combined installs across 15 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 morning sweep)
**GitHub:** [aws-samples/sample-well-architected-skills-and-steering](https://github.com/aws-samples/sample-well-architected-skills-and-steering) - 282 stars, MIT-0, main branch, last pushed Oct 26, 2026; skills under skills/<name>/SKILL.md, steering documents under powers/ and steering/, with per-tool adapters under adapters/ for 14 runtimes.
**Category:** AWS Architecture and Well-Architected Review
**Quality Tier:** 🟠 Orange - wa-review and aws-well-architected-framework-review carry Fail cells (Gen Agent Trust Hub).

This is an AWS sample repository, not a released product: aws-samples/sample-well-architected-skills-and-steering demonstrates reusable skills and steering that teach AI coding agents how to apply the AWS Well-Architected Framework. One set of playbooks ships as Agent Skills, steering documents and per-tool adapters for 14 supported runtimes (Claude Code, Codex, Cursor, Kiro, Gemini CLI, Copilot, Windsurf and others), so the same review guidance can be surfaced in many tools without re-authoring.

The core skill, aws-well-architected-framework-review, evaluates all 57 framework questions across 6 pillars and produces evidence-backed findings with prioritized remediation; wa-builder, wa-guardrails and wafr-facilitator extend that into learning artifacts, preventive controls and customer facilitation. The six pillar aliases (security-assessment, cost-optimization-review and so on) route to the framework review skill with a single-pillar scope. The review reference data spans 307 best practices plus 27 lens extensions, loaded one pillar file at a time.

## Installation

The README documents a skills.sh one-liner, a bootstrap script and a local install script. The fastest path:

```bash
npx skills add aws-samples/sample-well-architected-skills-and-steering
```

Preview the available skills, or install one specifically:

```bash
npx skills add aws-samples/sample-well-architected-skills-and-steering --list
npx skills add aws-samples/sample-well-architected-skills-and-steering --skill aws-well-architected-framework-review
```

For a global, user-level install across all projects:

```bash
npx skills add aws-samples/sample-well-architected-skills-and-steering -g
```

Alternatively, the bootstrap script auto-detects your installed AI tools and installs for all of them:

```bash
curl -sL https://raw.githubusercontent.com/aws-samples/sample-well-architected-skills-and-steering/main/bootstrap.sh | bash
```

The repository is also a conformant Agent Plugins 1.0.0 package via its root plugin.json, and includes a per-tool install.sh script for local clones.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| migration-readiness | 569 | assessing workload readiness to migrate to AWS (the 7 Rs) |
| wa-review | 413 | no counterpart in the current skills/ tree; not described in the README skills overview |
| wa-guardrails | 388 | generating preventive guardrails (Config rules, SCPs, CI checks, alarms) |
| aws-well-architected-framework-review | 345 | a full review across 6 pillars and 57 questions with citations |
| wafr-facilitator | 335 | facilitating a conversational WAFR with customers |
| wa-builder | 293 | learning WA and producing diagrams, decision trees and roadmaps |
| architecture-decision-record | 224 | wa-builder ADR mode; also a Claude Code command |
| security-assessment | 219 | Security pillar deep-dive |
| performance-efficiency | 217 | Performance Efficiency pillar deep-dive |
| reliability-improvement-plan | 216 | Reliability pillar deep-dive |
| operational-excellence | 212 | Operational Excellence pillar deep-dive |
| sustainability-optimization | 208 | Sustainability pillar deep-dive |

The remaining 3 indexed listings range from 20 to 194 installs (cost-optimization-review 194, example-skill 83, cost-optimization-audit 20).

## Why This Matters for Hermes Agents

A Well-Architected review is normally a consultant-led exercise, and this repository turns it into a repeatable agent workflow with the framework's actual questions and best practices encoded as reference data. That matters because an agent asked to review a workload otherwise produces generic advice without the evidence trail or the pillar-by-pillar citations a real review requires. The review skill is structured to cite the specific best practice behind each finding, which makes its output auditable rather than hand-wavy. wa-guardrails extends the value past a one-off assessment by turning findings into ongoing controls (Config rules, SCPs and CI checks), so the review becomes a gate instead of a snapshot. The 14-tool adapter layer is worth studying on its own: it shows one portable core translated into Claude Code commands, Cursor rules, Copilot instructions and other formats, which is the pattern an operator would use to standardize steering across a fleet of agents. The caveat is that this is a sample repository, so treat the guidance and the evaluation tooling as demonstration material rather than a supported AWS service.

## Usage

| You say | What happens |
|---|---|
| Run a Well-Architected review of my service | aws-well-architected-framework-review evaluates all 6 pillars and cites best practices |
| Assess whether we are ready to migrate to AWS | migration-readiness analyzes code, dependencies and configuration for the 7 Rs |
| Turn our review findings into ongoing controls | wa-guardrails generates Config rules, SCPs and CI policy checks |
| Help me run a WAFR with a customer | wafr-facilitator prepares tailored questions and probing follow-ups |
| Show me an annotated architecture diagram | wa-builder produces diagrams with pillar health overlays |
| Just review the Security pillar | security-assessment routes to the framework review with Security scope |
| Keep our workload compliant over time | wa-guardrails codifies the fixes as always-on steering |

## Verification

Confirm the framework review skill body resolves on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/aws-samples/sample-well-architected-skills-and-steering/main/skills/aws-well-architected-framework-review/SKILL.md | head -30
```

Preview what the installer will bring before committing:

```bash
npx skills add aws-samples/sample-well-architected-skills-and-steering --list
```

After install, confirm the skills landed in the agent skills directory (for example ~/.claude/skills for Claude Code).

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| migration-readiness | Pass | Pass | Pass |
| wa-review | Fail | Pass | Pass |
| wa-guardrails | Pass | Pass | Warn |
| aws-well-architected-framework-review | Fail | Pass | Pass |
| wafr-facilitator | Pass | Pass | Warn |
| wa-builder | Pass | Pass | Warn |
| architecture-decision-record | Pass | Pass | Warn |
| security-assessment | Pass | Pass | Pass |
| performance-efficiency | Pass | Pass | Pass |
| reliability-improvement-plan | Pass | Pass | Pass |
| operational-excellence | Pass | Pass | Pass |
| sustainability-optimization | Pass | Pass | Pass |
| cost-optimization-review | Pass | Pass | Pass |
| example-skill | Pass | Pass | Pass |
| cost-optimization-audit | not parsed | not parsed | not parsed |

## Limitations

- Snapshot data, verified Nov 24, 2026: 3,936 combined installs across 15 indexed listings; 282 GitHub stars; MIT-0 license; last pushed Oct 26, 2026. Counts drift over time.
- This is an AWS sample repository, not a released product; treat it as demonstration material rather than a supported AWS service.
- wa-review carries a Fail verdict and has no counterpart in the current skills/ tree, so the install index and the repository disagree on that listing.
- cost-optimization-audit returned "not parsed" on all three skills.sh checks, so it has no security signal at snapshot time.
- The pillar aliases (security-assessment, cost-optimization-review and the other four) route to the framework review skill rather than shipping standalone skill directories.
- The review skill loads reference data one pillar file at a time, so a full review reads a large amount of reference material.

## Related

- [AWS Agent Toolkit - Official AWS Skills for Hermes Agents](/hermes/skills/catalog/aws-agent-toolkit-setup)
- [AWS Skills - CDK, Serverless and Cost Ops Setup](/hermes/skills/catalog/zxkane-aws-skills-setup)
- [System Design Skills - Reasoning-Driven Architecture](/hermes/skills/catalog/system-design-skills-setup)
- [Cloudflare Skills - Edge Computing & Workers Platform](/hermes/skills/catalog/cloudflare-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with aws-well-architected-framework-review for a full assessment, then use the pillar aliases to scope a single pillar.
- Use --list first to preview the skills the installer will bring before a full install.
- Prefer the --symlink flag (or -Symlink on PowerShell) so upstream updates flow into your project without reinstalling.
- Run wa-guardrails after a review to convert findings into preventive controls rather than a one-off assessment.
- Treat the adapters/ directory as the source of truth for tool-specific steering, and the skills/ directory as the portable core.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
