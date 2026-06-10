"""Validate generated models against real-shape Slack payloads.

The upstream java-slack-sdk samples only ship the object form of Block Kit
``text``/``title`` fields. Real ``conversations.history`` /
``conversations.replies`` responses also ship raw strings in
``blocks[].elements[].text`` (rich_text_section) and ``blocks[].title``
(third-party app unfurls — Granola, Claude, etc.). These tests exercise the
supplementary fixtures under ``samples/`` to lock in the polymorphism."""

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

REPO_ROOT = Path(__file__).resolve().parent.parent
SAMPLES = REPO_ROOT / "samples"


CASES: list[tuple[str, type[BaseModel]]] = [
    ("web-api/conversations.history/granola_unfurl.json", ConversationsHistoryResponse),
    ("web-api/conversations.replies/granola_unfurl.json", ConversationsRepliesResponse),
]


@pytest.mark.parametrize(("sample", "model"), CASES)
def test_block_kit_string_payloads_validate(sample: str, model: type[BaseModel]) -> None:
    data = json.loads((SAMPLES / sample).read_text())
    parsed = model.model_validate(data)
    msg = parsed.messages[0]
    assert msg.blocks[0].elements[0].text == "*Sent using* <@U0APP2JJBP0>"
    assert msg.blocks[1].title == "Thinking completed"


ATTACHMENT_CASES: list[tuple[str, type[BaseModel]]] = [
    ("web-api/conversations.history/linear_unfurl.json", ConversationsHistoryResponse),
    ("web-api/conversations.replies/linear_unfurl.json", ConversationsRepliesResponse),
]


@pytest.mark.parametrize(("sample", "model"), ATTACHMENT_CASES)
def test_attachment_block_string_payloads_validate(sample: str, model: type[BaseModel]) -> None:
    data = json.loads((SAMPLES / sample).read_text())
    parsed = model.model_validate(data)
    elements = parsed.messages[0].attachments[0].blocks[0].elements
    assert elements[0].text == "*State*  Next"
    assert elements[1].text == "*Assignee*  Laurent Anadon"
    assert elements[2].text == "*Project*  Run 2026"


FILE_DIMENSION_CASES: list[tuple[str, type[BaseModel]]] = [
    ("web-api/conversations.history/file_dimensions.json", ConversationsHistoryResponse),
    ("web-api/conversations.replies/file_dimensions.json", ConversationsRepliesResponse),
]


@pytest.mark.parametrize(("sample", "model"), FILE_DIMENSION_CASES)
def test_attachment_file_int_dimensions_validate(sample: str, model: type[BaseModel]) -> None:
    data = json.loads((SAMPLES / sample).read_text())
    parsed = model.model_validate(data)
    attachment_file = parsed.messages[-1].attachments[0].files[0]
    assert attachment_file.thumb_360_w == 360
    assert attachment_file.thumb_1024_h == 373
    assert attachment_file.original_w == 2634


@pytest.mark.parametrize("model", [ConversationsHistoryResponse, ConversationsRepliesResponse])
def test_block_kit_object_payloads_still_validate(model: type[BaseModel]) -> None:
    payload = {
        "ok": True,
        "messages": [
            {
                "type": "message",
                "ts": "1700000000.000000",
                "user": "U1",
                "text": "x",
                "blocks": [
                    {
                        "type": "actions",
                        "block_id": "a",
                        "elements": [
                            {
                                "type": "button",
                                "text": {"type": "plain_text", "text": "Go", "emoji": True},
                            }
                        ],
                    },
                    {
                        "type": "section",
                        "block_id": "s",
                        "title": {"type": "plain_text", "text": "T", "emoji": True},
                    },
                ],
            }
        ],
    }
    parsed = model.model_validate(payload)
    elem_text = parsed.messages[0].blocks[0].elements[0].text
    assert getattr(elem_text, "text", None) == "Go"
    title_obj = parsed.messages[0].blocks[1].title
    assert getattr(title_obj, "text", None) == "T"


@pytest.mark.parametrize("model", [ConversationsHistoryResponse, ConversationsRepliesResponse])
def test_block_kit_still_rejects_garbage(model: type[BaseModel]) -> None:
    payload = {"ok": True, "messages": [{"blocks": [{"type": "section", "title": 12345}]}]}
    with pytest.raises(ValidationError):
        model.model_validate(payload)
