# Input Modes

Classify the review request before loading scenario-specific guidance.

## Review depth

Choose one depth after classifying the input type.

### Quick review

Use this depth when:
- the user explicitly asks for a quick review, fast review, lightweight review, or sanity check
- the likely goal is pre-commit triage, prioritization, or a compact first-pass judgment
- the user wants high-signal findings rather than exhaustive coverage

Expectations:
- focus on correctness, obvious regressions, missing tests, and direct security risk
- return the highest-value findings first
- be explicit that coverage is not exhaustive

Do not keep the request in quick review if:
- the user asks for architecture, standards, security deep dive, or merge readiness
- the user asks for exhaustive coverage or detailed scoring
- the available context is too incomplete to support even a reliable triage pass

In those cases, upgrade to the standard scenario workflow explicitly.

### Standard review

Use this depth for everything else, especially when review completeness matters more than speed.

## Code snippet or file

Use this mode when the user provides:
- a code block
- a full file
- a pasted function or class

Approach:
- infer intent from names, comments, and surrounding code
- focus on local correctness, readability, maintainability, and obvious security issues
- do not assume unchanged code outside the snippet is correct
- if the request is quick review, keep the output compact and avoid broad repository-wide inferences

## Git diff or patch

Use this mode when the input contains:
- unified diff markers such as `diff --git`, `@@`, `+++`, `---`
- added and removed lines

Approach:
- evaluate the behavioral change introduced by the patch
- pay extra attention to regressions caused by deleted logic
- note when the diff lacks enough surrounding context
- quick review is acceptable if the user wants a compact triage pass
- standard review is preferable if the user wants deeper assurance about cross-file behavior

## Commit review

Use this mode when the input is one commit or a small set of commits.

Approach:
- review the diff as the primary artifact
- use the commit message to infer intended behavior
- flag when the commit message and the actual change do not match
- assess whether the commit is too broad or mixes unrelated changes
- use quick review only when the user explicitly wants a fast pass

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
- do not use quick review as the default for PR/MR review

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
- prefer standard review unless the user explicitly requests a narrow, quick security triage
