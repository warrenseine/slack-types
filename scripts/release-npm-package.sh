#!/bin/bash

[[ "$npm_package_name" == "slack-types" ]] || {
    >&2 echo "error: run with npm (npm run release)"
    exit 1
}

npm install
npm run build
dirs=$(ls typescript)
mv typescript/* .
npm publish
mv $dirs typescript
