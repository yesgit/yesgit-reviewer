# AI Tooling Rules

This skill should treat common AI-assistant instruction files as valid policy sources.

## Common sources

- `CLAUDE.md`
- `AGENTS.md`
- `.cursorrules`
- `.cursor/rules/`
- `.github/copilot-instructions.md`
- local `rules/`, `instructions/`, or `policies/` directories
- skill-specific instruction files when the repository uses an agent framework

## Typical rule types

These files often define:
- editing restrictions
- generated-file restrictions
- test requirements
- architecture boundaries
- naming conventions
- documentation requirements
- preferred frameworks or patterns

## Review stance

- Treat them as repository policy, not merely suggestions, unless their wording is clearly advisory.
- If a tool-specific rule applies only within a subdirectory, its scope is local to that directory tree.
- If a tool-specific rule conflicts with a root-level advisory rule, prefer the more local rule.
- If two mandatory rules conflict, report the conflict instead of inventing a resolution.
