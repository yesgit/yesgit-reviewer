#!/usr/bin/env python3
"""Merge chunk-level review markdown files into a single summary skeleton."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import List


def load_reviews(paths: List[str]) -> List[tuple[str, str]]:
    loaded: List[tuple[str, str]] = []
    for path in paths:
        p = Path(path)
        loaded.append((p.name, p.read_text(encoding="utf-8").strip()))
    return loaded


def render_summary(reviews: List[tuple[str, str]]) -> str:
    lines: List[str] = []
    lines.append("## Summary")
    lines.append(f"- Combined {len(reviews)} chunk-level review(s)")
    lines.append("- Consolidate duplicate findings and keep the highest-severity version of each issue")
    lines.append("")
    lines.append("## Chunk Reviews")
    for name, content in reviews:
        lines.append("")
        lines.append(f"### {name}")
        lines.append(content or "_Empty review_")
    lines.append("")
    lines.append("## Finalization Notes")
    lines.append("- Deduplicate overlapping findings")
    lines.append("- Re-score the full change set after consolidation")
    lines.append("- Keep only material issues in the final output")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Merge review markdown files into one summary skeleton.")
    parser.add_argument("reviews", nargs="+", help="Chunk-level review markdown files")
    args = parser.parse_args()

    reviews = load_reviews(args.reviews)
    print(render_summary(reviews), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
