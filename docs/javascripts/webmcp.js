// WebMCP (W3C Community Group draft, webmachinelearning.github.io/webmcp):
// register read-only CorpusIQ docs tools for agentic browsers.
// Current Chrome exposes document.modelContext; older drafts exposed
// navigator.modelContext - resolve both, no-op when neither is present.
// Tools are read-only and return only public docs content.
(function () {
  if (typeof document === 'undefined') return;
  var mc = (document && document.modelContext)
        || (typeof navigator !== 'undefined' && navigator.modelContext)
        || null;
  if (!mc || typeof mc.registerTool !== 'function') return; // WebMCP not available in this browser

  var DOCS_BASE = '/docs';
  var SEARCH_INDEX = DOCS_BASE + '/search/search_index.json';

  function isSafePath(p) {
    return typeof p === 'string' && p.length > 0 && p.length < 500 && !/^[a-z]+:/i.test(p) && p.indexOf('..') === -1;
  }

  // Minimal keyword search over the mkdocs search index (title + text).
  async function searchDocs(query, limit) {
    var q = String(query || '').trim().toLowerCase();
    if (!q) return { error: 'query is required' };
    var lim = Math.min(Math.max(parseInt(limit, 10) || 5, 1), 10);
    var res = await fetch(SEARCH_INDEX, { credentials: 'omit' });
    if (!res.ok) return { error: 'search index unavailable: ' + res.status };
    var index = await res.json();
    var docs = index.docs || [];
    var scored = [];
    var tokens = q.split(/\s+/).filter(Boolean);
    for (var i = 0; i < docs.length; i++) {
      var d = docs[i];
      var title = (d.title || '').toLowerCase();
      var text = (d.text || '').toLowerCase();
      var score = 0;
      for (var t = 0; t < tokens.length; t++) {
        var tok = tokens[t];
        if (title.indexOf(tok) !== -1) score += 10;
        if (text.indexOf(tok) !== -1) score += 1;
      }
      if (score > 0) {
        scored.push({ score: score, title: d.title, url: DOCS_BASE + (d.location || ''), snippet: (d.text || '').slice(0, 300) });
      }
    }
    scored.sort(function (a, b) { return b.score - a.score; });
    return { results: scored.slice(0, lim), total_matches: scored.length };
  }

  // Fetch a page's text content (first ~3000 chars) for agent read-through.
  async function getPage(path) {
    var p = String(path || '');
    if (!isSafePath(p)) return { error: 'invalid path' };
    var url = DOCS_BASE + '/' + p.replace(/^\/+/, '');
    var res = await fetch(url, { credentials: 'omit' });
    if (!res.ok) return { error: 'page unavailable: ' + res.status };
    var html = await res.text();
    var title = (html.match(/<title>(.*?)<\/title>/i) || [])[1] || '';
    var m = html.replace(/<script[\s\S]*?<\/script>/gi, ' ').replace(/<style[\s\S]*?<\/style>/gi, ' ')
                .replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
    return { title: title, url: url, content_preview: m.slice(0, 3000) };
  }

  var registered = false;
  function register() {
    if (registered) return;
    registered = true;
    try {
      mc.registerTool({
        name: 'corpusiq_search_docs',
        description: 'Search the CorpusIQ documentation site. Returns matching page titles, URLs, and short snippets. Use for any question about CorpusIQ, MCP, connectors, or business data.',
        annotations: { readOnlyHint: true },
        inputSchema: {
          type: 'object',
          properties: {
            query: { type: 'string', description: 'Search term, e.g. "connect quickbooks to chatgpt"' },
            limit: { type: 'number', description: 'Max results (default 5, max 10)', minimum: 1, maximum: 10 }
          },
          required: ['query']
        },
        execute: function (input) { return searchDocs(input.query, input.limit); }
      });
      mc.registerTool({
        name: 'corpusiq_get_page',
        description: 'Fetch the text content of a CorpusIQ docs page by path (e.g. "quick-start", "connectors", "api/overview"). Returns the page title, URL, and the first 3000 characters of content.',
        annotations: { readOnlyHint: true },
        inputSchema: {
          type: 'object',
          properties: {
            path: { type: 'string', description: 'Docs page path without the /docs/ prefix' }
          },
          required: ['path']
        },
        execute: function (input) { return getPage(input.path); }
      });
    } catch (e) {
      // WebMCP registration failed (unsupported or restricted) - silent no-op.
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', register);
  } else {
    register();
  }
})();
