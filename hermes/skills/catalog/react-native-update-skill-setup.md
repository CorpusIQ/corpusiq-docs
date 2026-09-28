---
title: "React Native Update Skill - OTA Update Integration Setup"
description: "Setup guide for reactnativecn/react-native-update-skill - host-neutral agent skill for react-native-update OTA integration with Pushy and Cresc (230 installs)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/react-native-update-skill-setup/"
robots: "index,follow"
last_updated: "2026-09-28"
tags: ["hermes skill", "agent skill", "skill setup", "react native", "ota updates", "mobile"]
---

# React Native Update Skill - Setup Guide

**Source:** [reactnativecn/react-native-update-skill](https://github.com/reactnativecn/react-native-update-skill) (pushed Sep 27, 2026)
**Skill:** `reactnativecn/react-native-update-skill@react-native-update` (230 installs)
**Category:** Mobile Development / OTA Updates
**Quality Tier:** 🔵 Community (brand-new repo, no security verdicts published - verified Sep 28, 2026)

A host-neutral Agent Skill for integrating `react-native-update` (Pushy/Cresc) into React Native apps. It is built for any agent that supports Agent Skills - not tied to a specific host, model, or plugin system. Covers React Native CLI, Expo prebuild, tvOS/react-native-tvos, HarmonyOS, brownfield, monorepo, and mixed-native projects: update.json/appKey config, UpdateProvider/useUpdate wiring, native bundle loading, release baseline upload, cold-start recovery (forceBoot/purgeRestore), Hermes verification, expo-updates conflicts, and OTA failure triage.

---

## Installation

```bash
npx skills add reactnativecn/react-native-update-skill --skill react-native-update
```

The portable source is the complete `skill/react-native-update/` directory in the repo (SKILL.md + references + optional diagnostic scripts). Point any host's skill installer at the repository and select `skill/react-native-update`.

## Key Capabilities

| Capability | Trigger |
|---|---|
| Update.json / appKey configuration | "configure react-native-update for Pushy" |
| UpdateProvider / useUpdate wiring | "wire useUpdate into my app" |
| Native bundle loading & cold-start recovery | "set up forceBoot / purgeRestore" |
| Release baseline upload & bundleHash metadata | "upload a release baseline" |
| Hermes-base verification & expo-updates conflict resolution | "check Hermes compatibility" |
| OTA failure triage | "OTA update failed to load" |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Mobile client work** | Standardizes OTA update integration for client React Native apps (CLI, Expo prebuild, tvOS, HarmonyOS) |
| **Monorepo / brownfield builds** | Covers mixed-native and monorepo setups other RN guides skip |
| **Triage reference** | OTA failure modes (checkStrategy/updateStrategy, canary/metaInfo flows) documented for support questions |

## Limitations / Verification

- 0⭐ repo published Sep 27, 2026 - very new; install count (230) reflects Pushy/Cresc user base demand
- Requires a Pushy or Cresc account for actual OTA delivery
- Verify: `npx skills add reactnativecn/react-native-update-skill --list` shows the skill

## Security

No skills.sh security audits published (verified Sep 28, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Skills Marketplace](/docs/hermes/skills/marketplace)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Skills Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
