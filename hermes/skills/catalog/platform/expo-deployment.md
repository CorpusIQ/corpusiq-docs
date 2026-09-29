---
name: expo-deployment
description: "React Native deployment via Expo: build, configure, and ship mobile apps with EAS builds, environment profiles, and automated release flows for agent workflows."
triggers:
  - "expo deployment"
source: skills.sh marketplace
category: platform
setup: npx skills add expo/skills
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/platform/expo-deployment/"
robots: "index,follow"
last_updated: "2026-09-29"
title: "Expo Deployment - CorpusIQ Docs"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Expo Deployment

React Native deployment via Expo.

## Setup

```bash
npx skills add expo/skills@expo-deployment
```

## Capabilities

Build configuration, app store deployment, OTA updates, environment management.

## Hermes Integration

Install with `npx skills add` or via the Hermes skills manager. The skill auto-registers tools and workflows for the agent.

## Source

Discovered via skills.sh marketplace scan, June 2026.

## Roster Additions (Sep 29, 2026 sweep)

Two additional expo/skills listings surfaced in the Sep 29 sweep:

| Skill | Installs | What It Does |
|---|---|---|
| `expo-skill-eval` | 16,871 | Expo skill evaluation workflows |
| `eas-workflows` | 15,766 | EAS build and deployment workflows |

Install individually:

```bash
npx skills add expo/skills@expo-skill-eval
npx skills add expo/skills@eas-workflows
```

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills)  --  133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills)  --  133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
