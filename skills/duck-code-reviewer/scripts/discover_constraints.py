#!/usr/bin/env python3
"""Discover likely architecture, design, and policy files in a repository."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import List

from constraint_rules import is_constraint_source


def discover(root: Path) -> List[dict]:
    found: List[dict] = []
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        if is_constraint_source(path, root):
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
