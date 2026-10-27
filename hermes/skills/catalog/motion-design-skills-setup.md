---
title: "Motion Design Skills - After Effects and Remotion Setup"
description: "iart-ai's nine motion design skills: 26.6K combined installs. Timing, color, composition, After Effects, Remotion, logo and background animation."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/motion-design-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-27"
tags: ["hermes skill", "agent skill", "skill setup", "motion design", "after effects", "remotion"]
---

# Motion Design Skills - Setup Guide

**Source:** [iart-ai/motion-design-skills](https://www.skills.sh/iart-ai/motion-design-skills) via skills.sh - 26.6K combined installs across 9 indexed listings; first documented 2026-10-27 (Oct 27 morning sweep)

**GitHub:** [iart-ai/motion-design-skills](https://github.com/iart-ai/motion-design-skills) - 167 stars, MIT, branch main, nine skill directories under `skills/`, each with its own `SKILL.md` and a `references/` folder, plus a shared `scripts/` toolkit and a `.claude-plugin/` marketplace manifest

**Category:** Motion design and video production

**Quality Tier:** 🟡 Beta - 2.7K to 3.4K installs on every listing, MIT, nine skills for one discipline

iart.ai publishes motion design tooling, and this repository is that discipline packaged as nine installable skills. The split is intentional rather than thematic: one skill decides how something should move, one sets the direction above it, two carry the engines that render it (After Effects and Remotion), and five carry the brand elements that make a piece hold together (color, composition, logos, backgrounds, edit rhythm). The README states the skills run in Claude Code, Cursor, Codex and 40 or more agents, and that this pack is one of a 14-pack collection from the same publisher.

The giveaway that these are written by practitioners is the shape of the output. The skills do not answer with adjectives. `animation-principles` returns durations, cubic-bezier curves, stagger offsets and spring configs. `shot-composition` returns layer structure and camera-move plans with numbers. `color-motion` returns palettes in exact OKLCH and hex values. Every skill directory also ships a `references/` folder holding the long form detail, and the repository root carries a small `scripts/` toolkit for the verify step. Each `SKILL.md` in the tree is version 0.1.0, so treat the collection as new rather than settled.

## Installation

The README gives two paths. The generic one uses the skills CLI, which resolves the repository and prompts per skill:

```bash
npx skills add iart-ai/motion-design-skills
```

The second registers the repository as a Claude Code plugin marketplace, then installs the bundle from it:

```bash
/plugin marketplace add iart-ai/motion-design-skills
/plugin install motion-design-skills
```

The marketplace commands are two separate steps in the README: add the marketplace, then install the plugin named `motion-design-skills`. The `.claude-plugin/` directory holds the manifest that makes that work.

There is no build step and no runtime. Each directory under `skills/` is self contained, with a `SKILL.md` entry point, a `references/` folder for depth, and in the After Effects case an extra `scripts/` folder of its own. Copying a single directory into your agent's skills folder is equivalent to installing it.

The repository root also ships a three-script verify toolkit that its own `scripts/README.md` documents: `seek-shot.sh` freezes and screenshots moments from a standalone HTML animation, `contact-sheet.sh` tiles frames into one image for a start, mid and end review, and `probe-mp4.sh` reads and asserts the real resolution, codec, frame rate and duration of a rendered MP4. Those helpers need `ffmpeg` and `ffprobe` on the host.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| motion-art-direction | 3,438 | The creative direction layer above technique: motion language, tone and energy, pacing and rhythm, motion hierarchy, restraint, and cross-shot consistency, plus the decision about what should not move at all. |
| animation-principles | 3,049 | Tech agnostic timing, easing, spacing, weight and rhythm: concrete durations, cubic-bezier curves, stagger offsets and spring configs ready to hand to any implementation. |
| shot-composition | 3,022 | Grids, safe areas, focal hierarchy and negative space, layer structure across background, midground and foreground, 2D and 3D camera framing, and adapting one layout across 16:9, 9:16 and 1:1. |
| beat-sync-editing | 2,993 | Cutting to the beat: edit rhythm, match cuts, J-cuts and L-cuts, retiming, speed ramps, and translating a cut plan into NLE operations or frame numbers for Remotion and After Effects. |
| logo-animation | 2,930 | Logo reveals, stingers, app splash screens and loader loops for web through SVG or Lottie, video and app delivery, always with a static end-frame fallback. |
| color-motion | 2,920 | Palette construction, gradient backgrounds, perceptually uniform interpolation in OKLCH or Lab, grading order, and render color management including gamma shift and Rec.709 against sRGB. |
| after-effects | 2,828 | After Effects work: expressions and rigging with sliders and nulls, MOGRT and Lottie export recipes, performance triage for slow or crashing comps, project hygiene, and ExtendScript. |
| motion-background | 2,781 | Ambient loops behind content: CSS mesh gradients, GLSL shader auroras through Three.js, canvas particle constellations, seamless loop seams, and reduced-motion handling. |
| remotion-video | 2,658 | Programmatic video in React: compositions driven by `useCurrentFrame`, `interpolate` and `spring`, rendered to MP4, GIF or WebM through the CLI or `@remotion/renderer`, including one video per CSV row. |

No indexed listings fall below the threshold; all nine appear in the table above.

## Why This Matters for Hermes Agents

Motion is the part of frontend and video work where an agent is most confidently wrong. Asked to add an entrance animation, a model typically reaches for a default duration with a default easing curve, and the result reads as generic because nothing in the training data told it what this particular piece needed. The failure is not a compile error, so nobody catches it until a human watches the result and says it feels cheap.

These skills attack that gap with numbers. `animation-principles` is the tech agnostic one, and it converts a vague complaint into a duration, an easing curve and a stagger offset. That output is then actionable by whichever engine is in play, which is why it pairs cleanly with the other eight.

The engine skills cover the two places a Hermes agent actually produces motion: a React codebase through Remotion, or an After Effects project the user drives. The Remotion skill is the more useful of the two for an agent working unsupervised, because every frame is a pure function of the frame number, so output is deterministic and renderable in CI. The After Effects skill is a knowledge skill in the honest sense: it hands back expressions, rig setups, export checklists and ExtendScript, and it cannot render anything on its own.

The remaining skills cover direction and brand elements, and they are the ones that stop an agent from shipping nine individually correct animations that look like they came from nine different studios. Direction, color, composition, edit rhythm, logo and background each hold a small set of rules, and applying the same rules twice is what makes a sequence feel authored.

One caveat belongs up front: this is a small, new, single-publisher collection, not a measured benchmark. The install counts show distribution, and the skills read as well organised knowledge rather than battle tested procedure.

## Usage

| You say | What happens |
|---|---|
| "This animation looks robotic, make it feel natural" | animation-principles diagnoses the timing and spacing, then returns a duration, an easing curve and a stagger offset that replace the default ease. |
| "Cut this sequence to the music" | beat-sync-editing turns the track into beat positions, then plans cut points, match cuts and speed ramps as either NLE moves or exact frame numbers. |
| "Render one MP4 per row of this CSV" | remotion-video builds a React composition that takes the row as props, renders the batch, and probe-mp4.sh asserts each file's resolution, codec and frame rate. |
| "Animate our logo into a three second intro" | logo-animation plans the reveal and settle, syncs the final beat to a sound logo, and specifies the static end frame the video falls back to. |
| "These gradient backgrounds look muddy" | color-motion rebuilds the gradient with OKLCH interpolation, then checks the render path for gamma shift between preview and final video. |
| "My After Effects comp is unusable at 4K" | after-effects runs its performance triage, naming the pre-render, cache and rigging causes in order, then points at the matching export recipe. |
| "This layout breaks when I crop it to vertical" | shot-composition reframes for 9:16 around safe areas and focal hierarchy, and re-plans the camera move for the narrower frame. |

## Verification

Confirm the layout on main before installing. Every skill uses the same path shape, `skills/<name>/SKILL.md`:

```bash
for p in skills/motion-art-direction/SKILL.md \
         skills/animation-principles/SKILL.md \
         skills/shot-composition/SKILL.md \
         skills/after-effects/SKILL.md \
         skills/remotion-video/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/iart-ai/motion-design-skills/main/$p"
done
```

All five return 200, and the same path resolves for the other four (beat-sync-editing, logo-animation, color-motion, motion-background). Read the `SKILL.md` of the skill you intend to rely on before granting anything broad: it is short, and it tells you exactly what the skill will produce.

After install, each skill should appear in your agent's skills directory under its own folder name, matching the `name` field in its frontmatter. If you install through the skills CLI without flags it prompts before writing, which doubles as a check on what the index resolves.

For rendered output, the repository's own verify loop is the reference. `scripts/probe-mp4.sh out.mp4 1080x1920 30` prints the encoded file's real spec and exits non-zero when the resolution or frame rate is off, which is the only check that catches an export that silently fell back to the wrong codec.

## Security

skills.sh verdicts were not sampled for this fire, so every cell below reads Not checked; open the security pages on skills.sh for these listings before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| motion-art-direction | Not checked | Not checked | Not checked |
| animation-principles | Not checked | Not checked | Not checked |
| shot-composition | Not checked | Not checked | Not checked |
| after-effects | Not checked | Not checked | Not checked |

What the content itself asks for is worth reading before install. Eight of the nine skills are knowledge and code snippets: they return expressions, palettes, compositions and checklists, and they write files only where your agent writes them anyway. `remotion-video` is the one that pulls in a runtime, a Remotion project and npm dependencies, and then renders through headless Chrome, so review what it installs into a project. `after-effects` produces ExtendScript, which executes inside After Effects with whatever access that application has, so read any supplied `.jsx` before running it.

Nothing in the skill text documents credential handling or an outbound API call, which is a statement about the content and not an audit of it. The install commands write skill files into your project, so run them on a clean tree and read the diff.

## Limitations

- Snapshot data, verified 2026-10-27: 26,619 combined installs across 9 indexed listings; 167 GitHub stars; MIT; branch main. Counts drift over time.
- These are knowledge skills, not renderers. Nothing here produces a video by itself: `after-effects` needs the application, `remotion-video` needs a Node project with Remotion installed, and the `scripts/` helpers need `ffmpeg` and `ffprobe`.
- Every `SKILL.md` in the tree is version 0.1.0. The collection is new, the publisher ships it alongside a commercial product, and the install counts measure distribution rather than measured quality.
- The README closes with a funnel to the iart.ai agent product. The free layer you install here is the skill text, so expect the documentation to be written for people who may later buy the hosted tool.
- Coverage is one discipline. There is no general frontend, design system or accessibility guidance in this pack, only motion and the craft around it.
- All nine indexed listings have a matching directory in the current `skills/` tree, so there is no index versus tree drift to work around on this pack.

## Related

- [Diagram Design - Editorial HTML and SVG Diagrams](/hermes/skills/catalog/diagram-design-setup)
- [Hypit - AI Video Clone Production Setup](/hermes/skills/catalog/hypit-skills-setup)
- [Anatomy Skill - Isometric SVG Explainer Setup](/hermes/skills/catalog/anatomy-skill-setup)
- [Markdown Viewer Skills - Diagrams, Charts and Cards Setup](/hermes/skills/catalog/markdown-viewer-skills-setup)

## Pro Tips

- Install `animation-principles` on its own first. It is the only skill in the pack that pays for its context on every project where anything moves, and its output feeds the rest.
- Pair a principle skill with one engine skill rather than installing all nine. Timing advice plus a renderer is a working setup; nine overlapping skills compete for the same task.
- The numbers live one level down. Read the `references/` folder of whichever skill you depend on, because the `SKILL.md` routes and the reference holds the full recipe. `after-effects` ships five reference files, `animation-principles` three.
- Wire `scripts/probe-mp4.sh` into CI if you render in a pipeline. Asserting resolution and frame rate on the encoded file catches the export regression that a successful render command hides.
- If the deliverable is platform specific, check the sibling packs in the publisher's collection before installing this one: TikTok, YouTube, ecommerce, ads, explainer, map, WebGL and Manim variants exist, and each installs independently.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
