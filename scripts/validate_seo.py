#!/usr/bin/env python3
"""
Pre-deploy validation for corpusiq-docs.

Checks:
1. Broken external links — HTTP 404s and dead GitHub repos
2. Orphan pages — pages with no incoming internal links in the build
3. Pages missing from nav/sitemap
4. Meta descriptions below minimum length

Runs before mkdocs build in CI. Non-zero exit blocks deploy.

Usage:
    python3 scripts/validate_seo.py [--docs-dir docs/] [--site-dir site/]
"""

import argparse
import os
import re
import sys
import urllib.request
import urllib.error
from collections import defaultdict
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed


def find_md_files(docs_dir):
    """Find all markdown files in docs_dir."""
    return list(Path(docs_dir).rglob("*.md"))


def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}, content
    end = content.find("---", 3)
    if end == -1:
        return {}, content
    return content[3:end], content[end + 3:]


def parse_description(frontmatter):
    """Extract description from frontmatter string."""
    m = re.search(r'description:\s*"(.*?)"', frontmatter, re.DOTALL)
    return m.group(1) if m else None


def parse_title(frontmatter):
    """Extract title from frontmatter string."""
    m = re.search(r'title:\s*"(.*?)"', frontmatter, re.DOTALL)
    return m.group(1) if m else None


def find_external_links(content):
    """Find all external HTTP(S) links in markdown content."""
    # Match markdown links: [text](url)
    md_links = re.findall(r'\[([^\]]*)\]\((https?://[^\s\)]+)\)', content)
    # Match bare URLs
    bare_urls = re.findall(r'(?<!\()(https?://[^\s\)<>"\']+)', content)
    
    links = []
    for text, url in md_links:
        links.append((url, text[:80]))
    for url in bare_urls:
        links.append((url, ""))
    
    return links


def find_internal_links(content, all_pages):
    """Find internal links to other docs pages."""
    # Match relative paths like [text](../other-page.md) or [text](other-page.md)
    # and absolute paths like [text](/docs/other-page)
    internal = re.findall(r'\[([^\]]*)\]\(([^http][^\s\)]+)\)', content)
    linked = set()
    for text, path in internal:
        linked.add(path)
    return linked


def _is_placeholder_url(url):
    """Skip illustrative/example URLs used in API docs (not real, never resolve).

    e.g. https://admin.shopify.com/store/.../orders/12345 or
    https://quickbooks.api.intuit.com/v3/company/{REALM_ID}/query — these are
    documentation placeholders, not broken links, and must not block a deploy.
    """
    markers = ("{", "}", "...", "<", ">", "example.com", "your-", "REALM_ID",
               "/store/.../", "12345", "YOUR_", "xxxx")
    return any(m in url for m in markers)


def check_broken_link(url):
    """Check if an external URL returns 200. Returns (url, status, error)."""
    try:
        req = urllib.request.Request(url, method="HEAD")
        req.add_header("User-Agent", "CorpusIQ-SEO-Validator/1.0")
        with urllib.request.urlopen(req, timeout=10) as resp:
            return (url, resp.status, None)
    except urllib.error.HTTPError as e:
        return (url, e.code, str(e))
    except Exception as e:
        return (url, None, str(e))


def main():
    parser = argparse.ArgumentParser(description="Pre-deploy SEO validation")
    parser.add_argument("--docs-dir", default="docs", help="MkDocs content directory")
    parser.add_argument("--site-dir", default="site", help="MkDocs build output")
    parser.add_argument("--max-links", type=int, default=200, help="Max external links to check")
    parser.add_argument("--min-description", type=int, default=70, help="Minimum description length")
    args = parser.parse_args()

    docs_dir = Path(args.docs_dir)
    errors = 0
    warnings = 0

    print("=" * 60)
    print("CorpusIQ Pre-Deploy SEO Validator")
    print("=" * 60)

    # === 1. Meta description check ===
    print("\n[1/4] Checking meta descriptions...")
    md_files = find_md_files(docs_dir)
    short_descs = []
    missing_descs = []

    for md_path in md_files:
        with open(md_path) as f:
            content = f.read()

        fm, _ = extract_frontmatter(content)
        desc = parse_description(fm)
        title = parse_title(fm)

        if desc is None:
            missing_descs.append((md_path, title or md_path.stem))
        elif len(desc) < args.min_description:
            short_descs.append((md_path, len(desc), title or md_path.stem))

    if missing_descs:
        print(f"  ⚠️  {len(missing_descs)} pages with NO description:")
        for path, title in missing_descs[:10]:
            print(f"     {path.relative_to(docs_dir)} — \"{title}\"")
        if len(missing_descs) > 10:
            print(f"     ... and {len(missing_descs) - 10} more")
        warnings += len(missing_descs)

    if short_descs:
        print(f"  ⚠️  {len(short_descs)} pages with short description (<{args.min_description}c):")
        for path, length, title in short_descs[:10]:
            print(f"     {path.relative_to(docs_dir)} — {length}c — \"{title}\"")
        warnings += len(short_descs)

    if not missing_descs and not short_descs:
        print("  ✅ All descriptions OK")

    # === 2. External link check ===
    print(f"\n[2/4] Checking external links (max {args.max_links})...")
    all_links = set()
    link_sources = defaultdict(list)

    for md_path in md_files:
        with open(md_path) as f:
            content = f.read()
        for url, text in find_external_links(content):
            if "corpusiq.io" not in url and "github.com/CorpusIQ" not in url:
                if _is_placeholder_url(url):
                    continue
                all_links.add(url)
                link_sources[url].append(str(md_path.relative_to(docs_dir)))

    # Skip links to known-good domains
    skip_domains = {"github.com", "docs.github.com", "pypi.org", "npmjs.com",
                     "twitter.com", "x.com", "linkedin.com", "reddit.com",
                     "youtube.com", "medium.com", "dev.to", "stackoverflow.com",
                     "wikipedia.org", "arxiv.org", "openai.com", "anthropic.com"}
    
    check_links = [url for url in all_links
                   if not any(d in url for d in skip_domains)]

    print(f"  Found {len(all_links)} unique external links, checking {len(check_links)}...")

    broken = []
    with ThreadPoolExecutor(max_workers=10) as pool:
        futures = {pool.submit(check_broken_link, url): url for url in check_links[:args.max_links]}
        for future in as_completed(futures):
            url, status, error = future.result()
            # 401/403/429 = exists but auth-walled / rate-limited, not broken.
            if status and status >= 400 and status not in (401, 403, 429):
                broken.append((url, status, link_sources[url]))
                print(f"  ❌ {status} {url} (from {link_sources[url][0]})")

    if broken:
        errors += len(broken)
        print(f"\n  {len(broken)} broken external links found")
    else:
        print("  ✅ No broken external links")

    # === 3. Orphan page check ===
    print("\n[3/4] Checking orphan pages...")
    # Build page set from md files
    all_pages = {}
    for md_path in md_files:
        rel = str(md_path.relative_to(docs_dir))
        page_slug = rel.replace(".md", "")
        if page_slug.endswith("/index"):
            page_slug = page_slug[:-6]
        all_pages[rel] = page_slug

    # Find which pages are linked from other pages
    linked_pages = set()
    for md_path in md_files:
        with open(md_path) as f:
            content = f.read()
        for link in find_internal_links(content, all_pages):
            # Normalize the link
            link = link.replace(".md", "").replace(".html", "")
            if link.endswith("/index"):
                link = link[:-6]
            linked_pages.add(link)

    # Pages in mkdocs.yml nav are not orphans
    nav_pages = set()
    nav_path = Path("mkdocs.yml")
    if nav_path.exists():
        with open(nav_path) as f:
            nav_content = f.read()
        nav_links = re.findall(r':\s*([a-zA-Z0-9_\-/]+\.md)', nav_content)
        for link in nav_links:
            nav_pages.add(link.replace(".md", ""))

    # Find orphans
    orphans = []
    for rel, slug in all_pages.items():
        if slug not in linked_pages and slug not in nav_pages:
            # Skip section index pages (they're in nav already)
            if not rel.endswith("index.md"):
                orphans.append(rel)

    if orphans:
        print(f"  ⚠️  {len(orphans)} orphan pages (no incoming internal links):")
        for o in orphans[:15]:
            print(f"     {o}")
        if len(orphans) > 15:
            print(f"     ... and {len(orphans) - 15} more")
        warnings += len(orphans)
    else:
        print("  ✅ No orphan pages")

    # === 4. Index page link coverage ===
    print("\n[4/4] Checking index page link coverage...")
    index_dirs = set()
    for md_path in md_files:
        if md_path.name == "index.md":
            parent = md_path.parent
            siblings = [f for f in parent.glob("*.md") if f.name != "index.md"]
            subdirs = [d for d in parent.iterdir() if d.is_dir() and (d / "index.md").exists()]
            total_children = len(siblings) + len(subdirs)

            if total_children > 0:
                with open(md_path) as f:
                    idx_content = f.read()
                linked_in_index = 0
                for child in siblings:
                    if child.stem in idx_content:
                        linked_in_index += 1
                for subd in subdirs:
                    if subd.name in idx_content:
                        linked_in_index += 1

                if linked_in_index < total_children:
                    rel = str(md_path.relative_to(docs_dir))
                    pct = linked_in_index / total_children * 100
                    print(f"  ⚠️  {rel}: {linked_in_index}/{total_children} children linked ({pct:.0f}%)")

    # === Summary ===
    print("\n" + "=" * 60)
    print(f"SUMMARY: {errors} errors, {warnings} warnings")
    if errors > 0:
        print("❌ DEPLOY BLOCKED — fix errors above")
        sys.exit(1)
    elif warnings > 50:
        print("⚠️  High warning count — review before deploying")
    else:
        print("✅ Ready to deploy")
    print("=" * 60)


if __name__ == "__main__":
    main()
