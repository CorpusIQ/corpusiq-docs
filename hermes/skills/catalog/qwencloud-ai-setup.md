---
title: "QwenCloud AI Skills - Multimodal Suite Setup"
description: "qwencloud/qwencloud-ai: 15.1K combined installs. Ten Qwen skills for text, vision, image, video, speech and account billing."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/qwencloud-ai-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "qwen", "multimodal", "alibaba cloud"]
---

# QwenCloud AI Skills - Setup Guide

**Source:** [qwencloud/qwencloud-ai](https://www.skills.sh/qwencloud/qwencloud-ai) via skills.sh - 15.1K combined installs across 10 indexed listings; first seen 2026-11-01 (morning sweep)

**GitHub:** [qwencloud/qwencloud-ai](https://github.com/qwencloud/qwencloud-ai) - 44 stars, Apache-2.0, branch main, last pushed 2026-09-21; 10 `SKILL.md` files spread across eight category folders under `skills/`, each skill carrying its own `scripts/` folder and a `references/` folder of curl fallbacks and prompt guides

**Category:** Multimodal model access for agents: text, vision, image, video, speech and account operations

**Quality Tier:** 🟡 Yellow - the sampled listings are not clean: Socket returns Warn on qwencloud-vision and Snyk returns Warn with code W012 on qwencloud-image-generation, which matters more than usual because these skills ship executable Python rather than instructions alone

The repository's own one-line pitch is "fold QwenCloud's AI skills into your agent, just talk", and the skill set is organised exactly along that line: one skill per modality, plus the administrative skills that a paid API needs to be usable. Text, vision, image generation, video generation and text to speech cover the model calls. `qwencloud-model-selector` sits above them as an advisor, `qwencloud-ops-auth` handles credentials, and `qwencloud-usage` and `qwencloud-payment` read the account through the QwenCloud CLI. `qwencloud-update-check` is the pack's own housekeeping skill and is called by the other nine.

The design decision that shows up in every SKILL.md body is a key-type split. Standard pay-as-you-go keys (`sk-...`) work with either the bundled scripts or curl. Token Plan keys (`sk-sp-...`) are routed to a separate endpoint and must go through the Python scripts, never curl. Coding Plan keys share the `sk-sp-` prefix but cannot be used for direct API calls at all, and the scripts detect the prefix at startup and fail accordingly. Each skill also repeats the same credential rule: never print a key, report only "set" or "not set", and write a placeholder `.env` rather than asking the user to paste a secret into the conversation.

## Installation

The README documents a one-line install and requires Node.js 18 or newer:

```bash
npx skills add qwencloud/qwencloud-ai
```

When prompted, press `a` to select all skills, then Enter. The README also documents a non-interactive form and an agent-driven form, both of which skip the picker:

```bash
npx skills add qwencloud/qwencloud-ai -y
```

After installation the README points at `qwencloud-ops-auth` to walk through API key setup, which is the correct order: the execution skills fail on a missing key, and the auth skill is the one that knows about the placeholder `.env` convention.

Two runtime dependencies sit outside the skills CLI. The bundled scripts need Python 3.9 or newer; `tts_cosyvoice.py` additionally needs the `dashscope` SDK, which the other scripts do not. The account skills are CLI wrappers rather than HTTP calls: `qwencloud-usage` and `qwencloud-payment` need the QwenCloud CLI (version 1.3.0 or newer, installed with `npm install -g @qwencloud/qwencloud-cli`, Node 18 or newer) and an authenticated session, and `qwencloud-model-selector` needs the same CLI only for live model and account queries, not for its advisory path.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| qwencloud-vision | 1,811 | Image and video understanding: description, OCR, chart and table reading, multi-image comparison, and QVQ visual reasoning. |
| qwencloud-audio-tts | 1,678 | Text to speech through Qwen TTS and CosyVoice, including voice selection and instruction-driven delivery. |
| qwencloud-image-generation | 1,666 | Text to image and image editing with Wan and Qwen Image models: style transfer, subject consistency, multi-image composition, text rendering. |
| qwencloud-update-check | 1,648 | Version check against the upstream repository, rate limited to once every 24 hours and called by the other nine skills. |
| qwencloud-text | 1,643 | Chat, code generation and function calling through the OpenAI-compatible endpoint, including third-party models hosted on QwenCloud. |
| qwencloud-model-selector | 1,631 | Model and parameter advice, pricing and capability comparison, with a fast lookup path for the execution skills. |
| qwencloud-video-generation | 1,617 | Asynchronous text to video, image to video, first and last frame, and VACE video editing with Wan models. |
| qwencloud-ops-auth | 1,615 | API key and endpoint configuration, including the Token Plan and Coding Plan distinctions and the credential priority chain. |
| qwencloud-usage | 1,564 | Account auth, usage, billing, free tier quota, subscriptions, seats and call-log queries through the QwenCloud CLI. |
| qwencloud-payment | 247 | Payment method status, card binding and spending limit, with explicit confirmation before the browser handoff. |

The index and the tree agree here: ten listings, ten directories, so there is no snapshot artefact to discount. The one figure worth knowing is the spread. Nine skills sit between 1,564 and 1,811 installs, and `qwencloud-payment` trails at 247, which reads as a later addition that most installs have not picked up.

## Why This Matters for Hermes Agents

An agent that can write code does not automatically know which endpoint, which model id and which key type to use, and the failure mode is a 401 or a hallucinated model name rather than a clean error. This pack moves that knowledge into the repo: model ids come from a catalogue the skill is told not to guess beyond, request shapes come from per-modality scripts, and the key-type routing happens before the call instead of after three failed retries.

The modality split is also a context decision. Loading a 2,000-line document that covers text, images, video and billing puts four unrelated schemas in front of the model at once. Ten smaller skills let an operator load the one that matches the task, and `qwencloud-model-selector` exists specifically so an execution skill can resolve a model without pulling in the full catalogue itself.

The asynchronous parts are where the scripts earn their place. Video generation is submit, poll, download, with per-second billing, and the SKILL.md is explicit that duration is fixed at five seconds for the first-and-last-frame mode and that every other value fails. That is the kind of parameter an agent gets wrong from memory and gets right from a bundled script.

The account skills are the operator-facing half. Usage, billing, quota, seats and call logs arrive as structured output with a documented result contract that distinguishes `success`, `partial`, `empty`, `confirmation_required` and `error`, and the skill forbids reporting a partial page as complete. For an agent summarising spend, that rule is the difference between a useful answer and a confident wrong one.

The trade-off is vendor gravity. Everything here points at QwenCloud endpoints, model catalogues are fetched from a QwenCloud CDN, and the payment and usage skills only work with the vendor CLI. It is a coherent single-provider pack, not a portable abstraction layer, so it belongs in a profile that has deliberately chosen that provider.

## Usage

| You say | What happens |
|---|---|
| "Read this screenshot and give me the table as CSV" | `qwencloud-vision` runs its OCR path, returns the extracted table, and points at the chart and table reading guidance if the layout is ambiguous. |
| "Why does my QwenCloud key return a 401" | `qwencloud-ops-auth` detects the key type by prefix without printing the key, and names the cause: a Coding Plan key cannot be used for direct API calls. |
| "Which model is cheapest for summarising 10,000 short documents" | `qwencloud-model-selector` compares the catalogue on price and capability, then attaches the mandatory cost-estimate disclaimer rather than promising a bill. |
| "Turn this product image into a five second video" | `qwencloud-video-generation` submits asynchronously, polls until completion, and refuses any duration other than five seconds for the first-and-last-frame mode. |
| "Make a voiceover of this paragraph in a warm voice" | `qwencloud-audio-tts` selects a TTS model, formats the text for speech, and writes the audio file. |
| "How much did I spend on image generation this month" | `qwencloud-usage` queries the billing and usage endpoints through the CLI, marks the answer `partial` if pagination is unfinished, and never converts the returned currency. |
| "Am I running the latest version of these skills" | `qwencloud-update-check` compares the local `version.json` against the upstream release, with a 24 hour rate limit stored in `.agents/state.json`. |

## Verification

The raw path for the entry skill returned HTTP 200 on branch main when this guide was written on 2026-11-01:

```bash
curl -sL -o /dev/null -w "%{http_code} qwencloud-vision\n" \
  https://raw.githubusercontent.com/qwencloud/qwencloud-ai/main/skills/vision/qwencloud-vision/SKILL.md
```

Expect `200`. After a shallow clone, confirm that all ten skills arrived, since the category folders and the skill folders are not the same number:

```bash
git clone --depth 1 https://github.com/qwencloud/qwencloud-ai.git /tmp/qwencloud-ai
ls /tmp/qwencloud-ai/skills | wc -l
find /tmp/qwencloud-ai/skills -name SKILL.md | wc -l
```

The first count should be 8: audio, image, models, ops, text, usage, video and vision. The second should be 10, because `ops` holds three skills and the other seven hold one each. Also check that each skill directory carries `scripts/` and `references/` next to its `SKILL.md`; if a copy flattened the skills into bare markdown files, every execution path silently falls back to curl and the Token Plan routes stop working.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-01) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| qwencloud-vision | Pass | Warn | Pass |
| qwencloud-audio-tts | Pass | Pass | Pass |
| qwencloud-image-generation | Pass | Pass | Warn |

This is not a markdown-only pack, so the verdicts carry more weight than they do for instruction-only skill sets. Every execution skill ships runnable Python that reads the network, uploads local files to temporary object storage for the image and video paths, and streams responses back. `qwencloud-update-check` makes an outbound request to GitHub and writes a timestamp into `.agents/state.json`, and the model selector fetches catalogues from `alioth-intl.alicdn.com`. Nothing in the sampled code was flagged as malicious, but a Warn on Socket for `qwencloud-vision` and a Snyk Warn with code W012 on `qwencloud-image-generation` are the reason this guide is Yellow rather than Green, and both are worth reading on the security pages rather than taking from this table.

The credential handling is the part the pack does well, and it is worth holding the skills to their own text. Each SKILL.md states that a key must never be printed in plaintext, that detection reports only status, that `.env` should be written with a placeholder rather than a real value, and that the agent should not ask the user to paste a key into the chat. Those are exactly the behaviours a scanner flags when they are absent, so if you modify a skill, keep them.

Three operational points follow. The scripts accept `QWENCLOUD_API_KEY`, then `QWEN_API_KEY`, then `DASHSCOPE_API_KEY`, in that order, so a leftover `DASHSCOPE_API_KEY` in the environment will silently win over the variable you thought you were using. The temporary upload bucket used by the image and video paths has a 48 hour lifetime unless a custom OSS bucket is configured, which is a data-retention decision rather than a security defect but should be a conscious one. And the payment skill opens a browser page rather than handling card data, which keeps card material out of the agent's context entirely; the SKILL.md requires explicit confirmation before that command runs, and it should stay that way.

## Limitations

- Snapshot data, verified 2026-11-01: 15,120 combined installs across 10 indexed listings; 44 GitHub stars; Apache-2.0; last pushed 2026-09-21. Counts drift over time.
- The index lists 10 skills and the tree holds 10 directories, so there is no index-versus-tree drift to discount here.
- The README's own highlight block still says "9 skills, one interface" while the tree ships 10 directories. `qwencloud-payment` is the extra one, and its 247 installs against roughly 1,600 for everything else is consistent with a recent addition.
- Nine of the ten skills are effectively tied between 1,564 and 1,811 installs, so ordering in the index says nothing about which skill is most useful.
- Most paths need a funded account. Token Plan keys only work through the bundled Python scripts, Coding Plan keys cannot make direct API calls at all, and curl is documented as pay-as-you-go only.
- The pack is tied to one vendor: QwenCloud endpoints, a QwenCloud CDN for model catalogues, and a QwenCloud CLI for usage and payment. The local `cdn/` copies are fallbacks and can lag the live catalogues.
- Last pushed 2026-09-21, about six weeks before this snapshot. The model catalogue is fetched at runtime, so model ids stay current, but the scripts and reference files are that old.

## Related

- [QianWen AI Skills - Alibaba Qwen Multimodal Suite Setup](/hermes/skills/catalog/qianwen-ai-setup)
- [MiniMax AI Skills - Official Dev & Document Suite Setup](/hermes/skills/catalog/minimax-ai-skills-setup)
- [Gemini Skills - Official Google AI Development Suite Setup](/hermes/skills/catalog/gemini-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Load `qwencloud-ops-auth` before anything else in a fresh profile. Almost every first-run failure is a key that is present but of the wrong type, and this skill is the only one that explains the three key families.
- Keep the key in the environment, not in the prompt. The scripts accept `QWENCLOUD_API_KEY` first and `DASHSCOPE_API_KEY` last, so set the specific one and unset the generic one if both exist.
- For Token Plan keys, use the Python scripts and skip the curl examples entirely. The curl path is documented as pay-as-you-go only, and mixing the two produces authentication errors that look like the key is invalid.
- Ask `qwencloud-model-selector` before a batch job rather than after. It is instructed not to invent model names, which is the failure mode that burns a large batch on the first call.
- Treat video as a polling job, not a request. Submit once, poll, download, and remember that first-and-last-frame mode is fixed at five seconds; retrying a failed submit with a different duration is the most common way to waste spend here.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
