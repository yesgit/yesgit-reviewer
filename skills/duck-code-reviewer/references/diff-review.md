# Diff Review

Use this guide for unified diffs, patches, and commit-level diffs.

## Goal

Review the behavior introduced by the change, not just the edited lines.

## Process

1. Identify the files and subsystems touched.
2. Infer the intent of each hunk.
3. Review additions, deletions, and moved logic for:
   - incorrect behavior
   - missing validation
   - broken invariants
   - hidden side effects
   - missing tests
4. If context is too thin, say so explicitly.

## Diff-specific risks

- Deleted checks or guards causing regressions
- Renames that silently change semantics
- New branches without matching error handling
- Schema or config shape changes not reflected elsewhere
- Changes that require companion edits in tests, docs, or callers

## Large diffs

For large diffs:
- normalize noisy hunks first
- split by file or logical area
- review each chunk independently
- merge only the material findings into the final report

If many files are touched, prioritize:
- auth and permission code
- persistence and state transitions
- money, billing, or workflow logic
- concurrency and retry logic
- public API behavior
