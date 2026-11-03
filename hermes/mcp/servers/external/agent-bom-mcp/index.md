---
title: "agent-bom MCP - The Blast Radius of an AI Supply Chain"
description: "An open-source AI supply-chain BOM that inventories agents, MCP servers and packages, then shows which credential a vulnerable package can actually reach."
category: Security / Governance
stars: "★★★ (open source, driven: offline demo scan plus a live stdio MCP session)"
added: 2026-11-03
source: "the mcpservers.org /all newest page at position 22 of 30, filed at koda-ai-studio/agent-bom on GitHub with an Apache-2.0 licence and the PyPI package agent-bom, the official registry name io.github.koda-ai-studio/agent-bom, and a driven run on 2026-11-03: uvx agent-bom 0.113.0 scan --demo --offline (5 agents, 10 servers, 23 packages, 15 vulnerabilities, posture F 37/100, exit code 1 as a verdict) plus a stdio initialize and tools/list returning 8 tools"
relevance: ★★★
tags: [ai-supply-chain, sbom, mcp-security, blast-radius, cve, credentials, cisa-kev, epss, open-source, stdio, governance]
last_updated: "2026-11-03"
---

# agent-bom MCP

**A vulnerable package is a fact. What it can reach is the decision. Most scanners stop at the first and leave you to guess the second, so a CVSS 9.8 in a library three hops from production reads the same as one that sits next to nothing. The question an operator actually needs answered is narrower: which credential can this thing touch, and which agent is holding it.**

```
Server type:  Local (stdio), plus a CLI and a PyPI package
Install:      uvx agent-bom mcp server
Package:      agent-bom 0.113.0 (PyPI), Python 3.11 to 3.14, Apache-2.0
Registry:     io.github.koda-ai-studio/agent-bom
Source:       github.com/koda-ai-studio/agent-bom
Tools:        8, verified over stdio on 2026-11-03
Scan target:  a project path, a running agent config, or a container image
Vuln data:    OSV.dev for live checks, a bundled advisory DB for offline runs
Team mode:    GitHub Action koda-ai-studio/agent-bom@v0, or self-hosted via Helm
```

## What it does

agent-bom walks the AI layer of a machine or a repository, not just its dependency file. It discovers the agents that are installed (Claude Desktop, Cursor, a custom LangChain service, a support copilot), the MCP servers each one connects to, the packages those servers pull in, and the credentials sitting in the environment beside them. Then it joins that inventory to vulnerability data and prints the path a compromised package would take to reach a secret.

That join is the product. A package CVE is commodity data. `langchain@0.0.150 → llm-orchestrator → ANTHROPIC_API_KEY` is a finding someone can act on before lunch.

## What this pass measured

Driven, not documented. Two runs on 2026-11-03.

**The offline demo scan.** `uvx agent-bom scan --demo --offline` ships a curated sample with a bundled advisory DB of 17 advisories, so the output is reproducible without a network call.

| Measured | Value |
| --- | --- |
| Agents discovered | 5 (`cursor`, `langchain-service`, `support-copilot`, `data-pipeline`, `claude-desktop`) |
| MCP servers | 10 |
| Packages | 23 (14 PyPI, 9 npm) |
| Vulnerabilities | 15 findings, 7 critical, 11 high, 7 medium, 26 low across all finding categories |
| Posture grade | F, 37 of 100 |
| Top posture driver | Credential Hygiene, 14 credentials |
| Toxic combinations | 5 findings |
| Actively exploited | 1 CISA KEV, `pillow@9.0.0` CVE-2023-4863 at EPSS 99 percent |
| Runtime | 0.8 seconds total, 0.1 discovery and 0.5 scanning |
| Exit code | 1, a scan verdict rather than a scanner error |

The two findings worth reading in full are the reachability ones. CVE-2023-36258 in `langchain@0.0.150` carries a blast radius of `llm-orchestrator → ANTHROPIC_API_KEY +1` at EPSS 1 percent, which is a critical severity pointing at an API key that bills. CVE-2020-14343 in `pyyaml@5.3` reaches `shell-runner-service` at EPSS 5 percent, which is a deserialisation bug one hop from a shell. A flat CVE list ranks the pillow bug first on EPSS alone and buries both.

The remediation plan is per fix, not per CVE: `jsonwebtoken 8.5.1 → 9.0.0` clears 1 vulnerability, 1 agent, 2 credentials and 3 tools, with an install command and a `agent-bom check jsonwebtoken@9.0.0` verification step beside it. 15 of the findings were fixable.

Compliance output is deliberately modest and says so: 15 action required, 0 review, 0 evidence current, and a line stating that no framework is reported as compliant because the mappings are review evidence only. That is the right place to draw the line for a tool that cannot see your evidence collection.

**The MCP server mode.** `uvx agent-bom mcp server` answers a stdio session as `agent-bom` 0.113.0 and lists 8 tools, so the same inventory is available inside a coding agent rather than only from a terminal.

## Tools

| Tool | What it answers |
| --- | --- |
| `scan` | Full AI supply-chain scan returning an AI-BOM, by project path, config or image |
| `generate_sbom` | A software bill of materials for the agent setup, agents and servers and packages |
| `exposure_paths` | The attack-path queue in ranked order, with why each path ranks where it does |
| `check` | One package against OSV.dev before you install it |
| `remediate` | A remediation plan for the findings the scan raised |
| `policy_check` | A policy evaluated against current scan results, pass or fail with reasons |
| `intel_lookup` | One advisory from the local threat-intel database |
| `compliance` | Compliance posture with its source labelled, tenant evidence or a local scan |

`exposure_paths` is the one to open first. Its ranking is exposed as `ranking.order` with the reason attached, which means an analyst can argue with the order instead of accepting it.

## Installation

Terminal, scanning the project you are standing in:

```
uvx agent-bom scan . --no-discover -f html -o agent-bom-report.html
```

Sample data with no project and no network:

```
uvx agent-bom scan --demo --offline
```

As a tool inside Claude Code, Cursor or any stdio client:

```
claude mcp add agent-bom -- uvx agent-bom mcp server
```

Team mode is a GitHub Action on pull requests with a findings comment and SARIF into code scanning, and org mode is the Helm chart at `oci://ghcr.io/koda-ai-studio/charts/agent-bom` against your own infrastructure.

## What to ask it

- "Which of my agents can reach the AWS key, and through which package?"
- "We are adding this MCP server tomorrow. What does it pull in, and does that touch anything I would not hand to a contractor?"
- "Rank the open findings by what they can reach, not by severity."
- "Is this tool description trying to instruct my agent?" (the poisoning family, alongside `scan`)
- "Give me a delta against last week's scan of the same repository."

## The limits this guide will not paper over

- **The demo grade is not a posture.** F 37/100 is the sample environment, deliberately built to trip the gate. A real scan on a clean machine will not print that number, and neither will it print an A.
- **Offline means a 17-advisory bundled database.** Live breadth comes from OSV.dev through `check` and through an online scan. An offline run answers "would the pipeline work", not "is my estate clean today".
- **Exit code 1 is a verdict.** A non-zero exit can mean a security gate tripped or an assessment was incomplete. CI that treats any non-zero as "scanner crashed" will either ignore real findings or fail on clean code, so read the exit-code contract before wiring the gate.
- **It sees what it can discover.** Discovery covers known agent client configs, project manifests and running processes. An agent whose config lives somewhere unusual, or a credential exported into a shell profile, may fall outside the inventory. The first-run document states this caveat itself.
- **Compliance output is evidence to review.** No framework is marked compliant by this tool, and the tool says so on the screen.

## Where this sits in the catalog

The catalogue already carries three security surfaces, and none of them answer the reachability question.

[TrustScan MCP](/hermes/mcp/servers/external/trustscan-mcp/) scans one server or one skill for invisible Unicode injection, dangerous code patterns, hardcoded secrets and typosquat naming. [AgentTrust MCP](/hermes/mcp/servers/external/agenttrust-mcp/) returns a trust decision about an agent endpoint from monitoring, reliability and ownership evidence. [glc PromptGuard MCP](/hermes/mcp/servers/external/glc-promptguard-mcp/) scores a prompt, a retrieved chunk or a tool output before it reaches the model. Each inspects one artefact.

agent-bom inspects the graph between them: which agent holds which server, which server pulls which package, which package can reach which credential. That graph is also why it belongs in this catalogue rather than only in a developer one. The CorpusIQ position is that an answer is only as trustworthy as the sources behind it, and the same argument applies to the machine that produces the answer. An agent with ten servers and fourteen credentials in reach is a data-access decision, and it should be readable before the answer is trusted.

## Verification

```
uvx agent-bom scan --demo --offline   2026-11-03, agent-bom 0.113.0, 0.8s
                                      5 agents, 10 servers, 23 packages,
                                      15 vulns, exit 1 (verdict)
uvx agent-bom mcp server              initialize -> serverInfo agent-bom 0.113.0
                                      tools/list -> 8 tools
```

No account, no key, no network required for either run.

## FAQ

### Does it need an account?
No for local scans. The PyPI package is Apache-2.0 and runs offline. Account-scoped features exist only in the self-hosted org deployment.

### Is it a replacement for my dependency scanner?
No. It complements one. A dependency scanner answers "is this package vulnerable". This answers "which agent can a vulnerable package reach a credential through", and it reuses the same CVE data.

### Can it audit MCP tool descriptions?
Yes, that is the poisoning family in `scan`: it inventories the servers, reads their tool descriptions and flags instructions embedded in them.

### What does the delta look like between scans?
The second scan over the same target prints what changed since the first, which is the useful half of a weekly rescan: new CVEs against unchanged code.
