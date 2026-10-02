---
title: printing-press-library - Setup Guide
description: "mvanhorn/printing-press-library - the CLI Printing Press catalog: 472 agent-native CLIs across 22 categories (banking, travel, sports, media, dev tools) plus a discovery skill that searches and installs them. Rewritten Aug 27, 2026 to match the repo's actual CLI-catalog form."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/printing-press-library-setup/"
robots: "index,follow"
last_updated: "2026-08-27"
tags: ["hermes skill", "agent skill", "skill setup", "cli", "developer tools"]
---

# printing-press-library - Setup Guide

**Source:** [mvanhorn/printing-press-library](https://github.com/mvanhorn/printing-press-library)
**Skill:** `printing-press-library` (the catalog's discovery skill)
**Installs:** 679 (discovery skill, as of the Aug 12, 2026 sweep)
**Quality Tier:** 🔵 Community

> **Correction note (Aug 27, 2026):** an earlier version of this guide described the library as a print-ready document template library with a Python API. That was wrong. The repo is the **CLI Printing Press catalog** - 472 agent-native CLIs across 22 categories, each printed as a focused `pp-<name>` skill plus a Go binary, with a discovery skill that lets an agent search the catalog and install matching tools. This guide has been rewritten to match the actual repository.

## What it is

The CLI Printing Press philosophy: a well-designed CLI is muscle memory for an agent - no doc hunting, no wrong turns, no wasted tokens. This repo is the catalog of CLIs already printed and ready to install. Every entry ships:

1. A **focused skill** (`cli-skills/pp-<name>/SKILL.md`) the agent loads to learn the CLI's command surface
2. A **Go binary** (e.g. `mercury-pp-cli`) installed via the npm orchestrator
3. One-shot install: every install pulls the binary **and** the skill

Categories include banking/payments (pp-mercury), sports (pp-espn), travel (flight-goat), media/entertainment (movie-goat), dev tools (sentry-pp-cli, dub), and more - browse the full catalog at [printingpress.dev](https://printingpress.dev).

## Installation

### Discovery skill (recommended first install)

The discovery skill teaches an agent to search the catalog and pick the right focused skill, deferring CLI setup until the focused skill says it is needed.

```bash
# Vercel Agent Skills-compatible harnesses (verified live Aug 27, 2026)
npx skills add mvanhorn/printing-press-library -g -y --skill printing-press-library

# Hermes - command line
hermes skills install mvanhorn/printing-press-library/skills/printing-press-library

# Hermes - chat TUI
/skills install mvanhorn/printing-press-library/skills/printing-press-library

# OpenClaw
clawhub install printing-press-library
```

### Install specific CLIs (binary + focused skill in one shot)

```bash
# Starter pack: espn + flight-goat + movie-goat + recipe-goat
npx -y @mvanhorn/printing-press-library install starter-pack

# One tool
npx -y @mvanhorn/printing-press-library install espn

# Several at once (bundles and CLI names mix freely)
npx -y @mvanhorn/printing-press-library install espn sentry dub
```

Binary-only or skill-only:

```bash
npx -y @mvanhorn/printing-press-library install mercury --cli-only
npx -y @mvanhorn/printing-press-library install mercury --skill-only
```

### Catalog navigation

```bash
npx -y @mvanhorn/printing-press-library list
npx -y @mvanhorn/printing-press-library search flights
npx -y @mvanhorn/printing-press-library list --category travel
npx -y @mvanhorn/printing-press-library list --installed
npx -y @mvanhorn/printing-press-library update espn
npx -y @mvanhorn/printing-press-library uninstall espn --yes
```

Under the hood the npm package reads the live catalog in `registry.json`, resolves each CLI's Go module path, runs `go install`, and installs the matching skill from `cli-skills/pp-<name>`.

## Prerequisites

| Requirement | Details |
|---|---|
| Node.js | For the npm installer / discovery commands |
| Go 1.26.6+ | For the `go install` fallback on individual CLIs |
| `~/.local/bin` on `$PATH` | Default binary install location (macOS/Linux) |
| Per-CLI credentials | Each CLI needs its own auth (e.g. `mercury-pp-cli auth set-token`); see the focused skill |

## CorpusIQ Use Cases

1. **Agent tool discovery** - the discovery skill answers "what's the fastest CLI for X?" from a 472-entry catalog instead of an agent improvising API calls
2. **Banking ops** - pp-mercury for Mercury account/transfer/treasury operations with a read-only payment-plan approval workflow
3. **Sports/media data** - pp-espn and movie-goat for content research and trend monitoring
4. **Dev tooling** - sentry-pp-cli (local SQLite mirror, cross-org queries) for issue analytics
5. **One-command fleet setup** - `install starter-pack` provisions a whole tool set in a single invocation

## Verification

```bash
hermes skills list | grep printing-press-library
npx -y @mvanhorn/printing-press-library list --installed
```

## Related

- [pp-mercury - Mercury Banking CLI Setup](/hermes/skills/catalog/pp-mercury-setup) - the catalog's banking entry, with Hermes install path and payment-plan workflow
- [Skills Marketplace](/hermes/skills/marketplace) - more discovery batches
