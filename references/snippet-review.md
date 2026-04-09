# Snippet and File Review

Use this guide when the input is a pasted code block, function, class, module, or file.

## Goal

Review the code based on the local context that is available, while being explicit about what cannot be validated without surrounding files, tests, or runtime behavior.

## Process

1. Infer the purpose of the code from names, comments, and structure.
2. Identify the main control flow and data flow.
3. Review for:
   - local correctness
   - obvious edge cases
   - unsafe assumptions
   - maintainability and readability
   - missing validation and tests
4. Separate confirmed issues from concerns that depend on missing context.

## What to avoid

- Do not invent project-wide constraints that are not shown.
- Do not demand stylistic changes unless they improve clarity or reduce risk.
- Do not treat missing surrounding code as proof of a bug.

## Strong findings in snippet review

Prioritize:
- clear logic errors
- unhandled edge cases
- resource leaks
- unsafe input handling
- state inconsistencies
- misleading names or abstractions that hide behavior
