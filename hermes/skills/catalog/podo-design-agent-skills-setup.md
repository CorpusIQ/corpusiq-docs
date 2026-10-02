---
title: "Podo Design Agent Skills - 151-Skill Design Catalog Setup"
description: "Setup guide for podo/design-agent-skills - a curated design-skill catalog with one install command and profile-based selection (24/92/151 skills). 150 skills indexed on skills.sh, 17.3K combined installs, 149 at 100+. Covers UI craft, motion, Figma, accessibility, data viz, presentations, user research. Agent-agnostic symlink install across 30+ agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/podo-design-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-15"
tags: ["hermes skill", "agent skill", "skill setup", "design", "ui", "figma"]
---

# Podo Design Agent Skills - Setup Guide

**Source:** [podo/design-agent-skills](https://github.com/podo/design-agent-skills) (8⭐, MIT, created May 2026, pushed Aug 31, 2026)
**Skill:** `podo/design-agent-skills` (157 skills in repo; 150 indexed on skills.sh)
**Combined Installs:** 17,302 across indexed skills (Sep 15, 2026); 149 skills at 100+
**Category:** Design / UI Craft
**Quality Tier:** 🟡 Unverified (no skills.sh Trust Hub / Socket / Snyk verdicts published - verified Sep 15, 2026)

A curated design-skill catalog with a single entry point. Instead of installing design skills one publisher at a time, `npx skills add podo/design-agent-skills` gives agents a profile-based picker (Picks / Essentials / All) over a 151-skill library spanning UI craft, motion, Figma workflows, accessibility, data viz, presentations, PM tools, content design, and user research. Install is agent-agnostic: the interactive CLI auto-detects 30+ installed agents (vercel-labs/skills mechanism) and symlinks one canonical skill store into every agent directory.

**Redistribution disclosure:** most skills in the catalog are repackaged from upstream publishers - emilkowalski (design philosophy), anthropics (frontend design), figma-official, vercel, sleek (mobile app design), nexu-io/open-design (design-review), mastepanoski, addyosmani (quality patterns), and others. Podo curates and redistributes; upstream repos remain canonical. Treat this as a convenience layer, not the origin.

---

## Installation

```bash
# Interactive picker (arrow-key navigation, no flags) - verified live Sep 15: "Found 157 skills"
npx design-agent-skills

# Direct profile installs
npx skills add podo/design-agent-skills --picks -g       # 24 best-in-class skills
npx skills add podo/design-agent-skills --essentials -g  # ~92 skills, full coverage
npx skills add podo/design-agent-skills --all -g         # all 151 (default when no flag)

# Install the catalog entry point for browsing/selective use
npx skills add podo/design-agent-skills
```

## Prerequisites

| Requirement | Details |
|---|---|
| Node.js 18+ | `npx skills` / `npx design-agent-skills` requirement |
| Per-skill tooling | figma-official-skills needs a Figma account + Figma MCP; slidev-skill needs Slidev; gsap/framer-motion skills need those libraries |
| No API keys | Most skills are reference/playbook skills - no keys required |

## Roster - Selected 100+ Install Skills

| Skill | Installs | Domain |
|---|---|---|
| distinctive-frontend | 434 | Distinctive frontend design |
| taste-skill | 163 | Design taste calibration |
| color-expert / emilkowalski-skill | 146 / 146 | Color systems; Emil Kowalski design philosophy |
| ui-ux-pro-max | 145 | UI/UX patterns |
| apple-hig-skills | 143 | Apple Human Interface Guidelines |
| anthropics-skills | 141 | Anthropic frontend design |
| ux-writing-skill | 140 | UX copy |
| interaction-design | 139 | Interaction patterns |
| gsap-skills / framer-motion-skills | 139 / 136 | Animation libraries |
| excalidraw-diagram | 137 | Diagramming |
| shadcn-ui | 136 | shadcn/ui components |
| email-html-mjml | 135 | Email HTML/MJML |
| deanpeters-pm-skills | 135 | PM workflows |
| antvis-chart-skills | 134 | Data viz (AntV) |
| figma-official-skills | 134 | Figma workflows |
| material-3-skill | 132 | Material 3 |
| fixing-accessibility / wcag-ai-skill | 131 / 125 | Accessibility |
| remotion | 131 | Remotion video |
| impeccable | 131 | Design polish |
| user-research-cookiy | 129 | User research |
| textual-tui-skill / tui-design-skill | 128 / 111 | Terminal UI design |
| slidev-skill | 128 | Presentation decks |
| awesome-design-skills | 128 | Curated design references |
| copywriting-skill | 120 | Copywriting |
| mobile-app-design / mobile-app-ui-design | 120 / 119 | Mobile design |
| bencium-ux-designer | 119 | UX process |
| design-review-garrytan | 118 | Design review (repackaged nexu-io/open-design) |
| animate-skill / motion-catalogue / css-animation-skill | 118 / 118 / 113 | Motion |
| brand-design-md | 118 | Brand design |
| sleek-design-mobile-apps | 117 | Sleek mobile design (repackaged) |
| addyosmani-quality | 115 | Quality patterns |
| cloudflare-web-perf | 115 | Web performance |
| dark-pattern-audit | 114 | Ethics / dark-pattern audit |
| vercel-skills | 113 | Vercel skills (repackaged) |
| p5js-hermes | 112 | p5.js creative coding (Hermes-named) |
| ...and 100+ more | 100-163 | Design tokens, sprints, briefs, governance, PM, research |

Full inventory: 150 skills indexed (Sep 15, 2026 snapshot), 149 at 100+ installs, 17,302 combined.

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **UI template change requests** | ui-ux-pro-max + taste-skill for internal screenshot-based template changes |
| **Docs & marketing design** | email-html-mjml for campaign emails; slidev-skill for investor/partner decks |
| **Accessibility pass** | fixing-accessibility + wcag-ai-skill alongside the AccessLint suite |
| **Animation/motion quality** | gsap-skills + framer-motion-skills for docs interactive elements and product motion |
| **Data viz for reports** | antvis-chart-skills for analytics and recap visuals |

## Limitations / Verification

- Redistribution catalog: upstream repos are canonical; verify against the upstream for critical deliverables
- 8⭐ repo, no skills.sh security audits published - review skills before relying on them for production work
- Verify: `npx skills add podo/design-agent-skills --list` shows "Found 157 skills"

## Security

No skills.sh security audits published (verified Sep 15, 2026 - the publisher page renders no audit verdicts). Treat as unverified until reviewed:

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [AccessLint Skills - WCAG 2.2 Accessibility Audit Suite Setup](/hermes/skills/catalog/accesslint-skills-setup)
- [Sleek Design Mobile Apps - AI Mobile App Design Skill Setup](/hermes/skills/catalog/sleek-design-mobile-apps-setup)
- [Hallmark - Anti-AI-Slop Design Skill Setup](/hermes/skills/catalog/hallmark-setup)
- [Meng To Skills - Frontend & Motion Design Suite Setup](/hermes/skills/catalog/mengto-skills-setup)
- [Tech Logos - Brand Logo Installer for shadcn/ui Setup](/hermes/skills/catalog/tech-logos-setup)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
