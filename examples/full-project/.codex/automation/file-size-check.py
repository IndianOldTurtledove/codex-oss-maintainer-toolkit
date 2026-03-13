#!/usr/bin/env python3
"""Warn when files exceed a configurable line limit."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

SUGGESTIONS = {
    ".py": ["Extract helper functions", "Move constants to a dedicated module", "Split services from transport code"],
    ".ts": ["Move types into a separate file", "Split utility functions", "Break large feature modules apart"],
    ".tsx": ["Split into smaller components", "Move hooks into dedicated files"],
    ".vue": ["Split components", "Move composables and styles out of the view file"],
}


def changed_files() -> list[str]:
    result = subprocess.run(["git", "diff", "--name-only"], capture_output=True, text=True, check=False)
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def count_lines(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").splitlines())


def main() -> int:
    parser = argparse.ArgumentParser(description="Check file sizes by line count")
    parser.add_argument("files", nargs="*", help="Files to inspect")
    parser.add_argument("--changed", action="store_true", help="Use files from git diff")
    parser.add_argument("--limit", type=int, default=500, help="Line limit (default: 500)")
    args = parser.parse_args()

    targets = args.files or (changed_files() if args.changed else [])
    if not targets:
        print("No files provided.")
        return 1

    had_warning = False
    for file_name in targets:
        path = Path(file_name)
        if not path.exists() or not path.is_file():
            continue
        line_count = count_lines(path)
        if line_count <= args.limit:
            continue
        had_warning = True
        ext = path.suffix.lower()
        print(f"{path}: {line_count} lines (limit {args.limit})")
        for suggestion in SUGGESTIONS.get(ext, ["Consider splitting the file into smaller modules"]):
            print(f"- {suggestion}")
        print()

    if not had_warning:
        print("No oversized files detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
