# Full Codex Maintainer Project Example

This example shows how a repository can look after bootstrapping it with the Codex OSS Maintainer Toolkit.

## Structure

```text
full-project/
├── AGENTS.md
├── .codex/
│   ├── agents/
│   │   ├── code-reviewer.md
│   │   ├── error-resolver.md
│   │   └── README.md
│   ├── automation/
│   │   ├── recommend-skills.py
│   │   ├── debug-task-detector.py
│   │   ├── investigate-change.py
│   │   ├── suggest-checks.py
│   │   ├── file-size-check.py
│   │   └── verify-changed-files.sh
│   └── skills/
│       └── skill-rules.json
└── dev/
    ├── README.md
    ├── TEMPLATE-context.md
    ├── TEMPLATE-plan.md
    └── TEMPLATE-tasks.md
```

## How to Use

1. Copy `AGENTS.md` into the repository root and tailor it.
2. Keep `.codex/automation/` for reusable maintainer scripts.
3. Store sub-agent prompts in `.codex/agents/`.
4. Use `dev/` for multi-session context and handoffs.

## Typical Commands

```bash
python3 .codex/automation/recommend-skills.py "review this release regression"
python3 .codex/automation/investigate-change.py --changed
python3 .codex/automation/suggest-checks.py --changed
bash .codex/automation/verify-changed-files.sh
```
