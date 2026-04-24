# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = actions_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Dict, List, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


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
class ActionsResponse:
    actions: Optional[Dict[str, List[str]]] = None
    ok: Optional[bool] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ActionsResponse':
        assert isinstance(obj, dict)
        actions = from_union([lambda x: from_dict(lambda x: from_list(from_str, x), x), from_none], obj.get("actions"))
        ok = from_union([from_bool, from_none], obj.get("ok"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return ActionsResponse(actions, ok, error, needed, provided, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["actions"] = from_union([lambda x: from_dict(lambda x: from_list(from_str, x), x), from_none], self.actions)
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def actions_response_from_dict(s: Any) -> ActionsResponse:
    return ActionsResponse.from_dict(s)


def actions_response_to_dict(x: ActionsResponse) -> Any:
    return to_class(ActionsResponse, x)
