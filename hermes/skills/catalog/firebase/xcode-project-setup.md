---
name: xcode-project-setup
description: Modify Xcode projects (.pbxproj) to add Swift Packages and link files safely. 144K installs.
triggers:
  - "xcode project setup swift package"
source: skills.sh marketplace
category: firebase
setup: npx skills add firebase/agent-skills@xcode-project-setup
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/firebase/xcode-project-setup/"
robots: "index,follow"
last_updated: "2026-11-22"
title: "Xcode Project Setup - CorpusIQ Docs"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Xcode Project Setup

Safe edit path for an Xcode project file: add Swift Packages and link files without corrupting the .pbxproj.

## Setup

```bash
npx skills add firebase/agent-skills@xcode-project-setup
```

## Capabilities

- Add Swift Package dependencies to an iOS project
- Link source and resource files into targets
- Avoid the hand edits that break project files

## Hermes Integration

Install with `npx skills add` or via the Hermes skills manager. The skill loads as markdown instructions, so it works in Hermes, Claude Code, Codex, Cursor and any other Agent Skills compatible client.

## Source

Listing and description taken from the `firebase/agent-skills` publisher on skills.sh, reviewed in the November 22, 2026 standing window. See [Firebase skills](/hermes/skills/catalog/firebase) for the rest of the family.

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) - 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
