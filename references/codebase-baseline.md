# Codebase Baseline

Use this guide when explicit design docs are incomplete and you need to infer likely architectural conventions from the existing codebase.

## Goal

Build a lightweight baseline of how the repository is already structured so that new changes can be checked for drift.

## What to infer

Infer patterns such as:
- directory layering
- module placement conventions
- import or dependency direction
- naming patterns
- test colocation or test-directory layout
- common boundaries between UI, service, domain, data, and infrastructure layers

## Evidence quality

Treat inferred rules as weaker than explicit documented rules.

Strength guidance:
- explicit docs or policy files: stronger
- repeated codebase patterns: medium
- isolated examples: weak

## Use cases

Use inferred baselines when:
- the repository has little formal documentation
- the user asks whether new code matches the existing architecture
- explicit docs exist but are incomplete for the area being changed

## Reporting

When using inferred constraints, explicitly label them as inferred and cite the repeated code patterns that support the inference.
