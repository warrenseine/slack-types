#!/bin/bash

set -xe

[[ "$npm_package_name" == "slack-types" ]] || {
    >&2 echo "error: run with npm (npm run build)"
    exit 1
}

./scripts/generate-ts-app-backend-types.rb
./scripts/generate-ts-events-api-types.rb
./scripts/generate-ts-rtm-api-types.rb
./scripts/generate-ts-audit-api-types.rb
./scripts/generate-ts-scim-api-types.rb
./scripts/generate-ts-web-api-types.rb
