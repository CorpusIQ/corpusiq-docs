---
title: "CTF Security Skills — Offensive Security Suite Setup"
description: "ljagiello/ctf-skills — 12 skills, 71.6K installs: reverse engineering, web exploitation, OSINT, forensics, cryptography, and AI/ML challenge skills for security work."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ctf-security-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "security", "ctf", "osint"]
---

# CTF Security Skills — Setup Guide

**Source:** [ljagiello/ctf-skills](https://skills.sh/ljagiello/ctf-skills)
**GitHub:** [ljagiello/ctf-skills](https://github.com/ljagiello/ctf-skills)
**Skills:** 12 skills · 71.6K total installs
**Category:** Security / CTF
**First Seen:** catalogued August 15, 2026 evening sweep
**Quality Tier:** 🟡 Trusted (individual publisher, offensive-security content — use for authorized testing and CTF practice only)

A full offensive-security curriculum as agent skills: reverse engineering, web exploitation, binary exploitation (pwn), OSINT, cryptography, forensics, malware analysis, AI/ML challenge work, and writeup generation. Queued in prior sweeps; the publisher page confirms 71.6K installs across 12 skills — the largest security-focused cluster catalogued to date.

---

## Installation

```bash
npx skills add ljagiello/ctf-skills
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Security toolchain** | Ghidra, GDB, Burp Suite, and similar for the respective skills |
| **Authorization** | Explicit permission for any target you test against |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| ctf-reverse | 7.4K | Binary and code reverse engineering |
| ctf-web | 7.1K | Web application exploitation |
| ctf-pwn | 6.9K | Binary exploitation |
| ctf-osint | 6.7K | Open-source intelligence gathering |
| ctf-crypto | 6.7K | Cryptographic challenges |
| ctf-forensics | 6.6K | Digital forensics |
| solve-challenge | 6.5K | End-to-end challenge solving |
| ctf-misc | 6.4K | Miscellaneous challenge techniques |
| ctf-malware | 6.3K | Malware analysis |
| ctf-writeup | 5.5K | Writeup and documentation generation |
| ctf-ai-ml | 5.4K | AI/ML security challenges |
| find-skills | 7 | Skill discovery helper |

## Quick Start

1. Install: `npx skills add ljagiello/ctf-skills`
2. Start with `solve-challenge` for the general workflow, then load category-specific skills
3. Ask: "analyze this binary and produce a writeup of the vulnerability"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Security posture work** | ctf-web and ctf-reverse as structured checklists for our own penetration passes |
| **OSINT workflows** | ctf-osint as a methodology reference for competitive and market research |
| **Security content** | Writeup patterns for security-focused documentation |
| **Agent capability** | A reference for what an agent can do in a security analyst role |

## Limitations / Verification

- Publisher-page install counts verified; individual skill audit pages were not fetched for this multi-skill suite
- Offensive techniques — only use against systems you own or are explicitly authorized to test
- Skills assume CTF-style targets; adapting to production systems requires additional judgment

```bash
npx skills add ljagiello/ctf-skills   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
