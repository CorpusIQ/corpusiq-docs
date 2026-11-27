---
title: "OpenMotion - Open-Source Motion Graphics Studio Setup"
description: "nexu-io/openmotion - 9.8K combined installs: open-source Claude Motion and CapCut alternative turning reference videos into editable motion graphics."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/nexu-io-openmotion-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "motion graphics", "video", "capcut", "openmotion"]
---

# OpenMotion - Setup Guide

**Source:** [nexu-io/openmotion](https://www.skills.sh/nexu-io/openmotion) via skills.sh - 9.8K combined installs across 94 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 evening sweep)
**GitHub:** [nexu-io/openmotion](https://github.com/nexu-io/openmotion) - 16,780 stars, Apache-2.0 license, last pushed Nov 27, 2026, main branch; skills split across skills/<name>/SKILL.md, .agents/skills/<name>/SKILL.md, and library/design/skills/<name>/SKILL.md.
**Category:** Motion Graphics and Agentic Video (OpenMotion)
**Quality Tier:** 🟠 Orange - 20 of 94 listings sampled: nine pass all three checks, eight carry a single Snyk Warn, and three carry a Snyk Fail (openmotion, openmotion-recreate, live-dashboard).

nexu-io/openmotion is OpenMotion, an open-source full-stack agentic video studio and CapCut alternative built by OpenDesign. It recreates reference videos as editable motion graphics coded in HTML, CSS, and JavaScript, then renders MP4s for YouTube, Shorts, Reels, and TikTok. The repo ships 300+ Motion.md guides and supports 22 local agents, including Claude Code, Codex, Hermes, and WorkBuddy.

The indexed skill surface splits into layers: the main openmotion skill handles setup and workflow routing, five specialist skills cover production, direction, recreation, and template conversion, and further skills cover media generation, Design Studio HTML projects, BYOK provider wiring, and browser games. The long tail of listings is dominated by library design and template skills rather than the core video workflow.

## Installation

Install the main skill with the Skills CLI:

```bash
npx skills add nexu-io/openmotion --skill openmotion
```

List the available skill names, or add the five specialist video skills in one call:

```bash
npx skills add nexu-io/openmotion --list
npx skills add nexu-io/openmotion --skill openmotion-director openmotion-production openmotion-template-to-video openmotion-recreate openmotion-video-to-template
```

Installing a skill copies instructions only; it does not install a runtime or register MCP. The skill then connects to the hosted Streamable HTTP /mcp endpoint via OAuth 2.1. To wire the Cloud MCP connection, paste this instruction into the agent:

```text
Read https://github.com/nexu-io/openmotion/blob/main/docs/install.md and follow the instructions to connect OpenMotion in the current agent.
```

To run the studio from source (Node.js 26.11.1 plus Chrome/Chromium and FFmpeg/FFprobe for preview and export):

```bash
git -c filter.lfs.process= -c filter.lfs.smudge= -c filter.lfs.required=false clone --depth 1 --single-branch --branch main https://github.com/nexu-io/openmotion.git
cd openmotion
npm ci
npm run build:studio
npm start
```

For local agents with stdio MCP support, point mcpServers at the checkout's mcp.ts with MOTION_DATA_DIR set, or run the published app with openmotion setup --host <agent-name>.

## What It Provides

skills.sh publishes per-skill install counts for all 94 indexed listings. The 10 most-installed skills (100 installs or more) are listed below; the remaining 84 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| openmotion | 4,539 | create and edit videos, recreate a reference video, or adapt an editable template; connects Cloud MCP via OAuth 2.1 for setup and first use |
| openmotion-production | 264 | execute local edits, asset or audio replacements, previews, troubleshooting, exports, and delivery on an existing project |
| openmotion-director | 261 | plan and create original motion videos and graphics: esports recaps, explainers, product demos, and brand films; also creative review |
| openmotion-recreate | 259 | rebuild a reference video (link or file) as the user's own editable project, swapping in their copy, brand, and assets |
| openmotion-template-to-video | 250 | browse, compare, and recommend catalog templates, or make a video from an existing editable template, project folder, or ZIP |
| openmotion-video-to-template | 242 | rebuild a reference video into a reusable editable template with source files, assets, preview, and editing guide |
| openmotion-media | 186 | generate, poll, and inspect individual image, video, speech, or music assets through configured BYOK providers |
| openmotion-design | 119 | create, revise, version, annotate, import, and export HTML Design Studio projects: prototypes, decks, documents, and WebGL |
| add-byok-provider | 117 | add or maintain a built-in BYOK media provider: API research, credentials, model discovery, and generation adapters |
| openmotion-game | 100 | build, remix, validate, and locally publish playable browser games through the OpenMotion game tools |

The remaining 84 indexed listings range from 14 to 90 installs.

## Why This Matters for Hermes Agents

OpenMotion is the open-source answer to Claude Motion and CapCut: a full-stack agentic video studio where the agent authors HTML, CSS, and JavaScript scenes, edits them on a visual timeline, and renders MP4s. For Hermes agents the value is the BYOA and BYOK model: bring your own agent and your own media-provider keys, with no software subscription or per-render fee on the local workflow. The main openmotion skill routes to the right specialist (production for scoped edits, recreate for reference reconstruction, director for original films), so the agent does not need to guess which workflow applies. The 300+ Motion.md guides encode shot order, timing, and transitions in Markdown, making brand motion reusable and reviewable across projects. Because the MCP surface is a hosted Streamable HTTP endpoint with OAuth 2.1, agent-side setup stays light while rendering and media generation run in the local service and Model Gateway, keeping provider credentials out of project files.

## Usage

| You say | What happens |
|---|---|
| Recreate this reference video for our brand | Uses openmotion-recreate to rebuild it as an editable project and open it in Studio |
| Make a product demo video | Uses openmotion-director to plan and produce an original motion video |
| Replace the music and re-export | Uses openmotion-production for scoped edits, previews, and export |
| Turn this clip into a reusable template | Uses openmotion-video-to-template to package source, assets, and an editing guide |
| Show me catalog templates for a launch | Uses openmotion-template-to-video to browse, compare, and recommend templates |
| Generate a background track and voice-over | Uses openmotion-media to generate music and speech assets via configured providers |
| Build a playable browser game | Uses openmotion-game to build, remix, and locally publish a game |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/nexu-io/openmotion/main/README.md | head -60
curl -sL https://raw.githubusercontent.com/nexu-io/openmotion/main/skills/openmotion/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Warn and Fail verdicts noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| openmotion | Warn | Pass | Fail |
| openmotion-production | Pass | Pass | Warn |
| openmotion-director | Pass | Pass | Warn |
| openmotion-recreate | Pass | Pass | Fail |
| openmotion-template-to-video | Pass | Pass | Warn |
| openmotion-video-to-template | Pass | Pass | Warn |
| openmotion-media | Pass | Pass | Warn |
| openmotion-design | Pass | Pass | Warn |
| add-byok-provider | Pass | Pass | Warn |
| openmotion-game | Pass | Pass | Warn |
| odui-build | Pass | Pass | Pass |
| odui-dev | Pass | Pass | Pass |
| odui-check | Pass | Pass | Pass |
| odui-apply | Pass | Pass | Pass |
| prototype-web | Pass | Pass | Pass |
| invoice | Pass | Pass | Pass |
| poster-hero | Pass | Pass | Pass |
| meeting-notes | Pass | Pass | Pass |
| magazine-poster | Pass | Pass | Pass |
| live-dashboard | Pass | Pass | Fail |

Across the 20 sampled skills there are 48 Pass, 9 Warn, and 3 Fail cells. Nine skills pass all three checks; eight carry a single Snyk Warn; three carry a Snyk Fail (openmotion, openmotion-recreate, live-dashboard), of which openmotion also carries a Gen Agent Trust Hub Warn.

## Limitations

- Snapshot data, verified Nov 26, 2026: 9,848 combined installs across 94 indexed listings; 16,780 GitHub stars; Apache-2.0 license; last pushed Nov 27, 2026. Counts drift over time.
- The 84 sub-threshold listings are dominated by library design and template skills (deck-, frame-, card-, web-proto-, and social- prefixed names); the core video workflow lives in the nine skills/ openmotion-* skills.
- skills.sh sampled only 20 of the 94 indexed listings; the other 74 carry no published verdict.
- The three Snyk Fail verdicts (openmotion, openmotion-recreate, live-dashboard) place the suite at the Orange tier; re-check the skills.sh pages before relying on those skills in production.
- Cloud MCP is the default connection path; the legacy local source and npm install path is archived, and published npm versions can lag behind the checkout.
- Installing a skill copies instructions only and does not install a runtime or register MCP; media generation needs provider keys configured in Model Settings.

## Related

[Remotion Motion Graphics Skill - Agent Video Setup](/hermes/skills/catalog/remotion-motion-graphics-skill-setup) | [Herk Edit Kit - AI Video Editing Setup](/hermes/skills/catalog/herk-edit-kit-setup) | [Motion Graphics Skills - Launch Video Suite](/hermes/skills/catalog/motion-graphics-skills-setup) | [Motion Design Skill - LottieFiles Animation Setup](/hermes/skills/catalog/lottiefiles-motion-design-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the main openmotion skill and let it route to the right specialist workflow for the job.
- Keep your logo, fonts, copy, and approved facts in the Brand Kit section of Motion.md so recreations stay on-brand.
- Configure provider keys in Model Settings rather than embedding them in the project; credentials stay out of project files.
- Review the editable Studio project before exporting, and keep the HTML/CSS/JS source alongside the MP4 for the next revision.
- Re-check the security pages on skills.sh for openmotion, openmotion-recreate, and live-dashboard, which carry the sample's Snyk Fails.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
