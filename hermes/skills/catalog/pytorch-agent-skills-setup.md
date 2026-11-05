---
title: "PyTorch Agent Skills - Contributor Workflow Suite"
description: "pytorch/pytorch on skills.sh: 26.7K combined installs across 16 listings; contributor skills for dispatch macros, docstrings, PR review and triage."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pytorch-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "pytorch", "ml engineering", "code review"]
---

# PyTorch Agent Skills - Setup Guide

**Source:** [pytorch/pytorch](https://www.skills.sh/pytorch/pytorch) via skills.sh - 26.7K combined installs across 16 indexed listings; first seen 2026-11-04 (Nov 4, 2026 evening sweep)
**GitHub:** 105,148 stars, GitHub reports the licence as NOASSERTION while the LICENSE file carries a BSD-style three-clause body, last pushed 2026-11-05, 19 SKILL.md directories under .agents/skills/
**Category:** PyTorch contribution workflow: operator dispatch, docstrings, PR review, issue triage and AOTInductor debugging inside the pytorch/pytorch repository
**Quality Tier:** 🟡 Beta - GitHub licence field NOASSERTION (BSD-style body in LICENSE); Snyk Warn on pr-review.

These are PyTorch's own contributor skills, checked into the monorepo under `.agents/skills/` rather than published as a separate plugin. Each directory covers one recurring maintenance task, and the surrounding instructions expect them: `CLAUDE.md` at the repository root tells an agent to use the `/pr-review` skill when asked to review a pull request, and points at the `ghstack-ci` skill for CI work.

Nineteen skill directories ship in the tree. They divide into kernel and dispatch work (`add-uint-support`, `at-dispatch-v2`, `metal-kernel`), review and hygiene (`pr-review`, `docstring`, `pyrefly-type-coverage`), and triage or debugging (`triaging-issues`, `aoti-debug`). Eight of the 16 indexed listings clear the 500-install threshold.

## Installation

The repository README covers installing PyTorch as a library, not installing these skills, so the command below is the one the skills.sh listing prints for this source:

```bash
npx skills add pytorch/pytorch
```

The 19 skill directories are plain folders under `.agents/skills/`, each holding a `SKILL.md` with `name` and `description` frontmatter, so an agent pointed at a local clone can also read them directly. The tree ships with the source it describes, which makes the in-repo copies the authoritative version.

Contributor work still needs a built checkout. `CLAUDE.md` documents the editable install used for that, `pip install -e . -v --no-build-isolation`, and tells an agent to check for a local `.venv` before reaching for alternatives.

## What It Provides

Eight of the 16 indexed listings meet the 500-install threshold.

| Skill | Installs | Use For |
|---|---|---|
| add-uint-support | 3,632 | Adding uint16, uint32 and uint64 support to operators by updating AT_DISPATCH macros across ATen kernels |
| docstring | 3,267 | Writing docstrings for PyTorch functions and methods in the project's documented style |
| pr-review | 3,259 | Reviewing pull requests for code quality, security and backward compatibility |
| metal-kernel | 3,185 | Writing Metal and MPS kernels, wiring native_functions.yaml dispatch and porting CUDA kernels to Apple Silicon |
| at-dispatch-v2 | 3,182 | Converting AT_DISPATCH_ALL_TYPES_AND* and other dispatch macros to the AT_DISPATCH_V2 form in ATen C++ |
| pyrefly-type-coverage | 3,161 | Migrating a file to stricter Pyrefly checking with annotations on every function, class and attribute |
| triaging-issues | 3,147 | Routing new GitHub issues to oncall teams, applying labels and closing questions |
| aoti-debug | 3,143 | Debugging AOTInductor segfaults, device mismatches, constant loading failures and runtime errors |

The remaining 8 indexed listings range from 20 to 168 installs, covering the smaller contributor tasks in the same tree.

## Why This Matters for Hermes Agents

Almost every agent skill collection targets people who use a library. This one targets the people changing it, and the difference shows in the instructions: exact macro names, exact YAML fields, exact CI entry points rather than general advice about writing good code.

`at-dispatch-v2` is the cleanest example of a mechanical refactor expressed as a skill. The migration pattern is enumerated, so an agent applies it one kernel file at a time instead of inventing a rewrite and hoping the build catches the difference.

`pr-review` encodes project policy as a checklist. Backward compatibility and security are stated review dimensions rather than implicit expectations, which is what makes review output stable from one session to the next.

`triaging-issues` turns routing into a decision procedure: which oncall team, which labels, when a question gets closed. That is the kind of judgment that normally lives in one maintainer's head.

The honest limitation is scope. These skills assume a PyTorch checkout with a working build, and several of them assume a CUDA or MPS toolchain. An agent writing application code against `torch` gets little from this pack, while an agent preparing a PR against `pytorch/pytorch` gets a large amount.

## Usage

| You say | What happens |
|---|---|
| "add uint64 support to this operator" | add-uint-support finds the AT_DISPATCH sites and carries the unsigned type through the kernels |
| "convert these dispatch macros to v2" | at-dispatch-v2 rewrites the named ATen files to the AT_DISPATCH_V2 API |
| "write a docstring for this function" | docstring applies the project's docstring conventions to the signature |
| "review this PR" | pr-review checks code quality, security and backward compatibility, which is the same route CLAUDE.md names |
| "why does this AOTI build segfault?" | aoti-debug works through device mismatch, constant loading and runtime failure modes |
| "triage the new issues" | triaging-issues routes each issue to an oncall team, applies labels and closes questions |
| "add an MPS kernel for this op" | metal-kernel covers native_functions.yaml dispatch, the host-side operator and the Metal shader |

## Verification

Fetch a raw skill file to confirm the tree still matches what skills.sh indexed. This path is `.agents/skills/docstring/SKILL.md` on branch `main` and it returned 200 on November 4, 2026:

```bash
curl -fsSL https://raw.githubusercontent.com/pytorch/pytorch/main/.agents/skills/docstring/SKILL.md | head -20
```

A response opening with `name: docstring` and a description confirms the content is live. The repository itself keeps the skills at `.agents/skills/`, so a checkout doubles as a reference copy:

```bash
ls .agents/skills
```

That should print the 19 directories. After the CLI install, compare the agent skills directory the install prompt reported against that list to see exactly which skills were written.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-04) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| add-uint-support | Pass | Pass | Pass |
| docstring | Pass | Pass | Pass |
| pr-review | Pass | Pass | Warn |
| document-public-apis | Pass | Pass | Pass |

The one adverse verdict is Snyk's Warn on `pr-review`, the third most installed skill in the suite. Gen Agent Trust Hub and Socket pass it, and the other three sampled skills pass all three auditors. Nothing in the sampled set reads credentials; the risk in this pack is code quality in a very large C++ tree, not data access.

## Limitations

- Snapshot data, verified 2026-11-04: 26,667 combined installs across 16 indexed listings; 105,148 GitHub stars; NOASSERTION licence field; last pushed 2026-11-05. Counts drift over time.
- GitHub reports the licence as NOASSERTION even though `LICENSE` carries a BSD-style three-clause body. Treat the terms as BSD-style, but confirm with the project before redistributing the files.
- The last push date, 2026-11-05, is one day after this snapshot. It is carried verbatim from repository metadata and is most likely a timezone artifact.
- The repository README documents installing PyTorch, not installing these skills. The skills.sh line is the only install route found for this source.
- Several skills assume a compiled checkout and a CUDA or MPS toolchain. `aoti-debug`, `metal-kernel` and `at-dispatch-v2` are unusable without one.
- Eight of the 16 indexed listings sit below the 500-install threshold and are not described above.

## Related

- [AI Research Skills - 100-Skill ML Research Library Setup](/hermes/skills/catalog/ai-research-skills-setup)
- [HuggingFace Agent Skills - Datasets, Papers, ML Tools Setup](/hermes/skills/catalog/huggingface-agent-skills-setup)
- [OpenAI Agents Python Skills - Multi-Agent Setup](/hermes/skills/catalog/openai-agents-python-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `pr-review` before opening the PR, not after review comments arrive. The backward compatibility check is cheapest while the diff is still yours.
- Work `at-dispatch-v2` one kernel file per request. The conversion is mechanical, and a small diff is the only way to see a missed macro.
- Keep the build directory warm. `aoti-debug` and `metal-kernel` both need a compiled tree, and a rebuild between attempts dominates the loop.
- Use `add-uint-support` as the template for any new dtype rollout. The macro sites it touches are the same sites a new type needs.
- Pin the checkout in your prompt. The skills describe the tree they ship in, so a skill read from `main` and a checkout on a release branch can disagree.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
