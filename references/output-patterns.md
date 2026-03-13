# Maintainer Output Patterns

Patterns for producing consistent maintainer-facing outputs.

## Issue Triage Template

```markdown
# Issue Triage

## Summary
[One paragraph]

## Classification
- Type: bug / feature / support / duplicate
- Priority: high / medium / low

## Evidence
- Reproduction:
- Affected paths:
- Validation command:

## Next Action
1. ...
2. ...
```

## PR Review Template

```markdown
# PR Review

## Summary
[One sentence]

## Must Fix
1. [file] Problem and why it matters

## Should Fix
1. [file] Improvement suggestion

## Verification
- Command:
- Result:
```

## Release Note Template

```markdown
# Release Notes

## Highlights
- User-facing change
- Operational change

## Migration / Flags
- Required action

## Verification
- Command 1
- Command 2
```

## Maintainer Status Update Template

```markdown
# Maintainer Update

## Done
- ...

## In Progress
- ...

## Blockers
- ...

## Next Steps
1. ...
2. ...
```

## Choosing the Right Pattern

| Output | Pattern | Strictness |
|--------|---------|------------|
| Issue intake | Issue Triage | Medium |
| PR review | PR Review | High |
| Release communication | Release Note | Medium |
| Async handoff | Maintainer Status Update | Medium |
