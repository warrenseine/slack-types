# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_conversations_search_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


@dataclass
class OwnershipDetail:
    count: Optional[int] = None
    team_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OwnershipDetail':
        assert isinstance(obj, dict)
        count = from_union([from_int, from_none], obj.get("count"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        return OwnershipDetail(count, team_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["count"] = from_union([from_int, from_none], self.count)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        return result


@dataclass
class ListsClass:
    total_count: Optional[int] = None
    ownership_details: Optional[List[OwnershipDetail]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ListsClass':
        assert isinstance(obj, dict)
        total_count = from_union([from_int, from_none], obj.get("total_count"))
        ownership_details = from_union([lambda x: from_list(OwnershipDetail.from_dict, x), from_none], obj.get("ownership_details"))
        return ListsClass(total_count, ownership_details)

    def to_dict(self) -> dict:
        result: dict = {}
        result["total_count"] = from_union([from_int, from_none], self.total_count)
        result["ownership_details"] = from_union([lambda x: from_list(lambda x: to_class(OwnershipDetail, x), x), from_none], self.ownership_details)
        return result


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
class ChannelEmailAddress:
    team_id: Optional[str] = None
    user_id: Optional[str] = None
    conversation_id: Optional[str] = None
    date_created: Optional[int] = None
    address: Optional[str] = None
    name: Optional[str] = None
    icons: Optional[Icons] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ChannelEmailAddress':
        assert isinstance(obj, dict)
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        conversation_id = from_union([from_str, from_none], obj.get("conversation_id"))
        date_created = from_union([from_int, from_none], obj.get("date_created"))
        address = from_union([from_str, from_none], obj.get("address"))
        name = from_union([from_str, from_none], obj.get("name"))
        icons = from_union([Icons.from_dict, from_none], obj.get("icons"))
        return ChannelEmailAddress(team_id, user_id, conversation_id, date_created, address, name, icons)

    def to_dict(self) -> dict:
        result: dict = {}
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["user_id"] = from_union([from_str, from_none], self.user_id)
        result["conversation_id"] = from_union([from_str, from_none], self.conversation_id)
        result["date_created"] = from_union([from_int, from_none], self.date_created)
        result["address"] = from_union([from_str, from_none], self.address)
        result["name"] = from_union([from_str, from_none], self.name)
        result["icons"] = from_union([lambda x: to_class(Icons, x), from_none], self.icons)
        return result


@dataclass
class PropertiesCanvas:
    file_id: Optional[str] = None
    is_empty: Optional[bool] = None
    quip_thread_id: Optional[str] = None
    is_migrated: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PropertiesCanvas':
        assert isinstance(obj, dict)
        file_id = from_union([from_str, from_none], obj.get("file_id"))
        is_empty = from_union([from_bool, from_none], obj.get("is_empty"))
        quip_thread_id = from_union([from_str, from_none], obj.get("quip_thread_id"))
        is_migrated = from_union([from_bool, from_none], obj.get("is_migrated"))
        return PropertiesCanvas(file_id, is_empty, quip_thread_id, is_migrated)

    def to_dict(self) -> dict:
        result: dict = {}
        result["file_id"] = from_union([from_str, from_none], self.file_id)
        result["is_empty"] = from_union([from_bool, from_none], self.is_empty)
        result["quip_thread_id"] = from_union([from_str, from_none], self.quip_thread_id)
        result["is_migrated"] = from_union([from_bool, from_none], self.is_migrated)
        return result


@dataclass
class MeetingNotes:
    file_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MeetingNotes':
        assert isinstance(obj, dict)
        file_id = from_union([from_str, from_none], obj.get("file_id"))
        return MeetingNotes(file_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["file_id"] = from_union([from_str, from_none], self.file_id)
        return result


@dataclass
class PostingRestrictedTo:
    type: Optional[List[str]] = None
    user: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PostingRestrictedTo':
        assert isinstance(obj, dict)
        type = from_union([lambda x: from_list(from_str, x), from_none], obj.get("type"))
        user = from_union([lambda x: from_list(from_str, x), from_none], obj.get("user"))
        return PostingRestrictedTo(type, user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([lambda x: from_list(from_str, x), from_none], self.type)
        result["user"] = from_union([lambda x: from_list(from_str, x), from_none], self.user)
        return result


@dataclass
class Data:
    file_id: Optional[str] = None
    shared_ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        file_id = from_union([from_str, from_none], obj.get("file_id"))
        shared_ts = from_union([from_str, from_none], obj.get("shared_ts"))
        return Data(file_id, shared_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["file_id"] = from_union([from_str, from_none], self.file_id)
        result["shared_ts"] = from_union([from_str, from_none], self.shared_ts)
        return result


@dataclass
class Tab:
    id: Optional[str] = None
    label: Optional[str] = None
    type: Optional[str] = None
    data: Optional[Data] = None
    is_disabled: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Tab':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        label = from_union([from_str, from_none], obj.get("label"))
        type = from_union([from_str, from_none], obj.get("type"))
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        is_disabled = from_union([from_bool, from_none], obj.get("is_disabled"))
        return Tab(id, label, type, data, is_disabled)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["label"] = from_union([from_str, from_none], self.label)
        result["type"] = from_union([from_str, from_none], self.type)
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        result["is_disabled"] = from_union([from_bool, from_none], self.is_disabled)
        return result


@dataclass
class ThreadsRestrictedTo:
    type: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ThreadsRestrictedTo':
        assert isinstance(obj, dict)
        type = from_union([lambda x: from_list(from_str, x), from_none], obj.get("type"))
        return ThreadsRestrictedTo(type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([lambda x: from_list(from_str, x), from_none], self.type)
        return result


@dataclass
class Properties:
    canvas: Optional[PropertiesCanvas] = None
    posting_restricted_to: Optional[PostingRestrictedTo] = None
    threads_restricted_to: Optional[ThreadsRestrictedTo] = None
    huddles_restricted: Optional[bool] = None
    at_here_restricted: Optional[bool] = None
    at_channel_restricted: Optional[bool] = None
    tabs: Optional[List[Tab]] = None
    tabz: Optional[List[Tab]] = None
    meeting_notes: Optional[MeetingNotes] = None
    is_dormant: Optional[bool] = None
    has_slack_connect_invite_created: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Properties':
        assert isinstance(obj, dict)
        canvas = from_union([PropertiesCanvas.from_dict, from_none], obj.get("canvas"))
        posting_restricted_to = from_union([PostingRestrictedTo.from_dict, from_none], obj.get("posting_restricted_to"))
        threads_restricted_to = from_union([ThreadsRestrictedTo.from_dict, from_none], obj.get("threads_restricted_to"))
        huddles_restricted = from_union([from_bool, from_none], obj.get("huddles_restricted"))
        at_here_restricted = from_union([from_bool, from_none], obj.get("at_here_restricted"))
        at_channel_restricted = from_union([from_bool, from_none], obj.get("at_channel_restricted"))
        tabs = from_union([lambda x: from_list(Tab.from_dict, x), from_none], obj.get("tabs"))
        tabz = from_union([lambda x: from_list(Tab.from_dict, x), from_none], obj.get("tabz"))
        meeting_notes = from_union([MeetingNotes.from_dict, from_none], obj.get("meeting_notes"))
        is_dormant = from_union([from_bool, from_none], obj.get("is_dormant"))
        has_slack_connect_invite_created = from_union([from_bool, from_none], obj.get("has_slack_connect_invite_created"))
        return Properties(canvas, posting_restricted_to, threads_restricted_to, huddles_restricted, at_here_restricted, at_channel_restricted, tabs, tabz, meeting_notes, is_dormant, has_slack_connect_invite_created)

    def to_dict(self) -> dict:
        result: dict = {}
        result["canvas"] = from_union([lambda x: to_class(PropertiesCanvas, x), from_none], self.canvas)
        result["posting_restricted_to"] = from_union([lambda x: to_class(PostingRestrictedTo, x), from_none], self.posting_restricted_to)
        result["threads_restricted_to"] = from_union([lambda x: to_class(ThreadsRestrictedTo, x), from_none], self.threads_restricted_to)
        result["huddles_restricted"] = from_union([from_bool, from_none], self.huddles_restricted)
        result["at_here_restricted"] = from_union([from_bool, from_none], self.at_here_restricted)
        result["at_channel_restricted"] = from_union([from_bool, from_none], self.at_channel_restricted)
        result["tabs"] = from_union([lambda x: from_list(lambda x: to_class(Tab, x), x), from_none], self.tabs)
        result["tabz"] = from_union([lambda x: from_list(lambda x: to_class(Tab, x), x), from_none], self.tabz)
        result["meeting_notes"] = from_union([lambda x: to_class(MeetingNotes, x), from_none], self.meeting_notes)
        result["is_dormant"] = from_union([from_bool, from_none], self.is_dormant)
        result["has_slack_connect_invite_created"] = from_union([from_bool, from_none], self.has_slack_connect_invite_created)
        return result


@dataclass
class Conversation:
    id: Optional[str] = None
    name: Optional[str] = None
    purpose: Optional[str] = None
    member_count: Optional[int] = None
    created: Optional[int] = None
    creator_id: Optional[str] = None
    is_private: Optional[bool] = None
    is_archived: Optional[bool] = None
    is_general: Optional[bool] = None
    last_activity_ts: Optional[int] = None
    is_ext_shared: Optional[bool] = None
    is_global_shared: Optional[bool] = None
    is_org_default: Optional[bool] = None
    is_org_mandatory: Optional[bool] = None
    is_org_shared: Optional[bool] = None
    is_frozen: Optional[bool] = None
    internal_team_ids_count: Optional[int] = None
    internal_team_ids_sample_team: Optional[str] = None
    pending_connected_team_ids: Optional[List[str]] = None
    is_pending_ext_shared: Optional[bool] = None
    connected_team_ids: Optional[List[str]] = None
    conversation_host_id: Optional[str] = None
    channel_email_addresses: Optional[List[ChannelEmailAddress]] = None
    connected_limited_team_ids: Optional[List[str]] = None
    external_user_count: Optional[int] = None
    internal_team_ids: Optional[List[str]] = None
    channel_manager_count: Optional[int] = None
    is_disconnect_in_progress: Optional[bool] = None
    canvas: Optional[ListsClass] = None
    context_team_id: Optional[str] = None
    lists: Optional[ListsClass] = None
    properties: Optional[Properties] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Conversation':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        purpose = from_union([from_str, from_none], obj.get("purpose"))
        member_count = from_union([from_int, from_none], obj.get("member_count"))
        created = from_union([from_int, from_none], obj.get("created"))
        creator_id = from_union([from_str, from_none], obj.get("creator_id"))
        is_private = from_union([from_bool, from_none], obj.get("is_private"))
        is_archived = from_union([from_bool, from_none], obj.get("is_archived"))
        is_general = from_union([from_bool, from_none], obj.get("is_general"))
        last_activity_ts = from_union([from_int, from_none], obj.get("last_activity_ts"))
        is_ext_shared = from_union([from_bool, from_none], obj.get("is_ext_shared"))
        is_global_shared = from_union([from_bool, from_none], obj.get("is_global_shared"))
        is_org_default = from_union([from_bool, from_none], obj.get("is_org_default"))
        is_org_mandatory = from_union([from_bool, from_none], obj.get("is_org_mandatory"))
        is_org_shared = from_union([from_bool, from_none], obj.get("is_org_shared"))
        is_frozen = from_union([from_bool, from_none], obj.get("is_frozen"))
        internal_team_ids_count = from_union([from_int, from_none], obj.get("internal_team_ids_count"))
        internal_team_ids_sample_team = from_union([from_str, from_none], obj.get("internal_team_ids_sample_team"))
        pending_connected_team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("pending_connected_team_ids"))
        is_pending_ext_shared = from_union([from_bool, from_none], obj.get("is_pending_ext_shared"))
        connected_team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("connected_team_ids"))
        conversation_host_id = from_union([from_str, from_none], obj.get("conversation_host_id"))
        channel_email_addresses = from_union([lambda x: from_list(ChannelEmailAddress.from_dict, x), from_none], obj.get("channel_email_addresses"))
        connected_limited_team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("connected_limited_team_ids"))
        external_user_count = from_union([from_int, from_none], obj.get("external_user_count"))
        internal_team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("internal_team_ids"))
        channel_manager_count = from_union([from_int, from_none], obj.get("channel_manager_count"))
        is_disconnect_in_progress = from_union([from_bool, from_none], obj.get("is_disconnect_in_progress"))
        canvas = from_union([ListsClass.from_dict, from_none], obj.get("canvas"))
        context_team_id = from_union([from_str, from_none], obj.get("context_team_id"))
        lists = from_union([ListsClass.from_dict, from_none], obj.get("lists"))
        properties = from_union([Properties.from_dict, from_none], obj.get("properties"))
        return Conversation(id, name, purpose, member_count, created, creator_id, is_private, is_archived, is_general, last_activity_ts, is_ext_shared, is_global_shared, is_org_default, is_org_mandatory, is_org_shared, is_frozen, internal_team_ids_count, internal_team_ids_sample_team, pending_connected_team_ids, is_pending_ext_shared, connected_team_ids, conversation_host_id, channel_email_addresses, connected_limited_team_ids, external_user_count, internal_team_ids, channel_manager_count, is_disconnect_in_progress, canvas, context_team_id, lists, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["purpose"] = from_union([from_str, from_none], self.purpose)
        result["member_count"] = from_union([from_int, from_none], self.member_count)
        result["created"] = from_union([from_int, from_none], self.created)
        result["creator_id"] = from_union([from_str, from_none], self.creator_id)
        result["is_private"] = from_union([from_bool, from_none], self.is_private)
        result["is_archived"] = from_union([from_bool, from_none], self.is_archived)
        result["is_general"] = from_union([from_bool, from_none], self.is_general)
        result["last_activity_ts"] = from_union([from_int, from_none], self.last_activity_ts)
        result["is_ext_shared"] = from_union([from_bool, from_none], self.is_ext_shared)
        result["is_global_shared"] = from_union([from_bool, from_none], self.is_global_shared)
        result["is_org_default"] = from_union([from_bool, from_none], self.is_org_default)
        result["is_org_mandatory"] = from_union([from_bool, from_none], self.is_org_mandatory)
        result["is_org_shared"] = from_union([from_bool, from_none], self.is_org_shared)
        result["is_frozen"] = from_union([from_bool, from_none], self.is_frozen)
        result["internal_team_ids_count"] = from_union([from_int, from_none], self.internal_team_ids_count)
        result["internal_team_ids_sample_team"] = from_union([from_str, from_none], self.internal_team_ids_sample_team)
        result["pending_connected_team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.pending_connected_team_ids)
        result["is_pending_ext_shared"] = from_union([from_bool, from_none], self.is_pending_ext_shared)
        result["connected_team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.connected_team_ids)
        result["conversation_host_id"] = from_union([from_str, from_none], self.conversation_host_id)
        result["channel_email_addresses"] = from_union([lambda x: from_list(lambda x: to_class(ChannelEmailAddress, x), x), from_none], self.channel_email_addresses)
        result["connected_limited_team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.connected_limited_team_ids)
        result["external_user_count"] = from_union([from_int, from_none], self.external_user_count)
        result["internal_team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.internal_team_ids)
        result["channel_manager_count"] = from_union([from_int, from_none], self.channel_manager_count)
        result["is_disconnect_in_progress"] = from_union([from_bool, from_none], self.is_disconnect_in_progress)
        result["canvas"] = from_union([lambda x: to_class(ListsClass, x), from_none], self.canvas)
        result["context_team_id"] = from_union([from_str, from_none], self.context_team_id)
        result["lists"] = from_union([lambda x: to_class(ListsClass, x), from_none], self.lists)
        result["properties"] = from_union([lambda x: to_class(Properties, x), from_none], self.properties)
        return result


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
class AdminConversationsSearchResponse:
    ok: Optional[bool] = None
    conversations: Optional[List[Conversation]] = None
    next_cursor: Optional[str] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    total_count: Optional[int] = None
    response_metadata: Optional[ResponseMetadata] = None
    warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminConversationsSearchResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        conversations = from_union([lambda x: from_list(Conversation.from_dict, x), from_none], obj.get("conversations"))
        next_cursor = from_union([from_str, from_none], obj.get("next_cursor"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        total_count = from_union([from_int, from_none], obj.get("total_count"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        return AdminConversationsSearchResponse(ok, conversations, next_cursor, error, needed, provided, total_count, response_metadata, warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["conversations"] = from_union([lambda x: from_list(lambda x: to_class(Conversation, x), x), from_none], self.conversations)
        result["next_cursor"] = from_union([from_str, from_none], self.next_cursor)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["total_count"] = from_union([from_int, from_none], self.total_count)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["warning"] = from_union([from_str, from_none], self.warning)
        return result


def admin_conversations_search_response_from_dict(s: Any) -> AdminConversationsSearchResponse:
    return AdminConversationsSearchResponse.from_dict(s)


def admin_conversations_search_response_to_dict(x: AdminConversationsSearchResponse) -> Any:
    return to_class(AdminConversationsSearchResponse, x)
