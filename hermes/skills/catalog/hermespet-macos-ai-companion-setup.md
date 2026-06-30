---
title: HermesPet macOS AI Companion — Setup Guide
description: Install and configure hermespet-macos-ai-companion, a desktop pet/companion that brings Hermes Agent to your macOS desktop with persistent presence and visual feedback. 38 installs from aradotso/hermes-skills.
---

# HermesPet macOS AI Companion — Setup Guide

**Source:** [aradotso/hermes-skills](https://github.com/aradotso/hermes-skills) · 38 installs
**Category:** Hermes Agent Variants / Desktop Integration
**License:** MIT · **Platform:** macOS · **Published:** June 2026

A macOS-native desktop companion built on the Hermes Agent framework. Provides persistent visual presence, interaction feedback, and personality to your Hermes agent — turning it from a background process into a visible desktop assistant.

---

## What It Does

| Feature | Description |
|---------|-------------|
| **Desktop Pet** | Animated character lives on your macOS desktop |
| **Agent Status** | Visual feedback for agent state (idle, working, error) |
| **Quick Commands** | Click interactions for common Hermes commands |
| **Notifications** | Desktop alerts for agent task completion |
| **Persistence** | Survives sleep/wake cycles, always visible |

The companion bridges the gap between a headless agent process and an interactive desktop experience — useful for development, demos, and keeping Hermes visible during long-running tasks.

---

## Prerequisites

- macOS 14 Sonoma or later
- Hermes Agent installed and configured
- Node.js 18+ (for npx installation)
- Accessibility permissions granted (System Settings → Privacy → Accessibility)

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add aradotso/hermes-skills@hermespet-macos-ai-companion
```

### Manual Clone

```bash
git clone https://github.com/aradotso/hermes-skills.git
cd hermes-skills/hermespet-macos-ai-companion
npm install
npm run build
```

### Start the Companion

```bash
npm start
```

On first launch, macOS will request Accessibility permission. Grant it for the companion to overlay on the desktop.

---

## Usage with Hermes Agent

After starting, the pet appears as a small animated character in the corner of your screen. It changes expression based on:

- **Idle:** Neutral, occasional animations
- **Processing:** Focused/working animation when Hermes is executing tasks
- **Complete:** Success animation when tasks finish
- **Error:** Alert expression when something fails

Click the pet to access a quick-command menu for common Hermes operations.

```bash
# The companion autodetects Hermes via the hermes CLI
hermespet-macos-ai-companion --hermes-profile corpusiq
```

---

## Configuration

```json
// ~/.hermespet/config.json
{
  "hermesProfile": "corpusiq",
  "position": "bottom-right",
  "size": "small",
  "animations": true,
  "soundEffects": false,
  "startOnLogin": true
}
```

| Option | Values | Default |
|--------|--------|---------|
| `position` | top-left, top-right, bottom-left, bottom-right | bottom-right |
| `size` | small, medium, large | small |
| `animations` | true/false | true |
| `soundEffects` | true/false | false |
| `startOnLogin` | true/false | false |

---

## CorpusIQ Use Cases

| Use Case | How |
|----------|-----|
| Agent monitoring | Visual cue when long-running tasks complete |
| Demo/presentation | Desktop-visible agent for showing Hermes to others |
| Development feedback | Instant visual state for debugging agent workflows |
| Always-on awareness | Never forget Hermes is running a background task |

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Pet doesn't appear | Grant Accessibility permission in System Settings |
| Pet frozen | Restart with `npm restart` |
| Hermes not detected | Verify `hermes` is in PATH; pass `--hermes-profile` explicitly |
| High CPU usage | Set `animations: false` in config |

---

*← [Hermes Agent Variants](/hermes/skills/catalog/#hermes-agent-variants) | [Catalog Home](/hermes/skills/catalog/) →*

---

*Part of the Hermes Skills Library. Curated by CorpusIQ — one MCP endpoint, all your business tools. Content remains attributed to original authors and repositories.*
