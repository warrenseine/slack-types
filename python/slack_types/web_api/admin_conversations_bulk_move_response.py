# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_conversations_bulk_move_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, List, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class NotAdded:
    channel_id: Optional[str] = None
    errors: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'NotAdded':
        assert isinstance(obj, dict)
        channel_id = from_union([from_str, from_none], obj.get("channel_id"))
        errors = from_union([lambda x: from_list(from_str, x), from_none], obj.get("errors"))
        return NotAdded(channel_id, errors)

    def to_dict(self) -> dict:
        result: dict = {}
        result["channel_id"] = from_union([from_str, from_none], self.channel_id)
        result["errors"] = from_union([lambda x: from_list(from_str, x), from_none], self.errors)
        return result


@dataclass
class ResponseMetadata:
    messages: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseMetadata':
        assert isinstance(obj, dict)
        messages = from_union([lambda x: from_list(from_str, x), from_none], obj.get("messages"))
        return ResponseMetadata(messages)

    def to_dict(self) -> dict:
        result: dict = {}
        result["messages"] = from_union([lambda x: from_list(from_str, x), from_none], self.messages)
        return result


@dataclass
class AdminConversationsBulkMoveResponse:
    ok: Optional[bool] = None
    bulk_action_id: Optional[str] = None
    not_added: Optional[List[NotAdded]] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    response_metadata: Optional[ResponseMetadata] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminConversationsBulkMoveResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        bulk_action_id = from_union([from_str, from_none], obj.get("bulk_action_id"))
        not_added = from_union([lambda x: from_list(NotAdded.from_dict, x), from_none], obj.get("not_added"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return AdminConversationsBulkMoveResponse(ok, bulk_action_id, not_added, error, needed, provided, response_metadata, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["bulk_action_id"] = from_union([from_str, from_none], self.bulk_action_id)
        result["not_added"] = from_union([lambda x: from_list(lambda x: to_class(NotAdded, x), x), from_none], self.not_added)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def admin_conversations_bulk_move_response_from_dict(s: Any) -> AdminConversationsBulkMoveResponse:
    return AdminConversationsBulkMoveResponse.from_dict(s)


def admin_conversations_bulk_move_response_to_dict(x: AdminConversationsBulkMoveResponse) -> Any:
    return to_class(AdminConversationsBulkMoveResponse, x)
