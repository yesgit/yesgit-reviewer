#!/usr/bin/env python3
"""Normalize unified diffs by removing low-value noise hunks."""

from __future__ import annotations

import argparse
import re
import sys
from typing import Iterable, List


FILE_HEADER_RE = re.compile(r"^diff --git ")


def split_files(lines: Iterable[str]) -> List[List[str]]:
    files: List[List[str]] = []
    current: List[str] = []
    for line in lines:
        if FILE_HEADER_RE.match(line) and current:
            files.append(current)
            current = []
        current.append(line)
    if current:
        files.append(current)
    return files


def is_noise_only(file_lines: List[str]) -> bool:
    changed = [line for line in file_lines if line.startswith(("+", "-")) and not line.startswith(("+++", "---"))]
    if not changed:
        return False
    stripped = [line[1:].strip() for line in changed]
    return all(not token or token in {"{", "}", "(", ")", "[", "]", ",", ";"} for token in stripped)


def normalize_diff(text: str, drop_noise_only: bool) -> str:
    lines = text.splitlines(keepends=True)
    files = split_files(lines)
    kept: List[str] = []
    for file_lines in files:
        if drop_noise_only and is_noise_only(file_lines):
            continue
        kept.extend(file_lines)
    return "".join(kept)


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize a unified diff.")
    parser.add_argument("input", nargs="?", help="Input diff file. Reads stdin if omitted.")
    parser.add_argument("--keep-noise", action="store_true", help="Keep formatting-only hunks.")
    args = parser.parse_args()

    if args.input:
        with open(args.input, "r", encoding="utf-8") as fh:
            text = fh.read()
    else:
        text = sys.stdin.read()

    sys.stdout.write(normalize_diff(text, drop_noise_only=not args.keep_noise))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
