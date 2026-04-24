# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = chat_start_stream_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class ChatStartStreamResponse:
    ok: Optional[bool] = None
    ts: Optional[str] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    channel: Optional[str] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ChatStartStreamResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return ChatStartStreamResponse(ok, ts, error, needed, provided, channel, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["ts"] = from_union([from_str, from_none], self.ts)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def chat_start_stream_response_from_dict(s: Any) -> ChatStartStreamResponse:
    return ChatStartStreamResponse.from_dict(s)


def chat_start_stream_response_to_dict(x: ChatStartStreamResponse) -> Any:
    return to_class(ChatStartStreamResponse, x)
