---
title: Skill Vetter - Setup Guide for Hermes Agents
description: Security-first pre-install vetting for OpenClaw skills. Structured red-flag checklist covering permissions, patterns, and suspicious instructions. 20.6K+ installs with 97% trust score.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/skill-vetter-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Skill Vetter - Setup Guide

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

- **Trust Score** - overall safety assessment
- **Red Flags** - specific concerns with line references
- **Permission Summary** - what the skill can access
- **Recommendation** - Install, Review Further, or Block

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

## Vetting Protocol

The skill works through four stages and ends with one of three recommendations.

### Step 1: Metadata Check

- Verify `name` matches the expected skill name (no typosquatting)
- Check `version` follows semver
- Confirm `description` is clear and matches what the skill does
- Ensure `author` is identifiable (not anonymous)

### Step 2: Permission Scope Analysis

| Permission | Risk Level | Justification Required |
|---|---|---|
| `fileRead` | Low | Almost always legitimate |
| `fileWrite` | Medium | Must justify what files and why |
| `network` | Medium-High | Must specify endpoints and data sent |
| `shell` | High | Requires strong justification and sandboxing |

### Step 3: Pattern Analysis

- Command injection vectors (`eval`, `exec`, system calls)
- Obfuscated code or base64-encoded payloads
- Hardcoded URLs or IPs (potential data exfiltration)
- Excessive permission requests relative to stated functionality

### Step 4: Recommendation

- **INSTALL** - no red flags, permissions justified
- **REVIEW** - minor concerns, install with monitoring
- **BLOCK** - critical red flags, do not install

## Manual Vetting

When reviewing a skill by hand, apply the same checks in order:

1. Read the SKILL.md frontmatter - verify `name`, `version`, `description`, `author`
2. Check the `allowed-tools` or `permissions` section - assess risk level per tool
3. Scan for suspicious patterns: `eval()`, `exec()`, base64 strings, hardcoded URLs
4. Compare stated functionality against requested permissions - they should align
5. Document the decision: INSTALL / REVIEW / BLOCK with justification

## Hermes Integration

For CorpusIQ Hermes agents, put skill-vetter into the governance pipeline:

1. **Pre-install gate**: run vetting before any `npx skills add` command
2. **Weekly re-audit**: re-vet all installed skills every Sunday
3. **Audit log**: write vetting results to `~/.hermes/profiles/<your-profile>/skill-audits/YYYY-MM-DD.md`
4. **Block escalation**: BLOCK results go to the ops email digest (media@) immediately

## Troubleshooting

| Issue | Solution |
|---|---|
| Unknown skill format | Ensure the skill has a SKILL.md with proper frontmatter |
| Missing author info | Flag as REVIEW - anonymous skills require extra scrutiny |
| Permission mismatch | If a skill requests `shell` but only needs `fileRead`, flag as BLOCK |

## Related Skills

- [OpenClaw Ecosystem (June 26)](/hermes/skills/catalog/openclaw-ecosystem-june26-setup)
- [Clawd Strike Setup](/hermes/skills/catalog/clawdstrike-setup)
