# GitHub PR Review

Use this guide when the review target is a GitHub pull request and the host environment can provide PR metadata, diff context, checks, or comments.

## Goal

Review the pull request as a coherent unit, using the PR description, code diff, and available status signals to determine whether the change is safe and well-executed.

## Preferred context

If available, gather:
- PR title and description
- changed files and diff
- linked issue or ticket
- CI or check results
- notable review comments or unresolved discussions

Typical host tools may include:
- `gh pr view`
- `gh pr diff`
- `gh pr checks`

These tools are optional. The skill should still work with raw PR text and diff content when CLI tooling is unavailable.

## Review focus

- Does the implementation match the PR goal?
- Is the PR size reasonable for review?
- Are there hidden behavior changes not described in the PR?
- Are failing or missing checks relevant to merge risk?
- Are rollback, migration, or compatibility concerns called out?

## Output expectations

- Mention CI or check posture if available.
- Call out scope or reviewability problems if the PR is too large or noisy.
- Keep findings focused on merge risk and maintainability, not style trivia.
