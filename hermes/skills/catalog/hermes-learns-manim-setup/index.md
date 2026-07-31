---
title: Hermes Learns Manim — Math Animation Setup Guide
description: Enable Hermes Agent to create epic math and physics animations and study notes from text and images using the Manim animation library.
publisher: harleycoops/math-to-manim
stars: 2443
installs: 10
quality_tier: 🔵 Community
---

# Hermes Learns Manim — Math Animation Setup Guide

The `hermes-learns-manim` skill enables Hermes Agent to generate professional math and physics animations using the Manim (Mathematical Animation) library. Describe a concept in text or provide an image, and Hermes produces a rendered animation — ideal for educational content, explainer videos, and technical documentation.

**Publisher:** [harleycoops/math-to-manim](https://github.com/harleycoops/math-to-manim) — 2,443⭐  
**Source:** skills.sh  
**Quality Tier:** 🔵 Community (untested by CorpusIQ)

---

## What It Does

- **Text-to-Animation:** Converts natural language descriptions of math/physics concepts into Manim animations
- **Image-to-Animation:** Extracts formulas and diagrams from images and animates them
- **Study Notes:** Generates annotated study notes alongside animations
- **Multiple Output Formats:** MP4 video, GIF, or frame sequence output
- **LaTeX Rendering:** Full LaTeX math rendering within animations

---

## Prerequisites

| Requirement | Check |
|-------------|-------|
| Hermes Agent installed | `hermes --version` |
| Python 3.10+ | `python3 --version` |
| Manim installed | `pip install manim` |
| FFmpeg | `ffmpeg -version` |
| LaTeX (for math rendering) | `pdflatex --version` |

---

## Installation

### Step 1: Install System Dependencies

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install -y ffmpeg texlive texlive-latex-extra

# macOS
brew install ffmpeg mactex
```

### Step 2: Install Manim

```bash
pip install manim
```

### Step 3: Install the Skill

```bash
npx skills add https://github.com/harleycoops/math-to-manim --skill hermes-learns-manim
```

### Step 4: Verify Installation

```bash
hermes skills list | grep hermes-learns-manim
manim --version
```

---

## Usage

### Generate Animation from Text

```bash
hermes skill invoke hermes-learns-manim \
  --prompt "Explain the Fourier Transform with animated sine waves combining to form a square wave"
```

### Generate Animation from an Image

```bash
hermes skill invoke hermes-learns-manim \
  --image ~/Documents/equation.png \
  --output ~/Videos/fourier_explanation.mp4
```

### Generate Study Notes + Animation

```bash
hermes skill invoke hermes-learns-manim \
  --prompt "Derivative visualization: secant line approaching tangent line" \
  --notes \
  --output ~/Videos/derivatives/
```

### Quality Presets

```bash
# Preview quality (fast render)
hermes skill invoke hermes-learns-manim --quality draft --prompt "..."

# Production quality (slower, 1080p)
hermes skill invoke hermes-learns-manim --quality production --prompt "..."
```

---

## Output Structure

After running, the skill produces:

```
~/Videos/manim/
├── fourier_explanation.mp4       # Rendered animation
├── fourier_explanation_notes.md  # Study notes (if --notes flag)
└── fourier_explanation_source.py # Generated Manim source code
```

---

## Example Prompts

Try these to test the skill:

| Prompt | Expected Output |
|--------|----------------|
| "Gradient descent on a 3D surface, ball rolling to minimum" | 3D animated surface with path tracing |
| "Matrix multiplication visualized as row × column dot products" | Grid animation showing computation steps |
| "Pythagorean theorem proof with animated squares on triangle sides" | Classic geometric proof animation |
| "Neural network forward pass with sigmoid activations" | Node-and-edge animation with activation values |
| "Euler's formula e^(iπ) + 1 = 0 animated on complex plane" | Unit circle with rotating vector |

---

## Integration with CorpusIQ

For CorpusIQ content workflows:

- **Educational UGC:** Generate math/ML explainer videos for social media
- **Product Demos:** Animate algorithm visualizations for docs
- **Blog Content:** Enrich technical blog posts with custom animations
- **Client Deliverables:** Create professional visual explanations for consulting

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| "LaTeX not found" | texlive not installed | `sudo apt install texlive texlive-latex-extra` |
| Render takes too long | Production quality on complex scene | Use `--quality draft` for iteration |
| "FFmpeg not found" | FFmpeg missing | Install via system package manager |
| Animation looks wrong | Prompt too vague | Be specific about what should move and in what order |

---

## Related Skills

- [HyperFrames Video Pipeline](/hermes/skills/catalog/hyperframes-setup.html) — HTML-based video compositions
- [Remotion Best Practices](/hermes/skills/catalog/remotion-best-practices-setup.html) — React-based video production
- [Media Use](/hermes/skills/catalog/media-use-setup/) — Agent Media OS for all media needs

---

*Discovered July 31, 2026 · Published by harleycoops · 2,443⭐ parent repo*
