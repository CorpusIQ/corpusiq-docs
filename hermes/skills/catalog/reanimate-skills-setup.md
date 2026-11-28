---
title: "Reanimate Skills - Animation Reverse Engineering Suite"
description: "niazmorshed2007/reanimate: 4.1K combined installs. Claude Code skill to reverse-engineer animations frame by frame and prove the copy moves the same."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/reanimate-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "animation", "motion capture", "reverse engineering"]
---

# Reanimate Skills - Setup Guide

**Source:** [niazmorshed2007/reanimate](https://www.skills.sh/niazmorshed2007/reanimate) via skills.sh - 4.1K combined installs across 2 indexed listings; first documented 2026-11-27 (evening sweep)

**GitHub:** [niazmorshed2007/reanimate](https://github.com/niazmorshed2007/reanimate) - 2,700 stars, MIT, branch main, last pushed 2026-10-31; the installable skill is `skills/reanimate/SKILL.md` with `references/` and `scripts/` beside it, while `site/` holds the live example gallery.

**Category:** Animation reverse engineering, frame-by-frame motion capture and clone verification for agent runtimes

**Quality Tier:** 🟡 Yellow - Socket warns on reanimate and Snyk warns on both sampled listings.

reanimate is a Claude Code skill by Niaz Morshed that reverse-engineers an animation from a live website URL, a screen recording, an mp4, mov, webm, gif or Lottie file, or a prototype export, rebuilds it in your own codebase, then records the copy the same way and compares the two frame by frame. The README describes the loop: record the reference in a headless browser at a fixed viewport and frame rate, turn the motion into a per-element spec, build it with what the project already uses (CSS, Framer Motion, GSAP, three.js), film the copy, and iterate until timing, easing and layout match.

The index tracks two listings: reanimate at 4,116 installs and motion-clone at 1, which has no SKILL.md in the current repo tree. The skill ships a TypeScript capture pipeline (capture.ts, compare.ts, easing.ts, gl.ts, sheet.ts) beside its SKILL.md, plus a demo site under site/ that runs cloned animations from vercel.com, stripe.com, clerk.com, resend.com and others live in the browser.

## Installation

The README installs through the skills CLI. It asks which agents to set up; add `-a claude-code` to skip the question:

```bash
npx skills add NiazMorshed2007/reanimate -g
```

Then in Claude Code, say what you want, where it is and where it should go:

```text
/reanimate the hero entrance on https://example.com, into components/Hero.tsx
```

The skill needs Bun 1.1 or later on macOS or Linux (Windows is untested). The first run installs a static ffmpeg into the skill's folder and Playwright Chromium into Playwright's usual cache, about 250 MB together, and no API keys are required. It has been tested with Claude Code; other agents that read SKILL.md can install it too.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| reanimate | 4,116 | Clone a section, widget, page or animation from a live URL, video, gif or Lottie frame by frame, then verify the rebuilt copy matches the reference in timing, easing, sequence and layout. |
| motion-clone | 1 | Indexed listing with no SKILL.md in the current repo tree; not described in the README. |

Both indexed listings appear above.

## Why This Matters for Hermes Agents

reanimate is a clear example of a closed-loop agent workflow: the skill never accepts "looks right" as done. It films the reference, rebuilds it, films the copy the same way, and compares the two, then fixes the biggest difference and repeats until the numbers match. A builder wiring agent runtimes should copy that structure, because it turns a vague aesthetic goal into a measurable pass or fail.

The capture pipeline is what makes the loop work. It records in a headless browser at a fixed viewport and frame rate, and for canvas, WebGL and WebGPU it traces the GPU calls and scene graphs, running the page on a virtual clock with seeded randomness so two captures of the same animation come out byte-identical. That determinism is the difference between "close enough" and a clone that can actually be verified against the original.

The build step respects the host project, writing the animation with whatever is already there rather than imposing a new library. The README is equally explicit about the boundary: it clones what you point it at while leaving you responsible for whether you may use the copied fonts, images and code. That ownership posture is worth carrying into any clone-style workflow.

## Usage

| You say | What happens |
|---|---|
| "/reanimate the hero entrance on https://example.com, into components/Hero.tsx" | Records the reference, rebuilds it in Hero.tsx and iterates until timing, easing and layout match. |
| "/reanimate this loader, 0:03 to 0:05 of ~/Downloads/loader.mov" | Captures the three-second span of the recording and clones the loader from those frames. |
| "/reanimate the card hover in this gif, match it exactly" | Clones the hover at pixel-perfect level, matching fonts, colours and spacing within 2 percent pixel mismatch. |
| "/reanimate the logo marquee from https://example.com, with our logos and pause on hover" | Clones the marquee motion and layers your logos plus a pause-on-hover on top. |
| "Clone that WebGL globe from the site" | Uses --gl to trace shaders, uniforms and the scene graph, then rebuilds and compares channel by channel. |
| "It still looks off, keep going" | Films the copy again, fixes the biggest difference and repeats, usually 2 to 5 rounds. |

## Verification

Review the skill before installing by fetching its SKILL.md directly. The skill directory is the only installable part, so the raw path is straightforward:

```bash
curl -sL https://raw.githubusercontent.com/niazmorshed2007/reanimate/main/skills/reanimate/SKILL.md
```

After a clone, confirm the skill layout and the capture scripts:

```bash
git clone --depth 1 https://github.com/niazmorshed2007/reanimate.git /tmp/reanimate
ls /tmp/reanimate/skills/reanimate/
ls /tmp/reanimate/skills/reanimate/scripts/
```

The first listing should show SKILL.md alongside references/ and scripts/; the second should show capture.ts, compare.ts, easing.ts, frames.ts, gl.ts and sheet.ts.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| reanimate | Pass | Warn | Warn |
| motion-clone | Pass | Pass | Warn |

This guide is Yellow because Socket warns on reanimate and Snyk warns on both sampled listings; no listing fails. The Gen Agent Trust Hub passes both. The repository is mostly Markdown skill files plus a TypeScript capture pipeline under skills/reanimate/scripts/, and the first run downloads a static ffmpeg and Playwright Chromium, so the Warn flags are worth reading on the skills.sh security pages before installing into a production profile.

## Limitations

- Snapshot data, verified 2026-11-27: 4,117 combined installs across 2 indexed listings; 2,700 GitHub stars; MIT; last pushed 2026-10-31. Counts drift over time.
- motion-clone is an indexed listing with no SKILL.md in the current repo tree and no README description; its Use For cell above is name-level only.
- The skill needs Bun 1.1 or later on macOS or Linux; Windows is untested, and the first run downloads about 250 MB of ffmpeg and Playwright Chromium.
- Pages behind a login, YouTube and Loom cannot be recorded directly; hand the skill a screen recording instead.
- Physics springs are fitted from their overshoot and settle time, not read from the source, and worker clocks run in real time rather than on the virtual clock.
- It clones what you point it at; fonts, images and code from another site still belong to their owners, so confirm you may use what you copy.

## Related

- [iart JavaScript Animation Skills - Code-Drawn Motion](/hermes/skills/catalog/iart-javascript-animation-skills-setup)
- [Framer Motion Skills - React Animation Suite Setup](/hermes/skills/catalog/framer-motion-skills-setup)
- [Design Motion Principles Skill - Motion & Interaction Setup](/hermes/skills/catalog/design-motion-principles-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Point the skill at the exact span you want cloned (a section, a widget, a few seconds), because it clones what you point it at and pixel-level matching costs more rounds.
- Default is "moves the same"; say "match it exactly" only when you want fonts, colours and spacing too, since that raises the bar to under 2 percent pixel mismatch.
- Keep the original recording around so the skill can re-film and compare; the whole loop depends on filming both sides the same way.
- For canvas, WebGL or three.js work, use --gl and the virtual clock so captures are deterministic and comparable channel by channel.
- State the ownership boundary up front: the skill will copy fonts, images and code from the reference, so confirm you may use them before it runs.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
