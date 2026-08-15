---
title: Trail of Bits Skills Curated — Agent Security Suite Setup
description: "trailofbits/skills-curated — 31 skills, 2.4K installs: security research firm Trail of Bits curates Ghidra reverse engineering, ffuf web fuzzing, threat modeling, security review tooling, and OpenAI-branded agent skills (Playwright, PDF, deploy, CI)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/trailofbits-skills-curated-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "security", "reverse engineering", "fuzzing", "threat modeling"]
---

# Trail of Bits Skills Curated — Setup Guide

**Source:** [trailofbits/skills-curated](https://skills.sh/trailofbits/skills-curated)
**GitHub:** [trailofbits/skills-curated](https://github.com/trailofbits/skills-curated)
**Skills:** 31 skills · 2.4K total installs
**Category:** Security & Agent Workflow
**First Seen:** catalogued August 15, 2026 midday sweep (hot leaderboard #1 this hour)
**Quality Tier:** 🟡 Trusted (curated by Trail of Bits, a leading security research firm; install counts modest — ghidra-headless leads at 312)

Trail of Bits curates a security-and-workflow skill collection: reverse engineering with Ghidra, web fuzzing with ffuf, threat modeling and security review tooling, plus a set of OpenAI-branded agent skills covering PDFs, Playwright, spreadsheets, screenshots, deploys, CI fixes, and Sentry. It also includes agent workflow skills — planning-with-files, handoff, skill-extractor, and humanizer — that are directly relevant to agent operating discipline.

---

## Installation

```bash
npx skills add trailofbits/skills-curated
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Ghidra / ffuf** | For the reverse-engineering and fuzzing skills |
| **OpenAI API access** | For the OpenAI-branded skills |

## What It Provides (highlights)

| Area | Representative skills (installs) |
|---|---|
| Reverse engineering | ghidra-headless (312) |
| Web fuzzing | ffuf-web-fuzzing (80) |
| Security review | openai-security-threat-model (80), scv-scan (79), openai-security-best-practices (78), openai-security-ownership-map (66) |
| Security awareness | security-awareness (106), wooyun-legacy (89) |
| Agent workflow | humanizer (143), planning-with-files (117), skill-extractor (102), handoff (11), writing-great-skills (11), teach (11), grilling (13) |
| OpenAI-branded tools | openai-playwright (67), openai-pdf (67), openai-spreadsheet (73), openai-screenshot (70), openai-cloudflare-deploy (62), openai-netlify-deploy (61), openai-sentry (60), openai-gh-fix-ci (63), openai-gh-address-comments (63), openai-doc (63), openai-jupyter-notebook (63), openai-yeet (62) |
| Research | x-research (66), last30days (88) |

## Quick Start

1. Install: `npx skills add trailofbits/skills-curated`
2. Load planning-with-files and handoff for agent discipline, or the security-review skills for audits
3. Ask: "run a threat-model pass on this design using the security review skills"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Agent security posture** | Threat modeling and security best practices from a top research firm |
| **Workflow discipline** | planning-with-files and handoff mirror our session handoff doctrine |
| **Prose de-slop** | humanizer overlaps our de-AI-fication rules for public content |
| **Security tooling reference** | Ghidra and ffuf skill packaging for security audits |

## Limitations / Verification

- Install counts are modest (2.4K total; top skill 312) — brand authority, not volume, is the signal
- Multi-skill suite; individual security-audit pages not fetched this sweep
- OpenAI-branded skills assume OpenAI API access

```bash
npx skills add trailofbits/skills-curated   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
