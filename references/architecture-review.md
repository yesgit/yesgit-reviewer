# Architecture and Standards Review

Use this guide when the user asks whether code violates:
- architecture rules
- design constraints
- coding standards
- repository policies
- AI-tooling instructions

## Goal

Determine whether the change is inconsistent with the project's documented architecture or local directory-specific rules.

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
