---
title: "Alibaba Cloud Core Skills - Model Studio Setup"
description: "cinience/alicloud-skills: 6.3K combined installs across 20 listings for Qwen and Wan model APIs, OSS, ECS, log query and KMS"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/alicloud-core-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-10"
tags: ["hermes skill", "agent skill", "skill setup", "alibaba cloud", "model studio", "qwen", "dashscope"]
---

# Alibaba Cloud Core Skills - Setup Guide

**Source:** [cinience/alicloud-skills](https://www.skills.sh/cinience/alicloud-skills) via skills.sh - 6.3K combined installs across 20 indexed listings (6,261 exact); first seen 2026-11-10 (Nov 10, 2026 sweep)
**GitHub:** 397 stars, MIT license, `main` branch, last pushed 2026-08-11, 188 `SKILL.md` files under a `skills/<category>/<product>/<name>/` tree, with a `tests/` directory holding a smoke test per product area
**Category:** Cloud platform: Model Studio and DashScope models, object storage, compute, log service, key management and API discovery
**Quality Tier:** 🟠 Community with one failure - twenty listings sampled, one Agent Trust Hub failure and one warning, four Snyk warnings, and half the rendered index is smoke tests rather than product skills.

This is the broadest Alibaba Cloud skill set on skills.sh, and it is a different source from the AIOps collection already in this catalog. The AIOps set covers operating Alibaba Cloud resources; this one covers using Alibaba Cloud products, with a strong centre of gravity on Model Studio. The README describes the collection as core AI agent skills across product lines including Model Studio, OSS and ECS, and its index is generated from the `SKILL.md` files themselves so the English, Simplified Chinese and Traditional Chinese READMEs stay in step.

The model coverage is the reason this set exists. DashScope skills cover Qwen image generation and editing, Qwen VL image understanding, Qwen TTS and voice cloning, and Wan video generation including reference-to-video. Each skill documents the request and response mapping for its model family, the parameters that matter, and the async job pattern the video APIs use. Alongside the models are platform skills for object storage, ECS, VPC, log service queries, key management and product API discovery.

One property of the rendered index needs stating before anything else. Ten of the twenty listings are `-test` skills: minimal smoke tests whose descriptions all begin "Minimal ... smoke test". They exist so an operator can prove credentials and endpoints work before running a real skill, which is a sensible design and a poor thing to count as product coverage.

## Installation

The README's recommended install takes everything at once:

```bash
npx skills add cinience/alicloud-skills --all -y --force
```

It notes that if a selection prompt still appears, pressing `a` selects all and Enter submits.

Credentials come from environment variables, and the README is explicit that a RAM user or role with least privilege should be used rather than a root account:

```bash
export ALIBABACLOUD_ACCESS_KEY_ID="your-ak"
export ALIBABACLOUD_ACCESS_KEY_SECRET="your-sk"
export ALIBABACLOUD_REGION_ID="cn-beijing"
export DASHSCOPE_API_KEY="your-dashscope-api-key"
```

The `ALIBABACLOUD_*` prefix is the documented default. The README notes that runtime scripts also accept the legacy `ALIBABA_CLOUD_*` and `ALICLOUD_*` aliases, which matters if you already have older exports in a shell profile. An STS session token is supported through `ALIBABACLOUD_SECURITY_TOKEN`.

If you prefer a file, the README documents `~/.alibabacloud/credentials` with an ini block holding the key pair and an optional `dashscope_api_key`, and environment variables take precedence over it. The DashScope key is separate from the AccessKey pair, and the model skills need it while the platform skills do not.

Installing 188 skills at once is a lot of context for an agent. The selective form is worth knowing:

```bash
npx skills add cinience/alicloud-skills --skill aliyun-qwen-image
```

Note the naming asymmetry that will waste time otherwise: the skills.sh listings are named `alicloud-ai-image-qwen-image` while the directories and skill names are `aliyun-qwen-image`. Select by directory name, read by listing name.

## What It Provides

Nine listings clear the 300-install threshold:

| Skill | Installs | Use For |
|---|---|---|
| alicloud-ai-audio-tts-voice-clone | 396 | Voice cloning with Model Studio Qwen TTS VC models, then reusing the returned voice id in later synthesis calls. |
| alicloud-ai-image-qwen-image | 365 | Image generation through the DashScope SDK with the Qwen Image family, including prompt, size, seed and reference image mapping. |
| alicloud-observability-sls-log-query | 340 | Log queries in Alibaba Cloud Log Service using query and analysis syntax, for time-bounded error investigation. |
| alicloud-ai-multimodal-qwen-vl | 335 | Image understanding with Qwen VL models, mapping image inputs and structured outputs. |
| alicloud-ai-image-qwen-image-edit | 335 | Image editing with the Qwen Image Edit family: inpaint, replace, style transfer and local edits. |
| alicloud-ai-audio-tts | 314 | Speech synthesis with Qwen TTS models, including voice selection and audio format options. |
| alicloud-ai-video-wan-video | 307 | Video generation with Wan models through DashScope, including text-to-video and image-to-video with duration, fps and size. |
| alicloud-ai-audio-tts-voice-clone-test | 304 | Smoke test that proves a voice-clone call works end to end before a real cloning workflow is written. |
| alicloud-ai-multimodal-qwen-vl-test | 301 | Smoke test for image understanding, validating credentials and endpoint before the full VL skill is used. |

The remaining 11 indexed listings range from 295 to 299 installs, and all eleven are smoke tests: `alicloud-ai-video-wan-r2v-test` (299), `alicloud-ai-video-wan-video-test` (299), `alicloud-database-rds-supabase-test` (298), `alicloud-data-lake-dlf-next-test` (297), `alicloud-ai-entry-modelstudio-matrix-test` (297), `alicloud-storage-oss-ossutil-test` (297), `alicloud-ai-entry-modelstudio-test` (296), `alicloud-compute-ecs-test` (296), `alicloud-security-kms-test` (295), `alicloud-platform-openapi-product-api-discovery-test` (295) and `alicloud-ai-image-qwen-image-edit-test` (295).

Read the table with the smoke tests included and the pattern is clear. Seven real skills and thirteen smoke tests occupy the rendered index, and the install counts barely distinguish them. The smoke tests are useful and they are not what a guide should be measured on, which is why the tier note leads with the failure rather than the number.

The real skills cluster around Model Studio: two image skills, one video skill, one vision skill, two audio skills, plus log query. Everything else Alibaba Cloud offers is represented in the tree but not in the rendered slice.

## Why This Matters for Hermes Agents

Model access is the part of a cloud platform an agent touches directly, and DashScope is a different API shape from the OpenAI-compatible endpoints most agents know. A skill that documents `image.generate` request and response mapping, including which of `prompt`, `negative_prompt`, `size`, `seed` and `reference_image` each model family accepts, is the difference between an agent that generates the image you asked for and one that retries with invented parameters.

The video skills matter for a separate reason. Wan's video APIs are asynchronous: submit a job, poll, then fetch the result, with parameters that differ between text-to-video and image-to-video variants. An agent that treats video generation as a synchronous call will look like it is working and return nothing.

The smoke tests are the third useful part, and they are the part most guides would skip. Every platform integration failure looks the same from the outside: empty result, plausible narrative. A thirty-line smoke test that proves credentials, region and endpoint before the real workflow starts converts that into a specific error.

The caution is scope. These skills assume the model is hosted on Alibaba Cloud and speak to DashScope. If your workloads run against another provider, the request shapes here do not transfer, and the collection has nothing to offer beyond the general platform skills.

## Usage

| You say | What happens |
|---|---|
| "Generate a product image from this description" | Qwen image generation maps the prompt, size and seed to an `image.generate` call and returns the file |
| "Edit this photo to change the background" | Qwen Image Edit runs an inpaint or local-edit request that preserves the subject while replacing the region |
| "Make a 4 second clip from this still" | Wan video runs the image-to-video variant as an async job, then polls and returns the file rather than blocking |
| "What is in this image?" | Qwen VL describes the image and returns structured output where the skill defines one |
| "Why did our service throw 500s at 3am?" | Log service query runs a time-bounded query with analysis aggregation over the error status |
| "Prove our API key works before we build anything" | The matching smoke test validates auth, region reachability and one read-only call in a single run |
| "Clone this voice and read this script" | Voice clone creates the voice from sample audio and returns an id that the TTS skill uses for synthesis |

## Verification

Each listing resolves to a raw `SKILL.md` in its category tree, and the directory name is the Aliyun name rather than the skills.sh listing name. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/cinience/alicloud-skills/main/skills/ai/image/aliyun-qwen-image/SKILL.md | head -5
```

It should open with frontmatter holding `name: aliyun-qwen-image` and a description beginning `Use when generating images with Model Studio DashScope SDK`, then the delimiter and the instruction body. The tree is three levels deep on the AI skills and shallower elsewhere, so resolve the path from the tree rather than assuming a shape.

Credentials can be checked independently of any skill:

```bash
python3 -c "import os; print('ak' if os.getenv('ALIBABACLOUD_ACCESS_KEY_ID') else 'no ak', 'dashscope' if os.getenv('DASHSCOPE_API_KEY') else 'no dashscope')"
```

If the second value reads `no dashscope`, the image, video and audio skills have nothing to call even though the platform skills will still work.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-10) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| alicloud-ai-audio-tts-voice-clone | Pass | Pass | Pass |
| alicloud-ai-image-qwen-image | Pass | Pass | Warn |
| alicloud-observability-sls-log-query | Pass | Pass | Pass |
| alicloud-ai-multimodal-qwen-vl | Pass | Pass | Warn |
| alicloud-ai-image-qwen-image-edit | Pass | Pass | Pass |
| alicloud-ai-audio-tts | Warn | Pass | Pass |
| alicloud-ai-video-wan-video | Pass | Pass | Warn |
| alicloud-ai-audio-tts-voice-clone-test | Pass | Pass | Pass |
| alicloud-ai-multimodal-qwen-vl-test | Pass | Pass | Pass |
| alicloud-ai-video-wan-r2v-test | Pass | Pass | Warn |
| alicloud-ai-video-wan-video-test | Pass | Pass | Pass |
| alicloud-database-rds-supabase-test | Pass | Pass | Pass |
| alicloud-data-lake-dlf-next-test | Pass | Pass | Pass |
| alicloud-ai-entry-modelstudio-matrix-test | Pass | Pass | Pass |
| alicloud-storage-oss-ossutil-test | Pass | Pass | Pass |
| alicloud-ai-entry-modelstudio-test | Fail | Pass | Pass |
| alicloud-compute-ecs-test | Pass | Pass | Pass |
| alicloud-security-kms-test | Pass | Pass | Pass |
| alicloud-platform-openapi-product-api-discovery-test | Pass | Pass | Pass |
| alicloud-ai-image-qwen-image-edit-test | Pass | Pass | Pass |

Socket passes all 20. Agent Trust Hub fails `alicloud-ai-entry-modelstudio-test` and warns on `alicloud-ai-audio-tts`. Snyk warns on four. The failure on a test skill is the least damaging place for one to land, but it is a failure and the tier reflects it.

The property that matters most here is credential scope, and the README states it better than the scanners can: use a RAM user or role with least privilege, and never embed AccessKeys in code or CLI arguments. An AccessKey pair in this collection reaches ECS, OSS, KMS and the model APIs, which is most of an account. The DashScope key is narrower and separate, so keep the two in different places and grant platform access only to sessions that need it.

Prompt and data egress is the second property. Image, vision and video calls send your content to Alibaba Cloud, and `aliyun-qwen-vl` in particular takes whatever image you hand it. Decide before the session whether that content is allowed to leave the machine.

## Limitations

- Snapshot data, verified 2026-11-10: 6,261 combined installs across 20 indexed listings; 397 GitHub stars; MIT license; last pushed 2026-08-11. Counts drift over time.
- The source page reports a much larger total than the 20 rendered rows sum to, consistent with the 20-listing cap on the source page rather than an uncounted skill.
- Half the rendered index is smoke tests. They are genuinely useful and they inflate apparent breadth, so judge this collection by the seven product skills rather than the twenty listings.
- The repository was last pushed on 2026-08-11, three months before this snapshot, while the model families it documents turn over faster than that. Check the model names in a skill against the current DashScope catalogue before building on them.
- Listing names and directory names do not match (`alicloud-ai-image-qwen-image` versus `aliyun-qwen-image`), and a selective install by listing name will not find the skill.
- This is a third-party collection, not an Alibaba-maintained one. It is one of four Alibaba Cloud skill sets in this catalog, each from a different source, and the overlap between them is real rather than documented.

## Related

- [Alibaba Cloud AIOps Skills - 270-Skill Cloud Operations Suite Setup](/hermes/skills/catalog/alibaba-cloud-aiops-skills-setup)
- [QianWen AI Skills - Alibaba Qwen Multimodal Suite Setup](/hermes/skills/catalog/qianwen-ai-setup)
- [ModelStudio Skills - Alibaba Video and Data Tools](/hermes/skills/catalog/modelstudio-skills-setup)

## Pro Tips

- Run a smoke test before the first real call. Credentials, region and endpoint fail in the same silent way, and one test skill separates the three.
- Install selectively rather than with `--all`. At 188 skills the whole collection is a large fraction of an agent's context for what is usually one model family.
- Keep the DashScope key and the AccessKey pair separate, and only export the platform credentials in sessions that need ECS, OSS or KMS.
- Read the model names in the skill before trusting them. A skill written in August that names a snapshot model can still describe a request shape that has moved.
- Start from the listing name and install by directory name. The mapping is not obvious and a failed install reads like a missing skill rather than a naming mismatch.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
