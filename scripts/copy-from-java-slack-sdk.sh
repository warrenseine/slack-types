#!/bin/bash

set -xe

[[ "$npm_package_name" == "slack-types" ]] || {
    >&2 echo "error: run with npm (npm run build)"
    exit 1
}

test -f java-slack-sdk/pom.xml || git clone --depth 1 git@github.com:slackapi/java-slack-sdk.git

mkdir -p ./json/audit-api/ ./json/web-api/ ./json/events-api/ ./json/rtm-api/ ./json/scim-api/ ./json/app-backend/dialogs/ ./json/app-backend/interactive-components/ ./json/app-backend/slash-commands/ ./json/app-backend/views/

cp -a java-slack-sdk/json-logs/samples/audit/. ./json/audit-api/
cp -a java-slack-sdk/json-logs/samples/api/. ./json/web-api/
cp -a java-slack-sdk/json-logs/samples/events/. ./json/events-api/
cp -a java-slack-sdk/json-logs/samples/rtm/. ./json/rtm-api/
cp -a java-slack-sdk/json-logs/samples/scim/. ./json/scim-api/
cp -a java-slack-sdk/json-logs/samples/app-backend/dialogs/.  ./json/app-backend/dialogs/
cp -a java-slack-sdk/json-logs/samples/app-backend/interactive-components/. ./json/app-backend/interactive-components/
cp -a java-slack-sdk/json-logs/samples/app-backend/slash-commands/. ./json/app-backend/slash-commands/
cp -a java-slack-sdk/json-logs/samples/app-backend/views/. ./json/app-backend/views/

# Fix missing fields

json_file=json/app-backend/interactive-components/BlockActionPayload.json
jq '. + (.actions[0].selected_options = [.actions[0].selected_option])' $json_file > $json_file.tmp && mv $json_file.tmp $json_file
