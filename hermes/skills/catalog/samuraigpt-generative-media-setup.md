---
title: Generative Media Skills — AI Video, Logo & Design Generation for Hermes Agents
description: Six generative media skills for brand-aware video creation, logo design, UI generation, cinema direction, and social media video production. 10K+ combined installs. Uses Seedance 2.0 for video.
---

# Generative Media Skills — Setup Guide

**Source:** [samuraigpt/generative-media-skills](https://skills.sh/samuraigpt/generative-media-skills) (10K+ combined installs)
**Category:** Media Generation / Video Production
**Quality Tier:** 🟡 Beta

Six generative media skills for end-to-end AI media production. The flagship **social-media-video** skill reads brand identity documents, ICP profiles, and messaging to produce on-brand social videos — fully optimized for Seedance 2.0's instructional prompt grammar. Also includes logo creation, UI design, and cinematic video direction.

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **muapi-social-media-video** | 1.8K | Brand-aware social video (storyboard → reference frames → Seedance 2.0) |
| **muapi-seedance-2** | 1.7K | Seedance 2.0 video generation with instructional prompt grammar |
| **muapi-logo-creator** | 1.7K | AI logo generation from brand identity docs |
| **muapi-ui-design** | 1.7K | UI/screen design generation |
| **muapi-nano-banana** | 1.6K | Image generation (model-agnostic) |
| **muapi-cinema-director** | 1.6K | Cinematic video direction with camera movement scripting |

---

## Installation

```bash
npx skills add samuraigpt/generative-media-skills --skill muapi-social-media-video
npx skills add samuraigpt/generative-media-skills --skill muapi-seedance-2
npx skills add samuraigpt/generative-media-skills --skill muapi-logo-creator
npx skills add samuraigpt/generative-media-skills --skill muapi-ui-design
npx skills add samuraigpt/generative-media-skills --skill muapi-nano-banana
npx skills add samuraigpt/generative-media-skills --skill muapi-cinema-director
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Brand Files** | `brand-identity.md`, `ICP.md`, `messaging.md` in working directory or `brand/` subdirectory |
| **Seedance 2.0** | Required for video generation skills (muapi-seedance-2, muapi-social-media-video) |
| **Image Model** | Any available image model for reference frame generation |

---

## Key Capabilities

### Social Media Video Creator
End-to-end pipeline: Brand Files → Storyboard → Reference Images → Seedance 2.0 Video:

1. **Read brand files**: Extracts visual style, color palette, target audience, core messaging
2. **Write social post + storyboard**: Hook line, body, hashtags, CTA + time-coded storyboard
3. **Generate reference frames**: Uses best available image model for key scenes
4. **Produce video**: Optimized Seedance 2.0 prompt with camera movement, transitions

### Cinema Director
Cinematic video direction with camera movement scripting — dolly, pan, zoom, tracking shots — for professional-quality AI video.

### Logo Creator
Reads brand identity documents and generates logo variations optimized for different use cases (social profile, website header, app icon).

### UI Design
Generates UI/screen designs from product descriptions, brand identity, and platform context.

---

## Quick Start — Hermes Agent

```bash
# Create sample brand files
mkdir -p brand
cat > brand/brand-identity.md << 'EOF'
# Brand: CorpusIQ
## Visual Style
- Colors: #0f0f12 (dark), #f0b90b (gold accent)
- Typography: Modern, technical
- Logo: Geometric owl silhouette
## Tone
Technical, operator-focused, helpful-first
EOF

cat > brand/ICP.md << 'EOF'
# ICP: Business Operators
- Role: Operations managers, founders, growth leads
- Pain: Too many disconnected AI tools, need unified platform
- Goal: 10x operational efficiency with AI
EOF

cat > brand/messaging.md << 'EOF'
# Core Messaging
- Hook: "One platform. Every AI tool. Zero complexity."
- CTA: "Start free at corpusiq.ai"
- Tagline: "Operate at the speed of AI"
EOF

# Install the social media video skill
npx skills add samuraigpt/generative-media-skills --skill muapi-social-media-video
```

---

## Verification

```bash
npx skills list | grep samuraigpt
# Should list installed generative media skills
```

---

## Notes

- **Brand-file driven**: Skills read markdown brand documents — no coding required for consistent output
- **Seedance 2.0**: Primary video engine — uses instructional prompt grammar for precise camera control
- **Use case for CorpusIQ**: UGC video production, social media content, logo refinement, UI mockups for product specs
- **Model agnostic**: Image generation uses whatever model is available — not locked to one provider
- **Related skills**: [corpusiq-media-pipeline](corpusiq-media-pipeline), [corpusiq-heygen-video-automation](corpusiq-heygen-video-automation), [hyperframes](hyperframes)
