# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = mpim_open_response_from_dict(json.loads(json_string))

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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class Icons:
    image_36: Optional[str] = None
    image_48: Optional[str] = None
    image_72: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Icons':
        assert isinstance(obj, dict)
        image_36 = from_union([from_str, from_none], obj.get("image_36"))
        image_48 = from_union([from_str, from_none], obj.get("image_48"))
        image_72 = from_union([from_str, from_none], obj.get("image_72"))
        return Icons(image_36, image_48, image_72)

    def to_dict(self) -> dict:
        result: dict = {}
        result["image_36"] = from_union([from_str, from_none], self.image_36)
        result["image_48"] = from_union([from_str, from_none], self.image_48)
        result["image_72"] = from_union([from_str, from_none], self.image_72)
        return result


@dataclass
class BotProfile:
    id: Optional[str] = None
    deleted: Optional[bool] = None
    name: Optional[str] = None
    updated: Optional[int] = None
    app_id: Optional[str] = None
    icons: Optional[Icons] = None
    team_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BotProfile':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        deleted = from_union([from_bool, from_none], obj.get("deleted"))
        name = from_union([from_str, from_none], obj.get("name"))
        updated = from_union([from_int, from_none], obj.get("updated"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        icons = from_union([Icons.from_dict, from_none], obj.get("icons"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        return BotProfile(id, deleted, name, updated, app_id, icons, team_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["deleted"] = from_union([from_bool, from_none], self.deleted)
        result["name"] = from_union([from_str, from_none], self.name)
        result["updated"] = from_union([from_int, from_none], self.updated)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["icons"] = from_union([lambda x: to_class(Icons, x), from_none], self.icons)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        return result


@dataclass
class Latest:
    bot_id: Optional[str] = None
    type: Optional[str] = None
    text: Optional[str] = None
    user: Optional[str] = None
    ts: Optional[str] = None
    team: Optional[str] = None
    bot_profile: Optional[BotProfile] = None
    thread_ts: Optional[str] = None
    parent_user_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Latest':
        assert isinstance(obj, dict)
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        type = from_union([from_str, from_none], obj.get("type"))
        text = from_union([from_str, from_none], obj.get("text"))
        user = from_union([from_str, from_none], obj.get("user"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        team = from_union([from_str, from_none], obj.get("team"))
        bot_profile = from_union([BotProfile.from_dict, from_none], obj.get("bot_profile"))
        thread_ts = from_union([from_str, from_none], obj.get("thread_ts"))
        parent_user_id = from_union([from_str, from_none], obj.get("parent_user_id"))
        return Latest(bot_id, type, text, user, ts, team, bot_profile, thread_ts, parent_user_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["type"] = from_union([from_str, from_none], self.type)
        result["text"] = from_union([from_str, from_none], self.text)
        result["user"] = from_union([from_str, from_none], self.user)
        result["ts"] = from_union([from_str, from_none], self.ts)
        result["team"] = from_union([from_str, from_none], self.team)
        result["bot_profile"] = from_union([lambda x: to_class(BotProfile, x), from_none], self.bot_profile)
        result["thread_ts"] = from_union([from_str, from_none], self.thread_ts)
        result["parent_user_id"] = from_union([from_str, from_none], self.parent_user_id)
        return result


@dataclass
class Purpose:
    value: Optional[str] = None
    creator: Optional[str] = None
    last_set: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Purpose':
        assert isinstance(obj, dict)
        value = from_union([from_str, from_none], obj.get("value"))
        creator = from_union([from_str, from_none], obj.get("creator"))
        last_set = from_union([from_int, from_none], obj.get("last_set"))
        return Purpose(value, creator, last_set)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_union([from_str, from_none], self.value)
        result["creator"] = from_union([from_str, from_none], self.creator)
        result["last_set"] = from_union([from_int, from_none], self.last_set)
        return result


@dataclass
class Group:
    id: Optional[str] = None
    name: Optional[str] = None
    is_group: Optional[bool] = None
    created: Optional[int] = None
    creator: Optional[str] = None
    is_archived: Optional[bool] = None
    name_normalized: Optional[str] = None
    is_mpim: Optional[bool] = None
    is_open: Optional[bool] = None
    last_read: Optional[str] = None
    latest: Optional[Latest] = None
    unread_count: Optional[int] = None
    unread_count_display: Optional[int] = None
    members: Optional[List[str]] = None
    topic: Optional[Purpose] = None
    purpose: Optional[Purpose] = None
    priority: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Group':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        is_group = from_union([from_bool, from_none], obj.get("is_group"))
        created = from_union([from_int, from_none], obj.get("created"))
        creator = from_union([from_str, from_none], obj.get("creator"))
        is_archived = from_union([from_bool, from_none], obj.get("is_archived"))
        name_normalized = from_union([from_str, from_none], obj.get("name_normalized"))
        is_mpim = from_union([from_bool, from_none], obj.get("is_mpim"))
        is_open = from_union([from_bool, from_none], obj.get("is_open"))
        last_read = from_union([from_str, from_none], obj.get("last_read"))
        latest = from_union([Latest.from_dict, from_none], obj.get("latest"))
        unread_count = from_union([from_int, from_none], obj.get("unread_count"))
        unread_count_display = from_union([from_int, from_none], obj.get("unread_count_display"))
        members = from_union([lambda x: from_list(from_str, x), from_none], obj.get("members"))
        topic = from_union([Purpose.from_dict, from_none], obj.get("topic"))
        purpose = from_union([Purpose.from_dict, from_none], obj.get("purpose"))
        priority = from_union([from_int, from_none], obj.get("priority"))
        return Group(id, name, is_group, created, creator, is_archived, name_normalized, is_mpim, is_open, last_read, latest, unread_count, unread_count_display, members, topic, purpose, priority)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["is_group"] = from_union([from_bool, from_none], self.is_group)
        result["created"] = from_union([from_int, from_none], self.created)
        result["creator"] = from_union([from_str, from_none], self.creator)
        result["is_archived"] = from_union([from_bool, from_none], self.is_archived)
        result["name_normalized"] = from_union([from_str, from_none], self.name_normalized)
        result["is_mpim"] = from_union([from_bool, from_none], self.is_mpim)
        result["is_open"] = from_union([from_bool, from_none], self.is_open)
        result["last_read"] = from_union([from_str, from_none], self.last_read)
        result["latest"] = from_union([lambda x: to_class(Latest, x), from_none], self.latest)
        result["unread_count"] = from_union([from_int, from_none], self.unread_count)
        result["unread_count_display"] = from_union([from_int, from_none], self.unread_count_display)
        result["members"] = from_union([lambda x: from_list(from_str, x), from_none], self.members)
        result["topic"] = from_union([lambda x: to_class(Purpose, x), from_none], self.topic)
        result["purpose"] = from_union([lambda x: to_class(Purpose, x), from_none], self.purpose)
        result["priority"] = from_union([from_int, from_none], self.priority)
        return result


@dataclass
class ResponseMetadata:
    messages: Optional[List[str]] = None
    warnings: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseMetadata':
        assert isinstance(obj, dict)
        messages = from_union([lambda x: from_list(from_str, x), from_none], obj.get("messages"))
        warnings = from_union([lambda x: from_list(from_str, x), from_none], obj.get("warnings"))
        return ResponseMetadata(messages, warnings)

    def to_dict(self) -> dict:
        result: dict = {}
        result["messages"] = from_union([lambda x: from_list(from_str, x), from_none], self.messages)
        result["warnings"] = from_union([lambda x: from_list(from_str, x), from_none], self.warnings)
        return result


@dataclass
class MpimOpenResponse:
    ok: Optional[bool] = None
    group: Optional[Group] = None
    warning: Optional[str] = None
    response_metadata: Optional[ResponseMetadata] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MpimOpenResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        group = from_union([Group.from_dict, from_none], obj.get("group"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return MpimOpenResponse(ok, group, warning, response_metadata, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["group"] = from_union([lambda x: to_class(Group, x), from_none], self.group)
        result["warning"] = from_union([from_str, from_none], self.warning)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def mpim_open_response_from_dict(s: Any) -> MpimOpenResponse:
    return MpimOpenResponse.from_dict(s)


def mpim_open_response_to_dict(x: MpimOpenResponse) -> Any:
    return to_class(MpimOpenResponse, x)