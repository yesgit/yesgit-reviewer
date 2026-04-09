#!/usr/bin/env python3
"""Discover likely architecture, design, and policy files in a repository."""

from __future__ import annotations

import argparse
import fnmatch
import json
from pathlib import Path
from typing import List


PATTERNS = [
    "README.md",
    "README.*",
    "ARCHITECTURE.md",
    "DESIGN.md",
    "CONTRIBUTING.md",
    "STYLEGUIDE.md",
    "ADR.md",
    "CLAUDE.md",
    "AGENTS.md",
    ".cursorrules",
    ".github/copilot-instructions.md",
]

DIR_NAMES = {"docs", "doc", "design", "architecture", "spec", "standards", "policies", "rules", "instructions"}
TEXT_EXTENSIONS = {".md", ".mdx", ".txt", ".rst", ".adoc", ".yaml", ".yml", ".json", ".toml"}


def matches(path: Path, root: Path) -> bool:
    rel = path.relative_to(root).as_posix()
    if any(fnmatch.fnmatch(path.name, pattern) for pattern in PATTERNS):
        return True
    if rel in {".github/copilot-instructions.md"}:
        return True
    if any(part in DIR_NAMES for part in path.parts[:-1]) and path.suffix.lower() in TEXT_EXTENSIONS:
        return True
    if ".cursor" in path.parts and "rules" in path.parts and path.suffix.lower() in TEXT_EXTENSIONS:
        return True
    return False


def discover(root: Path) -> List[dict]:
    found: List[dict] = []
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        if matches(path, root):
            found.append(
                {
                    "path": path.relative_to(root).as_posix(),
                    "scope_path": path.parent.relative_to(root).as_posix() or ".",
                    "kind": "constraint_source",
                }
            )
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description="Discover likely architecture and policy files.")
    parser.add_argument("root", nargs="?", default=".", help="Repository root to scan")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    print(json.dumps(discover(root), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
