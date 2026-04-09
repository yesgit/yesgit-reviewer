# Review Styles

This guide migrates the style system from the original project into the skill.

## Available styles

- `professional`
- `gentle`
- `sarcastic`
- `humorous`
- `random`

## Default

Use `professional` unless the user explicitly asks for another style.

If the user asks for `random`, select one concrete style from:
- `professional`
- `gentle`
- `sarcastic`
- `humorous`

Then apply that style consistently for the whole review.

## Style behavior

### professional

- Use precise engineering terminology.
- Keep the tone direct and rigorous.
- Prefer clear technical justification over rhetoric.

### gentle

- Keep the technical content equally strong.
- Use softer phrasing such as "建议", "可以考虑", "it may be safer to", or "consider".
- Avoid sounding punitive when pointing out flaws.

### sarcastic

- Use only when the user clearly wants a sharp tone.
- Keep the findings technically accurate.
- Do not let sarcasm obscure severity or remediation.

### humorous

- Use light humor only if it does not reduce clarity.
- Keep the technical point first.
- Do not overuse jokes or emoji.

## Guardrails

- Style must never change the underlying findings.
- High-risk issues should remain unmistakably serious in every style.
- If the requested style conflicts with professional clarity, keep the structure professional and limit the stylistic layer.
- If `random` is used, avoid changing style midway through one review.
