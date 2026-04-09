---
name: yesgit-reviewer
description: Review code snippets, files, diffs, commits, PR/MR changes, architecture and standards violations, and design drift from existing code conventions. Use when the user asks for code review, diff review, commit review, PR review, MR review, architecture review, standards review, design review, or security-focused review.
---

# YesGit Code Reviewer

## When to use

Use this skill when the user asks to:
- review a code snippet or file
- review a git diff or patch
- review a commit
- review a pull request or merge request
- review architecture, design, or coding-standard violations
- focus on security, correctness, maintainability, performance, or testing risks

## Input classification

First classify the input before reviewing:
- code snippet or file content
- git diff or patch
- commit-level review
- pull request or merge request review
- security-focused review

Read [references/input-modes.md](references/input-modes.md), then load the matching reference:
- code snippet or file: [references/snippet-review.md](references/snippet-review.md)
- diff or patch: [references/diff-review.md](references/diff-review.md)
- commit: [references/commit-review.md](references/commit-review.md)
- PR or MR: [references/pr-mr-review.md](references/pr-mr-review.md)
- GitHub pull request with repo metadata or `gh` context: [references/github-pr-review.md](references/github-pr-review.md)
- GitLab merge request with repo metadata or `glab` context: [references/gitlab-mr-review.md](references/gitlab-mr-review.md)
- architecture, design, or standards review: [references/architecture-review.md](references/architecture-review.md)
- design inference from existing code: [references/design-inference-review.md](references/design-inference-review.md)
- security-focused request: [references/security-review.md](references/security-review.md)

Always apply the baseline checklist in [references/review-checklist.md](references/review-checklist.md), the scoring rules in [references/scoring.md](references/scoring.md), and the output contract in [references/output-format.md](references/output-format.md).
Also follow [references/language-and-localization.md](references/language-and-localization.md) for output language and [references/cross-platform.md](references/cross-platform.md) for script portability expectations.
When you need a stronger, opinionated review posture derived from the original platform prompts, also read:
- [references/default-review-profile.md](references/default-review-profile.md)
- [references/review-styles.md](references/review-styles.md)
- [references/batch-summary-protocol.md](references/batch-summary-protocol.md)
- [references/customization.md](references/customization.md)
For architecture and standards review, also read:
- [references/constraint-sources.md](references/constraint-sources.md)
- [references/ai-tooling-rules.md](references/ai-tooling-rules.md)
- [references/rule-precedence.md](references/rule-precedence.md)
- [references/violation-severity.md](references/violation-severity.md)
- [references/codebase-baseline.md](references/codebase-baseline.md)
- [references/design-inference-review.md](references/design-inference-review.md)
Treat explicit documented rules as stronger than inferred repository conventions.
When discovering rule sources, prioritize readable text-based policy files rather than arbitrary artifacts.

## Review workflow

1. Identify the review scope and the likely intent of the change.
2. Read the matching scenario reference for the input type.
3. Decide whether to review serially or use a multi-agent chunked review:
   - prefer serial review for snippets, single files, or small diffs
   - prefer multi-agent review for large diffs, multi-file PRs/MRs, mixed backend and frontend changes, or requests that combine multiple lenses such as security plus architecture
   - if the runtime does not support subagents, keep the same workflow but execute it serially
4. Apply the baseline checklist and note missing context explicitly instead of guessing.
5. If the diff is noisy or too large, use:
   - `scripts/normalize_diff.py` to remove low-value noise
   - `scripts/split_diff.py` to split the diff into smaller chunks
   - `scripts/discover_constraints.py` to locate readable architecture and policy files
   - `scripts/resolve_effective_constraints.py` to determine which explicit rules apply to a target path
   - `scripts/infer_design_constraints.py` to infer baseline patterns from existing code only when explicit docs are incomplete
6. For multi-agent review, split work into disjoint chunks by file groups, directories, or concern areas. Keep each chunk self-contained enough that one reviewer can inspect it without depending heavily on another chunk.
7. Give every subagent the same review objective, applicable constraints, and required output contract. Each subagent should report only concrete findings for its assigned chunk and should not attempt to produce the final merged review.
8. Review each chunk for correctness, security, maintainability, performance, testing, and operational risk.
9. If multiple chunk-level reviews exist, use `scripts/summarize_findings.py` or equivalent reasoning to merge them. Follow [references/batch-summary-protocol.md](references/batch-summary-protocol.md) when merging chunk or subagent results.
10. Score the change using [references/scoring.md](references/scoring.md). If the user asks for a detailed scorecard or if the review is chunked, prefer the weighted 100-point profile.
11. Format the answer exactly as defined in [references/output-format.md](references/output-format.md).
12. Match the user's language unless they request a different one explicitly.

## Multi-agent rules

- Do not require the user to opt in explicitly. Auto-select multi-agent review when the scope justifies it.
- Do not use subagents for tiny or obvious reviews where dispatch overhead exceeds the likely gain.
- Split by disjoint ownership when possible to reduce duplicate findings.
- If the user asks for a specific focus such as security or architecture, either assign one specialized pass to that focus or apply that lens consistently across all chunks.
- Give subagents only the chunk-local context plus the minimum global context they need, such as the review goal, severity rubric, and explicit repository rules.
- Require subagents to output findings using the same fields as the final review: location, issue, impact, recommendation, and severity.
- Require subagents to mark uncertainty explicitly instead of guessing across chunk boundaries.
- The primary reviewer must deduplicate overlapping findings, resolve severity conflicts, and produce one final score for the whole change.
- Never average chunk scores mechanically. Recompute the overall score after consolidation.
- If a bug spans multiple chunks, keep one canonical finding in the final report and mention affected areas in the location or impact text.

## Review rules

- Prefer concrete findings over generic advice.
- Tie every substantial finding to a file, symbol, hunk, or behavior when possible.
- Distinguish confirmed bugs from uncertain risks.
- Call out missing tests when behavior changes are not covered.
- Avoid style-only nitpicks unless they affect readability, correctness, or maintainability.
- If the context is insufficient, say what is missing and how that limits confidence.
- For security-focused reviews, prioritize exploitable issues and unsafe defaults.
- For architecture and design reviews, prefer explicit policy sources over inferred codebase patterns.
- Treat inferred design baselines as heuristics, not hard rules, unless repeated evidence is strong and no explicit policy contradicts them.

## Output requirements

Every review should include:
- a short summary of the change
- findings grouped by severity: high, medium, low, info
- for each finding: location, issue, impact, recommendation
- an overall risk assessment
- a score, using `1-10` for lightweight reviews or the weighted `0-100` scorecard when appropriate
- the top 3 recommendations

If there are no material findings, state that explicitly and mention any residual uncertainty or test coverage gaps.
