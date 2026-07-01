---
title: "Petdex — Animated Mascots for Hermes Agent"
description: "Install and configure animated petdex mascots for Hermes Agent. Add personality and visual feedback to your agent with desktop companions."
category: catalog
---

# Petdex — Animated Mascots Setup Guide

Add an animated desktop mascot to your Hermes agent. Petdex provides a collection of pixel-art animated companions that react to agent activity, giving your Hermes instance personality and visual feedback.

**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent) via [skills.sh](https://www.skills.sh/nousresearch/hermes-agent/petdex)

## Installation

```bash
npx skills add nousresearch/hermes-agent --skill petdex
```

## Prerequisites

- Hermes Agent installed and running
- Node.js 18+
- Display server (X11/Wayland on Linux; native on macOS)

## Usage

### List Available Mascots

```bash
# Browse the mascot catalog
hermes petdex list
```

### Select a Mascot

```bash
# Select by name
hermes petdex select blinky

# Random selection
hermes petdex random
```

### Configure Behavior

Mascots react to agent states:

```bash
# Show current mascot settings
hermes petdex config

# Set idle animation speed
hermes petdex config --idle-speed 2

# Enable reaction to errors
hermes petdex config --react-errors true
```

## Available Mascots

| Name | Style | Description |
|------|-------|-------------|
| `blinky` | Pixel | Classic blinking eye companion |
| `ghost` | Pixel | Friendly ghost that floats around |
| `cat` | Pixel | Animated cat with idle behaviors |
| `robot` | Pixel | Tiny robot with mechanical animations |
| `fox` | Pixel | Playful fox mascot |

Run `hermes petdex list` for the latest catalog.

## States & Animations

Mascots respond to these agent states:

| State | Behavior |
|-------|----------|
| **Idle** | Wandering, blinking, stretching |
| **Working** | Focused look, typing animation |
| **Error** | Alert expression, shaking |
| **Success** | Happy bounce, sparkle effect |
| **Waiting** | Tapping foot, looking around |

## Integration Tips

### Auto-start with Hermes

Add to your Hermes config (`~/.hermes/config.yaml`):

```yaml
petdex:
  enabled: true
  mascot: random
  idle_speed: 2
  react_errors: true
```

### Use as Agent Health Indicator

The mascot's visual state provides at-a-glance agent health:
- Happy/active = agent running normally
- Error state = check agent logs immediately
- Frozen = agent process may be hung

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Mascot not appearing | Check display server is running (`echo $DISPLAY`) |
| Mascot frozen | Restart with `hermes petdex restart` |
| High CPU usage | Lower idle speed: `hermes petdex config --idle-speed 1` |
| No mascots listed | Reinstall: `npx skills add nousresearch/hermes-agent --skill petdex` |
