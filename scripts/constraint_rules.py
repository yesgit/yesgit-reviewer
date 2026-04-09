"""Shared rule-source definitions for review helper scripts."""

from __future__ import annotations

import fnmatch
from pathlib import Path


DOCUMENT_RULE_FILENAMES = {
    "README.md",
    "README.txt",
    "ARCHITECTURE.md",
    "DESIGN.md",
    "CONTRIBUTING.md",
    "STYLEGUIDE.md",
    "ADR.md",
    "CLAUDE.md",
    "AGENTS.md",
    "SKILL.md",
    ".cursorrules",
    ".editorconfig",
    ".eslintrc",
    ".prettierrc",
    "biome.json",
    "biome.jsonc",
    "rome.json",
    "ruff.toml",
    ".ruff.toml",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini",
    ".flake8",
    "mypy.ini",
    "tsconfig.json",
    "jsconfig.json",
    ".stylelintrc",
    ".clang-format",
    "rustfmt.toml",
    ".rubocop.yml",
}

DOCUMENT_RULE_GLOBS = {
    "README.*",
    ".eslintrc.*",
    "eslint.config.*",
    ".prettierrc.*",
    "prettier.config.*",
    ".stylelintrc.*",
    "stylelint.config.*",
    ".golangci.yml",
    ".golangci.yaml",
}

SCOPED_DIR_NAMES = {
    "docs",
    "doc",
    "design",
    "architecture",
    "references",
    "spec",
    "standards",
    "policies",
    "rules",
    "instructions",
}

TEXT_EXTENSIONS = {".md", ".mdx", ".txt", ".rst", ".adoc", ".yaml", ".yml", ".json", ".toml"}

SPECIAL_RELATIVE_RULES = {
    ".github/copilot-instructions.md",
}


def is_named_rule_file(path: Path) -> bool:
    return path.name in DOCUMENT_RULE_FILENAMES or any(fnmatch.fnmatch(path.name, pattern) for pattern in DOCUMENT_RULE_GLOBS)


def is_text_rule_file(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS


def is_constraint_source(path: Path, root: Path) -> bool:
    rel = path.relative_to(root).as_posix()
    if rel in SPECIAL_RELATIVE_RULES:
        return True
    if is_named_rule_file(path):
        return True
    if any(part in SCOPED_DIR_NAMES for part in path.parts[:-1]) and is_text_rule_file(path):
        return True
    if ".cursor" in path.parts and "rules" in path.parts and is_text_rule_file(path):
        return True
    return False
