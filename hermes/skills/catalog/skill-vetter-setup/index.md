---
title: Skill Vetter — Setup Guide for Hermes Agents
description: Security-first pre-install vetting for OpenClaw skills. Structured red-flag checklist covering permissions, patterns, and suspicious instructions. 20.6K+ installs with 97% trust score.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/skill-vetter-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Skill Vetter — Setup Guide

**Source:** [useai-pro/openclaw-skills-security](https://github.com/useai-pro/openclaw-skills-security) (Community)
**Skill:** `skill-vetter` · **Installs:** 20.6K+ · **Category:** Security
**Platform:** Linux, macOS, Windows

Skill Vetter is a security-first pre-install audit tool for OpenClaw skills. Before installing any skill from ClawHub, GitHub, or other sources, it runs a structured red-flag checklist covering permissions requested, suspicious instruction patterns, file access scope, and network/shell access requirements. With a 97% trust score and last audited February 2026.

## Installation

```bash
npx skills add useai-pro/openclaw-skills-security@skill-vetter
```

## Prerequisites

| Requirement | Details |
|-------------|---------|
| OpenClaw or Hermes Agent | Skill execution environment |
| Skill to vet | A SKILL.md from ClawHub, GitHub, or shared source |

## When to Use

- Before installing a new skill from ClawHub
- When reviewing a SKILL.md from GitHub or other sources
- When someone shares a skill file and you need to assess safety
- Before integrating community skills into production workflows

## Vetting Checklist

The skill audits against these red-flag categories:

| Category | What It Checks |
|----------|---------------|
| **File Access** | Does the skill read/write files? Which directories? |
| **Network Access** | Does it make outbound requests? To which domains? |
| **Shell Access** | Does it execute shell commands? With what privileges? |
| **Permission Scope** | What `allowed-tools` are declared? Are they over-broad? |
| **Suspicious Patterns** | Obfuscated code, encoded payloads, eval/exec usage |
| **Data Exfiltration** | Does it send data off-machine? To where? |
| **Dependency Risk** | External package installs, version pinning, supply chain |

## Output

Produces a conservative manual review with:

- **Trust Score** — overall safety assessment
- **Red Flags** — specific concerns with line references
- **Permission Summary** — what the skill can access
- **Recommendation** — Install, Review Further, or Block

## Trust Score: 97/100

The skill itself has been audited:
- **Author**: useclawpro
- **Category**: Security
- **File Read**: Yes (required for auditing)
- **File Write**: No
- **Network**: No
- **Shell**: No
- **Last Audited**: February 2026

## Verification

After vetting a skill:
- Review the red-flag report before installing
- Cross-reference permissions against the skill's stated purpose
- For production, require second reviewer for any skill with shell or network access

## Related Skills

- [OpenClaw Ecosystem (June 26)](/hermes/skills/catalog/openclaw-ecosystem-june26-setup/)
- [Clawd Strike Setup](/hermes/skills/catalog/clawdstrike-setup/)
