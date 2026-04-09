# General Design Principles and Clean Code Heuristics

Use this guide as a fallback baseline when reviewing design quality, maintainability, and code cleanliness.

## Purpose

This reference adds a small set of widely used principles that help reviewers identify unnecessary complexity, weak abstractions, and maintainability risks.

These principles are intentionally advisory by default.
They must not override:
- explicit repository or directory-local rules
- formatter, lint, or editor configuration
- documented architectural constraints
- direct user instructions for the current review

## How to use this guide

- Use these heuristics when project-specific standards are missing, incomplete, or too narrow for a maintainability discussion.
- Prefer concrete, code-linked findings over abstract naming of principles.
- Only raise a finding when the principle violation creates a real cost such as bug risk, unclear ownership, hidden coupling, or avoidable maintenance burden.
- Do not treat these heuristics as style-only nit rules.

## Recommended principle set

### DRY

Look for:
- duplicated logic that must be kept in sync
- repeated branching or validation that is likely to drift
- copy-pasted code hiding a missing abstraction

Do not use DRY mechanically.
Small duplication may be acceptable when abstraction would increase coupling or obscure intent.

### KISS

Look for:
- abstractions that are more complex than the current need
- control flow that is difficult to follow without a clear payoff
- multi-layer indirection where direct code would be clearer

Raise a finding when simplicity would improve readability, defect resistance, or change safety.

### YAGNI

Look for:
- extension points with no real caller or use case
- speculative configuration, hooks, or generic frameworks
- premature generalization added without present requirements

Raise a finding only when the extra design has a real maintenance or correctness cost.

### SRP

Single Responsibility Principle can be used as advisory guidance when:
- one unit mixes unrelated concerns such as transport, business logic, persistence, and formatting
- changes to one reason force edits across unrelated behavior in the same unit

Prefer describing the concrete coupling rather than citing SRP alone.

### Interface and dependency clarity

Look for:
- hidden dependencies
- APIs that leak internal details
- boundaries that force callers to know too much about implementation
- dependency direction that increases coupling across layers

This can overlap with dependency inversion concerns, but findings should stay concrete and repository-aware.

## Clean Code heuristics worth using

These heuristics are usually safe and actionable when grounded in behavior:

- names should communicate intent clearly enough for local readers
- functions and methods should have a coherent primary responsibility
- side effects should be explicit rather than surprising
- error handling should be visible and safe
- non-obvious logic should have enough local explanation
- dense conditionals and branching should remain understandable
- avoid hidden temporal coupling where callers must follow undocumented ordering

## Heuristics to avoid enforcing rigidly

Do not report hard violations based only on statements such as:
- every function must be short
- comments are always bad
- abstraction is always better than duplication
- every module must satisfy a textbook SOLID interpretation

These ideas are too context-sensitive to serve as default hard rules.

## Reporting guidance

When using this guide:
- label it as `advisory`
- name the concrete maintainability or design risk
- explain why the existing project rules did not provide a stronger source
- prefer repository terminology over textbook terminology when possible

Example finding framing:
- instead of `violates SOLID`, say `this service mixes request parsing, domain validation, and persistence, which makes failures harder to isolate and test`
