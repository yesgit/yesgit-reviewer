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
- `spec/`
- `standards/`
- `policies/`

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

## Extraction principles

- Treat explicit "must", "must not", "required", "do not", and "forbidden" statements as stronger rules.
- Treat "should" and "prefer" as default rules unless a stricter source overrides them.
- Keep the source path attached to every extracted rule.
