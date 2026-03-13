# Codex Maintainer Agent Prompts

Reusable sub-agent prompts for Codex-assisted repository maintenance.

## Included Prompts

| Prompt | Purpose | When to Use |
|--------|---------|-------------|
| `code-reviewer.md` | Review a finished change set | Before merge or release |
| `error-resolver.md` | Diagnose and fix build/runtime failures | When checks or runtime fail |

## How to Use

- Use them with Codex sub-agent / task delegation features, or
- read the file and paste the workflow into your prompt.

Keep prompts concrete: trigger conditions, workflow, output format, and constraints.
