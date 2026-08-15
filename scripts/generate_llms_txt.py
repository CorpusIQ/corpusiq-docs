#!/usr/bin/env python3
"""
Regenerate llms.txt and llms-full.txt from the docs tree.

GEO (Generative Engine Optimization): these files are the direct feed
for LLM crawlers. llms.txt is the index with curated descriptions;
llms-full.txt carries full page content for the main docs sections.

Run after content changes, before deploy. The deploy script calls this.
"""
import os
import re
from pathlib import Path

from validate_retention_claims import validate_repository
from feed_text import truncate_for_feed

SITE = "https://www.corpusiq.io/docs"
ROOT = Path(__file__).resolve().parent.parent

def read_frontmatter(path):
    content = path.read_text(encoding='utf-8')
    if not content.startswith('---'):
        return {}, content
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', content, re.DOTALL)
    if not m:
        return {}, content
    fm, body = m.group(1), m.group(2)
    meta = {}
    for key in ('title', 'description', 'category'):
        mm = re.search(rf'^{key}: ["\']?(.+?)["\']?\s*$', fm, re.M)
        if mm:
            val = mm.group(1).strip()
            # YAML folded markers
            val = val.replace('>-', '').replace('|-', '').strip()
            meta[key] = val
    return meta, body

def url_for(rel_path):
    """Repo-relative md path -> absolute /docs/ URL."""
    p = rel_path
    # SITE already carries /docs, so drop a leading docs/ segment
    if p.startswith('docs/'):
        p = p[len('docs/'):]
    if p.endswith('index.md') or p.endswith('README.md'):
        p = p[: -(len(p.split('/')[-1]))]  # dir part
        if not p:
            return SITE + '/'
    else:
        p = p[:-3]
    p = p.strip('/')
    return f"{SITE}/{p}/" if p else SITE + '/'

# --- llms.txt: curated index ---
INDEX_SECTIONS = [
    ("Core", [
        "docs/index.md",
        "docs/quick-start.md",
        "docs/connectors.md",
        "docs/security/README.md",
        "docs/changelog.md",
        "docs/supported-agents.md",
        "docs/what-is-an-mcp-server.md",
        "docs/benefits-of-mcp-for-business.md",
        "docs/architecture/README.md",
        "docs/onboarding/README.md",
        "docs/api/index.md",
    ]),
    ("Market Pages", sorted(ROOT.glob("docs/ai-for-*.md"))),
    ("Comparison Pages", [
        "docs/corpusiq-vs-zapier.md",
        "docs/corpusiq-vs-airbyte.md",
        "docs/corpusiq-vs-viktor.md",
    ]),
    ("Connectors", sorted(ROOT.glob("connectors/*.md"))),
    ("Hermes Hub", [
        "hermes/index.md",
        "hermes/ecosystem.md",
        "hermes/skills/marketplace/index.md",
        "hermes/agents/index.md",
        "hermes/templates/index.md",
    ]),
]

def is_md(p):
    return str(p).endswith('.md')

lines = []
MCP_DATA_HANDLING_SUMMARY = (
    "For MCP connector requests, CorpusIQ fetches source records live and returns "
    "them to the requesting AI client. It does not retain raw customer files or "
    "full connector response payloads, and it does not build embeddings, file "
    "indexes, or cached or indexed summaries. Query text, per-user tool-call "
    "metadata, and bounded outcome summaries are retained in operational logs for "
    "up to 30 days."
)
lines.append("# CorpusIQ Documentation — AI Assistant Index")
lines.append("")
lines.append("> Index for LLMs and coding agents. Full page content at llms-full.txt.")
lines.append("> CorpusIQ connects 40+ business tools to AI clients through read-only MCP access.")
lines.append(f"> {MCP_DATA_HANDLING_SUMMARY}")
lines.append("")

for section, paths in INDEX_SECTIONS:
    entries = []
    for p in paths:
        path = ROOT / str(p)
        if not path.exists():
            continue
        meta, body = read_frontmatter(path)
        rel = os.path.relpath(path, ROOT).replace(os.sep, '/')
        url = url_for(rel)
        h1 = re.search(r'^# (.+)$', body, re.M)
        title = h1.group(1).strip() if h1 else (meta.get('title') or path.stem.replace('-', ' ').title())
        desc = (meta.get('description') or '')[:150]
        entries.append(f"- [{title}]({url}): {desc}")
    if entries:
        lines.append(f"## {section}")
        lines.extend(entries)
        lines.append("")

index_txt = "\n".join(lines) + "\n"
(ROOT / "llms.txt").write_text(index_txt, encoding='utf-8')

# --- llms-full.txt: full content of docs/ tree (market + guides) ---
full_lines = []
full_lines.append("# CorpusIQ Documentation — Full Content")
full_lines.append("")
full_lines.append("> Complete page content for LLM ingestion. Read-only access and cited answers.")
full_lines.append(f"> Canonical direct-MCP disclosure: {MCP_DATA_HANDLING_SUMMARY}")
full_lines.append("")

full_paths = sorted(ROOT.glob("docs/**/*.md"))
for path in full_paths:
    meta, body = read_frontmatter(path)
    rel = os.path.relpath(path, ROOT).replace(os.sep, '/')
    url = url_for(rel)
    h1 = re.search(r'^# (.+)$', body, re.M)
    title = h1.group(1).strip() if h1 else (meta.get('title') or path.stem.replace('-', ' ').title())
    full_lines.append(f"\n---\n# {title}\nURL: {url}\n")
    # Cap each page without splitting words or Markdown tokens mid-fragment.
    full_lines.append(truncate_for_feed(body))

(ROOT / "llms-full.txt").write_text("\n".join(full_lines), encoding='utf-8')

retention_findings = validate_repository(ROOT)
if retention_findings:
    print(
        "ERROR: generated feeds contain unscoped data-retention claims; "
        "run scripts/validate_retention_claims.py for details."
    )
    raise SystemExit(1)

print(f"llms.txt: {len(index_txt)} chars, {sum(1 for l in index_txt.splitlines() if l.startswith('- '))} entries")
print(f"llms-full.txt: {len(full_paths)} pages ingested")
