# Claude can't see CorpusIQ

You added CorpusIQ to Claude Desktop, opened a chat, and nothing
happens. No tools available. Claude doesn't mention CorpusIQ. Or you
get an error in the Claude sidebar about a missing MCP server.

The happy path is documented in
[../quickstart/02-connect-claude.md](../quickstart/02-connect-claude.md).
This page is for when the happy path didn't work.

## Cause 1: Claude Desktop wasn't restarted

Claude Desktop reads its MCP config file once, at startup. If you
edited the config while Claude was running, Claude is still using the
old config.

**Fix:** Quit Claude Desktop completely (not just close the window —
fully quit). Reopen it. Try again.

On Mac: `Cmd-Q` or right-click the dock icon → Quit. On Windows: right-
click the tray icon → Exit.

## Cause 2: Wrong config file path

The MCP config lives in different places per platform. Make sure you
edited the right one.

**Mac:**
`~/Library/Application Support/Claude/claude_desktop_config.json`

**Windows:**
`%APPDATA%\Claude\claude_desktop_config.json`
(usually `C:\Users\YourName\AppData\Roaming\Claude\claude_desktop_config.json`)

If the file doesn't exist, create it. The directory should already be
there if you've launched Claude Desktop at least once.

## Cause 3: JSON syntax error

The config file is JSON. A single missing comma or unbalanced brace
breaks the whole file, and Claude silently ignores it.

**How to check:** Paste the contents of `claude_desktop_config.json`
into any JSON validator (search "JSON validator" — there are dozens).
If it shows an error, fix the syntax.

Common slip-ups:
- Trailing comma after the last item (illegal in strict JSON).
- Smart quotes instead of straight quotes (happens if you pasted from
  a Word doc or rich-text email).
- Missing closing brace.

## Cause 4: The CorpusIQ server URL or command is wrong

The MCP config tells Claude how to reach CorpusIQ. If the URL or
command in your config doesn't match what the CorpusIQ team gave you,
Claude can't connect.

**How to check:** Compare your config entry to the exact snippet in
[../quickstart/02-connect-claude.md](../quickstart/02-connect-claude.md).
Character by character. URLs, ports, paths, and tokens must match
exactly.

## Cause 5: You haven't authenticated CorpusIQ inside Claude

Once the MCP server itself is wired up, Claude still needs you to
authenticate. When you open a new Claude chat, CorpusIQ should show as
an available MCP server in the connector sidebar with a "Connect" or
"Sign in" button. Click it and complete the CorpusIQ login.

If you don't see CorpusIQ in the sidebar at all after restarting
Claude, go back to Cause 1-4.

## Cause 6: Firewall or VPN blocking the connection

Corporate VPNs and some firewalls block outbound connections that look
unusual. If you're on a managed laptop and everything else above
checks out, try once on a personal network to confirm.

## Still stuck

Send support:
- Your operating system (Mac or Windows, version).
- The contents of `claude_desktop_config.json` (redact any tokens).
- A screenshot of Claude's MCP/connector panel.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
