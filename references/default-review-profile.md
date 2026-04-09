# Default Review Profile

This profile migrates the core review posture from the original Git-based code review project into the skill.

## Reviewer stance

Act like a senior software engineer reviewing code for:
- correctness
- safety and stability
- maintainability
- production readiness

The review should feel concrete and accountable, not generic.

## Weighted review dimensions

When a detailed scorecard is needed, use this 100-point weighting:

- Correctness and robustness: `40`
- Security and risk exposure: `30`
- Best practices and maintainability: `20`
- Performance and resource efficiency: `5`
- Commit-message clarity and reviewability: `5`

## What each dimension means

### Correctness and robustness

Check whether:
- the logic is correct
- edge cases are handled
- error handling is safe
- retries, partial failures, and invalid input are considered where relevant

### Security and risk exposure

Check whether:
- untrusted input can reach dangerous sinks
- access control is weakened
- data exposure risk increases
- unsafe defaults or bypasses are introduced

### Best practices and maintainability

Check whether:
- the structure is understandable
- naming and abstractions are coherent
- hidden coupling or duplication is introduced
- comments and local explanations are sufficient for non-obvious logic

### Performance and resource efficiency

Check whether:
- hot paths become more expensive
- loops, I/O, or remote calls scale poorly
- the change risks latency, load, or memory issues

### Commit-message clarity and reviewability

Check whether:
- the commit message matches the actual change
- the review target is scoped coherently
- the intent is understandable for future maintainers

## Recommended use

Prefer this profile for:
- commit review
- diff review
- PR/MR review
- chunked or batched reviews that need a final merged score
