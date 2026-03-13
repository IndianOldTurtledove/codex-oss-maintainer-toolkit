#!/usr/bin/env python3
"""Package a skill directory into a shareable ZIP archive."""

from __future__ import annotations

import os
import sys
import zipfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))
from quick_validate import validate_skill


def package_skill(skill_path: str, output_dir: str | None = None) -> Path | None:
    path = Path(skill_path).expanduser()
    if not path.exists() or not path.is_dir():
        print(f"Error: skill directory not found: {skill_path}")
        return None

    print(f"Validating {skill_path}...")
    is_valid, errors = validate_skill(str(path))
    if not is_valid:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return None

    output_path = Path(output_dir).expanduser() if output_dir else Path(".")
    output_path.mkdir(parents=True, exist_ok=True)
    archive_path = output_path / f"{path.name}.zip"

    print(f"Creating {archive_path}...")
    try:
        with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zf:
            for root_dir, dirs, files in os.walk(path):
                dirs[:] = [d for d in dirs if not d.startswith(".") and d != "__pycache__"]
                for file_name in files:
                    if file_name.startswith("."):
                        continue
                    file_path = Path(root_dir) / file_name
                    zf.write(file_path, file_path.relative_to(path))
        print(f"Package created: {archive_path}")
        return archive_path
    except Exception as exc:
        print(f"Error creating package: {exc}")
        return None


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: package_skill.py <skill-path> [output-directory]")
        return 1

    result = package_skill(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
