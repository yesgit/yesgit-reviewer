#!/usr/bin/env python3
"""Infer lightweight design conventions from an existing codebase."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List


SOURCE_EXTENSIONS = {
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".java",
    ".go",
    ".rb",
    ".php",
    ".cs",
}
LAYER_PATTERNS = {
    "service": [
        re.compile(r"\bservices?\b"),
        re.compile(r"[./]services?[./]"),
    ],
    "repository": [
        re.compile(r"\brepositories?\b"),
        re.compile(r"\brepo\b"),
        re.compile(r"\bdao\b"),
        re.compile(r"[./](repositories?|repo|dao)[./]"),
    ],
    "controller": [
        re.compile(r"\bcontrollers?\b"),
        re.compile(r"[./]controllers?[./]"),
    ],
    "domain": [
        re.compile(r"\bdomains?\b"),
        re.compile(r"\bmodels?\b"),
        re.compile(r"\bentities?\b"),
        re.compile(r"[./](domain|models?|entities?)[./]"),
    ],
}
INLINE_IMPORT_PATTERNS = [
    re.compile(r"^\s*import\s+.+$"),
    re.compile(r"^\s*from\s+\S+\s+import\s+.+$"),
    re.compile(r"^\s*(?:const|let|var)\s+.+?=\s*require\(.+\)"),
    re.compile(r"^\s*require(?:_relative)?\(.+\)"),
    re.compile(r"^\s*use\s+.+;$"),
    re.compile(r"^\s*using\s+.+;$"),
]
QUOTED_IMPORT_LINE_RE = re.compile(r'^\s*"[^"]+"\s*$')


def iter_source_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if path.is_file() and path.suffix in SOURCE_EXTENSIONS:
            yield path


def classify_path(rel_path: Path) -> str:
    parts = {part.lower() for part in rel_path.parts}
    if {"controller", "controllers"} & parts:
        return "controller"
    if {"service", "services"} & parts:
        return "service"
    if {"repo", "repository", "repositories", "dao"} & parts:
        return "repository"
    if {"domain", "model", "models", "entity", "entities"} & parts:
        return "domain"
    if {"infra", "infrastructure", "adapter", "adapters"} & parts:
        return "infrastructure"
    if {"api", "apis", "handler", "handlers", "route", "routes"} & parts:
        return "api"
    if {"test", "tests", "__tests__"} & parts:
        return "test"
    if {"ui", "views", "pages", "components"} & parts:
        return "ui"
    return "uncategorized"


def collect_imports(path: Path) -> List[str]:
    imports: List[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return imports

    in_go_import_block = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("import ("):
            in_go_import_block = True
            continue
        if in_go_import_block:
            if stripped == ")":
                in_go_import_block = False
                continue
            if QUOTED_IMPORT_LINE_RE.match(stripped):
                imports.append(stripped)
            continue

        if any(pattern.match(stripped) for pattern in INLINE_IMPORT_PATTERNS):
            imports.append(stripped)
    return imports


def infer(root: Path) -> Dict[str, object]:
    layer_counts: Counter[str] = Counter()
    suffix_counts: Counter[str] = Counter()
    test_patterns: Counter[str] = Counter()
    imports_by_layer: Dict[str, Counter[str]] = defaultdict(Counter)

    for path in iter_source_files(root):
        rel = path.relative_to(root)
        layer = classify_path(rel)
        layer_counts[layer] += 1
        suffix_counts[path.suffix] += 1

        filename = path.name.lower()
        if "test" in filename or rel.parts and any(part.lower() in {"test", "tests", "__tests__"} for part in rel.parts):
            test_patterns["has_tests"] += 1

        for imp in collect_imports(path):
            lowered = imp.lower()
            for inferred_layer, patterns in LAYER_PATTERNS.items():
                if any(pattern.search(lowered) for pattern in patterns):
                    imports_by_layer[layer][inferred_layer] += 1

    return {
        "root": root.as_posix(),
        "layer_counts": dict(layer_counts),
        "language_extensions": dict(suffix_counts),
        "test_patterns": dict(test_patterns),
        "import_tendencies": {layer: dict(counts) for layer, counts in imports_by_layer.items()},
        "notes": [
            "These are inferred conventions, not explicit documented rules.",
            "Use them as baseline signals when explicit design documents are missing or incomplete.",
            "Import tendencies are heuristic and depend on recognizable import syntax.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Infer lightweight design conventions from a codebase.")
    parser.add_argument("root", nargs="?", default=".", help="Repository root")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    print(json.dumps(infer(root), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
