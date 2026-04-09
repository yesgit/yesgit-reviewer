# Constraint Sources

Use these locations as likely sources of architecture, design, and standards rules.

## Repository-wide sources

- `README.md`
- `README.*`
- `ARCHITECTURE.md`
- `DESIGN.md`
- `CONTRIBUTING.md`
- `STYLEGUIDE.md`
- `ADR.md`
- `docs/`
- `doc/`
- `design/`
- `architecture/`
- `references/`
- `spec/`
- `standards/`
- `policies/`

Also check repository-root style and tooling configuration when it can define effective coding rules, for example:
- `.editorconfig`
- `.eslintrc`
- `.eslintrc.*`
- `eslint.config.*`
- `.prettierrc`
- `.prettierrc.*`
- `prettier.config.*`
- `biome.json`
- `biome.jsonc`
- `rome.json`
- `ruff.toml`
- `.ruff.toml`
- `pyproject.toml`
- `setup.cfg`
- `tox.ini`
- `.flake8`
- `mypy.ini`
- `tsconfig.json`
- `jsconfig.json`
- `.stylelintrc`
- `.stylelintrc.*`
- `stylelint.config.*`
- `.clang-format`
- `rustfmt.toml`
- `.golangci.yml`
- `.golangci.yaml`
- `.rubocop.yml`

## Directory-local sources

Also look for rule files inside or near the target path, such as:
- `<dir>/README.md`
- `<dir>/ARCHITECTURE.md`
- `<dir>/DESIGN.md`
- `<dir>/CONTRIBUTING.md`
- `<dir>/AGENTS.md`
- `<dir>/CLAUDE.md`
- `<dir>/.cursorrules`
- `<dir>/.cursor/rules/`
- `<dir>/.editorconfig`
- `<dir>/.eslintrc`
- `<dir>/.eslintrc.*`
- `<dir>/eslint.config.*`
- `<dir>/.prettierrc`
- `<dir>/.prettierrc.*`
- `<dir>/prettier.config.*`
- `<dir>/biome.json`
- `<dir>/biome.jsonc`
- `<dir>/pyproject.toml`
- `<dir>/ruff.toml`
- `<dir>/.ruff.toml`
- `<dir>/.stylelintrc`
- `<dir>/.stylelintrc.*`
- `<dir>/stylelint.config.*`
- `<dir>/.clang-format`

## Extraction principles

- Treat explicit "must", "must not", "required", "do not", and "forbidden" statements as stronger rules.
- Treat "should" and "prefer" as default rules unless a stricter source overrides them.
- Keep the source path attached to every extracted rule.
- If a style or lint config is path-scoped or directory-local, treat it as applying only where that tool would normally apply it.
- More local style configuration should override broader repository defaults when the underlying tool supports overrides or nearest-config resolution.
- If no project-specific style rule is present, ecosystem conventions may be used only as advisory review guidance.
