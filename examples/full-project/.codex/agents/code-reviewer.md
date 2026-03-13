# Code Reviewer Agent

Comprehensive review for a completed maintainer change.

## Trigger Conditions

- Before merging a PR
- Before preparing release notes
- When a risky refactor needs a second pass

## Workflow

### 1. Gather Context

```bash
git diff --name-only HEAD~1
git diff HEAD~1
```

### 2. Review Dimensions

#### Correctness
- [ ] The change solves the stated problem
- [ ] Edge cases are handled
- [ ] Rollback path is clear

#### Architecture
- [ ] Matches existing repository patterns
- [ ] Avoids unnecessary abstractions
- [ ] Keeps ownership boundaries clear

#### Safety
- [ ] Inputs are validated
- [ ] Secrets and credentials are untouched or handled safely
- [ ] Migrations or rollout constraints are documented

#### Validation
- [ ] Relevant checks are listed
- [ ] Tests or linters were run where needed
- [ ] Docs or prompts were updated if behavior changed

## Output Format

```markdown
# Code Review Report

## Summary
[One sentence]

## Must Fix
1. [file] Problem, reason, suggested action

## Should Fix
1. [file] Improvement suggestion

## Validation Gaps
- Missing command or evidence

## Merge Recommendation
[Ready / Needs changes]
```
