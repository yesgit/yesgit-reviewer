# Cross-Platform Notes

This skill should remain portable across macOS, Linux, and Windows environments whenever possible.

## Script design rules

- Prefer Python 3 standard library over shell-specific tooling.
- Avoid relying on Bash-only features for core helper logic.
- Avoid GNU-specific flags when a Python implementation is practical.
- Read and write UTF-8 text explicitly.
- Use filesystem-safe path handling via `pathlib` or `os.path`.
- Do not assume `/tmp`, `/bin/bash`, or Unix-only directory layouts.

## Current helper scripts

The helper scripts in `scripts/` are implemented in Python and use only the standard library:
- `normalize_diff.py`
- `split_diff.py`
- `summarize_findings.py`
- `discover_constraints.py`
- `resolve_effective_constraints.py`
- `infer_design_constraints.py`

That makes them broadly portable as long as Python 3 is available.

## Operational expectations

- The host agent may still use platform-specific tools such as `git`, `gh`, or `glab` when available.
- The skill itself should not require those tools for its core review logic unless a future scenario explicitly depends on them.
- If a platform-specific command is suggested, provide a fallback when possible.
