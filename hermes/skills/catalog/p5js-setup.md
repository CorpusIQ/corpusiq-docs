---
title: p5js — Creative Coding & Generative Art Setup
description: Install and configure p5js from nousresearch/hermes-agent. Creative coding library skill for generative art, interactive visuals, and algorithmic design — 321 installs.
category: hermes-skills
publisher: nousresearch
installs: 321
source: https://skills.sh/nousresearch/hermes-agent/p5js
---

# p5js — Creative Coding Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/p5js) (321 installs)
**Category:** Creative / Generative Art
**License:** MIT · **Platforms:** Linux, macOS, Windows
**Dependencies:** Node.js 18+, p5.js library

Agent skill for p5.js — the industry-standard creative coding library by the Processing Foundation. Enables Hermes to generate interactive visuals, generative art, data visualizations, and algorithmic designs using the full p5.js API. 321 installs makes this one of the most popular creative skills in the Hermes ecosystem.

---

## What It Does

| Capability | How |
|-----------|-----|
| **Generative art** | Algorithmic drawings, particle systems, flow fields |
| **Interactive visuals** | Mouse/keyboard-responsive sketches |
| **Data visualization** | Charts, graphs, and data-driven art |
| **Animation loops** | Frame-by-frame animation with draw() cycle |
| **3D rendering** | WEBGL mode for 3D shapes and scenes |
| **Export** | Save canvas as PNG, SVG, or GIF |

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add nousresearch/hermes-agent --skill p5js
```

### Direct from Hermes Agent Repo

```bash
git clone --depth 1 https://github.com/nousresearch/hermes-agent.git /tmp/hermes-agent
cp -r /tmp/hermes-agent/skills/creative/p5js ~/.hermes/skills/
```

---

## Usage Examples

### Generative Art

```
Hermes, create a p5.js sketch that generates a flow field of 10,000 particles in neon colors.
```

### Data Visualization

```
Using p5js, visualize this dataset as an interactive bar chart with hover effects.
```

### Algorithmic Design

```
Create a p5.js sketch that draws a recursive tree fractal that grows with mouse movement.
```

---

## Key p5.js Functions the Skill Understands

| Function | Purpose |
|----------|---------|
| `setup()` | Initialize canvas, set frame rate |
| `draw()` | Continuous animation loop |
| `createCanvas(w, h)` | Set canvas dimensions |
| `background(r, g, b)` | Clear canvas with color |
| `fill(r, g, b)` | Set shape fill color |
| `stroke(r, g, b)` | Set outline color |
| `noise(x, y)` | Perlin noise for organic patterns |
| `random(min, max)` | Random number generation |
| `translate(x, y)` | Move origin point |
| `rotate(angle)` | Rotate coordinate system |
| `push()/pop()` | Save/restore transformation state |

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v0.14.0+ |
| Node.js | 18+ |
| Browser or p5.js runtime | For rendering output |

---

## Verification

After install, test with:

```
Hermes, create a simple p5.js sketch: a 400x400 canvas with a circle that follows the mouse cursor.
```

The agent should generate a complete p5.js sketch with `setup()` and `draw()` functions.

---

## Pitfalls

- **Browser required for rendering:** p5.js sketches need a browser or HTML canvas to render. The skill generates the code — you need a runtime to see the output.
- **Performance:** Large particle systems (10K+ particles) or complex 3D scenes can be slow. Use `frameRate()` to cap performance.
- **Not a video tool:** p5.js generates real-time visuals, not video files. For video output, use `manim-video` or export frames and stitch them.
- **WEBGL limitations:** WEBGL mode has a different API from 2D mode. Some 2D functions (`fill`, `stroke`) work differently in 3D.

---

## See Also

- [ascii-art-setup.md](ascii-art-setup.md) — ASCII art generation
- [excalidraw-setup.md](excalidraw-setup.md) — Diagram creation
- [design-md-setup.md](design-md-setup.md) — Visual identity design tokens

---

*Setup guide by CorpusIQ. Source: [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent) (MIT).*
