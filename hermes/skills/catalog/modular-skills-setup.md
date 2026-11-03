---
title: "Modular Skills - Mojo and MAX Agent Suite"
description: "modular/skills: 18.3K combined installs. Modular's official Mojo and MAX skills: syntax, GPU kernels, Python interop and the model lifecycle."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/modular-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "mojo", "max", "gpu", "model serving"]
---

# Modular Skills - Setup Guide

**Source:** [modular/skills](https://www.skills.sh/modular/skills) via skills.sh - 18.3K combined installs across 12 indexed listings; first seen 2026-10-31 (evening sweep)

**GitHub:** [modular/skills](https://github.com/modular/skills) - 207 stars, license field NOASSERTION (the repository's `LICENSE` is the LLVM Apache License v2.0 with LLVM Exceptions and the README states "Apache 2.0"), branch main, last pushed 2026-10-31; 11 `SKILL.md` directories at the repository root, one per skill, alongside a `.claude-plugin/marketplace.json` manifest

**Category:** Mojo and MAX platform work for agents: language patterns, GPU kernels and package layout

**Quality Tier:** 🟡 Yellow - `new-modular-project` carries a Gen Agent Trust Hub Warn while its Socket and Snyk verdicts pass, and the GitHub license field reads NOASSERTION even though the LICENSE file is Apache 2.0 with LLVM Exceptions

These are Modular's own skills, published under the Agent Skills Standard and aimed at any coding agent, not just Claude Code. The README splits them into two families. Four skills cover writing Mojo and starting projects: `mojo-syntax` corrects pretrained assumptions so an agent writes modern Mojo, `mojo-gpu-fundamentals` adds the patterns for NVIDIA, AMD and Apple silicon GPUs, `mojo-python-interop` handles both directions of the Python boundary including extension modules, and `new-modular-project` scaffolds a project with a `pixi` or `uv` environment. The other seven walk a model through the MAX lifecycle, from a Hugging Face checkpoint to a measured deployment.

The lifecycle half is where the design shows. Each skill names the state it expects the model to be in and hands off to a named successor: `import-model` ports an architecture into MAX as a ModuleV3 model and hands to `debug-model` when the server runs but the text is wrong; `serve-model` stands up an OpenAI-compatible endpoint and picks the flags; `benchmark-model` measures throughput and latency and hands to `profile-model` when the numbers show a bottleneck; `profile-model` works cheapest-first from a utilization snapshot to a kernel breakdown to a single-kernel deep dive; `eval-model` measures task accuracy on standard benchmarks and separates serving failures from wrong answers; `migrate-max-v2-to-v3` ports a V2 graph API model to ModuleV3. The README is explicit that the handoffs are part of the contract, which is unusual in a skill collection and is the reason the set works as a pipeline rather than as seven overlapping prompt files.

## Installation

The README documents four routes. Claude Code users get the plugin marketplace:

```text
/plugin marketplace add modular/skills
/plugin install skills@modular
```

The manifest behind that route is `.claude-plugin/marketplace.json`, named `modular` and versioned `26.5`, which declares three plugins: `skills` with all eleven directories, plus `max-skills` for model work on MAX and `mojo-skills` for writing Mojo. Install a subset with `/plugin install max-skills@modular` or `/plugin install mojo-skills@modular`.

Codex and other agents use the skills CLI, with Node.js installed:

```bash
npx skills add modular/skills
```

The same README documents the update and single-skill forms:

```bash
npx skills update
npx skills add modular/skills --skill mojo-syntax
```

The fourth route is manual, and it is the one that fits a Hermes profile: clone the repository and copy or symlink the skill directories into the agent's skills directory, which the README gives as `~/.claude/skills/` for Claude Code. For this profile the copy is explicit, one directory per skill, because one indexed listing has no directory to copy:

```bash
git clone --depth 1 https://github.com/modular/skills.git /tmp/modular-skills
mkdir -p ~/.hermes/profiles/corpusiq/skills
for d in mojo-syntax mojo-gpu-fundamentals mojo-python-interop new-modular-project \
         import-model debug-model profile-model eval-model serve-model \
         benchmark-model migrate-max-v2-to-v3; do
  cp -r "/tmp/modular-skills/$d" ~/.hermes/profiles/corpusiq/skills/
done
```

Copy the directories, not just the `SKILL.md` files. Several skills carry their own `scripts/` folder and a `pixi.toml`, so `import-model` ships `inspect_hf.py`, `scaffold.py` and `check_port.py`, and `eval-model` ships `eval_dataset.py` with a test suite beside it.

The runtime expectations are real rather than nominal. The project skills initialise a `pixi` or `uv` environment, `serve-model` sets up the `max-nightly` conda channel or nightly wheel index, and the GPU, profiling and benchmarking skills assume a machine where MAX can actually use a device, with `profile-model` targeting NVIDIA or AMD GPUs. A laptop profile can install and read all of it, but only a host with a working MAX install can run most of the lifecycle.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| mojo-syntax | 2,957 | Writing modern Mojo: corrects pretrained assumptions about the language, and the README says to use it whenever an agent writes Mojo, including when another Mojo skill also applies. |
| mojo-gpu-fundamentals | 2,690 | Programming NVIDIA, AMD and Apple silicon GPUs in Mojo, pairing with `mojo-syntax` and covering the misconceptions about how Mojo GPU code is written. |
| mojo-python-interop | 2,614 | Mojo calling Python and Python calling Mojo: calling Python libraries from Mojo, exposing Mojo types and functions to Python, and building Python extension modules. |
| new-modular-project | 2,453 | Starting a Mojo or MAX project from scratch and initialising the `pixi` or `uv` environment it needs. |
| import-model | 1,473 | Importing a Hugging Face architecture into MAX as a ModuleV3 model: inspecting the config and modelling code, scaffolding from a similar registered architecture and verifying outputs match. |
| debug-model | 1,296 | Parity debugging once a model loads and generates but the output is wrong: tensor-dump comparators against a reference, numerical verification before recompiling, and a serve-versus-pipeline bisect. |
| profile-model | 1,194 | Finding where inference time goes and whether the GPU is saturated, cheapest first: a utilization snapshot, a kernel breakdown with `nsys` or `rocprofv3`, then an `ncu` deep dive. |
| eval-model | 1,011 | Measuring task accuracy against GSM8K, MMLU, HellaSwag, ARC, AIME, GPQA, TruthfulQA, WinoGrande and BABILong, and separating serving failures from wrong model answers. |
| serve-model | 979 | Standing up an OpenAI-compatible endpoint with `max serve`, including the environment, a Hugging Face repo or local checkpoint, custom architectures and the serve flags a model needs. |
| benchmark-model | 917 | Driving load against a `max serve` endpoint with `max benchmark`: throughput, TTFT, TPOT and inter-token latency, plus GPU utilization when it runs on the same NVIDIA host. |
| closure-migration | 489 | Indexed with 489 installs but no directory in the current tree and no README entry, so its scope is undocumented here; the migration skill the README describes is `migrate-max-v2-to-v3`. |
| migrate-max-v2-to-v3 | 239 | Porting a model written against the V2 graph API (`max.nn.legacy`, `TensorValue`, explicit `Graph`) to ModuleV3 (`max.nn`), leaving V2 code untouched and verifying greedy outputs match. |

All 12 indexed listings clear the 0-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

Mojo is a language where a model's training data actively misleads it. The README states the problem directly: `mojo-syntax` exists to correct pretrained assumptions, and `mojo-gpu-fundamentals` exists to overcome misconceptions about how Mojo GPU code is written. For an agent, that is the difference between generating a plausible Mojo file and generating one that compiles against the current compiler, and it is a problem a generic coding prompt cannot solve because the wrong answer looks fine.

The lifecycle skills encode a different kind of knowledge: which failure belongs to which stage. "The server runs but the output is gibberish" is `debug-model`, not `import-model`; "it crashes on load" is `import-model`; "it is slow" is `profile-model` before `benchmark-model` runs again. Each skill names its entry state and its successor, so a model that loads the wrong one is usually told so inside the file, which is the closest thing to routing an agent can have without a controller.

The platform knowledge is also current by construction. Modular ships these alongside the platform, the manifest is versioned, and the skills reference the flags of the day such as `--custom-architectures`, `--quantization-encoding` and `--trust-remote-code`. A profile working near MAX is better served by a versioned first-party skill than by a blog post about MAX from last year.

## Usage

| You say | What happens |
|---|---|
| "Write this kernel in Mojo" | `mojo-syntax` loads the current syntax and conventions first, and `mojo-gpu-fundamentals` adds the GPU target patterns when the code runs on an accelerator. |
| "Start a new Mojo project called nvfp4-for-metal" | `new-modular-project` scaffolds the layout and initialises the `pixi` or `uv` environment for the platform. |
| "Bring up Qwen in MAX from Hugging Face" | `import-model` inspects the upstream config and modelling code, scaffolds a ModuleV3 model from the closest registered architecture and verifies outputs against the reference. |
| "It serves but the greedy tokens diverge from the reference" | `debug-model` builds tensor-dump comparators, bisects serve versus pipeline, and verifies a fix numerically before recompiling. |
| "Serve this model behind an OpenAI-compatible endpoint" | `serve-model` sets up the environment, points at the checkpoint or Hugging Face ID, and picks the devices, quantization, max length and task flags. |
| "How fast is this deployment, and where is the time going" | `benchmark-model` measures throughput and latency against the running endpoint, then hands to `profile-model` when a bottleneck shows up in the numbers. |
| "Did the port change accuracy" | `eval-model` runs the standard benchmark set against the endpoint and separates a serving problem from a wrong answer. |

## Verification

The raw path for `mojo-syntax` returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} mojo-syntax\n" \
  https://raw.githubusercontent.com/modular/skills/main/mojo-syntax/SKILL.md
```

Expect `200`. After the copy lands, confirm all eleven directories arrived and that the script-bearing skills kept their helpers:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/{mojo-syntax,serve-model,import-model,eval-model}/ | wc -l
head -5 ~/.hermes/profiles/corpusiq/skills/mojo-syntax/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/import-model/scripts | head -4
```

The count should print 4, the header should show `name: mojo-syntax`, and the script listing should show `inspect_hf.py` and `scaffold.py`.

## Security

One of the five sampled skills carries a Gen Agent Trust Hub warn, which is what makes this pack Yellow alongside the license field.

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| mojo-syntax | Pass | Pass | Pass |
| new-modular-project | Warn | Pass | Pass |
| profile-model | Pass | Pass | Pass |
| benchmark-model | Pass | Pass | Pass |
| migrate-max-v2-to-v3 | Pass | Pass | Pass |

The warn sits on the one skill that creates projects and initialises environments, which is a plausible heuristic hit rather than a specific finding: a skill that writes files and runs an environment command looks different from a prose skill. Socket and Snyk both pass it.

The larger reviewable surface is the scripts. Several skills ship Python helpers under `scripts/` plus a `pixi.toml`, and the lifecycle skills run real commands: `max serve`, `max benchmark`, `nsys`, `rocprofv3`, `ncu`, and dataset downloads for evaluation. Read the `scripts/` folder of any skill before its first run, and prefer a disposable environment for `new-modular-project` because it initialises one.

The license needs both facts stated. GitHub reports NOASSERTION because the `LICENSE` file is the LLVM Project text: the Apache License v2.0 with LLVM Exceptions, while the README's own License section says "Apache 2.0. See the LICENSE file for details." Neither is a restrictive license, and the LLVM exceptions are broader than plain Apache 2.0 rather than narrower, but the metadata mismatch is why the tier is Yellow rather than Green. Treat Hugging Face tokens and any registry credentials as environment variables, and keep them out of prompts and out of the files an agent writes.

## Limitations

- Snapshot data, verified 2026-10-31: 18,312 combined installs across 12 indexed listings; 207 GitHub stars; license field NOASSERTION with an Apache 2.0 plus LLVM Exceptions LICENSE file; last pushed 2026-10-31. Counts drift over time.
- Index and tree disagree by one: 12 indexed listings against 11 `SKILL.md` directories. `closure-migration` carries 489 installs, has no directory in the current tree and no entry in the README, so there is nothing to load and nothing to document.
- The lifecycle skills assume working hardware and a working MAX install. `serve-model`, `benchmark-model`, `profile-model` and `eval-model` all expect a machine that can run the model, and `profile-model` targets NVIDIA or AMD GPUs specifically.
- `eval-model` does not trigger on its own. The README says to ask for it by name, so a profile relying on automatic skill selection will not run accuracy checks.
- The collection is a platform suite, not a general programming suite. Coverage starts at writing Mojo and ends at a measured MAX deployment; it says nothing about the rest of a model pipeline.
- The plugin route is Claude Code specific. The README's `/plugin marketplace add` commands do not transfer to Hermes, which is why the directory copy is the durable route here.

## Related

- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)
- [Tigris Data Skills - Object Storage for Agents](/hermes/skills/catalog/tigrisdata-skills-setup)
- [Lev Nikolaevich Skills - DevOps and Delivery Setup](/hermes/skills/catalog/levnikolaevich-claude-code-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `mojo-syntax` even if you install nothing else. Every other Mojo skill in the set says to use it alongside, and it is the one that fixes the model's stale assumptions about the language.
- Follow the handoff order. `import-model` to `debug-model` for wrong output, `profile-model` before a second `benchmark-model` when throughput disappoints, and `eval-model` last to check that the speed did not cost accuracy.
- Copy directories, not `SKILL.md` files. `import-model` and `eval-model` are mostly scripts, and a bare markdown copy removes the part that does the work.
- Name the entry state in the prompt. Saying "it loads and generates but tokens diverge" routes to `debug-model`, while "it will not start" routes to `import-model`; the skills are written around that distinction.
- Keep the skills next to the project they serve. The environment a `pixi` or `uv` scaffold creates is per project, so a global install of the lifecycle skills across several repos gets confusing fast.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
