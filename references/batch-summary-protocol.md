# Batch Summary Protocol

Use this protocol when a large diff or multi-file change is reviewed in chunks, including cases where chunks were reviewed by multiple subagents in parallel.

## Goal

Merge chunk-level reviews into one final report without losing the details developers need to locate problems.

## Required output structure

The merged report should contain four parts:

1. Global summary and recommendations
2. Severity-grouped findings as the primary view
3. A compact location index for chunk or file traceability
4. Unified scorecard and total score

## Part 1: Global summary

- Deduplicate overlapping findings across chunks.
- Deduplicate overlapping findings across subagents that reviewed neighboring files or related layers.
- Summarize the main risk themes.
- Provide consolidated recommendations instead of repeating chunk text.

## Part 2: Severity-grouped findings

Present the final findings primarily by severity so the reader can quickly understand what to fix first.

Each merged finding should still preserve enough location detail to map back to files, hunks, symbols, or logical areas.

Do not expose raw subagent chatter or internal coordination notes.

## Part 3: Location index

After the severity-grouped findings, add a compact location index so the reader can navigate the code quickly.

Recommended format:

```md
## Location Index
- `path/to/file.py:42`: finding A, finding C
- `pkg/service/auth.ts#login`: finding B
- `Chunk 3 (frontend form validation)`: finding D
```

Use chunk labels only when a precise file or symbol reference is not practical.

## Part 4: Unified scorecard

Re-score the entire change set after consolidation.

Do not:
- average chunk scores mechanically
- copy the highest or lowest chunk score
- reuse chunk numbers without recomputing overall impact
- preserve conflicting severities without resolving them into one final severity per finding

When using the weighted 100-point profile, include:
- Correctness and robustness: `XX`
- Security and risk exposure: `XX`
- Best practices and maintainability: `XX`
- Performance and resource efficiency: `XX`
- Commit-message clarity and reviewability: `XX`

The last line should be:
- Chinese output: `总分:XX分`
- English output: `Total Score: XX/100`

## Self-check

Before finalizing a merged review, verify:
- location traceability was not lost
- duplicate issues were merged
- conflicting severities were normalized
- the final score reflects full-change risk, not chunk arithmetic
