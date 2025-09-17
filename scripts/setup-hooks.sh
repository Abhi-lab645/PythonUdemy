#!/usr/bin/env bash
# Setup script for repository hooks. Run once per clone to enable versioned hooks.
set -euo pipefail
repo_root=$(git rev-parse --show-toplevel)
cd "$repo_root"

git config core.hooksPath .githooks
echo "core.hooksPath set to .githooks"
