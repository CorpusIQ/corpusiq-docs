# 2. Connect CorpusIQ to Claude

CorpusIQ runs as an **MCP server** — a standard way for AI assistants to talk
to outside data. Claude Desktop has built-in MCP support, so this takes about
two minutes.

## Prerequisites

- A CorpusIQ account ([step 1](01-create-account.md)).
- **Claude Desktop** installed (free download from anthropic.com). The browser
  version of Claude does not currently support MCP connectors.

## Steps

1. In CorpusIQ, open **Settings → Integrations → Claude Desktop**. Copy the
   MCP configuration block we generate for you. It contains your personal API
   token — don't share it.
2. Open Claude Desktop. Click your name → **Settings → Developer →
   Edit Config**. This opens `claude_desktop_config.json` in your editor.
3. Paste the block from CorpusIQ into the `mcpServers` section. If the file
   was empty, just paste the whole thing.
4. Save the file and fully quit Claude Desktop (not just close the window —
   quit it from the menu bar).
5. Reopen Claude. You should see a small plug/tools icon near the message box
   indicating MCP tools are available.

<!-- screenshot: CorpusIQ Integrations panel showing Claude config block -->
<!-- screenshot: Claude Desktop Developer settings -->
<!-- screenshot: Claude conversation with the MCP tools indicator -->

## Verify it's working

In Claude, type:

> What CorpusIQ connectors do I have configured?

You should get back a status table listing every connector — most marked
"Not connected" since you haven't authenticated any yet. That's expected.

## Next

[4. Authenticate your first connector →](04-first-connector.md)

## Trouble?

- Claude doesn't show the tools icon → see
  [Claude can't see CorpusIQ](../troubleshooting/claude-cant-see-corpusiq.md).
- "Invalid JSON" error → the config block must be valid JSON; re-copy from
  CorpusIQ instead of hand-editing.
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
