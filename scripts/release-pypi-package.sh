#!/bin/bash

set -e

[[ "$npm_package_name" == "slack-types" ]] || {
    >&2 echo "error: run with npm (npm run release)"
    exit 1
}

rm -rf dist/
uv build
uv publish
