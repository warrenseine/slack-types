# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = conversations_info_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


@dataclass
class Tab:
    type: Optional[str] = None
    label: Optional[str] = None
    id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Tab':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        label = from_union([from_str, from_none], obj.get("label"))
        id = from_union([from_str, from_none], obj.get("id"))
        return Tab(type, label, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["label"] = from_union([from_str, from_none], self.label)
        result["id"] = from_union([from_str, from_none], self.id)
        return result


@dataclass
class Tabz:
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Tabz':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        return Tabz(type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        return result


@dataclass
class Properties:
    is_dormant: Optional[bool] = None
    tabs: Optional[List[Tab]] = None
    tabz: Optional[List[Tabz]] = None
    has_slack_connect_invite_created: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Properties':
        assert isinstance(obj, dict)
        is_dormant = from_union([from_bool, from_none], obj.get("is_dormant"))
        tabs = from_union([lambda x: from_list(Tab.from_dict, x), from_none], obj.get("tabs"))
        tabz = from_union([lambda x: from_list(Tabz.from_dict, x), from_none], obj.get("tabz"))
        has_slack_connect_invite_created = from_union([from_bool, from_none], obj.get("has_slack_connect_invite_created"))
        return Properties(is_dormant, tabs, tabz, has_slack_connect_invite_created)

    def to_dict(self) -> dict:
        result: dict = {}
        result["is_dormant"] = from_union([from_bool, from_none], self.is_dormant)
        result["tabs"] = from_union([lambda x: from_list(lambda x: to_class(Tab, x), x), from_none], self.tabs)
        result["tabz"] = from_union([lambda x: from_list(lambda x: to_class(Tabz, x), x), from_none], self.tabz)
        result["has_slack_connect_invite_created"] = from_union([from_bool, from_none], self.has_slack_connect_invite_created)
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
class Channel:
    id: Optional[str] = None
    name: Optional[str] = None
    is_channel: Optional[bool] = None
    is_group: Optional[bool] = None
    is_im: Optional[bool] = None
    created: Optional[int] = None
    is_archived: Optional[bool] = None
    is_general: Optional[bool] = None
    unlinked: Optional[int] = None
    name_normalized: Optional[str] = None
    is_shared: Optional[bool] = None
    creator: Optional[str] = None
    is_ext_shared: Optional[bool] = None
    is_org_shared: Optional[bool] = None
    shared_team_ids: Optional[List[str]] = None
    pending_shared: Optional[List[str]] = None
    pending_connected_team_ids: Optional[List[str]] = None
    is_pending_ext_shared: Optional[bool] = None
    is_member: Optional[bool] = None
    is_private: Optional[bool] = None
    is_mpim: Optional[bool] = None
    last_read: Optional[str] = None
    topic: Optional[Purpose] = None
    purpose: Optional[Purpose] = None
    previous_names: Optional[List[str]] = None
    locale: Optional[str] = None
    num_members: Optional[int] = None
    is_read_only: Optional[bool] = None
    is_thread_only: Optional[bool] = None
    is_non_threadable: Optional[bool] = None
    internal_team_ids: Optional[List[str]] = None
    connected_team_ids: Optional[List[str]] = None
    conversation_host_id: Optional[str] = None
    is_moved: Optional[int] = None
    is_global_shared: Optional[bool] = None
    is_org_default: Optional[bool] = None
    is_org_mandatory: Optional[bool] = None
    connected_limited_team_ids: Optional[List[str]] = None
    context_team_id: Optional[str] = None
    updated: Optional[int] = None
    properties: Optional[Properties] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Channel':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        is_channel = from_union([from_bool, from_none], obj.get("is_channel"))
        is_group = from_union([from_bool, from_none], obj.get("is_group"))
        is_im = from_union([from_bool, from_none], obj.get("is_im"))
        created = from_union([from_int, from_none], obj.get("created"))
        is_archived = from_union([from_bool, from_none], obj.get("is_archived"))
        is_general = from_union([from_bool, from_none], obj.get("is_general"))
        unlinked = from_union([from_int, from_none], obj.get("unlinked"))
        name_normalized = from_union([from_str, from_none], obj.get("name_normalized"))
        is_shared = from_union([from_bool, from_none], obj.get("is_shared"))
        creator = from_union([from_str, from_none], obj.get("creator"))
        is_ext_shared = from_union([from_bool, from_none], obj.get("is_ext_shared"))
        is_org_shared = from_union([from_bool, from_none], obj.get("is_org_shared"))
        shared_team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("shared_team_ids"))
        pending_shared = from_union([lambda x: from_list(from_str, x), from_none], obj.get("pending_shared"))
        pending_connected_team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("pending_connected_team_ids"))
        is_pending_ext_shared = from_union([from_bool, from_none], obj.get("is_pending_ext_shared"))
        is_member = from_union([from_bool, from_none], obj.get("is_member"))
        is_private = from_union([from_bool, from_none], obj.get("is_private"))
        is_mpim = from_union([from_bool, from_none], obj.get("is_mpim"))
        last_read = from_union([from_str, from_none], obj.get("last_read"))
        topic = from_union([Purpose.from_dict, from_none], obj.get("topic"))
        purpose = from_union([Purpose.from_dict, from_none], obj.get("purpose"))
        previous_names = from_union([lambda x: from_list(from_str, x), from_none], obj.get("previous_names"))
        locale = from_union([from_str, from_none], obj.get("locale"))
        num_members = from_union([from_int, from_none], obj.get("num_members"))
        is_read_only = from_union([from_bool, from_none], obj.get("is_read_only"))
        is_thread_only = from_union([from_bool, from_none], obj.get("is_thread_only"))
        is_non_threadable = from_union([from_bool, from_none], obj.get("is_non_threadable"))
        internal_team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("internal_team_ids"))
        connected_team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("connected_team_ids"))
        conversation_host_id = from_union([from_str, from_none], obj.get("conversation_host_id"))
        is_moved = from_union([from_int, from_none], obj.get("is_moved"))
        is_global_shared = from_union([from_bool, from_none], obj.get("is_global_shared"))
        is_org_default = from_union([from_bool, from_none], obj.get("is_org_default"))
        is_org_mandatory = from_union([from_bool, from_none], obj.get("is_org_mandatory"))
        connected_limited_team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("connected_limited_team_ids"))
        context_team_id = from_union([from_str, from_none], obj.get("context_team_id"))
        updated = from_union([from_int, from_none], obj.get("updated"))
        properties = from_union([Properties.from_dict, from_none], obj.get("properties"))
        return Channel(id, name, is_channel, is_group, is_im, created, is_archived, is_general, unlinked, name_normalized, is_shared, creator, is_ext_shared, is_org_shared, shared_team_ids, pending_shared, pending_connected_team_ids, is_pending_ext_shared, is_member, is_private, is_mpim, last_read, topic, purpose, previous_names, locale, num_members, is_read_only, is_thread_only, is_non_threadable, internal_team_ids, connected_team_ids, conversation_host_id, is_moved, is_global_shared, is_org_default, is_org_mandatory, connected_limited_team_ids, context_team_id, updated, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["is_channel"] = from_union([from_bool, from_none], self.is_channel)
        result["is_group"] = from_union([from_bool, from_none], self.is_group)
        result["is_im"] = from_union([from_bool, from_none], self.is_im)
        result["created"] = from_union([from_int, from_none], self.created)
        result["is_archived"] = from_union([from_bool, from_none], self.is_archived)
        result["is_general"] = from_union([from_bool, from_none], self.is_general)
        result["unlinked"] = from_union([from_int, from_none], self.unlinked)
        result["name_normalized"] = from_union([from_str, from_none], self.name_normalized)
        result["is_shared"] = from_union([from_bool, from_none], self.is_shared)
        result["creator"] = from_union([from_str, from_none], self.creator)
        result["is_ext_shared"] = from_union([from_bool, from_none], self.is_ext_shared)
        result["is_org_shared"] = from_union([from_bool, from_none], self.is_org_shared)
        result["shared_team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.shared_team_ids)
        result["pending_shared"] = from_union([lambda x: from_list(from_str, x), from_none], self.pending_shared)
        result["pending_connected_team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.pending_connected_team_ids)
        result["is_pending_ext_shared"] = from_union([from_bool, from_none], self.is_pending_ext_shared)
        result["is_member"] = from_union([from_bool, from_none], self.is_member)
        result["is_private"] = from_union([from_bool, from_none], self.is_private)
        result["is_mpim"] = from_union([from_bool, from_none], self.is_mpim)
        result["last_read"] = from_union([from_str, from_none], self.last_read)
        result["topic"] = from_union([lambda x: to_class(Purpose, x), from_none], self.topic)
        result["purpose"] = from_union([lambda x: to_class(Purpose, x), from_none], self.purpose)
        result["previous_names"] = from_union([lambda x: from_list(from_str, x), from_none], self.previous_names)
        result["locale"] = from_union([from_str, from_none], self.locale)
        result["num_members"] = from_union([from_int, from_none], self.num_members)
        result["is_read_only"] = from_union([from_bool, from_none], self.is_read_only)
        result["is_thread_only"] = from_union([from_bool, from_none], self.is_thread_only)
        result["is_non_threadable"] = from_union([from_bool, from_none], self.is_non_threadable)
        result["internal_team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.internal_team_ids)
        result["connected_team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.connected_team_ids)
        result["conversation_host_id"] = from_union([from_str, from_none], self.conversation_host_id)
        result["is_moved"] = from_union([from_int, from_none], self.is_moved)
        result["is_global_shared"] = from_union([from_bool, from_none], self.is_global_shared)
        result["is_org_default"] = from_union([from_bool, from_none], self.is_org_default)
        result["is_org_mandatory"] = from_union([from_bool, from_none], self.is_org_mandatory)
        result["connected_limited_team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.connected_limited_team_ids)
        result["context_team_id"] = from_union([from_str, from_none], self.context_team_id)
        result["updated"] = from_union([from_int, from_none], self.updated)
        result["properties"] = from_union([lambda x: to_class(Properties, x), from_none], self.properties)
        return result


@dataclass
class ConversationsInfoResponse:
    ok: Optional[bool] = None
    channel: Optional[Channel] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ConversationsInfoResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        channel = from_union([Channel.from_dict, from_none], obj.get("channel"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return ConversationsInfoResponse(ok, channel, error, needed, provided, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["channel"] = from_union([lambda x: to_class(Channel, x), from_none], self.channel)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def conversations_info_response_from_dict(s: Any) -> ConversationsInfoResponse:
    return ConversationsInfoResponse.from_dict(s)


def conversations_info_response_to_dict(x: ConversationsInfoResponse) -> Any:
    return to_class(ConversationsInfoResponse, x)
