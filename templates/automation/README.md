# Codex Automation Helpers

Standalone scripts that complement AGENTS.md and reusable skills.

These scripts are designed for manual use, CI hooks, or editor integrations. They are not tied to a proprietary IDE event model.

## Included Scripts

| Script | Purpose |
|--------|---------|
| `recommend-skills.py` | Suggest helper skills from a prompt and optional file list |
| `debug-task-detector.py` | Detect when a debugging workflow should be enforced |
| `investigate-change.py` | Generate an investigation checklist before editing |
| `suggest-checks.py` | Suggest validation commands from file paths or `git diff` |
| `file-size-check.py` | Warn when files exceed a size threshold |
| `verify-changed-files.sh` | Run basic syntax/format sanity checks on changed files |

## Typical Usage

```bash
python3 .codex/automation/recommend-skills.py "triage this issue about auth regressions"
python3 .codex/automation/debug-task-detector.py "TypeError in release script on line 42"
python3 .codex/automation/investigate-change.py --changed
python3 .codex/automation/suggest-checks.py --changed
python3 .codex/automation/file-size-check.py src/huge_module.py
bash .codex/automation/verify-changed-files.sh
```
