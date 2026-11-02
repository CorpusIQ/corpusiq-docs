---
title: "Motion Graphics Skills - Launch Video Suite"
description: "charlie947/motion-graphics-skills: 28.5K combined installs. Fifteen Claude Code skills for launch films, animated charts, reels and 3D openers."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/motion-graphics-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "motion graphics", "video", "animation"]
---

# Motion Graphics Skills - Setup Guide

**Source:** [charlie947/motion-graphics-skills](https://www.skills.sh/charlie947/motion-graphics-skills) via skills.sh - 28.5K combined installs across 15 indexed listings; first seen 2026-11-02 (morning sweep)

**GitHub:** [charlie947/motion-graphics-skills](https://github.com/charlie947/motion-graphics-skills) - 524 stars, MIT with a `LICENSE` file in the root, branch main, last pushed 2026-10-11; 15 `SKILL.md` directories under `skills/`, one per skill, with `motion-effects` carrying a `references/` folder and `motion-prompt-writer` a single `CANON-FACTS.txt`

**Category:** Motion graphics for agents: storyboards, kinetic type, 3D scenes and rendered launch clips

**Quality Tier:** 🟢 Production - all five sampled listings pass Gen Agent Trust Hub, Socket and Snyk, the repository is MIT licensed, and what ships is Markdown plus one validation script

Charlie Hills publishes this pack as the working method behind his MarTech AI newsletter, and the README opens with the whole premise in one line: no After Effects, no video generator, Claude Code writes the animation as code, draws every frame and renders an MP4. The fifteen skills are Markdown instructions, so there is nothing to compile and no API key to hold. The one outside dependency is export: HyperFrames, or ffmpeg plus Chrome.

The pack is organised in the order a real job runs. `brand-intake` runs once and interviews you for five frames you like, then writes `brand.md` (who you are, what you sell, your assets) and `MOTION.md` (colours, type, timing, motion rules) plus a read-first rule in `CLAUDE.md`. Every other skill reads those two files before it draws anything. Planning skills turn a rough idea into a brief or an eight-part Motion prompt, launch skills build product films, explainers cover documentary, chart, milestone and effect formats, and the three promotion skills handle newsletter covers, edition promos and vertical exports.

## Installation

The README's one-liner installs all fifteen skills:

```bash
npx skills add charlie947/motion-graphics-skills
```

The README then says to open Claude Code, pick Opus 5.5 with `/model`, and run `brand-intake` first. Nothing in the repository mentions Hermes, but the skills are plain folders with a `SKILL.md`, so the same tree loads from a Hermes profile skills directory. The manual loop below is the README's own copy loop with the destination changed from `~/.claude/skills/` to a Hermes profile, and it keeps any skill folder you already have:

```bash
git clone https://github.com/charlie947/motion-graphics-skills.git
mkdir -p ~/.hermes/profiles/corpusiq/skills
for skill in motion-graphics-skills/skills/*; do
  [ -f "$skill/SKILL.md" ] || continue
  destination="$HOME/.hermes/profiles/corpusiq/skills/$(basename "$skill")"
  if [ -e "$destination" ]; then
    printf 'Preserved existing skill: %s\n' "$destination"
  else
    cp -R "$skill" "$destination"
  fi
done
```

Codex is a different destination: the README copies the same folders into `.agents/skills/` in the project root and tells you to check that the skills load from `.agents/skills/<name>/SKILL.md`. Claude Desktop takes one zipped skill folder at a time, for example `zip -r brand-intake.skill brand-intake` from inside `skills/`.

MP4 export is the one thing the pack does not build itself. The README says to add HyperFrames once, free and open source:

```bash
npx skills add heygen-com/hyperframes
```

Without it you get the HTML with `window.seek()` and the encode is still pending, unless ffmpeg and Chrome are on the machine. `loop-cover` additionally wants ffmpeg and Python 3 to measure its seam, and `reel-export` and `model-showdown` want ffmpeg plus ffprobe for stacking and checks.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| vox-explainer | 2,087 | A 30 to 60 second documentary explainer in code: torn paper, halftone texture, bold condensed type, motion on twos, and a source found for every fact before anything is drawn. |
| motion-effects | 2,079 | Any of 16 premium effects built in your own brand as one 8 second looping HTML file with `window.seek(seconds)` for frame-exact MP4 or GIF export: interfaces, data, type and systems. |
| reel-export | 2,033 | Turning a 16:9 or 4:5 video into a clean 1080 x 1920 Reel or TikTok: headline and logos inside the safe zone, H.264, yuv420p, bt709, a silent track when there is no sound, ffprobe before upload. |
| animated-chart | 2,019 | A looping chart for LinkedIn or a newsletter: bars that become a line, a number that counts up, a before and after, with every value kept exactly as you gave it. |
| title-sequence-3d | 1,986 | An 8 to 15 second cinematic opener in Three.js: a camera moving through a lit scene such as a rainy street with brand names as neon signs, then a title landing. |
| brand-intake | 1,986 | The setup step every other skill reads: a short interview plus reference frames becomes `brand.md` and `MOTION.md`, plus a rule in `CLAUDE.md` so both are read before anything animates. |
| launch-video | 1,980 | A 30 to 45 second product launch: one sentence split across scenes, real product screens with slow camera moves, a typed prompt, a proof beat and a call to action. |
| motion-brief-writer | 1,974 | A rough idea turned into a precise build brief in your brand, asking first for exact numbers, size and length, keeping real results apart from sample data and never inventing a figure. |
| apple-launch-film | 1,961 | An Apple-style Mac launch film in code: a thin menu bar, the black notch growing into widgets scene by scene, gradient wallpapers and one short caption per scene. |
| loop-cover | 1,915 | A newsletter or blog cover as a seamless 896 x 640 GIF, 180 frames at 20fps, only the element you name moving, with the seam measured rather than eyeballed. |
| milestone-reveal | 1,912 | A 12 second loop of thousands of points drifting like a night sky then pulling into your real follower, subscriber or revenue number, with a line drawn underneath. |
| newsletter-promo | 1,885 | A 12 to 20 second promo from one edition: a hook question, three proof frames from the edition, then the newsletter name and where to read it. |
| model-showdown | 1,883 | One brief given to three AI models, each first try kept and rendered the same way, stacked into a comparison video with model names and logos. |
| reference-to-motion | 1,451 | A reference video broken down for its moves and an optional look reference for its style, then a scene-by-scene Motion prompt for your own topic and brand. |
| motion-prompt-writer | 1,325 | A complete eight-part Claude Motion prompt (the bar, format, the one rule, look, motion, never, before you finish, the scene) from your brand plus one moment. |

No indexed listings fall below the threshold; all 15 appear above.

The tree matches the index exactly. Fifteen listings, fifteen `SKILL.md` directories, and each folder holds either nothing but its `SKILL.md` or one supporting file, so the count in the table is the count you install.

## Why This Matters for Hermes Agents

Motion graphics is where an agent improvises most convincingly: invented numbers on screen, brand colours guessed from a logo, a glow effect nobody asked for. This pack pushes the decisions into files a run can read. `brand.md` and `MOTION.md` are the identity, a brief or an eight-part Motion prompt is the spec, and the house rules are written down instead of left to the model: every name, date and number comes from a list you approved, logos and screenshots come from your files and are never redrawn from memory, and the first three seconds have to carry the hook.

The output format is the useful part for an agent. Most skills emit one HTML file with `window.seek(seconds)`, which means a frame is addressable, a render is repeatable, and an export is a function of a spec rather than a lucky ffmpeg chain. That is the same property that makes a render reviewable by a second pass: ask for one frame from the middle of every shot and check it for cut-off text, overlaps and wrong facts before encoding.

The cost model is flat. There is no API key, no subscription and no per-render charge in the free pack, so a cron job that builds a clip spends compute and nothing else. The only paid surfaces are opt in and external: HyperFrames for encoding, or ffmpeg on the machine, and an image model if a photoreal human face is genuinely needed, which the README names as the one honest limit.

The pack also states its own failure modes, which is what makes it usable unattended. Without `brand.md` a skill asks for hex codes and never calls the result on-brand, without ffmpeg the reel and showdown checks stay pending rather than passing silently, and without the free apple-design skill the Apple film still builds but its motion goes unchecked against Apple's rules.

## Usage

| You say | What happens |
|---|---|
| "Set up my brand for motion, here are five frames I like" | brand-intake interviews you for who you are, what you sell and which assets exist, then writes `brand.md` and `MOTION.md` and adds the read-first rule to `CLAUDE.md`. |
| "Make a launch video for my new cohort" | launch-video builds a 30 to 45 second film from one sentence split across scenes, with real product screens, a typed prompt, a proof beat and a call to action. |
| "Make a Vox-style video: why do we dream?" | vox-explainer finds a source for each fact, writes the script, adds a voice and renders a 30 to 60 second torn-paper explainer. |
| "Animate my Q3 chart, here are the numbers" | animated-chart loops bars into a line or counts a number up, and holds every value exactly as given rather than smoothing it. |
| "Celebrate 10,000 subscribers" | milestone-reveal drifts thousands of points like a night sky, pulls them into the real number, draws a line underneath and settles the label. |
| "Break down this reference and turn it into a Motion prompt" | reference-to-motion reads the video for its moves and an optional site or moodboard for the look, then writes a scene-by-scene Motion prompt for your topic. |
| "Make this a reel for Instagram" | reel-export reframes to 1080 x 1920, keeps headline and logos inside the safe zone, encodes H.264 with bt709 and runs an ffprobe check before you upload. |

## Verification

The raw paths below returned 200 on branch main when this guide was written on 2026-11-02. Probe before installing:

```bash
for p in brand-intake vox-explainer motion-effects reel-export; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/charlie947/motion-graphics-skills/main/skills/$p/SKILL.md"
done
```

After a clone, count the folders instead of trusting the index, and run the repository's own validator:

```bash
git clone --depth 1 https://github.com/charlie947/motion-graphics-skills.git /tmp/motion-graphics-skills
find /tmp/motion-graphics-skills/skills -name SKILL.md | wc -l
bash /tmp/motion-graphics-skills/validate-skills.sh
head -4 /tmp/motion-graphics-skills/skills/brand-intake/SKILL.md
```

The count should be 15. `validate-skills.sh` checks every skill's frontmatter, that the name matches its folder, the description length, the folder structure and the pack's house style across the skills, their reference files and the prompts folder, so a green run is the cheapest confirmation that the copy is intact. The `head` should print the `name:` and `description:` of `brand-intake`, which is what the agent routes on.

`/tmp/motion-graphics-skills/validate-skills.sh` resolves its own directory, so it runs from anywhere as long as the clone is intact.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| vox-explainer | Pass | Pass | Pass |
| animated-chart | Pass | Pass | Pass |
| motion-brief-writer | Pass | Pass | Pass |
| newsletter-promo | Pass | Pass | Pass |
| motion-prompt-writer | Pass | Pass | Pass |

All five sampled listings are Pass on all three auditors, and the sample covers the explainer, the chart, the brief writer, the promo and the prompt writer rather than only the setup skill.

What lands on disk is the smallest surface in this catalog. Twenty-two Markdown files, four PNGs, two GIFs, two zips in `downloads/`, and one shell script: `validate-skills.sh`, 208 lines, which reads files and prints a report. Twelve of the fifteen skill folders hold nothing but a `SKILL.md`, `motion-effects` adds a `references/` folder, and `motion-prompt-writer` adds one text file of canon facts. No skill ships an executable, nothing runs on clone, and no skill needs a network call or a key.

The two zips in `downloads/` and the GIFs in `assets/` are the only binary content, and they are documentation for the prompt writer and the readme demo. If you mirror this pack into a restricted profile, the whole thing is text.

## Limitations

- Snapshot data, verified 2026-11-02: 28,476 combined installs across 15 indexed listings; 524 GitHub stars; MIT; last pushed 2026-10-11. Counts drift over time.
- The GitHub repository description still says 13 skills, while the README badge, the skill table and the tree all ship 15. Read the tree, not the description.
- Encoding is not in the pack. MP4 export wants HyperFrames, or ffmpeg plus Chrome, `loop-cover` wants ffmpeg and Python 3 to measure its seam, and `reel-export` and `model-showdown` want ffmpeg plus ffprobe.
- `apple-launch-film` builds without the separate free `apple-design` skill, but its motion then goes unchecked against Apple's rules. `model-showdown` can only compare the models your own accounts can reach.
- The README names one honest limit: code draws motion, type and UI well, but a photoreal human face still needs an image model.
- Nothing in the repository mentions Hermes. Claude Code, Codex and Claude Desktop are the documented surfaces, and `brand-intake` writes its read-first rule into `CLAUDE.md`, so a Hermes run has to read `brand.md` and `MOTION.md` itself.

## Related

- [Animation Principles Skills - Motion Setup](/hermes/skills/catalog/dylantarre-animation-principles-setup)
- [Design Motion Principles Skill - Motion & Interaction Setup](/hermes/skills/catalog/design-motion-principles-skill-setup)
- [remotion-best-practices - Video Production Setup](/hermes/skills/catalog/remotion-best-practices-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `brand-intake` before anything else and give it real frames, not a description of your brand. Every other skill reads `brand.md` and `MOTION.md` first, and a thin pair produces work that looks like the tool rather than like you.
- Ask for a brief before asking for a video. `motion-brief-writer` and `motion-prompt-writer` turn one idea into a spec with exact numbers, timing and a self-check, and a spec is the difference between a render you can fix and one you re-roll.
- Render one frame from the middle of every shot and look at it. The pack's own house rule is to check for cut-off text, overlaps and wrong facts before export, and that check catches more than a preview ever does.
- Keep facts in a list you approved before the build starts. The banned-defaults list in the README (typewriter text, glow, bounce, gradients on text, purple-to-blue backgrounds) is worth reading once and then keeping out of every prompt.
- If a clip shows a product interface, feed it real components instead of letting the model draw buttons from memory. Spacing gets guessed otherwise, and guessed spacing is the tell that a launch film was generated.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
