---
title: "Upgrading Hermes Agent - Breaking Changes and Migration"
description: "Track Hermes Agent breaking changes by release: removed tools, renamed commands and the exact replacement for each migration step."
category: setup
tags: [hermes-agent, upgrade, migration, breaking-changes, release-notes, browser-tools]
last_updated: 2026-11-27
canonical: "https://www.corpusiq.io/docs/hermes/setup/upgrading/"
robots: "index,follow"

---

# Upgrading Hermes Agent - Breaking Changes and Migration

Most Hermes Agent upgrades ask nothing of you. A small number change something you already depend on - a tool name, a command, a config key - and those fail quietly: your prompt calls a tool that no longer exists, or a client launches a command that was renamed. The agent then reports it has no such tool, which reads like a bug rather than a migration.

This page is the checklist. It lists the breaking changes by release, the exact replacement for each, and the read-only commands that tell you what an upgrade will do before you run it.

## How do I check which version I run?

```bash
hermes --version
```

That prints the version string, the install directory and the install method (git, docker or nix). Two more commands are read-only and safe on a live machine:

| Command | What it answers |
|---|---|
| `hermes update --check` | Is a newer release available? Nothing is installed. |
| `hermes update --plan` | Which services exist, which are running, and which will be restarted. |

## How do I upgrade?

```bash
hermes update
```

The command pulls the new code (or updates the package), reinstalls dependencies and restarts the services that were running. Pre-update backups run by default: `--no-backup` skips both the quick state snapshot and the full archive, and `--backup` forces a full one. Take your own snapshot first if the machine holds work you cannot rebuild - see [Backup and Restore](/hermes/setup/backup-and-restore).

## Breaking changes in v0.23.0 (November 5, 2026)

v0.23.0 rolls up the v0.22.1 to v0.22.7 patch window and is the release most likely to touch an existing setup.

| Change | What stops working | Fix |
|---|---|---|
| Built-in browser tools removed | The ten `browser_*` tools, including `browser_navigate` and `browser_click`, no longer exist | Use `browser_exec` - mapping below |
| `hermes mcp serve` renamed | Any MCP client that launches Hermes as a server fails with an unknown command | Change the client arguments to `hermes mcp-serve`, which now lives in the official mcp-serve plugin |
| Desktop minimum OS raised | Desktop does not start on macOS 11, macOS 12 or 32-bit Windows | macOS 13 or newer, 64-bit Windows |
| Office skills merged | The separate Word, PowerPoint and Excel skills are replaced by one `microsoft-office` skill | Point prompts and skill lists at `microsoft-office`; old copies stay on disk until you remove them |
| Webapp off by default | Nothing is served to a browser tab, even on a machine that used it before | Turn on `webapp.enabled` or Web Access in Settings |

### Why did browser_navigate stop working?

Browser automation now runs through a single tool, `browser_exec`, which takes Python instead of one tool per action. The helper functions are pre-imported, and one call can navigate, read, type, click and capture in sequence.

| Removed tool | What it did | Use inside `browser_exec` |
|---|---|---|
| `browser_navigate` | Open a URL | `new_tab(url)` for the first page, `goto_url(url)` to move an existing tab |
| `browser_snapshot`, `browser_get_state` | Describe the page as text | `page_info()` |
| `browser_evaluate` | Run JavaScript in the page | `js("expression")` |
| `browser_type` | Type into a field | `fill_input(selector, text)` |
| `browser_click` | Click an element | `js("document.querySelector('selector').click()")`, or `click_at_xy(x, y)` for coordinates |
| `browser_screenshot` | Capture an image | `capture_screenshot()` |

A single call that opens a page, reads the title and saves a screenshot looks like this:

```python
# One browser_exec call: open the page, read it, capture it
new_tab("https://example.com/pricing")
wait_for_load()
print(js("document.title"))
print(page_info())
print(capture_screenshot())
```

Anything the old tools exposed through a protocol command is still available through raw CDP: `cdp("Accessibility.getFullAXTree")` returns every element's role and name, and `cdp("DOM.getBoxModel", backendNodeId=n)` returns the coordinates to click.

One caveat on the name: the removal applies to Hermes' own built-in tools. A third-party MCP server can still publish its own tools called `browser_navigate` or `browser_click` under its server namespace, so check where a tool comes from before you assume it survived or disappeared.

## Breaking changes in v0.22.0

| Change | What it means for an existing home | What to do |
|---|---|---|
| Python 3.14 is the runtime for managed installs | The installer manages the interpreter for you | Nothing, unless you pinned KittenTTS, which is unavailable on 3.14 |
| Windows desktop is MSIX-only | The NSIS and MSI installers are gone, and Windows 11 22H2 or newer is required | Reinstall through the Microsoft Store package |
| macOS builds are Apple Silicon by default | Intel Macs need a non-default build | Check before upgrading a Mac that runs every day |
| One gateway per machine is the default | Per-profile gateways are folded into the multiplexed default when nothing conflicts | Nothing; `hermes update` performs the fold |
| Idle and daily session resets retired | A chat no longer resets itself on a timer, and configs that still set `session_reset` idle or daily modes log a warning | Start a fresh chat with `/new` or `/reset` |
| Automatic session pruning is on | Ended sessions inactive for 90 days are deleted at startup; pinned and open sessions are never touched | Set `sessions.auto_prune: false` to keep everything |
| Memory providers moved to catalog plugins | Honcho, Supermemory, Hindsight, Mem0, OpenViking, Holographic, Home Assistant, Spotify and Langfuse now install as plugins | Nothing; existing homes are migrated on update or first start with data intact |
| Tool rename | `todo`, `cronjob` and `process` became `todo_list`, `cronjob_manage` and `process_manage` | Update prompts and skill files; the old names still resolve as aliases |
| Removal of the plugin compatibility layer | Plugins written against the old import path stop loading | Update the plugin to its current release |
| `hermes sync` removed | The old skill-sync command is gone | Manage skills with the curator commands instead |

### Why did my sessions disappear?

`session_reset` idle and daily resets were retired in v0.22.0, and pruning became the default in the same window. Ended sessions that have been inactive for 90 days are deleted when the agent starts; pinned sessions and sessions with an open chat are never pruned. If you need to keep everything, set `sessions.auto_prune: false` in the config. If you need the state database smaller instead, the path is [Session Cleanup](/hermes/setup/session-cleanup).

### Which command replaced hermes mcp serve?

`hermes mcp-serve`. The subcommand moved out of core into the official mcp-serve plugin, which also gained a `--tools` mode. The command itself does not rewrite anything for you: every MCP client that launches Hermes as a server carries its own argument list, so update each one after the upgrade. `hermes mcp-serve --help` prints the current options.

## How do I upgrade a machine that runs all day?

1. Read the plan: `hermes update --plan` lists every service across every profile and how each will be restarted.
2. Snapshot the state: `hermes backup` for a full archive, or let the update take its default quick snapshot.
3. Update: `hermes update`.
4. Confirm what you are running: `hermes --version`.
5. Run one chat turn, one scheduled job and one browser task before you walk away. Those three cover the surfaces that upgrades actually break.

## What if an upgrade breaks something?

Work from the symptom, because each symptom has one or two known causes:

| Symptom | First check |
|---|---|
| The agent says a tool does not exist | The browser removal and the renames above |
| An MCP client cannot start Hermes | Its arguments still say `mcp serve` |
| A scheduled job did not fire | Whether the service came back - `hermes update --plan` shows what should be running |
| A chat looks emptier than expected | Pruning defaults, then whether the session was pinned |

Configuration lives outside the install directory, so a reinstall does not erase it, and the pre-update backup is the restore path. If you report a problem, include the output of `hermes --version` and the exact error text: the version line carries the install method, which decides most triage questions.

## FAQ

### Do I have to upgrade?

No. A working machine can stay on its release. Upgrade when you want a fix or a feature, and read the section for each release between your version and the target before you do.

### Where are the full release notes?

Every documented release is in the [Hermes changelog](/hermes/changelog), with the highlights, upgrade notes and the pull requests behind each change. This page is the migration summary; the changelog is the record.

### Does an upgrade rewrite my config?

The config format gains keys with each release and old keys are usually accepted with a warning rather than removed. When a key is retired outright, the release notes say so - the `session_reset` retirement above is an example.

### Can I run two versions on one machine?

Not as one agent. A machine runs one gateway that owns its sessions, so two installs would fight over the same state. Use separate machines or separate profiles and pick one version per host.

## Related Pages

- [Hermes Agent Setup Overview](/hermes/setup) - All platform options
- [Backup and Restore](/hermes/setup/backup-and-restore) - Snapshot before you upgrade
- [Session Cleanup](/hermes/setup/session-cleanup) - Keeping the state database small
- [Hermes Changelog](/hermes/changelog) - Full notes for every release
- [Session Handoff](/hermes/knowledge/session-handoff) - Moving context between sessions
- [Troubleshooting](/hermes/troubleshooting) - Connection and gateway failures

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
