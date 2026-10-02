---
title: "Harmony Next Skills - HarmonyOS NEXT Dev Library Setup"
description: "Setup guide for linhay/harmony-next.skills - offline HarmonyOS NEXT dev library for AI coding assistants: ArkTS/ArkUI, API 12-26, DevEco. 320 installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/harmony-next-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-30"
tags: ["hermes skill", "agent skill", "skill setup", "harmonyos", "mobile development", "arkts"]
---

# Harmony Next Skills - Setup Guide

**Source:** [linhay/harmony-next.skills](https://github.com/linhay/harmony-next.skills) (357⭐, no LICENSE file, master branch)
**Skill:** `linhay/harmony-next.skills` (1 installable skill, 320 installs)
**Publisher:** linhay
**Category:** Mobile Development / HarmonyOS
**Quality Tier:** 🔵 Community (good-faith publisher, no LICENSE file, verified Sep 30, 2026)

One indexed skill, harmony-next, that ships as a full offline knowledge library for HarmonyOS NEXT development, covering API 12 through 26 declarations, ArkTS and ArkUI, the NDK, DevEco Studio, emulator automation, and device management. The repository targets Gemini CLI, Claude Code, Codex, and other AI coding assistants, and any host that reads SKILL.md directories, including Hermes Agent, can use it. The README is Chinese first with an English README_en.md available.

---

## Installation

```bash
# The indexed skill
npx skills add linhay/harmony-next.skills

# Or clone the full offline knowledge library
git clone https://github.com/linhay/harmony-next.skills
```

Verify the catalog with `npx skills add linhay/harmony-next.skills --list` (1 skill).

## Roster

| Skill | Installs | Does |
|---|---|---|
| harmony-next | 320 | Offline HarmonyOS NEXT development reference: API 12-26 declarations, ArkTS/ArkUI, NDK, DevEco Studio, emulator automation, device management |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Offline API reference** | API 12-26 declarations answer HarmonyOS app questions without network lookups |
| **ArkTS/ArkUI review** | Check ArkTS and ArkUI syntax against the bundled declarations during mobile work |
| **DevEco tooling** | Emulator automation and device management guidance for DevEco Studio workflows |

## Limitations / Verification

- No LICENSE file in the repository; default copyright applies, so reuse beyond personal use needs author permission
- README is Chinese first; English speakers should read README_en.md
- Only one skill is indexed on skills.sh; the library value sits in the bundled reference files rather than the skill wrapper
- Verify: `npx skills add linhay/harmony-next.skills --list` shows 1 skill

## Security

No LICENSE file in the repository (verified Sep 30, 2026); default copyright applies, so treat the content as all rights reserved unless the author grants permission. No skills.sh security audits published (verified Sep 30, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [React Native Update Skill - Setup Guide](/hermes/skills/catalog/react-native-update-skill-setup)
- [Sleek Design Mobile Apps - Setup Guide](/hermes/skills/catalog/sleek-design-mobile-apps-setup)
- [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
