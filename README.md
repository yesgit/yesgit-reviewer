# code-reviewer-skill

Repository wrapper for the `code-reviewer` skill.

The shipped skill lives in `skills/code-reviewer/`. Its behavior, invocation guidance, and review workflow are defined in `skills/code-reviewer/SKILL.md`.

This repository keeps only packaging-level material outside the skill directory:
- `skills/code-reviewer/` contains the actual skill
- `examples/` contains prompt fixtures for manual validation

To install locally:

```bash
mkdir -p ~/.codex/skills
cp -R skills/code-reviewer ~/.codex/skills/
```
