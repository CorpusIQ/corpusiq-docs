---
title: "TikTok Video Skills - Short-Form Video Suite Setup"
description: "iart-ai/tiktok-video-skills: 9.9K combined installs. Four vertical video skills: retention hooks, karaoke captions, lower thirds and countdowns."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/tiktok-video-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "tiktok", "short-form video", "captions", "remotion"]
---

# TikTok Video Skills - Setup Guide

**Source:** [iart-ai/tiktok-video-skills](https://www.skills.sh/iart-ai/tiktok-video-skills) via skills.sh - 9.9K combined installs across 4 indexed listings; first documented 2026-11-02 (evening sweep)

**GitHub:** [iart-ai/tiktok-video-skills](https://github.com/iart-ai/tiktok-video-skills) - 20 stars, MIT license, branch main, last pushed 2026-06-22; four skill folders under `skills/`, each with its own `SKILL.md`, `README.md` and `references/`, plus a shared `scripts/` toolkit and a `.claude-plugin` marketplace manifest

**Category:** Vertical short-form video for agents: retention structure, word-timed captions, lower thirds and drift-free countdowns

**Quality Tier:** 🟢 Green - every sampled listing passes all three auditors and the repository is MIT licensed; the caveats are size, not safety: four skills, 20 stars, and one listing left unsampled

The repository comes from iart.ai, a studio that publishes an open-source collection of 14 video skill packs for coding agents, and this is the short-form pack. It is small and complete: four folders under `skills/`, 630 lines of `SKILL.md` across them, five reference pages, a `scripts/` folder of three bash helpers that close the verify loop, a `.claude-plugin` manifest for the Claude Code marketplace route, an MIT `LICENSE`, and a `showcase.gif` plus `showcase.html` for the preview.

The four skills cut short-form video into the pieces a build actually needs: the retention grammar (`short-form-video`), word-timed karaoke captions (`caption-animation`), name and role overlays (`lower-thirds`) and drift-free timers (`countdown-video`). All four are written against Remotion and share one house style. Motion is driven from `useCurrentFrame()`, never from `Date.now()`, `Math.random()` or a timer, so a render is deterministic; the deliverable is checked by rendering stills at named frames before spending an encode; and each skill ends with a "before you finish" checklist rather than a summary. The install counts sit between 2,154 and 2,961, a spread of 807, which reads like a pack install rather than four separate adoptions.

## Installation

The README documents two routes. The skills CLI one is the shortest:

```bash
npx skills add iart-ai/tiktok-video-skills
```

Claude Code can also take the repository as a plugin marketplace, which the README shows as two slash commands:

```bash
/plugin marketplace add iart-ai/tiktok-video-skills
/plugin install tiktok-video-skills
```

For a Hermes profile the manual copy is straightforward, because the four skills live in `skills/`:

```bash
git clone --depth 1 https://github.com/iart-ai/tiktok-video-skills.git /tmp/tiktok-video-skills
mkdir -p ~/.hermes/profiles/corpusiq/skills
cp -R /tmp/tiktok-video-skills/skills/. ~/.hermes/profiles/corpusiq/skills/
```

Copy the folder, not just `SKILL.md`. Each skill points at one or two reference pages, and those pages hold the runnable compositions the skills describe: a full `<Short>` with a frame-driven shot scheduler, a word-timed caption component with an SRT parser, a lower-third component with a roster batch script, a countdown with digit reels and a flip card.

The `scripts/` helpers are a separate install. `scripts/README.md` says to run them from the project where the deliverable lives, so copy that folder into the video project rather than into the skills directory:

```bash
cp -R /tmp/tiktok-video-skills/scripts ~/your-video-project/scripts
```

The heavy path assumes Remotion (`npx remotion still`, `npx remotion render`). The helpers add two system dependencies: `scripts/probe-mp4.sh` needs `ffprobe` from ffmpeg, and `scripts/seek-shot.sh` needs Playwright Chromium once via `npx playwright install chromium`. None of that is needed for the skills to load, only to close the verify loop.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| short-form-video | 2,961 | The hook, retention and loop grammar for 9:16 video: one idea per short, an open loop set in the first three seconds and closed last, a visual interrupt every 2 to 4 seconds, uneven cut intervals, seamless first-to-last-frame loops, the 900x1400 center safe box, and a platform-by-platform view-through threshold. Also the entry point that hands captions to the `caption-animation` skill rather than re-implementing them. |
| caption-animation | 2,558 | Word-timed captions from a Whisper or SRT transcript: per-word spring pop driven off each token's own `startMs`, a single accent color on the active word, `createTikTokStyleCaptions()` paging at 1 to 4 words, the type spec (bold sans, 56 to 80px, 2 to 6px stroke), safe-area placement, and the burn-in versus sidecar SRT/VTT decision. |
| lower-thirds | 2,185 | Name and role overlays that read as produced rather than pasted: staggered enter (bar, then name, then role), a 3 to 5 second dwell, an exit faster than the enter, a 1.6x minimum size contrast between name and role, left anchoring inside title-safe, and a roster map that renders one design across a list of speakers. |
| countdown-video | 2,154 | Frame-accurate timers for "starting soon" screens, launches and sales: remaining time recomputed from the frame or `performance.now()` on every tick instead of a drifting `setInterval`, `mm:ss` and `dd:hh:mm:ss` formatting with `tabular-nums`, digit reel and flip-card transitions, and a background loop whose period divides the timeline. |

All 4 indexed listings clear the threshold and appear in the table above.

The shared `scripts/` toolkit is what makes the suite testable: `seek-shot.sh` freezes a standalone HTML page at `?t=N` and screenshots each moment, `contact-sheet.sh` tiles a start, mid and end frame into one image, and `probe-mp4.sh` reads the encoded file's real resolution, codec, fps and duration and asserts them against a contract such as `1080x1920 30`. Every skill's "deliver and verify" section calls these by name.

## Why This Matters for Hermes Agents

Agents produce short-form video that looks like a template: a slow fade-in, evenly spaced cuts, a hook that arrives at second four, and captions split evenly across a line. The suite attacks that directly. It states the metric the work is judged on (roughly 70 percent average view-through, with per-platform numbers), then explains why a metronome of cuts reads as boredom and why a fade up from black is the single worst opening frame.

The second thing it fixes is determinism. An agent that drives motion from `setInterval` or `Math.random()` produces a render that cannot be reproduced or checked, and an agent that fakes caption timing by splitting a line's duration evenly produces drift you can see on the first replay. These skills make frame-driven animation a checked rule with a test attached (the still at frame N must show a specific word or digit), which is the difference between a claim and a verification.

The third is the hand-off structure. `short-form-video` explicitly refuses to re-implement captions and points at `caption-animation`; `lower-thirds` and `countdown-video` reuse the same Remotion contract. For a builder wiring skills into a pipeline that means one composition convention across four tasks, so a caption style fixed in one skill does not have to be re-fixed in another.

Finally, the verify loop is cheap. Stills cost seconds and an encode costs minutes, so an agent that renders three named frames and looks at them catches framing, safe-area and timing faults before it burns a render. The packaged helpers turn that from advice into a command.

## Usage

| You say | What happens |
|---|---|
| "Make a 9:16 TikTok template that hooks in the first second" | Drafts the hook line and commits to one of the four hook archetypes, puts the hook on screen as text by frame 1 with no fade-up, and budgets the body while keeping the hook at roughly one second. |
| "This Reel dies at second four, fix the pacing" | Adds a visual interrupt every 2 to 4 seconds with deliberately uneven intervals, replaces the flat middle with a punch-in zoom or a b-roll insert, and re-checks the retention arc beat by beat. |
| "Turn this voiceover transcript into word-by-word captions" | Normalizes the transcript to `text`, `startMs` and `endMs` tokens, pages them at 1 to 4 words, springs each word in from 60 percent scale, and highlights only the active word in one accent color. |
| "Build a 5-minute starting-soon countdown that ends exactly on zero" | Computes remaining time from the frame each render, sets `durationInFrames` to the duration times fps, formats `mm:ss`, and asserts the digit value at a sampled frame before encoding. |
| "Add a name and role lower third, and do the whole speaker list" | Animates bar, name and role in that order with a 3 to 5 second dwell, then makes name, role and theme props so the same design renders once per roster row. |
| "Check the safe areas before we render" | Confirms hook, subject and captions sit inside the center 900x1400 box and that the bottom 320px, top 120px and right 120px stay clear of platform UI. |
| "Is the loop seam clean?" | Compares the first and last rendered stills for matching composition, position and color, and re-renders the seam frame instead of assuming it matches. |

## Verification

The raw path below returned 200 on branch main on 2026-11-02:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/iart-ai/tiktok-video-skills/main/skills/short-form-video/SKILL.md
```

After a clone, confirm that all four skills and their references arrived, because a partial copy is the common failure:

```bash
git clone --depth 1 https://github.com/iart-ai/tiktok-video-skills.git /tmp/tiktok-video-skills
find /tmp/tiktok-video-skills -name SKILL.md | wc -l
find /tmp/tiktok-video-skills -path '*references*' -name '*.md' | wc -l
head -3 /tmp/tiktok-video-skills/skills/short-form-video/SKILL.md
```

The first count should print 4, the second 5, and `head` should show `name: short-form-video` and the description the runtime routes on. On the installed copy:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -E 'short-form-video|caption-animation|lower-thirds|countdown-video'
grep -c 'references/' ~/.hermes/profiles/corpusiq/skills/short-form-video/SKILL.md
```

Four directories and a non-zero pointer count mean the skills can still reach their detail.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| short-form-video | Pass | Pass | Pass |
| caption-animation | Pass | Pass | Pass |
| lower-thirds | Pass | Pass | Pass |

The suite is documentation plus three small bash helpers. There is no install script, no hook, no dependency manifest at the repository root and nothing that executes when a skill loads. The three helpers in `scripts/` are readable POSIX `bash`: one calls `ffprobe`, one calls `ffmpeg`, one drives a headless browser through Playwright to screenshot a page you name. Read them before you run them, because they are outside the scope of the skill audit even though they ship in the same tree.

The licence is MIT with an iart.ai copyright line, so copying the skill text into a private profile, or adapting the reference compositions into a product, has an explicit grant. The `countdown-video` listing was not sampled by the auditors, so its verdict is unknown rather than clean; it carries the same code shape as the other three, one `SKILL.md` and two reference pages.

The one thing worth thinking about is the domain. These skills teach a paid studio's craft, and the README links its commercial product at iart.ai with UTM parameters; the most recent commit before this snapshot is one that added UTM tracking to every iart.ai link in the repository. That is a marketing choice, not a payload, but it does mean any agent reading the README will surface a commercial link to a user.

## Limitations

- Snapshot data, verified 2026-11-02: 9,858 combined installs across 4 indexed listings; 20 GitHub stars; MIT; last pushed 2026-06-22. Counts drift over time.
- Only three of the four listings were sampled by the auditors. `countdown-video` has no recorded verdict.
- The heavy path assumes Remotion. The suite targets it explicitly (`npx remotion still`, `npx remotion render`, `<Composition>` with a zod schema), so a project on After Effects, Manim or plain HTML has to translate the guidance rather than apply it. The `scripts/README.md` does map a light HTML tier and a Manim tier, but only the Remotion path has full skill coverage.
- The packaged helpers need system dependencies that the skills do not install for you: `ffprobe` and `ffmpeg` for the probe and contact sheet, Playwright Chromium for the seek helper.
- 20 stars and one publisher. The repository is part of a 14-pack collection, so it is maintained as a series rather than as a standalone library, and there is no changelog or support statement in the tree.
- Every skill is versioned `0.1.0` with no compatibility table, so the guidance is a snapshot of one house style rather than a versioned contract.

## Related

- [remotion-best-practices - Video Production Setup](/hermes/skills/catalog/remotion-best-practices-setup)
- [Apidojo Social Media Skills - X/Instagram/TikTok Scraper Suite Setup](/hermes/skills/catalog/apidojo-social-media-skills-setup)
- [Video Agent Skills - Video Production for Agents](/hermes/skills/catalog/video-agent-skills-setup)
- [Claude Ads - Paid Media Skill Suite Setup](/hermes/skills/catalog/claude-ads-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Ask for one skill at a time and let the hand-offs do their job. `short-form-video` deliberately does not implement caption animation; a request that mixes hook structure with caption styling should load both skills rather than forcing one to cover the other.
- Render stills before encoding, always. Three stills at the hook, a mid-body frame and the last frame cost seconds; the encode costs minutes and tells you nothing about the loop seam.
- Run `scripts/probe-mp4.sh out.mp4 1080x1920 30` instead of trusting the render dialog. It reads the encoded file, so it catches a composition that silently rendered at the wrong resolution or frame rate.
- When a short feels flat, check the cut intervals before touching the content. The skill's rule is uneven intervals and an interrupt every 2 to 4 seconds; a metronome is usually the fault.
- For a roster of lower thirds, verify one row with stills before rendering all of them. A layout overflow caught once is cheap; caught after a 40-name batch render it is not.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
