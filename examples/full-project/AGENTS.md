# AGENTS.md

## Purpose

This repository is maintained with Codex. Use this file to tell Codex how the project is organized, what rules matter, and how changes must be validated.

## Repository Map

Replace these placeholders with your real structure:

- `src/`: production source code
- `tests/`: automated checks
- `scripts/`: operational scripts and local helpers
- `docs/` or `dev/`: decision logs and handoff notes

## Standard Workflow

1. Read the relevant files before editing.
2. Prefer the smallest safe change.
3. Follow existing patterns before introducing a new abstraction.
4. Run targeted validation after each meaningful change.
5. Record blockers, risks, and follow-up work in `dev/`.

## Validation Policy

Document the commands that prove a change works. Example:

```bash
pytest -q
pnpm test
pnpm lint
python3 scripts/check_something.py
```

## Maintainer Notes

- List owners for risky areas.
- Call out production or migration constraints.
- Note any required environment variables or credentials boundaries.
- Keep this file close to the code it governs and update it when the repo layout changes.

## Optional Local Tooling

- `.codex/automation/`: reusable helper scripts
- `.codex/agents/`: sub-agent prompts or review playbooks
- `.codex/skills/`: local skill drafts or helper metadata
- `dev/`: long-running task context
