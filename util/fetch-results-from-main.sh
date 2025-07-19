#!/bin/bash

set -e

cd "$(dirname "$0")"

if ! command -v gh >/dev/null 2>&1; then
    echo "Error: gh (GitHub CLI) is not installed. Please see https://github.com/cli/cli#installation" >&2
    exit 1
fi

run_id="$(gh run list --repo uutils/coreutils --workflow GnuTests.yml --branch main --event push --status completed --limit 1 --json databaseId --jq '.[0].databaseId')"

if [[ -z "$run_id" ]]; then
    echo "Failed to get latest run ID from main branch." >&2
    exit 1
fi

rm -f aggregated-result.json

gh run download "$run_id" --repo uutils/coreutils -n aggregated-result
