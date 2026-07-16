"""
MkDocs hook: auto-generate child-page link sections on index pages.

When an index.md has child .md files or subdirectories with their own
index.md, this hook appends an "All Pages" section at the bottom of
the index page, ensuring every child page has at least one incoming
internal link — eliminating orphan pages at build time.

Usage: add to mkdocs.yml:
    hooks:
      - scripts/hooks/auto_link_children.py
"""

import os
import re
from pathlib import Path


def on_page_content(html, page, config, files):
    """
    After Markdown is rendered to HTML, append a child-page listing
    if this is a section index page with children.
    """
    return html


def on_page_markdown(markdown, page, config, files):
    """
    Before Markdown is rendered, append child page links to index pages.
    This is the preferred hook — works before MkDocs processes the content.
    """
    # Only process section index pages (index.md in a directory with children)
    if not page.file.name == "index":
        return markdown

    docs_dir = Path(config["docs_dir"])
    # Section index pages in this repo are named either index.md or README.md
    # (MkDocs treats README.md as the directory index). Derive the section
    # directory from the source file's parent so page_dir is always the
    # containing directory, never the index file itself. The previous
    # str.replace("index.md", "") left README.md paths untouched, so page_dir
    # pointed at the file and iterdir() raised NotADirectoryError, failing the
    # whole build.
    page_dir = (docs_dir / page.file.src_path).parent

    if not page_dir.is_dir():
        return markdown

    # Find children: sibling .md files and subdirectories with their own index
    # (index.md or README.md). Skip the section's own index file so it does not
    # link to itself.
    children = []
    for item in sorted(page_dir.iterdir()):
        if item.name in ("index.md", "README.md"):
            continue
        if item.suffix == ".md":
            # Extract title from frontmatter
            title = _extract_title(item)
            slug = item.stem + ".html"
            children.append((title, slug))
        elif item.is_dir():
            child_index = None
            if (item / "index.md").exists():
                child_index = item / "index.md"
            elif (item / "README.md").exists():
                child_index = item / "README.md"
            if child_index is not None:
                title = _extract_title(child_index)
                slug = item.name + "/index.html"
                children.append((title, slug))

    if not children:
        return markdown

    # Check if the page already has a child-page listing section
    if "## All Pages" in markdown or "## All " in markdown:
        return markdown

    # Build the listing
    lines = ["\n\n## All Pages\n"]
    current_dir = page_dir.name if page_dir != docs_dir else ""
    for title, slug in children:
        # Compute relative URL from this index page
        lines.append(f"- [{title}]({slug})\n")

    return markdown + "\n".join(lines)


def _extract_title(md_path):
    """Extract title from markdown frontmatter. Accepts str or Path."""
    md_path = Path(md_path)
    try:
        with open(md_path) as f:
            content = f.read()
        if content.startswith("---"):
            end = content.find("---", 3)
            if end != -1:
                fm = content[3:end]
                m = re.search(r'title:\s*"(.*?)"', fm)
                if m:
                    return m.group(1)
        # Fallback: first heading
        m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        if m:
            return m.group(1)
    except Exception:
        pass
    return md_path.stem.replace("-", " ").title()
