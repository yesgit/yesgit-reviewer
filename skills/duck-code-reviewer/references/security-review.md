# Security Review

Use this guide for security-focused code review or whenever the change touches trust boundaries.

## Priorities

Prioritize issues by exploitability and blast radius:
- remote code execution
- auth bypass
- privilege escalation
- injection
- sensitive data exposure
- SSRF and internal network access
- path traversal
- insecure defaults

## Security checklist

### Input handling

- Is untrusted input validated, normalized, and encoded for its sink?
- Are allowlists used where appropriate?
- Are parser edge cases or dangerous formats involved?

### Auth and authorization

- Are permissions enforced server-side?
- Can object identifiers be tampered with?
- Are tenant or user boundaries preserved?

### Data handling

- Are secrets logged, returned, or stored insecurely?
- Is sensitive data minimized and masked?
- Are tokens scoped and rotated appropriately?

### Dangerous sinks

- SQL and query construction
- shell or command execution
- file paths and archive extraction
- dynamic evaluation
- template rendering
- outbound HTTP requests

### Safety defaults

- Does failure open access accidentally?
- Are debug paths exposed in production?
- Does missing config reduce security?

## Security output

When reporting a security finding, include:
- the trust boundary involved
- a plausible attack path
- the likely impact
- the concrete mitigation
