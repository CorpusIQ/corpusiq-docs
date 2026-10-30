---
title: "Bailian CLI - Alibaba Model Studio Agent Skills Setup"
description: "modelstudioai/cli: 59.8K combined installs. Alibaba's official bl CLI ships nine Qwen agent skills for media, fine-tuning, sandbox and managed agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/modelstudio-cli-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "alibaba model studio", "qwen", "cli"]
---

# Bailian CLI - Setup Guide

**Source:** [modelstudioai/cli](https://www.skills.sh/modelstudioai/cli) via skills.sh - 59.8K combined installs across 9 indexed listings; first seen 2026-10-29 (evening sweep)

**GitHub:** [modelstudioai/cli](https://github.com/modelstudioai/cli) - 366 stars, Apache-2.0 License, branch main, last pushed 2026-10-30 (a China-time commit stamp, one day ahead of this US-evening sweep); nine skill directories under `skills/<name>/SKILL.md`, each with generated `reference/` pages, plus one downstream plugin skill at `packages/bailian-kb-dsh/skills/bailian-kb/SKILL.md`, inside a pnpm monorepo of `packages/core`, `packages/runtime`, `packages/commands`, `packages/cli` and `packages/kscli`

**Category:** AI platform CLI and model, media, training and agent tooling for Alibaba Cloud Model Studio (DashScope)

**Quality Tier:** 🟡 Beta - first-party Apache-2.0 CLI from Alibaba Cloud Model Studio with a real monorepo and generated docs, but two Snyk Warns among the six sampled listings (bailian-managed-agent, bailian-knowledge)

modelstudioai/cli is Alibaba Cloud's official command line interface for Model Studio, the platform behind Qwen models and the DashScope API. It installs a single binary, `bl` (also exposed as `bailian`), that covers text, image, video and speech generation, asset understanding, fine-tuning and deployment, batch inference, sandbox instances, cloud-side managed agents, knowledge bases, personal memory, web search and account operations. The license is Apache-2.0 and the repository is a layered pnpm monorepo: `packages/core` for pure logic, `packages/runtime` for the CLI framework, `packages/commands` for command implementations, and `packages/cli` and `packages/kscli` as the two product entrypoints.

The nine indexed skills are the agent-facing layer, and they are mostly generated rather than hand-written. `tools/generate-reference.ts` walks `packages/cli/src/commands.ts` and writes each `skills/<skill>/reference/` page by command owner, while `tools/sync-skill-metadata.ts` copies `metadata.version` out of `packages/cli/package.json`; both run from `pnpm run sync:skill-assets` and a pre-commit hook. Each `SKILL.md` frontmatter carries version 2.7.2 and a `requires.bins: ["bl"]` line, and each business skill opens by telling the agent to read `../bailian-protocol/SKILL.md` first. That shared protocol skill is where the family keeps its rules: provider selection and consent classes, version pre-check, call attribution on every agent command, high-risk confirmation, and error reporting.

## Installation

The repository README documents the CLI, not the skills, so the install instructions to follow are in `INSTALL.md`, which is written for an agent to execute step by step. It prefers npm on Node 18.17.0 or newer, then the CLI's own registry installer:

```bash
npm install -g bailian-cli
bl skill init
```

`bl skill init` fetches the registry index and installs every skill whose name starts with `bailian-`, which is the whole family including the shared protocol. Confirm both halves before going further:

```bash
bl --version
bl skill list
```

If `bl skill init` fails, `INSTALL.md` permits exactly one fallback, and only when both `node -v` and `git --version` succeed. The skills CLI version is pinned there, with the reason given in the file: 1.5.18 is the last release that still supports Node 18.

```bash
npx skills@1.5.18 add modelstudioai/cli --all -g
```

That `--all` form is the only one this repository documents. A per-skill `npx skills add modelstudioai/cli --skill bailian-gen` is the generic skills CLI convention rather than an instruction from this repo; for a subset, the supported route is the CLI's own flag, and the protocol has to be included or the sibling skills cannot read it:

```bash
bl skill add --name bailian-protocol,bailian-gen
```

Hosts without Node use the binary installer, which runs `bl skill init` itself once the binary is in place:

```bash
curl -fsSL https://bailian.aliyun.com/cli/install.sh | bash
```

Then authenticate, because every API-facing command needs it. `INSTALL.md` is explicit that the interactive console login belongs in the user's own terminal, and that only masked fields should ever be quoted back:

```bash
bl auth status --output json
bl auth login --console
bl auth login --console --console-site international
```

Subscription plans such as Token Plan cannot use `--console` and pass a key instead:

```bash
bl auth login --api-key <API_KEY>
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| bailian-cli | 18,816 | The hub skill for the `bl` binary: app calls with `bl app`, model catalog and search with `bl model list` and `bl model search`, SDK snippets with `bl model code`, usage and quota, workspace and MCP marketplace, file upload, pipelines, Batch inference and ParseX parsing, auth and config, and the skill manager itself (`bl skill add`, `list`, `update`, `remove`). |
| bailian-gen | 9,234 | Full-modality media: `bl image`, `bl video`, `bl speech`, `bl omni` and `bl vision describe`, covering text to image, image editing, reference to video, speech synthesis and transcription, and image or video understanding. Images and audio return synchronously to local files while video is an async task taken back with `--download` or polling. |
| bailian-protocol | 9,222 | The shared execution protocol every other skill reads before running anything: consent classes for personal, knowledge and media operations, version pre-check, the four `BAILIAN_CALLER_*` attribution variables on every agent command, high-risk confirmation including exit code 7, and error reporting rules. |
| bailian-finetune | 9,209 | The training pipeline as ordered commands: `bl dataset validate` against the chatml, dpo, cpt, tts or image schema, upload for a file id, `bl finetune create`, watch, checkpoint selection, export, optional compression, then `bl deploy` for a dedicated endpoint. Writes are previewed with `--dry-run` first. |
| bailian-managed-agent | 9,204 | Declarative infrastructure for cloud-side agents: `agents.yaml` as the only source of truth, validate, `bl managed-agent plan` to show the pending diff, scoped apply and destroy, plus deployments with schedules and environment variables, sessions, events, files, webhooks and memory stores. Destructive paths are gated behind an explicit confirmation instead of an automatic `--yes`. |
| bailian-web-search | 3,170 | Model-aware routing for web search inside a `bl` workflow: a Token Plan profile or a `token-plan` base URL host goes to model-native search through `bl text chat --api responses`, everything else goes to `bl search web` over Bailian MCP, with one fallback to model-native search if MCP auth or transport fails. |
| bailian-sandbox | 855 | Sandbox instance and template lifecycle over an E2B-compatible REST control plane: create, list, get, connect, pause, resume and delete instances, list built-in base images offline, upload template mount files, and manage templates with build status. Connection output feeds WebShell, browser-use automation or VNC. |

The remaining 2 indexed listings range from 28 to 103 installs.

## Why This Matters for Hermes Agents

Most agent tool integrations pay for their breadth twice: once in the JSON schemas that sit in context on every turn, and once in docs that drift from the released flags. This family takes the opposite approach. A `SKILL.md` holds intent routing and hard rules, the flags and examples live in generated `reference/` pages that the agent opens only when it needs them, and both are regenerated from the same command registry the binary ships, so `bl <command> --help` and the skill text are supposed to agree. For a Hermes profile that already runs a coding agent against a cloud API, that structure is worth more than any single command in it.

The protocol skill is the other half of the design that matters at scale. One file owns consent, version pre-check and call attribution, and every business skill defers to it by relative path rather than restating the rules, which is why installing a subset without `bailian-protocol` breaks the family rather than degrading it. Attribution is concrete: each agent command is wrapped with `BAILIAN_CALLER_TYPE`, `BAILIAN_CALLER_NAME`, `BAILIAN_SKILL_NAME` and `BAILIAN_SKILL_VERSION`, set per command rather than exported into the shell, so a shared host can tell which agent and which skill spent the tokens.

The install path is also Hermes-aware in a way that most skills in this catalog are not. `bl skill init` writes a canonical copy under `~/.bailian/skills/<name>/` with a `skill-lock.json` record, then links each skill into every supported agent directory it detects, and Hermes Agent is one of the detected targets, resolved from `HERMES_HOME`. That means the same install can populate a specific Hermes profile and the lock file keeps a hash per skill, so `bl skill update` upgrades content instead of leaving two competing copies on disk.

The limits are honest and mostly geographic. The README states that app orchestration, native MCP setup, training and deployment, account operations and plan onboarding are currently limited to China site accounts, so a non-China account gets the model, media, search and parsing commands without the agent platform. The skills themselves are written mostly in Chinese with English mixed in, which works for Qwen-family intent matching but is worth testing against how your own router decides to load a skill.

## Usage

| You say | What happens |
|---|---|
| "Generate a picture of a cat in a spacesuit on Mars, then turn it into a video" | bailian-gen runs `bl image generate --prompt ... --out-dir ./out/` for the still, writes it to disk, then submits the video as an async task and takes the result back with `--download` or by polling. |
| "Which model should I use for image understanding and support chat?" | bailian-cli calls `bl advisor recommend` for intent to candidate recall and ranking, then `bl model list --model <family> --enrich` for parameters, and `bl model code --sdk dashscope` when you want the SDK snippet. |
| "Fine-tune a model on this JSONL file" | bailian-finetune validates with `bl dataset validate --file train.jsonl --schema chatml`, uploads for a file id, creates the job with `bl finetune create`, watches progress, exports the result and optionally deploys an endpoint. |
| "Deploy a short-film director agent to Model Studio" | bailian-managed-agent writes `agents.yaml`, runs `bl managed-agent plan` and shows you the diff, and only applies the scoped change after you confirm. It is instructed never to add `--yes` on its own. |
| "Search the web for the newest Model Studio features" | bailian-web-search classifies the connection first: a Token Plan profile uses model-native search through `bl text chat --api responses`, otherwise it runs `bl search web --query ...`, and it falls back once if MCP auth or transport fails. |
| "Give me a sandbox with a browser I can watch" | bailian-sandbox creates the instance, then `bl sandbox connect` returns connection information for WebShell, browser-use automation or the VNC view. |
| "How much free quota do I have left?" | bailian-cli asks which product you mean if it is unclear, then runs `bl usage` or `bl quota`, with `--output json` and `NO_COLOR=1` for machine-readable output. |

## Verification

The raw paths below returned 200 on branch main when this guide was written on 2026-10-29:

```bash
curl -sL -o /dev/null -w "%{http_code} bailian-cli\n" \
  https://raw.githubusercontent.com/modelstudioai/cli/main/skills/bailian-cli/SKILL.md
curl -sL -o /dev/null -w "%{http_code} protocol\n" \
  https://raw.githubusercontent.com/modelstudioai/cli/main/skills/bailian-protocol/SKILL.md
curl -sL -o /dev/null -w "%{http_code} bailian-kb\n" \
  https://raw.githubusercontent.com/modelstudioai/cli/main/packages/bailian-kb-dsh/skills/bailian-kb/SKILL.md
```

Expect `200` on each. After install, confirm the canonical copy and the lock file, then ask the CLI to diff local state against the registry:

```bash
ls ~/.bailian/skills
head -20 ~/.bailian/skills/skill-lock.json
bl skill list --output json
```

`bl skill list` reports one status per skill: `installed`, `outdated`, `not-installed`, `missing` when the lock has a skill whose directory was deleted, and `untracked` when a directory exists that the CLI does not manage. A healthy run of `bl skill init` leaves nine `bailian-*` entries and no `untracked` ones.

The installer fans each skill out to every supported agent it detects, and Hermes Agent is on that list through `getHermesHome`, which reads `HERMES_HOME` first. Export the profile before installing if you want the copy there rather than in the default home:

```bash
export HERMES_HOME=~/.hermes/profiles/corpusiq
bl skill init
ls "$HERMES_HOME/skills/bailian-cli/SKILL.md"
```

To review a skill before installing it, read the raw file directly and check that the frontmatter still declares the binary dependency and a version:

```bash
curl -sL https://raw.githubusercontent.com/modelstudioai/cli/main/skills/bailian-cli/SKILL.md | head -30
```

A good copy shows `name: bailian-cli`, `metadata.version: "2.7.2"` and `requires.bins: ["bl"]`, followed by the instruction to read `../bailian-protocol/SKILL.md` and to stop if that file is missing.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| bailian-cli | Pass | Pass | Pass |
| bailian-gen | Pass | Pass | Pass |
| bailian-protocol | Pass | Pass | Pass |
| bailian-finetune | Pass | Pass | Pass |
| bailian-managed-agent | Pass | Pass | Warn |
| bailian-knowledge | Pass | Pass | Warn |

No sampled listing fails. Two of the six carry a Snyk Warn, on the two skills that drive the highest-impact cloud writes: bailian-managed-agent, which can apply and destroy agent deployments, and bailian-knowledge, which uploads personal documents to a managed retrieval service. In practice a warn means read the finding before you let an unattended agent use those two, because the risk is not in the markdown but in the command the markdown authorizes. The pack records verdicts without finding text, so open the Snyk entry on each skills.sh page rather than guessing at the rule.

Two structural points belong in the same review. The Linux and macOS route pipes a remote script into bash (`curl -fsSL https://bailian.aliyun.com/cli/install.sh | bash`), and `INSTALL.md` itself notes the installer is not maintained in the repository, so prefer the npm route on hosts you care about. The other is the registry: `bl skill init` downloads content-addressed tar packages from an index and then links them into agent skill directories, which is a supply chain you are trusting on every `bl skill update`. The skills themselves are markdown and reference pages; the protocol skill's own rules are the strongest built-in control here, since it forbids writing live API keys into skills, logs or chat, and tells the agent to quote only masked fields from `bl auth status --output json`.

## Limitations

- Snapshot data, verified 2026-10-29: 59,841 combined installs across 9 indexed listings; 366 GitHub stars; Apache-2.0; last pushed 2026-10-30. Counts drift over time.
- The index and the tree disagree. skills.sh lists nine skills, all of which exist under `skills/`, while the pack records 12 in-tree skill directories; the difference includes the downstream plugin skill at `packages/bailian-kb-dsh/skills/bailian-kb/SKILL.md`, which is not an indexed listing and is a knowledge-base management tool for a different host rather than a `bl` skill.
- Large parts of the suite are China site only. The README states that app orchestration, native MCP setup, training and deployment, account operations and plan onboarding are not yet supported for international or global site accounts, which removes several of the most advertised workflows for non-China users.
- The skill text is mostly Chinese with English terms mixed in, including every `description` field. Routing that depends on English intent phrases may under-trigger, and reviewers who do not read Chinese cannot audit the routing tables quickly.
- `reference/` pages are generated artifacts driven by `packages/cli/src/commands.ts`, and `metadata.version` is synced from the package manifest. Hand edits are overwritten by `pnpm run sync:skill-assets` and by the pre-commit hook, and a local edit to an installed copy diverges from the registry hash that `bl skill update` compares against.
- Two install prerequisites are easy to miss: the npm route needs Node 18.17.0 or newer, and the documented skills CLI fallback is pinned to `skills@1.5.18`, so a newer unpinned release is not what the repository tested against.

## Related

- [QianWen AI Skills - Alibaba Qwen Multimodal Suite Setup](/hermes/skills/catalog/qianwen-ai-setup)
- [HuggingFace Agent Skills - Datasets, Papers, ML Tools Setup](/hermes/skills/catalog/huggingface-agent-skills-setup)
- [Cli Anything Harnesses Setup](/hermes/skills/catalog/cli-anything-harnesses-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the whole family, not one skill. Every business skill opens by reading `../bailian-protocol/SKILL.md` and is told to stop if it is missing, so a subset install needs `bl skill add --name bailian-protocol,<skill>` rather than a single name.
- Export `HERMES_HOME` before `bl skill init`. The fan-out step resolves the Hermes home from that variable, and the canonical copy plus `skill-lock.json` live under `~/.bailian/skills` either way.
- Put `bl skill list --output json` in your health check, not `bl skill init`. The list command distinguishes `outdated` from `missing`, which is the difference between a stale skill and a directory someone deleted.
- Set `NO_COLOR=1` and add `--output json` for anything a script or cron parses, and never echo a key: `INSTALL.md` tells the agent to report only masked fields from `bl auth status`.
- Treat `bl managed-agent plan` and `--dry-run` as mandatory steps. Exit code 7 with `requires_confirmation` is normal control flow, not a CLI bug, and re-confirmation is required after the target or scope changes.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
