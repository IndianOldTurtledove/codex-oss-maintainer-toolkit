# AGENTS.md

## Mission

This repository is a Codex-first toolkit for open-source maintainers. Keep the repo aligned with Codex terminology, AGENTS.md conventions, reusable skills, and maintainer automation workflows.

## Repository Map

- `SKILL.md`: the primary Codex skill for maintainer workflow design.
- `scripts/`: authoring helpers for creating, validating, and packaging skills.
- `references/`: reusable patterns for outputs and multi-step workflows.
- `templates/`: bootstrap material for Codex projects (`AGENTS.md`, automation scripts, agent prompts, dev docs, skill catalog).
- `examples/full-project/`: example repository layout after bootstrapping.
- `demo/`: marketing/demo pages that should stay consistent with the public positioning.

## Editing Rules

1. Read before editing and keep changes minimal.
2. If you change public positioning, update `README.md`, `README_EN.md`, `SKILL.md`, `install.sh`, and `demo/` in the same turn.
3. If you change anything in `templates/`, sync the same structure in `examples/full-project/`.
4. Prefer Codex/OpenAI terminology. Remove stale vendor-specific references unless they are historical context that is explicitly needed.
5. Validate with targeted commands before finishing. At minimum, run the repository search guard and the relevant Python/shell checks.

## Default Maintainer Workflow

1. Audit the repository and identify maintainer bottlenecks.
2. Write or refine `AGENTS.md` close to the work.
3. Move repetitive maintainer tasks into skills, references, or automation scripts.
4. Add verification commands so contributors can prove changes worked.
5. Keep templates, examples, and docs coherent.
