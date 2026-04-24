# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_conversations_get_conversation_prefs_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class CanHuddle:
    enabled: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CanHuddle':
        assert isinstance(obj, dict)
        enabled = from_union([from_bool, from_none], obj.get("enabled"))
        return CanHuddle(enabled)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enabled"] = from_union([from_bool, from_none], self.enabled)
        return result


@dataclass
class CanThread:
    type: Optional[List[str]] = None
    user: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CanThread':
        assert isinstance(obj, dict)
        type = from_union([lambda x: from_list(from_str, x), from_none], obj.get("type"))
        user = from_union([lambda x: from_list(from_str, x), from_none], obj.get("user"))
        return CanThread(type, user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([lambda x: from_list(from_str, x), from_none], self.type)
        result["user"] = from_union([lambda x: from_list(from_str, x), from_none], self.user)
        return result


@dataclass
class MembershipLimit:
    value: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MembershipLimit':
        assert isinstance(obj, dict)
        value = from_union([from_int, from_none], obj.get("value"))
        return MembershipLimit(value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_union([from_int, from_none], self.value)
        return result


@dataclass
class Prefs:
    who_can_post: Optional[CanThread] = None
    can_thread: Optional[CanThread] = None
    membership_limit: Optional[MembershipLimit] = None
    can_huddle: Optional[CanHuddle] = None
    enable_at_channel: Optional[CanHuddle] = None
    enable_at_here: Optional[CanHuddle] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Prefs':
        assert isinstance(obj, dict)
        who_can_post = from_union([CanThread.from_dict, from_none], obj.get("who_can_post"))
        can_thread = from_union([CanThread.from_dict, from_none], obj.get("can_thread"))
        membership_limit = from_union([MembershipLimit.from_dict, from_none], obj.get("membership_limit"))
        can_huddle = from_union([CanHuddle.from_dict, from_none], obj.get("can_huddle"))
        enable_at_channel = from_union([CanHuddle.from_dict, from_none], obj.get("enable_at_channel"))
        enable_at_here = from_union([CanHuddle.from_dict, from_none], obj.get("enable_at_here"))
        return Prefs(who_can_post, can_thread, membership_limit, can_huddle, enable_at_channel, enable_at_here)

    def to_dict(self) -> dict:
        result: dict = {}
        result["who_can_post"] = from_union([lambda x: to_class(CanThread, x), from_none], self.who_can_post)
        result["can_thread"] = from_union([lambda x: to_class(CanThread, x), from_none], self.can_thread)
        result["membership_limit"] = from_union([lambda x: to_class(MembershipLimit, x), from_none], self.membership_limit)
        result["can_huddle"] = from_union([lambda x: to_class(CanHuddle, x), from_none], self.can_huddle)
        result["enable_at_channel"] = from_union([lambda x: to_class(CanHuddle, x), from_none], self.enable_at_channel)
        result["enable_at_here"] = from_union([lambda x: to_class(CanHuddle, x), from_none], self.enable_at_here)
        return result


@dataclass
class AdminConversationsGetConversationPrefsResponse:
    ok: Optional[bool] = None
    prefs: Optional[Prefs] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminConversationsGetConversationPrefsResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        prefs = from_union([Prefs.from_dict, from_none], obj.get("prefs"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return AdminConversationsGetConversationPrefsResponse(ok, prefs, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["prefs"] = from_union([lambda x: to_class(Prefs, x), from_none], self.prefs)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def admin_conversations_get_conversation_prefs_response_from_dict(s: Any) -> AdminConversationsGetConversationPrefsResponse:
    return AdminConversationsGetConversationPrefsResponse.from_dict(s)


def admin_conversations_get_conversation_prefs_response_to_dict(x: AdminConversationsGetConversationPrefsResponse) -> Any:
    return to_class(AdminConversationsGetConversationPrefsResponse, x)
