#!/usr/bin/env python3
"""Pure text helpers for deterministic public feed generation."""

from __future__ import annotations

import re


TRUNCATION_NOTICE = "[Content truncated; see the canonical page for the complete text.]"


def _backoff_incomplete_markdown(excerpt: str) -> str:
    """Remove a trailing Markdown/HTML block that truncation left incomplete."""
    while excerpt:
        candidates: list[int] = []

        # A feed excerpt must not publish an open disclosure block. Back off to
        # the earliest still-unmatched <details> tag, which also removes an
        # orphan <summary> nested inside it.
        details_stack: list[int] = []
        for match in re.finditer(r"</?details\b[^>]*>", excerpt, re.IGNORECASE):
            if match.group(0).lower().startswith("</"):
                if details_stack:
                    details_stack.pop()
            else:
                details_stack.append(match.start())
        if details_stack:
            candidates.append(details_stack[0])

        # Likewise, never leave a fenced code block open.
        open_fence: tuple[str, int] | None = None
        offset = 0
        for line in excerpt.splitlines(keepends=True):
            fence = re.match(r"^\s*(```|~~~)", line)
            if fence:
                marker = fence.group(1)
                if open_fence is None:
                    open_fence = (marker, offset)
                elif marker == open_fence[0]:
                    open_fence = None
            offset += len(line)
        if open_fence is not None:
            candidates.append(open_fence[1])

        lines = excerpt.splitlines(keepends=True)
        nonempty = [index for index, line in enumerate(lines) if line.strip()]
        if nonempty:
            last_index = nonempty[-1]
            last_line = lines[last_index].strip()
            last_start = sum(len(line) for line in lines[:last_index])
            # A heading or thematic break with no following body is an orphan.
            if re.match(r"^#{1,6}\s+\S", last_line) or re.match(
                r"^(?:---+|\*\*\*+|___+)$", last_line
            ):
                candidates.append(last_start)
            # If the selected boundary lands inside a table, remove the entire
            # trailing table paragraph rather than publishing a partial row set.
            if last_line.startswith("|") and last_line.endswith("|"):
                paragraph_start = excerpt.rfind("\n\n", 0, last_start)
                candidates.append(0 if paragraph_start < 0 else paragraph_start + 2)

        if not candidates:
            break
        backed_off = excerpt[: min(candidates)].rstrip()
        if backed_off == excerpt:
            break
        excerpt = backed_off

    return excerpt


def truncate_for_feed(body: str, limit: int = 12_000) -> str:
    """Truncate at a paragraph, line, sentence, or word boundary.

    A hard character slice can split a word or Markdown token and publish malformed
    feed text. Prefer the strongest available boundary near the limit, then append
    an explicit deterministic notice.
    """
    stripped = body.rstrip()
    if len(stripped) <= limit:
        return stripped

    prefix = body[:limit]
    minimum = max(1, limit // 2)
    # Prefer a complete paragraph. If none exists in the latter half, use a
    # complete line. Never choose a later word boundary over an earlier
    # structural boundary: that corrupts Markdown links, tables, and headings.
    cut = prefix.rfind("\n\n", minimum)
    if cut < minimum:
        cut = prefix.rfind("\n", minimum)
    if cut < minimum:
        cut = prefix.rfind(" ", minimum)
    if cut < minimum:
        cut = limit

    excerpt = _backoff_incomplete_markdown(prefix[:cut].rstrip())
    return f"{excerpt}\n\n{TRUNCATION_NOTICE}"
