# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = file_change_payload_from_dict(json.loads(json_string))

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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


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
class File:
    id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'File':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        return File(id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        return result


@dataclass
class Event:
    type: Optional[str] = None
    file_id: Optional[str] = None
    file: Optional[File] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Event':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        file_id = from_union([from_str, from_none], obj.get("file_id"))
        file = from_union([File.from_dict, from_none], obj.get("file"))
        return Event(type, file_id, file)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["file_id"] = from_union([from_str, from_none], self.file_id)
        result["file"] = from_union([lambda x: to_class(File, x), from_none], self.file)
        return result


@dataclass
class FileChangePayload:
    token: Optional[str] = None
    enterprise_id: Optional[str] = None
    team_id: Optional[str] = None
    api_app_id: Optional[str] = None
    type: Optional[str] = None
    authed_users: Optional[List[str]] = None
    authed_teams: Optional[List[str]] = None
    authorizations: Optional[List[Authorization]] = None
    is_ext_shared_channel: Optional[bool] = None
    event_id: Optional[str] = None
    event_time: Optional[int] = None
    event_context: Optional[str] = None
    event: Optional[Event] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FileChangePayload':
        assert isinstance(obj, dict)
        token = from_union([from_str, from_none], obj.get("token"))
        enterprise_id = from_union([from_str, from_none], obj.get("enterprise_id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        api_app_id = from_union([from_str, from_none], obj.get("api_app_id"))
        type = from_union([from_str, from_none], obj.get("type"))
        authed_users = from_union([lambda x: from_list(from_str, x), from_none], obj.get("authed_users"))
        authed_teams = from_union([lambda x: from_list(from_str, x), from_none], obj.get("authed_teams"))
        authorizations = from_union([lambda x: from_list(Authorization.from_dict, x), from_none], obj.get("authorizations"))
        is_ext_shared_channel = from_union([from_bool, from_none], obj.get("is_ext_shared_channel"))
        event_id = from_union([from_str, from_none], obj.get("event_id"))
        event_time = from_union([from_int, from_none], obj.get("event_time"))
        event_context = from_union([from_str, from_none], obj.get("event_context"))
        event = from_union([Event.from_dict, from_none], obj.get("event"))
        return FileChangePayload(token, enterprise_id, team_id, api_app_id, type, authed_users, authed_teams, authorizations, is_ext_shared_channel, event_id, event_time, event_context, event)

    def to_dict(self) -> dict:
        result: dict = {}
        result["token"] = from_union([from_str, from_none], self.token)
        result["enterprise_id"] = from_union([from_str, from_none], self.enterprise_id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["api_app_id"] = from_union([from_str, from_none], self.api_app_id)
        result["type"] = from_union([from_str, from_none], self.type)
        result["authed_users"] = from_union([lambda x: from_list(from_str, x), from_none], self.authed_users)
        result["authed_teams"] = from_union([lambda x: from_list(from_str, x), from_none], self.authed_teams)
        result["authorizations"] = from_union([lambda x: from_list(lambda x: to_class(Authorization, x), x), from_none], self.authorizations)
        result["is_ext_shared_channel"] = from_union([from_bool, from_none], self.is_ext_shared_channel)
        result["event_id"] = from_union([from_str, from_none], self.event_id)
        result["event_time"] = from_union([from_int, from_none], self.event_time)
        result["event_context"] = from_union([from_str, from_none], self.event_context)
        result["event"] = from_union([lambda x: to_class(Event, x), from_none], self.event)
        return result


def file_change_payload_from_dict(s: Any) -> FileChangePayload:
    return FileChangePayload.from_dict(s)


def file_change_payload_to_dict(x: FileChangePayload) -> Any:
    return to_class(FileChangePayload, x)
