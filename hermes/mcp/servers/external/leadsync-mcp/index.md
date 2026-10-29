---
title: "LeadSync MCP - Meta Lead Ads Into Your CRM From Chat"
description: "Wire Facebook and Instagram lead forms to a CRM, a sheet or an inbox, map the fields, and find out what happened to one lead."
category: Marketing
stars: ★★ (published tools and limits verified, key required)
added: 2026-10-29
source: "published package @leadsync/mcp 0.1.1 on npm and the vendor repository lmoulton/leadsync-skills read 29 October 2026, plus the mcp.so feed card"
relevance: ★★★
tags: [lead-generation, meta-ads, facebook-lead-ads, crm, google-sheets, autoresponder, local-mcp]
last_updated: "2026-10-29"
---

# LeadSync MCP

**A lead form that stops delivering is invisible. The ad keeps spending, the form keeps accepting, and the only signal is a sales team that says the pipeline went quiet.**

```
Server type: Local (stdio)
Install:     npx -y @leadsync/mcp
Package:     @leadsync/mcp 0.1.1 on npm
Env:         LEADSYNC_API_KEY (ls_live_...)
Runtime:     Node.js 20 or later
Account:     LeadSync (free trial accepted)
```

## Why This Matters for Operators

Meta lead ads sit upstream of everything else a business does with a lead, and the connection between the form and the destination is where silent failure lives. A field gets renamed on the form, a CRM token expires, a mapping drops the phone number, and every one of those looks identical from the outside: fewer leads.

This server turns the plumbing into something an assistant can inspect. It sets up the connection between a lead form and a destination, maps the fields explicitly, adds an autoresponder, sends a test lead through the path, and answers the question an operator actually asks, which is what happened to one specific lead.

The catalogue carries ads platforms and it carries CRMs, but the join between a paid lead and the record a salesperson works is its own system, and this is the entry for it.

## What It Does

The published install surface is a package plus a set of skills:

- **`npx @leadsync/skills --claude`**, `--cursor`, `--codex`, or `--all` registers the MCP server and the skills for the clients you have.
- **`npx @leadsync/skills login`** authenticates the CLI.
- **`--project-dir <dir>`** puts Cursor's `mcp.json` in a project folder instead of the home folder. `--uninstall` removes the server and the skills again.
- **Claude Code plugin** is the alternative route: `claude plugin marketplace add lmoulton/leadsync-skills`, then `claude plugin install leadsync@leadsync-skills`. An optional API key setting can be pasted there, and it takes priority over `~/.leadsync/.env`.

A generic client takes the plain form:

```json
{
  "mcpServers": {
    "leadsync": {
      "command": "npx",
      "args": ["-y", "@leadsync/mcp"],
      "env": { "LEADSYNC_API_KEY": "ls_live_your_key_here" }
    }
  }
}
```

The work it covers, in the vendor's own words, is connecting Meta lead forms to Google Sheets, CRMs and email, mapping the fields, adding autoresponders, sending test leads, and finding out what happened to a lead.

## The Limit That Matters Most

The vendor states it plainly and it should be quoted rather than smoothed over: **the ChatGPT, Gemini and Claude web apps only connect to hosted MCP servers with a sign-in, so they cannot use this server.** It is a local stdio server, so it works in Claude Desktop, Claude Code, Cursor, Codex and Gemini CLI, and not in the browser chat surfaces.

That single sentence decides whether this entry is usable for a given team. An operator who works entirely inside a browser chat cannot reach it today, and anyone planning to standardise on hosted connectors should treat it as a desktop-side tool.

## Limits Worth Recording

A LeadSync account and a live API key are required, so no live probe was possible this pass and the tool list is not reproduced here. The entry records the install surface, the scope of the work and the client limitation, all of which are checkable without a credential.

Meta's lead form field definitions are the company's, not this server's. When a form changes on the Meta side, a mapping is a thing that needs re-checking, and no connector removes that duty.

## FAQ

### Do the ChatGPT and Claude web apps work with it?
No. The vendor states that the browser apps only connect to hosted MCP servers with a sign-in. Use Claude Desktop, Claude Code, Cursor, Codex or Gemini CLI.

### What destinations can a Meta lead form reach?
Google Sheets, CRMs, email and SMS, with field mapping, autoresponders and a test-lead path so the connection can be proven before real spend arrives.

### Can my agent tell me why one lead did not arrive?
Yes, that is one of the named jobs: find out what happened to a lead, rather than only configuring the pipe.

### Where does the API key live?
In `~/.leadsync/.env` after `login`, or in the client's keychain if you paste it into the Claude Code plugin setting, which takes priority over the env file.
