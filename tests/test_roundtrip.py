"""Validate generated Pydantic models against the JSON samples they were generated from."""

import json
from pathlib import Path

import pytest
from pydantic import BaseModel

from slack_types.app_backend.interactive_components.block_action_payload import (
    BlockActionPayload,
)
from slack_types.app_backend.slash_commands.slash_command_payload import (
    SlashCommandPayload,
)
from slack_types.events_api.app_mention_payload import AppMentionPayload
from slack_types.events_api.message_payload import MessagePayload
from slack_types.scim_api.v1.users_response import UsersResponse as UsersResponseV1
from slack_types.scim_api.v2.resource_types_response import ResourceTypesResponse
from slack_types.scim_api.v2.users_response import UsersResponse as UsersResponseV2
from slack_types.web_api.conversations_history_response import (
    ConversationsHistoryResponse,
)
from slack_types.web_api.conversations_list_response import ConversationsListResponse
from slack_types.web_api.conversations_replies_response import (
    ConversationsRepliesResponse,
)
from slack_types.web_api.team_info_response import TeamInfoResponse

REPO_ROOT = Path(__file__).resolve().parent.parent
JSON_ROOT = REPO_ROOT / "json"


ROUND_TRIP_CASES: list[tuple[str, type[BaseModel]]] = [
    # Web API methods used by pearl's SlackMessagingProvider.
    ("web-api/team.info.json", TeamInfoResponse),
    ("web-api/conversations.list.json", ConversationsListResponse),
    ("web-api/conversations.history.json", ConversationsHistoryResponse),
    ("web-api/conversations.replies.json", ConversationsRepliesResponse),
    # Events API representative payloads.
    ("events-api/AppMentionPayload.json", AppMentionPayload),
    ("events-api/MessagePayload.json", MessagePayload),
    # App backend payloads.
    (
        "app-backend/interactive-components/BlockActionPayload.json",
        BlockActionPayload,
    ),
    ("app-backend/slash-commands/SlashCommandPayload.json", SlashCommandPayload),
    # SCIM v1 + v2.
    ("scim-api/v1/Users.json", UsersResponseV1),
    ("scim-api/v2/Users.json", UsersResponseV2),
    ("scim-api/v2/ResourceTypes.json", ResourceTypesResponse),
]


@pytest.mark.parametrize(("sample", "model"), ROUND_TRIP_CASES)
def test_sample_validates(sample: str, model: type[BaseModel]) -> None:
    data = json.loads((JSON_ROOT / sample).read_text())
    parsed = model.model_validate(data)
    assert isinstance(parsed, model)
