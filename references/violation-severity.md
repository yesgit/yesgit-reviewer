# Violation Severity

Use this guide to grade architecture, design, and standards violations.

## High

Use `High` when the change:
- breaks a mandatory architectural boundary
- introduces forbidden dependencies
- violates security or safety policy
- modifies generated or protected files against explicit policy
- conflicts with a mandatory rule likely to cause production or organizational risk

## Medium

Use `Medium` when the change:
- violates a clear default design rule
- increases coupling or layering leakage
- bypasses an intended abstraction
- omits required tests or docs defined by local policy

## Low

Use `Low` when the change:
- violates a minor project convention
- weakens consistency without immediate risk
- diverges from naming or placement guidance that has limited impact

## Info

Use `Info` when:
- the docs are ambiguous
- two rules conflict and need owner clarification
- the change is compliant but carries policy-related follow-up work
