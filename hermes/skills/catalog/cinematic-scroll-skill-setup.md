---
title: "cinematic-scroll-skill — Scroll-Driven Website Builder Setup"
description: "Set up the cinematic-scroll-skill (9⭐) to generate cinematic, scroll-driven websites from briefs using your Hermes agent."
skill_name: cinematic-scroll-skill
category: web-design
difficulty: Medium
platforms: [Linux, macOS, Windows]
---

# cinematic-scroll-skill — Full Setup Guide

**Repo:** [MustBeSimo/cinematic-scroll-skill](https://github.com/MustBeSimo/cinematic-scroll-skill) | ⭐ 9
**Author:** MustBeSimo | **Language:** TypeScript

cinematic-scroll-skill is a Hermes Agent / Claude Code skill that generates cinematic, scroll-driven websites from natural-language briefs. It produces visual systems, motion storyboards, and production-ready HTML/CSS/JS output.

---

## Prerequisites

- Node.js 20+
- Hermes Agent or Claude Code
- Modern browser for preview

---

## Installation

```bash
# Install via skills CLI
npx skills add MustBeSimo/cinematic-scroll-skill

# Or clone manually
git clone https://github.com/MustBeSimo/cinematic-scroll-skill.git
cd cinematic-scroll-skill
npm install
```

---

## Configuration

The skill auto-configures. No API keys required — it generates everything locally.

### Custom Templates (Optional)

Add your own design system to `~/.hermes/skills/cinematic-scroll/templates/`:

```
templates/
├── minimal/
│   ├── style.css
│   └── index.html
├── editorial/
│   ├── style.css
│   └── index.html
└── tech/
    ├── style.css
    └── index.html
```

---

## Usage

### Basic Brief

Tell your Hermes agent:

```
Use cinematic-scroll-skill to build a landing page for a SaaS analytics dashboard.
Dark theme, gradient accents, data-visualization-heavy.
3 sections: hero with particle effect, feature cards with scroll-triggered reveals,
and a pricing table with hover animations.
```

The skill generates:
1. **Visual system** — color palette, typography, spacing, component tokens
2. **Motion storyboard** — which elements animate on scroll, timing, easing
3. **Performance budget** — CSS/JS size targets, LCP/FID thresholds
4. **HTML/CSS/JS** — production-ready output

### Output Location

Generated sites go to `~/cinematic-output/<project-name>/`:

```
cinematic-output/
└── saas-landing/
    ├── index.html
    ├── styles.css
    ├── scripts.js
    ├── assets/
    └── brief.md           # Your original brief preserved
```

### Preview

```bash
cd ~/cinematic-output/saas-landing
python3 -m http.server 8080
# Open http://localhost:8080
```

---

## Brief Format Reference

The skill understands these directives:

| Directive | Example | Effect |
|-----------|---------|--------|
| Theme | "Dark theme" | Color palette direction |
| Sections | "3 sections: hero, features, pricing" | Page structure |
| Motion | "scroll-triggered reveals, parallax" | Animation style |
| Components | "cards, table, nav" | UI components |
| Vibe | "editorial, tech, playful" | Design language |
| Constraints | "no JS frameworks, <50KB CSS" | Technical limits |

### Example Briefs

**Portfolio:**
```
Use cinematic-scroll-skill to build a photographer's portfolio.
Light theme, minimal, image-first layout. Full-bleed hero with lazy-loaded gallery.
Scroll-triggered captions. Contact form with slide-in animation.
<100KB total, no frameworks.
```

**Product Page:**
```
Use cinematic-scroll-skill to build a product page for wireless earbuds.
Dark-to-light gradient, tech vibe. 5 sections: hero animation, feature breakdown
with 3D card flips, spec comparison table, reviews carousel, sticky CTA.
```

---

## Design System Output

The skill generates a design system alongside the website:

```css
/* Generated Design Tokens */
:root {
  --color-bg: #0a0a0f;
  --color-surface: #14141f;
  --color-primary: #6c5ce7;
  --color-accent: #00cec9;
  --color-text: #e8e8f0;
  --font-display: 'Inter', sans-serif;
  --font-body: 'Inter', sans-serif;
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 32px;
  --space-xl: 64px;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
  --motion-fast: 150ms ease-out;
  --motion-medium: 300ms ease-out;
  --motion-slow: 600ms cubic-bezier(0.16, 1, 0.3, 1);
}
```

---

## Motion Features

The skill supports these scroll-triggered animations:

| Animation | Trigger | Use |
|-----------|---------|-----|
| Fade up | Element enters viewport | Content reveals |
| Scale in | Element enters viewport | Hero elements |
| Parallax | Scroll position | Background depth |
| Sticky | Section boundary | Persistent elements |
| Pin | Section enter | Fixed-position narratives |
| Horizontal scroll | Section pin | Galleries, timelines |

---

## Performance Budgets

The skill enforces these defaults (customizable in your brief):

| Metric | Default | Strict Mode |
|--------|:-------:|:-----------:|
| Total CSS | <30KB | <15KB |
| Total JS | <10KB | <5KB |
| LCP (Largest Contentful Paint) | <2.5s | <1.5s |
| FID (First Input Delay) | <100ms | <50ms |
| Images | Optimized, lazy | Next-gen format only |

---

## Troubleshooting

### "Skill not found"

The skill may not be published to skills.sh yet. Install from GitHub directly:
```bash
git clone https://github.com/MustBeSimo/cinematic-scroll-skill.git
cp -r cinematic-scroll-skill ~/.hermes/skills/
```

### "Generated site looks broken"

1. Make sure CSS Grid and CSS Scroll-Driven Animations are supported in your browser
2. Chrome 115+, Safari 17.4+, Firefox 125+
3. Check the console for JS errors (should be none — no frameworks used)

### "Brief not understood"

The skill works best with structured briefs. Include:
- Theme/color direction
- Number of sections
- Component types
- Motion preferences
- Any constraints

---

*Guide last updated: July 4, 2026 | [Repo](https://github.com/MustBeSimo/cinematic-scroll-skill) | [Report issue](https://github.com/CorpusIQ/corpusiq-docs/issues)*
