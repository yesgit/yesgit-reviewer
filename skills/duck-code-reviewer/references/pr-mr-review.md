# PR/MR Review

Use this guide when reviewing pull requests or merge requests.

## Review order

1. Read the PR/MR title and description.
2. Identify the goal, scope, and intended rollout.
3. Check whether the change set is cohesive or mixes unrelated work.
4. Review the code diff.
5. Check tests, CI signals, and migration or deployment implications if available.

## What to evaluate

### Scope quality

- Is the change set too large to review safely?
- Does it mix refactor, behavior change, and cleanup in one PR?
- Are there unrelated formatting or generated-file changes adding noise?

### Intent alignment

- Does the code actually implement the stated goal?
- Are there hidden behavior changes not mentioned in the description?
- Are tradeoffs, assumptions, or rollout constraints missing?

### Test posture

- Are key behavior changes covered?
- Are regression tests present for bug fixes?
- Are CI failures, flaky checks, or missing checks relevant?

### Operational risk

- Does this require migration, backfill, feature flags, or config rollout?
- Can the change break compatibility with existing clients or data?
- Is there a safe rollback path?

## Good review behavior

- Keep findings actionable.
- Distinguish "request changes" issues from follow-up suggestions.
- Avoid restating the PR summary unless it helps frame a real risk.
