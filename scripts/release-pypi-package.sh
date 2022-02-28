#!/bin/bash

[[ "$npm_package_name" == "slack-types" ]] || {
    >&2 echo "error: run with pip (npm run release)"
    exit 1
}

python3 -m build
