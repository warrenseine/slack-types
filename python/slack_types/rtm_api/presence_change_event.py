# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = presence_change_event_from_dict(json.loads(json_string))

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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class PresenceChangeEvent:
    type: Optional[str] = None
    user: Optional[str] = None
    users: Optional[List[str]] = None
    presence: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PresenceChangeEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        user = from_union([from_str, from_none], obj.get("user"))
        users = from_union([lambda x: from_list(from_str, x), from_none], obj.get("users"))
        presence = from_union([from_str, from_none], obj.get("presence"))
        return PresenceChangeEvent(type, user, users, presence)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["user"] = from_union([from_str, from_none], self.user)
        result["users"] = from_union([lambda x: from_list(from_str, x), from_none], self.users)
        result["presence"] = from_union([from_str, from_none], self.presence)
        return result


def presence_change_event_from_dict(s: Any) -> PresenceChangeEvent:
    return PresenceChangeEvent.from_dict(s)


def presence_change_event_to_dict(x: PresenceChangeEvent) -> Any:
    return to_class(PresenceChangeEvent, x)