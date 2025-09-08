#!/bin/bash

# Find the root path of the git repository
ROOT_PATH=$(git rev-parse --show-toplevel 2>/dev/null)

# If not in a git repo, fallback to script directory
if [ -z "$ROOT_PATH" ]; then
    ROOT_PATH="$(cd "$(dirname "$0")/.." && pwd)"
fi

# Export the variable
export ROOT_PATH

# Print the root path
echo "ROOT_PATH=$ROOT_PATH"

$ROOT_PATH/.venv/bin/pip install -r $ROOT_PATH/requirements.txt

