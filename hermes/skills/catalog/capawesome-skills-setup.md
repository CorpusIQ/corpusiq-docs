---
title: "Capawesome Skills — Capacitor and Ionic Ecosystem Suite Setup"
description: "capawesome-team/skills — 37 skills, 11.4K installs: the Capacitor ecosystem team's suite covering plugin installation, app development, Ionic frameworks, upgrades, and Capawesome Cloud."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/capawesome-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-18"
tags: ["hermes skill", "agent skill", "skill setup", "capacitor", "ionic", "mobile", "plugins"]
---

# Capawesome Skills — Setup Guide

**Source:** [capawesome-team/skills](https://skills.sh/capawesome-team/skills)
**GitHub:** [capawesome-team/skills](https://github.com/capawesome-team/skills)
**Skills:** 37 skills · 11.4K total installs
**Category:** Mobile Development
**First Seen:** March 16, 2026 (catalogued August 18, 2026 sweep)
**Quality Tier:** 🟡 Trusted — Snyk Fail on the capacitor-plugins flagship (named); Gen Agent Trust Hub Pass and Socket Pass; 38 GitHub stars

Capawesome is a well-known Capacitor and Ionic ecosystem team (plugin vendor, capawesome.cloud services, Capawesome CLI). This is their agent skill suite for mobile app work: installing and configuring Capacitor plugins from official, Capawesome, community, Firebase, MLKit, and RevenueCat sources; app development across Ionic (Angular, React, Vue) and Capacitor (Angular, React, Vue); plugin development and SPM support; in-app purchases and push notifications; and migrations between Capawesome Cloud and Capgo. The flagship capacitor-plugins skill encodes careful agent behavior: step-by-step guidance, auto-detection of project state before asking questions, one decision at a time, and concrete options instead of open-ended prompts.

---

## Installation

```bash
npx skills add capawesome-team/skills
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/capawesome-team/skills --skill capacitor-plugins
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npm** | For the skill installer and project tooling |
| **Capacitor 6, 7, or 8 app** | The skills assume an existing Capacitor project |
| **iOS** | Xcode plus CocoaPods or Swift Package Manager for iOS plugins |
| **Android** | Android Studio for Android plugins |

## What It Provides

| Skill Group | Examples | Purpose |
|---|---|---|
| Plugin installation | capacitor-plugins, capacitor-plugin-development, capacitor-plugin-spm-support | Install and configure plugins from official, community, Firebase, MLKit, and RevenueCat sources |
| App development | capacitor-app-development, capacitor-app-creation, capacitor-angular, capacitor-react, capacitor-vue | Cross-framework Capacitor app builds |
| Ionic development | ionic-app-development, ionic-angular, ionic-react, ionic-vue, ionic-expert | Ionic framework app builds and upgrades |
| Feature skills | capacitor-push-notifications, capacitor-in-app-purchases, capacitor-app-upgrades | Push, purchases, and upgrade workflows |
| Ecosystem services | capawesome-cloud, capawesome-cli, capawesome-live-updates, capawesome-native-builds, capawesome-app-store-publishing | Capawesome Cloud and CLI services |
| Migrations | capgo-cloud-migration, ionic-appflow-migration, capacitor-app-migrations, capacitor-plugin-migrations | Platform migration paths |

Top skills by installs: capacitor-plugins (1.1K), ionic-angular (747), ionic-app-development (633), ionic-expert (628).

## Quick Start

1. Install: `npx skills add capawesome-team/skills`
2. Load capacitor-plugins and name the plugin source (official, Capawesome, community, Firebase, MLKit, RevenueCat)
3. Follow the step-by-step agent behavior — auto-detection first, one question at a time

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Mobile client builds** | Capacitor and Ionic skills support agent-built mobile apps for operator dashboards |
| **Plugin sourcing** | capacitor-plugins covers six plugin sources including Firebase and RevenueCat |
| **In-app purchases** | capacitor-in-app-purchases maps to monetization workflows |
| **Live updates** | capawesome-live-updates covers OTA update patterns for deployed apps |

## Limitations / Verification

- Security audits on the capacitor-plugins flagship: Gen Agent Trust Hub Pass, Socket Pass, Snyk Fail (named in the tier)
- Publisher-page total verified (11.4K across 37 skills); 38 GitHub stars as of the sweep
- Below the 20K install guide bar — drafted on ecosystem-team authority (Capawesome is the recognized Capacitor plugin vendor) and direct relevance to agent-built mobile apps
- Skills assume an existing Capacitor project and macOS/iOS tooling for native work

```bash
npx skills add capawesome-team/skills   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
