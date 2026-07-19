---
title: taste-skill — Design-to-Code & AI Image Generation for Hermes (156K installs)
description: Install and use leonxlnx/taste-skill — convert screenshots to production code, generate web/mobile UI from text, with design-system awareness and accessibility-first output.
---

# taste-skill — Setup Guide

**Source:** [leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill) (156,100 installs)
**Category:** Design / Image Generation
**Languages:** TypeScript

AI-powered design-to-code and image generation skill. Three high-install capabilities: `image-to-code` (156.1K) converts screenshots and designs into production-ready frontend code, `imagegen-frontend-web` (155.5K) generates responsive web UI from text descriptions, and `imagegen-frontend-mobile` (151.9K) generates mobile UI designs. Built on modern AI image models with design-system awareness and accessibility-first output.

---

## Installation

```bash
# Design-to-code (screenshot → React/Vue/HTML)
npx skills add leonxlnx/taste-skill@image-to-code

# Web UI generation (text → responsive design)
npx skills add leonxlnx/taste-skill@imagegen-frontend-web

# Mobile UI generation (text → React Native/Flutter)
npx skills add leonxlnx/taste-skill@imagegen-frontend-mobile
```

Verify:
```bash
npx skills list | grep taste-skill
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | 18+ |
| **Hermes Agent** | Any version |
| **Design system** | Optional — provide existing tokens for consistent output |
| **AI model access** | OpenAI API key (GPT-4o) or Anthropic API key (Claude) |

---

## Key Capabilities

### image-to-code: Screenshot → Production Code

```
┌──────────────────┐     ┌───────────────────┐     ┌──────────────────┐
│  Screenshot/Design│ ──▶ │  AI Analysis      │ ──▶ │  Generated Code  │
│  (PNG, Figma URL) │     │  (layout, colors,  │     │  (React + Tailwind)│
│                    │     │   components)      │     │                    │
└──────────────────┘     └───────────────────┘     └──────────────────┘
```

```bash
# Convert a screenshot to React code
taste image-to-code \
  --source "landing-page-screenshot.png" \
  --framework "react" \
  --styling "tailwind" \
  --output "src/pages/LandingPage.tsx"

# Convert a Figma design
taste image-to-code \
  --source "https://figma.com/file/abc123" \
  --framework "nextjs" \
  --typescript \
  --responsive
```

**Supported frameworks:** React, Next.js, Vue, Svelte, plain HTML
**Styling options:** Tailwind CSS, styled-components, CSS Modules, vanilla CSS
**Output quality:** Production-ready with TypeScript types, accessibility attributes, responsive breakpoints

### imagegen-frontend-web: Text → Responsive Web UI

```bash
# Generate a SaaS dashboard from description
taste imagegen-web \
  --prompt "Analytics dashboard with revenue chart, KPI cards, recent transactions table, and sidebar navigation. Dark mode, professional" \
  --framework "nextjs" \
  --styling "tailwind" \
  --output "src/app/dashboard/"

# Generate a landing page with specific sections
taste imagegen-web \
  --prompt "SaaS landing page: hero with CTA, feature grid (3x2), testimonials carousel, pricing table (3 tiers), FAQ accordion, footer" \
  --responsive \
  --dark-mode \
  --output "src/app/landing/"
```

### imagegen-frontend-mobile: Text → Mobile UI

```bash
# Generate a React Native screen
taste imagegen-mobile \
  --prompt "E-commerce product detail: image carousel, price, variants selector, add-to-cart button, reviews section" \
  --framework "react-native" \
  --output "src/screens/ProductDetail.tsx"

# Generate Flutter screen
taste imagegen-mobile \
  --prompt "Fitness tracking home: steps counter, heart rate chart, workout list, bottom nav (Home, Workouts, Profile)" \
  --framework "flutter" \
  --output "lib/screens/fitness_home.dart"
```

### Design System Awareness

```bash
# Provide existing design tokens for consistent output
taste imagegen-web \
  --prompt "New feature settings page" \
  --design-tokens "tokens/colors.json" \
  --typography "tokens/typography.json" \
  --components "tokens/components.json"
```

When design tokens are provided, generated code respects:
- Color palette (primary, secondary, accent, semantic colors)
- Typography scale (font families, sizes, weights, line heights)
- Spacing scale (4px/8px grid)
- Border radius tokens
- Shadow/elevation tokens
- Existing component API (Button, Card, Input, etc.)

### Iterative Refinement

```bash
# Refine generated output with natural language
taste refine \
  --target "src/pages/LandingPage.tsx" \
  --change "Make the CTA button more prominent — increase size, add subtle glow animation"

taste refine \
  --target "src/app/dashboard/" \
  --change "Replace the line chart with a bar chart, swap sidebar from left to top navigation"
```

---

## Common Workflows for CorpusIQ

### Competitive UI Analysis

```bash
# Screenshot competitor dashboard → generate equivalent → analyze differences
taste image-to-code \
  --source "competitor-dashboard.png" \
  --framework "react" \
  --output "research/competitor-dashboard.tsx"

# Then use the generated code to understand their UI patterns
```

### Landing Page Iteration

```bash
# Generate 3 landing page variants for A/B testing
for variant in "benefit-focused" "feature-focused" "social-proof"; do
  taste imagegen-web \
    --prompt "CorpusIQ landing page: hero, features, testimonials, pricing, footer — $variant variant" \
    --output "ab-tests/landing-$variant/"
done
```

### Docs Site Page Generation

```bash
# Generate consistent docs pages with existing design tokens
taste imagegen-web \
  --prompt "Integration setup guide: steps with code blocks, prerequisites table, troubleshooting FAQ" \
  --design-tokens "corpusiq-docs/tokens/" \
  --output "docs/hermes/skills/catalog/new-skill-setup/"
```

---

## Accessibility-First Output

Generated code automatically includes:

| Feature | Implementation |
|---|---|
| **Semantic HTML** | `<nav>`, `<main>`, `<article>`, `<section>`, proper heading hierarchy |
| **ARIA labels** | `aria-label`, `aria-describedby`, `role` attributes on interactive elements |
| **Keyboard navigation** | `tabindex`, focus management, skip-to-content links |
| **Color contrast** | WCAG AA minimum (4.5:1 for text, 3:1 for large text) |
| **Screen reader** | Alt text on images, descriptive link text, live regions for updates |
| **Reduced motion** | `prefers-reduced-motion` media query support |

---

## Comparison: taste-skill vs Other Design Tools

| Feature | taste-skill | v0.dev | bolt.new | Cursor Composer |
|---|---|---|---|---|
| **Screenshot → code** | ✅ image-to-code | ⚠️ Partial | ❌ | ⚠️ Partial |
| **Text → web UI** | ✅ imagegen-web | ✅ | ✅ | ⚠️ |
| **Text → mobile UI** | ✅ imagegen-mobile | ❌ | ❌ | ❌ |
| **Design system aware** | ✅ Token integration | ⚠️ Limited | ❌ | ❌ |
| **Iterative refinement** | ✅ Natural language | ✅ Chat | ✅ Chat | ✅ Inline |
| **Install base** | 156K | N/A (platform) | N/A (platform) | N/A (IDE) |
| **Hermes integration** | ✅ CLI + API | ❌ Web only | ❌ Web only | ❌ IDE only |
| **Offline capable** | ⚠️ Needs API | ❌ | ❌ | ❌ |

**Recommendation:** taste-skill is the only tool that bridges design → code with design-system awareness AND works as a Hermes skill. Use it for rapid prototyping, competitive analysis, and docs site consistency.

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Generated code doesn't match screenshot | Low-res or complex screenshot | Use high-res (2x+), crop to single screen, avoid overlapping elements |
| Colors don't match brand | No design tokens provided | Pass `--design-tokens "tokens/colors.json"` with brand colors |
| Mobile UI doesn't look native | Wrong framework specified | Use `--framework "react-native"` for native look or `"flutter"` for Material |
| Output has accessibility issues | AI model hallucinating ARIA | Run `taste audit-a11y --target "output/"` for automatic fixes |
| Generation takes 30+ seconds | Large/complex prompt | Break into smaller components (header, hero, features — separately) |
| Tailwind classes conflict | Multiple generations in same project | Use `--prefix "tw-"` to namespace Tailwind classes |

---

## See Also

- [skill-creator](/hermes/skills/catalog/skill-creator-setup/) — Anthropic's skill creation framework (317K installs)
- [remotion-best-practices](/hermes/skills/catalog/remotion-best-practices-setup/) — Programmatic video with React (430K installs)
- [apify-agent-skills](/hermes/skills/catalog/apify-agent-skills-setup/) — Web scraping for competitive research
- [firecrawl-workflows](/hermes/skills/catalog/firecrawl-workflows-setup/) — Market research automation
