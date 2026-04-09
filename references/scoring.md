# Scoring

This skill supports two scoring modes:
- compact score: `1-10`
- weighted scorecard: `0-100`

## When to use each mode

- Use `1-10` for lightweight snippet reviews or fast review passes.
- Use `1-10` by default for quick review mode.
- Use `0-100` when the user asks for detailed scoring, when reviewing commits or diffs with explicit history, or when merging chunk-level reviews.

## Compact method

Start from `10` and subtract based on severity, confidence, and coverage gaps.

Suggested deductions:
- High severity confirmed defect: `-3` each
- Medium severity confirmed defect: `-2` each
- Low severity confirmed defect: `-1` each
- Significant missing tests for behavior-changing code: `-1` to `-2`
- Major uncertainty due to missing context: `-1`

Quick review notes:
- Keep the score aligned to the limited scope of the pass.
- If the change needs standard review to judge safely, say so and lower confidence rather than pretending the compact score is authoritative.

## Compact interpretation

- `9-10`: Strong change with no material concerns
- `7-8`: Generally sound, but has moderate risks or gaps
- `5-6`: Noticeable issues that should be addressed before merge
- `3-4`: High-risk change with multiple serious concerns
- `1-2`: Unsafe to merge in current form

## Weighted method

Use the weighted profile from [default-review-profile.md](default-review-profile.md):

- Correctness and robustness: `40`
- Security and risk exposure: `30`
- Best practices and maintainability: `20`
- Performance and resource efficiency: `5`
- Commit-message clarity and reviewability: `5`

Subtract within each category based on the observed issues, then sum the categories.

## Rules

- Do not overfit the score to style nits.
- A single severe security bug can pull the score down sharply.
- If context is missing, reduce confidence and explain why.
- The score must match the written findings.
