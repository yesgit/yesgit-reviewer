# Rule Precedence

Use this precedence model for architecture, design, and standards review.

## Core principle

Rules are hierarchical and path-scoped. More local rules override more distant default rules.

## Resolution order

For a target file or directory, evaluate rules from nearest scope to farthest:

1. Rules in the target directory
2. Rules in the nearest ancestor directory
3. Rules in higher ancestor directories
4. Repository root rules

## Rule strengths

Each rule should be interpreted as one of:
- `mandatory`
- `default`
- `advisory`

## Override behavior

- `mandatory` rules cannot be silently overridden by weaker parent or child defaults.
- `default` rules may be overridden by more local `default` or `mandatory` rules.
- `advisory` rules should guide review but should not be treated as hard violations unless the user asks for strict enforcement.

## Conflict handling

- More local `default` overrides less local `default`.
- More local `mandatory` overrides less local `default`.
- If two `mandatory` rules conflict, report a policy conflict.
- If no local override exists, inherit the parent rule.

## Reporting

When citing a violation, state:
- which rule won precedence
- which file defined it
- which parent rules were superseded, if relevant
