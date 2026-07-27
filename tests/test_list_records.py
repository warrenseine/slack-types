"""Validate Slack List record cells against real-shape payloads.

``conversations.history`` / ``conversations.replies`` unfurl Slack Lists as
``messages[].attachments[].list_records[]``. The upstream java-slack-sdk samples
only ever captured string cell values and a single linked message, but real
responses put a ``bool`` in checkbox columns, an epoch ``int`` in date columns,
and a *list* of linked messages in message columns — which used to abort the
whole history page with a ValidationError.

The fixtures live under ``tests/fixtures/`` rather than ``samples/`` on purpose:
``samples/`` is fed to genson during codegen, where this payload would invent a
throwaway ``MessageItem`` class and narrow ``user: List[Any]`` to ``List[str]``.
The widening is owned by the hardening pass in ``scripts/build.py`` instead.
"""

import json
from pathlib import Path

import pytest
from pydantic import BaseModel, ValidationError

from slack_types.web_api.conversations_history_response import (
    ConversationsHistoryResponse,
)
from slack_types.web_api.conversations_replies_response import (
    ConversationsRepliesResponse,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"

CASES: list[tuple[str, type[BaseModel]]] = [
    (
        "web-api/conversations.history/list_record_typed_fields.json",
        ConversationsHistoryResponse,
    ),
    (
        "web-api/conversations.replies/list_record_typed_fields.json",
        ConversationsRepliesResponse,
    ),
]


def _load(fixture: str) -> dict:
    return json.loads((FIXTURES / fixture).read_text())


@pytest.mark.parametrize(("fixture", "model"), CASES)
def test_typed_cell_values_validate(fixture: str, model: type[BaseModel]) -> None:
    records = _load(fixture)
    parsed = model.model_validate(records)
    fields = parsed.messages[0].attachments[0].list_records[0].fields

    assert fields[0].value == "Acme onboarding"
    # A checkbox column stays a bool rather than being coerced to "False".
    assert fields[3].value is False
    # Date columns arrive as epoch seconds and must not become strings.
    assert fields[4].value == 1754485178
    assert isinstance(fields[4].value, int) and not isinstance(fields[4].value, bool)


@pytest.mark.parametrize(("fixture", "model"), CASES)
def test_cell_message_accepts_list_and_object(
    fixture: str, model: type[BaseModel]
) -> None:
    parsed = model.model_validate(_load(fixture))
    records = parsed.messages[0].attachments[0].list_records

    listed = records[0].fields[1].message
    assert isinstance(listed, list)
    assert listed[0].ts == "1747252047.403059"

    # The single-object form the samples captured must still parse.
    single = records[1].fields[1].message
    assert not isinstance(single, list)
    assert single.ts == "1747331176.884219"


@pytest.mark.parametrize(("fixture", "model"), CASES)
def test_cells_still_reject_garbage(fixture: str, model: type[BaseModel]) -> None:
    records = _load(fixture)
    records["messages"][0]["attachments"][0]["list_records"][0]["fields"][0]["value"] = {
        "nested": "object"
    }
    with pytest.raises(ValidationError):
        model.model_validate(records)
