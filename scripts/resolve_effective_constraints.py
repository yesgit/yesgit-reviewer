#!/usr/bin/env python3
"""Resolve the effective constraint-source stack for a target path."""

from __future__ import annotations

import argparse
import fnmatch
import json
from pathlib import Path
from typing import List


FILENAMES = {
    "README.md",
    "README.txt",
    "ARCHITECTURE.md",
    "DESIGN.md",
    "CONTRIBUTING.md",
    "STYLEGUIDE.md",
    "CLAUDE.md",
    "AGENTS.md",
    ".cursorrules",
}
TEXT_EXTENSIONS = {".md", ".mdx", ".txt", ".rst", ".adoc", ".yaml", ".yml", ".json", ".toml"}
SCOPED_DIR_NAMES = {"docs", "doc", "design", "architecture", "spec", "standards", "policies", "rules", "instructions"}


def is_text_rule_file(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS


def collect_scoped_rule_files(repo_root: Path, cursor: Path) -> List[Path]:
    candidates: List[Path] = []
    for dirname in sorted(SCOPED_DIR_NAMES):
        scoped_dir = cursor / dirname
        if scoped_dir.is_dir():
            for candidate in sorted(p for p in scoped_dir.rglob("*") if is_text_rule_file(p)):
                candidates.append(candidate)
    return candidates


def collect_candidates(root: Path, current: Path) -> List[dict]:
    results: List[dict] = []
    repo_root = root.resolve()
    path = current.resolve()

    if path.is_file():
        cursor = path.parent
    else:
        cursor = path

    while True:
        for name in sorted(FILENAMES):
            candidate = cursor / name
            if candidate.is_file():
                results.append(
                    {
                        "path": candidate.relative_to(repo_root).as_posix(),
                        "scope_path": cursor.relative_to(repo_root).as_posix() or ".",
                        "precedence": len(results) + 1,
                    }
                )

        for candidate in collect_scoped_rule_files(repo_root, cursor):
            results.append(
                {
                    "path": candidate.relative_to(repo_root).as_posix(),
                    "scope_path": cursor.relative_to(repo_root).as_posix() or ".",
                    "precedence": len(results) + 1,
                }
            )

        cursor_rules = cursor / ".cursor" / "rules"
        if cursor_rules.is_dir():
            for candidate in sorted(p for p in cursor_rules.rglob("*") if is_text_rule_file(p)):
                results.append(
                    {
                        "path": candidate.relative_to(repo_root).as_posix(),
                        "scope_path": cursor.relative_to(repo_root).as_posix() or ".",
                        "precedence": len(results) + 1,
                    }
                )

        github_copilot = cursor / ".github" / "copilot-instructions.md"
        if github_copilot.is_file():
            results.append(
                {
                    "path": github_copilot.relative_to(repo_root).as_posix(),
                    "scope_path": cursor.relative_to(repo_root).as_posix() or ".",
                    "precedence": len(results) + 1,
                }
            )

        if cursor == repo_root:
            break
        if repo_root not in cursor.parents and cursor != repo_root:
            break
        cursor = cursor.parent

    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Resolve effective constraint sources for a target path.")
    parser.add_argument("root", help="Repository root")
    parser.add_argument("target", help="Target file or directory inside the repository")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    target = (root / args.target).resolve() if not Path(args.target).is_absolute() else Path(args.target).resolve()
    print(json.dumps(collect_candidates(root, target), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
