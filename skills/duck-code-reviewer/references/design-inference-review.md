# Design Inference Review

Use this guide when the user wants to know whether new code fits the existing architecture or implicit design conventions of the repository.

## Goal

Infer the current design baseline from old code, then compare the new code or diff against that baseline.

## Process

1. Gather explicit rules first using:
   - [constraint-sources.md](constraint-sources.md)
   - [ai-tooling-rules.md](ai-tooling-rules.md)
2. If the explicit rules are incomplete, infer baseline patterns using:
   - [codebase-baseline.md](codebase-baseline.md)
   - `scripts/infer_design_constraints.py`
3. Distinguish:
   - explicit documented rules
   - inferred repository conventions
4. Review the new code or diff against both, giving explicit rules higher weight.

## What to detect

- architecture drift
- unexpected dependency direction
- misplaced files or modules
- naming patterns inconsistent with established local conventions
- new layers or abstractions introduced without precedent or explanation
- divergence from established testing layout

## Output expectations

When reporting a design mismatch, include:
- whether the rule was explicit or inferred
- the baseline evidence
- the new code that deviates
- whether the deviation appears intentional, risky, or acceptable with documentation

## Important

Do not treat every variation from the old code as a bug.
The purpose is to identify meaningful drift, not to freeze the architecture forever.
