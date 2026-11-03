---
title: "Runpod Plugin - GPU Pod and Serverless Skill Setup"
description: "runpod/runpod-plugins-official: 134.1K combined installs. Official Runpod plugin, 16 skills plus a hosted MCP server for GPU pods and serverless."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/runpod-plugins-official-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "runpod", "gpu", "serverless", "mcp"]
---

# Runpod Plugin - Setup Guide

**Source:** [runpod/runpod-plugins-official](https://www.skills.sh/runpod/runpod-plugins-official) via skills.sh - 134.1K combined installs across 19 indexed listings; first documented 2026-11-03 (nightly sweep)

**GitHub:** [runpod/runpod-plugins-official](https://github.com/runpod/runpod-plugins-official) - 47 stars, Apache-2.0, branch main, last pushed 2026-11-02; one plugin at `plugins/runpod/` holding 16 skill directories under `plugins/runpod/skills/` (173 Markdown files including references, 27 golden paths and 51 concept YAML files), two internal authoring skills under `.claude/skills/`, a bundled `.mcp.json`, and an `ontology/` validator toolkit

**Category:** GPU pod, serverless endpoint, template and volume operations on Runpod, delivered as skills plus a hosted MCP server

**Quality Tier:** 🟡 Yellow - `runpodctl` and `flash` pass all three auditors but the third sampled skill, `companion-clis`, carries a Warn from Gen Agent Trust Hub, Socket and Snyk

Runpod publishes this as the official plugin marketplace for agents that manage GPU workloads, and the repository ships exactly one plugin. That plugin is not a single skill but a small routing system: a `runpod` router, the lane skills it points at (`runpodctl`, `flash`, `runpod-mcp`, `runpod-usage`, `runpod-templates`, `runpod-build-template`, `companion-clis`, `runpod-migrate`), and seven MCP journey skills (`discovery`, `lifecycle-crud`, `serverless-deploy`, `pod-deploy`, `pod-doctor`, `endpoint-ops`, `cost-audit`) that turn a request into a read, a decision and then a change. The plugin manifest is versioned at 1.9.0 and lists Runpod itself as the owner.

The design detail worth understanding before installing is that the knowledge and the tooling are separated on purpose. The skills decide what to do and in what order; the actual calls go through `runpodctl`, the `flash` deployment tool, or the hosted MCP server at `https://mcp.runpod.io/`. Each skill also names the concepts it covers, and those concepts live as one YAML file each in `runpod-usage/concepts/`, so a rule an agent applies traces back to a public source rather than to a paragraph someone wrote once.

## Installation

The README's quick start is four lines, and only the first is essential:

```bash
npx skills add runpod/runpod-plugins-official   # the skills, any agent
curl -sSL https://cli.runpod.net | bash         # runpodctl (or: brew install runpod/runpodctl/runpodctl)
uv tool install runpod-flash                    # flash, optional (or: pip install runpod-flash)
npx @runpod/mcp-server@latest add               # hosted MCP server, guided setup with OAuth
```

Claude Code can install the plugin natively, which also wires the hosted MCP server through the bundled `.mcp.json`:

```
/plugin marketplace add runpod/runpod-plugins-official
/plugin install runpod@runpod
/reload-plugins
```

Codex takes the marketplace route and may need the MCP server added by hand if the tools do not appear after install:

```bash
codex plugin marketplace add https://github.com/runpod/runpod-plugins-official.git
codex plugin add runpod@runpod
codex mcp add runpod --url https://mcp.runpod.io/
```

One API key covers the CLI, the flash tool and the MCP server. Export it for the current shell, or let `runpodctl doctor` prompt for it and write `~/.runpod/config.toml`:

```bash
export RUNPOD_API_KEY=<key>
runpodctl doctor
```

For the MCP server the README offers OAuth as the alternative to a key on disk: in Claude Code, `/mcp` then `runpod` then "Sign in with Runpod". Other clients install the skills the same way and add the MCP server themselves with `npx @runpod/mcp-server@latest add`, which detects the agent and configures the hosted server.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| runpodctl | 14,934 | Terminal, CI and scripting work: pods, serverless endpoints, templates, network volumes, Hub deploys, models, SSH and file transfer, plus `doctor`. |
| flash | 14,477 | Code-first serverless: writing and deploying handlers with runpod-flash, `@Endpoint`, `@remote`, `flash dev`, resource sizing and debugging. |
| companion-clis | 14,123 | The prerequisite CLIs around a Runpod workflow: HuggingFace, GitHub, Docker and AWS, each with its own credentials. |
| runpod | 13,315 | The router. Start here when the right lane skill is unclear. |
| runpod-usage | 13,258 | Concepts and design choices: pods versus serverless, GPU and VRAM, image construction, storage, networking, workload development. |
| runpod-mcp | 13,231 | Infrastructure through the hosted MCP server's tool calls: pods, endpoints and jobs, templates, volumes, registry credentials, secrets, clusters, catalog, billing. |
| runpod-migrate | 11,582 | Moving a codebase from the GraphQL API or REST v1 to REST v2: inventory, rewrite call sites, flag breaking changes, verify. |
| runpod-templates | 10,878 | Finding and troubleshooting official pod templates, including ComfyUI workflow model metadata repair. |
| pod-doctor | 3,501 | A pod that is unreachable, GPU-blind or stuck: read the logs, run an account-wide stuck-pod check, act only on authorization. |
| pod-deploy | 3,501 | Provisioning a pod for interactive, development or training use, reading stock first and handing back a working proxy URL or SSH address. |
| serverless-deploy | 3,495 | Taking a HuggingFace repo, ComfyUI workflow, Hub release, container image, GGUF or Civitai asset to a warmed endpoint proved with one real job. |
| cost-audit | 3,484 | Read-only spend audit: idle spend, serverless bills that look wrong, spend by resource type and by resource, whole-account snapshot. |
| discovery | 3,476 | Catalog questions: GPU and CPU types with price, live stock per data center, CUDA versions with capacity, Hub marketplace, public endpoints. |
| endpoint-ops | 3,474 | Operating an existing endpoint: queued jobs, dying workers, scaling, idle timeout, FlashBoot, GPU pinning, queue cancel and purge. |
| lifecycle-crud | 3,471 | The reusable plumbing: templates, network volumes, registry credentials, account secrets, SSH keys and Instant Clusters, created and read back. |
| runpod-build-template | 2,004 | Building a complete template project from an app request, local code or a GitHub repo, with a documented Dockerfile and app files. |
| write-guide | 736 | Internal authoring skill (frontmatter marks it internal): writing a skill, reference doc or golden path that agrees with the concept graph. |
| add-concept | 731 | Internal authoring skill: adding or changing a node in the concept graph under `runpod-usage/concepts/`, duplicate checks included. |
| runpod-comfyui-models | 465 | Legacy listing: ComfyUI workflow repair was folded into `runpod-templates`, which is the skill to install today. |

No indexed listings fall below the threshold; all 19 appear above.

## Why This Matters for Hermes Agents

GPU work is the one category where a confident wrong answer costs real money per hour, and most agent skills in this space are prose about a console. This plugin is built the other way round: the router decides the lane, the lane skill insists on reading state before writing it, and the read-only skills say so in their own descriptions. `cost-audit` reports that every figure comes from the MCP billing and list reads and that it never stops or changes anything. `discovery` is read-only by construction. `endpoint-ops` changes only the setting the user authorized, with a read before and after. `pod-doctor` performs a recovery action only when the user authorizes one. That is a useful contract to have written down, because an agent that inherits it will ask before terminating a pod.

The second reason is the concept graph. Fifty-one YAML files under `runpod-usage/concepts/` hold one node each for things like a pod, a network volume, a worker or a billing record, and every skill, reference and golden path lists the concepts it covers. The practical effect is that an agent answering "why did I get billed when nothing was running" is pointed at the billing rule and at a worked example that used it, instead of at a model's recollection of how serverless billing usually works.

The third is the golden paths. There are 27 of them under `runpod/skills/runpod/golden-paths/`, covering an Ollama pod, a ComfyUI pod, a Whisper endpoint, a fine-tune pod, a model-to-endpoint pipeline, a dev pod, a network-volume handoff, a fine-tune-to-serverless move, a custom serverless dev loop and multi-region HA serverless, among others. The README states plainly that these files deliberately carry no `SKILL.md` so that agents never auto-load them, and that asking for them is what pulls them in. That is a deliberate context-budget decision, and it is worth copying: the expensive worked examples stay on disk until the task needs one.

## Usage

| You say | What happens |
|---|---|
| "List my Runpod endpoints" | The router sends it to `runpod-mcp`, which calls the hosted server's `list-endpoints` tool. This is also the README's smoke test after install. |
| "Spin up an A100 pod for a week of fine-tuning" | `pod-deploy` reads stock and the catalog, picks the image and GPU class, co-locates a network volume so checkpoints outlive the pod, and returns the proxy URL or SSH address. |
| "Deploy this handler to serverless" | `serverless-deploy` picks the engine for the modality, sizes the GPU from the model metadata, provisions, warms and proves the endpoint with one real job, then reports what it bills. |
| "What is this bill, nothing should be running?" | `cost-audit` reads the billing and list endpoints, separates idle spend from serverless charges, and breaks the total down by resource without changing anything. |
| "Cheapest GPU that fits a 13B model?" | `discovery` sizes the VRAM need against live stock and price per data center, and quotes what the options actually cost. |
| "My endpoint has been IN_QUEUE forever" | `endpoint-ops` diagnoses queued jobs and dying workers, tunes scaling and idle timeout, and pins the GPU selection if that is the cause. |
| "Move this repo off the GraphQL API" | `runpod-migrate` inventories which parts use which API version, shows the inventory before changing anything, rewrites call sites and flags breaking changes. |

## Verification

The raw path below returned 200 on branch main on 2026-11-03:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/runpod/runpod-plugins-official/main/plugins/runpod/skills/runpodctl/SKILL.md
```

After a clone, confirm the plugin layout, the bundled MCP declaration and the skill count:

```bash
git clone --depth 1 https://github.com/runpod/runpod-plugins-official.git /tmp/runpod-plugin
ls /tmp/runpod-plugin/plugins/runpod/skills | wc -l
cat /tmp/runpod-plugin/plugins/runpod/.mcp.json
head -3 /tmp/runpod-plugin/plugins/runpod/skills/runpod/SKILL.md
```

The count should print 16, `.mcp.json` should declare one server named `runpod` of type `http` at `https://mcp.runpod.io/`, and `head` should show `name: runpod`. Then check the tool side, because the skills are inert without it:

```bash
runpodctl doctor
runpodctl get pod
```

`doctor` reports whether the key is readable and where it was written, and `get pod` is the cheapest proof that the account is reachable. In a Claude Code session, `/plugin` should list Runpod under Installed, and the first Runpod request should produce an MCP tool call rather than a shell command.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-03) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| runpodctl | Pass | Pass | Pass |
| flash | Pass | Pass | Pass |
| companion-clis | Warn | Warn | Warn |

The warn on `companion-clis` is the one to read before installing the optional pieces. That skill does not ship binaries; it documents the HuggingFace, GitHub, Docker and AWS CLIs, and each of those brings its own credentials and its own trust decision. The README says the same thing in its own words: companion CLIs install separately, per task.

What the plugin does carry is real authority over a cloud account. Every mutating skill routes through the MCP server or `runpodctl` with the same API key, and that key can create pods, delete volumes and stop endpoints. Treat it as a production credential: keep it in the shell environment or `~/.runpod/config.toml`, not in a skill file or a committed `.env`. The OAuth route in Claude Code exists for this reason, since it keeps no key on disk. Note also that the hosted MCP server is a network dependency at `https://mcp.runpod.io/`, so anything the agent does through it is visible to that endpoint.

The repository is unusual in shipping its own guards. The `ontology/` directory holds a validator, a bundle builder and a SQLite exporter for the concept graph, and `hooks/` holds eleven Python checkers that validate the marketplace manifest, frontmatter, links, branding, versions and a set of migration claims. Those run in CI rather than at install time, but they are the reason the skill text and the concept graph tend not to drift apart.

## Limitations

- Snapshot data, verified 2026-11-03: 134,136 combined installs across 19 indexed listings; 47 GitHub stars; Apache-2.0; last pushed 2026-11-02. Counts drift over time.
- Three of the 19 indexed listings are not deployment lanes. `write-guide` and `add-concept` are marked `internal: true` and ship under `.claude/skills/` rather than the plugin's own skills directory, and `runpod-comfyui-models` is a legacy name whose ComfyUI repair work was folded into `runpod-templates`.
- The skills do nothing on their own. Without `runpodctl`, `runpod-flash` or the MCP server, a lane skill can plan but not act, and the README notes the router detects that state and walks the user through setup.
- `companion-clis` warns on all three auditors and its dependencies are separate installs with separate credentials. If a task needs `docker` or `aws`, decide about those tools on their own merits.
- The golden paths never auto-load, by design. An agent that is not asked to look at the examples will plan from the skill text alone, which is thinner than the worked commands the paths contain.
- The MCP route depends on a hosted service. For a local stdio variant or a Codex-specific setup, the `runpod-mcp` skill carries the alternatives, but nothing in the plugin falls back automatically.

## Related

- [OpenCLI Skills - Agent CLI with Browser Automation Setup](/hermes/skills/catalog/opencli-skills-setup)
- [Limrun Skills - Cloud iOS & Android Simulator Setup](/hermes/skills/catalog/limrun-skills-setup)
- [Science Skills - PubMed, arXiv and Lab Data Setup](/hermes/skills/catalog/science-skills-setup)
- [Composio - SDK Monorepo and Agent Toolkit Setup Guide](/hermes/skills/catalog/composiohq-composio-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `runpodctl` alongside the skills even if you plan to use the MCP server. It is the fallback lane when the MCP tools are not connected, and `runpodctl doctor` is the fastest way to prove the key works.
- Say "look at the examples first" when the task is a design rather than a one-off action. The golden paths are the only place the commands that were actually run against a real account live, and they will not load otherwise.
- Ask for the plan before the change. Every mutating lane reads before it writes, and saying so out loud keeps a `pod-deploy` from becoming a `pod-terminate` you did not want.
- Use `cost-audit` before provisioning, not only when the bill looks wrong. It is read-only and it answers what is already running, which is the usual reason a new pod is not the right move.
- Rerun `npx skills add runpod/runpod-plugins-official` to update. The plugin is versioned and releases are what carry changes, so a stale copy will describe an older CLI surface.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
