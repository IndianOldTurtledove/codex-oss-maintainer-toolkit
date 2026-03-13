#!/usr/bin/env python3
"""Detect whether a prompt should enter a systematic debugging workflow."""

from __future__ import annotations

import argparse
import re
import sys

SIGNALS = {
    r"error|exception|traceback|stack trace": 4,
    r"TypeError|ValueError|KeyError|AttributeError|ImportError|RuntimeError": 5,
    r"failed|failure|crash|crashed": 4,
    r"line\s+\d+|\.py:\d+|\.ts:\d+|\.js:\d+": 4,
    r"报错|出错|异常|崩溃|失败|白屏|卡住": 4,
    r"bug|debug|broken|regression": 3,
    r"又|still|again|依然|还是": 2,
}
THRESHOLD = 6

CHECKLIST = """# Systematic Debugging Checklist

1. Reproduce the failure with an exact command or path.
2. Read the failing file and nearby callers before editing.
3. Compare against a known-working pattern.
4. Form one hypothesis and test the smallest change.
5. Re-run the failing command and at least one adjacent validation command.
"""


def read_prompt(prompt_parts: list[str]) -> str:
    if prompt_parts:
        return " ".join(prompt_parts).strip()
    return sys.stdin.read().strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Detect debugging tasks from a prompt")
    parser.add_argument("prompt", nargs="*", help="Prompt to analyze. If omitted, stdin is used.")
    parser.add_argument("--show-score", action="store_true", help="Print score and matched signals")
    args = parser.parse_args()

    prompt = read_prompt(args.prompt)
    if not prompt:
        print("No prompt provided.")
        return 1

    score = 0
    matched: list[str] = []
    for pattern, weight in SIGNALS.items():
        if re.search(pattern, prompt, re.IGNORECASE):
            score += weight
            matched.append(pattern)

    if args.show_score:
        print(f"Score: {score}")
        if matched:
            print("Matched:")
            for item in matched:
                print(f"- {item}")
        print()

    if score >= THRESHOLD:
        print(CHECKLIST)
    else:
        print("No debug workflow trigger.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
