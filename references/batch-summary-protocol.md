# Batch Summary Protocol

Use this protocol when a large diff or multi-file change is reviewed in chunks.

## Goal

Merge chunk-level reviews into one final report without losing the details developers need to locate problems.

## Required output structure

The merged report should contain three parts:

1. Global summary and recommendations
2. Chunk-level findings retention
3. Unified scorecard and total score

## Part 1: Global summary

- Deduplicate overlapping findings across chunks.
- Summarize the main risk themes.
- Provide consolidated recommendations instead of repeating chunk text.

## Part 2: Chunk-level retention

Keep enough chunk detail so the reader can map issues back to files or logical areas.

Recommended format:

```md
#### Chunk X (<file range or area>)
<Preserve the important findings and score details for that chunk>
```

Do not flatten everything into only a top-level summary if that would hide where the issues were found.

## Part 3: Unified scorecard

Re-score the entire change set after consolidation.

Do not:
- average chunk scores mechanically
- copy the highest or lowest chunk score
- reuse chunk numbers without recomputing overall impact

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
- chunk detail was not lost
- duplicate issues were merged
- the final score reflects full-change risk, not chunk arithmetic
