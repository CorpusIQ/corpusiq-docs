---
title: "3. Connect CorpusIQ to ChatGPT - CorpusIQ Docs"
description: "Use CorpusIQ inside ChatGPT through two paths: the CorpusIQ app on the ChatGPT app store, or the MCP connector route for desktop and agent use."
last_updated: "2026-11-02"
---

# 3. Connect CorpusIQ to ChatGPT

CorpusIQ works with ChatGPT through two paths. Pick whichever fits.

## Option A - CorpusIQ app in ChatGPT (easiest)

If you have ChatGPT Plus, Pro, Team, or Enterprise:

1. Open the listing: **[CorpusIQ on ChatGPT](https://chatgpt.com/plugins/plugin_asdk_app_6a9f5d19efbc8191b9d5a5fd4be12426)**.
   You can also search "CorpusIQ" in ChatGPT.
2. Click **Connect** on the listing. ChatGPT will ask you to authorize
   CorpusIQ on first use - a single click-through.
3. After auth, ask ChatGPT business questions and it will use your connected
   CorpusIQ sources.

<!-- screenshot: CorpusIQ listing in the ChatGPT plugin directory -->
<!-- screenshot: OAuth approval prompt -->

## Option B - ChatGPT MCP connector (Enterprise / direct)

If you're on ChatGPT Enterprise or want to wire CorpusIQ as a first-class MCP
tool source:

1. In CorpusIQ, **Settings → Integrations → ChatGPT MCP**. Copy the **MCP
   server URL** and **personal token**.
2. In ChatGPT, open **Settings → Connectors → Add MCP server**.
3. Paste the URL and token. Save.
4. In a new chat, click the tools icon and confirm "CorpusIQ" is listed.

<!-- screenshot: ChatGPT Connectors settings -->

## If you previously used a Custom GPT

OpenAI retires custom GPTs on **December 11, 2026** (February 11, 2027 only for
FedRAMP and Enterprise workspaces with an approved deferral). Custom GPT
actions do not transfer during migration. Move to Option A above: the CorpusIQ
listing in the ChatGPT app store is the supported path and needs no GPT of your
own.

## Verify it's working

Ask:

> List my CorpusIQ connectors and their status.

You should see a status table. Most connectors will say "Not connected" until
you authenticate them - that's the next step.

## Next

[4. Authenticate your first connector →](04-first-connector.md)

## Trouble?

See [ChatGPT can't see CorpusIQ](../troubleshooting/chatgpt-cant-see-corpusiq.md).

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
