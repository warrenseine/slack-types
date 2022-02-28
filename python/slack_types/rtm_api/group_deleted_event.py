# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = group_deleted_event_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast


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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class GroupDeletedEvent:
    type: Optional[str] = None
    channel: Optional[str] = None
    date_deleted: Optional[int] = None
    actor_id: Optional[str] = None
    event_ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'GroupDeletedEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        date_deleted = from_union([from_int, from_none], obj.get("date_deleted"))
        actor_id = from_union([from_str, from_none], obj.get("actor_id"))
        event_ts = from_union([from_str, from_none], obj.get("event_ts"))
        return GroupDeletedEvent(type, channel, date_deleted, actor_id, event_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["date_deleted"] = from_union([from_int, from_none], self.date_deleted)
        result["actor_id"] = from_union([from_str, from_none], self.actor_id)
        result["event_ts"] = from_union([from_str, from_none], self.event_ts)
        return result


def group_deleted_event_from_dict(s: Any) -> GroupDeletedEvent:
    return GroupDeletedEvent.from_dict(s)


def group_deleted_event_to_dict(x: GroupDeletedEvent) -> Any:
    return to_class(GroupDeletedEvent, x)
