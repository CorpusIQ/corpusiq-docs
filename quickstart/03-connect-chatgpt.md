# 3. Connect CorpusIQ to ChatGPT

CorpusIQ works with ChatGPT through two paths. Pick whichever fits.

## Option A — CorpusIQ Custom GPT (easiest)

If you have ChatGPT Plus, Pro, or Team:

1. In CorpusIQ, open **Settings → Integrations → ChatGPT**. Click **Open
   CorpusIQ GPT**. This takes you to our published Custom GPT in the GPT
   Store.
2. Click **Start chat**. ChatGPT will ask you to authenticate to CorpusIQ on
   first use — a single click-through.
3. After auth, you can ask the GPT business questions and it will use your
   connected CorpusIQ sources.

<!-- screenshot: CorpusIQ Custom GPT landing page -->
<!-- screenshot: OAuth approval prompt -->

## Option B — ChatGPT MCP connector (Enterprise / direct)

If you're on ChatGPT Enterprise or want to wire CorpusIQ as a first-class MCP
tool source:

1. In CorpusIQ, **Settings → Integrations → ChatGPT MCP**. Copy the **MCP
   server URL** and **personal token**.
2. In ChatGPT, open **Settings → Connectors → Add MCP server**.
3. Paste the URL and token. Save.
4. In a new chat, click the tools icon and confirm "CorpusIQ" is listed.

<!-- screenshot: ChatGPT Connectors settings -->

## Verify it's working

Ask:

> List my CorpusIQ connectors and their status.

You should see a status table. Most connectors will say "Not connected" until
you authenticate them — that's the next step.

## Next

[4. Authenticate your first connector →](04-first-connector.md)

## Trouble?

See [ChatGPT can't see CorpusIQ](../troubleshooting/chatgpt-cant-see-corpusiq.md).
