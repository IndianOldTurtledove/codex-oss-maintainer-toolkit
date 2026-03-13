# Maintainer Workflow Patterns

Patterns for structuring repeatable Codex-assisted maintainer work.

## Issue Triage Workflow

```markdown
## Incoming Issue

1. Summarize the report in one paragraph.
2. Classify: bug / feature / support / duplicate.
3. Identify affected files, owners, and reproduction steps.
4. Decide the next action:
   - request more detail
   - open implementation task
   - close as duplicate
   - redirect to docs/support
5. Record the decision in a reusable template.
```

## PR Review Workflow

```markdown
## Pull Request Review

1. Read the PR description and linked issue.
2. Inspect file boundaries and architectural impact.
3. Run or suggest the smallest useful validation command.
4. Review for correctness, tests, rollback risk, and release notes.
5. Output actionable comments with file paths.
```

## Debugging Workflow

```markdown
## Debugging

1. Reproduce the failure.
2. Read the failing path before editing.
3. Compare with a nearby working pattern.
4. Test one hypothesis at a time.
5. Verify the fix and check for regressions.
```

## Release Note Workflow

```markdown
## Release Notes

1. Group merged changes by user-facing impact.
2. Pull migrations, flags, or rollout constraints into a dedicated section.
3. Add verification commands and rollback notes.
4. Keep the summary short; push details into bullet lists.
```

## Plan-Validate-Execute

Use this when the task is high risk or touches many files.

```markdown
1. Plan the change and list affected files.
2. Validate assumptions (tests, schema, repo rules, owners).
3. Execute the smallest safe batch.
4. Verify the result immediately.
5. Record follow-up work in dev docs.
```

## Choosing the Right Pattern

| Task Type | Pattern |
|-----------|---------|
| New issue intake | Issue Triage |
| Completed feature | PR Review |
| Production bug | Debugging |
| Release prep | Release Note Workflow |
| Multi-file refactor | Plan-Validate-Execute |
