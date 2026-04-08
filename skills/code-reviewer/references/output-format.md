# Output Format

Use this structure for the final review.

```md
## Summary
- Brief description of what changed
- Overall assessment in one sentence

## Findings

### High
- Location: <file/symbol/hunk or "unknown">
  Issue: <what is wrong>
  Impact: <why it matters>
  Recommendation: <what to change>

### Medium
- ...

### Low
- ...

### Info
- ...

## Risk Assessment
- Overall risk: <low|medium|high>
- Confidence: <low|medium|high>
- Main uncertainty: <if any>

## Score
- Score: <1-10>/10

## Top Recommendations
1. <highest-value fix>
2. <second-highest-value fix>
3. <third-highest-value fix>
```

For detailed commit, diff, PR/MR, or chunk-merged reviews, this expanded format is also valid:

```md
## Summary
- Brief description of what changed
- Overall assessment in one sentence

## Findings
...

## Weighted Scorecard
- Correctness and robustness: XX/40
- Security and risk exposure: XX/30
- Best practices and maintainability: XX/20
- Performance and resource efficiency: XX/5
- Commit-message clarity and reviewability: XX/5

## Total Score
- Chinese output: 总分:XX分
- English output: Total Score: XX/100

## Top Recommendations
1. ...
2. ...
3. ...
```

## Rules

- If a severity level has no findings, omit that section.
- If there are no material findings, say so under `Findings` and still include residual risk or uncertainty.
- Keep findings concrete and concise.
- Avoid speculative claims without stating uncertainty.
- Localize section headings and field labels to match the user's language.
- For Chinese output, prefer headings such as `总结`, `问题`, `风险评估`, `加权评分明细`, `总分`, and `优先建议`.
