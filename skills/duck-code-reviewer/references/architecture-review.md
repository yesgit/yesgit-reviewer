# Architecture and Standards Review

Use this guide when the user asks whether code violates:
- architecture rules
- design constraints
- coding standards
- repository policies
- AI-tooling instructions
- general design principles or code cleanliness expectations

## Goal

Determine whether the change is inconsistent with the project's documented architecture or local directory-specific rules.
This includes effective style, lint, formatter, and editor rules when the user asks about standards or coding conventions.
If explicit project rules are incomplete, you may also use [general-design-principles.md](general-design-principles.md) as advisory maintainability guidance.

## Review model

This review has two phases:

1. Constraint discovery
2. Constraint-to-code comparison

Do not start with code-only review if the request is explicitly about design or standards. First determine the active rules.

## Constraint discovery

Read the sources described in:
- [constraint-sources.md](constraint-sources.md)
- [ai-tooling-rules.md](ai-tooling-rules.md)

Use:
- `scripts/discover_constraints.py` to find likely rule files
- `scripts/resolve_effective_constraints.py` to determine the applicable rule stack for a target file or directory

## What to look for

- forbidden dependencies or imports
- layering violations
- module-boundary violations
- naming or file-placement rules
- style, formatting, or lint rules that are explicitly configured for the affected path
- testing requirements
- generated-file modification bans
- API or workflow constraints defined in docs
- AI-agent instructions that prohibit certain edits or require specific workflows

## Output expectations

When reporting a violation, include:
- the violated rule
- the source document that defined it
- the effective scope of that rule
- the conflicting code or change
- whether the rule was mandatory, default, or advisory

## Important

If rules conflict, resolve them with [rule-precedence.md](rule-precedence.md).
If the docs are ambiguous or contradictory, report that ambiguity as part of the findings.
Do not report generic design principles as hard violations unless the repository explicitly adopts them.
