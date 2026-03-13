#!/usr/bin/env python3
"""Suggest validation commands for changed files."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

CHECK_COMMANDS: dict[str, list[str]] = {
    ".py": ["ruff check {file}", "python3 -m py_compile {file}"],
    ".ts": ["pnpm eslint {file}", "pnpm tsc --noEmit"],
    ".tsx": ["pnpm eslint {file}", "pnpm tsc --noEmit"],
    ".js": ["pnpm eslint {file}"],
    ".jsx": ["pnpm eslint {file}"],
    ".vue": ["pnpm eslint {file}"],
    ".json": ["python3 -m json.tool {file} > /dev/null"],
    ".sh": ["bash -n {file}"],
    ".md": [],
}


def changed_files() -> list[str]:
    result = subprocess.run(["git", "diff", "--name-only"], capture_output=True, text=True, check=False)
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Suggest verification commands from file paths")
    parser.add_argument("files", nargs="*", help="Files to analyze")
    parser.add_argument("--changed", action="store_true", help="Use files from git diff")
    args = parser.parse_args()

    targets = args.files or (changed_files() if args.changed else [])
    if not targets:
        print("No files provided.")
        return 1

    suggestions: list[str] = []
    for file_path in targets:
        ext = Path(file_path).suffix.lower()
        for command in CHECK_COMMANDS.get(ext, []):
            rendered = command.format(file=file_path)
            if rendered not in suggestions:
                suggestions.append(rendered)

    if not suggestions:
        print("No specific checks suggested.")
        return 0

    print("# Suggested Checks")
    for command in suggestions:
        print(f"- {command}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
