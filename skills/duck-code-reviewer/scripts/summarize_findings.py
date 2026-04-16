#!/usr/bin/env python3
"""Merge chunk-level review markdown files into a single summary skeleton."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import List


LABELS = {
    "en": {
        "summary": "## Summary",
        "combined": "- Combined {count} chunk-level review(s)",
        "consolidate": "- Consolidate duplicate findings and keep the highest-severity version of each issue",
        "chunk_reviews": "## Chunk Reviews",
        "empty": "_Empty review_",
        "finalization": "## Finalization Notes",
        "dedupe": "- Deduplicate overlapping findings",
        "rescore": "- Re-score the full change set after consolidation",
        "material": "- Keep only material issues in the final output",
    },
    "zh": {
        "summary": "## 总结",
        "combined": "- 已合并 {count} 份分块审查结果",
        "consolidate": "- 去重重复问题，并保留每个问题中严重级别最高的版本",
        "chunk_reviews": "## 分块审查结果",
        "empty": "_空审查结果_",
        "finalization": "## 收尾说明",
        "dedupe": "- 对重叠问题去重",
        "rescore": "- 汇总后重新评估整组变更分数",
        "material": "- 最终输出仅保留实质性问题",
    },
}


def load_reviews(paths: List[str]) -> List[tuple[str, str]]:
    loaded: List[tuple[str, str]] = []
    for path in paths:
        p = Path(path)
        loaded.append((p.name, p.read_text(encoding="utf-8").strip()))
    return loaded


def render_summary(reviews: List[tuple[str, str]], lang: str) -> str:
    labels = LABELS[lang]
    lines: List[str] = []
    lines.append(labels["summary"])
    lines.append(labels["combined"].format(count=len(reviews)))
    lines.append(labels["consolidate"])
    lines.append("")
    lines.append(labels["chunk_reviews"])
    for name, content in reviews:
        lines.append("")
        lines.append(f"### {name}")
        lines.append(content or labels["empty"])
    lines.append("")
    lines.append(labels["finalization"])
    lines.append(labels["dedupe"])
    lines.append(labels["rescore"])
    lines.append(labels["material"])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Merge review markdown files into one summary skeleton.")
    parser.add_argument("--lang", choices=sorted(LABELS), default="en", help="Output language")
    parser.add_argument("reviews", nargs="+", help="Chunk-level review markdown files")
    args = parser.parse_args()

    reviews = load_reviews(args.reviews)
    print(render_summary(reviews, lang=args.lang), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
