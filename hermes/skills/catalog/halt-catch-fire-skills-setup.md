---
title: Halt-Catch-Fire Agent Skills — Setup Guide
description: Install and configure 6 new agent skills from halt-catch-fire — Remotion video rendering, AI avatar video, Twitter automation, AI video/image generation, and browser automation. 500K+ combined installs.
---

# Halt-Catch-Fire Agent Skills — Setup Guide

**Source:** [halt-catch-fire/skills](https://skills.sh/halt-catch-fire/skills)
**First Discovered:** June 27, 2026
**Total Ecosystem Installs:** 500K+

Six new agent skills from halt-catch-fire covering video rendering (Remotion), AI-powered media generation, Twitter/X automation, and browser automation for agents. These skills appeared on skills.sh in late June 2026 and rapidly accumulated installs across the Hermes/Nous Research ecosystem.

---

## Available Skills

| Skill | Installs | Recent Weekly | Description |
|---|---|---|---|
| `remotion-render` | 173K | 62,946 | Render Remotion video compositions programmatically |
| `ai-avatar-video` | 173K | 62,942 | Generate AI avatar-driven video content |
| `twitter-automation` | 173K | 62,923 | Automate Twitter/X posting, reading, and engagement |
| `ai-video-generation` | 173K | 62,920 | AI-powered video generation workflows |
| `ai-image-generation` | 173K | 62,921 | AI image generation with multiple model backends |
| `agent-browser` | 32K | 11,856 | Browser automation for agent-driven web interaction |

---

## Prerequisites

- Hermes Agent installed and running
- Node.js 18+ with `npx` available
- For `remotion-render`: Remotion project or template
- For AI media generation: API keys for supported AI services (configured in Hermes)
- For `twitter-automation`: Twitter/X API credentials

---

## Installation

```bash
# Install individual skills
npx skills add halt-catch-fire/skills --skill remotion-render
npx skills add halt-catch-fire/skills --skill ai-avatar-video
npx skills add halt-catch-fire/skills --skill twitter-automation
npx skills add halt-catch-fire/skills --skill ai-video-generation
npx skills add halt-catch-fire/skills --skill ai-image-generation
npx skills add halt-catch-fire/skills --skill agent-browser

# Or install all at once
npx skills add halt-catch-fire/skills
```

---

## Skill Details

### 1. remotion-render

Programmatic Remotion video rendering from agent prompts. Generate video compositions, apply effects, and export to MP4.

**Use cases:**
- Automated social media video generation
- Data visualization animations
- Programmatic video editing pipelines

**Usage:**
```
Render a 30-second product demo using the Remotion template at ./templates/product-launch
Export as 1080p MP4 with the "fade" transition between scenes
```

### 2. ai-avatar-video

AI avatar video generation — talking head videos driven by text input.

**Use cases:**
- Automated video presentations
- Customer onboarding videos
- Social media content with AI presenters

**Usage:**
```
Create a 60-second AI avatar video explaining our new feature
Use the "professional" avatar preset with the product screenshot as background
```

### 3. twitter-automation

Full Twitter/X automation — posting, reading timelines, engaging with mentions.

**Use cases:**
- Automated social media management
- Brand monitoring and engagement
- Content scheduling

**Usage:**
```
Post this thread about our product launch
Monitor @mentions for the last 24 hours and draft responses
```

### 4. ai-video-generation

General AI video generation using multiple backends (Runway, Pika, Kling, etc.).

**Use cases:**
- Text-to-video generation
- Image-to-video animation
- Video style transfer

**Usage:**
```
Generate a 10-second video from this product screenshot with a zoom-in effect
```

### 5. ai-image-generation

Multi-model AI image generation (Stable Diffusion, DALL-E, Flux, Midjourney API).

**Use cases:**
- Social media image creation
- Product mockups
- Marketing assets

**Usage:**
```
Generate a hero image for our blog post about AI agents, 1200x630, modern tech aesthetic
```

### 6. agent-browser

Browser automation for agents — navigate, click, extract data, fill forms.

**Use cases:**
- Web scraping and data extraction
- Automated testing
- Form filling and submission

**Usage:**
```
Navigate to docs.ourproduct.com and extract the API reference section
Fill out the contact form on this page with our company details
```

---

## Verification

After installation, verify the skills are available:

```bash
# List installed skills
npx skills list

# Test a skill
npx skills run remotion-render --help
```

---

## Troubleshooting

| Issue | Solution |
|---|---|
| Skill not found after install | Restart Hermes Agent to reload the skill registry |
| `remotion-render` fails on render | Ensure Remotion project structure is valid and dependencies are installed |
| `twitter-automation` auth errors | Verify Twitter API v2 credentials in Hermes config |
| `agent-browser` timeout | Increase browser timeout in skill config or check network connectivity |

---

## Quality Assessment

These skills are rated **Community Tier 🔵** pending further validation:

- Published by halt-catch-fire on skills.sh
- Rapid adoption suggests utility but limited track record
- Recommend supervised use for the first 5-10 runs
- Test in isolated environments before production deployment

---

## See Also

- [Remotion Documentation](https://remotion.dev)
- [Twitter API v2 Documentation](https://developer.twitter.com/en/docs/twitter-api)
- [Hermes Browser Automation Guide](/hermes/skills/development/)
- [AI Video Generation Strategy](/hermes/skills/marketing/)
