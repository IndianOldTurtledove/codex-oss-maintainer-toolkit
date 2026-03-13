#!/usr/bin/env python3
"""Quick validation for Codex skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ALLOWED_PROPERTIES = {"name", "description", "license", "allowed-tools", "metadata"}
NAME_PATTERN = re.compile(r"^[a-z0-9]([a-z0-9-]*[a-z0-9])?$")
MAX_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024
MAX_SKILL_LINES = 500


def validate_skill(skill_path: str) -> tuple[bool, list[str]]:
    errors: list[str] = []
    path = Path(skill_path).expanduser()

    if not path.exists():
        return False, [f"Path does not exist: {skill_path}"]
    if not path.is_dir():
        return False, [f"Path is not a directory: {skill_path}"]

    skill_md = path / "SKILL.md"
    if not skill_md.exists():
        return False, ["SKILL.md not found"]

    content = skill_md.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return False, ["Missing YAML frontmatter (file must start with ---)"]

    parts = content.split("---", 2)
    if len(parts) < 3:
        return False, ["Invalid frontmatter format (must be enclosed in ---)"]

    frontmatter_text = parts[1].strip()
    body = parts[2]
    frontmatter: dict[str, str] = {}

    for line in frontmatter_text.splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip()

    name = frontmatter.get("name")
    if not name:
        errors.append("Missing required field: name")
    else:
        if not NAME_PATTERN.match(name):
            errors.append(f"Invalid name format: {name}")
        elif len(name) > MAX_NAME_LENGTH:
            errors.append(f"name too long: {len(name)} > {MAX_NAME_LENGTH}")
        elif "--" in name:
            errors.append("name cannot contain consecutive hyphens")

    description = frontmatter.get("description")
    if not description:
        errors.append("Missing required field: description")
    else:
        if len(description) > MAX_DESCRIPTION_LENGTH:
            errors.append(f"description too long: {len(description)} > {MAX_DESCRIPTION_LENGTH}")
        if "<" in description and ">" in description:
            errors.append("description cannot contain angle brackets")

    unknown = set(frontmatter) - ALLOWED_PROPERTIES
    if unknown:
        errors.append(f"Unknown frontmatter properties: {sorted(unknown)}")

    line_count = len(body.strip().splitlines())
    if line_count > MAX_SKILL_LINES:
        errors.append(f"SKILL.md body too long: {line_count} > {MAX_SKILL_LINES} lines")

    windows_path_pattern = re.compile(r"[A-Za-z]:\\|\\[a-zA-Z0-9_-]+\.[a-zA-Z]+")
    if windows_path_pattern.search(content):
        errors.append("Contains Windows-style paths (use / instead)")

    return len(errors) == 0, errors


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: quick_validate.py <skill-directory>")
        return 1

    is_valid, errors = validate_skill(sys.argv[1])
    if is_valid:
        print(f"Skill '{sys.argv[1]}' is valid")
        return 0

    print(f"Skill '{sys.argv[1]}' has errors:")
    for error in errors:
        print(f"  - {error}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
