# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = canvases_create_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, List, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


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
class CanvasesCreateResponse:
    ok: Optional[bool] = None
    canvas_id: Optional[str] = None
    detail: Optional[str] = None
    error: Optional[str] = None
    response_metadata: Optional[ResponseMetadata] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CanvasesCreateResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        canvas_id = from_union([from_str, from_none], obj.get("canvas_id"))
        detail = from_union([from_str, from_none], obj.get("detail"))
        error = from_union([from_str, from_none], obj.get("error"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return CanvasesCreateResponse(ok, canvas_id, detail, error, response_metadata, needed, provided, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["canvas_id"] = from_union([from_str, from_none], self.canvas_id)
        result["detail"] = from_union([from_str, from_none], self.detail)
        result["error"] = from_union([from_str, from_none], self.error)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def canvases_create_response_from_dict(s: Any) -> CanvasesCreateResponse:
    return CanvasesCreateResponse.from_dict(s)


def canvases_create_response_to_dict(x: CanvasesCreateResponse) -> Any:
    return to_class(CanvasesCreateResponse, x)
