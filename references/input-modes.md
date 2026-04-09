# Input Modes

Classify the review request before loading scenario-specific guidance.

## Code snippet or file

Use this mode when the user provides:
- a code block
- a full file
- a pasted function or class

Approach:
- infer intent from names, comments, and surrounding code
- focus on local correctness, readability, maintainability, and obvious security issues
- do not assume unchanged code outside the snippet is correct

## Git diff or patch

Use this mode when the input contains:
- unified diff markers such as `diff --git`, `@@`, `+++`, `---`
- added and removed lines

Approach:
- evaluate the behavioral change introduced by the patch
- pay extra attention to regressions caused by deleted logic
- note when the diff lacks enough surrounding context

## Commit review

Use this mode when the input is one commit or a small set of commits.

Approach:
- review the diff as the primary artifact
- use the commit message to infer intended behavior
- flag when the commit message and the actual change do not match
- assess whether the commit is too broad or mixes unrelated changes

## Pull request or merge request

Use this mode when the review includes:
- PR/MR description
- linked issues
- multiple files or commits
- CI status or test results

Approach:
- understand the stated goal first
- assess whether the scope is coherent and reviewable
- review the code changes, test coverage, and rollout risk together

## Security-focused review

Use this mode when the user explicitly asks for security review or when the code touches:
- authentication or authorization
- secrets or credentials
- input handling
- networking
- file system access
- database queries
- command execution

Approach:
- prioritize exploitability and impact
- focus less on style and more on unsafe behavior and trust boundaries
