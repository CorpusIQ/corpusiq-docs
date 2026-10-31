---
title: offprompt MCP - API Keys That Never Enter the Chat
description: "Local MCP that opens a 127.0.0.1 page to collect an API key and writes it to .env.local, so the agent only ever sees the key name and a fingerprint."
category: Developer Tools
stars: n/a (new listing, npm 0.3.0)
added: 2026-10-30
source: "mcp.so homepage recentServers block on 2026-10-30 at 18:28Z under the slug offprompt, verified and featured, submitted by Valerio Leo, plus the npm registry record for offprompt at 0.3.0 (MIT, engines node >=22, zero runtime dependencies, bin offprompt, repository github.com/offprompt/offprompt) and HTTP 200 reads on github.com/offprompt/offprompt and offprompt.dev; there is no remote endpoint to probe because the server is local stdio"
relevance: ★★
tags: [secrets, api-keys, security, developer-tools, env, stdio, local, mit]
last_updated: "2026-10-30"
---

# offprompt MCP

**Every credential problem in agent work has the same shape: the shortest path to a working integration runs through the model's context, and once a key is in a transcript, it is in a log, a cache and a provider's retention window too.**

offprompt inverts that path. The server is a local stdio MCP that, when an agent needs a secret, opens a page on `127.0.0.1` in your browser, lets you type the value there, and writes it straight into `.env.local` or a file you choose. The agent gets back the key's name and a fingerprint, never the value.

```
Server type: local stdio over npm
Package:     offprompt 0.3.0 (MIT)
Install:     npx -y offprompt mcp  after  npx offprompt init
Runtime:     Node 22 or later, zero runtime dependencies
Tools:       collect_secret, await_secret, cancel_secret
Page:        127.0.0.1 in your browser, no remote code loaded
Output:      .env.local in the project, or a file you name
Repository:  github.com/offprompt/offprompt
```

Manual configuration, for a client that does not get set up by `init`:

```json
{
  "mcpServers": {
    "offprompt": {
      "command": "npx",
      "args": ["-y", "offprompt", "mcp"]
    }
  }
}
```

## What it does

`npx offprompt init` runs in a project, detects the coding agents installed there and registers the server for them. From then on, when a task needs a credential, the agent calls `collect_secret` with a key name and a provider, the page opens, the value is typed by a person and lands in the env file. `await_secret` covers the case where the agent must wait for the human step to finish rather than racing past it, and `cancel_secret` is the abort path that a two-tool design usually forgets.

Three tools is the right surface for this job. Every added tool is another way for the model to ask for something, and the whole point of this server is that it asks for exactly one thing and then gets out of the way.

## Intake and retrieval are different problems

The catalogue already carries [Vaultwarden MCP](/hermes/mcp/servers/external/vaultwarden-mcp/), which keeps vault passwords behind a desktop approval window, and the shared principle is the same. The use case is not.

A vault exists to give an agent read access to credentials that are already stored, for an account a business already runs. offprompt solves the earlier moment: a project needs a new key during a build, the developer does not want to paste it into a chat window, and the file that will consume it is `.env.local` on this machine. One is retrieval from a system of record. The other is intake into a working tree, and the failure mode of doing it the usual way is a key pasted into a transcript that then gets summarised, cached and shared.

That distinction is why this entry is filed under developer tooling rather than security infrastructure. The server does not hold a vault and does not store anything: the value goes where you would have put it by hand.

## The fingerprint is the design decision worth copying

An agent that cannot see the value still has to know that the write worked, and it has to know which key it holds when a project has three Stripe keys for three environments. The vendor's answer is a **fingerprint**: a derived, non-reversible marker returned instead of the value, so the agent can confirm identity and success without ever holding the secret.

That is the correct shape for any tool in this class, and it is worth stating why plainly. A tool that returns "ok" leaves the agent unable to distinguish a key it just collected from the one that was already in the file, which is exactly the confusion that produces a production key in a staging test. A fingerprint is checkable, loggable and useless to anyone reading the log.

## Format validation as a second gate

The page checks the pasted value against **65 provider formats** as it is typed, naming Stripe, OpenAI, Anthropic, AWS and Supabase among others. In practice this catches the two mistakes that actually happen: the wrong key copied from a dashboard with three of them, and a truncated paste.

The value of the check is timing rather than correctness. A malformed key caught at the page costs one retype; the same key written to `.env.local` costs a confusing 401 an hour later, at the point where the agent is already mid-task and reporting the wrong cause.

## The cloud sandbox path is the trade to make deliberately

The vendor supports agents running in a remote sandbox by reaching your browser through a **Cloudflare quick tunnel**. That is the honest solution to a real problem, since `127.0.0.1` inside a container is not your laptop, but it changes the threat model: a one-page tunnel is still a publicly reachable URL while it lives, and the property that makes the local mode strong, that nothing leaves the machine, does not survive the move.

The right reading is not that the feature is unsafe but that it should be a deliberate choice: use the local page when the agent runs locally, and treat the tunneled path as exposing a credential-entry form to the internet for the length of the session. A buyer should confirm the tunnel is created per collection, torn down after the write, and that the page requires something the URL alone does not carry.

## Supply chain is unusually thin, and that is checkable

The npm record carries **zero runtime dependencies** and a single `bin` entry, which for a security tool is not a footnote. A package that installs nothing inherits nothing: no transitive dependency gets a hook into a step whose entire job is handling secrets. The engine floor is Node 22, and the licence is MIT with the repository public at `github.com/offprompt/offprompt`, so the claim can be read rather than trusted.

## What this pass did not establish

Nothing was installed or executed here. The three tool names come from the vendor's published description, the version, licence, dependency count and Node floor come from the npm registry record, and the repository and site both answer HTTP 200. What is not established: whether `await_secret` blocks the call or returns a token to poll, whether the file write is restricted to known env filenames or accepts any path the agent names, and whether the tunnel is scoped to a single collection. The last two decide how much the design is worth, and both are one install away from being answered.

## FAQ

### Does the agent ever see the key?
No. Per the vendor, it receives the key's name, a fingerprint and whether the write succeeded. The value goes from the browser page to the file.

### Does it work with Claude Code, Cursor and Codex?
Yes, and `offprompt init` registers the server for the agents it detects. It is a standard stdio MCP server, so any client that can launch `npx` can run it.

### Where is the secret stored?
In the project's `.env.local`, or a file you name, which is where it would have gone by hand. Nothing is held by the server or sent to a third party in local mode.

### Is there a hosted version?
No. It is a local package under MIT, which is the point: the credential path stays on the machine that owns the project.

## See Also

- [Vaultwarden MCP - Self-Hosted Password Vault Access](/hermes/mcp/servers/external/vaultwarden-mcp/) - the retrieval side of the same principle
- [Vetting an MCP Server Before You Connect It](/hermes/guides/vetting-an-mcp-server) - the ten-minute check that starts with narrowing the credential
- [NexaLayer MCP - Proxy Sessions That Cap Their Spend](/hermes/mcp/servers/external/nexalayer-mcp/) - the other half of agent credential safety, bounding what a key can cost
