#!/usr/bin/env python3
"""Absolutize relative internal docs links in a built MkDocs site tree.

Production serves docs pages without a trailing slash. Raw MkDocs output uses
directory-style relative links that assume a trailing slash page URL. On a
no-slash URL, links like "../mcp-for-hr" resolve one segment too high and can
404. This pass rewrites relative internal `href` and `src` targets to
root-absolute `/docs/...` paths so navigation stays valid regardless of URL
shape.

Usage:
    python scripts/absolutize_internal_links.py [site_dir] [--check]

Exit 0 = stable
Exit 1 = change required in --check mode, missing resolved target, or
         processing failure
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import posixpath
import re
import sys


ATTR_RE = re.compile(
    r"(?P<prefix>(?P<name>href|src)\s*=\s*)(?P<quote>['\"])(?P<value>[^'\"]*)(?P=quote)",
    re.IGNORECASE,
)

SKIP_VALUE_PREFIXES = (
    "http://",
    "https://",
    "//",
    "mailto:",
    "tel:",
    "javascript:",
    "data:",
    "#",
)


@dataclass(frozen=True)
class Summary:
    files_touched: int
    references_rewritten: int
    distinct_targets: int


class MissingResolvedTarget(Exception):
    def __init__(self, file_rel: str, reference: str, resolved_target: str):
        super().__init__(f"{file_rel}: {reference} -> {resolved_target}")
        self.file_rel = file_rel
        self.reference = reference
        self.resolved_target = resolved_target


def _split_path_query_fragment(reference: str) -> tuple[str, str]:
    fragment_index = reference.find("#")
    if fragment_index >= 0:
        before_fragment = reference[:fragment_index]
        fragment = reference[fragment_index:]
    else:
        before_fragment = reference
        fragment = ""

    query_index = before_fragment.find("?")
    if query_index >= 0:
        path_only = before_fragment[:query_index]
        query = before_fragment[query_index:]
    else:
        path_only = before_fragment
        query = ""

    return path_only, f"{query}{fragment}"


def _is_skipped_value(reference: str) -> bool:
    if reference.startswith("/"):
        return True
    lowered = reference.lower()
    return lowered.startswith(SKIP_VALUE_PREFIXES)


def _page_base(rel_file: str) -> str:
    if rel_file.endswith("index.html"):
        return rel_file[: -len("index.html")]
    return rel_file


def _resolve_target_rel(base: str, reference_path: str) -> str:
    resolved = posixpath.normpath(posixpath.join(base, reference_path))
    if resolved == ".":
        return ""
    return resolved.lstrip("/")


def _resolved_target_exists(site_dir: Path, resolved_rel: str) -> bool:
    if resolved_rel in {"", "."}:
        return True
    if resolved_rel == ".." or resolved_rel.startswith("../"):
        return False
    return (site_dir / resolved_rel).exists()


def _to_docs_absolute(resolved_rel: str) -> str:
    if not resolved_rel:
        return "/docs"
    return "/docs/" + resolved_rel.lstrip("/")


def _rewrite_html_text(
    text: str,
    rel_file: str,
    site_dir: Path,
) -> tuple[str, int, set[str]]:
    base = _page_base(rel_file)
    refs_rewritten = 0
    touched_targets: set[str] = set()

    def replace_attr(match: re.Match[str]) -> str:
        nonlocal refs_rewritten

        prefix = match.group("prefix")
        quote = match.group("quote")
        original_value = match.group("value")

        if _is_skipped_value(original_value):
            return match.group(0)

        path_only, suffix = _split_path_query_fragment(original_value)
        resolved_rel = _resolve_target_rel(base, path_only)
        resolved_docs = _to_docs_absolute(resolved_rel)

        if not _resolved_target_exists(site_dir, resolved_rel):
            raise MissingResolvedTarget(rel_file, original_value, resolved_docs)

        rewritten = f"{resolved_docs}{suffix}"
        if rewritten == original_value:
            return match.group(0)

        refs_rewritten += 1
        touched_targets.add(resolved_docs)
        return f"{prefix}{quote}{rewritten}{quote}"

    updated = ATTR_RE.sub(replace_attr, text)
    return updated, refs_rewritten, touched_targets


def absolutize_internal_links(site_dir: Path, *, check: bool) -> Summary:
    if not site_dir.exists() or not site_dir.is_dir():
        raise RuntimeError(f"Site directory not found: {site_dir}")

    updates: list[tuple[Path, str]] = []
    files_touched = 0
    refs_rewritten = 0
    distinct_targets: set[str] = set()

    for html_path in sorted(site_dir.rglob("*.html")):
        rel_file = html_path.relative_to(site_dir).as_posix()
        if rel_file == "404.html" or rel_file.startswith("hermes/data/"):
            continue

        original = html_path.read_text(encoding="utf-8")
        updated, file_refs, file_targets = _rewrite_html_text(original, rel_file, site_dir)

        if updated != original:
            files_touched += 1
            if not check:
                updates.append((html_path, updated))
        refs_rewritten += file_refs
        distinct_targets.update(file_targets)

    if not check:
        for path, content in updates:
            path.write_text(content, encoding="utf-8")

    return Summary(
        files_touched=files_touched,
        references_rewritten=refs_rewritten,
        distinct_targets=len(distinct_targets),
    )


def _print_summary(summary: Summary, *, check: bool) -> None:
    files_label = "Files to touch" if check else "Files touched"
    refs_label = "References to rewrite" if check else "References rewritten"
    print(f"{files_label}: {summary.files_touched}")
    print(f"{refs_label}: {summary.references_rewritten}")
    print(f"Distinct targets: {summary.distinct_targets}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site_dir", nargs="?", default="site")
    parser.add_argument("--check", action="store_true", help="Report drift without modifying files")
    args = parser.parse_args(argv)

    site_dir = Path(args.site_dir)
    try:
        summary = absolutize_internal_links(site_dir, check=args.check)
    except MissingResolvedTarget as exc:
        print(
            f"ERROR: missing resolved target in {exc.file_rel}: {exc.reference} -> {exc.resolved_target}",
            file=sys.stderr,
        )
        raise SystemExit(1) from exc
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    _print_summary(summary, check=args.check)
    has_changes = summary.files_touched > 0 or summary.references_rewritten > 0
    if args.check and has_changes:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

