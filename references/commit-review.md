# Commit Review

Use this guide when the review target is a single commit or a small stack of tightly related commits.

## Goal

Review the diff in the context of the commit message and assess whether the commit is coherent, correct, and safe to land.

## Process

1. Read the commit message first.
2. Infer the intended change and compare it with the actual diff.
3. Review the code change using [diff-review.md](diff-review.md).
4. Evaluate whether the commit is well-scoped and self-consistent.
5. Call out missing tests, rollout notes, or context if the commit changes behavior.

## Commit-specific checks

- Does the commit message describe the actual behavior change?
- Does the commit mix unrelated concerns?
- Would the commit be understandable in history six months later?
- Is the change atomic enough to revert cleanly if needed?
- Are there follow-up edits implied but missing from the commit?

## Findings that matter

Prioritize:
- commit message mismatches
- mixed refactor and behavior changes
- incomplete behavior changes split awkwardly across commits
- broad commits that hide risk
