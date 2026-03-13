#!/usr/bin/env python3
"""Suggest local skills for a maintainer task prompt."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

PRIORITY_WEIGHT = {"critical": 4, "high": 3, "medium": 2, "low": 1}


def read_prompt(prompt_parts: list[str]) -> str:
    if prompt_parts:
        return " ".join(prompt_parts).strip()
    return sys.stdin.read().strip()


def find_rules(explicit: str | None) -> Path | None:
    if explicit:
        candidate = Path(explicit).expanduser()
        return candidate if candidate.exists() else None

    candidates = [
        Path.cwd() / ".codex" / "skills" / "skill-rules.json",
        Path.cwd() / "skill-rules.json",
        Path.cwd() / "templates" / "skill-rules.json",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def load_rules(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def matches_prompt(prompt: str, triggers: dict[str, Any]) -> bool:
    prompt_lower = prompt.lower()
    prompt_triggers = triggers.get("promptTriggers", {})

    for keyword in prompt_triggers.get("keywords", []):
        if keyword.lower() in prompt_lower:
            return True

    for pattern in prompt_triggers.get("intentPatterns", []):
        try:
            if re.search(pattern, prompt, re.IGNORECASE):
                return True
        except re.error:
            continue

    return False


def matches_files(files: list[str], triggers: dict[str, Any]) -> bool:
    if not files:
        return False
    include = triggers.get("fileTriggers", {}).get("include", [])
    return any(pattern.strip("*") in file_path for pattern in include for file_path in files)


def main() -> int:
    parser = argparse.ArgumentParser(description="Suggest local maintainer skills for a prompt")
    parser.add_argument("prompt", nargs="*", help="Prompt to analyze. If omitted, stdin is used.")
    parser.add_argument("--rules", help="Path to skill-rules.json")
    parser.add_argument("--files", nargs="*", default=[], help="Optional changed file list")
    args = parser.parse_args()

    prompt = read_prompt(args.prompt)
    if not prompt:
        print("No prompt provided.")
        return 1

    rules_path = find_rules(args.rules)
    if not rules_path:
        print("No skill-rules.json found.")
        return 1

    rules = load_rules(rules_path)
    matches: list[tuple[str, dict[str, Any]]] = []
    for skill_name, rule in rules.get("skills", {}).items():
        triggers = rule.get("triggers", {})
        if matches_prompt(prompt, triggers) or matches_files(args.files, triggers):
            matches.append((skill_name, rule))

    matches.sort(key=lambda item: PRIORITY_WEIGHT.get(item[1].get("priority", "low"), 0), reverse=True)

    if not matches:
        print("No suggested skills.")
        return 0

    print("# Suggested Skills")
    print(f"Rules file: {rules_path}")
    print()
    for skill_name, rule in matches:
        priority = rule.get("priority", "low")
        enforcement = rule.get("enforcement", "suggest")
        print(f"- {skill_name} ({priority}, {enforcement})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
