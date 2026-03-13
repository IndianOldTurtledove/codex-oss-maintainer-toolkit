# Dev Docs - Cross-Session Context System

Preserve implementation decisions, progress, and constraints across Codex sessions.

## When to Use

| Scenario | Use Dev Docs? |
|----------|---------------|
| Tasks > 2 hours | Yes |
| Multi-session features | Yes |
| Complex multi-file changes | Yes |
| Simple bug fixes | No |
| Single-file changes | No |

## Directory Structure

```text
dev/
├── README.md
├── active/
│   └── [task-name]/
│       ├── [task-name]-plan.md
│       ├── [task-name]-context.md
│       └── [task-name]-tasks.md
└── archive/
```

## Key Principles

1. `context.md` is the most important file.
2. Record both the decision and the reason.
3. Keep entries short and operational.
4. Update after milestones, not only at the end.
