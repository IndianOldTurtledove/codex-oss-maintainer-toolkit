#!/bin/bash
# Codex OSS Maintainer Toolkit installer

set -euo pipefail

MODE="project"
TARGET=""
YES=false
FORCE=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --global|-g)
      MODE="global"
      shift
      ;;
    --project|-p)
      MODE="project"
      shift
      ;;
    --target|-t)
      TARGET="$2"
      shift 2
      ;;
    --yes|-y)
      YES=true
      shift
      ;;
    --force|-f)
      FORCE=true
      shift
      ;;
    --help|-h)
      cat <<'HELP'
Usage: ./install.sh [--global|--project] [--target PATH] [--yes] [--force]

Modes:
  --global, -g   Install this repository as a reusable Codex skill bundle
  --project, -p  Bootstrap a target repository with AGENTS.md and maintainer templates

Options:
  --target, -t   Install destination. Defaults to ~/.codex/skills/codex-oss-maintainer-toolkit for --global,
                 or the current working directory for --project.
  --yes, -y      Skip confirmation prompt
  --force, -f    Overwrite existing files when bootstrapping a project
  --help, -h     Show this help message
HELP
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 1
      ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ "$MODE" == "global" ]]; then
  DEST="${TARGET:-$HOME/.codex/skills/codex-oss-maintainer-toolkit}"
  if [[ "$YES" != true ]]; then
    echo "Install Codex skill bundle to: $DEST"
    read -r -p "Continue? [y/N] " REPLY
    [[ "$REPLY" =~ ^[Yy]$ ]] || exit 1
  fi

  mkdir -p "$DEST"
  for item in SKILL.md scripts references templates README.md README_EN.md LICENSE install.sh AGENTS.md; do
    src="$SCRIPT_DIR/$item"
    dst="$DEST/$item"
    rm -rf "$dst"
    if [[ -d "$src" ]]; then
      cp -R "$src" "$dst"
    else
      cp "$src" "$dst"
    fi
  done

  find "$DEST" -type d -name "__pycache__" -prune -exec rm -rf {} + 2>/dev/null || true
  find "$DEST" -name ".DS_Store" -delete 2>/dev/null || true

  echo "Installed global Codex skill bundle to: $DEST"
  echo "Next: restart Codex or refresh the client if it caches the skill index."
  exit 0
fi

DEST="${TARGET:-$(pwd)}"
AGENTS_DEST="$DEST/AGENTS.md"
CODEX_DIR="$DEST/.codex"
AUTOMATION_DIR="$CODEX_DIR/automation"
AGENT_DIR="$CODEX_DIR/agents"
SKILL_DIR="$CODEX_DIR/skills"
DEV_DIR="$DEST/dev"

if [[ "$YES" != true ]]; then
  echo "Bootstrap Codex maintainer files into: $DEST"
  read -r -p "Continue? [y/N] " REPLY
  [[ "$REPLY" =~ ^[Yy]$ ]] || exit 1
fi

mkdir -p "$AUTOMATION_DIR" "$AGENT_DIR" "$SKILL_DIR" "$DEV_DIR/active" "$DEV_DIR/archive"

copy_file() {
  local src="$1"
  local dst="$2"

  if [[ -e "$dst" && "$FORCE" != true ]]; then
    echo "Skip existing: $dst"
    return
  fi

  rm -rf "$dst"
  if [[ -d "$src" ]]; then
    cp -R "$src" "$dst"
  else
    cp "$src" "$dst"
  fi
  echo "Installed: $dst"
}

copy_file "$SCRIPT_DIR/templates/AGENTS.md" "$AGENTS_DEST"
copy_file "$SCRIPT_DIR/templates/automation/." "$AUTOMATION_DIR"
copy_file "$SCRIPT_DIR/templates/agents/." "$AGENT_DIR"
copy_file "$SCRIPT_DIR/templates/skill-rules.json" "$SKILL_DIR/skill-rules.json"
copy_file "$SCRIPT_DIR/templates/dev-docs/." "$DEV_DIR"

chmod +x "$AUTOMATION_DIR"/*.sh 2>/dev/null || true

cat <<DONE
Bootstrap complete.

Created/updated:
- $AGENTS_DEST
- $AUTOMATION_DIR
- $AGENT_DIR
- $SKILL_DIR/skill-rules.json
- $DEV_DIR

Recommended next steps:
1. Edit AGENTS.md to reflect the real repo map and validation commands.
2. Tailor .codex/automation/suggest-checks.py for your toolchain.
3. Move recurring maintainer prompts into ~/.codex/skills or repo-local drafts.
DONE
