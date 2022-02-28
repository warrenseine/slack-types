#!/bin/bash

set -xe

[[ "$npm_package_name" == "slack-types" ]] || {
    >&2 echo "error: run with npm (npm run build)"
    exit 1
}

./scripts/generate-py-app-backend-types.rb
./scripts/generate-py-events-api-types.rb
./scripts/generate-py-rtm-api-types.rb
./scripts/generate-py-audit-api-types.rb
./scripts/generate-py-scim-api-types.rb
./scripts/generate-py-web-api-types.rb

find python/slack_types -type d -exec touch "{}/__init__.py" ';'
