---
title: "QianWen AI Skills - Alibaba Qwen Multimodal Suite Setup"
description: "QianWen AI Skills: 56.2K combined installs. Eleven skills wrap the Alibaba Qwen API for text, vision, image, video, speech, billing and auth."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/qianwen-ai-setup/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skill setup", "qwen", "multimodal", "image generation", "text to speech"]
---

# QianWen AI Skills - Setup Guide

**Source:** [qianwen-ai/qianwen-ai](https://www.skills.sh/qianwen-ai/qianwen-ai) via skills.sh - 56.2K combined installs across 11 indexed listings; snapshot 2026-10-28 (Oct 28 evening sweep)

**GitHub:** [QianWen-AI/qianwen-ai](https://github.com/QianWen-AI/qianwen-ai) - 115 stars, Apache-2.0, branch main, last pushed 2026-10-10; 11 `SKILL.md` directories under `skills/<category>/<name>/`, one per indexed listing, with no listing that lacks a directory

**Category:** Multimodal AI API skills: text, vision, media generation, account and billing operations

**Quality Tier:** 🟡 Beta - maintained by the QianWen-AI organization and install heavy, 115 GitHub stars, 11 indexed listings matched one to one by 11 `SKILL.md` directories, and two of the six sampled skills carry an auditor warning

QianWen AI Skills is a skill pack from the QianWen-AI organization that wraps the Alibaba Qwen platform in eleven agent skills. One install covers text generation and function calling, vision and OCR, image generation and editing, video generation and editing, text to speech, model selection with pricing, API key management, usage and billing queries, recharge, skill discovery, and a version checker that the other ten skills call. The repository is Apache-2.0, installs through the skills.sh CLI, and ships one `SKILL.md` per skill with a Chinese primary README and an English mirror.

The install numbers are high against the repository's footprint: 56.2K combined installs across eleven indexed listings against 115 GitHub stars, with the smallest listing at 2,718. It is a client for a commercial API rather than a free tool, so every skill spends against your own QianWen account, and two of the eleven reach money and credentials directly. The README advertises ten skills while the repository tree and the install index both carry eleven; the extra one is the update checker, which the README's skill table omits.

## Installation

The README requires Node.js 18 or newer. One command installs every skill, and the picker wants `a` for all of them followed by Enter:

```bash
npx skills add QianWen-AI/qianwen-ai
```

The README's other documented route hands the job to the agent. This is the English mirror of that prompt, trimmed to the steps that matter:

```text
Please install QianWen AI Skills for me:
1. Check if Node.js is installed, install it if not
2. Run: npx skills add QianWen-AI/qianwen-ai
3. If a skill selection prompt appears, select all skills and confirm
4. Once installed, list what skills I got and walk me through what I can do
```

There is no plugin marketplace or MCP route in the README, so the skills.sh CLI is the only documented installer. For a Hermes profile, the manual copy keeps the category folders out of the skills directory, since skills live at `skills/<category>/<name>/SKILL.md`:

```bash
git clone https://github.com/QianWen-AI/qianwen-ai.git
cp -R qianwen-ai/skills/*/qianwen-* ~/.hermes/profiles/corpusiq/skills/
```

Credentials come after the skills. `qianwen-ops-auth` loads a key from the environment first (`DASHSCOPE_API_KEY`, with `QIANWEN_API_KEY` as an alias that wins when both are set), then from a `.env` file in the working directory or the repository root. Keys are created in the QianWen console at `https://platform.qianwenai.com/home/api-keys`.

The account skills carry a second dependency that the README does not mention. `qianwen-usage`, `qianwen-model-selector` and `qianwen-payment` all depend on the QianWen CLI, which is a separate global install and reports its version with `qianwen version`:

```bash
npm install -g @qianwenai/qianwen-cli
```

The usage skill pins a CLI baseline of 1.3.0 and tells the agent not to call the `billing` and `subscription` groups below that version.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| qianwen-update-check | 5769 | Comparing the installed pack version in `version.json` against the GitHub copy with semver, returning `has_update`, and rate limiting the check to once every 24 hours through `.agents/state.json`. |
| qianwen-image-generation | 5754 | Text to image and image editing on Wan and Qwen Image models: style transfer, subject consistency, text rendering inside images, and interleaved text and image output. |
| qianwen-vision | 5743 | Reading images and video with Qwen vision models: OCR, chart and table extraction, screenshot understanding, multi-image comparison, and visual reasoning. |
| qianwen-audio-tts | 5692 | Turning text into speech with Qwen TTS voices for narration, voiceover and audiobook batches. Speech recognition is explicitly out of scope. |
| qianwen-text | 5623 | Text generation, chat, code writing, reasoning and function calling on Qwen text models. |
| qianwen-video-generation | 5591 | Text to video, image to video, first and last frame, reference-based role play, and VACE video editing on Wan and HappyHorse models. |
| qianwen-model-selector | 5568 | Advisory model choice: mapping a task and a budget to a Qwen model and parameters, with pricing and cost estimation for pay-as-you-go keys. |
| qianwen-usage | 5528 | Account and spend queries through the `qianwen` CLI: auth status, free tier quota, usage summary and per-model breakdown, billing history, call logs, subscriptions and team seats. |
| qianwen-ops-auth | 5519 | API key and endpoint setup: the credential priority chain, key type detection by prefix, 401 troubleshooting, and non-plaintext key handling. |
| qianwen-find-skills | 2724 | Discovering, comparing and optionally installing published Agent Skills from QianWen SkillHubs. |
| qianwen-payment | 2718 | Balance checks, fixed-amount recharge through Alipay, recharge history, recharge page guidance, and Token Plan quotes and purchases. |

All 11 indexed listings clear the 500-install threshold and appear in the table above; the tail below the threshold is empty.

## Why This Matters for Hermes Agents

Most agent work is multimodal in practice: a screenshot to read, a PDF to summarize, a voice line to synthesize, a poster to render. Each of those normally drags in a separate provider, key, SDK and quota story. This pack puts all of them behind one `DASHSCOPE_API_KEY` on Alibaba's Qwen and Wan models, so a Hermes profile gets text, vision, image, video and speech from a single credential and a single failure mode to debug.

Routing is the second gain. Every `SKILL.md` frontmatter carries a TRIGGER and DO NOT TRIGGER block that names its neighbour skill, so an agent holding both `qianwen-vision` and `qianwen-image-generation` will not confuse reading a chart with drawing one. The blocks also state the negative case: text to speech refuses speech recognition, image generation refuses video, and vision refuses generation.

The account skills are what make unattended runs defensible. `qianwen-model-selector` prices a pay-as-you-go call before it happens, `qianwen-usage` returns free tier quota and per-model spend as JSON, and `qianwen-ops-auth` reports key state without ever printing the key. The corollary is to install the whole pack rather than a subset, because the update checker is a shared dependency that the other ten skills delegate to.

## Usage

| You say | What happens |
|---|---|
| "Summarize every PDF in this folder with the cheapest text model" | model-selector picks a Qwen text model that fits the budget, then text writes and runs the batch call over the folder. |
| "Extract the text from these 200 screenshots into one spreadsheet" | vision runs OCR through Qwen vision models, handles the multi-image comparison, and returns rows ready to write out. |
| "Make 20 product posters: ink wash, flat and 3D" | image-generation builds a Wan or Qwen Image batch, one call per style, with subject consistency across the set. |
| "Turn each of these five product shots into a short showcase clip" | video-generation runs image to video on Wan or HappyHorse, one call per asset, with an optional first and last frame. |
| "Read these 30 chapters aloud in a warm female voice" | audio-tts batches Qwen TTS synthesis per chapter and reports which files landed. |
| "How much free quota is left on qwen3.6-plus, and what did last month cost" | usage runs `qianwen usage free-tier` and the billing summary with `--format json`, then reports the parsed numbers rather than a guess. |
| "The account is out of balance, top it up so the batch can finish" | payment reads the balance snapshot, confirms the amount with you, and returns the Alipay recharge route from the CLI rather than constructing a URL. |

## Verification

All eleven raw paths below returned 200 on branch `main` when this guide was written on 2026-10-28. The layout is one directory per skill under a category folder, so probe before installing a subset:

```bash
for p in ops/qianwen-update-check image/qianwen-image-generation vision/qianwen-vision \
         audio/qianwen-audio-tts text/qianwen-text video/qianwen-video-generation \
         models/qianwen-model-selector usage/qianwen-usage ops/qianwen-ops-auth \
         meta/qianwen-find-skills ops/qianwen-payment; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/QianWen-AI/qianwen-ai/main/skills/$p/SKILL.md"
done
```

Read these two before installing, because one decides how the key is handled and the other decides how money is reported:

- https://raw.githubusercontent.com/QianWen-AI/qianwen-ai/main/skills/ops/qianwen-ops-auth/SKILL.md
- https://raw.githubusercontent.com/QianWen-AI/qianwen-ai/main/skills/usage/qianwen-usage/SKILL.md

After install, confirm what actually landed. Expect eleven directories and a frontmatter name that matches each directory:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -c '^qianwen-'
head -5 ~/.hermes/profiles/corpusiq/skills/qianwen-text/SKILL.md
```

For the account side, `qianwen auth status --format json` should return an authentication payload rather than a 401, and `qianwen version` should be 1.3.0 or newer before any billing command is trusted. The update checker can be run on demand with `python3 <skill>/scripts/check_update.py --print-response`.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| qianwen-update-check | Pass | Pass | Warn W011/W012 |
| qianwen-image-generation | Pass | Pass | Pass |
| qianwen-vision | Pass | Pass | Pass |
| qianwen-audio-tts | Pass | Pass | Pass |
| qianwen-text | Warn | Pass | Pass |
| qianwen-video-generation | Pass | Pass | Pass |

Two of the six sampled listings carry a warning: `qianwen-update-check` on Snyk with codes W011 and W012, and `qianwen-text` on Gen Agent Trust Hub. The other four pass all three auditors, and this snapshot carries no verdict for the remaining five listings.

The credential rule is written into the pack rather than left to the agent. `qianwen-ops-auth` forbids asking for a key in chat, forbids printing one, and allows writing a real key into `.env` only when the user insists; its status checks report set or not set, valid or invalid, and an HTTP status code, never the value. Keep that behaviour when you wire the pack into a profile: the key belongs in the environment, not in a conversation or a log.

Two skills change state on the account. `qianwen-payment` can create a recharge order and buy Token Plan credits, which is real money through Alipay, and `qianwen-usage` can log out and revoke the session server side. Both skills require confirmation before acting, so leave those two out of unattended cron runs and keep them in an interactive session where a human confirms the amount.

What the install itself runs is small by count: the clone holds 125 files, one `SKILL.md` per skill plus a `scripts/` folder that is mostly Python helpers calling the Qwen API, and Node preflight and polling modules for the payment routes. None of it executes on clone. The risk sits in what the skills then do, which is call a paid API with your key and, for the account skills, operate the QianWen CLI against your balance.

## Limitations

- Snapshot data, verified 2026-10-28: 56229 combined installs across 11 indexed listings; 115 GitHub stars; Apache-2.0 license; last pushed 2026-10-10. Counts drift over time.
- The primary README.md is Chinese and the English mirror is README_en.md. Skill frontmatter and `SKILL.md` bodies are English, so an agent reads them fine while a human reviewing the repository may not.
- The README advertises 10 skills while the tree and the install index carry 11. The extra is `qianwen-update-check`, a version checker that the other ten call, and the README's skill table does not list it. No indexed listing lacks a directory.
- `qianwen-payment` and `qianwen-ops-auth` touch billing and credentials: recharge runs through Alipay, Token Plan purchases spend credits, and ops-auth reads keys from the environment and can write them into a `.env` file.
- Every skill bills your own QianWen account. The README states that costs are charged to your account, that generated content is not guaranteed accurate, and that the project offers no availability or stability guarantee.
- Node.js 18 or newer is required for the install, and `qianwen-payment` states 18.18 or newer for its own routes. The account skills also need the separate `@qianwenai/qianwen-cli` global package at 1.3.0 or newer, the update checker needs Python 3.9 plus curl, and nothing here works offline.

## Related

- [Gemini Skills - Official Google AI Development Suite Setup](/hermes/skills/catalog/gemini-skills-setup)
- [Skills Collective AI Media - Image & Video Gen Setup](/hermes/skills/catalog/skills-collective-ai-media-setup)
- [Remotion Best Practices - Video Production Setup](/hermes/skills/catalog/remotion-best-practices-setup)

## Pro Tips

- Install all eleven. The update checker is what the other ten call before they run, and a partial install leaves them looking for a skill that is not there.
- Put `DASHSCOPE_API_KEY` in the profile environment rather than in a message. Set one variable only: `QIANWEN_API_KEY` takes priority when both are present, which is a quiet way to run on a key you forgot you exported.
- Know which key type you hold. `sk-sp-` is a Token Plan key with a limited model catalog that must be given an exact supported model, while `sk-ws-` is a standard pay-as-you-go key with the full catalog and per-token billing.
- Ask for the price before the batch: model-selector estimates pay-as-you-go cost, and `qianwen usage free-tier` says whether quota covers the job before anything is spent.
- Use `--format json` on every `qianwen` command and parse that. The `table` format carries ANSI codes and Unicode box drawing, and parsing it will break.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
