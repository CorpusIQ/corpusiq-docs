---
title: "popular-web-designs — Setup Guide"
description: "54 real-world design systems (Stripe, Linear, Vercel) as HTML/CSS templates. Official Hermes skill for generating branded web UIs. 451+ installs on skills.sh."
---

# popular-web-designs

**Source:** `nousresearch/hermes-agent` (official Hermes bundled skill)  
**Installs:** 451+ on skills.sh  
**Category:** Creative / Design  
**Skill ID:** `popular-web-designs`

## Overview

54 real-world design systems ready for use when generating HTML/CSS. Each template captures a site's complete visual language: color palette, typography hierarchy, component styles, spacing system, shadows, responsive behavior, and practical agent prompts with exact CSS values.

Design systems include: Stripe, Linear, Vercel, Apple, Airbnb, Notion, Supabase, Claude, Figma, Spotify, Coinbase, NVIDIA, Uber, and 40+ more.

## Installation

```bash
npx skills add nousresearch/hermes-agent@popular-web-designs -a hermes-agent -y
```

After installation, the skill becomes available in Hermes sessions. Verify:

```bash
hermes skills inspect popular-web-designs
```

## How to Use

1. Pick a design from the catalog (54 templates available)
2. Load it: `skill_view(name="popular-web-designs", file_path="templates/<site>.md")`
3. Use the design tokens and component specs when generating HTML
4. Pair with `generative-widgets` skill to serve the result via cloudflared tunnel

Each template includes a **Hermes Implementation Notes** block with CDN font substitutes, Google Fonts `<link>` tags, and CSS font-family stacks.

### Triggers

The skill activates when you mention:
- "build a page that looks like [Stripe/Linear/Vercel/...]"
- "make it look like stripe"
- "design like linear"
- "vercel style"
- "create a UI"
- "web design"
- "landing page"
- "dashboard design"

## Design Catalog

### AI & Machine Learning
| Template | Site | Style |
|---|---|---|
| `claude.md` | Anthropic Claude | Warm terracotta accent, clean editorial |
| `cohere.md` | Cohere | Vibrant gradients, data-rich dashboard |
| `elevenlabs.md` | ElevenLabs | Dark cinematic UI, audio-waveform |
| `minimax.md` | Minimax | Bold dark interface, neon accents |
| `mistral.ai.md` | Mistral AI | French minimalism, purple-toned |
| `ollama.md` | Ollama | Terminal-first, monochrome simplicity |
| `opencode.ai.md` | OpenCode AI | Developer-centric dark theme |
| `replicate.md` | Replicate | Clean white canvas, code-forward |
| `runwayml.md` | RunwayML | Cinematic dark UI |
| `together.ai.md` | Together AI | Technical, blueprint-style |
| `voltagent.md` | VoltAgent | Void-black, emerald accent |
| `x.ai.md` | xAI | Stark monochrome, futuristic |

### Developer Tools & Platforms
| Template | Site | Style |
|---|---|---|
| `cursor.md` | Cursor | Sleek dark, gradient accents |
| `expo.md` | Expo | Dark theme, code-centric |
| `linear.app.md` | Linear | Ultra-minimal dark, purple accent |
| `lovable.md` | Lovable | Playful gradients, friendly |
| `mintlify.md` | Mintlify | Clean, green-accented |
| `posthog.md` | PostHog | Playful, developer-friendly |
| `raycast.md` | Raycast | Sleek dark chrome |
| `resend.md` | Resend | Minimal dark, monospace accents |
| `sentry.md` | Sentry | Dark dashboard, pink-purple |
| `supabase.md` | Supabase | Dark emerald, code-first |
| `superhuman.md` | Superhuman | Premium dark, purple glow |
| `vercel.md` | Vercel | Black and white precision, Geist |

### Enterprise & Finance
| Template | Site | Style |
|---|---|---|
| `stripe.md` | Stripe | Clean gradients, sophisticated |
| `airtable.md` | Airtable | Colorful, data-centric |
| `apple.md` | Apple | Minimalist, product-focused |
| `bmw.md` | BMW | Premium automotive, dark |
| `clickhouse.md` | ClickHouse | Technical, data-dense |
| `coinbase.md` | Coinbase | Geometric, trustworthy blue |
| `hashicorp.md` | HashiCorp | Enterprise, neutral |
| `ibm.md` | IBM | Corporate blue, systematic |
| `intercom.md` | Intercom | Friendly, conversational |
| `kraken.md` | Kraken | Dark crypto exchange |
| `nvidia.md` | NVIDIA | Industrial, clean |
| `revolut.md` | Revolut | Fintech, bold |
| `uber.md` | Uber | Bold, movement-focused |
| `wise.md` | Wise | Clean fintech, green accent |

### Design & Creative
| Template | Site | Style |
|---|---|---|
| `figma.md` | Figma | Creative tool, colorful |
| `framer.md` | Framer | Design-forward, animation |
| `miro.md` | Miro | Collaborative, whiteboard |
| `pinterest.md` | Pinterest | Visual discovery, masonry |
| `sanity.md` | Sanity | Content platform, geometric |
| `webflow.md` | Webflow | Visual development, clean |
| `zapier.md` | Zapier | Automation, orange accent |

### Consumer
| Template | Site | Style |
|---|---|---|
| `airbnb.md` | Airbnb | Rounded, friendly, warm |
| `cal.md` | Cal.com | Scheduling, clean |
| `notion.md` | Notion | All-white, minimal |
| `spotify.md` | Spotify | Dark, vibrant green |
| `warp.md` | Warp | Terminal-native, dark |

## Related Skills

- **`claude-design`** — Use for the design *process and taste* (scoping a brief, producing variants, verifying artifacts). Pair with `popular-web-designs` when you want a thoughtfully-designed page styled after a known brand.
- **`design-md`** — Use when the deliverable is a formal DESIGN.md token spec file, not a rendered artifact.
- **`generative-widgets`** — Use to serve generated HTML via cloudflared tunnel for live preview.

## Font Substitution Reference

Most sites use proprietary fonts unavailable via CDN. Each template maps to a Google Fonts substitute:

| Proprietary Font | CDN Substitute | Character |
|---|---|---|
| Geist / Geist Sans | Geist (Google Fonts) | Geometric, compressed tracking |
| sohne-var (Stripe) | Source Sans 3 | Light weight elegance |
| Berkeley Mono | JetBrains Mono | Technical monospace |
| Airbnb Cereal VF | DM Sans | Rounded, friendly |
| Circular (Spotify) | DM Sans | Geometric, warm |
| figmaSans | Inter | Clean humanist |
| CoinbaseDisplay/Sans | DM Sans | Geometric, trustworthy |
| IBM Plex Sans/Mono | IBM Plex Sans/Mono | Available on Google Fonts |

## Verification

```bash
# Check skill is installed
hermes skills inspect popular-web-designs

# List available templates
ls ~/.hermes/skills/popular-web-designs/templates/

# Load a specific design
# Then in a Hermes session: "Build a landing page using the Stripe design template"
```

## Notes

- Official Hermes bundled skill from nousresearch/hermes-agent
- 54 design templates covering all major tech brands
- Each template includes exact CSS values, typography, spacing, and shadows
- Templates sourced from VoltAgent/awesome-design-md collection
- Pairs with `claude-design` for workflow and `design-md` for formal specs
