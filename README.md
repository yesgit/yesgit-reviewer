# Duck Code Reviewer

A comprehensive code review skill for Claude Code that provides structured, multi-depth review of code snippets, diffs, commits, and pull/merge requests.

## Overview

Duck Code Reviewer embeds a systematic approach to code review, helping you catch security issues, architecture violations, correctness bugs, and maintainability risks before they reach production.

## Usage

This skill activates when you ask Claude to:
- Review a code snippet or file
- Review a git diff or patch
- Review a commit or pull request
- Check for architecture or standards violations
- Perform a security-focused review

## Review Modes

### Quick Review
High-signal triage for fast feedback:
- Prioritizes correctness, obvious regressions, missing tests, and security risks
- Avoids deep architecture inference or style-only feedback
- Best for pre-commit sanity checks

### Standard Review
Comprehensive analysis:
- Deep architecture and design reasoning
- Cross-file analysis
- Security, performance, maintainability assessment
- Best for merge readiness and architecture reviews

## Features

- **Multi-agent review**: Automatically splits large diffs across multiple reviewers for thorough coverage
- **Constraint discovery**: Locates and applies project-specific rules from architecture docs and lint configs
- **Security-focused**: Prioritizes exploitable issues and unsafe defaults
- **Design inference**: Learns patterns from existing code when explicit docs are missing
- **Scoring**: Provides 1-10 score for lightweight reviews or weighted 0-100 scorecard for detailed reviews

## Output Format

Every review includes:
1. Summary of the change
2. Findings grouped by severity (high, medium, low, info)
3. Location, issue, impact, and recommendation for each finding
4. Overall risk assessment
5. Score (1-10 or 0-100)
6. Top 3 recommendations

## Installation

Add to your Claude Code skills configuration:

```json
{
  "skills": {
    "paths": ["/path/to/duck-code-reviewer/skills"]
  }
}
```

Or install via marketplace (when published).

## Repository

https://github.com/yesgit/duck-code-reviewer

## License

MIT
