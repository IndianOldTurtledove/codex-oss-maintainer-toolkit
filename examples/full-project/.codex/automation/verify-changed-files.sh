#!/bin/bash
set -euo pipefail

mapfile -t FILES < <((git diff --name-only; git diff --cached --name-only) | sort -u | sed '/^$/d')

if [[ ${#FILES[@]} -eq 0 ]]; then
  echo "No changed files detected."
  exit 0
fi

for file in "${FILES[@]}"; do
  [[ -f "$file" ]] || continue
  case "$file" in
    *.py)
      python3 -m py_compile "$file"
      ;;
    *.json)
      python3 -m json.tool "$file" > /dev/null
      ;;
    *.sh)
      bash -n "$file"
      ;;
  esac
done

echo "Basic changed-file verification passed."
