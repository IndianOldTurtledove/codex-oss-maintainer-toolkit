#!/usr/bin/env python3
"""Initialize a new Codex skill from a lightweight template."""

from __future__ import annotations

import argparse
import re
import stat
from pathlib import Path

SKILL_TEMPLATE = """---
name: {name}
description: TODO: Describe what this skill does and when Codex should use it.
---

# {title}

Briefly explain the maintainer problem this skill solves.

## Quick Start

Provide the shortest useful workflow.

## Core Workflow

1. Audit the task.
2. Read the relevant files.
3. Apply the smallest safe change.
4. Run the validation command.

## References

List any reference files or scripts that should be loaded on demand.
"""

REFERENCE_TEMPLATE = """# {title} Reference

## Goal

Document the repeatable rules, edge cases, and command snippets for this skill.

## Inputs

- Prompt patterns
- Key files
- External tools or services

## Validation

- Command 1
- Command 2
"""

OPENAI_YAML_TEMPLATE = """display_name: {title}
short_description: TODO: Short human-facing summary.
default_prompt: Help me use the {title} workflow in this repository.
"""

EXAMPLE_SCRIPT = """#!/usr/bin/env python3
\"\"\"Example helper for the {title} skill.\"\"\"

from __future__ import annotations

import sys


def main() -> int:
    if len(sys.argv) < 2:
        print(\"Usage: example.py <input>\")
        return 1

    print(f\"Received: {{sys.argv[1]}}\")
    return 0


if __name__ == \"__main__\":
    raise SystemExit(main())
"""

NAME_PATTERN = re.compile(r"^[a-z0-9]([a-z0-9-]*[a-z0-9])?$")


def validate_name(name: str) -> bool:
    if not NAME_PATTERN.match(name):
        return False
    if len(name) > 64:
        return False
    if "--" in name:
        return False
    return True


def to_title(name: str) -> str:
    return " ".join(word.capitalize() for word in name.split("-"))


def init_skill(name: str, base_path: str = ".codex/skills") -> Path:
    skill_path = Path(base_path).expanduser() / name
    if skill_path.exists():
        raise SystemExit(f"Error: skill directory already exists: {skill_path}")

    title = to_title(name)
    (skill_path / "scripts").mkdir(parents=True)
    (skill_path / "references").mkdir()
    (skill_path / "agents").mkdir()

    (skill_path / "SKILL.md").write_text(SKILL_TEMPLATE.format(name=name, title=title), encoding="utf-8")
    (skill_path / "references" / "reference.md").write_text(REFERENCE_TEMPLATE.format(title=title), encoding="utf-8")
    (skill_path / "agents" / "openai.yaml").write_text(OPENAI_YAML_TEMPLATE.format(title=title), encoding="utf-8")

    script_path = skill_path / "scripts" / "example.py"
    script_path.write_text(EXAMPLE_SCRIPT.format(title=title), encoding="utf-8")
    script_path.chmod(script_path.stat().st_mode | stat.S_IXUSR)
    return skill_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a new Codex skill")
    parser.add_argument("name", help="Skill name in hyphen-case, e.g. issue-triage")
    parser.add_argument("--path", default=".codex/skills", help="Base path for skill drafts (default: .codex/skills)")
    args = parser.parse_args()

    if not validate_name(args.name):
        print(f"Error: invalid skill name '{args.name}'")
        print("Requirements:")
        print("  - lowercase letters, digits, and hyphens only")
        print("  - max 64 characters")
        print("  - no leading or trailing hyphens")
        print("  - no consecutive hyphens")
        return 1

    skill_path = init_skill(args.name, args.path)
    print(f"Initialized skill: {skill_path}")
    print("Next steps:")
    print(f"  1. Edit {skill_path / 'SKILL.md'}")
    print(f"  2. Fill {skill_path / 'agents' / 'openai.yaml'}")
    print("  3. Add scripts or references as needed")
    print(f"  4. Validate: python3 scripts/quick_validate.py {skill_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
