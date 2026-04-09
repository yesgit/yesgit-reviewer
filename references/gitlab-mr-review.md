# GitLab MR Review

Use this guide when the review target is a GitLab merge request and the host environment can provide MR metadata, changes, pipelines, or discussions.

## Goal

Review the merge request with emphasis on correctness, rollout safety, and whether the MR is ready to merge.

## Preferred context

If available, gather:
- MR title and description
- changed files and diff
- pipeline status
- linked issue, task, or incident
- unresolved discussions

Typical host tools may include:
- `glab mr view`
- `glab mr diff`
- `glab mr checks`

These tools are optional. The skill should still work when only MR text and diff are provided.

## Review focus

- Does the MR description explain intent, rollout, and risk?
- Is the MR reviewable as a single unit?
- Are there missing tests, migration notes, or follow-up tasks?
- Do pipeline signals increase confidence or reveal risk?
- Is the MR safe to merge and safe to roll back?

## Output expectations

- Mention pipeline posture if available.
- Highlight operational concerns such as migration order, compatibility, and monitoring.
- Distinguish must-fix blockers from follow-up suggestions.
