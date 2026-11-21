---
title: "Droid Tings - Agent Skills and Droids Setup Guide"
description: "ovachiever/droid-tings: Agent Skills and custom Droids for Factory Droid and Claude Code - 8.4K combined installs across 96 listings."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ovachiever-droid-tings-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "security", "nextjs", "cloudflare"]
---

# Droid Tings - Agent Skills and Droids Setup Guide

**Source:** [ovachiever/droid-tings](https://www.skills.sh/ovachiever/droid-tings) via skills.sh - 8.4K combined installs across 96 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 evening sweep)
**GitHub:** [ovachiever/droid-tings](https://github.com/ovachiever/droid-tings) - 56 stars, master branch, last pushed Nov 25, 2025; skills under `skills/<name>/SKILL.md`, custom droids under `droids/`, and two workflow commands under `commands/`; GitHub metadata reports NOASSERTION while the README declares MIT.
**Category:** Agent Skills and Droids Collection
**Quality Tier:** 🟠 Orange - sampled skills.sh verdicts carry one Snyk Fail (secret-scanner) alongside several Pass cells; treat as community code pending your own review.

`droid-tings` is a broad, curated collection from ovachiever that bundles Agent Skills in the Factory SKILL.md format with custom Droids for Factory's Droid system and Claude AI. The README counts 375 skills and 155 custom droids plus two workflow commands, aggregated from 15+ upstream repositories alongside original and personal work. It spans security, Next.js and React, Cloudflare, scientific writing, and data tooling.

The repository ships skills under `skills/<name>/SKILL.md`, droids under `droids/`, and commands under `commands/`, installed by copying into Factory's `.factory/` directories rather than through an agent-plugin installer. skills.sh indexes 96 of the collection's listings at 8,362 combined installs.

## Installation

```bash
git clone https://github.com/ovachiever/droid-tings.git
cd droid-tings
```

Copy the skills, droids and commands into Factory's directories. Use the project path for one repo or the home path for personal use across all projects.

```bash
# skills: project-specific, or personal for use across all projects
cp -r skills/* .factory/skills/
cp -r skills/* ~/.factory/skills/

# custom droids
cp droids/* .factory/droids/      # or ~/.factory/droids/

# workflow commands
cp commands/* .factory/commands/  # or ~/.factory/commands/
```

Restart the Droid and Factory auto-detects the new skills, droids and commands. These steps follow the repository's own Quick Start; the collection targets Factory's Droid system, so it does not use the Agent Skills `npx skills add` installer.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| security-auditor | 784 | continuous OWASP Top 10 and vulnerability scanning for SQL injection, XSS, secrets and auth issues |
| react-hook-form-zod | 725 | type-safe React forms with React Hook Form and Zod, one schema shared by client and server |
| deep-reading-analyst | 287 | deep analysis of articles and papers through 10+ thinking models such as SCQA, 5W2H and first principles |
| nextjs-shadcn-builder | 263 | build Next.js apps or migrate React, Vue and Angular frontends to Next.js plus shadcn/ui |
| reportlab | 141 | PDF generation for invoices, reports, charts, tables and barcodes via Platypus and Canvas |
| cloudflare-r2 | 132 | S3-compatible R2 object storage for uploads, CORS, presigned URLs and multipart uploads |
| scientific-schematics | 131 | publication-quality scientific diagrams through AI generation with iterative refinement |
| tailwind-v4-shadcn | 129 | Tailwind v4 with shadcn/ui using CSS variable architecture and automatic dark mode |
| threejs-graphics-optimizer | 125 | THREE.js performance rules for smooth 60fps rendering across devices |
| react-native-expo | 105 | React Native 0.76+ apps with Expo SDK 52, New Architecture and React 19 changes |

Playwright Browser Automation (227 installs) also tops 100 installs, but its display name contains spaces so it is listed here in prose rather than in the table above. The remaining 84 indexed listings range from 54 to 99 installs.

## Why This Matters for Hermes Agents

The collection front-loads the skills an agent most often needs to ship real work: security-auditor and secret-scanner catch OWASP Top 10 classes and leaked credentials before they reach a commit or a deployment, which is the failure an agent is worst at self-correcting. react-hook-form-zod and nextjs-shadcn-builder replace ad-hoc React with type-safe, shadcn-aligned patterns, so generated UI reads as deliberate rather than templated. The Cloudflare skills cover a wide slice of the Workers and edge surface, from R2 storage to Workers AI and Turnstile. The scientific set spans writing, schematics, slides and database lookups, useful when an agent must produce publication-grade output. Because the tree ships 375 skill directories while skills.sh indexes only 96, most of the collection is reachable only by cloning the repository rather than through the marketplace page. Finally, the README carries an explicit as-is warning, so treat it as community code and review each skill before production use.

## Usage

| You say | What happens |
|---|---|
| Review this PR for OWASP Top 10 issues and exposed secrets | security-auditor and secret-scanner scan for SQL injection, XSS, secrets and auth issues before commit |
| Build a type-safe form with React Hook Form and Zod validation | react-hook-form-zod generates a validated form with one schema shared by client and server |
| Migrate my React frontend to Next.js with shadcn/ui | nextjs-shadcn-builder analyzes the codebase and converts it to Next.js plus shadcn/ui with CSS variable theming |
| Generate a publication-ready PDF report with charts and tables | reportlab produces invoices, reports, charts, tables and barcodes via Platypus and Canvas |
| Store and serve files from Cloudflare R2 | cloudflare-r2 handles uploads, CORS, presigned URLs and multipart uploads |
| Create a scientific diagram for a neural network paper | scientific-schematics generates a publication-quality figure with iterative refinement |
| Set up Tailwind v4 with shadcn/ui and automatic dark mode | tailwind-v4-shadcn applies the CSS variable architecture with the @theme inline pattern |

## Verification

```bash
# after install, confirm the skills landed in the Factory skills directory
ls .factory/skills/
# review one skill before relying on it
curl -sL https://raw.githubusercontent.com/ovachiever/droid-tings/master/skills/security-auditor/SKILL.md
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200. Canonical skills live under `skills/<name>/SKILL.md` on the master branch; droids live under `droids/` and the two workflow commands under `commands/`.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| security-auditor | Pass | Pass | Pass |
| react-hook-form-zod | Pass | Pass | Pass |
| deep-reading-analyst | Pass | Pass | Warn |
| nextjs-shadcn-builder | Pass | Pass | Pass |
| Playwright Browser Automation | not parsed | not parsed | not parsed |
| reportlab | Pass | Pass | Pass |
| cloudflare-r2 | Pass | Pass | Pass |
| scientific-schematics | Pass | Pass | Pass |
| tailwind-v4-shadcn | Pass | Pass | Pass |
| threejs-graphics-optimizer | Pass | Pass | Pass |
| react-native-expo | Pass | Pass | Pass |
| readme-updater | Pass | Pass | Pass |
| scholar-evaluation | Pass | Pass | Pass |
| csv-data-summarizer | Pass | Pass | Warn |
| dependency-auditor | Pass | Pass | Warn |
| fastmcp | Pass | Pass | Pass |
| markitdown | Pass | Pass | Pass |
| zustand-state-management | Pass | Pass | Pass |
| secret-scanner | Pass | Pass | Fail |
| rag-implementation | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 20, 2026: 8,362 combined installs across 96 indexed listings; 56 GitHub stars; no standard license declared (GitHub metadata NOASSERTION); last pushed Nov 25, 2025. Counts drift over time.
- The repository has no standard permissive license recognized by GitHub (metadata NOASSERTION). The README declares MIT for the collection and the tree carries a LICENSE file, but the collection aggregates skills from 15+ upstream repositories and individual skills may carry their own licenses, so review each skill before reuse or redistribution.
- The skills.sh index covers only 96 of the roughly 375 skill directories in the tree, and some indexed listing names do not map one to one with tree directories (for example Playwright Browser Automation resolves to skills/playwright-skill and Gemini CLI to skills/gemini-cli), so the install index is a partial view of the collection.
- Security verdicts are sampled: only 20 of the 96 listings carry skills.sh verdict cells, and one of those, secret-scanner, carries a Snyk Fail. Re-check the security pages on skills.sh before production use.
- The README documents a Factory Droid installation by copying into `.factory/` directories, not an Agent Skills package manager, so the setup steps here follow the repository's own Quick Start.

## Related

- [Security and Hardening - Agent Security Setup](/hermes/skills/catalog/security-and-hardening-setup)
- [Next.js Agent Skills - App Router Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [Cloudflare Skills - Workers and Edge Setup](/hermes/skills/catalog/cloudflare-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Review security-auditor and secret-scanner output before committing; the secret-scanner skill itself carries a Snyk Fail in the skills.sh sample, so re-check its security page before trusting it.
- Install only the skill directories you need rather than copying the whole tree, since the collection bundles 375 skills from 15+ upstream sources with mixed licenses.
- Keep the repository on the master branch and re-clone to update; there is no package manager, so updates are manual.
- Use `.factory/skills/` for team-shared skills and `~/.factory/skills/` for personal ones.
- Treat the skills.sh page as a partial index: clone the repository to browse the full collection.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
