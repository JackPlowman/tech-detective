#!/bin/bash
set -e +x

# Check if there are any changes in the watched folder
if git diff --cached --name-only | grep -q "^detector/"; then
  just detector::install
  just detector::ruff-fix
fi
