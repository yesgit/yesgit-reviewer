#!/usr/bin/env python3
"""Split a unified diff into smaller chunks by file count or approximate line count."""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path
from typing import List


FILE_HEADER_RE = re.compile(r"^diff --git ")


def split_files(text: str) -> List[str]:
    chunks: List[List[str]] = []
    current: List[str] = []
    for line in text.splitlines(keepends=True):
        if FILE_HEADER_RE.match(line) and current:
            chunks.append(current)
            current = []
        current.append(line)
    if current:
        chunks.append(current)
    return ["".join(chunk) for chunk in chunks]


def group_files(file_diffs: List[str], max_files: int, max_lines: int) -> List[str]:
    groups: List[List[str]] = []
    current: List[str] = []
    current_lines = 0
    for file_diff in file_diffs:
        file_lines = len(file_diff.splitlines())
        need_flush = current and (
            len(current) >= max_files or current_lines + file_lines > max_lines
        )
        if need_flush:
            groups.append(current)
            current = []
            current_lines = 0
        current.append(file_diff)
        current_lines += file_lines
    if current:
        groups.append(current)
    return ["".join(group) for group in groups]


def main() -> int:
    parser = argparse.ArgumentParser(description="Split a unified diff into smaller chunks.")
    parser.add_argument("input", help="Input diff file")
    parser.add_argument("--output-dir", required=True, help="Directory for chunk files")
    parser.add_argument("--max-files", type=int, default=5, help="Maximum files per chunk")
    parser.add_argument("--max-lines", type=int, default=400, help="Approximate maximum lines per chunk")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as fh:
        text = fh.read()

    file_diffs = split_files(text)
    groups = group_files(file_diffs, max_files=args.max_files, max_lines=args.max_lines)

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    for index, group in enumerate(groups, start=1):
        path = out_dir / f"chunk_{index:03d}.diff"
        path.write_text(group, encoding="utf-8")

    print(f"Wrote {len(groups)} chunk(s) to {os.fspath(out_dir)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
