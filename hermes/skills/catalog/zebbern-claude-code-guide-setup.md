---
title: "Zebbern Claude Code Guide - Usage and Pentest Skills Setup"
description: "zebbern/claude-code-guide: 6.0K combined installs across 87 listings; a Claude Code usage guide plus a large penetration-testing playbook set."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/zebbern-claude-code-guide-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "claude code", "security", "penetration testing"]
---

# Zebbern Claude Code Guide - Setup Guide

**Source:** [zebbern/claude-code-guide](https://www.skills.sh/zebbern/claude-code-guide) via skills.sh - 6.0K combined installs across 87 indexed listings; first seen Nov 18, 2026 (Nov 18, 2026 evening sweep)
**GitHub:** 4,716 stars, MIT licence, `main` branch, last pushed 2026-11-18. The repo combines a long written Claude Code guide in the README with a `skills/` directory of agent skills and an `agents/` pack of sub-agent definitions for Claude Code and Codex.
**Category:** Claude Code usage guide and security skills
**Quality Tier:** 🟠 Orange - 2 Fails among 12 sampled skills (ethical-hacking-methodology, aws-penetration-testing); all 12 sampled skills carry at least one Warn.

The everyday part of this repo is a comprehensive, community-maintained Claude Code guide: installation and auth, configuration and environment variables, the slash-command and CLI-flag references, sub-agents, MCP, hooks, and troubleshooting. Alongside it sits a `skills/` directory that includes general-purpose developer skills such as React and Next.js best practices, TypeScript, Playwright, code-to-diagram, and test-suite authoring, plus the `agents/` pack of sub-agent definitions.

A large share of the indexed listings are something else entirely: penetration-testing playbooks. Of the 87 indexed skills, the top 14 by installs are all offensive-security material covering ethical-hacking methodology, pentest checklists and commands, WordPress, SQL, SSH, SMTP, AWS, and cloud penetration testing, Metasploit, Active Directory attacks, Linux privilege escalation, and HTML injection testing. These are playbooks for authorised security assessments; the Security section below carries the skills.sh verdicts for the sampled set, and the offensive material should be used only for authorised testing.

## Installation

The repo is a written guide first, so most of it is read directly. To bring the bundled skills into an agent, clone the repo and reference or copy the skill directories:

```bash
git clone --depth 1 https://github.com/zebbern/claude-code-guide.git
```

Skills live under `skills/<name>/SKILL.md`; the sub-agents live under `agents/.claude/agents/` (for Claude Code) and `agents/.codex/agents/` (for Codex). Copy the individual `SKILL.md` files into your agent's skills directory, or point your agent at the cloned repo.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ethical-hacking-methodology | 168 | Penetration-testing methodology playbook covering the assessment lifecycle, reconnaissance, scanning, and report writing. |
| pentest-checklist | 165 | A structured checklist and methodology for planning and scoping a penetration-testing engagement. |
| wordpress-penetration-testing | 161 | WordPress security assessment playbook covering vulnerability scanning and enumeration. |
| pentest-commands | 151 | A command reference for penetration-testing tools such as nmap, hydra, john, and nikto. |
| sql-injection-testing | 150 | SQL injection testing playbook covering detection and exploitation across database systems. |
| metasploit-framework | 139 | Guidance for using the Metasploit Framework in security assessments. |
| active-directory-attacks | 132 | Windows domain penetration-testing playbook covering Active Directory assessment techniques. |
| cloud-penetration-testing | 130 | Cloud security assessment playbook covering Azure, AWS, and GCP. |
| ssh-penetration-testing | 127 | SSH service security assessment methodology. |
| network-101 | 125 | Configuring and testing network services for penetration-testing lab environments. |
| smtp-penetration-testing | 124 | SMTP mail-server security testing methodology. |
| aws-penetration-testing | 123 | Amazon Web Services security assessment playbook covering IAM, S3, and Lambda. |
| linux-privilege-escalation | 122 | Linux privilege-escalation assessment playbook covering enumeration and elevation paths. |
| html-injection-testing | 121 | HTML injection testing playbook covering detection and remediation guidance. |

The remaining 73 indexed listings range from 37 to 119 installs. Below this table the listings shift to general developer skills such as React, Next.js, TypeScript, and Playwright, along with the remainder of the security playbook set.

## Why This Matters for Hermes Agents

For builders, this repo is two different resources under one name, and it pays to treat them separately. The written guide is one of the more complete community references for Claude Code itself, useful when wiring up an agent to configuration, MCP servers, sub-agents, or hooks, and the bundled developer skills are plain SKILL.md files any harness that loads skills can use.

The security listings are a different proposition. They are playbooks, not configuration references, and they are aimed at authorised penetration testing and lab work rather than day-to-day development. The skills.sh sample reflects that split: two of the twelve sampled skills fail a verdict and eleven of the twelve carry at least one Warn.

Anyone installing this set should pull the guide and the developer skills deliberately, and keep the offensive playbooks isolated and used only under a written testing scope.

## Usage

| You say | What happens |
|---|---|
| "Set up Claude Code from scratch" | The guide walks through installation, auth, and configuration in order. |
| "Fix a permissions error in Claude Code" | The troubleshooting section covers permission issues and settings precedence. |
| "Generate a Playwright test suite" | The playwright skill provides test authoring and CI guidance. |
| "Plan a penetration test engagement" | pentest-checklist returns a scoped methodology and checklist for the assessment. |
| "Review this diff for security issues" | The security-reviewer sub-agent or the security best-practices section applies. |
| "Add an MCP server to my setup" | The guide's MCP section covers adding, auth, and troubleshooting servers. |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/zebbern/claude-code-guide/main/skills/network-101/SKILL.md
```

Then clone and copy the skills you need:

```bash
git clone --depth 1 https://github.com/zebbern/claude-code-guide.git
```

After install, ask your agent to explain a Claude Code flag or plan an assessment and check the next response changes.

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ethical-hacking-methodology | Fail | Warn | Pass |
| pentest-checklist | Pass | Warn | Pass |
| wordpress-penetration-testing | Warn | Warn | Warn |
| pentest-commands | Pass | Warn | Pass |
| sql-injection-testing | Pass | Warn | Pass |
| metasploit-framework | Pass | Warn | Warn |
| active-directory-attacks | Warn | Warn | Pass |
| cloud-penetration-testing | Pass | Warn | Pass |
| ssh-penetration-testing | Warn | Warn | Pass |
| network-101 | Pass | Warn | Pass |
| smtp-penetration-testing | Pass | Warn | Pass |
| aws-penetration-testing | Warn | Fail | Warn |

The sample covers 12 of the 87 indexed listings; two fail (ethical-hacking-methodology and aws-penetration-testing) and all twelve carry at least one Warn.

## Limitations

- Snapshot data, verified Nov 18, 2026: 6,009 combined installs across 87 indexed listings; 4,716 GitHub stars; MIT licence; last pushed 2026-11-18. Counts drift over time.
- The 14 skills shown above are all offensive-security playbooks; the everyday developer skills sit lower in the install band, between 37 and 119 installs.
- The written guide targets Claude Code specifically, so the install, auth, and command material does not transfer one-to-one to other agents.
- The penetration-testing playbooks are for authorised testing only and should be isolated from general development use.
- The repo mixes a guide, skills, and sub-agents, so a naive install of everything pulls the full offensive set along with the reference material.

## Related

- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)
- [Claude Code Extensions - Agents, Skills & Hooks Setup](/hermes/skills/catalog/nodnarbnitram-claude-code-extensions-setup)
- [Daymade Claude Code Skills - General-Purpose Suite Setup](/hermes/skills/catalog/daymade-claude-code-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read the written guide in the README before touching the skills; the setup, config, and troubleshooting sections answer most questions.
- Pull the developer skills and the guide deliberately, and leave the offensive playbooks out of your default install.
- The commands and provider model mappings change quickly; treat the official Claude Code docs as authoritative.
- Use the sub-agent definitions as templates for your own reviewer, debugger, or architect agents.
- Treat the pentest playbooks as scoped reference for authorised assessments, never as day-to-day tooling.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
