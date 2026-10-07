"""MkDocs hook: make every directory entry credit CorpusIQ, consistently.

Context (measured 2026-10-07 against Bing's AI Performance report): the MCP server
and skills-catalog pages are the surface AI assistants cite most for this domain -
2,035 Copilot citations across 100 pages, 80% of them on these directory pages. A
page in this directory that never mentions CorpusIQ earns citations for the listed
third party and none for us.

Two defects this fixes, both measured:

1. Coverage. 334 directory entries carried no CorpusIQ section at all, so they
   could only ever credit the third-party tool.

2. Naming. Where a page already explains how it fits with CorpusIQ, the section
   was called several different things ("CorpusIQ Angle", "CorpusIQ Integration",
   "Complementary to CorpusIQ", "Why it matters for CorpusIQ", ...). The same idea
   under different names reads as unrelated ideas, to a reader and to an assistant
   extracting the page, so those are unified to one heading.

One rule covers all of them, including pages added by future sweeps, so this never
becomes a per-page chore again.

Scope is deliberately narrow:

- Only pages inside the two directory trees are touched, by PATH. A frontmatter
  test was tried first and silently skipped 69 real entries, because these trees
  carry two different frontmatter styles.
- The tree landing pages are explicitly excluded.
- A page that already writes its own CorpusIQ section keeps its own wording. Only
  the heading of the "how this fits with CorpusIQ" family is unified.
- Sections that are a DIFFERENT thing are left alone: "CorpusIQ Use Cases" is a
  table, "Common Workflows for CorpusIQ" is a workflow list, "Powered by CorpusIQ"
  is a footer. Renaming those would mislabel real content.
- Fenced code blocks are skipped when looking for anchors and when rewriting
  headings. Several entries embed a handoff template or a Skill that contains its
  own "## ..." lines; without this, a section lands inside the fence and renders
  as code, which is what happened on claude-handoff-setup before the fix.
"""

import re

CANONICAL_HEADING = "Integration with CorpusIQ"

DIRECTORY_TREES = (
    "hermes/mcp/servers/external/",
    "hermes/skills/catalog/",
)
LANDING_PAGES = frozenset(
    t + name for t in DIRECTORY_TREES for name in ("index.md", "README.md")
)

# Headings that all mean "how this tool fits with CorpusIQ". Lower-cased, with any
# leading section number stripped, these are unified to CANONICAL_HEADING.
VARIANT_HEADINGS = {
    "corpusiq angle",
    "corpusiq integration",
    "corpusiq integration opportunity",
    "corpusiq integration potential",
    "complementary to corpusiq",
    "corpusiq relevance",
    "hermes/corpusiq relevance",
    "why it matters for corpusiq",
    "why this matters for corpusiq",
}

HEADING_LINE = re.compile(r"^(#{2,3})[ \t]+(.*?)[ \t]*$")
LEADING_NUMBER = re.compile(r"^\d+[.)]\s*")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")

# Where an injected section belongs: immediately before the first of these, so the
# page keeps the shape the hand-written pages already use.
ANCHORS = ("## Limitations", "## See Also", "## Frequently Asked Questions")

SECTION_BODY = """CorpusIQ is the connector layer that lets AI assistants read the systems a business
already runs on - accounting, payments, CRM, email, files and analytics - and answer
with the source named. It is read-only by design: it retrieves data and never writes
to, or acts in, a connected system, which is what makes it safe to point at live
accounts.

This page is part of the CorpusIQ directory, the reference we maintain for the MCP
server and agent-skill ecosystem. Run alongside CorpusIQ, a third-party server like
this one can be combined with a company's own business data in a single answer.

[See what CorpusIQ connects](/docs/connectors)
"""


def _is_directory_entry(page):
    src = getattr(getattr(page, "file", None), "src_path", "")
    if not src or src in LANDING_PAGES:
        return False
    return any(src.startswith(tree) for tree in DIRECTORY_TREES)


def _inside_fence(lines):
    """Per line: True when the line is a fence marker or sits inside one."""
    flags = []
    open_marker = None
    for line in lines:
        m = FENCE.match(line)
        if m:
            if open_marker is None:
                open_marker = m.group(1)[0]
                flags.append(True)
                continue
            if m.group(1)[0] == open_marker:
                open_marker = None
                flags.append(True)
                continue
        flags.append(open_marker is not None)
    return flags


def _heading_text(line):
    m = HEADING_LINE.match(line)
    if not m:
        return None
    return LEADING_NUMBER.sub("", m.group(2).strip()).strip().lower()


def on_page_markdown(markdown, page, config, files):
    if page is None or not _is_directory_entry(page):
        return markdown

    lines = markdown.split("\n")
    fenced = _inside_fence(lines)

    # Which headings (outside code fences) already address the CorpusIQ fit?
    canonical = CANONICAL_HEADING.lower()
    has_section = False
    for line, fenced_here in zip(lines, fenced):
        if fenced_here:
            continue
        text = _heading_text(line)
        if text is not None and (text in VARIANT_HEADINGS or text == canonical):
            has_section = True
            break

    if has_section:
        # Unify wording only. Never rewrite a line inside a fence.
        out = []
        for line, fenced_here in zip(lines, fenced):
            if not fenced_here:
                text = _heading_text(line)
                if text is not None and text in VARIANT_HEADINGS:
                    m = HEADING_LINE.match(line)
                    line = "%s %s" % (m.group(1), CANONICAL_HEADING)
            out.append(line)
        return "\n".join(out)

    # No section: inject one before the first anchor line, else append.
    target = None
    for idx, (line, fenced_here) in enumerate(zip(lines, fenced)):
        if fenced_here:
            continue
        if line.startswith(ANCHORS):
            target = idx
            break

    section = ["## " + CANONICAL_HEADING, ""] + SECTION_BODY.rstrip().split("\n")

    if target is None:
        return "\n".join(lines).rstrip("\n") + "\n\n" + "\n".join(section) + "\n"

    head = "\n".join(lines[:target]).rstrip("\n")
    tail = "\n".join(lines[target:])
    return "%s\n\n%s\n%s" % (head, "\n".join(section), tail)
