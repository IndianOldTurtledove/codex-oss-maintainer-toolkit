# Codex OSS Maintainer Toolkit

[中文](README.md) | [English](README_EN.md)

A Codex-first toolkit for open-source maintainers who want to turn a repository into a clean `Codex + AGENTS.md + reusable skills` workflow.

## What This Repository Provides

1. **A Codex maintainer skill** for designing maintainer workflows
2. **AGENTS.md templates** for project-specific instructions
3. **Automation script templates** for triage, debugging, file checks, and verification
4. **Maintainer agent prompts** for PR review and error resolution
5. **Dev docs templates** for cross-session progress tracking

## Positioning

Recommended published repository name: `codex-oss-maintainer-toolkit`

This repository is no longer positioned as legacy single-vendor infrastructure. It is focused on:

- Codex-native repository setup
- AGENTS.md adoption
- open-source maintainer automation
- skill authoring and validation
- PR review, issue triage, and release-note workflows

## Quick Start

### Clone the repository

```bash
git clone https://github.com/IndianOldTurtledove/codex-oss-maintainer-toolkit.git
cd codex-oss-maintainer-toolkit
```

### Install as a global Codex skill

```bash
./install.sh --global --yes
```

Default destination:

```bash
~/.codex/skills/codex-oss-maintainer-toolkit
```

### Bootstrap another repository

```bash
./install.sh --project --target /path/to/your/repo --yes
```

This creates:

```text
/path/to/your/repo/
├── AGENTS.md
├── .codex/
│   ├── agents/
│   ├── automation/
│   └── skills/
│       └── skill-rules.json
└── dev/
    ├── active/
    └── archive/
```

## Core Commands

```bash
python3 scripts/init_skill.py issue-triage
python3 scripts/quick_validate.py .codex/skills/issue-triage
python3 scripts/package_skill.py .codex/skills/issue-triage
```

## Automation Templates

The reusable scripts live in `templates/automation/`.

| Script | Purpose |
|--------|---------|
| `recommend-skills.py` | Suggest local skills for a prompt |
| `debug-task-detector.py` | Detect when a systematic debugging workflow should be used |
| `investigate-change.py` | Generate a pre-edit investigation checklist |
| `suggest-checks.py` | Suggest validation commands from file paths or `git diff` |
| `file-size-check.py` | Warn about oversized files |
| `verify-changed-files.sh` | Run basic verification over files in `git diff` |

## Project Structure

```text
codex-oss-maintainer-toolkit/
├── AGENTS.md
├── SKILL.md
├── install.sh
├── scripts/
├── references/
├── templates/
├── examples/
└── demo/
```

## Design Principles

1. **Codex-first**: organize around AGENTS.md, skills, and verifiable scripts
2. **Maintainer-centric**: reduce repetitive review, triage, and release overhead
3. **Progressive disclosure**: keep core instructions short, push detail into references/
4. **Evidence-driven**: every workflow should end with explicit verification

## Recommended Application Framing

If you plan to apply for OpenAI's Codex for Open Source program, emphasize that this repository:

- captures real maintainer workflows,
- reduces issue triage / PR review / release overhead,
- and is built around Codex-native workflows such as AGENTS.md, skills, and repeatable automation.

## Validation Commands

```bash
python3 scripts/quick_validate.py .
python3 scripts/init_skill.py demo-skill --path /tmp/codex-skills
python3 scripts/package_skill.py /tmp/codex-skills/demo-skill /tmp
bash install.sh --help
rg -n -i "legacy-brand|legacy-hook|legacy-config" .
```

## License

MIT License. See [LICENSE](LICENSE).
