---
title: "kosa8 MCP - Sealed microVMs You Can Rewind"
description: "A local MCP gateway that runs each tool server in its own microVM, pins tool definitions against change, and checkpoints a whole machine in under a second."
category: Security
stars: n/a (vendor licence, 14-day trial then from 29 USD a month)
added: 2026-10-31
source: "The mcp.so homepage recentServers block on 2026-10-31 at 03:22Z under the slug kosa8, verified and featured, plus HTTP 200 reads on kosa8.com, kosa8.com/pricing/ and kosa8.com/download/, HTTP 200 on github.com/kosa8ai/kosa8-claude-plugin with its README, and the vendor documentation at docs.kosa8.com including the tool server page that describes the gateway, per-server sandboxes and tool definition pinning"
relevance: ★★★
tags: [sandbox, microvm, agent-security, mcp-gateway, checkpoint, egress-broker, tool-pinning, local-mcp, mit-plugin]
last_updated: "2026-10-31"
---

# kosa8 MCP

**A tool server is somebody else's program, installed a moment before it starts, running with your files and your keys. kosa8 answers that with one machine per server, and answers the quieter risk, a tool description rewritten after you approved it, by pinning the definitions and withholding the change.**

```
Server type: Local (stdio gateway, optional HTTP on loopback)
Install:     kosa8.com/download, then `kosa8 mcp serve`
Auth:        vendor licence, 14-day trial without a card, plans from 29 USD/month
Platforms:   Apple-silicon Mac, x86-64 Linux, Windows through WSL2 preview
Plugin:      github.com/kosa8ai/kosa8-claude-plugin (MIT)
Docs:        docs.kosa8.com, release v0.11.0
```

The client configuration is one entry, because the gateway is the single server the assistant ever sees:

```json
{
  "mcpServers": {
    "kosa8": {
      "command": "kosa8",
      "args": ["mcp", "serve"]
    }
  }
}
```

Claude Code reaches the same thing through the plugin marketplace, with `/plugin marketplace add kosa8ai/kosa8-claude-plugin` followed by `/plugin install kosa8@kosa8`, which adds slash commands for status, sandbox, checkpoint, rewind and a parallel-fork explore.

## What it does

kosa8 gives an assistant a sealed computer and a way to save it, copy it and put it back. The MCP surface sits on top of that machine:

- **Thirty built-in tools** served by the gateway itself, sandbox creation among them, so the assistant can make a machine, run code in it, read and write files and take a checkpoint without a second program.
- **Tool servers registered into their own sandboxes.** Each one runs as a container in a sandbox named `mcp-NAME`, with the network rule you gave it, and a server that needs no network gets none.
- **One gateway, namespaced tools.** A server called `github` offering `create_issue` appears to the model as `github_create_issue`, its description prefixed with `[github via kosa8 sandbox mcp-github]` and marked as potentially destructive so clients that ask before destructive calls will ask. A name collision is skipped rather than allowed to shadow, and the name `kosa8` is reserved for the built-in set.
- **Pinned tool definitions**, covered below, with `kosa8 mcp pins show` to read what was pinned.
- **Checkpoint, rewind and fork** on the running machine, memory and processes included, at roughly 0.7 seconds to save and about a second to restore, with fork producing live copies to try several approaches at once.
- **Approvals and audit**: one or two named approvers on risky actions, and a hash-chained, tamper-evident log of every decision.

## The pin is the control the ecosystem was missing

Every permission model built for MCP so far watches the wrong object. It watches the tool name, the argument schema and sometimes the server identity, and all three stay constant while the thing the model actually reads changes. A tool description is prose, and a model follows prose. A server that edits its description has changed what your assistant will do without changing one field a permission list can see, which is the attack the literature calls a rug pull and the reason it keeps working.

kosa8 pins each tool definition on first use and then refuses the change: a later edit to any pinned definition is withheld until a person approves it. That single move converts the description from mutable marketing copy into evidence, and it is the difference between an allow-list of names and an allow-list of behaviour. The check worth running in a trial is whether the pin covers the argument schema and the annotations as well as the prose, because a server that keeps its description and widens what a parameter accepts has moved the same ground.

## Isolation is per server, not per agent

The usual way to launch a third-party server is `npx` or `pip` moments before it starts, which means it runs as you, with your files, your SSH keys and your whole network, and it is trusted by default because the alternative is reading the source first. Here each server gets a real microVM with its own kernel rather than a container sharing yours, its own egress rule, and no visibility of the other servers or of your workspace beyond the one folder you granted.

The credentials design follows from the same reasoning: an egress broker on the host injects API keys on the way out, so the sandbox holds a placeholder and the agent never possesses the value. That is the same inversion the catalogue records in [offprompt MCP](/hermes/mcp/servers/external/offprompt-mcp/), arrived at from the other end, where the key is kept from the agent at the networking layer instead of at a collection page.

## Checkpoint and fork change what an agent can attempt

An agent that cannot undo works carefully, and careful is expensive: it plans for the failure instead of trying the step. A machine that saves in under a second and restores in about one is a different proposition, because the failing step becomes cheap to retry rather than a reason to replan, and fork turns one attempt into a comparison of three. This is the part that reads as convenience and is actually a containment feature, since the safe move is the one that can be rolled back.

## What this pass did not establish

Nothing was installed or executed, so the thirty tools, the 213 documented commands and the checkpoint timings are the vendor's publications and not measurements taken here. The documentation link on the mcp.so card points at `kosa8.com/docs`, which answers 404; the live documentation is at `docs.kosa8.com`. The plugin repository is MIT, which covers the plugin, while the daemon itself is a signed and notarised download, so the audit a security reviewer wants to do on the part that runs the VMs cannot be done from the repository. Four questions a trial should settle: whether pins cover schemas and annotations as well as descriptions, whether an approval is replayable once granted, whether the HTTP mode is genuinely loopback-only without the explicit unsafe flag, and what the daemon does on a machine whose kernel the microVM layer does not support.

## FAQ

### Does kosa8 replace my MCP client?
No. Your client stays the client and kosa8 becomes the single server it is configured with, fronting the tool servers you register. Everything it does not front is unchanged.

### Is it only for Claude Code?
No. Any MCP client that launches a stdio command works, and there is an HTTP mode with a bearer token on loopback. The plugin, the slash commands and the bundled agents are Claude Code packaging.

### What does it cost?
A 14-day trial without a card, then plans from 29 USD a month per the vendor pricing page.

### Is the source open?
The Claude Code plugin repository is MIT. The daemon that runs the microVMs is distributed as a signed, notarised binary from kosa8.com, so this entry does not claim a licence for it.

## See Also

- [Superserve MCP - Sandbox Infrastructure for AI Agents](/hermes/mcp/servers/external/superserve-mcp/) - cloud sandboxes rather than local ones, without the checkpoint and fork surface
- [offprompt MCP - API Keys That Never Enter the Chat](/hermes/mcp/servers/external/offprompt-mcp/) - keeping a credential out of the transcript from the client side
- [Poison Armor MCP: Prompt-Injection Firewall for AI Agents](/hermes/mcp/servers/external/poison-armor-mcp/) - screening the text that reaches the model rather than the tool definition
- [WatchCron MCP - Know When a Job Stops Reporting](/hermes/mcp/servers/external/watchcron-mcp/) - the monitoring layer an agent-operated machine still needs
