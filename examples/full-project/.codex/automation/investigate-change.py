#!/usr/bin/env python3
"""Generate a pre-edit investigation checklist for changed files."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def changed_files() -> list[str]:
    result = subprocess.run(["git", "diff", "--name-only"], capture_output=True, text=True, check=False)
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Create an investigation checklist before editing code")
    parser.add_argument("files", nargs="*", help="Files to investigate")
    parser.add_argument("--changed", action="store_true", help="Use files from git diff")
    args = parser.parse_args()

    targets = args.files or (changed_files() if args.changed else [])
    if not targets:
        print("No files provided.")
        return 1

    print("# Investigation Checklist")
    for file_path in targets:
        base_name = Path(file_path).stem
        print()
        print(f"## {file_path}")
        print(f"- Read the file: sed -n '1,200p' {file_path}")
        print(f"- Inspect recent changes: git diff -- {file_path}")
        print(f"- Search references: rg -n \"{base_name}\" .")
        print(f"- Look for related tests: rg -n \"{base_name}\" tests src")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
