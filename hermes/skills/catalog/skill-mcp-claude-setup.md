---
title: "Skill MCP Claude - Frontend Skills and Manager Setup"
description: "bbeierle12/skill-mcp-claude - 7.6K combined installs: a Flask skills manager plus 77 frontend and animation skill files."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/skill-mcp-claude-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "gsap", "shaders", "frontend"]
---

# Skill MCP Claude - Frontend Skills and Manager Setup

**Source:** [bbeierle12/skill-mcp-claude](https://www.skills.sh/bbeierle12/skill-mcp-claude) via skills.sh - 7.6K combined installs across 77 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 evening sweep)
**GitHub:** [bbeierle12/skill-mcp-claude](https://github.com/bbeierle12/skill-mcp-claude) - 9 stars, MIT, main branch, last pushed Nov 23, 2026; a Skills Manager app (Flask API, MCP server, single-file web UI) whose skills/ directory holds the 77 indexed skill files.
**Category:** Frontend Animation Skills and MCP Skills Management
**Quality Tier:** 🟢 Green - every one of the 20 sampled skills passes Gen Agent Trust Hub, Socket and Snyk with no Warn or Fail cells.

The repository describes itself as a visual web interface for managing Claude MCP skills through a Flask API and Claude Code CLI integration, and that application is real: server.py is the MCP server, skills_manager_api.py is the Flask HTTP API on port 5050, and skills-manager.html is the single-file web UI. But the 77 listings that skills.sh indexes are not MCP-manager features. They are the skill files in the skills/ directory, and the overwhelming majority are frontend and animation skills (GSAP, shaders, D3, React Three Fiber, particles, Web Audio and post-processing), plus document and office skills and a handful of general development skills.

For an installing agent the takeaway is simple: the skills/ directory is a self-contained library you can copy into any agent that reads SKILL.md files, while the manager application is a separate way to browse and edit those same files through a web UI. The top two skills, gsap-react and gsap-scrolltrigger, dominate installs, and the long tail runs down to single-digit counts.

## Installation

Clone the repository and install the manager's Python dependencies:

```bash
git clone https://github.com/bbeierle12/skill-mcp-claude
cd skill-mcp-claude
pip install -r requirements.txt
```

Run the Flask API, which opens at http://localhost:5050:

```bash
python skills_manager_api.py
```

Run the MCP server for Claude Desktop:

```bash
python server.py
```

To use the skills without the manager, copy skill folders from skills/ into the agent skill directory (Claude Code reads .claude/skills/, Cursor and Codex read .agents/skills/).

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| gsap-react | 728 | GSAP integration with React: useGSAP hook, refs, cleanup, reusable hooks |
| gsap-scrolltrigger | 615 | scroll-driven GSAP animation: pinning, scrubbing, snap points, parallax |
| gsap-fundamentals | 286 | core GSAP: tweens, timelines, easing and animation properties |
| shader-effects | 226 | visual shader effects: glow, chromatic aberration, distortion, glitch |
| d3js-visualization | 189 | D3 charts and interactive data visualizations |
| particles-gpu | 174 | GPU particle systems via instancing, buffer attributes and custom shaders |
| shader-fundamentals | 173 | GLSL fundamentals: vertex and fragment shaders, uniforms, varyings |
| gsap-sequencing | 163 | complex GSAP timelines: labels, callbacks, nested timelines, position parameters |
| audio-analysis | 154 | Tone.js and Web Audio analysis: FFT, frequency data, waveform |
| software-architecture | 150 | Clean Architecture, SOLID and design-pattern guidance for system design |
| particles-physics | 134 | particle physics: gravity, wind, drag, attractors, turbulence, collision |
| r3f-fundamentals | 125 | React Three Fiber setup: Canvas, scene hierarchy, cameras, lighting |
| shader-noise | 123 | procedural GLSL noise: Perlin, simplex, Worley, FBM, domain warping |
| form-ux-patterns | 120 | complex-form UX: multi-step, chunking, progressive disclosure, conditional fields |
| audio-reactive | 108 | binding audio analysis to visual parameters, beat detection, frequency mapping |
| postfx-effects | 106 | post-processing: chromatic aberration, vignette, depth of field, film grain, grading |
| frontend-dev-guidelines | 105 | React/TypeScript frontend guidelines: Suspense, lazy loading, styling, routing |
| gsap-router | 102 | GSAP router routing to four specialized GSAP skills |
| shader-sdf | 100 | signed distance functions: primitives, boolean ops, smoothing, raymarching |
| r3f-performance | 100 | R3F performance: LOD, culling, instancing, draw-call reduction, profiling |

The remaining 57 indexed listings range from 13 to 98 installs.

## Why This Matters for Hermes Agents

The skills/ directory is a concentrated frontend animation library: GSAP, GLSL shaders, D3, React Three Fiber, particles, Web Audio and post-processing, plus form and document tooling. For an agent building animated interfaces this is a fast path, because gsap-react and gsap-scrolltrigger answer the two questions that consume the most time in React animation work: how to integrate GSAP cleanly with the component lifecycle, and how to drive animation from scroll. The shader and R3F skills cover the graphics side, where a single wrong uniform or an uncontrolled draw call produces a broken frame.

The manager application is separate from the skill library. If you only want the skills, copy the skill folders into the agent skill directory and ignore the Flask server, the MCP server and the web UI. If you want the manager, it gives you a browser view, a REST API and MCP tools over those same files, plus a daily audit that grades each skill. Do not expect the indexed listings to behave as MCP tools; they are markdown skill files that the manager happens to host.

## Usage

| You say | What happens |
|---|---|
| Animate a React component with GSAP | Uses gsap-react for useGSAP, refs and cleanup |
| Add a scroll-triggered pinned section | Uses gsap-scrolltrigger for pinning, scrub and snap |
| Write a GLSL shader with distortion | Uses shader-fundamentals plus shader-effects |
| Make a D3 bar chart | Uses d3js-visualization |
| Build a React Three Fiber scene | Uses r3f-fundamentals and r3f-performance |
| Add particle effects | Uses particles-gpu and particles-physics |
| Manage skills through a browser UI | Runs the Flask API and opens the web UI |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/bbeierle12/skill-mcp-claude/main/README.md | head -40
```

Confirm the gsap-react skill body is present before React animation work:

```bash
curl -sL https://raw.githubusercontent.com/bbeierle12/skill-mcp-claude/main/skills/gsap-react/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| gsap-react | Pass | Pass | Pass |
| gsap-scrolltrigger | Pass | Pass | Pass |
| gsap-fundamentals | Pass | Pass | Pass |
| shader-effects | Pass | Pass | Pass |
| d3js-visualization | Pass | Pass | Pass |
| particles-gpu | Pass | Pass | Pass |
| shader-fundamentals | Pass | Pass | Pass |
| gsap-sequencing | Pass | Pass | Pass |
| audio-analysis | Pass | Pass | Pass |
| software-architecture | Pass | Pass | Pass |
| particles-physics | Pass | Pass | Pass |
| r3f-fundamentals | Pass | Pass | Pass |
| shader-noise | Pass | Pass | Pass |
| form-ux-patterns | Pass | Pass | Pass |
| audio-reactive | Pass | Pass | Pass |
| postfx-effects | Pass | Pass | Pass |
| frontend-dev-guidelines | Pass | Pass | Pass |
| gsap-router | Pass | Pass | Pass |
| shader-sdf | Pass | Pass | Pass |
| r3f-performance | Pass | Pass | Pass |

The 57 listings outside the sample carry no verdict cells in this guide, so check their own pages before installing them.

## Limitations

- Snapshot data, verified Nov 23, 2026: 7,637 combined installs across 77 indexed listings; 9 GitHub stars; MIT licence; last pushed Nov 23, 2026. Counts drift over time.
- Index-versus-tree mismatch: the repo describes itself as a visual web interface for managing Claude MCP skills, but the indexed listings are frontend and animation skill files in skills/, not MCP-manager behaviour. The manager is one app; the indexed skills are its sample library.
- The README names the project folder skills-mcp, but the repository clones as skill-mcp-claude; adjust the cd path accordingly.
- The install band is steep: the top two skills (gsap-react 728, gsap-scrolltrigger 615) dwarf the tail, which runs to single digits; 57 listings sit below 100 installs.
- 57 of the 77 listings sit outside the verdict sample and carry no security cells in this guide.

## Related

- [Build MCP Server Setup](/hermes/skills/catalog/build-mcp-server-setup)
- [Awesome Copilot - MCP Server Generators & GitHub Automation Setup](/hermes/skills/catalog/awesome-copilot-setup)
- [MCP Use Setup](/hermes/skills/catalog/mcp-use-setup)
- [Native MCP Setup](/hermes/skills/catalog/native-mcp-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy the skill folders from skills/ directly if you only need the skills; the manager is optional.
- Pair gsap-fundamentals with gsap-react or gsap-scrolltrigger: the fundamentals skill is the shared foundation.
- The README names the project folder skills-mcp, but the clone directory is skill-mcp-claude; adjust the cd path.
- Run scripts/run_daily_audit.py if you want the per-skill relevance grading the manager displays.
- Verify a skill exists in the current tree before installing a long-tail name; the index runs to 77 listings with single-digit installs at the bottom.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
