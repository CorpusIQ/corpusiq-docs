---
title: "OSINT Skills — 57-Skill Open-Source Intelligence Suite"
description: "useosint/osint-skills — 57 skills, 285.8K combined installs. Photo verification, deepfake detection, corporate X-rays, data-broker digging, domain recon, and intel brief writing for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/osint-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-13"
tags: ["hermes skill", "agent skill", "skill setup", "osint"]
---

# OSINT Skills — Setup Guide

**Source:** [skills.sh](https://www.skills.sh/useosint/osint-skills) (285.8K combined installs)
**GitHub:** [useosint/osint-skills](https://github.com/useosint/osint-skills)
**Category:** Open-Source Intelligence
**First Seen:** August 13, 2026 sweep
**Quality Tier:** 🟢 Production (verification) / 🟡 Beta (advanced techniques)

The largest OSINT skill cluster on skills.sh — 57 skills covering the full investigation lifecycle. Flagships center on media verification (is this photo real, find the original image) and safe investigation practice (investigate without getting made, what leaked about you). The long tail adds domain recon, people search, breach analysis, geolocation, and intel-brief writing. Directly useful for brand protection, competitor research, and due diligence.

---

## Installation

```bash
npx skills add useosint/osint-skills
```

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| is-this-photo-real | 58.0K | Detecting AI-generated or manipulated images |
| investigate-without-getting-made | 58.0K | OPSEC-safe investigation methodology |
| what-leaked-about-you | 57.6K | Personal data-exposure audits |
| find-the-original-image | 56.3K | Reverse image provenance tracing |
| x-ray-a-company | 1.8K | Corporate structure and exposure mapping |
| read-deleted-pages | 1.8K | Wayback/archive recovery of removed content |
| find-exposed-servers / find-hidden-subdomains / recon-a-domain-passively / who-owns-this-domain | 1.6–1.8K | Domain and infrastructure reconnaissance |
| secrets-in-git-history / secrets-in-file-metadata | 1.6–1.7K | Credential and metadata leak hunting |
| dig-through-data-brokers / find-anyone / whose-number-is-this | 1.6–1.7K | People and data-broker research |
| follow-the-crypto | 1.6K | Blockchain transaction tracing |
| geolocate-from-pixels / where-was-this-taken / track-planes-and-ships | 1.6K | GEOINT: photos, flights, vessels |
| hunt-a-handle / pattern-of-life-from-socials / what-an-email-reveals | 1.6K | Identity and social-graph analysis |
| write-the-intel-brief / investigate-anything / google-like-a-spy | 1.5–1.6K | Synthesis and search technique |
| (31 more) | ~600 each | Breach data, registries, wayback, Shodan, dorking, link analysis |

## Prerequisites

- No API keys for most skills; some advanced workflows benefit from Shodan/VPN access
- Operate within legal boundaries — these are investigative patterns, not intrusion tools

## CorpusIQ Use Cases

- **Competitor intelligence** — `x-ray-a-company` + `recon-a-domain-passively` feed the competitive-intelligence brief workflow
- **Brand protection** — `find-leaks-in-the-wild`, `find-exposed-servers`, and `secrets-in-git-history` as periodic risk scans for corpusiq.io
- **Lead verification** — `who-really-owns-it` and `whose-number-is-this` validate inbound leads before outreach spend
- **Content verification** — `is-this-photo-real` as a gate for UGC-sourced claims in daily reports

## Limitations / Verification

- Flagship verification skills are procedural (technique-based), not automated detectors — they guide an agent through manual checks
- Verify by running `is-this-photo-real` workflow on a known AI image and confirming the workflow flags it

## Related

- [Solana Dev Skill — Blockchain Development Setup](/hermes/skills/catalog/solana-dev-skill-setup/)
- [SquirrelScan Skills — Website Audit Setup](/hermes/skills/catalog/squirrelscan-skills-setup/)
