# Customization and Override Model

This guide adapts the upstream project's configurable prompt approach to a pure skill repository.

## Goal

Allow teams to customize review behavior without turning the skill into a platform-specific integration.

## What is portable from the upstream model

The upstream project supports:
- project-level prompt overrides
- branch-level prompt overrides
- configurable review styles
- prompt templates rendered with variables

For a pure skill repository, the portable part is the idea of layered review profiles, not the database-backed configuration itself.

## Recommended override order

When teams customize this skill, use the following precedence:

1. Explicit user instruction in the current request
2. Team or repository-specific review profile
3. Scenario-specific reference
4. Default review profile

## Safe customization points

Teams may customize:
- review style
- severity thresholds
- preferred output language
- domain-specific checklist items
- mandatory focus areas such as security or performance

Teams should avoid customizing:
- the output structure so heavily that findings become inconsistent
- scoring semantics without documenting the new scale
- style in ways that hide serious issues

## Suggested implementation pattern

If a team wants a specialized variant, create a sibling reference file such as:
- `references/team-backend-profile.md`
- `references/team-frontend-profile.md`
- `references/strict-security-profile.md`

Then instruct the host agent to load that profile in addition to:
- `default-review-profile.md`
- the scenario reference
- `output-format.md`

## Why this differs from the upstream project

The upstream project resolves prompt overrides from database and branch configuration at runtime.

This pure skill repository intentionally does not depend on:
- database state
- project admin panels
- branch webhook configuration

Instead, customization is file-based and explicit, which keeps the skill portable and publishable.
