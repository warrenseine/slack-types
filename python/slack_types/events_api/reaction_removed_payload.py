# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = reaction_removed_payload_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, cast, Callable


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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class Authorization:
    enterprise_id: Optional[str] = None
    team_id: Optional[str] = None
    user_id: Optional[str] = None
    is_bot: Optional[bool] = None
    is_enterprise_install: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Authorization':
        assert isinstance(obj, dict)
        enterprise_id = from_union([from_str, from_none], obj.get("enterprise_id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        is_bot = from_union([from_bool, from_none], obj.get("is_bot"))
        is_enterprise_install = from_union([from_bool, from_none], obj.get("is_enterprise_install"))
        return Authorization(enterprise_id, team_id, user_id, is_bot, is_enterprise_install)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enterprise_id"] = from_union([from_str, from_none], self.enterprise_id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["user_id"] = from_union([from_str, from_none], self.user_id)
        result["is_bot"] = from_union([from_bool, from_none], self.is_bot)
        result["is_enterprise_install"] = from_union([from_bool, from_none], self.is_enterprise_install)
        return result


@dataclass
class Item:
    type: Optional[str] = None
    channel: Optional[str] = None
    ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        return Item(type, channel, ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["ts"] = from_union([from_str, from_none], self.ts)
        return result


@dataclass
class Event:
    type: Optional[str] = None
    user: Optional[str] = None
    item: Optional[Item] = None
    reaction: Optional[str] = None
    item_user: Optional[str] = None
    event_ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Event':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        user = from_union([from_str, from_none], obj.get("user"))
        item = from_union([Item.from_dict, from_none], obj.get("item"))
        reaction = from_union([from_str, from_none], obj.get("reaction"))
        item_user = from_union([from_str, from_none], obj.get("item_user"))
        event_ts = from_union([from_str, from_none], obj.get("event_ts"))
        return Event(type, user, item, reaction, item_user, event_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["user"] = from_union([from_str, from_none], self.user)
        result["item"] = from_union([lambda x: to_class(Item, x), from_none], self.item)
        result["reaction"] = from_union([from_str, from_none], self.reaction)
        result["item_user"] = from_union([from_str, from_none], self.item_user)
        result["event_ts"] = from_union([from_str, from_none], self.event_ts)
        return result


@dataclass
class ReactionRemovedPayload:
    token: Optional[str] = None
    team_id: Optional[str] = None
    enterprise_id: Optional[str] = None
    api_app_id: Optional[str] = None
    event: Optional[Event] = None
    type: Optional[str] = None
    event_id: Optional[str] = None
    event_time: Optional[int] = None
    authorizations: Optional[List[Authorization]] = None
    is_ext_shared_channel: Optional[bool] = None
    event_context: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ReactionRemovedPayload':
        assert isinstance(obj, dict)
        token = from_union([from_str, from_none], obj.get("token"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        enterprise_id = from_union([from_str, from_none], obj.get("enterprise_id"))
        api_app_id = from_union([from_str, from_none], obj.get("api_app_id"))
        event = from_union([Event.from_dict, from_none], obj.get("event"))
        type = from_union([from_str, from_none], obj.get("type"))
        event_id = from_union([from_str, from_none], obj.get("event_id"))
        event_time = from_union([from_int, from_none], obj.get("event_time"))
        authorizations = from_union([lambda x: from_list(Authorization.from_dict, x), from_none], obj.get("authorizations"))
        is_ext_shared_channel = from_union([from_bool, from_none], obj.get("is_ext_shared_channel"))
        event_context = from_union([from_str, from_none], obj.get("event_context"))
        return ReactionRemovedPayload(token, team_id, enterprise_id, api_app_id, event, type, event_id, event_time, authorizations, is_ext_shared_channel, event_context)

    def to_dict(self) -> dict:
        result: dict = {}
        result["token"] = from_union([from_str, from_none], self.token)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["enterprise_id"] = from_union([from_str, from_none], self.enterprise_id)
        result["api_app_id"] = from_union([from_str, from_none], self.api_app_id)
        result["event"] = from_union([lambda x: to_class(Event, x), from_none], self.event)
        result["type"] = from_union([from_str, from_none], self.type)
        result["event_id"] = from_union([from_str, from_none], self.event_id)
        result["event_time"] = from_union([from_int, from_none], self.event_time)
        result["authorizations"] = from_union([lambda x: from_list(lambda x: to_class(Authorization, x), x), from_none], self.authorizations)
        result["is_ext_shared_channel"] = from_union([from_bool, from_none], self.is_ext_shared_channel)
        result["event_context"] = from_union([from_str, from_none], self.event_context)
        return result


def reaction_removed_payload_from_dict(s: Any) -> ReactionRemovedPayload:
    return ReactionRemovedPayload.from_dict(s)


def reaction_removed_payload_to_dict(x: ReactionRemovedPayload) -> Any:
    return to_class(ReactionRemovedPayload, x)