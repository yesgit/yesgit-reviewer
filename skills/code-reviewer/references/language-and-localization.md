# Language and Localization

Use the user's language by default.

## Default behavior

- If the user asks in Chinese, review in Chinese.
- If the user asks in English, review in English.
- If the user mixes languages, prefer the language used for the request itself.
- If the user explicitly requests another language, follow that request.

## Code and identifiers

- Keep code, file paths, identifiers, function names, CLI commands, and error strings in their original language.
- Do not translate code tokens.
- Only translate surrounding explanations and recommendations.

## Review terminology

Keep severity labels stable unless the user explicitly asks for localized labels.

Preferred default labels:
- `High`
- `Medium`
- `Low`
- `Info`

If the user wants fully localized output, localized labels are acceptable as long as the structure remains the same.

## Section headings and score labels

Section headings should normally follow the user's language as well.

Recommended Chinese localization:
- `Summary` -> `总结`
- `Findings` -> `问题`
- `Risk Assessment` -> `风险评估`
- `Weighted Scorecard` -> `加权评分明细`
- `Total Score` -> `总分`
- `Top Recommendations` -> `优先建议`

Recommended Chinese field labels:
- `Overall risk` -> `整体风险`
- `Confidence` -> `置信度`
- `Main uncertainty` -> `主要不确定性`

If the response body is Chinese, do not leave these section headers in English unless the user explicitly asks for bilingual output.

## Mixed-language repositories

When repository comments, docs, and identifiers mix Chinese and English:
- describe behavior in the user's language
- preserve original quoted strings only when needed for precision
- avoid unnecessary translation of framework or domain terminology
