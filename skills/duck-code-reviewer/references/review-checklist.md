# Review Checklist

Apply this baseline checklist to every review.

## Correctness

- Does the change implement the intended behavior?
- Are edge cases handled?
- Are error paths explicit and safe?
- Can the change break existing behavior or assumptions?
- Are null, empty, timeout, retry, and partial-failure cases handled where relevant?

## Security

- Is untrusted input validated and encoded correctly?
- Are authentication and authorization checks preserved?
- Are secrets, tokens, or credentials exposed?
- Does the change create injection, traversal, deserialization, or SSRF risk?
- Are defaults safe if configuration is missing or malformed?

## Maintainability

- Is the control flow understandable?
- Are names, abstractions, and boundaries clear?
- Is logic duplicated unnecessarily?
- Does the change increase coupling or hidden side effects?
- Is there enough local explanation for non-obvious logic?
- Does the change violate applicable project style, lint, formatter, or editor configuration in a way that harms readability or maintainability?

## Performance

- Does the change introduce unnecessary I/O, repeated work, or high-complexity loops?
- Are expensive operations performed in hot paths?
- Does the change scale with data size, concurrency, or request volume?
- Are caching, batching, pagination, or streaming concerns relevant?

## Testing

- Is behavior-changing code covered by tests?
- Are new edge cases tested?
- If no tests are present, is that acceptable for the risk level?
- Does the change likely require integration or regression tests, not just unit tests?

## Operations and rollout

- Does the change affect configuration, migrations, or deployment order?
- Could it fail silently in production?
- Are logging, metrics, and observability good enough to diagnose issues?
- Does rollback look safe?

## Review discipline

- Prioritize material risks over nits.
- Prefer fewer, stronger findings.
- Separate confirmed defects from plausible concerns.
- Treat repository-local style configuration as stronger than generic best-practice preferences.
- Treat generic ecosystem style guidance as advisory unless the repository explicitly adopts it.
